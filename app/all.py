from about import ABOUT
from skills import SKILLS
from projects import PROJECTS
from contact import CONTACT
from certifications import CERTIFICATIONS
from colors import Colors, title, section, bold, highlight, skill_item
from ascii_art import DEVOPS_BANNER, SECTION_DIVIDER, ASCII_DOCKER, ASCII_KUBERNETES, ASCII_AWS, ASCII_TERRAFORM, ASCII_GITHUB

ALL = f"""{DEVOPS_BANNER}

{Colors.CYAN}{Colors.BOLD}📋 ABOUT ME{Colors.RESET}
{Colors.CYAN}{'─' * 78}{Colors.RESET}
{ABOUT}

{Colors.CYAN}{Colors.BOLD}🛠️  TECHNICAL SKILLS{Colors.RESET}
{Colors.CYAN}{'─' * 78}{Colors.RESET}
{SKILLS}

{Colors.CYAN}{Colors.BOLD}🔑 KEY TECHNOLOGIES{Colors.RESET}
{Colors.CYAN}{'─' * 78}{Colors.RESET}
{ASCII_DOCKER}   {ASCII_KUBERNETES}   {ASCII_AWS}
{ASCII_TERRAFORM}   {ASCII_GITHUB}

{Colors.CYAN}{Colors.BOLD}💼 PROFESSIONAL EXPERIENCE{Colors.RESET}
{Colors.CYAN}{'─' * 78}{Colors.RESET}
{PROJECTS}

{Colors.CYAN}{Colors.BOLD}🎓 CERTIFICATIONS & EDUCATION{Colors.RESET}
{Colors.CYAN}{'─' * 78}{Colors.RESET}
{CERTIFICATIONS}

{Colors.CYAN}{Colors.BOLD}📧 CONTACT INFORMATION{Colors.RESET}
{Colors.CYAN}{'─' * 78}{Colors.RESET}
{CONTACT}

{Colors.GREEN}{Colors.BOLD}✨ Type 'help' for commands or select a specific section.{Colors.RESET}
"""
