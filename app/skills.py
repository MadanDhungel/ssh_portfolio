from colors import Colors, bold, section, skill_item

SKILLS = f"""{Colors.GREEN}{Colors.BOLD}DevOps & Automation:{Colors.RESET}
{skill_item(Colors.CYAN + 'Version Control:' + Colors.RESET + ' Git, GitHub')}
{skill_item(Colors.CYAN + 'Cloud Platforms:' + Colors.RESET + ' AWS, OVHcloud')}
{skill_item(Colors.CYAN + 'Infrastructure as Code:' + Colors.RESET + ' Terraform, Ansible')}
{skill_item(Colors.CYAN + 'Containers & Orchestration:' + Colors.RESET + ' Docker, Kubernetes, AWS ECS, OVH Managed Kubernetes')}
{skill_item(Colors.CYAN + 'CI/CD & GitOps:' + Colors.RESET + ' GitHub Actions, Jenkins, GitLab CI/CD, Argo CD')}
{skill_item(Colors.CYAN + 'Monitoring & Logging:' + Colors.RESET + ' Prometheus, Grafana, AWS CloudWatch')}
{skill_item(Colors.CYAN + 'Scripting & Automation:' + Colors.RESET + ' Python, Bash')}

{Colors.GREEN}{Colors.BOLD}Cloud & Virtualization:{Colors.RESET}
{skill_item(Colors.YELLOW + 'OVHcloud:' + Colors.RESET + ' Managed Kubernetes, Object Storage, Virtual Machines, IAM')}
{skill_item(Colors.YELLOW + 'AWS:' + Colors.RESET + ' EC2, S3, Auto Scaling, Load Balancing, ECS, EKS')}
{skill_item(Colors.YELLOW + 'Platforms:' + Colors.RESET + ' VMware ESXi, Hyper-V, VirtualBox, Proxmox')}

{Colors.GREEN}{Colors.BOLD}System Administration:{Colors.RESET}
{skill_item(Colors.MAGENTA + 'Linux:' + Colors.RESET + ' Ubuntu, CentOS, RHEL')}
{skill_item(Colors.MAGENTA + 'Windows Server:' + Colors.RESET + ' Active Directory, Group Policy, DNS, DHCP')}
{skill_item(Colors.MAGENTA + 'Backup & Disaster Recovery,' + Colors.RESET + ' High Availability Solutions')}

{Colors.GREEN}{Colors.BOLD}Networking & Security:{Colors.RESET}
{skill_item(Colors.RED + 'Network Devices:' + Colors.RESET + ' Cisco, Juniper, MikroTik')}
{skill_item(Colors.RED + 'Services:' + Colors.RESET + ' DNS, DHCP, Load Balancers, Proxy Servers')}
{skill_item(Colors.RED + 'Firewalls & Security:' + Colors.RESET + ' Fortinet, Sophos')}
{skill_item(Colors.RED + 'Monitoring:' + Colors.RESET + ' Zabbix, Nagios, Cacti, SmokePing')}

{Colors.GREEN}{Colors.BOLD}Databases & Development:{Colors.RESET}
{skill_item(Colors.BLUE + 'Databases:' + Colors.RESET + ' MySQL, PostgreSQL')}
{skill_item(Colors.BLUE + 'Methodologies:' + Colors.RESET + ' SDLC, Agile, Git workflows')}
{skill_item(Colors.BLUE + 'Deployment:' + Colors.RESET + ' CI/CD, Blue-Green, Rolling Updates, GitOps')}
"""
