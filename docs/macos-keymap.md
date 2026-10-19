# Sweep 34키 · macOS 전체 매핑

실제 `config/includes/3x5.dtsi`와 `keypos_34keys.h`의 LAYER_FROM38 변환을 기준으로 생성했습니다. 각 레이어는 10 + 10 + 10 + 4 = 34키입니다.

`탭 / 홀드` 표기, `▽` = 아래 레이어 키 사용, `—` = 입력 없음. 왼손과 오른손은 각각 화면 왼쪽→오른쪽 순서입니다.

**언어 전환:** 기본 레이어의 `.`를 150ms 이상 누르면 `Ctrl+Option+Space`. 짧게 누르면 `.`. 길게 누른 채 유지하면 Space 반복 입력이 생길 수 있으므로 원하는 만큼 전환한 뒤 놓으세요.

macOS 시스템 설정 → 키보드 → 키보드 단축키 → 입력 소스에서 “입력 메뉴에서 다음 소스 선택”이 `Ctrl+Option+Space`로 설정되어 있어야 합니다.

## DEF

| 행 | 왼손: 바깥 → 안쪽 | 오른손: 안쪽 → 바깥 |
|---|---|---|
| 상단 | Q · W · E · R · T | Y · U · I · O · P |
| 중단 | A / Cmd · S / Opt · D / Shift · F / Ctrl · G | H · J / Ctrl · K / Shift · L / Opt · ' / Cmd |
| 하단 | Z · X · C · V · B | N · M · , / Shift · . / Lang ⌃⌥Space · / |
| 엄지 | Space / NAV · Tab / SYS | Enter / SYM · Backspace / NUM |

<details><summary>실제 ZMK 바인딩 34개</summary>

```text
&kp Q  &kp W  &kp E  &kp R  &kp T     |     &kp Y  &kp U  &kp I  &kp O  &kp P
&aml M_PNK A  &aml M_RNG S  &asl M_MDL D  &aml M_IDX F  &kp G     |     &kp H  &amr M_IDX J  &asr M_MDL K  &amr M_RNG L  &amr M_PNK SQT
&kp Z  &kp X  &kp C  &kp V  &kp B     |     &kp N  &kp M  &mt RSHFT COMMA  &mt LANG DOT  &kp SLASH
NAV_SPC  SYS_TAB     |     &lt SYM RET  NUM_BSPC
```

</details>

## NUM

| 행 | 왼손: 바깥 → 안쪽 | 오른손: 안쪽 → 바깥 |
|---|---|---|
| 상단 | [ · 7 · 8 · 9 · ] | — · Left click · Mouse ↑ · Right click · Scroll ↑ |
| 중단 | ; · 4 · 5 · 6 · = | — · Mouse ← · Mouse ↓ · Mouse → · Scroll ↓ |
| 하단 | ` · 1 · 2 · 3 · \ | — · Ctrl · Shift · Opt · Cmd |
| 엄지 | 0 · - | ▽ · ▽ |

<details><summary>실제 ZMK 바인딩 34개</summary>

```text
&kp LBKT  &kp N7  &kp N8  &kp N9  &kp RBKT     |     &none  &mkp LCLK  &mmv MOVE_UP  &mkp RCLK  &msc SCRL_UP
&kp SEMI  &kp N4  &kp N5  &kp N6  &kp EQUAL     |     &none  &mmv MOVE_LEFT  &mmv MOVE_DOWN  &mmv MOVE_RIGHT  &msc SCRL_DOWN
&kp GRAVE  &kp N1  &kp N2  &kp N3  &kp BSLH     |     &none  &kp M_IDX  &kp M_MDL  &kp M_RNG  &kp M_PNK
&kp N0  &kp MINUS     |     &trans  &trans
```

</details>

## SYM

| 행 | 왼손: 바깥 → 안쪽 | 오른손: 안쪽 → 바깥 |
|---|---|---|
| 상단 | { · & · * · ( · } | PrintScreen · F7 · F8 · F9 · F12 |
| 중단 | : / Cmd · $ / Opt · % / Shift · ^ / Ctrl · + | ScrollLock · F4 · F5 · F6 · F11 |
| 하단 | ~ · ! · @ · # · &#124; | Pause · F1 · F2 · F3 · F10 |
| 엄지 | ) · _ | ▽ · ▽ |

<details><summary>실제 ZMK 바인딩 34개</summary>

```text
&kp LBRC  &kp AMPS  &kp ASTRK  &kp LPAR  &kp RBRC     |     &kp PSCRN  &kp F7  &kp F8  &kp F9  &kp F12
&mt M_PNK COLON  &mt M_RNG DLLR  &mt M_MDL PRCNT  &mt M_IDX CARET  &kp PLUS     |     &kp SLCK  &kp F4  &kp F5  &kp F6  &kp F11
&kp TILDE  &kp EXCL  &kp AT  &kp HASH  &kp PIPE     |     &kp PAUSE_BREAK  &kp F1  &kp F2  &kp F3  &kp F10
&kp RPAR  &kp UNDER     |     &trans  &trans
```

</details>

## NAV

| 행 | 왼손: 바깥 → 안쪽 | 오른손: 안쪽 → 바깥 |
|---|---|---|
| 상단 | Shift+Tab · Ctrl+Tab (swapper) · Shift+Tab · Cmd+Tab (swapper) · Close ⌘W / Quit ⌘Q | Insert · Backspace / Opt+Backspace · ↑ / ⌘↑ · Ctrl+D / Opt+Delete · PageUp |
| 중단 | Cmd · Opt · Shift · Ctrl · — | CapsLock · ← / ⌘← · ↓ / ⌘↓ · → / ⌘→ · PageDown |
| 하단 | Undo ⌘Z · Cut ⌘X · Copy ⌘C · Paste ⌘V · Redo ⌘⇧Z | Delete · Previous track · Next track · Volume − · Volume + |
| 엄지 | ▽ · ▽ | Enter · Backspace |

<details><summary>실제 ZMK 바인딩 34개</summary>

```text
&kp LS(TAB)  &T_RHT  &kp LS(TAB)  &W_RHT  &ht W_CLS T_CLS     |     &kp INS  &ht WD_BSPC CH_BSPC  &ht ST_DOC UP  &ht WD_DEL CH_DEL  &kp PG_UP
&kp M_PNK  &kp M_RNG  &kp M_MDL  &kp M_IDX  &none     |     &kp CAPS  &ht LN_STR LEFT  &ht EN_DOC DOWN  &ht LN_END RIGHT  &kp PG_DN
&kp C_UND  &kp C_CUT  &kp C_CPY  &kp C_PST  &kp C_RDO     |     &kp DEL  &kp C_PREV  &kp C_NEXT  &kp C_VOL_DN  &kp C_VOL_UP
&trans  &trans     |     &kp RET  &kp BSPC
```

</details>

## SYS

| 행 | 왼손: 바깥 → 안쪽 | 오른손: 안쪽 → 바깥 |
|---|---|---|
| 상단 | Reset / Bootloader · Windows 전환 · — · Lock ⌃⌘Q · Soft off | Soft off · KP7 · KP8 · KP9 · Reset / Bootloader |
| 중단 | Cmd · Opt · Shift · Ctrl · — | — · KP4 · KP5 · KP6 · — |
| 하단 | BT clear ALL · BT profile 0 · BT profile 1 · BT profile 2 · BT clear selected | — · KP1 · KP2 · KP3 · — |
| 엄지 | ▽ · ▽ | — · KP0 |

<details><summary>실제 ZMK 바인딩 34개</summary>

```text
&rst_boot 0 0  &to WIN_DEF  &none  &kp LOCK  &soft_off     |     &soft_off  &kp KP_N7  &kp KP_N8  &kp KP_N9  &rst_boot 0 0
&kp M_PNK  &kp M_RNG  &kp M_MDL  &kp M_IDX  &none     |     &none  &kp KP_N4  &kp KP_N5  &kp KP_N6  &none
&bt BT_CLR_ALL  &bt BT_SEL 0  &bt BT_SEL 1  &bt BT_SEL 2  &bt BT_CLR     |     &none  &kp KP_N1  &kp KP_N2  &kp KP_N3  &none
&trans  &trans     |     &none  &kp KP_N0
```

</details>

## 콤보 전체 (기존 그대로)

위치 이름은 기본 레이어의 물리 키를 기준으로 표기합니다.

| 이름 | 물리 키 | 레이어 | 동작 |
|---|---|---|---|
| esc | Q + W | DEF | `&kp ESC` |
| lpar | D + F | DEF | `&kp LPAR` |
| rpar | J + K | DEF | `&kp RPAR` |
| lbkt | S + D | DEF | `&kp LBKT` |
| rbkt | K + L | DEF | `&kp RBKT` |
| sel_all | S + D | NAV | `&kp C_ALL` |
| key_re | D + F | NAV | `&key_repeat` |
| semi | M + , | DEF | `&kp SEMI` |
| colon | , + . | DEF | `&kp COLON` |
| mute | . + / | NAV | `&kp C_MUTE` |
| plpu | M + , | NAV | `&kp C_PP` |
| capswd | F + J | DEF | `&caps_word` |
| stdio | G + H | SYS | `&studio_unlock` |
| def | F + J | NUM NAV SYS | `&to DEF` |
| plus | D + F | NUM | `&kp PLUS` |
| minus | E + R | NUM | `&kp MINUS` |
| star | E + F | NUM | `&kp STAR` |
| slash | D + R | NUM | `&kp SLASH` |
| comma | C + V | NUM | `&kp COMMA` |
| dot | X + C | NUM | `&kp DOT` |
| ret | S + D | NUM | `&kp RET` |
| tab | W + E | NUM | `&kp TAB` |
| plus_n | J + K | SYS | `&kp KP_PLUS` |
| minus_n | U + I | SYS | `&kp KP_MINUS` |
| star_n | U + K | SYS | `&kp KP_MULTIPLY` |
| slash_n | J + I | SYS | `&kp KP_DIVIDE` |
| comma_n | M + , | SYS | `&kp COMMA` |
| dot_n | , + . | SYS | `&kp KP_DOT` |
| ret_n | K + L | SYS | `&kp RET` |
| tab_n | I + O | SYS | `&kp TAB` |
