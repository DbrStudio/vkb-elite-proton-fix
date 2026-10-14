# VKB Gladiator EVO DirectInput Fix for Elite Dangerous

**Language:** English | [Deutsch](README.de.md)

Fixes VKB Gladiator EVO joysticks being detected as Xbox/XInput controllers instead of DirectInput devices in **Elite Dangerous on Linux/Proton**.

Tested manually with two VKB Gladiator EVO Premium sticks (right: `231D:0200`, left: `231D:0201`). Steam app ID: `359320`.

## Instructions

| Method | Deutsch | English | Status |
|---|---|---|---|
| **Manual registry fix** | [DE_VKB-Proton-Elite.md](DE_VKB-Proton-Elite.md) | [EN_VKB-Proton-Elite.md](EN_VKB-Proton-Elite.md) | **Tested and working** |
| **Automatic fix (`fix_vkb.py`)** | [DE_Registry_fix.md](DE_Registry_fix.md) | [EN_Registry_fix.md](EN_Registry_fix.md) | **Experimental, not yet tested on a live Proton installation** |

The automatic script is intended to find both sticks, back up the Wine registry entries, and apply the same changes as the manual fix. **Use the manual instructions if you want the tested method.**

[`VKB.public.reg.template`](VKB.public.reg.template) is only an example. It contains placeholder device-instance IDs and **cannot be imported unchanged**. Keep personal registry backups out of the repository.

## Button names

The manual guide uses button mapping files from [EDCD/EliteCustomButtonNames](https://github.com/EDCD/EliteCustomButtonNames). Thanks to that project for providing named VKB buttons in Elite Dangerous.

## Planned

My personal **dual-VKB Elite Dangerous `.binds` configuration** will be added once it is finished.
