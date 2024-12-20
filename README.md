# CI/CD Pipeline with Blue/Green Deployment and GitOps

This project demonstrates a CI/CD pipeline using GitHub Actions, implementing a blue/green deployment strategy for a simple Python application on Kubernetes. It also showcases GitOps principles using ArgoCD.

## CI Workflow

The CI workflow (`.github/workflows/ci.yml`) is triggered on pushes to the `main` branch or pull requests. It consists of two jobs:

1. `build-test`: Checks out the code, installs dependencies, and runs unit tests.
2. `build-and-push`: If tests pass, builds a Docker image, tags it with the Git SHA, pushes it to a container registry, and stores the image tag as an artifact for the CD pipeline.

## CD Workflow

The CD workflow (`.github/workflows/cd-blue-green.yml`) is triggered manually or on changes to files in the `k8s/` directory. It performs the following steps:

1. Downloads the image tag artifact from the CI workflow.
2. Deploys the new version as the "green" deployment.
3. Waits for the green deployment to become healthy.
4. Switches the service to point to the green deployment.
5. Commits the updated manifests back to the repository.
6. Optionally scales down or removes the old (blue) deployment.

## GitOps with ArgoCD

ArgoCD is used for continuous deployment and synchronization of the cluster state with the Git repository. The ArgoCD Application manifest (`k8s/argocd/application.yaml`) points to the `k8s/` directory in the repository.

When the CI/CD workflows commit changes to the manifests, ArgoCD detects these changes and automatically syncs them to the cluster.

## Setup

1. Install ArgoCD on your Kubernetes cluster.
2. Set up the following repository secrets for registry access and Kubeconfig:
   - `REGISTRY_URL`
   - `REGISTRY_USERNAME`
   - `REGISTRY_PASSWORD`
   - `KUBECONFIG`
3. Adapt the workflows and manifests to your specific environment (e.g., EKS, GKE, or AKS).

## Usage

1. Make changes to the application code or manifests.
2. Push the changes to the `main` branch.
3. The CI workflow will run tests, build, and push the Docker image.
4. The CD workflow will deploy the new version using the blue/green strategy and update the manifests in the repository.
5. ArgoCD will sync the changes to the cluster.
