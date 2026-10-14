# Manual VKB Gladiator EVO DirectInput Fix (Linux/Proton)

Makes two VKB Gladiator EVO sticks appear as **DirectInput joysticks** instead of Xbox/XInput controllers in Elite Dangerous (Steam app ID `359320`). **Tested successfully.**

## 1. Disable Steam Input

**Steam → Elite Dangerous → Properties → Controller → Disable Steam Input**

## 2. Edit the Wine registry

```sh
protontricks 359320 regedit
```

Open:

```text
HKEY_LOCAL_MACHINE\System\CurrentControlSet\Enum\WINEBUS
```

Locate the **device instance** under each key:

- `VID_231D&PID_0200` → right VKB
- `VID_231D&PID_0201` → left VKB

Set the following values on **both** instances:

| Value | Type | Set to |
|---|---|---|
| `Service` | `REG_SZ` | `winehid` |
| `DeviceDesc` | `REG_SZ` | `Wine HID compatible device` |
| `CompatibleIDs` | `REG_MULTI_SZ` | `WINEBUS\WINE_COMP_HID` (remove `WINEBUS\WINE_COMP_XINPUT`) |

Some users report needing to delete entries under `WINEXINPUT`. **That was not necessary in my case.** Leave all other values unchanged.

## 3. Verify

```sh
protontricks -c 'wine control joy.cpl' 359320
```

Under **Joysticks**, check:

- **Enable SDL** enabled
- **Disable hidraw** unchecked
- Both VKBs listed as **Connected (DirectInput devices)**

## 4. Show VKB button names in Elite

Button naming files are provided by [EDCD/EliteCustomButtonNames](https://github.com/EDCD/EliteCustomButtonNames).

Copy these files into Elite's `Bindings/DeviceButtonMaps/` folder:

```text
231D0200.buttonMap  → right VKB
231D0201.buttonMap  → left VKB
```

## 5. Save a working registry backup

In `regedit`, select `Enum\WINEBUS` → **Registry → Export Registry File** → save as `VKB.reg`.

To restore, use **Registry → Import Registry File**. Restart Elite/Proton and check detection again. **Keep this backup private.**
