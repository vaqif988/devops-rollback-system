# Kubernetes DevOps Rollback Demo

This project demonstrates a production-like DevOps setup with:

- Python Flask demo application
- Docker image build
- Kubernetes deployment using Helm
- GitHub Actions CI/CD
- One-click rollback using a dedicated workflow

## Features

- Automatic Docker build & push on `main` branch
- Versioned images using commit SHA
- Helm-based deployment to Kubernetes
- Health checks (`/health` endpoint)
- Manual, one-click rollback from GitHub Actions (Helm rollback)

## Tech Stack

- Python 3 + Flask
- Docker
- Kubernetes
- Helm 3
- GitHub Actions

## How to use

1. Set up a Kubernetes cluster (minikube, k3s, EKS, etc.)
2. Create Docker registry and push credentials
3. Configure GitHub Secrets:
   - `REGISTRY_USER`
   - `REGISTRY_PASSWORD`
   - `KUBE_CONFIG` (base64 or raw kubeconfig)
4. Push code to `main` → CD will deploy it automatically.
5. To rollback:
   - Go to GitHub → Actions → `Rollback Release`
   - Click `Run workflow` → previous release will be restored.
////