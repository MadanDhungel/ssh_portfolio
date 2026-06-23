# ANSI Color Codes for Terminal
class Colors:
    # Text Colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # Background Colors
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_BLUE = '\033[44m'
    BG_CYAN = '\033[46m'
    
    # Styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    
    # Reset
    RESET = '\033[0m'

def colored(text, color):
    """Apply color to text"""
    return f"{color}{text}{Colors.RESET}"

def bold(text):
    """Make text bold"""
    return f"{Colors.BOLD}{text}{Colors.RESET}"

def title(text):
    """Format as title"""
    return f"{Colors.CYAN}{Colors.BOLD}{text}{Colors.RESET}"

def section(text):
    """Format as section header"""
    return f"{Colors.GREEN}{Colors.BOLD}{text}{Colors.RESET}"

def highlight(text):
    """Highlight text"""
    return f"{Colors.YELLOW}{text}{Colors.RESET}"

def skill_item(text):
    """Format skill item"""
    return f"{Colors.BLUE}▸{Colors.RESET} {text}"

def section_header(text):
    """Format as decorative section header"""
    return f"{Colors.CYAN}{Colors.BOLD}{text}{Colors.RESET}"

def divider():
    """Return a decorative divider"""
    return f"{Colors.CYAN}{'─' * 78}{Colors.RESET}"

def top_divider():
    """Return top border"""
    return f"{Colors.CYAN}{Colors.BOLD}╭{'─' * 76}╮{Colors.RESET}"

def bottom_divider():
    """Return bottom border"""
    return f"{Colors.CYAN}{Colors.BOLD}╰{'─' * 76}╯{Colors.RESET}"

def label(text):
    """Format as label with icon"""
    return f"{Colors.GREEN}▻{Colors.RESET} {Colors.BOLD}{text}{Colors.RESET}"

def success(text):
    """Format success message"""
    return f"{Colors.GREEN}✓ {text}{Colors.RESET}"

def error(text):
    """Format error message"""
    return f"{Colors.RED}✗ {text}{Colors.RESET}"

def keyword(text):
    """Highlight keyword in bold yellow"""
    return f"{Colors.YELLOW}{Colors.BOLD}{text}{Colors.RESET}"

def tech_badge(text):
    """Format as technology badge"""
    return f"{Colors.BLUE}{Colors.BOLD}[{text}]{Colors.RESET}"

def achievement(text):
    """Format achievement with star"""
    return f"{Colors.YELLOW}★{Colors.RESET} {text}"

def position(title, company, dates):
    """Format job position with highlighting"""
    return f"{Colors.GREEN}{Colors.BOLD}{title}{Colors.RESET} @ {Colors.CYAN}{company}{Colors.RESET} {Colors.DIM}({dates}){Colors.RESET}"

def technology(text):
    """Highlight technology name"""
    return f"{Colors.MAGENTA}{text}{Colors.RESET}"

def value_prop(text):
    """Highlight value proposition"""
    return f"{Colors.GREEN}{Colors.BOLD}{text}{Colors.RESET}"

def metric(value):
    """Highlight metric/number"""
    return f"{Colors.YELLOW}{Colors.BOLD}{value}{Colors.RESET}"

def box_section(title, content):
    """Create a boxed section with title"""
    width = 80
    return f"""{Colors.CYAN}{Colors.BOLD}┌{'─' * (width - 2)}┐{Colors.RESET}
{Colors.CYAN}{Colors.BOLD}│{Colors.RESET} {Colors.YELLOW}{title:<{width-4}}{Colors.CYAN}{Colors.BOLD}│{Colors.RESET}
{Colors.CYAN}{Colors.BOLD}├{'─' * (width - 2)}┤{Colors.RESET}
{content}
{Colors.CYAN}{Colors.BOLD}└{'─' * (width - 2)}┘{Colors.RESET}"""
