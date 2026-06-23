# SSH Portfolio - Kubernetes Deployment Guide

This directory contains all Kubernetes manifests for deploying the SSH Portfolio application.

## Files Overview

- **namespace.yaml** - Creates the `ssh-portfolio` namespace
- **pvc.yaml** - PersistentVolumeClaim for SSH host keys (persistent storage)
- **deployment.yaml** - Main deployment with 1 replica of the SSH portfolio app
- **service.yaml** - LoadBalancer service to expose the app on port 2222
- **configmap.yaml** - Configuration data for the app

## Prerequisites

- Kubernetes cluster running (minikube, K3s, EKS, etc.)
- Docker image built: `ssh-portfolio:latest`
- kubectl installed and configured

## Deployment Steps

### 1. Build Docker Image

```bash
cd /home/madan/ssh-portfolio
docker build -t ssh-portfolio:latest .
```

### 2. Deploy to Kubernetes

```bash
# Apply all manifests
kubectl apply -f app/kubernetes/

# Or apply individually
kubectl apply -f app/kubernetes/namespace.yaml
kubectl apply -f app/kubernetes/configmap.yaml
kubectl apply -f app/kubernetes/pvc.yaml
kubectl apply -f app/kubernetes/deployment.yaml
kubectl apply -f app/kubernetes/service.yaml
```

### 3. Verify Deployment

```bash
# Check namespace
kubectl get namespaces | grep ssh-portfolio

# Check pod status
kubectl get pods -n ssh-portfolio

# Check service
kubectl get svc -n ssh-portfolio

# View service details
kubectl describe svc ssh-portfolio -n ssh-portfolio
```

### 4. Access the SSH Portfolio

**For Minikube:**
```bash
minikube service ssh-portfolio -n ssh-portfolio
# This will give you the IP and port
ssh -p 2222 <minikube-ip>
```

**For Local Cluster:**
```bash
# Get the LoadBalancer IP
kubectl get svc ssh-portfolio -n ssh-portfolio

# Access via SSH
ssh -p 2222 <service-ip>
```

**For Cloud (AWS EKS, etc.):**
```bash
# Get the external LoadBalancer IP/DNS
kubectl get svc ssh-portfolio -n ssh-portfolio -w

# Access
ssh -p 2222 <external-ip>
```

### 5. View Logs

```bash
kubectl logs -n ssh-portfolio deployment/ssh-portfolio
```

### 6. Port Forwarding (if LoadBalancer not available)

```bash
kubectl port-forward -n ssh-portfolio svc/ssh-portfolio 2222:2222
ssh -p 2222 localhost
```

## Storage

The SSH host key is stored in `/ssh-keys/` inside the container, which is mounted to a PersistentVolumeClaim. This ensures:
- Host key persists across pod restarts
- No "host key changed" warnings when pod restarts
- SSH fingerprint stays consistent

## Resource Limits

- CPU Request: 100m
- CPU Limit: 500m
- Memory Request: 128Mi
- Memory Limit: 256Mi

Adjust these in `deployment.yaml` based on your cluster capacity.

## Scaling

To scale the deployment:
```bash
kubectl scale deployment ssh-portfolio -n ssh-portfolio --replicas=3
```

Note: With multiple replicas, each pod will have its own SSH host key unless you use a shared storage solution.

## Cleanup

To remove all resources:
```bash
kubectl delete namespace ssh-portfolio
```

This will delete all resources in the namespace including the deployment, service, and PVC.
