# VKB Gladiator EVO unter Elite Dangerous (Linux/Proton)

Zwei VKB Gladiator EVOs als **DirectInput-Joysticks** statt Xbox-/XInput-Controller in Elite Dangerous erkennen lassen (Steam-App-ID `359320`). **Erfolgreich getestet.**

## 1. Steam Input deaktivieren

Verhindert zusätzliche Controller-Emulation durch Steam.

**Steam → Elite Dangerous → Eigenschaften → Controller → Steam Input deaktivieren**

## 2. Wine-Registry anpassen

Ändert die Erkennung beider VKBs von XInput auf HID/DirectInput.

```sh
protontricks 359320 regedit
```

Pfad:

```text
HKEY_LOCAL_MACHINE\System\CurrentControlSet\Enum\WINEBUS
```

In den **Geräteinstanzen** unter diesen beiden Schlüsseln die Werte setzen:

- `VID_231D&PID_0200` → rechter VKB
- `VID_231D&PID_0201` → linker VKB

| Feld | Typ | Wert |
|---|---|---|
| `Service` | `REG_SZ` | `winehid` |
| `DeviceDesc` | `REG_SZ` | `Wine HID compatible device` |
| `CompatibleIDs` | `REG_MULTI_SZ` | `WINEBUS\WINE_COMP_HID` (ohne `WINEBUS\WINE_COMP_XINPUT`) |

Einige Nutzer berichten, dass die Einträge unter `WINEXINPUT` gelöscht werden müssen. Bei mir war das nicht notwendig. Andere Felder unverändert lassen.

## 3. Erkennung prüfen

Öffnet Wines Gamecontroller-Verwaltung.

```sh
protontricks -c 'wine control joy.cpl' 359320
```

Unter **Joysticks**:
- `Enable SDL` **aktiviert**
- `Disable hidraw` **deaktiviert**
- Beide VKBs unter **Connected (DirectInput devices)**

## 4. VKB-Buttonnamen in Elite

Die Buttonmaps stammen aus [EDCD/EliteCustomButtonNames](https://github.com/EDCD/EliteCustomButtonNames).

Kopiere diese Dateien in Elites `Bindings/DeviceButtonMaps/`-Verzeichnis:

```text
231D0200.buttonMap  → VKB rechts
231D0201.buttonMap  → VKB links
```

## 5. Funktionierende Registry sichern

In `regedit` den Zweig `Enum\WINEBUS` markieren → **Registry → Export Registry File** → **`VKB.reg`** speichern.

Später über **Registry → Import Registry File** wieder importierbar. Anschließend Elite/Proton vollständig neu starten und die Erkennung erneut prüfen.

**Dieses Backup privat aufbewahren.**