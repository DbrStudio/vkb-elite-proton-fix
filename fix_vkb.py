#!/usr/bin/env python3
"""Elite Dangerous / Proton: map VKB Gladiator EVO sticks to DirectInput."""

import os
import re
import shlex
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

APP_ID = "359320"
WINEBUS = r"HKLM\System\CurrentControlSet\Enum\WINEBUS"
FULL_WINEBUS = r"HKEY_LOCAL_MACHINE\System\CurrentControlSet\Enum\WINEBUS"
DEVICES = {"0200": "rechts", "0201": "links"}
BACKUP_DIR = Path.home() / ".local/state/vkb-elite-proton-fix/backups"


def run_reg(*args: str) -> None:
    command = shlex.join(("wine", "reg", *args))
    subprocess.run(["protontricks", "-c", command, APP_ID], check=True)


def wine_path(path: Path) -> str:
    # Wine's standard Z: drive maps the Unix filesystem.
    return "Z:" + str(path.resolve()).replace("/", "\\")


def read_reg(path: Path) -> str:
    raw = path.read_bytes()
    if raw.startswith((b"\xff\xfe", b"\xfe\xff")):
        return raw.decode("utf-16")
    if raw[:8].count(b"\x00") >= 2:
        return raw.decode("utf-16-le")
    return raw.decode("utf-8-sig")


def find_instances(exported: str) -> list[str]:
    result = []
    for product_id, side in DEVICES.items():
        pattern = re.compile(
            rf"^\[({re.escape(FULL_WINEBUS)}\\VID_231D&PID_{product_id}\\[^\\\]\r\n]+)\]\r?$",
            re.IGNORECASE | re.MULTILINE,
        )
        matches = list(pattern.finditer(exported))
        if len(matches) != 1:
            raise ValueError(f"VKB {side}: {len(matches)} Geräteinstanzen gefunden (erwartet: 1).")
        section_end = exported.find("\n[", matches[0].end())
        section = exported[matches[0].end():section_end if section_end != -1 else None]
        for value in ('"Service"=', '"DeviceDesc"=', '"CompatibleIDs"='):
            if value.lower() not in section.lower():
                raise ValueError(f"VKB {side}: Registry-Wert {value} fehlt. Keine Änderung.")
        result.append(matches[0].group(1))
    return result


def build_patch(instances: list[str]) -> str:
    multi_sz = (r"WINEBUS\WINE_COMP_HID" + "\0\0").encode("utf-16le")
    bytes_as_hex = [f"{value:02x}" for value in multi_sz]
    hex_lines = [",".join(bytes_as_hex[i:i + 24]) for i in range(0, len(bytes_as_hex), 24)]
    hex_value = ",\\\r\n  ".join(hex_lines)
    entries = ["Windows Registry Editor Version 5.00", ""]
    for path in instances:
        entries.extend([
            f"[{path}]",
            '"Service"="winehid"',
            '"DeviceDesc"="Wine HID compatible device"',
            f'"CompatibleIDs"=hex(7):{hex_value}',
            "",
        ])
    return "\r\n".join(entries) + "\r\n"


def main() -> None:
    if not shutil.which("protontricks"):
        raise RuntimeError("protontricks fehlt.")
    old_umask = os.umask(0o077)
    try:
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
        backup = BACKUP_DIR / f"VKB-{stamp}.reg"
        patch = BACKUP_DIR / f"VKB-patch-{stamp}.reg"

        print("Sichere WINEBUS-Registry …", flush=True)
        run_reg("export", WINEBUS, wine_path(backup))
        if not backup.is_file() or backup.stat().st_size == 0:
            raise RuntimeError("Backup fehlt oder ist leer. Keine Änderung.")

        instances = find_instances(read_reg(backup))
        patch.write_text(build_patch(instances), encoding="utf-16")
        print("Gefunden: VKB rechts und links. Wende DirectInput-Fix an …", flush=True)
        run_reg("import", wine_path(patch))
        print(f"Fertig. Privates Backup: {backup}")
        print("Beide VKBs mit 'wine control joy.cpl' im Elite-Prefix prüfen.")
    finally:
        os.umask(old_umask)


if __name__ == "__main__":
    try:
        main()
    except (OSError, UnicodeError, ValueError, subprocess.CalledProcessError, RuntimeError) as exc:
        print(f"Fehler: {exc}", file=sys.stderr)
        sys.exit(1)
