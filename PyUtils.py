#!/usr/bin/env python3

import base64
import hashlib
import json
import os
import platform
import re
import secrets
import shutil
import socket
import string
import sys
import time
import urllib.parse
from datetime import datetime


APP_NAME = "PyUtils"
VERSION = "1.0.0"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def header(title):
    clear()
    print("╭────────────────────────────────────────╮")
    print(f"│   {APP_NAME:<34}│")
    print(f"│  {title:<40}│")
    print("╰────────────────────────────────────────╯\n")


def password_generator():
    header("Password Generator")

    try:
        length = int(input("Length [20]: ") or "20")
        amount = int(input("Amount [1]: ") or "1")
    except ValueError:
        print("Invalid number.")
        pause()
        return

    use_upper = input("Uppercase letters? [Y/n]: ").lower() != "n"
    use_lower = input("Lowercase letters? [Y/n]: ").lower() != "n"
    use_digits = input("Numbers? [Y/n]: ").lower() != "n"
    use_symbols = input("Symbols? [Y/n]: ").lower() != "n"

    chars = ""
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()-_=+[]{};:,.?/"

    if not chars or length < 1 or amount < 1:
        print("Invalid configuration.")
        pause()
        return

    print("\nGenerated passwords:\n")
    for _ in range(amount):
        print(secrets.choice(chars) if length == 1 else
              "".join(secrets.choice(chars) for _ in range(length)))

    pause()


def hash_generator():
    header("Hash Generator")

    value = input("Text to hash: ").encode("utf-8")

    print("\n")
    for algorithm in ("md5", "sha1", "sha256", "sha512"):
        print(f"{algorithm.upper():<8} {hashlib.new(algorithm, value).hexdigest()}")

    pause()


def file_hash():
    header("File Hash Checker")

    path = Path(input("File path: ").strip().strip('"'))

    if not path.is_file():
        print("File not found.")
        pause()
        return

    print("\nCalculating...")
    hashes = {a: hashlib.new(a) for a in ("md5", "sha1", "sha256", "sha512")}

    with path.open("rb") as f:
        while chunk := f.read(1024 * 1024):
            for h in hashes.values():
                h.update(chunk)

    print()
    for name, h in hashes.items():
        print(f"{name.upper():<8} {h.hexdigest()}")

    pause()


def system_info():
    header("System Information")

    try:
        total, used, free = shutil.disk_usage(Path.home())
        disk = f"{free / (1024**3):.1f} GB free / {total / (1024**3):.1f} GB"
    except Exception:
        disk = "Unavailable"

    print(f"OS           : {platform.system()} {platform.release()}")
    print(f"Version      : {platform.version()}")
    print(f"Architecture : {platform.machine()}")
    print(f"Processor    : {platform.processor() or 'Unknown'}")
    print(f"Python       : {platform.python_version()}")
    print(f"Hostname     : {socket.gethostname()}")
    print(f"Disk (home)  : {disk}")
    print(f"Working dir  : {Path.cwd()}")

    pause()


def network_info():
    header("Network Information")

    hostname = socket.gethostname()

    try:
        local_ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        local_ip = "Unavailable"

    print(f"Hostname     : {hostname}")
    print(f"Local IP     : {local_ip}")

    try:
        print(f"DNS test     : {socket.gethostbyname('example.com')}")
    except socket.gaierror:
        print("DNS test     : Failed")

    pause()


def json_formatter():
    header("JSON Formatter")

    print("Paste JSON, then press Enter twice on an empty line.")
    lines = []

    while True:
        line = input()
        if not line:
            break
        lines.append(line)

    raw = "\n".join(lines)

    try:
        data = json.loads(raw)
        print("\nFormatted JSON:\n")
        print(json.dumps(data, indent=4, ensure_ascii=False))
    except json.JSONDecodeError as e:
        print(f"\n❌ Invalid JSON: {e}")

    pause()


def base64_tool():
    header("Base64 Encoder / Decoder")

    mode = input("[1] Encode  [2] Decode\n\nChoose: ").strip()
    value = input("\nText: ")

    try:
        if mode == "1":
            result = base64.b64encode(value.encode()).decode()
        elif mode == "2":
            result = base64.b64decode(value).decode("utf-8")
        else:
            print("Invalid choice.")
            pause()
            return

        print(f"\nResult:\n{result}")
    except Exception as e:
        print(f"\nError: {e}")

    pause()


def timestamp_tool():
    header("Timestamp Converter")

    print("[1] Current Unix timestamp")
    print("[2] Unix timestamp → date")
    print("[3] Date → Unix timestamp")

    choice = input("\nChoose: ").strip()

    try:
        if choice == "1":
            print(f"\n{int(time.time())}")

        elif choice == "2":
            ts = float(input("Unix timestamp: "))
            print(datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S"))

        elif choice == "3":
            value = input("Date (YYYY-MM-DD HH:MM:SS): ")
            dt = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
            print(int(dt.timestamp()))

        else:
            print("Invalid choice.")
    except ValueError as e:
        print(f"Error: {e}")

    pause()


def color_converter():
    header("Color Converter")

    value = input("Hex color (#RRGGBB): ").strip().lstrip("#")

    if not re.fullmatch(r"[0-9a-fA-F]{6}", value):
        print("Invalid hexadecimal color.")
        pause()
        return

    r, g, b = (
        int(value[0:2], 16),
        int(value[2:4], 16),
        int(value[4:6], 16),
    )

    print(f"\nHEX : #{value.upper()}")
    print(f"RGB : rgb({r}, {g}, {b})")

    pause()


def url_tool():
    header("URL Encoder / Decoder")

    print("[1] Encode")
    print("[2] Decode")

    choice = input("\nChoose: ")
    value = input("Text/URL: ")

    if choice == "1":
        result = urllib.parse.quote(value, safe="")
    elif choice == "2":
        result = urllib.parse.unquote(value)
    else:
        print("Invalid choice.")
        pause()
        return

    print(f"\nResult:\n{result}")
    pause()


def disk_analyzer():
    header("Disk Analyzer")

    path = Path(input("Folder path [current]: ").strip().strip('"') or ".")

    if not path.is_dir():
        print("Folder not found.")
        pause()
        return

    print("\nScanning...\n")
    results = []

    try:
        for item in path.iterdir():
            try:
                size = 0
                if item.is_file():
                    size = item.stat().st_size
                elif item.is_dir():
                    for root, _, files in os.walk(item):
                        for filename in files:
                            try:
                                size += (Path(root) / filename).stat().st_size
                            except OSError:
                                pass
                results.append((size, item.name))
            except OSError:
                pass
    except OSError as e:
        print(f"Error: {e}")
        pause()
        return

    results.sort(reverse=True)

    for size, name in results[:20]:
        if size >= 1024**3:
            text = f"{size / 1024**3:.2f} GB"
        elif size >= 1024**2:
            text = f"{size / 1024**2:.2f} MB"
        elif size >= 1024:
            text = f"{size / 1024:.2f} KB"
        else:
            text = f"{size} B"

        print(f"{text:>12}  {name}")

    pause()


def url_parser():
    header("URL Parser")

    value = input("URL: ").strip()
    parsed = urllib.parse.urlparse(value)

    print(f"\nScheme   : {parsed.scheme}")
    print(f"Domain  : {parsed.hostname or ''}")
    print(f"Port    : {parsed.port or ''}")
    print(f"Path    : {parsed.path}")
    print(f"Query   : {parsed.query}")
    print(f"Fragment: {parsed.fragment}")

    pause()


def main():
    while True:
        header("© 2026 Eyemane | https://github.com/eyemanee")

        print("  [1]  🔐 Password Generator")
        print("  [2]  🔑 Text Hash Generator")
        print("  [3]  📄 File Hash Checker")
        print("  [4]  🖥️  System Information")
        print("  [5]  🌐 Network Information")
        print("  [6]  📝 JSON Formatter")
        print("  [7]  🔤 Base64 Encoder / Decoder")
        print("  [8]  ⏱️  Timestamp Converter")
        print("  [9]  🎨 Color Converter")
        print("  [10] 🔗 URL Encoder / Decoder")
        print("  [11] 📊 Disk Analyzer")
        print("  [12] 🔎 URL Parser")
        print("  [0]  ❌ Exit")

        choice = input("\nChoose an option: ").strip()

        actions = {
            "1": password_generator,
            "2": hash_generator,
            "3": file_hash,
            "4": system_info,
            "5": network_info,
            "6": json_formatter,
            "7": base64_tool,
            "8": timestamp_tool,
            "9": color_converter,
            "10": url_tool,
            "11": disk_analyzer,
            "12": url_parser,
        }

        if choice == "0":
            clear()
            print("Thanks for using PyUtils!")
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid option.")
            time.sleep(0.8)


if __name__ == "__main__":
    main()
