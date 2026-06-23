from colors import Colors

# ASCII Art for Tools - Enhanced with better visuals
ASCII_DOCKER = f"""{Colors.BLUE}{Colors.BOLD}
     🐳  DOCKER
   ╭───────────╮
   │ ◻ ◻ ◻   │
   │ ◻ ◻ ◻   │
   │ ◻ ◻ ◻   │
   ╰───────────╯
{Colors.RESET}"""

ASCII_KUBERNETES = f"""{Colors.BLUE}{Colors.BOLD}
    ☸  KUBERNETES
   ╔───────────╗
   ║ ✦ ✦ ✦  ║
   ║ ✦ ☸ ✦  ║
   ║ ✦ ✦ ✦  ║
   ╚───────────╝
{Colors.RESET}"""

ASCII_AWS = f"""{Colors.YELLOW}{Colors.BOLD}
     ☁️   AWS
   ╭───────────╮
   │ ▲ ▲ ▲   │
   │ ▲ ▲ ▲   │
   │ ▲ ▲ ▲   │
   ╰───────────╯
{Colors.RESET}"""

ASCII_TERRAFORM = f"""{Colors.MAGENTA}{Colors.BOLD}
    🌍  TERRAFORM
   ╔───────────╗
   ║ ◆ ◆ ◆  ║
   ║ ◆ ◆ ◆  ║
   ║ ◆ ◆ ◆  ║
   ╚───────────╝
{Colors.RESET}"""

ASCII_GITHUB = f"""{Colors.WHITE}{Colors.BOLD}
     🐙  GITHUB
   ╔───────────╗
   ║ ◉─◉─◉  ║
   ║ │ ◉ │  ║
   ║ ◉─◉─◉  ║
   ╚───────────╝
{Colors.RESET}"""

ASCII_JENKINS = f"""{Colors.RED}{Colors.BOLD}
    🔴  JENKINS
   ╔───────────╗
   ║ ◆   ◆  ║
   ║   ◆    ║
   ║ ◆   ◆  ║
   ╚───────────╝
{Colors.RESET}"""

ASCII_PROMETHEUS = f"""{Colors.YELLOW}{Colors.BOLD}
    📊  PROMETHEUS
   ╔───────────╗
   ║ ◎ ◎ ◎  ║
   ║ ◎ ◉ ◎  ║
   ║ ◎ ◎ ◎  ║
   ╚───────────╝
{Colors.RESET}"""

ASCII_GRAFANA = f"""{Colors.MAGENTA}{Colors.BOLD}
    📈  GRAFANA
   ╔───────────╗
   ║ ◈ ◈ ◈  ║
   ║ ◈ ◆ ◈  ║
   ║ ◈ ◈ ◈  ║
   ╚───────────╝
{Colors.RESET}"""

ASCII_LINUX = f"""{Colors.YELLOW}{Colors.BOLD}
     🐧  LINUX
   ╔───────────╗
   ║ ▓ ▓ ▓  ║
   ║ ▓ ▓ ▓  ║
   ║ ▓ ▓ ▓  ║
   ╚───────────╝
{Colors.RESET}"""

ASCII_PYTHON = f"""{Colors.BLUE}{Colors.BOLD}
     🐍  PYTHON
   ╔───────────╗
   ║ ● ● ●  ║
   ║ ● ○ ●  ║
   ║ ● ● ●  ║
   ╚───────────╝
{Colors.RESET}"""

# Tool icons map
TOOLS_ICONS = {
    "Docker": ASCII_DOCKER,
    "Kubernetes": ASCII_KUBERNETES,
    "AWS": ASCII_AWS,
    "Terraform": ASCII_TERRAFORM,
    "GitHub": ASCII_GITHUB,
    "Jenkins": ASCII_JENKINS,
    "Prometheus": ASCII_PROMETHEUS,
    "Grafana": ASCII_GRAFANA,
    "Linux": ASCII_LINUX,
    "Python": ASCII_PYTHON,
}

DEVOPS_BANNER = f"""{Colors.CYAN}{Colors.BOLD}
╔═════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                             ║
║{Colors.YELLOW}🚀  DEVOPS ENGINEER - COMPLETE PORTFOLIO  🚀{Colors.CYAN}                    ║
║                                                                                             ║
║{Colors.GREEN}🏆 AWS Certified • 🐳 Container Expert • ☸ K8s Master{Colors.CYAN}            ║
║{Colors.MAGENTA}🔐 Infrastructure as Code • 🔄 CI/CD{Colors.CYAN}                           ║
║                                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}"""

SECTION_DIVIDER = f"{Colors.CYAN}{'═' * 80}{Colors.RESET}"

# Additional visual elements
TOP_DIVIDER = f"{Colors.CYAN}{Colors.BOLD}╭{'─' * 78}╮{Colors.RESET}"
BOTTOM_DIVIDER = f"{Colors.CYAN}{Colors.BOLD}╰{'─' * 78}╯{Colors.RESET}"
SUBSECTION_DIVIDER = f"{Colors.CYAN}{'─' * 80}{Colors.RESET}"
DECORATION_LINE = f"{Colors.CYAN}{Colors.BOLD}{'▓' * 80}{Colors.RESET}"

# Decorative separators
STAR_DIVIDER = f"{Colors.YELLOW}{'★ ' * 40}{Colors.RESET}"
DOT_DIVIDER = f"{Colors.BLUE}{'• ' * 40}{Colors.RESET}"
