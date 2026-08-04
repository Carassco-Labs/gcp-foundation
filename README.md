# GCP Foundation

A production-ready starter repository for building, containerizing, and deploying Python & FastAPI AI applications on Google Cloud Platform (GCP).

## 🚀 Objectives

- **GCP Cloud Native Architecture**: Learn GCP from a hands-on engineering perspective.
- **Production FastAPI Application**: Develop modular Python web apps with health checks & tests.
- **Containerization**: Build lightweight, secure multi-stage Docker containers.
- **Serverless Deployment**: Automatically deploy workloads to GCP Cloud Run.
- **CI/CD Automation**: Implement GitHub Actions pipelines for continuous integration and delivery.
- **Infrastructure & Security**: Manage secrets with GCP Secret Manager and enforce least-privilege IAM policies.

## 🛠️ Technologies

- **Cloud Platform**: Google Cloud Platform (Cloud Run, Cloud Storage, Secret Manager, IAM)
- **Framework**: FastAPI (Python 3.11)
- **Containerization**: Docker, Docker Compose
- **CI/CD**: GitHub Actions
- **Testing**: Pytest, HTTPX

## 📂 Repository Structure

```text
├── .github/
│   └── workflows/        # GitHub Actions CI/CD pipelines
├── app/                  # FastAPI source code & application logic
├── architecture/         # System architecture & cloud diagrams
├── docs/                 # Detailed GCP step-by-step documentation
├── scripts/              # Helper shell scripts (e.g. deployment)
├── terraform/            # Infrastructure as Code (IaC) configurations
├── tests/                # Automated unit & integration tests
├── Dockerfile            # Multi-stage Docker container build definition
├── docker-compose.yml    # Local development container orchestration
└── README.md             # Project overview & objectives
```

## 🚧 Status

Under active development as part of the AI Builder Portfolio.