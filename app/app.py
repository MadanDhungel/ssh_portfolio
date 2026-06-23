import time
import sys
from about import ABOUT
from skills import SKILLS
from projects import PROJECTS
from contact import CONTACT
from certifications import CERTIFICATIONS
from all import ALL
from colors import Colors

PORTFOLIO = {
    "about": ABOUT,
    "skills": SKILLS,
    "projects": PROJECTS,
    "contact": CONTACT,
    "certifications": CERTIFICATIONS,
    "all": ALL,
}

def banner():
    print(f"""{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║         {Colors.YELLOW}🚀  DEVOPS ENGINEER - COMPLETE PORTFOLIO  🚀{Colors.CYAN}         ║
║                                                                          ║
║              {Colors.GREEN}☁️  AWS • 🐳 Docker • ☸ Kubernetes • 🔄 CI/CD{Colors.CYAN}      ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}""")
    print()

def help_menu():
    print(f"""
{Colors.CYAN}{Colors.BOLD}╭──────────────────────────────────────────────────────╮{Colors.RESET}
{Colors.CYAN}{Colors.BOLD}│{Colors.RESET} {Colors.YELLOW}{Colors.BOLD}Available Commands{Colors.RESET}{Colors.CYAN}{Colors.BOLD}                               │{Colors.RESET}
{Colors.CYAN}{Colors.BOLD}├──────────────────────────────────────────────────────┤{Colors.RESET}
{Colors.CYAN}{Colors.BOLD}│{Colors.RESET} {Colors.GREEN}0{Colors.RESET}  all        🎯 View complete portfolio{Colors.CYAN}{Colors.BOLD}         │{Colors.RESET}
{Colors.CYAN}{Colors.BOLD}│{Colors.RESET} {Colors.YELLOW}1{Colors.RESET}  about      👤 Who am I{Colors.CYAN}{Colors.BOLD}                    │{Colors.RESET}
{Colors.CYAN}{Colors.BOLD}│{Colors.RESET} {Colors.BLUE}2{Colors.RESET}  skills     🛠️  My technical stack{Colors.CYAN}{Colors.BOLD}           │{Colors.RESET}
{Colors.CYAN}{Colors.BOLD}│{Colors.RESET} {Colors.MAGENTA}3{Colors.RESET}  projects   💼 My work & experience{Colors.CYAN}{Colors.BOLD}        │{Colors.RESET}
{Colors.CYAN}{Colors.BOLD}│{Colors.RESET} {Colors.RED}4{Colors.RESET}  contact    📧 How to reach me{Colors.CYAN}{Colors.BOLD}             │{Colors.RESET}
{Colors.CYAN}{Colors.BOLD}│{Colors.RESET} {Colors.CYAN}5{Colors.RESET}  certs      🎓 Certifications & achievements{Colors.CYAN}{Colors.BOLD} │{Colors.RESET}
{Colors.CYAN}{Colors.BOLD}│{Colors.RESET} {Colors.GREEN}6{Colors.RESET}  clear      🗑️  Clear screen{Colors.CYAN}{Colors.BOLD}               │{Colors.RESET}
{Colors.CYAN}{Colors.BOLD}│{Colors.RESET} {Colors.BOLD}help{Colors.RESET}       ❓ Show this help menu{Colors.CYAN}{Colors.BOLD}            │{Colors.RESET}
{Colors.CYAN}{Colors.BOLD}│{Colors.RESET} {Colors.BOLD}exit{Colors.RESET}       👋 Exit session{Colors.CYAN}{Colors.BOLD}                   │{Colors.RESET}
{Colors.CYAN}{Colors.BOLD}╰──────────────────────────────────────────────────────╯{Colors.RESET}
""")

def clear():
    print("\033c", end="")

COMMAND_MAP = {
    "0": "all",
    "1": "about",
    "2": "skills",
    "3": "projects",
    "4": "contact",
    "5": "certifications",
    "6": "clear",
}

def main():
    banner()
    
    # Login prompt with styled input
    user = input(f"{Colors.CYAN}🔐 login as:{Colors.RESET} ")
    print()
    
    # Authentication message with animated dots
    print(f"{Colors.GREEN}⏳ Authenticating {Colors.YELLOW}{user}{Colors.GREEN}...{Colors.RESET}", end="", flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print()
    print()
    
    # Success message
    print(f"{Colors.GREEN}✓ Access granted! Welcome to the portfolio.{Colors.RESET}\n")
    time.sleep(0.5)
    help_menu()

    while True:
        cmd = input(f"{Colors.GREEN}{user}{Colors.RESET}@{Colors.CYAN}portfolio{Colors.RESET}:~{Colors.YELLOW}${Colors.RESET} ").strip().lower()
        
        if not cmd:
            continue
        
        if cmd in COMMAND_MAP:
            cmd = COMMAND_MAP[cmd]

        if cmd == "all":
            print()
            print(PORTFOLIO["all"])
            print()
        elif cmd == "about":
            print()
            print(f"{Colors.CYAN}{Colors.BOLD}📋 ABOUT ME{Colors.RESET}")
            print(f"{Colors.CYAN}{'─' * 78}{Colors.RESET}")
            print(PORTFOLIO["about"])
            print()
        elif cmd == "skills":
            print()
            print(f"{Colors.CYAN}{Colors.BOLD}🛠️  TECHNICAL SKILLS{Colors.RESET}")
            print(f"{Colors.CYAN}{'─' * 78}{Colors.RESET}")
            print(PORTFOLIO["skills"])
            print()
        elif cmd == "projects":
            print()
            print(f"{Colors.CYAN}{Colors.BOLD}💼 PROFESSIONAL EXPERIENCE{Colors.RESET}")
            print(f"{Colors.CYAN}{'─' * 78}{Colors.RESET}")
            print(PORTFOLIO["projects"])
            print()
        elif cmd == "contact":
            print()
            print(f"{Colors.CYAN}{Colors.BOLD}📧 CONTACT INFORMATION{Colors.RESET}")
            print(f"{Colors.CYAN}{'─' * 78}{Colors.RESET}")
            print(PORTFOLIO["contact"])
            print()
        elif cmd == "certifications":
            print()
            print(f"{Colors.CYAN}{Colors.BOLD}🎓 CERTIFICATIONS & ACHIEVEMENTS{Colors.RESET}")
            print(f"{Colors.CYAN}{'─' * 78}{Colors.RESET}")
            print(PORTFOLIO["certifications"])
            print()
        elif cmd == "help":
            help_menu()
        elif cmd == "clear":
            clear()
        elif cmd == "exit":
            print()
            print(f"{Colors.YELLOW}👋 Thank you for visiting my portfolio!{Colors.RESET}")
            print(f"{Colors.RED}❌ Session terminated.{Colors.RESET}")
            print()
            break
        else:
            print(f"{Colors.RED}✗ Command not found. Type '{Colors.BOLD}help{Colors.RESET}{Colors.RED}' for available commands.{Colors.RESET}")

if __name__ == "__main__":
    main()
