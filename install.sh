#!/bin/bash

# ═══════════════════════════════════════════════════════════════════════════════
# BugBounty Toolkit - Linux Installer
# ═══════════════════════════════════════════════════════════════════════════════

set -e

clear

echo ""
echo "╔═══════════════════════════════════════════════════════════════════════╗"
echo "║                                                                       ║"
echo "║   BugBounty Toolkit - Professional Edition Installer                  ║"
echo "║                                                                       ║"
echo "║   Version: 1.0 │ Author: Nobody                                       ║"
echo "║                                                                       ║"
echo "╚═══════════════════════════════════════════════════════════════════════╝"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python3 is not installed or not in PATH!"
    echo ""
    echo "Please install Python 3.9+ using your package manager:"
    echo "  Ubuntu/Debian: sudo apt install python3 python3-pip python3-venv"
    echo "  Fedora: sudo dnf install python3 python3-pip"
    echo "  Arch: sudo pacman -S python"
    echo ""
    exit 1
fi

echo "[*] Python3 detected!"
python3 --version
echo ""

# Create virtual environment
echo "[*] Creating virtual environment..."
if [ -d "venv" ]; then
    echo "[!] Virtual environment already exists, skipping creation"
else
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "[ERROR] Failed to create virtual environment!"
        exit 1
    fi
    echo "[✓] Virtual environment created successfully"
fi

# Activate virtual environment
echo "[*] Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "[*] Upgrading pip..."
pip install --upgrade pip setuptools wheel

# Install requirements
if [ -f "requirements.txt" ]; then
    echo "[*] Installing required packages from requirements.txt..."
    pip install -r requirements.txt
    if [ $? -eq 0 ]; then
        echo "[✓] All packages installed successfully!"
    else
        echo "[ERROR] Failed to install packages!"
        exit 1
    fi
else
    echo "[WARNING] requirements.txt not found, skipping package installation"
fi

echo ""
echo "╔═══════════════════════════════════════════════════════════════════════╗"
echo "║                   Installation Complete!                             ║"
echo "║                                                                       ║"
echo "║   To start using the toolkit, run:                                    ║"
echo "║      ./run.sh                                                         ║"
echo "║                                                                       ║"
echo "╚═══════════════════════════════════════════════════════════════════════╝"
echo ""
