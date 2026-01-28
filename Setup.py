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
from typing import List, Dict, Tuple, Optional
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
# TOOLS INSTALLATION DATABASE
# ═══════════════════════════════════════════════════════════════════════════════

TOOLS_INSTALL_DB = {
    # RECONNAISSANCE TOOLS
    "altdns": {
        "name": "Altdns",
        "category": "Reconnaissance",
        "description": "Subdomain discovery through alterations and permutations",
        "install": {
            "linux": ["pip install altdns"]
        }
    },
    "amass": {
        "name": "Amass",
        "category": "Reconnaissance",
        "description": "Advanced in-depth subdomain enumeration",
        "install": {
            "linux": [
                "wget https://github.com/OWASP/amass/releases/download/v3.23.0/amass_linux_amd64.zip",
                "unzip amass_linux_amd64.zip",
                "sudo mv amass /usr/local/bin/"
            ]
        }
    },
    "subfinder": {
        "name": "Subfinder",
        "category": "Reconnaissance",
        "description": "Fast and passive subdomain enumeration",
        "install": {
            "linux": [
                "go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"
            ]
        }
    },
    "sublist3r": {
        "name": "Sublist3r",
        "category": "Reconnaissance",
        "description": "Fast subdomains enumeration tool",
        "install": {
            "linux": [
                "git clone https://github.com/aboul3la/Sublist3r.git",
                "cd Sublist3r && pip install -r requirements.txt"
            ]
        }
    },
    "theHarvester": {
        "name": "TheHarvester",
        "category": "Reconnaissance",
        "description": "E-mail, subdomain and people names harvester",
        "install": {
            "linux": ["pip install theHarvester"]
        }
    },
    "dnsrecon": {
        "name": "DNSRecon",
        "category": "Reconnaissance",
        "description": "DNS enumeration and reconnaissance",
        "install": {
            "linux": ["pip install dnspython"]
        }
    },
    "dnsenum": {
        "name": "DNSenum",
        "category": "Reconnaissance",
        "description": "DNS enumeration and network mapping",
        "install": {
            "linux": ["apt-get install -y dnsenum"]
        }
    },
    "fierce": {
        "name": "Fierce",
        "category": "Reconnaissance",
        "description": "DNS subdomain scanner",
        "install": {
            "linux": ["pip install fierce"]
        }
    },
    "Knockpy": {
        "name": "Knockpy",
        "category": "Reconnaissance",
        "description": "Knockpy is a python tool to enumerate subdomains",
        "install": {
            "linux": ["pip install knockpy"]
        }
    },
    "gitGraber": {
        "name": "GitGraber",
        "category": "Reconnaissance",
        "description": "GitHub sensitive data leak detection",
        "install": {
            "linux": [
                "git clone https://github.com/hisxo/GitGraber.git",
                "cd GitGraber && pip install -r requirements.txt"
            ]
        }
    },
    "Recon-ng": {
        "name": "Recon-ng",
        "category": "Reconnaissance",
        "description": "Web reconnaissance framework",
        "install": {
            "linux": ["pip install recon-ng"]
        }
    },
    "waybackurls": {
        "name": "Waybackurls",
        "category": "Reconnaissance",
        "description": "Fetch wayback machine URLs",
        "install": {
            "linux": ["go install github.com/tomnomnom/waybackurls@latest"]
        }
    },
    "massdns": {
        "name": "MassDNS",
        "category": "Reconnaissance",
        "description": "High-performance DNS stubresolver",
        "install": {
            "linux": [
                "git clone https://github.com/blechschmidt/massdns.git",
                "cd massdns && make"
            ]
        }
    },
    
    # SCANNING TOOLS
    "Nmap": {
        "name": "Nmap",
        "category": "Scanning",
        "description": "Network mapper - port scanning and network exploration",
        "install": {
            "linux": ["apt-get install -y nmap"]
        }
    },
    "masscan": {
        "name": "Masscan",
        "category": "Scanning",
        "description": "Fast TCP port scanner",
        "install": {
            "linux": ["apt-get install -y masscan"]
        }
    },
    "httprobe": {
        "name": "Httprobe",
        "category": "Scanning",
        "description": "Take list of domains and probe for working HTTP/HTTPS",
        "install": {
            "linux": ["go install github.com/tomnomnom/httprobe@latest"]
        }
    },
    "wafw00f": {
        "name": "Wafw00f",
        "category": "Scanning",
        "description": "WAF detection tool",
        "install": {
            "linux": ["pip install wafw00f"]
        }
    },
    "whatweb": {
        "name": "WhatWeb",
        "category": "Scanning",
        "description": "Website fingerprinting tool",
        "install": {
            "linux": ["apt-get install -y whatweb"]
        }
    },
    "Nikto": {
        "name": "Nikto",
        "category": "Scanning",
        "description": "Web server scanner",
        "install": {
            "linux": ["apt-get install -y nikto"]
        }
    },
    
    # VULNERABILITY SCANNING TOOLS
    "dirb": {
        "name": "Dirb",
        "category": "Vulnerability Scanning",
        "description": "Web content discovery using dictionary-based brute force",
        "install": {
            "linux": ["apt-get install -y dirb"]
        }
    },
    "dirsearch": {
        "name": "Dirsearch",
        "category": "Vulnerability Scanning",
        "description": "Fast directory discovery tool",
        "install": {
            "linux": ["pip install dirsearch"]
        }
    },
    "gobuster": {
        "name": "Gobuster",
        "category": "Vulnerability Scanning",
        "description": "Fast directory/subdomain discovery tool",
        "install": {
            "linux": ["apt-get install -y gobuster"]
        }
    },
    "ffuf": {
        "name": "Ffuf",
        "category": "Vulnerability Scanning",
        "description": "Fast web fuzzer",
        "install": {
            "linux": ["go install github.com/ffuf/ffuf@latest"]
        }
    },
    "wfuzz": {
        "name": "Wfuzz",
        "category": "Vulnerability Scanning",
        "description": "Web application fuzzer",
        "install": {
            "linux": ["pip install wfuzz"]
        }
    },
    "sqlmap": {
        "name": "SQLMap",
        "category": "Vulnerability Scanning",
        "description": "SQL injection detection and exploitation",
        "install": {
            "linux": ["apt-get install -y sqlmap"]
        }
    },
    "commix": {
        "name": "Commix",
        "category": "Vulnerability Scanning",
        "description": "Command injection detection and exploitation",
        "install": {
            "linux": ["pip install commix"]
        }
    },
    "XSStrike": {
        "name": "XSStrike",
        "category": "Vulnerability Scanning",
        "description": "XSS detection and exploitation",
        "install": {
            "linux": [
                "git clone https://github.com/s0md3v/XSStrike.git",
                "cd XSStrike && pip install -r requirements.txt"
            ]
        }
    },
    "droopescan": {
        "name": "Droopescan",
        "category": "Vulnerability Scanning",
        "description": "Drupal scanner",
        "install": {
            "linux": ["pip install droopescan"]
        }
    },
    "joomscan": {
        "name": "Joomscan",
        "category": "Vulnerability Scanning",
        "description": "Joomla vulnerability scanner",
        "install": {
            "linux": ["apt-get install -y joomscan"]
        }
    },
    "wpscan": {
        "name": "WPScan",
        "category": "Vulnerability Scanning",
        "description": "WordPress vulnerability scanner",
        "install": {
            "linux": ["gem install wpscan"]
        }
    },
    
    # EXPLOITATION TOOLS
    "thc-hydra": {
        "name": "THC-Hydra",
        "category": "Exploitation",
        "description": "Fast network login cracker",
        "install": {
            "linux": ["apt-get install -y hydra"]
        }
    },
    "dotdotpwn": {
        "name": "Dotdotpwn",
        "category": "Exploitation",
        "description": "Directory traversal scanner",
        "install": {
            "linux": [
                "git clone https://github.com/wireghoul/dotdotpwn.git",
                "cd dotdotpwn && perl dotdotpwn.pl"
            ]
        }
    },
    
    # AWS SECURITY TOOLS
    "awscli": {
        "name": "AWS CLI",
        "category": "AWS Security",
        "description": "Amazon Web Services command line interface",
        "install": {
            "linux": ["pip install awscli"]
        }
    },
    "bucket_finder": {
        "name": "Bucket Finder",
        "category": "AWS Security",
        "description": "S3 bucket discovery tool",
        "install": {
            "linux": ["pip install bucket_finder"]
        }
    },
    "CloudFlair": {
        "name": "CloudFlair",
        "category": "AWS Security",
        "description": "Find origin IP behind CloudFlare",
        "install": {
            "linux": [
                "git clone https://github.com/christophetd/CloudFlair.git",
                "cd CloudFlair && pip install -r requirements.txt"
            ]
        }
    },
    "s3recon": {
        "name": "S3 Recon",
        "category": "AWS Security",
        "description": "S3 bucket enumeration tool",
        "install": {
            "linux": ["pip install s3-recon"]
        }
    },
    "S3Scanner": {
        "name": "S3Scanner",
        "category": "AWS Security",
        "description": "Scan S3 buckets for public access",
        "install": {
            "linux": [
                "git clone https://github.com/sa7mon/S3Scanner.git",
                "cd S3Scanner && pip install -r requirements.txt"
            ]
        }
    },
    "teh_s3_bucketeers": {
        "name": "Teh S3 Bucketeers",
        "category": "AWS Security",
        "description": "S3 enumeration and testing",
        "install": {
            "linux": ["pip install s3-bucketeers"]
        }
    },
    
    # SUBDOMAIN TAKEOVER TOOLS
    "subjack": {
        "name": "Subjack",
        "category": "Subdomain Takeover",
        "description": "Subdomain takeover detection tool",
        "install": {
            "linux": ["go install github.com/haccer/subjack@latest"]
        }
    },
    "SubOver": {
        "name": "SubOver",
        "category": "Subdomain Takeover",
        "description": "Subdomain takeover vulnerability scanner",
        "install": {
            "linux": ["go install github.com/Ice3man543/SubOver@latest"]
        }
    },
    
    # UTILITIES
    "virtual-host-discovery": {
        "name": "Virtual Host Discovery",
        "category": "Utilities",
        "description": "Virtual host enumeration tool",
        "install": {
            "linux": [
                "git clone https://github.com/AlexisAhmed/virtual-host-discovery.git",
                "cd virtual-host-discovery && chmod +x virtual-host-discovery.sh"
            ]
        }
    },
    "tmux": {
        "name": "Tmux",
        "category": "Utilities",
        "description": "Terminal multiplexer",
        "install": {
            "linux": ["apt-get install -y tmux"]
        }
    },
    "zsh": {
        "name": "Zsh",
        "category": "Utilities",
        "description": "Z Shell - interactive shell and scripting language",
        "install": {
            "linux": ["apt-get install -y zsh"]
        }
    }
}


# ═══════════════════════════════════════════════════════════════════════════════
# INSTALLER CLASS
# ═══════════════════════════════════════════════════════════════════════════════

class BugbountyInstaller:
    """Professional Bugbounty Toolkit Installer"""
    
    def __init__(self):
        self.os_type = self._detect_os()
        self.tools_db = TOOLS_INSTALL_DB
        self.installed_count = 0
        self.failed_count = 0
        self.skipped_count = 0
        self.install_log = []
    
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('clear')
    
    def _detect_os(self) -> str:
        """Detect operating system"""
        return 'linux'
    
    def print_header(self):
        """Print the beautiful header"""
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
{Colors.BRIGHT_CYAN}║{Colors.RESET}         {Colors.BRIGHT_YELLOW}{Symbols.ROCKET} Automated Setup & Installer {Symbols.ROCKET}{Colors.RESET}                  {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}                                                                              {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}  Platform: {Colors.BRIGHT_GREEN}{self.os_type.upper():<8}{Colors.RESET} | Total Tools: {Colors.BRIGHT_YELLOW}{len(self.tools_db):<3}{Colors.RESET}              {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}                                                                              {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
        """
        print(banner)
    
    def print_separator(self, title=""):
        """Print a nice separator"""
        if title:
            separator = f"\n{Colors.BRIGHT_CYAN}═══════ {Colors.BRIGHT_YELLOW}{title}{Colors.RESET} {Colors.BRIGHT_CYAN}═══════{Colors.RESET}"
        else:
            separator = f"{Colors.BRIGHT_CYAN}{'═' * 80}{Colors.RESET}"
        print(separator)
    
    def run_command(self, command: str, show_output: bool = False) -> Tuple[bool, str]:
        """Execute a shell command"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=not show_output,
                text=True,
                timeout=300,
                executable='/bin/bash'
            )
            
            return result.returncode == 0, result.stdout + result.stderr
        except subprocess.TimeoutExpired:
            return False, "Installation timeout"
        except Exception as e:
            return False, str(e)
    
    def install_tool(self, tool_id: str, tool_info: Dict) -> bool:
        """Install a single tool"""
        tool_name = tool_info['name']
        category = tool_info['category']
        
        print(f"\n{Colors.BRIGHT_CYAN}[*]{Colors.RESET} Installing {Colors.BRIGHT_YELLOW}{tool_name}{Colors.RESET} {Colors.GRAY}({category}){Colors.RESET}")
        
        install_commands = tool_info['install'].get(self.os_type, [])
        
        if not install_commands:
            print(f"  {Colors.BRIGHT_YELLOW}{Symbols.WARNING}{Colors.RESET} No installation method available for {self.os_type}")
            return False
        
        for cmd in install_commands:
            success, output = self.run_command(cmd)
            
            if not success:
                print(f"  {Colors.BRIGHT_RED}{Symbols.FAILED}{Colors.RESET} Command failed: {cmd}")
                if output and "No such file" not in output:
                    print(f"  {Colors.GRAY}Error: {output[:100]}...{Colors.RESET}")
                self.install_log.append(f"[FAILED] {tool_name}: {cmd}")
                return False
        
        print(f"  {Colors.BRIGHT_GREEN}{Symbols.SUCCESS}{Colors.RESET} Installation successful")
        self.install_log.append(f"[SUCCESS] {tool_name}")
        return True
    
    def show_menu(self):
        """Show installer menu"""
        self.clear_screen()
        self.print_header()
        
        self.print_separator("Main Menu")
        
        print(f"\n{Colors.BRIGHT_CYAN}{Symbols.ARROW} Options:{Colors.RESET}\n")
        print(f"  {Colors.BRIGHT_GREEN}[1] Install all tools{Colors.RESET}")
        print(f"  {Colors.BRIGHT_GREEN}[2] Install tools by category{Colors.RESET}")
        print(f"  {Colors.BRIGHT_GREEN}[3] Install specific tool{Colors.RESET}")
        print(f"  {Colors.BRIGHT_GREEN}[4] View tool list{Colors.RESET}")
        print(f"  {Colors.BRIGHT_GREEN}[5] Check prerequisites{Colors.RESET}")
        print(f"  {Colors.BRIGHT_RED}[0] Exit{Colors.RESET}")
        
        return input(f"\n{Colors.YELLOW}[?] Select option: {Colors.RESET}").strip()
    
    def install_all_tools(self):
        """Install all tools"""
        self.clear_screen()
        self.print_header()
        
        self.print_separator("Installing All Tools")
        
        print(f"\n{Colors.BRIGHT_YELLOW}{Symbols.WARNING} This will install {len(self.tools_db)} tools and may take a long time.{Colors.RESET}")
        confirm = input(f"\n{Colors.YELLOW}Continue? (yes/no): {Colors.RESET}").strip().lower()
        
        if confirm != 'yes':
            print(f"{Colors.BRIGHT_YELLOW}Installation cancelled.{Colors.RESET}")
            time.sleep(2)
            return
        
        print(f"\n{Colors.BRIGHT_CYAN}Starting installation...{Colors.RESET}\n")
        
        for tool_id, tool_info in self.tools_db.items():
            try:
                if self.install_tool(tool_id, tool_info):
                    self.installed_count += 1
                else:
                    self.failed_count += 1
            except KeyboardInterrupt:
                print(f"\n{Colors.BRIGHT_YELLOW}{Symbols.WARNING} Installation interrupted by user{Colors.RESET}")
                break
            except Exception as e:
                print(f"  {Colors.BRIGHT_RED}{Symbols.FAILED} Error: {str(e)}{Colors.RESET}")
                self.failed_count += 1
        
        self.show_installation_summary()
    
    def install_by_category(self):
        """Install tools by category"""
        self.clear_screen()
        self.print_header()
        
        self.print_separator("Select Category")
        
        # Get unique categories
        categories = {}
        for tool_id, tool_info in self.tools_db.items():
            cat = tool_info['category']
            if cat not in categories:
                categories[cat] = []
            categories[cat].append((tool_id, tool_info))
        
        # Display categories
        print(f"\n{Colors.BRIGHT_CYAN}{Symbols.ARROW} Available categories:{Colors.RESET}\n")
        cat_list = list(categories.keys())
        for idx, cat in enumerate(cat_list, 1):
            count = len(categories[cat])
            print(f"  {Colors.BRIGHT_GREEN}[{idx}] {cat} ({count} tools){Colors.RESET}")
        
        print(f"  {Colors.BRIGHT_RED}[0] Back{Colors.RESET}\n")
        
        try:
            choice = int(input(f"{Colors.YELLOW}[?] Select category: {Colors.RESET}"))
            
            if choice == 0:
                return
            
            if 1 <= choice <= len(cat_list):
                selected_cat = cat_list[choice - 1]
                self.print_separator(f"Installing {selected_cat}")
                
                for tool_id, tool_info in categories[selected_cat]:
                    try:
                        if self.install_tool(tool_id, tool_info):
                            self.installed_count += 1
                        else:
                            self.failed_count += 1
                    except KeyboardInterrupt:
                        print(f"\n{Colors.BRIGHT_YELLOW}{Symbols.WARNING} Installation interrupted{Colors.RESET}")
                        break
                    except Exception as e:
                        print(f"  {Colors.BRIGHT_RED}{Symbols.FAILED} Error: {str(e)}{Colors.RESET}")
                        self.failed_count += 1
                
                self.show_installation_summary()
        except ValueError:
            print(f"{Colors.BRIGHT_RED}Invalid input{Colors.RESET}")
            time.sleep(2)
    
    def install_specific_tool(self):
        """Install a specific tool"""
        self.clear_screen()
        self.print_header()
        
        self.print_separator("Select Tool to Install")
        
        print(f"\n{Colors.BRIGHT_CYAN}{Symbols.ARROW} Available tools:{Colors.RESET}\n")
        
        tool_list = list(self.tools_db.items())
        for idx, (tool_id, tool_info) in enumerate(tool_list, 1):
            print(f"  {Colors.BRIGHT_GREEN}[{idx:2d}] {tool_info['name']:<20} {Colors.GRAY}({tool_info['category']}){Colors.RESET}")
        
        print(f"\n  {Colors.BRIGHT_RED}[0] Back{Colors.RESET}\n")
        
        try:
            choice = int(input(f"{Colors.YELLOW}[?] Select tool: {Colors.RESET}"))
            
            if choice == 0:
                return
            
            if 1 <= choice <= len(tool_list):
                tool_id, tool_info = tool_list[choice - 1]
                self.print_separator(f"Installing {tool_info['name']}")
                
                if self.install_tool(tool_id, tool_info):
                    self.installed_count += 1
                    print(f"\n{Colors.BRIGHT_GREEN}{Symbols.SUCCESS} Tool installed successfully{Colors.RESET}")
                else:
                    self.failed_count += 1
                    print(f"\n{Colors.BRIGHT_RED}{Symbols.FAILED} Tool installation failed{Colors.RESET}")
                
                input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")
        except ValueError:
            print(f"{Colors.BRIGHT_RED}Invalid input{Colors.RESET}")
            time.sleep(2)
    
    def view_tool_list(self):
        """View all available tools"""
        self.clear_screen()
        self.print_header()
        
        self.print_separator("All Available Tools")
        
        categories = {}
        for tool_id, tool_info in self.tools_db.items():
            cat = tool_info['category']
            if cat not in categories:
                categories[cat] = []
            categories[cat].append((tool_id, tool_info))
        
        for cat, tools in sorted(categories.items()):
            print(f"\n{Colors.BRIGHT_YELLOW}{cat}:{Colors.RESET}")
            for tool_id, tool_info in tools:
                print(f"  {Colors.BRIGHT_GREEN}●{Colors.RESET} {tool_info['name']:<20} {Colors.GRAY}- {tool_info['description']}{Colors.RESET}")
        
        self.print_separator()
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")
    
    def check_prerequisites(self):
        """Check if prerequisites are installed"""
        self.clear_screen()
        self.print_header()
        
        self.print_separator("Checking Prerequisites")
        
        prerequisites = {
            "pip": "Python package manager",
            "git": "Version control system",
            "go": "Go programming language",
        }
        
        if self.os_type != 'windows':
            prerequisites["curl"] = "URL fetcher"
        
        print(f"\n{Colors.BRIGHT_CYAN}{Symbols.ARROW} Checking prerequisites:{Colors.RESET}\n")
        
        all_good = True
        for tool, description in prerequisites.items():
            if shutil.which(tool):
                print(f"  {Colors.BRIGHT_GREEN}{Symbols.SUCCESS}{Colors.RESET} {tool:<10} - {description}")
            else:
                print(f"  {Colors.BRIGHT_RED}{Symbols.FAILED}{Colors.RESET} {tool:<10} - {description}")
                all_good = False
        
        print()
        if all_good:
            print(f"{Colors.BRIGHT_GREEN}All prerequisites are installed!{Colors.RESET}")
        else:
            print(f"{Colors.BRIGHT_YELLOW}Some prerequisites are missing. Install them manually for best results.{Colors.RESET}")
            
            if self.os_type == 'linux':
                print(f"\n{Colors.CYAN}Install missing tools with:{Colors.RESET}")
                print(f"  sudo apt-get update && sudo apt-get install -y python3-pip git curl")
            elif self.os_type == 'macos':
                print(f"\n{Colors.CYAN}Install missing tools with:{Colors.RESET}")
                print(f"  brew install python git curl")
            elif self.os_type == 'windows':
                print(f"\n{Colors.CYAN}Install missing tools with:{Colors.RESET}")
                print(f"  choco install python git")
        
        self.print_separator()
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")
    
    def show_installation_summary(self):
        """Show installation summary"""
        self.print_separator("Installation Summary")
        
        total = len(self.tools_db)
        print(f"\n{Colors.BRIGHT_GREEN}{Symbols.SUCCESS} Installed: {self.installed_count}/{total}{Colors.RESET}")
        print(f"{Colors.BRIGHT_RED}{Symbols.FAILED} Failed: {self.failed_count}/{total}{Colors.RESET}")
        print(f"{Colors.BRIGHT_YELLOW}{Symbols.WARNING} Skipped: {self.skipped_count}/{total}{Colors.RESET}")
        
        if self.install_log:
            print(f"\n{Colors.BRIGHT_CYAN}Installation Log:{Colors.RESET}")
            for log_entry in self.install_log[-10:]:  # Show last 10
                print(f"  {log_entry}")
        
        self.print_separator()
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")
    
    def run(self):
        """Main installer loop"""
        while True:
            choice = self.show_menu()
            
            if choice == "1":
                self.install_all_tools()
            elif choice == "2":
                self.install_by_category()
            elif choice == "3":
                self.install_specific_tool()
            elif choice == "4":
                self.view_tool_list()
            elif choice == "5":
                self.check_prerequisites()
            elif choice == "0":
                self.exit_installer()
            else:
                print(f"{Colors.BRIGHT_RED}Invalid option{Colors.RESET}")
                time.sleep(1)
    
    def exit_installer(self):
        """Exit the installer"""
        self.clear_screen()
        
        exit_banner = f"""
{Colors.BRIGHT_CYAN}╔══════════════════════════════════════════════════════════════════════════════╗{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}                                                                              {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}              {Colors.BRIGHT_GREEN}Thank you for using Nobody's BugBounty Installer!{Colors.RESET}              {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}                                                                              {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}          {Colors.BRIGHT_YELLOW}Next step: Run 'python BugbountyToolkit.py' to launch the toolkit{Colors.RESET}        {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}║{Colors.RESET}                                                                              {Colors.BRIGHT_CYAN}║{Colors.RESET}
{Colors.BRIGHT_CYAN}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
        """
        print(exit_banner)
        sys.exit(0)


# ═══════════════════════════════════════════════════════════════════════════════
# ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    installer = BugbountyInstaller()
    installer.run()
