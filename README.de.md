# VKB Gladiator EVO DirectInput-Fix für Elite Dangerous

**Sprache:** [English](README.md) | Deutsch

Behebt das Problem, dass VKB Gladiator EVO-Joysticks in **Elite Dangerous unter Linux/Proton** als Xbox-/XInput-Controller statt als DirectInput-Geräte erkannt werden.

Manuell mit zwei VKB Gladiator EVO Premium getestet (rechts: `231D:0200`, links: `231D:0201`). Steam-App-ID: `359320`.

## Anleitungen

| Methode | Deutsch | English | Status |
|---|---|---|---|
| **Manueller Registry-Fix** | [DE_VKB-Proton-Elite.md](docs/DE_VKB-Proton-Elite.md) | [EN_VKB-Proton-Elite.md](docs/EN_VKB-Proton-Elite.md) | **Getestet und funktionsfähig** |
| **Automatischer Fix (`fix_vkb.py`)** | [DE_Registry_fix.md](docs/DE_Registry_fix.md) | [EN_Registry_fix.md](docs/EN_Registry_fix.md) | **Experimentell, noch nicht in einer laufenden Proton-Installation getestet** |

Das automatische Skript soll beide Sticks finden, die Wine-Registry-Einträge sichern und dieselben Änderungen wie die manuelle Anleitung durchführen. **Wer die getestete Methode nutzen möchte, sollte die manuelle Anleitung verwenden.**

[`VKB.public.reg.template`](templates/VKB.public.reg.template) ist nur eine Vorlage. Die Geräteinstanz-IDs sind Platzhalter; die Datei kann **nicht unverändert importiert werden**. Persönliche Registry-Backups gehören nicht ins Repository.

## Buttonnamen

Die manuelle Anleitung verwendet Buttonmaps aus [EDCD/EliteCustomButtonNames](https://github.com/EDCD/EliteCustomButtonNames). Vielen Dank an das Projekt für die benannten VKB-Tasten in Elite Dangerous.

## Geplant

Meine persönliche **Dual-VKB-Konfiguration für Elite Dangerous (`.binds`)** wird hinzugefügt, sobald sie fertig ist.
