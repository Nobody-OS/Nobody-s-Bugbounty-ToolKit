#!/bin/bash

################################################################################
# BugBounty Toolkit - macOS Installation Script
# Version: 1.0
# Author: Nobody
# Platform: macOS
################################################################################

set -e

# Colors
RED='\033[91m'
GREEN='\033[92m'
YELLOW='\033[93m'
CYAN='\033[96m'
RESET='\033[0m'

# Clear screen
clear

# Print banner
print_banner() {
    echo -e "${CYAN}╔══════════════════════════════════════════════════════════════════════════════╗${RESET}"
    echo -e "${CYAN}║${RESET}                                                                              ${CYAN}║${RESET}"
    echo -e "${CYAN}║${RESET}              BugBounty Toolkit - macOS Installer                              ${CYAN}║${RESET}"
    echo -e "${CYAN}║${RESET}                                                                              ${CYAN}║${RESET}"
    echo -e "${CYAN}║${RESET}  This script will:                                                           ${CYAN}║${RESET}"
    echo -e "${CYAN}║${RESET}  1. Check Python installation                                                ${CYAN}║${RESET}"
    echo -e "${CYAN}║${RESET}  2. Create virtual environment                                               ${CYAN}║${RESET}"
    echo -e "${CYAN}║${RESET}  3. Install dependencies                                                     ${CYAN}║${RESET}"
    echo -e "${CYAN}║${RESET}  4. Setup the toolkit                                                        ${CYAN}║${RESET}"
    echo -e "${CYAN}║${RESET}                                                                              ${CYAN}║${RESET}"
    echo -e "${CYAN}╚══════════════════════════════════════════════════════════════════════════════╝${RESET}"
    echo
}

# Check if running on macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo -e "${RED}[ERROR] This installer is for macOS only!${RESET}"
    echo -e "${RED}Current OS: $OSTYPE${RESET}"
    exit 1
fi

print_banner

# Check for Python
echo -e "${YELLOW}[*] Checking Python installation...${RESET}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[ERROR] Python 3 is not installed!${RESET}"
    echo
    echo "Install Python 3 using Homebrew:"
    echo "  brew install python3"
    echo
    echo "Or download from: https://www.python.org/downloads/macos/"
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1)
echo -e "${GREEN}[OK] $PYTHON_VERSION found!${RESET}"
echo

# Check for pip
echo -e "${YELLOW}[*] Checking pip installation...${RESET}"
if ! python3 -m pip --version &> /dev/null; then
    echo -e "${RED}[ERROR] pip is not installed!${RESET}"
    exit 1
fi

echo -e "${GREEN}[OK] pip found!${RESET}"
echo

# Check if venv exists
if [ -d "venv" ]; then
    echo -e "${YELLOW}[!] Virtual environment already exists.${RESET}"
    echo -e "${YELLOW}[!] Skipping creation...${RESET}"
else
    echo -e "${YELLOW}[*] Creating virtual environment...${RESET}"
    python3 -m venv venv
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}[OK] Virtual environment created!${RESET}"
    else
        echo -e "${RED}[ERROR] Failed to create virtual environment!${RESET}"
        exit 1
    fi
fi
echo

# Activate virtual environment
echo -e "${YELLOW}[*] Activating virtual environment...${RESET}"
source venv/bin/activate
if [ $? -eq 0 ]; then
    echo -e "${GREEN}[OK] Virtual environment activated!${RESET}"
else
    echo -e "${RED}[ERROR] Failed to activate virtual environment!${RESET}"
    exit 1
fi
echo

# Upgrade pip
echo -e "${YELLOW}[*] Upgrading pip...${RESET}"
python3 -m pip install --quiet --upgrade pip 2>/dev/null || true
echo -e "${GREEN}[OK] pip upgraded!${RESET}"
echo

# Install requirements
echo -e "${YELLOW}[*] Installing dependencies from requirements.txt...${RESET}"
if [ ! -f "requirements.txt" ]; then
    echo -e "${RED}[ERROR] requirements.txt not found!${RESET}"
    exit 1
fi

pip install -q -r requirements.txt
if [ $? -eq 0 ]; then
    echo -e "${GREEN}[OK] Dependencies installed!${RESET}"
else
    echo -e "${RED}[ERROR] Failed to install dependencies!${RESET}"
    exit 1
fi
echo

# Run setup if it exists
if [ -f "Setup.py" ]; then
    echo -e "${YELLOW}[*] Running setup script...${RESET}"
    python Setup.py
fi
echo

# Success message
echo
echo -e "${CYAN}╔══════════════════════════════════════════════════════════════════════════════╗${RESET}"
echo -e "${CYAN}║${RESET}                    ${GREEN}INSTALLATION COMPLETED!${RESET}                             ${CYAN}║${RESET}"
echo -e "${CYAN}╚══════════════════════════════════════════════════════════════════════════════╝${RESET}"
echo
echo -e "Next steps:"
echo -e "1. Run ./run.sh to start the toolkit"
echo -e "   OR"
echo -e "2. Open Terminal in this folder and type:"
echo -e "   ${CYAN}source venv/bin/activate${RESET}"
echo -e "   ${CYAN}python BugbountyToolkit.py${RESET}"
echo
