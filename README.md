# BugBounty Toolkit - macOS Edition

A comprehensive reconnaissance and exploitation framework for bug bounty hunters.

**Version:** 1.0  
**Author:** Nobody  
**Status:** Development  
**Platform:** macOS Only

---

## Installation Methods

### Method 1: One-Click Installer (Recommended)

Run the installation script:

```bash
chmod +x install.sh
./install.sh
```

This will:
- Check if Python is installed
- Create a virtual environment
- Install all dependencies
- Run the setup script
- Verify installation

Then launch with:
```bash
./run.sh
```

### Method 2: Manual Installation with Python

**Requirements:**
- Python 3.9 or higher
- pip package manager

**Steps:**

1. **Download the repository:**
   - Clone from Git or download the ZIP file
   - Extract to your desired location

2. **Create a virtual environment:**
```bash
python3 -m venv venv
```

3. **Activate the virtual environment:**
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

### Method 3: Using Homebrew

If you prefer Homebrew package management:

```bash
# Install Python if not already installed
brew install python3

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run toolkit
python BugbountyToolkit.py
```

---

## Features

- **Reconnaissance Tools:** Subdomain enumeration, DNS scanning, OSINT
- **Exploitation Framework:** Automated vulnerability scanning
- **macOS-Optimized:** Fully compatible with macOS 10.12+
- **Tool Integration:** Unified interface for multiple security tools

---

## Quick Start

**Option 1 - Automatic (Easiest):**
```bash
chmod +x install.sh
./install.sh
./run.sh
```

**Option 2 - Manual:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python BugbountyToolkit.py
```

---

## Project Structure

```
MacOS/
├── BugbountyToolkit.py      # Main application
├── Setup.py                 # Automated setup script
├── install.sh               # Installation script
├── run.sh                   # Quick launcher
├── requirements.txt         # Python dependencies
├── README.md                # This file
└── .gitignore              # Git ignore rules
```

---

## System Requirements

- **Python:** 3.9 or higher
- **macOS:** 10.12 (Sierra) or later
- **RAM:** 4GB minimum
- **Disk Space:** 2GB for tools and data
- **Xcode Command Line Tools:** May be required for some tools

---

## Troubleshooting

### Python not found / "python: command not found"
```bash
# Install Python via Homebrew
brew install python3

# Verify installation
python3 --version
```

### "Permission denied" on install.sh
```bash
chmod +x install.sh
./install.sh
```

### Virtual environment won't activate
```bash
# Make sure you're using bash or zsh
source venv/bin/activate

# For fish shell users
source venv/bin/activate.fish
```

### Missing Xcode Command Line Tools
```bash
xcode-select --install
```

### pip install fails with SSL errors
```bash
# Update pip first
python3 -m pip install --upgrade pip

# Then try installing again
pip install -r requirements.txt

# If still failing, try:
pip install --upgrade certifi
```

### "No module named 'colorama'" or other import errors
```bash
# Reinstall all dependencies
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

### Port already in use
- Check Activity Monitor for conflicting processes
- Or specify a different port when running the toolkit

---

## Usage

After installation, run the toolkit:

**Option 1 - Using shell script (Easiest):**
```bash
./run.sh
```

**Option 2 - Manual activation:**
```bash
source venv/bin/activate
python BugbountyToolkit.py
```

**Option 3 - Without virtual environment:**
```bash
python3 BugbountyToolkit.py
```

Follow the on-screen menu to select tools and options.

---

## Uninstallation

To completely remove the toolkit:

```bash
# Remove virtual environment
rm -rf venv

# Or remove entire directory
rm -rf BugbountyToolkit
```

---

## Homebrew Package Dependencies

Some tools may require additional installation via Homebrew:

```bash
# Network tools
brew install nmap

# Security tools
brew install sqlmap nikto

# Utilities
brew install wget curl git

# Optional: tmux for session management
brew install tmux
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
