# BugBounty Toolkit - Professional Edition

A comprehensive reconnaissance and exploitation framework for bug bounty hunters.

**Version:** 1.0  
**Author:** Nobody  
**Status:** Development  

---

## Installation Methods

### Method 1: One-Click Windows Installer (Recommended for Windows Users)

Simply double-click `install.bat`:

```bash
install.bat
```

This will:
- Check if Python is installed
- Create a virtual environment
- Install all dependencies
- Run the setup script

Then launch with:
```bash
run.bat
```

### Method 2: Manual Installation with Python

**Requirements:**
- Python 3.9 or higher
- pip package manager

**Steps:**

1. **Clone the repository** (if using Git):
```bash
git clone https://github.com/NobodyOS/BugbountyToolkit.git
cd BugbountyToolkit
```

Or download the ZIP file and extract it.

2. **Create a virtual environment:**
```bash
python -m venv venv
```

3. **Activate the virtual environment:**

**Windows:**
```bash
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

5. **Run the toolkit:**
```bash
python BugbountyToolkit.py
```

### Method 3: Git Clone Setup

If you have Git installed:

```bash
# Clone the repository
git clone https://github.com/NobodyOS/BugbountyToolkit.git
cd BugbountyToolkit

# On Windows
install.bat

# On macOS/Linux
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python BugbountyToolkit.py
```

---

## Features

- **Reconnaissance Tools:** Subdomain enumeration, port scanning, service detection
- **Exploitation Framework:** Automated vulnerability scanning
- **Multi-platform Support:** Windows, macOS, Linux
- **Tool Integration:** Unified interface for multiple security tools

---

## Quick Start

### Windows Users:
1. Double-click `install.bat`
2. Double-click `run.bat`

### macOS/Linux Users:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python BugbountyToolkit.py
```

---

## Project Structure

```
BugbountyToolkit/
├── BugbountyToolkit.py      # Main application
├── Setup.py                  # Automated setup script
├── install.bat               # Windows one-click installer
├── run.bat                   # Quick launcher (Windows)
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── .gitignore               # Git ignore rules
```

---

## System Requirements

- **Python:** 3.9 or higher
- **RAM:** 4GB minimum
- **Disk Space:** 2GB for tools and data
- **OS:** Windows 7+, macOS 10.12+, or modern Linux distro

---

## Troubleshooting

### Python not found
- Install Python from https://www.python.org/
- Ensure "Add Python to PATH" is checked during installation
- Restart your computer after installation

### Virtual environment won't activate
```bash
# Try using Python 3 explicitly
python3 -m venv venv
```

### Permission denied (macOS/Linux)
```bash
chmod +x install.sh
./install.sh
```

### Dependency installation fails
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Then try installing again
pip install -r requirements.txt
```

---

## Usage

After installation, run:

**Windows:**
```bash
run.bat
```

**macOS/Linux:**
```bash
source venv/bin/activate
python BugbountyToolkit.py
```

Follow the on-screen menu to select tools and options.

---

## Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

This project is provided as-is for educational and authorized security testing purposes only.

---

## Support

For issues, questions, or suggestions:
- Check the Troubleshooting section above
- Review existing GitHub issues
- Create a new issue with detailed information

---

## Disclaimer

This toolkit is designed for authorized security testing only. Unauthorized access to computer systems is illegal. Users are responsible for ensuring their activities comply with all applicable laws and regulations.

---

**Happy Hunting! 🎯**