#!/usr/bin/env python3
"""Structural regression checks after C preprocessing; not a firmware build."""
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory() as directory:
    stub = Path(directory)
    for header in ('behaviors.dtsi', 'dt-bindings/zmk/keys.h', 'dt-bindings/zmk/bt.h',
                   'dt-bindings/zmk/outputs.h', 'behaviors/rgbled_widget.dtsi',
                   'zephyr/dt-bindings/input/input-event-codes.h',
                   'dt-bindings/zmk/pointing.h', 'input/processors.dtsi'):
        path = stub / header
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text('#define ZMK_MACRO(name, ...)\n' if header == 'behaviors.dtsi' else '')
    # Real keymap includes, real 34-key transform, real custom behaviors/combos.
    # Only external SDK headers are stubbed; keycodes remain symbolic for checks.
    text = subprocess.check_output(['clang', '-E', '-P', '-x', 'assembler-with-cpp',
        '-I', str(stub), '-I', str(ROOT / 'config'), str(ROOT / 'config/sweep.keymap')], text=True)

layers = re.findall(r'display-name = "((?:MAC|WIN) \w+)";\s*bindings = <(.*?)>;', text, re.S)
assert [n for n, _ in layers] == [p+' '+n for p in ('MAC', 'WIN') for n in ('DEF','NUM','SYM','NAV','SYS')]
values = {}
for name, contents in layers:
    bindings = re.findall(r'&\w+[^&]*', contents)
    bindings = [' '.join(b.split()) for b in bindings]
    assert len(bindings) == 34, (name, len(bindings))
    values[name] = bindings
assert values['MAC SYS'][1] == '&to 5'
assert values['WIN SYS'][1] == '&to 0'
assert values['MAC DEF'][28] == '&mt LC(LA(SPC)) DOT'
assert values['WIN DEF'][28] == '&mt RALT DOT'
assert values['MAC DEF'][30:] == ['&nav_ht 0 SPC', '&sys_ht 0 TAB', '&lt 2 RET', '&num_ht 0 BSPC']
assert values['WIN DEF'][30:] == ['&win_nav_ht 0 SPC', '&win_sys_ht 0 TAB', '&lt 7 RET', '&win_num_ht 0 BSPC']
assert values['MAC NAV'][22:24] == ['&kp LG(C)', '&kp LG(V)']
assert values['WIN NAV'][22:24] == ['&kp LC(C)', '&kp LC(V)']
assert values['MAC NAV'][3] == '&sw_g'
assert values['WIN NAV'][3] == '&sw_a'
# Critical: after Shift+layer (&to) clears WIN_DEF, fallback must stay Windows.
for name in ('WIN NUM', 'WIN SYM', 'WIN NAV', 'WIN SYS'):
    assert '&trans' not in values[name], name
assert values['WIN SYS'][31] == '&win_sys_ht 0 TAB'
assert values['WIN NUM'][33] == '&win_num_ht 0 BSPC'
assert re.search(r'combo_win_sel_all\s*\{[^}]*bindings = <&kp LC\(A\)>;[^}]*layers = <8>;', text)
assert re.search(r'combo_win_def\s*\{[^}]*bindings = <&to 5>;[^}]*layers = <6 8 9>;', text)
assert len(re.findall(r'combo_\w+\s*\{', text)) == 60
labels = re.findall(r'\b(\w+):\s*[-\w]+\s*\{', text)
assert len(labels) == len(set(labels)), 'Duplicate behavior labels'
for label in ('win_num_ht','win_nav_ht','win_sys_ht','win_morph_num0','win_morph_nav0','win_morph_sys0'):
    assert label in labels, label
assert 'LAYER_FROM38' not in text
print('PASS: 10 x 34 bindings, both OS switches, thumb routing, macOS/Windows shortcuts,')
print('      60 scoped combos, Windows latch fallback, and unique custom behavior labels.')
print('External SDK keycode validation, linking and hardware operation require a real ZMK build.')
