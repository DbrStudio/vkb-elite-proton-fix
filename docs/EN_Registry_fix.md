# Experimental Automatic Registry Fix

**Not yet tested on a live Proton installation.** For the tested method, use [the manual guide](EN_VKB-Proton-Elite.md).

## Requirements

Disable **Steam Input** for Elite Dangerous and close the game and launcher. Install Python 3 and Protontricks.

## Run

```sh
python3 fix_vkb.py
```

The script locates the right (`231D:0200`) and left (`231D:0201`) VKB Gladiator EVO device instances under `WINEBUS`, backs up the registry, and changes:

| Registry value | New value |
|---|---|
| `Service` | `winehid` |
| `DeviceDesc` | `Wine HID compatible device` |
| `CompatibleIDs` | `WINEBUS\WINE_COMP_HID` |

Other values and the `WINEXINPUT` branch are left untouched.

Backups are saved to `~/.local/state/vkb-elite-proton-fix/backups/`. **Do not commit these files.**

## Check

```sh
protontricks -c 'wine control joy.cpl' 359320
```

Both VKBs should appear under **DirectInput**. Restart Elite Dangerous before testing in-game.

To restore a backup, run `protontricks 359320 regedit` and choose **Registry → Import Registry File** to import the relevant `VKB-*.reg` file.
