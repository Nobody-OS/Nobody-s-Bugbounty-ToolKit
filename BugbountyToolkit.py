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
║  Platform: Windows                                                           ║
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

# Check Windows platform
if sys.platform not in ['win32', 'cygwin']:
    print("\n[ERROR] This Windows edition is designed for Windows systems only.")
    sys.exit(1)

# Try to import colorama for Windows color support
try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False


# ═══════════════════════════════════════════════════════════════════════════════
# COLORS & STYLING FOR WINDOWS
# ═══════════════════════════════════════════════════════════════════════════════

class Colors:
    """Color codes for Windows console"""
    
    if COLORAMA_AVAILABLE:
        RED = Fore.RED
        GREEN = Fore.GREEN
        YELLOW = Fore.YELLOW
        BLUE = Fore.BLUE
        MAGENTA = Fore.MAGENTA
        CYAN = Fore.CYAN
        WHITE = Fore.WHITE
        BRIGHT_RED = Fore.RED
        BRIGHT_GREEN = Fore.GREEN
        BRIGHT_YELLOW = Fore.YELLOW
        BRIGHT_CYAN = Fore.CYAN
        BRIGHT_MAGENTA = Fore.MAGENTA
        BOLD = Style.BRIGHT
        RESET = Style.RESET_ALL
        GRAY = Fore.WHITE
        DIM = Style.DIM
    else:
        RED = ""
        GREEN = ""
        YELLOW = ""
        BLUE = ""
        MAGENTA = ""
        CYAN = ""
        WHITE = ""
        BRIGHT_RED = ""
        BRIGHT_GREEN = ""
        BRIGHT_YELLOW = ""
        BRIGHT_CYAN = ""
        BRIGHT_MAGENTA = ""
        BOLD = ""
        RESET = ""
        GRAY = ""
        DIM = ""


class Symbols:
    """Unicode symbols for prettier output"""
    
    SUCCESS = "OK"
    FAILED = "FAIL"
    WARNING = "WARN"
    INFO = "INFO"
    ARROW = "-->"
    POINT = ">"
    DASH = "-"
    CROSS = "X"
    STAR = "*"
    HOURGLASS = "..."
    SHIELD = "#"
    ROCKET = "!"
    TARGET = "@"
    LOCK = "L"
    UNLOCK = "U"


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
    """Professional Bugbounty Toolkit with CLI interface - Windows Edition"""
    
    def __init__(self):
        self.tools = TOOLS_DATABASE
        self.installed_tools = {}
        self.check_installed_tools()
    
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls')
    
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
{Colors.BRIGHT_CYAN}║{Colors.RESET}         {Colors.BRIGHT_YELLOW}* BugBounty Toolkit - Professional Edition *{Colors.RESET}        {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}                      Windows Edition                                {Colors.BRIGHT_CYAN}║{Colors.RESET}
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
                installed = "OK" if self.installed_tools.get(tool_id) else "NO"
                installed_color = Colors.BRIGHT_GREEN if self.installed_tools.get(tool_id) else Colors.BRIGHT_RED
                
                print(f"\n  {Colors.BOLD}{tool_info['name']}{Colors.RESET}")
                print(f"    Type: {Colors.CYAN}{tool_info['type']}{Colors.RESET}")
                print(f"    Description: {Colors.WHITE}{tool_info['description']}{Colors.RESET}")
                print(f"    Status: {installed_color}{installed}{Colors.RESET}")
        
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
                    
                    installed = "OK" if self.installed_tools.get(tool_id) else "NO"
                    installed_color = Colors.BRIGHT_GREEN if self.installed_tools.get(tool_id) else Colors.BRIGHT_RED
                    
                    print(f"{Colors.BRIGHT_GREEN}[+] {tool_info['name']}{Colors.RESET}")
                    print(f"  Category: {Colors.CYAN}{category}{Colors.RESET}")
                    print(f"  Type: {Colors.CYAN}{tool_info['type']}{Colors.RESET}")
                    print(f"  Status: {installed_color}{installed}{Colors.RESET}")
                    print(f"  URL: {Colors.CYAN}{tool_info['url']}{Colors.RESET}\n")
        
        if not found:
            print(f"\n{Colors.BRIGHT_RED}[!] No tools found matching '{search_term}'{Colors.RESET}\n")
        
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
            print(f"\n{Colors.BRIGHT_YELLOW}[!] No tools currently installed{Colors.RESET}\n")
        else:
            print(f"\n{Colors.BRIGHT_GREEN}[OK] Found {len(self.installed_tools)} installed tools:{Colors.RESET}\n")
            for tool_id in sorted(self.installed_tools.keys()):
                for category, tools in self.tools.items():
                    if tool_id in tools:
                        tool_info = tools[tool_id]
                        print(f"  {Colors.BRIGHT_GREEN}[OK]{Colors.RESET} {tool_info['name']:<20} [{category}]")
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
                print(f"{Colors.BRIGHT_RED}[!] Invalid option{Colors.RESET}")
                time.sleep(1)
    
    def show_installation_guide(self):
        """Show installation guide"""
        self.clear_screen()
        self.print_header()
        
        guide = f"""
{Colors.BRIGHT_CYAN}Quick Installation Instructions for Windows:{Colors.RESET}

{Colors.BRIGHT_YELLOW}1. Using Chocolatey:{Colors.RESET}

   choco install nmap nikto sqlmap wfuzz -y

{Colors.BRIGHT_YELLOW}2. Using pip (Python tools):{Colors.RESET}

   pip install dnsenum dnsrecon theHarvester wfuzz wafw00f

{Colors.BRIGHT_YELLOW}3. Download Binaries:{Colors.RESET}

   - Visit https://github.com/OWASP/amass/releases (Amass)
   - Visit https://nmap.org/download.html (Nmap)
   - Visit https://github.com/projectdiscovery/subfinder (Subfinder)

{Colors.BRIGHT_YELLOW}4. Extract and Add to PATH:{Colors.RESET}

   1. Extract downloaded files
   2. Move to C:\\Program Files\\YourTool
   3. Add to System PATH via Environment Variables

{Colors.BRIGHT_MAGENTA}Pro Tip: Use WSL2 (Windows Subsystem for Linux) for better compatibility!{Colors.RESET}

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

Name:        Nobody's BugBounty Toolkit - Windows Edition
Version:     1.0 Professional Edition
Status:      Active Development
Platform:    Windows 7+

{Colors.BRIGHT_YELLOW}【 Tools Included 】{Colors.RESET}

Categories:
  * Reconnaissance: Domain enumeration, DNS scanning
  * Scanning: Network scanning, WAF detection
  * Vulnerability Scanning: SQL injection, Web fuzzing
  * Exploitation: Credential cracking

{Colors.BRIGHT_MAGENTA}【 Disclaimer 】{Colors.RESET}

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
