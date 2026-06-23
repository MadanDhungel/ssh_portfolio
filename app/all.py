from about import ABOUT
from skills import SKILLS
from projects import PROJECTS
from contact import CONTACT
from certifications import CERTIFICATIONS
from colors import Colors, title, section, bold, highlight, skill_item
from ascii_art import DEVOPS_BANNER, SECTION_DIVIDER, ASCII_DOCKER, ASCII_KUBERNETES, ASCII_AWS, ASCII_TERRAFORM, ASCII_GITHUB

ALL = f"""{DEVOPS_BANNER}

{section('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ABOUT ME ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{ABOUT}

{section('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ TECHNICAL SKILLS ━━━━━━━━━━━━━━━━━━━━━━━━━')}
{SKILLS}

{Colors.CYAN}Key Technologies:{Colors.RESET}
{ASCII_DOCKER}   {ASCII_KUBERNETES}   {ASCII_AWS}
{ASCII_TERRAFORM}   {ASCII_GITHUB}

{section('━━━━━━━━━━━━━━━━━━━━━━━ PROFESSIONAL EXPERIENCE ━━━━━━━━━━━━━━━━━━━━')}
{PROJECTS}

{section('━━━━━━━━━━━━━━━━━━━━━━ CERTIFICATIONS & EDUCATION ━━━━━━━━━━━━━━━━━━━')}
{CERTIFICATIONS}

{section('━━━━━━━━━━━━━━━━━━━━━━ CONTACT INFORMATION ━━━━━━━━━━━━━━━━━━━━━━')}
{CONTACT}

{Colors.GREEN}{Colors.BOLD}Type 'help' for commands or select a specific section.{Colors.RESET}
"""
