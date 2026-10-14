# Experimenteller automatischer Registry-Fix

**Noch nicht in einer laufenden Proton-Installation getestet.** Für die getestete Methode siehe [manuelle Anleitung](DE_VKB-Proton-Elite.md).

## Vorbereitung

Steam Input für Elite deaktivieren und Elite samt Launcher schließen. Benötigt `python3` und `protontricks`.

## Fix anwenden

```sh
python3 fix_vkb.py
```

Das Skript findet die VKBs (`231D:0200` rechts, `231D:0201` links), sichert `WINEBUS` und setzt bei beiden Geräteinstanzen:

| Feld | Wert |
|---|---|
| `Service` | `winehid` |
| `DeviceDesc` | `Wine HID compatible device` |
| `CompatibleIDs` | `WINEBUS\WINE_COMP_HID` |

Andere Registry-Werte, `WINEXINPUT` und WineBus-Einstellungen bleiben unverändert. Private Backups liegen unter `~/.local/state/vkb-elite-proton-fix/backups/` und gehören **nicht** ins Repository.

## Prüfen

```sh
protontricks -c 'wine control joy.cpl' 359320
```

Unter **Joysticks** sollten beide VKBs als **DirectInput** erscheinen. Anschließend Elite neu starten.

**Wiederherstellen:** Mit `protontricks 359320 regedit` das zuvor angelegte `VKB-*.reg` über **Registry → Import Registry File** importieren.