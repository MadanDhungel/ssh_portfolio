from colors import Colors, bold, section, skill_item, keyword, tech_badge

SKILLS = f"""{Colors.GREEN}{Colors.BOLD}☁️  DevOps & Automation:{Colors.RESET}
{skill_item('📦 Version Control: ' + keyword('Git') + ' • ' + keyword('GitHub'))}
{skill_item('☁️  Cloud Platforms: ' + keyword('AWS') + ' • ' + keyword('OVHcloud'))}
{skill_item('🏗️  Infrastructure as Code: ' + keyword('Terraform') + ' • ' + keyword('Ansible'))}
{skill_item('🐳 Containers & Orchestration: ' + keyword('Docker') + ' • ' + keyword('Kubernetes') + ' • ' + keyword('AWS ECS') + ' • ' + keyword('OVH K8s'))}
{skill_item('⚙️  CI/CD & GitOps: ' + keyword('GitHub Actions') + ' • ' + keyword('Jenkins') + ' • ' + keyword('GitLab CI/CD') + ' • ' + keyword('Argo CD'))}
{skill_item('📊 Monitoring & Logging: ' + keyword('Prometheus') + ' • ' + keyword('Grafana') + ' • ' + keyword('AWS CloudWatch'))}
{skill_item('🐍 Scripting & Automation: ' + keyword('Python') + ' • ' + keyword('Bash'))}

{Colors.GREEN}{Colors.BOLD}🌩️  Cloud & Virtualization:{Colors.RESET}
{skill_item('☁️  OVHcloud: ' + keyword('Managed Kubernetes') + ' • ' + keyword('Object Storage') + ' • ' + keyword('Virtual Machines') + ' • ' + keyword('IAM'))}
{skill_item('☁️  AWS: ' + keyword('EC2') + ' • ' + keyword('S3') + ' • ' + keyword('Auto Scaling') + ' • ' + keyword('Load Balancing') + ' • ' + keyword('ECS') + ' • ' + keyword('EKS'))}
{skill_item('💻 Platforms: ' + keyword('VMware ESXi') + ' • ' + keyword('Hyper-V') + ' • ' + keyword('VirtualBox') + ' • ' + keyword('Proxmox'))}

{Colors.GREEN}{Colors.BOLD}🖥️  System Administration:{Colors.RESET}
{skill_item('🐧 Linux: ' + keyword('Ubuntu') + ' • ' + keyword('CentOS') + ' • ' + keyword('RHEL'))}
{skill_item('🪟 Windows Server: ' + keyword('Active Directory') + ' • ' + keyword('Group Policy') + ' • ' + keyword('DNS') + ' • ' + keyword('DHCP'))}
{skill_item('💾 Backup & Disaster Recovery: ' + keyword('HA Solutions') + ' • ' + keyword('Backup Strategies'))}

{Colors.GREEN}{Colors.BOLD}🔒 Networking & Security:{Colors.RESET}
{skill_item('🔌 Network Devices: ' + keyword('Cisco') + ' • ' + keyword('Juniper') + ' • ' + keyword('MikroTik'))}
{skill_item('⚡ Services: ' + keyword('DNS') + ' • ' + keyword('DHCP') + ' • ' + keyword('Load Balancers') + ' • ' + keyword('Proxy Servers'))}
{skill_item('🛡️  Firewalls & Security: ' + keyword('Fortinet') + ' • ' + keyword('Sophos'))}
{skill_item('👁️  Monitoring: ' + keyword('Zabbix') + ' • ' + keyword('Nagios') + ' • ' + keyword('Cacti') + ' • ' + keyword('SmokePing'))}

{Colors.GREEN}{Colors.BOLD}💾 Databases & Development:{Colors.RESET}
{skill_item('🗄️  Databases: ' + keyword('MySQL') + ' • ' + keyword('PostgreSQL'))}
{skill_item('📋 Methodologies: ' + keyword('SDLC') + ' • ' + keyword('Agile') + ' • ' + keyword('Git workflows'))}
{skill_item('🚀 Deployment: ' + keyword('CI/CD') + ' • ' + keyword('Blue-Green') + ' • ' + keyword('Rolling Updates') + ' • ' + keyword('GitOps'))}
"""
