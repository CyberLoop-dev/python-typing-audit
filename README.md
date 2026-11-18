<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:60a5fa&height=170&section=header&text=Python%20Typing%20Audit&fontColor=ffffff&fontSize=38&animation=fadeIn" width="100%" alt="Python Typing Audit banner"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&duration=2800&pause=900&color=60A5FA&center=true&vCenter=true&width=650&lines=Find+missing+Python+annotations;Review+function+signatures+with+AST;Run+locally+without+third-party+packages" alt="Typing introduction"/>
<p>Find missing function annotations with a lightweight AST check.</p>
<p><img src="https://img.shields.io/github/license/CyberLoop-dev/python-typing-audit?style=for-the-badge" alt="License"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/python-typing-audit?style=for-the-badge" alt="Language"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/python-typing-audit?style=for-the-badge" alt="Stars"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/python-typing-audit?style=for-the-badge" alt="Last commit"/></p>
<img src="assets/icon.svg" width="112" alt="Project icon"/>
</div>

## ✨ Overview
Python Typing Audit parses Python source files with the built-in AST module and reports function parameters or return values that lack annotations. It is a review aid, not a type checker.

## 🚀 Features
- ✨ Scan a Python file or a directory recursively
- ✨ Report missing argument and return annotations with line numbers
- ✨ Ignore the conventional `self` and `cls` parameters
- ✨ Export machine-readable JSON
- ✨ Return a non-zero exit code when findings exist in strict mode

## 🎬 Demo
Run `python main.py src/ --strict` to list missing annotations and use the exit code in a local check.

## ⚡ Quick Start
```bash
python main.py path/to/project
python main.py path/to/project --json
python main.py path/to/project --strict
```

## 🧰 Tech Stack
Python 3.10+ and the standard-library `ast`, `argparse`, and `pathlib` modules.

## 🗂️ Folder Structure
```text
.
├── main.py
├── requirements.txt
├── tests/test_main.py
├── assets/icon.svg
├── .gitignore
└── LICENSE
```

## 🧭 Roadmap
- [ ] Add per-file ignore patterns
- [ ] Add a configurable exclusion list
- [ ] Add a GitHub Actions example

## 🤝 Contributing
Issues and focused pull requests are welcome. Include AST-based tests for new reporting rules.

## 📄 License
Released under the [MIT License](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:60a5fa&height=100&section=footer" width="100%" alt="Animated wave footer"/></div>
