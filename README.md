# zmk-config

This is my personal [zmk-config](https://zmk.dev/) for my Split keyboards. <br />

## macOS Sweep build

Hold the base-layer dot key to send Control+Option+Space (next input source on
macOS); tap it for a dot. All key positions and layers are unchanged.
See [the complete 34-key macOS mapping](docs/macos-keymap.md) for all five layers
and combos.

The Sweep keymap is configured for macOS. The physical 34-key layout and all
layers stay the same; navigation shortcuts use Command/Option equivalents for
copy, paste, undo, app and tab switching, word deletion, line/document
navigation, screen lock, and input-source switching. The profile is selected by
`#define MAC_OS` at the top of `config/sweep.keymap`.

To build with GitHub Actions, push this repository to a GitHub fork, enable
Actions if GitHub disabled them for the fork, and run the workflow from the
Actions tab. Download the `sweep_peripheral_left` and `sweep_peripheral_right`
artifacts from the completed run.

### Flashing a Bluetooth Sweep

1. Keep the two halves separated while flashing.
2. Flash the `settings_reset` Nice!Nano UF2 to each half once. Double-tap the
   controller's reset button to expose its USB drive, copy the UF2 file, and
   wait for the automatic reboot.
3. Flash the `sweep_peripheral_left` UF2 to the left half and the
   `sweep_peripheral_right` UF2 to the right half using the same double-reset
   and copy process.
4. After both halves reboot, pair the keyboard in macOS under **System
   Settings → Bluetooth**. The left half is the central half and should be the
   half connected to USB during initial pairing.

Never flash a Totem/XIAO artifact to a Sweep/Nice!Nano controller.

### Flashing a Sweep dongle

The dongle target is enabled in `build.yaml` as `sweep_dongle`. After pushing
that change, download the additional `sweep_dongle` UF2 from the GitHub Actions
artifact. If the dongle was paired to the previous firmware, first flash the
Nice!Nano `settings_reset` UF2 to the dongle, then flash the new
`sweep_dongle` UF2. Keep the keyboard halves powered off while resetting and
flashing the dongle. Then flash the keyboard halves, power everything on, and
pair the dongle as the host's USB keyboard.

When using the dongle, the dongle is the only central. The left and right Sweep
targets are built as peripherals with `CONFIG_ZMK_SPLIT_ROLE_CENTRAL=n` so they
can connect to the dongle instead of trying to act as a host central.

The dongle build also includes ZMK Studio's USB RPC endpoint and disables Studio
locking. Connect the dongle by USB and open [zmk.studio](https://zmk.studio/) in
Chrome or Edge to view and edit the graphical keymap. In dongle mode, use the
dongle for Studio; the two keyboard halves are peripherals and do not provide
the host's USB Studio endpoint.

The dongle build also restores the optional `zmk-dongle-display` screen for a
128x64 I2C OLED: it shows layer/output/battery/modifier data, WPM, and the
animated Bongo Cat widget. The display is wired through the Nice!Nano
`pro_micro_i2c` bus at address `0x3c` and uses the SH1106 128x64 controller
settings from the original configuration. The NUM-layer mouse movement speed is
set to twice the previous default and reaches acceleration sooner.

Sweep Bluethooth(Nice!Nano) or Dongle(Nice!Naon), Studio available. <br />
Totem Bluethooth(Xiao_ble) or Dongle(Xiao_ble), Studio available.<br /><br />

The thumb, number, symbol, and function layers follow the Miryoku layout almost exactly.<br />
It provides the RShift function on the R4 row of the base layer for language switching.
<br />

Uses Urob's Timeless-Home-row-mods.<br />
The navigation layer and number layer perform the following actions when used with the Shift key.
Tap: &kp | hold: &mo layer | shift + hold: &to layer. Pressing the Home key(F+J) in combination while in the &to layer state returns you to the base layer. This feature is useful when pressing navigation keys or number pad keys with one hand. This is taken from Urob's SMART_NUM Behaviors.<br />

There are symbol layers, but frequently used symbols are provided as combos. Function keys are provided on the opposite side of the symbol layers to reduce the layer key, and modifier keys are provided for shortcuts.<br />

The number layer provides the four basic arithmetic operations as combo keys, just like a full-size keyboard.<br />

The navigation layer replaces the action of tapping the arrow keys multiple times with a hold. On the opposite side of the navigation keys are frequently used shortcuts like Copy, Task Switcher, etc.<br />

This keymap provides modifier key combination shortcuts. (e.g., SHIFT+ →, CTRL+1, ALT+F4, CTRL+ALT+DEL)<br />

## Modules

Additional features are provided by the following [modules](https://zmk.dev/docs/features/modules): <br />

- [**zmk-rgbled-widgets**](https://github.com/caksoylar/zmk-rgbled-widget) to show the connection and battery status with the built-in LEDs of the Xiao BLE controller.
- [**zmk-smart-toggle**](https://github.com/caksoylar/zmk-smart-toggle) custom behavior module that implements a "smart toggle" key. Used in Swapper.

## Boards and Keymaps

<details open>
  <summary><a href="https://github.com/davidphilipbarr/Sweep">Sweep</a> (34 keys)</summary>
  <img src="keymap-drawer/sweep.svg" >

  _(keymap image created with [caksoylar/keymap-drawer](https://github.com/caksoylar/keymap-drawer))_
</details>

<details>
  <summary><a href="https://github.com/GEIGEIGEIST/zmk-config-totem">Totem</a> (38 keys)</summary>
  <img src="keymap-drawer/totem.svg" >

  _(keymap image created with [caksoylar/keymap-drawer](https://github.com/caksoylar/keymap-drawer))_
</details>

<br />

## Inspirations

- [caksoylar/zmk-config](https://github.com/caksoylar/zmk-config)
- [eigatech/zmk-config](https://github.com/eigatech/zmk-config)
- [manna-harbour/miryoku_zmk](https://github.com/manna-harbour/miryoku_zmk)
- [minusfive/zmk-config](https://github.com/minusfive/zmk-config)
- [urob/zmk-config](https://github.com/urob/zmk-config)
