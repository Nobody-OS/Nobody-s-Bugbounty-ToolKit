#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                                                                              ║
║         ███╗   ██╗ ██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗███████╗        ║
║         ████╗  ██║██╔═══██╗██╔══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝██╔════╝        ║
║         ██╔██╗ ██║██║   ██║██████╔╝██║   ██║██║  ██║ ╚████╔╝ ███████╗        ║
║         ██║╚██╗██║██║   ██║██╔══██╗██║   ██║██║  ██║  ╚██╔╝  ╚════██║        ║
║         ██║ ╚████║╚██████╔╝██████╔╝╚██████╔╝██████╔╝   ██║   ███████║        ║
║         ╚═╝  ╚═══╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝        ║
║                                                                              ║
║                                                                              ║
║             【 BugBounty Toolkit - Professional Edition 】                   ║
║                                                                              ║
║  A Comprehensive Reconnaissance & Exploitation Framework                     ║
║  Version: 1.0 | Author: Nobody | Status: Development                         ║
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

# Linux-only check
if sys.platform not in ['linux', 'linux2']:
    print("\n[ERROR] This toolkit is Linux-only. Please use a Linux system.")
    sys.exit(1)


# ═══════════════════════════════════════════════════════════════════════════════
# COLORS & STYLING
# ═══════════════════════════════════════════════════════════════════════════════

class Colors:
    """Professional ANSI color codes"""
    
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
    
    # Background Colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'


class Symbols:
    """Unicode symbols for prettier output"""
    
    SUCCESS = "✓"
    FAILED = "✗"
    WARNING = "⚠"
    INFO = "ℹ"
    ARROW = "➜"
    POINT = "●"
    DASH = "─"
    CROSS = "✕"
    STAR = "★"
    HOURGLASS = "⏳"
    SHIELD = "⚔"
    ROCKET = "🚀"
    TARGET = "🎯"
    LOCK = "🔒"
    UNLOCK = "🔓"


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
        "sublist3r": {
            "name": "Sublist3r",
            "description": "Fast subdomains enumeration tool",
            "url": "https://github.com/aboul3la/Sublist3r",
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
        },
        "dnsenum": {
            "name": "DNSenum",
            "description": "DNS enumeration and network mapping",
            "url": "https://github.com/fwaeytens/dnsenum",
            "type": "DNS Enumeration",
            "category": "Reconnaissance"
        },
        "fierce": {
            "name": "Fierce",
            "description": "DNS subdomain scanner",
            "url": "https://github.com/mschwager/fierce",
            "type": "DNS Enumeration",
            "category": "Reconnaissance"
        },
        "Knockpy": {
            "name": "Knockpy",
            "description": "Knockpy is a python tool to enumerate subdomains",
            "url": "https://github.com/guelfoweb/knock",
            "type": "Subdomain Enumeration",
            "category": "Reconnaissance"
        },
        "gitGraber": {
            "name": "GitGraber",
            "description": "GitHub sensitive data leak detection",
            "url": "https://github.com/hisxo/GitGraber",
            "type": "Information Gathering",
            "category": "Reconnaissance"
        },
        "Recon-ng": {
            "name": "Recon-ng",
            "description": "Web reconnaissance framework",
            "url": "https://github.com/lanmaster53/recon-ng",
            "type": "Information Gathering",
            "category": "Reconnaissance"
        },
        "waybackurls": {
            "name": "Waybackurls",
            "description": "Fetch wayback machine URLs",
            "url": "https://github.com/tomnomnom/waybackurls",
            "type": "URL Discovery",
            "category": "Reconnaissance"
        },
        "massdns": {
            "name": "MassDNS",
            "description": "High-performance DNS stubresolver",
            "url": "https://github.com/blechschmidt/massdns",
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
        "masscan": {
            "name": "Masscan",
            "description": "Fast TCP port scanner",
            "url": "https://github.com/robertdavidgraham/masscan",
            "type": "Port Scanning",
            "category": "Scanning"
        },
        "httprobe": {
            "name": "Httprobe",
            "description": "Take list of domains and probe for working HTTP/HTTPS",
            "url": "https://github.com/tomnomnom/httprobe",
            "type": "HTTP Probe",
            "category": "Scanning"
        },
        "wafw00f": {
            "name": "Wafw00f",
            "description": "WAF (Web Application Firewall) detection tool",
            "url": "https://github.com/enablesecurity/wafw00f",
            "type": "WAF Detection",
            "category": "Scanning"
        },
        "whatweb": {
            "name": "WhatWeb",
            "description": "Website fingerprinting tool",
            "url": "https://github.com/urbanadventurer/WhatWeb",
            "type": "Web Fingerprinting",
            "category": "Scanning"
        },
        "Nikto": {
            "name": "Nikto",
            "description": "Web server scanner",
            "url": "https://github.com/sullo/nikto",
            "type": "Web Scanning",
            "category": "Scanning"
        }
    },
    
    "VULNERABILITY_SCANNING": {
        "dirb": {
            "name": "Dirb",
            "description": "Web content discovery using dictionary-based brute force",
            "url": "https://github.com/SULLO/nikto/wiki/Dirb",
            "type": "Directory Enumeration",
            "category": "Vulnerability Scanning"
        },
        "dirsearch": {
            "name": "Dirsearch",
            "description": "Fast directory discovery tool",
            "url": "https://github.com/maurosoria/dirsearch",
            "type": "Directory Enumeration",
            "category": "Vulnerability Scanning"
        },
        "gobuster": {
            "name": "Gobuster",
            "description": "Fast directory/subdomain discovery tool",
            "url": "https://github.com/OJ/gobuster",
            "type": "Directory Enumeration",
            "category": "Vulnerability Scanning"
        },
        "ffuf": {
            "name": "Ffuf",
            "description": "Fast web fuzzer",
            "url": "https://github.com/ffuf/ffuf",
            "type": "Fuzzing",
            "category": "Vulnerability Scanning"
        },
        "wfuzz": {
            "name": "Wfuzz",
            "description": "Web application fuzzer",
            "url": "https://github.com/xmendez/wfuzz",
            "type": "Fuzzing",
            "category": "Vulnerability Scanning"
        },
        "sqlmap": {
            "name": "SQLMap",
            "description": "SQL injection detection and exploitation",
            "url": "https://github.com/sqlmapproject/sqlmap",
            "type": "SQL Injection",
            "category": "Vulnerability Scanning"
        },
        "commix": {
            "name": "Commix",
            "description": "Command injection detection and exploitation",
            "url": "https://github.com/commixproject/commix",
            "type": "Command Injection",
            "category": "Vulnerability Scanning"
        },
        "XSStrike": {
            "name": "XSStrike",
            "description": "XSS detection and exploitation",
            "url": "https://github.com/s0md3v/XSStrike",
            "type": "XSS Detection",
            "category": "Vulnerability Scanning"
        },
        "droopescan": {
            "name": "Droopescan",
            "description": "Drupal scanner",
            "url": "https://github.com/droope/droopescan",
            "type": "CMS Scanner",
            "category": "Vulnerability Scanning"
        },
        "joomscan": {
            "name": "Joomscan",
            "description": "Joomla vulnerability scanner",
            "url": "https://github.com/OWASP/joomscan",
            "type": "CMS Scanner",
            "category": "Vulnerability Scanning"
        },
        "wpscan": {
            "name": "WPScan",
            "description": "WordPress vulnerability scanner",
            "url": "https://github.com/wpscanteam/wpscan",
            "type": "CMS Scanner",
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
        },
        "dotdotpwn": {
            "name": "Dotdotpwn",
            "description": "Directory traversal scanner",
            "url": "https://github.com/wireghoul/dotdotpwn",
            "type": "Path Traversal",
            "category": "Exploitation"
        }
    },
    
    "AWS_SECURITY": {
        "awscli": {
            "name": "AWS CLI",
            "description": "Amazon Web Services command line interface",
            "url": "https://github.com/aws/aws-cli",
            "type": "Cloud",
            "category": "AWS Security"
        },
        "bucket_finder": {
            "name": "Bucket Finder",
            "description": "S3 bucket discovery tool",
            "url": "https://github.com/RoboJackets/bucket_finder",
            "type": "S3 Enumeration",
            "category": "AWS Security"
        },
        "s3recon": {
            "name": "S3 Recon",
            "description": "S3 bucket enumeration tool",
            "url": "https://github.com/ScanAPI/s3-recon",
            "type": "S3 Enumeration",
            "category": "AWS Security"
        },
        "S3Scanner": {
            "name": "S3Scanner",
            "description": "Scan S3 buckets for public access",
            "url": "https://github.com/sa7mon/S3Scanner",
            "type": "S3 Enumeration",
            "category": "AWS Security"
        },
        "teh_s3_bucketeers": {
            "name": "Teh S3 Bucketeers",
            "description": "S3 enumeration and testing",
            "url": "https://github.com/tomdev/teh_s3_bucketeers",
            "type": "S3 Enumeration",
            "category": "AWS Security"
        },
        "CloudFlair": {
            "name": "CloudFlair",
            "description": "Find origin IP behind CloudFlare",
            "url": "https://github.com/christophetd/CloudFlair",
            "type": "Cloud Reconnaissance",
            "category": "AWS Security"
        }
    },
    
    "SUBDOMAIN_TAKEOVER": {
        "subjack": {
            "name": "Subjack",
            "description": "Subdomain takeover detection tool",
            "url": "https://github.com/haccer/subjack",
            "type": "Subdomain Takeover",
            "category": "Subdomain Takeover"
        },
        "SubOver": {
            "name": "SubOver",
            "description": "Subdomain takeover vulnerability scanner",
            "url": "https://github.com/Ice3man543/SubOver",
            "type": "Subdomain Takeover",
            "category": "Subdomain Takeover"
        }
    },
    
    "UTILITIES": {
        "virtual-host-discovery": {
            "name": "Virtual Host Discovery",
            "description": "Virtual host enumeration tool",
            "url": "https://github.com/AlexisAhmed/virtual-host-discovery",
            "type": "Virtual Host Discovery",
            "category": "Utilities"
        },
        "tmux": {
            "name": "Tmux",
            "description": "Terminal multiplexer",
            "url": "https://github.com/tmux/tmux",
            "type": "Terminal",
            "category": "Utilities"
        },
        "zsh": {
            "name": "Zsh",
            "description": "Z Shell - interactive shell and scripting language",
            "url": "https://github.com/zsh-users/zsh",
            "type": "Shell",
            "category": "Utilities"
        }
    }
}


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN APPLICATION CLASS
# ═══════════════════════════════════════════════════════════════════════════════

class BugbountyToolkit:
    """Professional Bugbounty Toolkit with CLI interface"""
    
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
            ("5", "Quick tools launcher", Colors.BRIGHT_YELLOW),
            ("6", "About & Credits", Colors.BRIGHT_MAGENTA),
            ("0", "Exit", Colors.BRIGHT_RED),
        ]
        
        for key, text, color in menu_items:
            print(f"  {color}[{key}] {text}{Colors.RESET}")
        
        print()
    
    def print_separator(self, title=""):
        """Print a nice separator"""
        if title:
            separator = f"{Colors.BRIGHT_CYAN}═══════ {Colors.BRIGHT_YELLOW}{title}{Colors.RESET} {Colors.BRIGHT_CYAN}═══════{Colors.RESET}"
        else:
            separator = f"{Colors.BRIGHT_CYAN}{'═' * 80}{Colors.RESET}"
        print(separator)
    
    def list_all_tools(self):
        """List all tools organized by category"""
        self.clear_screen()
        self.print_header()
        
        for category, tools in self.tools.items():
            self.print_separator(category)
            
            for tool_id, tool_info in tools.items():
                installed = "✓" if self.installed_tools.get(tool_id) else "✗"
                installed_color = Colors.BRIGHT_GREEN if self.installed_tools.get(tool_id) else Colors.BRIGHT_RED
                
                print(f"\n  {Colors.BOLD}{tool_info['name']}{Colors.RESET}")
                print(f"    {Colors.GRAY}├─ Type: {Colors.CYAN}{tool_info['type']}{Colors.RESET}")
                print(f"    {Colors.GRAY}├─ Description: {Colors.WHITE}{tool_info['description']}{Colors.RESET}")
                print(f"    {Colors.GRAY}├─ Status: {installed_color}{installed}{Colors.RESET}")
                print(f"    {Colors.GRAY}└─ URL: {Colors.CYAN}{tool_info['url']}{Colors.RESET}")
        
        self.print_separator()
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")
    
    def search_tool(self):
        """Search for a tool"""
        self.clear_screen()
        self.print_header()
        
        self.print_separator("Tool Search")
        search_term = input(f"\n{Colors.YELLOW}[?] Enter tool name to search: {Colors.RESET}").strip().lower()
        
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
                    print(f"  {Colors.GRAY}Category: {Colors.CYAN}{category}{Colors.RESET}")
                    print(f"  {Colors.GRAY}Type: {Colors.CYAN}{tool_info['type']}{Colors.RESET}")
                    print(f"  {Colors.GRAY}Status: {installed_color}{installed}{Colors.RESET}")
                    print(f"  {Colors.GRAY}URL: {Colors.CYAN}{tool_info['url']}{Colors.RESET}\n")
        
        if not found:
            print(f"\n{Colors.BRIGHT_RED}{Symbols.FAILED} No tools found matching '{search_term}'{Colors.RESET}\n")
        
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")
    
    def check_installed_tools(self):
        """Check which tools are installed"""
        for category, tools in self.tools.items():
            for tool_id, tool_info in tools.items():
                # Check if tool is available in system PATH
                if shutil.which(tool_id) or shutil.which(tool_info['name'].lower()):
                    self.installed_tools[tool_id] = True
    
    def show_installed_tools(self):
        """Display installed tools"""
        self.clear_screen()
        self.print_header()
        self.print_separator("Installed Tools Status")
        
        if not self.installed_tools:
            print(f"\n{Colors.BRIGHT_YELLOW}{Symbols.WARNING} No tools currently installed{Colors.RESET}\n")
            print("Run installation commands or configure tools manually.")
        else:
            print(f"\n{Colors.BRIGHT_GREEN}{Symbols.SUCCESS} Found {len(self.installed_tools)} installed tools:{Colors.RESET}\n")
            for tool_id in sorted(self.installed_tools.keys()):
                for category, tools in self.tools.items():
                    if tool_id in tools:
                        tool_info = tools[tool_id]
                        print(f"  {Colors.BRIGHT_GREEN}{Symbols.SUCCESS}{Colors.RESET} {tool_info['name']:<20} [{category}]")
                        break
        
        self.print_separator()
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")
    
    def tool_management(self):
        """Tool management menu"""
        while True:
            self.clear_screen()
            self.print_header()
            
            self.print_separator("Tool Management")
            print(f"\n{Colors.BRIGHT_CYAN}{Symbols.ARROW} Management Options:{Colors.RESET}\n")
            print(f"  {Colors.BRIGHT_GREEN}[1] View all tools{Colors.RESET}")
            print(f"  {Colors.BRIGHT_GREEN}[2] View installed tools{Colors.RESET}")
            print(f"  {Colors.BRIGHT_GREEN}[3] Installation guide{Colors.RESET}")
            print(f"  {Colors.BRIGHT_RED}[0] Back to main menu{Colors.RESET}")
            
            choice = input(f"\n{Colors.YELLOW}[?] Select option: {Colors.RESET}").strip()
            
            if choice == "1":
                self.list_all_tools()
            elif choice == "2":
                self.show_installed_tools()
            elif choice == "3":
                self.show_installation_guide()
            elif choice == "0":
                break
            else:
                print(f"{Colors.BRIGHT_RED}{Symbols.FAILED} Invalid option{Colors.RESET}")
                time.sleep(1)
    
    def show_installation_guide(self):
        """Show installation guide"""
        self.clear_screen()
        self.print_header()
        self.print_separator("Installation Guide")
        
        guide = f"""
{Colors.BRIGHT_CYAN}Quick Installation Instructions:{Colors.RESET}

{Colors.BRIGHT_YELLOW}1. Using Package Managers:{Colors.RESET}

   {Colors.CYAN}# Ubuntu/Debian{Colors.RESET}
   sudo apt-get update
   sudo apt-get install nmap masscan nikto sqlmap commix

   {Colors.CYAN}# For Go-based tools (ffuf, subfinder, etc.){Colors.RESET}
   go get -u github.com/ffuf/ffuf
   go get -u github.com/projectdiscovery/subfinder/v2/cmd/subfinder

{Colors.BRIGHT_YELLOW}2. Using pip (Python tools):{Colors.RESET}

   pip install dnsenum dnsrecon theHarvester wfuzz dirsearch

{Colors.BRIGHT_YELLOW}3. Clone from GitHub:{Colors.RESET}

   git clone https://github.com/projectdiscovery/subfinder
   git clone https://github.com/OJ/gobuster
   git clone https://github.com/s0md3v/XSStrike

{Colors.BRIGHT_YELLOW}4. Docker (Recommended):{Colors.RESET}

   docker pull projectdiscovery/subfinder
   docker pull ffuf/ffuf
   docker pull sqlmap/sqlmap

{Colors.BRIGHT_MAGENTA}Pro Tip: Use a docker-compose file to manage all tools!{Colors.RESET}

{Colors.BRIGHT_CYAN}For detailed installation, visit tool repositories at URLs listed above.{Colors.RESET}
        """
        
        print(guide)
        self.print_separator()
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")
    
    def quick_launcher(self):
        """Quick tools launcher"""
        self.clear_screen()
        self.print_header()
        self.print_separator("Quick Tools Launcher")
        
        print(f"\n{Colors.BRIGHT_YELLOW}{Symbols.ARROW} Enter tool name or ID to launch:{Colors.RESET}\n")
        
        tools_list = []
        idx = 1
        for category, tools in self.tools.items():
            for tool_id, tool_info in tools.items():
                tools_list.append((idx, tool_id, tool_info['name'], category))
                print(f"  [{Colors.BRIGHT_CYAN}{idx:2d}{Colors.RESET}] {tool_info['name']:<25} {Colors.GRAY}({category}){Colors.RESET}")
                idx += 1
                if idx % 5 == 0:
                    print()
        
        print(f"\n  {Colors.BRIGHT_RED}[0]{Colors.RESET} Back to menu\n")
        
        try:
            choice = int(input(f"{Colors.YELLOW}[?] Select tool number: {Colors.RESET}"))
            if choice == 0:
                return
            
            for idx, tool_id, tool_name, category in tools_list:
                if idx == choice:
                    self.launch_tool(tool_id, tool_name)
                    return
        except ValueError:
            print(f"{Colors.BRIGHT_RED}{Symbols.FAILED} Invalid input{Colors.RESET}")
            time.sleep(1)
    
    def launch_tool(self, tool_id: str, tool_name: str):
        """Launch a tool"""
        self.clear_screen()
        
        print(f"{Colors.BRIGHT_GREEN}{Symbols.ROCKET} Launching {tool_name}...{Colors.RESET}\n")
        
        try:
            subprocess.run([tool_id])
        except FileNotFoundError:
            print(f"{Colors.BRIGHT_RED}{Symbols.FAILED} Tool '{tool_name}' is not installed or not in PATH{Colors.RESET}")
            print(f"{Colors.YELLOW}Please install it first using the installation guide.{Colors.RESET}\n")
            input("Press Enter to continue...")
        except Exception as e:
            print(f"{Colors.BRIGHT_RED}{Symbols.FAILED} Error launching tool: {str(e)}{Colors.RESET}\n")
            input("Press Enter to continue...")
    
    def show_about(self):
        """Show about and credits"""
        self.clear_screen()
        self.print_header()
        self.print_separator("About & Credits")
        
        about_text = f"""
{Colors.BRIGHT_CYAN}【 Project Information 】{Colors.RESET}

{Colors.BOLD}Name:{Colors.RESET}        Nobody's BugBounty Toolkit
{Colors.BOLD}Version:{Colors.RESET}     1.0 Professional Edition
{Colors.BOLD}Status:{Colors.RESET}      Active Development
{Colors.BOLD}Platform:{Colors.RESET}    Linux

{Colors.BRIGHT_YELLOW}【 Tools Included 】{Colors.RESET}

Total Tools: {len([t for c in self.tools.values() for t in c])}

Categories:
  • {Colors.BRIGHT_GREEN}Reconnaissance:{Colors.RESET} Domain enumeration, DNS scanning, OSINT
  • {Colors.BRIGHT_GREEN}Scanning:{Colors.RESET} Network scanning, port scanning, fingerprinting
  • {Colors.BRIGHT_GREEN}Vulnerability Scanning:{Colors.RESET} Web fuzzing, SQL injection, XSS detection
  • {Colors.BRIGHT_GREEN}Exploitation:{Colors.RESET} Credential cracking, path traversal
  • {Colors.BRIGHT_GREEN}AWS Security:{Colors.RESET} Cloud enumeration, S3 bucket scanning
  • {Colors.BRIGHT_GREEN}Subdomain Takeover:{Colors.RESET} Subdomain takeover detection
  • {Colors.BRIGHT_GREEN}Utilities:{Colors.RESET} Shells, terminal multiplexers

{Colors.BRIGHT_MAGENTA}【 Credits & Attribution 】{Colors.RESET}

This toolkit aggregates many open-source security tools created by the
security community. We gratefully acknowledge all tool developers and 
maintain links to original repositories for proper attribution.

Each tool retains its original license and copyright information.

{Colors.BRIGHT_YELLOW}【 Disclaimer 】{Colors.RESET}

This toolkit is designed for authorized security testing and educational
purposes only. Users are responsible for obtaining proper authorization
before testing any system. Misuse may violate local laws and regulations.

{Colors.BRIGHT_CYAN}Use responsibly. Stay ethical. Happy hunting!{Colors.RESET}
        """
        
        print(about_text)
        self.print_separator()
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")
    
    def run(self):
        """Main application loop"""
        while True:
            self.print_header()
            self.print_menu()
            
            choice = input(f"{Colors.YELLOW}[?] Select option: {Colors.RESET}").strip()
            
            if choice == "1":
                self.list_all_tools()
            elif choice == "2":
                self.search_tool()
            elif choice == "3":
                self.show_installed_tools()
            elif choice == "4":
                self.tool_management()
            elif choice == "5":
                self.quick_launcher()
            elif choice == "6":
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
