# SSH Portfolio - Helm Chart

This is a Helm chart for deploying the SSH Portfolio application on Kubernetes.

## Prerequisites

- Kubernetes cluster (1.19+)
- Helm 3.x
- Docker image built: `ssh-portfolio:latest`

## Installation

### 1. Build Docker Image

```bash
cd /home/madan/ssh-portfolio/app
docker build -t ssh-portfolio:latest .
```

### 2. Install Helm Chart

```bash
# Using default values
helm install ssh-portfolio ./helm/ssh-portfolio/

# Using custom namespace
helm install ssh-portfolio ./helm/ssh-portfolio/ -n my-namespace --create-namespace

# With custom values
helm install ssh-portfolio ./helm/ssh-portfolio/ -f custom-values.yaml
```

### 3. Verify Installation

```bash
helm list
kubectl get all -n ssh-portfolio
```

## Configuration

Edit `values.yaml` to customize:

- **replicaCount** - Number of pod replicas
- **image.repository** - Docker image repository
- **image.tag** - Docker image tag
- **service.type** - LoadBalancer, NodePort, or ClusterIP
- **storage.enabled** - Enable persistent volume for SSH keys
- **resources** - CPU and memory limits
- **autoscaling** - Enable HPA

Example custom values:

```yaml
replicaCount: 3
image:
  tag: v1.0.0
service:
  type: NodePort
  nodePort: 30222
resources:
  requests:
    cpu: 200m
    memory: 256Mi
  limits:
    cpu: 1000m
    memory: 512Mi
```

## Usage

### Port Forwarding

```bash
kubectl port-forward -n ssh-portfolio svc/ssh-portfolio 2222:2222
ssh -p 2222 localhost
```

### Check Logs

```bash
kubectl logs -n ssh-portfolio deployment/ssh-portfolio
kubectl logs -n ssh-portfolio deployment/ssh-portfolio -f
```

### Scale Deployment

```bash
kubectl scale -n ssh-portfolio deployment/ssh-portfolio --replicas=3
```

Or update `values.yaml` and upgrade:

```bash
helm upgrade ssh-portfolio ./helm/ssh-portfolio/
```

## Upgrade

```bash
helm upgrade ssh-portfolio ./helm/ssh-portfolio/ -f custom-values.yaml
```

## Rollback

```bash
helm rollback ssh-portfolio
```

## Uninstall

```bash
helm uninstall ssh-portfolio -n ssh-portfolio
```

## Troubleshooting

### Check Release Status

```bash
helm status ssh-portfolio -n ssh-portfolio
```

### Get Release Values

```bash
helm get values ssh-portfolio -n ssh-portfolio
```

### Dry Run

```bash
helm install ssh-portfolio ./helm/ssh-portfolio/ --dry-run --debug
```

## File Structure

```
helm/ssh-portfolio/
├── Chart.yaml              # Chart metadata
├── values.yaml             # Default values
├── README.md               # This file
└── templates/
    ├── namespace.yaml      # Kubernetes namespace
    ├── deployment.yaml     # Deployment resource
    ├── service.yaml        # Service resource
    ├── configmap.yaml      # ConfigMap resource
    ├── pvc.yaml            # PersistentVolumeClaim resource
    └── NOTES.txt           # Post-install notes
```

## Best Practices

1. Always specify image tags in production (not `latest`)
2. Set resource requests and limits appropriately
3. Use persistent volumes for SSH keys to maintain consistent fingerprints
4. Implement proper RBAC policies
5. Monitor pod logs and metrics
6. Test upgrades in staging environment first

## References

- [Helm Documentation](https://helm.sh/docs/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
