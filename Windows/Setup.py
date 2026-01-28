#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║         ███╗   ██╗ ██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗███████╗        ║
║         ████╗  ██║██╔═══██╗██╔══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝██╔════╝        ║
║         ██╔██╗ ██║██║   ██║██████╔╝██║   ██║██║  ██║ ╚████╔╝ ███████╗        ║
║         ██║╚██╗██║██║   ██║██╔══██╗██║   ██║██║  ██║  ╚██╔╝  ╚════██║        ║
║         ██║ ╚████║╚██████╔╝██████╔╝╚██████╔╝██████╔╝   ██║   ███████║        ║
║         ╚═╝  ╚═══╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝        ║
║                                                                              ║
║         【 BugBounty Toolkit - Automated Setup & Installer 】                ║
║                                                                              ║
║  Install all bugbounty tools automatically with a single command             ║
║  Version: 1.0 | Author: Nobody | Status: Development                         ║
║  Platform: Windows Edition                                                  ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import subprocess
import time
from pathlib import Path

# Check Windows platform
if sys.platform not in ['win32', 'cygwin']:
    print("\n[ERROR] This Windows edition is designed for Windows systems only.")
    sys.exit(1)

# Try to import colorama for Windows color support
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLORAMA = True
except ImportError:
    COLORAMA = False


class Colors:
    if COLORAMA:
        RED = Fore.RED
        GREEN = Fore.GREEN
        YELLOW = Fore.YELLOW
        CYAN = Fore.CYAN
        RESET = Style.RESET_ALL
    else:
        RED = GREEN = YELLOW = CYAN = RESET = ""


class BugbountySetup:
    """Setup and initialization for Windows"""
    
    def __init__(self):
        self.current_dir = Path(__file__).parent
        self.venv_dir = self.current_dir / "venv"
    
    def clear_screen(self):
        os.system("cls")
    
    def print_banner(self):
        self.clear_screen()
        print(f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════════════╗{Colors.RESET}
{Colors.CYAN}║{Colors.RESET}                      Nobody's BugBounty Toolkit Setup                         {Colors.CYAN}║{Colors.RESET}
{Colors.CYAN}║{Colors.RESET}                          Windows Edition                                  {Colors.CYAN}║{Colors.RESET}
{Colors.CYAN}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
        """)
    
    def check_python(self):
        """Check if Python is installed"""
        self.print_banner()
        print(f"\n{Colors.YELLOW}[*] Checking Python installation...{Colors.RESET}")
        
        try:
            result = subprocess.run(["python", "--version"], capture_output=True, text=True)
            if result.returncode == 0:
                version = result.stdout.strip()
                print(f"{Colors.GREEN}[OK] {version} found!{Colors.RESET}")
                return True
        except:
            pass
        
        print(f"{Colors.RED}[ERROR] Python not found in PATH!{Colors.RESET}")
        print(f"\nPlease install Python from: https://www.python.org/downloads/")
        print(f"Make sure to check 'Add Python to PATH' during installation!")
        input("\nPress Enter to exit...")
        return False
    
    def install_dependencies(self):
        """Install Python dependencies"""
        self.print_banner()
        print(f"\n{Colors.YELLOW}[*] Installing dependencies...{Colors.RESET}\n")
        
        req_file = self.current_dir / "requirements.txt"
        if not req_file.exists():
            print(f"{Colors.RED}[ERROR] requirements.txt not found!{Colors.RESET}")
            return False
        
        try:
            subprocess.run([
                sys.executable, "-m", "pip", "install", "-q", "-r", str(req_file)
            ], check=True)
            print(f"{Colors.GREEN}[OK] Dependencies installed successfully!{Colors.RESET}")
            return True
        except Exception as e:
            print(f"{Colors.RED}[ERROR] Failed to install dependencies: {str(e)}{Colors.RESET}")
            return False
    
    def run_setup(self):
        """Run setup wizard"""
        self.print_banner()
        
        if not self.check_python():
            return False
        
        if not self.install_dependencies():
            input("\nPress Enter to exit...")
            return False
        
        self.print_banner()
        print(f"""
{Colors.GREEN}╔══════════════════════════════════════════════════════════════════════════════╗{Colors.RESET}
{Colors.GREEN}║{Colors.RESET}                  {Colors.YELLOW}SETUP COMPLETED SUCCESSFULLY!{Colors.RESET}                  {Colors.GREEN}║{Colors.RESET}
{Colors.GREEN}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

Next steps:
  1. Double-click 'run.bat' to launch the toolkit
  2. Or run: python BugbountyToolkit.py

Happy hunting!
        """)
        
        input(f"\n{Colors.YELLOW}Press Enter to exit...{Colors.RESET}")
        return True


if __name__ == "__main__":
    setup = BugbountySetup()
    setup.run_setup()
