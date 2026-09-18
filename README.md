# zmk-config

This is my personal [zmk-config](https://zmk.dev/) for my Split keyboards. <br />
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
