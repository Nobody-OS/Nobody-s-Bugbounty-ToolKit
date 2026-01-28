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
║  Platform: macOS Edition                                                    ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import subprocess
import time
from pathlib import Path

# Check macOS platform
if sys.platform != 'darwin':
    print("\n[ERROR] This macOS edition is designed for macOS systems only.")
    sys.exit(1)


class Colors:
    """ANSI color codes for macOS Terminal"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'


class BugbountySetup:
    """Setup and initialization for macOS"""
    
    def __init__(self):
        self.current_dir = Path(__file__).parent
        self.venv_dir = self.current_dir / "venv"
    
    def clear_screen(self):
        os.system("clear")
    
    def print_banner(self):
        self.clear_screen()
        print(f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════════════╗{Colors.RESET}
{Colors.CYAN}║{Colors.RESET}                      Nobody's BugBounty Toolkit Setup                         {Colors.CYAN}║{Colors.RESET}
{Colors.CYAN}║{Colors.RESET}                           macOS Edition                                  {Colors.CYAN}║{Colors.RESET}
{Colors.CYAN}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
        """)
    
    def check_python(self):
        """Check if Python is installed"""
        self.print_banner()
        print(f"\n{Colors.YELLOW}[*] Checking Python installation...{Colors.RESET}")
        
        try:
            result = subprocess.run(["python3", "--version"], capture_output=True, text=True)
            if result.returncode == 0:
                version = result.stdout.strip()
                print(f"{Colors.GREEN}[OK] {version} found!{Colors.RESET}")
                return True
        except:
            pass
        
        print(f"{Colors.RED}[ERROR] Python 3 not found!{Colors.RESET}")
        print(f"\nInstall Python using Homebrew:")
        print(f"  brew install python3")
        print(f"\nOr download from: https://www.python.org/downloads/macos/")
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
  1. Run ./run.sh to launch the toolkit
  2. Or run: python3 BugbountyToolkit.py

Happy hunting!
        """)
        
        input(f"\n{Colors.YELLOW}Press Enter to exit...{Colors.RESET}")
        return True


if __name__ == "__main__":
    setup = BugbountySetup()
    setup.run_setup()
