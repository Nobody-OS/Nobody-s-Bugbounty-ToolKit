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
║             【 BugBounty Toolkit - Professional Edition 】                   ║
║                                                                              ║
║  A Comprehensive Reconnaissance & Exploitation Framework                     ║
║  Version: 1.0 | Author: Nobody | Status: Development                         ║
║  Platform: macOS                                                            ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import subprocess
import json
import time
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
import shutil

# Check macOS platform
if sys.platform != 'darwin':
    print("\n[ERROR] This macOS edition is designed for macOS systems only.")
    sys.exit(1)


# ═══════════════════════════════════════════════════════════════════════════════
# COLORS & STYLING
# ═══════════════════════════════════════════════════════════════════════════════

class Colors:
    """Professional ANSI color codes for macOS Terminal"""
    
    # Basic Colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    
    # Bright Colors
    BRIGHT_RED = '\033[38;5;196m'
    BRIGHT_GREEN = '\033[38;5;46m'
    BRIGHT_YELLOW = '\033[38;5;226m'
    BRIGHT_CYAN = '\033[38;5;51m'
    BRIGHT_MAGENTA = '\033[38;5;201m'
    
    # Styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    RESET = '\033[0m'


class Symbols:
    """Unicode symbols for prettier output"""
    
    SUCCESS = "✓"
    FAILED = "✗"
    WARNING = "⚠"
    INFO = "ℹ"
    ARROW = "➜"
    POINT = "●"
    HOURGLASS = "⏳"
    ROCKET = "🚀"
    TARGET = "🎯"


# ═══════════════════════════════════════════════════════════════════════════════
# BUGBOUNTY TOOLS DATABASE
# ═══════════════════════════════════════════════════════════════════════════════

TOOLS_DATABASE = {
    "RECONNAISSANCE": {
        "amass": {
            "name": "Amass",
            "description": "Advanced in-depth subdomain enumeration",
            "url": "https://github.com/OWASP/amass",
            "type": "Subdomain Enumeration",
            "category": "Reconnaissance"
        },
        "subfinder": {
            "name": "Subfinder",
            "description": "Fast and passive subdomain enumeration",
            "url": "https://github.com/projectdiscovery/subfinder",
            "type": "Subdomain Enumeration",
            "category": "Reconnaissance"
        },
        "theHarvester": {
            "name": "TheHarvester",
            "description": "E-mail, subdomain and people names harvester",
            "url": "https://github.com/laramies/theHarvester",
            "type": "Information Gathering",
            "category": "Reconnaissance"
        },
        "dnsrecon": {
            "name": "DNSRecon",
            "description": "DNS enumeration and reconnaissance",
            "url": "https://github.com/darkoperator/dnsrecon",
            "type": "DNS Enumeration",
            "category": "Reconnaissance"
        }
    },
    
    "SCANNING": {
        "Nmap": {
            "name": "Nmap",
            "description": "Network mapper - port scanning and network exploration",
            "url": "https://github.com/nmap/nmap",
            "type": "Network Scanning",
            "category": "Scanning"
        },
        "wafw00f": {
            "name": "Wafw00f",
            "description": "WAF (Web Application Firewall) detection tool",
            "url": "https://github.com/enablesecurity/wafw00f",
            "type": "WAF Detection",
            "category": "Scanning"
        }
    },
    
    "VULNERABILITY_SCANNING": {
        "sqlmap": {
            "name": "SQLMap",
            "description": "SQL injection detection and exploitation",
            "url": "https://github.com/sqlmapproject/sqlmap",
            "type": "SQL Injection",
            "category": "Vulnerability Scanning"
        },
        "wfuzz": {
            "name": "Wfuzz",
            "description": "Web application fuzzer",
            "url": "https://github.com/xmendez/wfuzz",
            "type": "Fuzzing",
            "category": "Vulnerability Scanning"
        }
    },
    
    "EXPLOITATION": {
        "thc-hydra": {
            "name": "THC-Hydra",
            "description": "Fast network login cracker",
            "url": "https://github.com/vanhauser-thc/thc-hydra",
            "type": "Credential Cracking",
            "category": "Exploitation"
        }
    }
}


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN APPLICATION CLASS
# ═══════════════════════════════════════════════════════════════════════════════

class BugbountyToolkit:
    """Professional Bugbounty Toolkit with CLI interface - macOS Edition"""
    
    def __init__(self):
        self.tools = TOOLS_DATABASE
        self.installed_tools = {}
        self.check_installed_tools()
    
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('clear')
    
    def print_header(self):
        """Print the beautiful header"""
        self.clear_screen()
        
        banner = f"""
{Colors.BRIGHT_CYAN}╔══════════════════════════════════════════════════════════════════════════════╗{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}                                                                              {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}  {Colors.BRIGHT_RED}███╗   ██╗ ██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗███████╗████████╗{Colors.RESET}   {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}  {Colors.BRIGHT_RED}████╗  ██║██╔═══██╗██╔══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝██╔════╝╚══██╔══╝{Colors.RESET}   {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}  {Colors.BRIGHT_RED}██╔██╗ ██║██║   ██║██████╔╝██║   ██║██║  ██║ ╚████╔╝ █████╗     ██║{Colors.RESET}    {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}  {Colors.BRIGHT_RED}██║╚██╗██║██║   ██║██╔══██╗██║   ██║██║  ██║  ╚██╔╝  ██╔══╝     ██║{Colors.RESET}    {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}  {Colors.BRIGHT_RED}██║ ╚████║╚██████╔╝██████╔╝╚██████╔╝██████╔╝   ██║   ███████╗   ██║{Colors.RESET}    {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}  {Colors.BRIGHT_RED}╚═╝  ╚═══╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝   ╚═╝{Colors.RESET}    {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}                                                                              {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}         {Colors.BRIGHT_YELLOW}{Symbols.STAR} BugBounty Toolkit - Professional Edition {Symbols.STAR}{Colors.RESET}        {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}                      macOS Edition                                  {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}                                                                              {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}  Comprehensive Reconnaissance & Exploitation Framework                   {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}  Version: 1.0 | Status: {Colors.BRIGHT_GREEN}READY{Colors.RESET} | Author: {Colors.BRIGHT_MAGENTA}Nobody{Colors.RESET}              {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}                                                                              {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
        """
        print(banner)
    
    def print_menu(self):
        """Print main menu"""
        print(f"\n{Colors.BRIGHT_CYAN}{Symbols.ARROW} Main Menu:{Colors.RESET}\n")
        
        menu_items = [
            ("1", "List all tools by category", Colors.BRIGHT_GREEN),
            ("2", "Search tool", Colors.BRIGHT_GREEN),
            ("3", "Check installed tools", Colors.BRIGHT_GREEN),
            ("4", "Tool management", Colors.BRIGHT_YELLOW),
            ("5", "About & Credits", Colors.BRIGHT_MAGENTA),
            ("0", "Exit", Colors.BRIGHT_RED),
        ]
        
        for key, text, color in menu_items:
            print(f"  {color}[{key}] {text}{Colors.RESET}")
        
        print()
    
    def list_all_tools(self):
        """List all tools organized by category"""
        self.clear_screen()
        self.print_header()
        
        for category, tools in self.tools.items():
            print(f"\n{Colors.BRIGHT_YELLOW}=== {category} ==={Colors.RESET}")
            
            for tool_id, tool_info in tools.items():
                installed = "✓" if self.installed_tools.get(tool_id) else "✗"
                installed_color = Colors.BRIGHT_GREEN if self.installed_tools.get(tool_id) else Colors.BRIGHT_RED
                
                print(f"\n  {Colors.BOLD}{tool_info['name']}{Colors.RESET}")
                print(f"    ├─ Type: {Colors.CYAN}{tool_info['type']}{Colors.RESET}")
                print(f"    ├─ Description: {Colors.WHITE}{tool_info['description']}{Colors.RESET}")
                print(f"    ├─ Status: {installed_color}{installed}{Colors.RESET}")
                print(f"    └─ URL: {Colors.CYAN}{tool_info['url']}{Colors.RESET}")
        
        print()
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")
    
    def search_tool(self):
        """Search for a tool"""
        self.clear_screen()
        self.print_header()
        
        search_term = input(f"\n{Colors.YELLOW}Enter tool name to search: {Colors.RESET}").strip().lower()
        
        found = False
        for category, tools in self.tools.items():
            for tool_id, tool_info in tools.items():
                if search_term in tool_info['name'].lower() or search_term in tool_id.lower():
                    if not found:
                        print()
                        found = True
                    
                    installed = "✓" if self.installed_tools.get(tool_id) else "✗"
                    installed_color = Colors.BRIGHT_GREEN if self.installed_tools.get(tool_id) else Colors.BRIGHT_RED
                    
                    print(f"{Colors.BRIGHT_GREEN}{Symbols.POINT} {tool_info['name']}{Colors.RESET}")
                    print(f"  Category: {Colors.CYAN}{category}{Colors.RESET}")
                    print(f"  Type: {Colors.CYAN}{tool_info['type']}{Colors.RESET}")
                    print(f"  Status: {installed_color}{installed}{Colors.RESET}")
                    print(f"  URL: {Colors.CYAN}{tool_info['url']}{Colors.RESET}\n")
        
        if not found:
            print(f"\n{Colors.BRIGHT_RED}{Symbols.FAILED} No tools found matching '{search_term}'{Colors.RESET}\n")
        
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")
    
    def check_installed_tools(self):
        """Check which tools are installed"""
        for category, tools in self.tools.items():
            for tool_id, tool_info in tools.items():
                if shutil.which(tool_id) or shutil.which(tool_info['name'].lower()):
                    self.installed_tools[tool_id] = True
    
    def show_installed_tools(self):
        """Display installed tools"""
        self.clear_screen()
        self.print_header()
        
        print(f"\n{Colors.BRIGHT_YELLOW}=== Installed Tools Status ==={Colors.RESET}")
        
        if not self.installed_tools:
            print(f"\n{Colors.BRIGHT_YELLOW}{Symbols.WARNING} No tools currently installed{Colors.RESET}\n")
        else:
            print(f"\n{Colors.BRIGHT_GREEN}{Symbols.SUCCESS} Found {len(self.installed_tools)} installed tools:{Colors.RESET}\n")
            for tool_id in sorted(self.installed_tools.keys()):
                for category, tools in self.tools.items():
                    if tool_id in tools:
                        tool_info = tools[tool_id]
                        print(f"  {Colors.BRIGHT_GREEN}{Symbols.SUCCESS}{Colors.RESET} {tool_info['name']:<20} [{category}]")
                        break
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")
    
    def tool_management(self):
        """Tool management menu"""
        while True:
            self.clear_screen()
            self.print_header()
            
            print(f"\n{Colors.BRIGHT_CYAN}{Symbols.ARROW} Management Options:{Colors.RESET}\n")
            print(f"  {Colors.BRIGHT_GREEN}[1] View all tools{Colors.RESET}")
            print(f"  {Colors.BRIGHT_GREEN}[2] View installed tools{Colors.RESET}")
            print(f"  {Colors.BRIGHT_GREEN}[3] Installation guide{Colors.RESET}")
            print(f"  {Colors.BRIGHT_RED}[0] Back to main menu{Colors.RESET}")
            
            choice = input(f"\n{Colors.YELLOW}Select option: {Colors.RESET}").strip()
            
            if choice == "1":
                self.list_all_tools()
            elif choice == "2":
                self.show_installed_tools()
            elif choice == "3":
                self.show_installation_guide()
            elif choice == "0":
                break
            else:
                print(f"{Colors.BRIGHT_RED}Invalid option{Colors.RESET}")
                time.sleep(1)
    
    def show_installation_guide(self):
        """Show installation guide"""
        self.clear_screen()
        self.print_header()
        
        guide = f"""
{Colors.BRIGHT_CYAN}Installation Guide for macOS:{Colors.RESET}

{Colors.BRIGHT_YELLOW}1. Using Homebrew (Recommended):{Colors.RESET}

   First, install Homebrew if you don't have it:
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

   Then install tools:
   {Colors.CYAN}brew install nmap sqlmap nikto wget curl git{Colors.RESET}

{Colors.BRIGHT_YELLOW}2. Using pip (Python tools):{Colors.RESET}

   {Colors.CYAN}pip install theHarvester wfuzz dnspython wafw00f{Colors.RESET}

{Colors.BRIGHT_YELLOW}3. Clone from GitHub:{Colors.RESET}

   {Colors.CYAN}git clone https://github.com/projectdiscovery/subfinder{Colors.RESET}
   {Colors.CYAN}git clone https://github.com/OWASP/amass{Colors.RESET}

{Colors.BRIGHT_YELLOW}4. Install Command Line Tools:{Colors.RESET}

   Some tools require Xcode Command Line Tools:
   {Colors.CYAN}xcode-select --install{Colors.RESET}

{Colors.BRIGHT_MAGENTA}Pro Tip: Use tmux for session management!{Colors.RESET}
{Colors.CYAN}brew install tmux{Colors.RESET}

{Colors.BRIGHT_CYAN}For detailed installation, visit tool repositories at URLs listed above.{Colors.RESET}
        """
        
        print(guide)
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")
    
    def show_about(self):
        """Show about and credits"""
        self.clear_screen()
        self.print_header()
        
        about_text = f"""
{Colors.BRIGHT_CYAN}【 Project Information 】{Colors.RESET}

Name:        Nobody's BugBounty Toolkit - macOS Edition
Version:     1.0 Professional Edition
Status:      Active Development
Platform:    macOS 10.12+

{Colors.BRIGHT_YELLOW}【 Tools Included 】{Colors.RESET}

Categories:
  • {Colors.BRIGHT_GREEN}Reconnaissance:{Colors.RESET} Subdomain enumeration, DNS scanning, OSINT
  • {Colors.BRIGHT_GREEN}Scanning:{Colors.RESET} Network scanning, WAF detection
  • {Colors.BRIGHT_GREEN}Vulnerability Scanning:{Colors.RESET} SQL injection, Web fuzzing
  • {Colors.BRIGHT_GREEN}Exploitation:{Colors.RESET} Credential cracking

{Colors.BRIGHT_MAGENTA}【 Credits & Attribution 】{Colors.RESET}

This toolkit aggregates many open-source security tools created by the
security community. Each tool retains its original license.

{Colors.BRIGHT_YELLOW}【 Disclaimer 】{Colors.RESET}

This toolkit is designed for authorized security testing and educational
purposes only. Users are responsible for obtaining proper authorization
before testing any system. Misuse may violate local laws and regulations.

Use responsibly. Stay ethical. Happy hunting!
        """
        
        print(about_text)
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")
    
    def run(self):
        """Main application loop"""
        while True:
            self.print_header()
            self.print_menu()
            
            choice = input(f"{Colors.YELLOW}Select option: {Colors.RESET}").strip()
            
            if choice == "1":
                self.list_all_tools()
            elif choice == "2":
                self.search_tool()
            elif choice == "3":
                self.show_installed_tools()
            elif choice == "4":
                self.tool_management()
            elif choice == "5":
                self.show_about()
            elif choice == "0":
                self.exit_application()
            else:
                print(f"{Colors.BRIGHT_RED}Invalid option. Try again.{Colors.RESET}")
                time.sleep(1)
    
    def exit_application(self):
        """Exit the application"""
        self.clear_screen()
        
        exit_banner = f"""
{Colors.BRIGHT_CYAN}╔══════════════════════════════════════════════════════════════════════════════╗{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}                                                                              {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}                  {Colors.BRIGHT_YELLOW}Thank you for using Nobody's BugBounty Toolkit!{Colors.RESET}                 {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}                                                                              {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}                    {Colors.BRIGHT_GREEN}Happy hunting! Stay ethical and responsible.{Colors.RESET}              {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}                                                                              {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
        """
        print(exit_banner)
        sys.exit(0)


# ═══════════════════════════════════════════════════════════════════════════════
# ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    app = BugbountyToolkit()
    app.run()
