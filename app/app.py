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
║            {Colors.YELLOW}🚀  DEVOPS ENGINEER - COMPLETE PORTFOLIO  🚀{Colors.CYAN}            ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
""")

def help_menu():
    print(f"""{Colors.CYAN}{Colors.BOLD}
Available commands:{Colors.RESET}
  {Colors.GREEN}0{Colors.RESET}. all         - View complete portfolio
  {Colors.YELLOW}1{Colors.RESET}. about       - Who am I
  {Colors.BLUE}2{Colors.RESET}. skills      - My technical stack
  {Colors.MAGENTA}3{Colors.RESET}. projects    - My work & experience
  {Colors.RED}4{Colors.RESET}. contact     - How to reach me
  {Colors.CYAN}5{Colors.RESET}. certs       - Certifications & achievements
  {Colors.GREEN}6{Colors.RESET}. clear       - Clear screen
  {Colors.BOLD}help{Colors.RESET}           - Show commands
  {Colors.BOLD}exit{Colors.RESET}           - Exit session
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
    user = input(f"{Colors.CYAN}login as:{Colors.RESET} ")
    print(f"{Colors.GREEN}Authenticating {Colors.YELLOW}{user}{Colors.GREEN} ...{Colors.RESET}")
    time.sleep(1)
    print(f"{Colors.GREEN}✓ Access granted.{Colors.RESET}\n")
    help_menu()

    while True:
        cmd = input(f"{Colors.GREEN}{user}{Colors.RESET}@{Colors.CYAN}portfolio{Colors.RESET}:~{Colors.YELLOW}${Colors.RESET} ").strip().lower()
        
        if cmd in COMMAND_MAP:
            cmd = COMMAND_MAP[cmd]

        if cmd == "all":
            print(PORTFOLIO["all"])
        elif cmd == "about":
            print(PORTFOLIO["about"])
        elif cmd == "skills":
            print(PORTFOLIO["skills"])
        elif cmd == "projects":
            print(PORTFOLIO["projects"])
        elif cmd == "contact":
            print(PORTFOLIO["contact"])
        elif cmd == "certifications":
            print(PORTFOLIO["certifications"])
        elif cmd == "help":
            help_menu()
        elif cmd == "clear":
            clear()
        elif cmd == "exit":
            print(f"{Colors.RED}Session terminated.{Colors.RESET}")
            break
        else:
            print(f"{Colors.RED}Command not found. Type 'help'.{Colors.RESET}")

if __name__ == "__main__":
    main()
