# GCP Foundation (`gcp-foundation`)

[![Carassco Labs Handbook Compliant](https://img.shields.io/badge/Handbook-100%25%20Compliant-0052CC.svg)](file:///Users/dalehendriques/Downloads/MELVIN_WORK/carassco-labs/handbook/README.md)
[![GCP Native](https://img.shields.io/badge/GCP-Cloud%20Run%20%7C%20Secret%20Manager-4285F4.svg)](https://cloud.google.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-v0.110%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Multi--Stage-2496ED.svg)](https://www.docker.com/)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions%20WIF-2088FF.svg)](https://github.com/features/actions)

> **Official Backend & AI Cloud Infrastructure Template for Carassco Labs**

---

## 📌 Why This Repository Exists

`gcp-foundation` is the foundational engineering baseline for every backend microservice, API platform, and AI application built inside **Carassco Labs**. 

Rather than treating cloud setup as a series of ad-hoc tutorial scripts, this repository serves as a **production-ready architecture template**. It codifies Staff Engineer-level patterns for containerization, secret management, observability, keyless CI/CD, and GCP cloud-native deployment.

Every future backend project in Carassco Labs inherits directly from this baseline, guaranteeing 100% architectural consistency, security compliance, and zero-effort setup across teams.

---

## 👥 Who Should Use It

- **Backend Engineers**: Building new RESTful, gRPC, or event-driven microservices in Python.
- **AI / ML Engineers**: Developing LLM orchestrators, RAG pipelines, or model serving interfaces backed by GCP Vertex AI.
- **Platform & DevOps Engineers**: Standardizing Terraform infrastructure modules, CI/CD pipelines, and IAM security boundaries.

---

## 🧬 How Future Projects Inherit From It

Every new backend project at Carassco Labs is instantiated from `gcp-foundation` as a GitHub Template repository or cloned baseline.

### Method 1: Using the Automated Scaffolding Script

Run the built-in repository bootstrap generator from the `gcp-foundation` root:

```bash
python scripts/bootstrap_project.py \
  --project-name "my-new-ai-service" \
  --description "AI-powered document extraction engine" \
  --destination "../my-new-ai-service"
```

The script re-keys settings, updates package paths, initializes fresh Git history, and verifies compliance with Carassco Labs standards.

### Method 2: GitHub Repository Template

1. Navigate to the `gcp-foundation` repository on GitHub.
2. Click **Use this template** ➔ **Create a new repository**.
3. Name your target service (e.g., `carassco-labs/claims-service`).

---

## 📘 Integration with Carassco Labs Handbook

`gcp-foundation` directly embeds and enforces the standards defined in the [Carassco Labs Handbook](file:///Users/dalehendriques/Downloads/MELVIN_WORK/carassco-labs/handbook/README.md):

| Handbook Chapter | Implementation in `gcp-foundation` |
| :--- | :--- |
| **[02 Project Structure](file:///Users/dalehendriques/Downloads/MELVIN_WORK/carassco-labs/handbook/docs/02-project-structure-standards.md)** | Modular `app/` packaging (`core/`, `api/`, `services/`, `schemas/`). |
| **[03 Python Standards](file:///Users/dalehendriques/Downloads/MELVIN_WORK/carassco-labs/handbook/docs/03-python-standards.md)** | Strict type annotations, `ruff` linting, Python 3.11+ async patterns. |
| **[04 FastAPI Standards](file:///Users/dalehendriques/Downloads/MELVIN_WORK/carassco-labs/handbook/docs/04-fastapi-standards.md)** | Pydantic v2 data models, dependency injection, standardized exception handlers. |
| **[06 Google Cloud Standards](file:///Users/dalehendriques/Downloads/MELVIN_WORK/carassco-labs/handbook/docs/06-google-cloud-standards.md)** | Cloud Run serverless execution, GCP Secret Manager resolution, Cloud Logging. |
| **[07 Docker Standards](file:///Users/dalehendriques/Downloads/MELVIN_WORK/carassco-labs/handbook/docs/07-docker-standards.md)** | Multi-stage Docker builds, non-root `appuser`, layer caching. |
| **[08 CI/CD Standards](file:///Users/dalehendriques/Downloads/MELVIN_WORK/carassco-labs/handbook/docs/08-cicd-standards.md)** | Keyless Workload Identity Federation, automated pytest & deployment workflows. |
| **[19 Architecture Decisions](file:///Users/dalehendriques/Downloads/MELVIN_WORK/carassco-labs/handbook/docs/19-architecture-decision-records.md)** | ADR-001 through ADR-005 formatted per handbook templates. |

---

## 🧠 Integration with Knowledge Repository

`gcp-foundation` is fully indexed in the [Carassco Labs Knowledge Base](file:///Users/dalehendriques/Downloads/MELVIN_WORK/carassco-labs/knowledge/README.md).

- **Knowledge Graph Node ID**: `node:carassco:infrastructure:gcp-foundation`
- **Schema Mapping**: Aligned with `knowledge/schema/repository.schema.json`.
- **Architectural Indexing**: All ADRs and system diagrams in `architecture/` are registered in the knowledge graph to inform automated AI coding agents and team architectural reviews.

---

## 📂 Repository Directory Layout

```text
gcp-foundation/
├── .github/                  # CI/CD pipelines (GitHub Actions) & PR templates
├── app/                      # FastAPI core kernel layout & modular scaffolding
├── architecture/             # High-level system architecture & Mermaid sequence diagrams
├── assets/                   # Architecture diagrams & graphic assets
├── config/                   # Multi-environment configuration profiles
├── docker/                   # Multi-stage Docker definitions & compose manifests
├── docs/                     # Comprehensive architecture & operational docs
│   ├── adr/                  # Architectural Decision Records (ADR-001 - ADR-005)
│   ├── ARCHITECTURE.md       # High-level architecture documentation
│   ├── CONFIGURATION.md      # Configuration & Secret Manager design
│   ├── DEPLOYMENT.md         # Deployment & rollback strategy
│   └── PROJECT_OVERVIEW.md   # Business goals, stack & roadmap
├── examples/                 # Reference patterns for services, endpoints, & events
├── infrastructure/           # Terraform IaC GCP infrastructure modules
├── scripts/                  # Project bootstrapping, validation, & management tools
├── tests/                    # Unit, integration, & fixture test architecture
├── .env.example              # Local environment configuration template
├── Dockerfile                # Multi-stage production container build
├── docker-compose.yml        # Local development orchestration manifest
└── README.md                 # Root engineering template reference (This document)
```

---

## 📐 Architecture Decision Records (ADRs)

Key architectural decisions governing this foundation are formally recorded:

- **[ADR-001: Why Google Cloud Platform](file:///Users/dalehendriques/Downloads/MELVIN_WORK/carassco-labs/gcp-foundation/docs/adr/ADR-001-why-google-cloud-platform.md)**
- **[ADR-002: Why FastAPI](file:///Users/dalehendriques/Downloads/MELVIN_WORK/carassco-labs/gcp-foundation/docs/adr/ADR-002-why-fastapi.md)**
- **[ADR-003: Why Docker](file:///Users/dalehendriques/Downloads/MELVIN_WORK/carassco-labs/gcp-foundation/docs/adr/ADR-003-why-docker.md)**
- **[ADR-004: Why Cloud Run](file:///Users/dalehendriques/Downloads/MELVIN_WORK/carassco-labs/gcp-foundation/docs/adr/ADR-004-why-cloud-run.md)**
- **[ADR-005: Why GitHub Actions](file:///Users/dalehendriques/Downloads/MELVIN_WORK/carassco-labs/gcp-foundation/docs/adr/ADR-005-why-github-actions.md)**

---

## ⚡ Quick Start for Developers

To explore the architecture and prepare your local environment for downstream development:

```bash
# 1. Clone the repository
git clone https://github.com/carassco-labs/gcp-foundation.git
cd gcp-foundation

# 2. Setup local environment variables
cp .env.example .env

# 3. Validate project architecture compliance
python scripts/validate.sh
```

---

## 📜 License & Governance

Managed under the **Carassco Labs Engineering Governance Framework**. Proprietary to Carassco Labs.