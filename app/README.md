# SSH Portfolio - Complete Deployment Guide

## Overview

This directory contains all necessary files for deploying the SSH Portfolio application using Docker and Kubernetes.

### Directory Structure

```
ssh-portfolio/
├── app/
│   ├── kubernetes/
│   │   ├── namespace.yaml       # K8s namespace
│   │   ├── configmap.yaml       # App configuration
│   │   ├── pvc.yaml             # Persistent volume for SSH keys
│   │   ├── deployment.yaml      # Main deployment
│   │   ├── service.yaml         # Service (LoadBalancer)
│   │   ├── kustomization.yaml   # Kustomize manifest
│   │   ├── deploy.sh            # Deployment script
│   │   └── README.md            # K8s specific guide
│   └── docker-compose.yaml      # Docker Compose setup
├── Dockerfile
├── requirements.txt
└── [Python source files]
```

## Quick Start

### Option 1: Docker Compose (Local Development)

```bash
cd /home/madan/ssh-portfolio/app
docker-compose up -d
ssh -p 2222 localhost
```

### Option 2: Docker (Single Container)

```bash
cd /home/madan/ssh-portfolio
docker build -t ssh-portfolio:latest .
docker run -d -p 2222:2222 ssh-portfolio:latest
ssh -p 2222 localhost
```

### Option 3: Kubernetes

#### Local Kubernetes (Minikube/K3s)

```bash
cd /home/madan/ssh-portfolio/app/kubernetes
chmod +x deploy.sh
./deploy.sh
```

#### Manual Kubernetes Deployment

```bash
kubectl apply -f app/kubernetes/
kubectl port-forward -n ssh-portfolio svc/ssh-portfolio 2222:2222
ssh -p 2222 localhost
```

#### Using Kustomize

```bash
kubectl apply -k app/kubernetes/
```

## Kubernetes Deployment Details

### Namespace
- **Name:** ssh-portfolio
- **Purpose:** Isolate the app from other workloads

### Components

1. **ConfigMap** - Application metadata and configuration
2. **PersistentVolumeClaim** - 1Gi storage for SSH host keys
3. **Deployment** - 1 replica of the SSH portfolio pod
4. **Service** - LoadBalancer to expose port 2222

### Pod Specifications

- **Image:** ssh-portfolio:latest
- **Port:** 2222/TCP
- **CPU Request:** 100m
- **CPU Limit:** 500m
- **Memory Request:** 128Mi
- **Memory Limit:** 256Mi
- **Probes:** Liveness and Readiness checks on port 2222

### Storage

SSH host keys are persisted in `/ssh-keys/` volume:
- Survives pod restarts
- Ensures consistent SSH fingerprint
- Uses PersistentVolumeClaim (1Gi)

## Access Methods

### Port Forwarding
```bash
kubectl port-forward -n ssh-portfolio svc/ssh-portfolio 2222:2222 &
ssh -p 2222 localhost
```

### LoadBalancer (Cloud)
```bash
kubectl get svc ssh-portfolio -n ssh-portfolio
ssh -p 2222 <EXTERNAL-IP>
```

### NodePort (On-Premise)
Edit `service.yaml`:
```yaml
spec:
  type: NodePort
```

Then:
```bash
ssh -p 2222 <node-ip>:<node-port>
```

## Monitoring

### View Logs
```bash
kubectl logs -n ssh-portfolio deployment/ssh-portfolio
kubectl logs -n ssh-portfolio deployment/ssh-portfolio -f  # Follow logs
```

### Check Pod Status
```bash
kubectl get pods -n ssh-portfolio
kubectl describe pod -n ssh-portfolio <pod-name>
```

### Check Events
```bash
kubectl get events -n ssh-portfolio
```

## Scaling

### Scale Deployment
```bash
kubectl scale deployment ssh-portfolio -n ssh-portfolio --replicas=3
```

**Note:** Each pod will have its own SSH host key. For shared keys, use:
- StatefulSet with shared storage
- External secrets management (Vault, AWS Secrets Manager)

## Cleanup

```bash
# Delete all resources
kubectl delete namespace ssh-portfolio

# Or just delete specific resources
kubectl delete deployment ssh-portfolio -n ssh-portfolio
kubectl delete svc ssh-portfolio -n ssh-portfolio
kubectl delete pvc ssh-portfolio-pvc -n ssh-portfolio
```

## Troubleshooting

### Pod won't start
```bash
kubectl describe pod -n ssh-portfolio <pod-name>
kubectl logs -n ssh-portfolio <pod-name>
```

### Can't connect via SSH
```bash
# Check service
kubectl get svc -n ssh-portfolio
kubectl describe svc ssh-portfolio -n ssh-portfolio

# Check pod is running
kubectl get pods -n ssh-portfolio

# Check port forwarding
kubectl port-forward -n ssh-portfolio pod/<pod-name> 2222:2222
```

### Storage issues
```bash
kubectl get pvc -n ssh-portfolio
kubectl describe pvc ssh-portfolio-pvc -n ssh-portfolio
```

## Best Practices

1. **Image Management**
   - Always use specific tags (not `latest` in production)
   - Use private container registries for production

2. **Resource Management**
   - Set appropriate resource requests/limits
   - Monitor resource usage: `kubectl top pods -n ssh-portfolio`

3. **Security**
   - Run as non-root user (if possible)
   - Use NetworkPolicies to restrict traffic
   - Keep SSH host keys secure with RBAC

4. **High Availability**
   - Use multiple replicas with a load balancer
   - Use StatefulSet for consistent host keys
   - Implement pod disruption budgets

5. **Monitoring**
   - Enable logging aggregation (ELK, Loki)
   - Set up alerts for pod failures
   - Use Prometheus for metrics collection

## Production Deployment

For production, consider:

1. Using a private container registry
2. Implementing Ingress with TLS/SSL
3. Using StatefulSet for persistent SSH keys
4. Setting up monitoring and alerting
5. Using network policies for security
6. Implementing pod security policies
7. Using RBAC for access control
8. Setting up backup for persistent volumes

## References

- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [Kustomize Documentation](https://kustomize.io/)
