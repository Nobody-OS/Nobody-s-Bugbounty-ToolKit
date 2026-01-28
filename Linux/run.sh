#!/bin/bash

# ═══════════════════════════════════════════════════════════════════════════════
# BugBounty Toolkit - Linux Launcher
# ═══════════════════════════════════════════════════════════════════════════════

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "[!] Virtual environment not found. Running installer first..."
    chmod +x install.sh
    ./install.sh
fi

# Activate virtual environment
source venv/bin/activate

# Run the toolkit
python3 BugbountyToolkit.py
