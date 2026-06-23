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
    return f"{Colors.BLUE}•{Colors.RESET} {text}"
