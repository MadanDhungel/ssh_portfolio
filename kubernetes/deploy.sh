#!/bin/bash
# Quick deployment script for SSH Portfolio on Kubernetes

set -e

NAMESPACE="ssh-portfolio"
IMAGE_NAME="ssh-portfolio"
IMAGE_TAG="latest"

echo "🚀 SSH Portfolio Kubernetes Deployment Script"
echo "=============================================="

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to print status
print_status() {
    echo -e "${GREEN}✓${NC} $1"
}

print_info() {
    echo -e "${YELLOW}ℹ${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

# Check if kubectl is installed
if ! command -v kubectl &> /dev/null; then
    print_error "kubectl not found. Please install kubectl."
    exit 1
fi

# Check if Docker image exists
echo ""
print_info "Checking if Docker image exists..."
if docker image inspect $IMAGE_NAME:$IMAGE_TAG > /dev/null 2>&1; then
    print_status "Docker image found: $IMAGE_NAME:$IMAGE_TAG"
else
    print_error "Docker image not found. Building..."
    cd /home/madan/ssh-portfolio
    docker build -t $IMAGE_NAME:$IMAGE_TAG .
    print_status "Docker image built successfully"
fi

# Apply manifests
echo ""
print_info "Deploying to Kubernetes..."
kubectl apply -f namespace.yaml && print_status "Namespace created"
kubectl apply -f configmap.yaml && print_status "ConfigMap created"
kubectl apply -f pvc.yaml && print_status "PersistentVolumeClaim created"
kubectl apply -f deployment.yaml && print_status "Deployment created"
kubectl apply -f service.yaml && print_status "Service created"

# Wait for deployment to be ready
echo ""
print_info "Waiting for deployment to be ready..."
kubectl rollout status deployment/ssh-portfolio -n $NAMESPACE --timeout=5m

# Get service info
echo ""
print_status "Deployment complete!"
echo ""
print_info "Service Information:"
kubectl get svc ssh-portfolio -n $NAMESPACE

echo ""
print_info "Pod Status:"
kubectl get pods -n $NAMESPACE

echo ""
print_info "Access your SSH Portfolio:"
echo "  kubectl port-forward -n ssh-portfolio svc/ssh-portfolio 2222:2222"
echo "  ssh -p 2222 localhost"
