#!/bin/bash

################################################################################
# BugBounty Toolkit - macOS Launcher
# Version: 1.0
# Author: Nobody
# Platform: macOS
################################################################################

# Colors
RED='\033[91m'
GREEN='\033[92m'
YELLOW='\033[93m'
CYAN='\033[96m'
RESET='\033[0m'

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo -e "${RED}[ERROR] Virtual environment not found!${RESET}"
    echo
    echo "Please run install.sh first to set up the toolkit."
    echo
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Check if BugbountyToolkit.py exists
if [ ! -f "BugbountyToolkit.py" ]; then
    echo -e "${RED}[ERROR] BugbountyToolkit.py not found!${RESET}"
    exit 1
fi

# Print header
clear
echo
echo -e "${CYAN}╔══════════════════════════════════════════════════════════════════════════════╗${RESET}"
echo -e "${CYAN}║${RESET}           BugBounty Toolkit - Launching Application                      ${CYAN}║${RESET}"
echo -e "${CYAN}╚══════════════════════════════════════════════════════════════════════════════╝${RESET}"
echo

# Run the toolkit
python BugbountyToolkit.py

# Check if there was an error
if [ $? -ne 0 ]; then
    echo
    echo -e "${RED}[ERROR] The toolkit encountered an error!${RESET}"
    exit 1
fi

exit 0
