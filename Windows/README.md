# BugBounty Toolkit - Windows Edition

A comprehensive reconnaissance and exploitation framework for bug bounty hunters.

**Version:** 1.0  
**Author:** Nobody  
**Status:** Development  
**Platform:** Windows Only

---

## Installation Methods

### Method 1: One-Click Installer (Recommended)

Simply double-click `install.bat`:

```batch
install.bat
```

This will:
- Check if Python is installed
- Create a virtual environment
- Install all dependencies
- Run the setup script
- Verify installation

Then launch with:
```batch
run.bat
```

### Method 2: Manual Installation with Python

**Requirements:**
- Python 3.9 or higher
- pip package manager

**Steps:**

1. **Download the repository:**
   - Download the ZIP file from GitHub
   - Extract it to your desired location

2. **Create a virtual environment:**
```batch
python -m venv venv
```

3. **Activate the virtual environment:**
```batch
venv\Scripts\activate.bat
```

4. **Install dependencies:**
```batch
pip install -r requirements.txt
```

5. **Run the toolkit:**
```batch
python BugbountyToolkit.py
```

### Method 3: Windows PowerShell Setup

If you prefer PowerShell:

```powershell
# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run toolkit
python BugbountyToolkit.py
```

---

## Features

- **Reconnaissance Tools:** Subdomain enumeration, port scanning, service detection
- **Exploitation Framework:** Automated vulnerability scanning
- **Windows-Optimized:** Fully compatible with Windows 7 and later
- **Tool Integration:** Unified interface for multiple security tools

---

## Quick Start

**Option 1 - Automatic (Easiest):**
1. Double-click `install.bat`
2. Double-click `run.bat`

**Option 2 - Manual:**
```batch
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python BugbountyToolkit.py
```

---

## Project Structure

```
Windows/
├── BugbountyToolkit.py      # Main application
├── Setup.py                 # Automated setup script
├── install.bat              # One-click installer
├── run.bat                  # Quick launcher
├── requirements.txt         # Python dependencies
├── README.md                # This file
└── .gitignore              # Git ignore rules
```

---

## System Requirements

- **Python:** 3.9 or higher
- **Windows:** Windows 7 SP1 or later (32-bit or 64-bit)
- **RAM:** 4GB minimum
- **Disk Space:** 2GB for tools and data
- **Administrator Rights:** May be required for some tools

---

## Troubleshooting

### Python not found / "python is not recognized"
1. Install Python from https://www.python.org/
2. **Important:** During installation, check the box "Add Python to PATH"
3. Restart your computer after installation
4. Open a new Command Prompt and try again

### "The system cannot find the file specified"
```batch
# Use the full path to Python if it's not in PATH
C:\Python39\python -m venv venv
```

### Virtual environment won't activate
- Make sure you're using Command Prompt (cmd.exe), not PowerShell
- If using PowerShell, run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- Then use: `.\venv\Scripts\Activate.ps1`

### pip install fails
```batch
# Upgrade pip first
python -m pip install --upgrade pip

# Then try installing again
pip install -r requirements.txt

# If that fails, try:
pip install --user -r requirements.txt
```

### Port already in use
- Close other applications using the same port
- Or specify a different port when running the toolkit

### Permission denied errors
- Run Command Prompt as Administrator
- Right-click on cmd.exe and select "Run as Administrator"

### DLL/Module import errors
```batch
# Reinstall all dependencies
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

---

## Usage

After installation, run the toolkit:

**Option 1 - Using batch file (Easiest):**
```batch
run.bat
```

**Option 2 - Manual activation:**
```batch
venv\Scripts\activate.bat
python BugbountyToolkit.py
```

**Option 3 - PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
python BugbountyToolkit.py
```

Follow the on-screen menu to select tools and options.

---

## Uninstallation

To completely remove the toolkit:

1. Delete the extracted folder
2. Or run in Command Prompt:
```batch
rmdir /s /q venv
```

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
