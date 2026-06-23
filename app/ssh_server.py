import asyncio
import os
import sys

import asyncssh
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

HELP_TEXT = f"""{Colors.CYAN}{Colors.BOLD}
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
"""

COMMAND_MAP = {
    "0": "all",
    "1": "about",
    "2": "skills",
    "3": "projects",
    "4": "contact",
    "5": "certifications",
    "6": "clear",
}

HOST_KEY_PATH = os.environ.get("SSH_HOST_KEY_PATH", "ssh_host_key")
LISTEN_PORT = int(os.environ.get("SSH_PORT", "2222"))


def ensure_host_key(path: str) -> None:
    """Generate a host key on first run if one doesn't already exist."""
    if not os.path.exists(path):
        key = asyncssh.generate_private_key("ssh-ed25519")
        key.write_private_key(path)


def to_term(text: str) -> str:
    """Convert plain '\n' line endings to the '\r\n' a terminal expects."""
    return text.replace("\n", "\r\n")


class PortfolioSSHServer(asyncssh.SSHServer):
    def connection_made(self, conn: asyncssh.SSHServerConnection) -> None:
        peer = conn.get_extra_info("peername")
        print(f"[+] Connection from {peer}")

    def connection_lost(self, exc: Exception | None) -> None:
        if exc:
            print(f"[-] Connection lost: {exc}")
        else:
            print("[-] Connection closed")

    def begin_auth(self, username: str) -> bool:
        # Open access: this is a public portfolio, not a real shell account,
        # so no password/key is required to log in and look around.
        return False


async def handle_client(process: asyncssh.SSHServerProcess) -> None:
    username = process.get_extra_info("username") or "guest"

    welcome = f"""{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║            {Colors.YELLOW}🚀  DEVOPS ENGINEER - COMPLETE PORTFOLIO  🚀{Colors.CYAN}            ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    
    process.stdout.write(to_term(welcome))
    process.stdout.write(to_term(f"{Colors.GREEN}Authenticating {Colors.YELLOW}{username}{Colors.GREEN} ...{Colors.RESET}\n"))
    await asyncio.sleep(0.6)
    process.stdout.write(to_term(f"{Colors.GREEN}✓ Access granted.{Colors.RESET}\n\n"))
    process.stdout.write(to_term(HELP_TEXT))

    try:
        while True:
            prompt = f"{Colors.GREEN}{username}{Colors.RESET}@{Colors.CYAN}portfolio{Colors.RESET}:~{Colors.YELLOW}${Colors.RESET} "
            process.stdout.write(to_term(f"\r\n{prompt}"))
            line = await process.stdin.readline()
            if not line:
                break

            cmd = line.strip().lower()

            if cmd == "":
                continue
            elif cmd in COMMAND_MAP:
                cmd = COMMAND_MAP[cmd]
            
            if cmd == "all":
                process.stdout.write(to_term(PORTFOLIO["all"]))
            elif cmd == "about":
                process.stdout.write(to_term(PORTFOLIO["about"]))
            elif cmd == "skills":
                process.stdout.write(to_term(PORTFOLIO["skills"]))
            elif cmd == "projects":
                process.stdout.write(to_term(PORTFOLIO["projects"]))
            elif cmd == "contact":
                process.stdout.write(to_term(PORTFOLIO["contact"]))
            elif cmd == "certifications":
                process.stdout.write(to_term(PORTFOLIO["certifications"]))
            elif cmd == "help":
                process.stdout.write(to_term(HELP_TEXT))
            elif cmd == "clear":
                process.stdout.write("\033[2J\033[H")
            elif cmd == "exit":
                process.stdout.write(to_term(f"{Colors.RED}Session terminated.{Colors.RESET}\n"))
                break
            else:
                process.stdout.write(to_term(f"{Colors.RED}Command not found. Type 'help'.{Colors.RESET}\n"))
    except asyncssh.TerminalSizeChanged:
        pass
    finally:
        process.exit(0)


async def start_server() -> None:
    ensure_host_key(HOST_KEY_PATH)
    await asyncssh.create_server(
        PortfolioSSHServer,
        "",
        LISTEN_PORT,
        server_host_keys=[HOST_KEY_PATH],
        process_factory=handle_client,
    )
    print(f"[*] SSH portfolio server listening on port {LISTEN_PORT}")


async def main() -> None:
    await start_server()
    await asyncio.Future()  # run forever


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (OSError, asyncssh.Error) as exc:
        sys.exit(f"Error starting server: {exc}")
