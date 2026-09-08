# ⚡ PyUtils

### The all-in-one developer utility toolkit for Python.

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Dependencies](https://img.shields.io/badge/Dependencies-0-success?style=for-the-badge)](#-installation)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=for-the-badge)](#-installation)
[![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)](#)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](#-license)

> **12 useful developer tools. One file. Zero external dependencies.**

---

## ✨ Overview

**PyUtils** is a lightweight, all-in-one command-line toolkit designed for developers, students and power users.

Instead of installing a different utility for every small task, PyUtils puts everything into one simple terminal application.

🔐 Generate passwords
🔑 Calculate hashes
📄 Analyze files
🌐 Inspect network information
📝 Format JSON
🔤 Encode and decode Base64
⏱️ Convert timestamps
🎨 Convert colors
🔗 Encode and parse URLs
📊 Analyze disk usage

Everything runs **locally on your machine**.

---

## 🚀 Features

### 🔐 Security

* Secure password generation using `secrets`
* Custom password length
* Generate multiple passwords
* Uppercase / lowercase control
* Numbers and symbols
* MD5, SHA-1, SHA-256 and SHA-512
* File hash verification

### 🛠️ Developer Tools

* JSON formatter & validator
* Base64 encoder / decoder
* Unix timestamp converter
* HEX → RGB converter
* URL encoder / decoder
* URL parser

### 💻 System Tools

* Operating system information
* Python version
* CPU information
* Architecture
* Hostname
* Local IP address
* DNS test
* Disk space information
* Directory size analyzer

---

## 🖥️ Interface

PyUtils uses a simple terminal-based interface designed to stay fast and lightweight.

```text
╭────────────────────────────────────────╮
│  ⚡ PyUtils                            │
│  All-in-one Developer Toolkit          │
╰────────────────────────────────────────╯

  [1]  🔐 Password Generator
  [2]  🔑 Text Hash Generator
  [3]  📄 File Hash Checker
  [4]  🖥️  System Information
  [5]  🌐 Network Information
  [6]  📝 JSON Formatter
  [7]  🔤 Base64 Encoder / Decoder
  [8]  ⏱️  Timestamp Converter
  [9]  🎨 Color Converter
  [10] 🔗 URL Encoder / Decoder
  [11] 📊 Disk Analyzer
  [12] 🔎 URL Parser
  [0]  ❌ Exit

Choose an option:
```

---

## 📦 Installation

### Requirements

* Python **3.9 or newer**
* No external Python packages
* Windows, Linux or macOS

### Clone

```bash
git clone https://github.com/yourusername/PyUtils.git
cd PyUtils
```

### Run

```bash
python PyUtils.py
```

On Windows:

```bash
py PyUtils.py
```

That's it.

**No `pip install`. No virtual environment. No configuration.**

---

## 🪟 Windows `.exe`

Want to use PyUtils without installing Python?

You can compile it into a standalone executable using [PyInstaller](https://pyinstaller.org/).

### Install PyInstaller

```bash
py -m pip install pyinstaller
```

### Build

```bash
py -m PyInstaller --onefile PyUtils.py
```

Your executable will be available at:

```text
dist/
└── PyUtils.exe
```

### ⚠️ Important

PyUtils is a **CLI application** and uses `input()` / `stdin`.

Therefore, **do not use**:

```bash
--windowed
```

Otherwise the executable will fail with errors such as:

```text
RuntimeError: lost sys.stdin
```

---

## 📚 Tools

| Tool                   | Description                              |
| :--------------------- | :--------------------------------------- |
| 🔐 Password Generator  | Generate secure random passwords         |
| 🔑 Hash Generator      | Hash text with multiple algorithms       |
| 📄 File Hash Checker   | Verify file integrity                    |
| 🖥️ System Information | Display system details                   |
| 🌐 Network Information | Display hostname, IP and DNS information |
| 📝 JSON Formatter      | Format and validate JSON                 |
| 🔤 Base64              | Encode and decode Base64                 |
| ⏱️ Timestamp           | Convert Unix timestamps and dates        |
| 🎨 Color Converter     | Convert HEX colors to RGB                |
| 🔗 URL Encoder         | Encode and decode URLs                   |
| 📊 Disk Analyzer       | Analyze directory sizes                  |
| 🔎 URL Parser          | Extract URL components                   |

---

## 🔒 Privacy

PyUtils is **local-first**.

Your data stays on your computer.

* No accounts
* No telemetry
* No API keys
* No cloud processing
* No external services required

Passwords, files, JSON and other inputs are processed locally.

---

## ⚡ Performance

PyUtils intentionally uses only Python's standard library.

### Dependencies

```text
External dependencies: 0
```

This makes PyUtils:

* ⚡ Lightweight
* 📦 Easy to distribute
* 🔧 Easy to maintain
* 🔒 Independent from third-party packages
* 🖥️ Easy to compile into an executable

---

## 🧩 Project Structure

```text
PyUtils/
│
├── PyUtils.py          # Main application
├── README.md           # Documentation
├── LICENSE             # Project license
└── dist/
    └── PyUtils.exe     # Optional compiled version
```

The entire application currently lives in **one Python file**.

---

## 🗺️ Roadmap

### v1.1

* [ ] UUID generator
* [ ] Regex tester
* [ ] Text statistics
* [ ] Random data generator
* [ ] Lorem Ipsum generator

### v1.2

* [ ] JWT decoder
* [ ] Unix permissions calculator
* [ ] IP calculator
* [ ] Port checker
* [ ] More encoding formats

### v2.0

* [ ] Improved terminal interface
* [ ] Configuration system
* [ ] Plugin architecture
* [ ] Export results to files
* [ ] Interactive command mode
* [ ] Cross-platform improvements

---

## 🤝 Contributing

Contributions are welcome!

### 1. Fork the repository

Click **Fork** at the top of the GitHub repository.

### 2. Clone your fork

```bash
git clone https://github.com/yourusername/PyUtils.git
cd PyUtils
```

### 3. Create a branch

```bash
git checkout -b feature/my-feature
```

### 4. Make your changes

Keep the project:

* Lightweight
* Dependency-free
* Cross-platform where possible
* Easy to understand

### 5. Commit

```bash
git commit -m "feat: add new utility"
```

### 6. Push

```bash
git push origin feature/my-feature
```

Then open a **Pull Request**.

---

## 🐛 Bug Reports

Found a bug?

Before opening an issue, make sure you're using a supported Python version.

When reporting a bug, include:

* Operating system
* Python version
* PyUtils version
* Steps to reproduce
* Error message

Screenshots are also appreciated.

---

## 💡 Feature Requests

Have an idea for a new utility?

Open a **Feature Request** and describe:

1. What the tool should do
2. Why it would be useful
3. A possible implementation

---

## 📜 License

This project is licensed under the **MIT License**.

See [`LICENSE`](LICENSE) for more information.

---

## ⭐ Support

If PyUtils is useful to you:

**⭐ Star the repository**

It helps the project grow and motivates future development.

---

<div align="center">

### ⚡ PyUtils

**One file. Zero dependencies. Twelve tools.**

Made with 🐍 Python

</div>
