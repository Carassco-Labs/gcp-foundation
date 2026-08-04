# System Architecture

## Overview

The `gcp-foundation` repository is designed around a modern, serverless cloud architecture on Google Cloud Platform (GCP).

```text
+------------------+         +------------------+         +--------------------+
|  GitHub Actions  | ------> | Artifact Registry | ------> |   GCP Cloud Run    |
| (CI/CD Pipeline) |         | (Docker Images)  |         | (Serverless App)   |
+------------------+         +------------------+         +--------------------+
                                                                    |
                                                                    v
                                                          +--------------------+
                                                          | GCP Secret Manager |
                                                          |  (Secrets/Configs) |
                                                          +--------------------+
```

## Architectural Highlights

- **Stateless Application Tier**: Hosted on GCP Cloud Run, auto-scaling from 0 to N instances based on inbound traffic.
- **Container Registry**: GCP Artifact Registry stores immutable, versioned Docker image tags.
- **Continuous Delivery**: GitHub Actions triggers workflow runs on `main` branch pushes using Workload Identity Federation (keyless OIDC authentication).
- **Security & Secret Management**: App configuration and sensitive keys are retrieved securely from GCP Secret Manager at runtime.
