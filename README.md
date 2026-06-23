# SSH Portfolio - Madan Dhungel

A professional DevOps Engineer portfolio accessible via SSH. Built with Python, Docker, Kubernetes, and Helm.

## 🎯 Overview

An interactive SSH-based portfolio showcasing:
- Professional experience and achievements
- Technical skills and technologies
- Certifications and education
- Contact information
- Colorful terminal UI with ASCII art

## 📁 Project Structure

```
ssh-portfolio/
├── app/                          # Application code and Docker build
│   ├── Dockerfile                # Container image definition
│   ├── requirements.txt           # Python dependencies
│   ├── docker-compose.yaml        # Docker Compose setup
│   ├── ssh_server.py              # Main SSH server application
│   ├── app.py                     # Local terminal application
│   ├── about.py                   # Profile information
│   ├── skills.py                  # Technical skills
│   ├── projects.py                # Professional experience
│   ├── contact.py                 # Contact information
│   ├── certifications.py          # Certifications & education
│   ├── all.py                     # Complete portfolio view
│   ├── colors.py                  # Terminal color utilities
│   ├── ascii_art.py               # ASCII art for tools
│   └── README.md                  # App-specific guide
│
├── kubernetes/                    # Kubernetes manifests
│   ├── namespace.yaml             # K8s namespace
│   ├── configmap.yaml             # Configuration
│   ├── pvc.yaml                   # Persistent volume
│   ├── deployment.yaml            # Pod deployment
│   ├── service.yaml               # Networking service
│   ├── kustomization.yaml         # Kustomize manifest
│   ├── deploy.sh                  # Deployment script
│   └── README.md                  # K8s-specific guide
│
├── helm/                          # Helm chart
│   └── ssh-portfolio/             # Helm chart for SSH Portfolio
│       ├── Chart.yaml             # Chart metadata
│       ├── values.yaml            # Default configuration
│       ├── README.md              # Helm guide
│       └── templates/             # K8s template files
│           ├── namespace.yaml
│           ├── configmap.yaml
│           ├── pvc.yaml
│           ├── deployment.yaml
│           ├── service.yaml
│           └── NOTES.txt
│
└── README.md                      # This file
```

## 🚀 Quick Start

### Option 1: Docker

```bash
cd /home/madan/ssh-portfolio/app
docker build -t ssh-portfolio:latest .
docker run -d -p 2222:2222 ssh-portfolio:latest
ssh -p 2222 localhost
```

### Option 2: Docker Compose

```bash
cd /home/madan/ssh-portfolio/app
docker-compose up -d
ssh -p 2222 localhost
```

### Option 3: Kubernetes

```bash
cd /home/madan/ssh-portfolio/app
docker build -t ssh-portfolio:latest .

kubectl apply -f ../kubernetes/
kubectl port-forward -n ssh-portfolio svc/ssh-portfolio 2222:2222 &
ssh -p 2222 localhost
```

### Option 4: Helm

```bash
cd /home/madan/ssh-portfolio/app
docker build -t ssh-portfolio:latest .

helm install ssh-portfolio ./helm/ssh-portfolio/

kubectl port-forward -n ssh-portfolio svc/ssh-portfolio 2222:2222 &
ssh -p 2222 localhost
```

## 🎮 Available Commands

Once connected via SSH:

```
0. all       - View complete portfolio
1. about     - Who am I
2. skills    - My technical stack
3. projects  - My work & experience
4. contact   - How to reach me
5. certs     - Certifications & achievements
6. clear     - Clear screen
help         - Show commands
exit         - Exit session
```

## 📋 Features

✅ **Colorful Terminal UI** - ANSI colored text with ASCII art  
✅ **Persistent SSH Keys** - Host key survives pod restarts  
✅ **Docker & Docker Compose** - Multiple deployment options  
✅ **Kubernetes Ready** - Full K8s manifests included  
✅ **Helm Chart** - Production-ready Helm deployment  
✅ **Health Checks** - Liveness and readiness probes  
✅ **Scalable** - Ready for multi-replica deployments  

## 📚 Documentation

- **[App Guide](app/README.md)** - Application structure
- **[Kubernetes Guide](kubernetes/README.md)** - K8s deployment
- **[Helm Guide](helm/ssh-portfolio/README.md)** - Helm chart usage

## 🔧 Configuration

### Environment Variables

- `SSH_PORT` - SSH listening port (default: 2222)
- `SSH_HOST_KEY_PATH` - Path to SSH host key

## 📊 Accessing SSH Portfolio

### Local Machine
```bash
ssh -p 2222 localhost
```

### Remote Server
```bash
ssh -p 2222 <server-ip>
```

### Kubernetes (Port Forwarding)
```bash
kubectl port-forward -n ssh-portfolio svc/ssh-portfolio 2222:2222
ssh -p 2222 localhost
```

### Kubernetes (LoadBalancer)
```bash
kubectl get svc ssh-portfolio -n ssh-portfolio
ssh -p 2222 <external-ip>
```

## 📞 Contact

- **Email:** madandhungel08@gmail.com
- **Phone:** +977-9868156201
- **GitHub:** github.com/MadanDhungel
- **LinkedIn:** linkedin.com/in/MadanDhungel
- **Website:** madandhungel.com.np

---

Made with ❤️ by Madan Dhungel
