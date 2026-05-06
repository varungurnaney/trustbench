# Platform Migration Summary — Q3/Q4 2025

**Prepared by:** Engineering Leadership, Prism Data Platform
**Date:** January 8, 2026
**Classification:** Internal

---

## 1. Overview

Prism Data Platform completed a major platform migration during Q3-Q4 2025, transforming the company's architecture from a monolithic VM-based infrastructure to a Kubernetes-native, multi-cloud platform. This summary documents the key changes and their timeline.

## 2. Migration Timeline

| Phase | Component | Start Date | Completion Date | Status |
|-------|-----------|------------|-----------------|--------|
| Phase 1 | Kubernetes cluster deployment (AWS EKS) | June 2025 | July 2025 | Complete |
| Phase 2 | Data ingestion pipeline migration to K8s | August 2025 | October 2025 | Complete |
| Phase 3 | GPU inference cluster deployment | August 2025 | September 2025 | Complete |
| Phase 4 | Apache Flink processing cluster migration | September 2025 | October 2025 | Complete |
| Phase 5 | Kafka cluster migration to MSK | October 2025 | November 2025 | Complete |
| Phase 6 | Observability stack migration (Grafana/Prometheus/Loki) | November 2025 | December 2025 | Complete |
| Phase 7 | Legacy VM decommission | January 2026 | February 2026 | In Progress |

## 3. Scope of Changes

### 3.1 Infrastructure Changes
- **Compute:** Migrated from 120 EC2 instances to 8 EKS clusters (dev, staging, prod x3 regions, GPU, monitoring, CI/CD)
- **Networking:** New VPC architecture with service mesh (Istio). Pod-to-pod mTLS. New ingress controllers.
- **Storage:** Migrated from EBS-backed VM storage to EFS + S3 with CSI drivers
- **Container Runtime:** Introduced containerd as runtime. Previous: no containerization.

### 3.2 Application Architecture Changes
- **Data Ingestion:** Monolithic Java service -> 12 microservices on K8s with Horizontal Pod Autoscaling
- **Stream Processing:** Custom Java stream processor -> Apache Flink on K8s
- **ML Inference:** Single GPU server -> Kubernetes-managed GPU cluster with NVIDIA GPU Operator
- **Monitoring:** Datadog -> Grafana/Prometheus/Loki (in-house observability stack)

### 3.3 Security-Relevant Changes
- New Kubernetes RBAC model replacing Linux user/group permissions
- New container image CI/CD pipeline (previously: VM AMI pipeline)
- Service mesh (Istio) mTLS replacing VPN-based network security
- New secrets management (External Secrets Operator + AWS Secrets Manager)
- New monitoring and alerting infrastructure

### 3.4 Customer Sector Changes
- **Q2 2025:** Onboarded first healthcare customers (3 hospital systems) — HIPAA compliance required
- **Q3 2025:** Onboarded first retail customers (2 major retailers) — PCI DSS considerations for payment data streams
- Prior to 2025: Financial services customers only

## 4. Security Review Status

| Review | Status | Date | Reviewer |
|--------|--------|------|----------|
| Kubernetes security configuration review | Complete | August 2025 | External firm (CrowdSec) |
| Container image pipeline security review | Complete | September 2025 | Internal security team |
| Network architecture review (Istio/mTLS) | Complete | October 2025 | External firm (CrowdSec) |
| Secrets management review | Complete | September 2025 | Internal security team |
| Grafana/Prometheus security review | Not Performed | N/A | N/A |
| Flink cluster security review | Not Performed | N/A | N/A |
| Comprehensive post-migration security assessment | Not Performed | N/A | N/A |

## 5. Incidents Related to Migration

The following Q4 2025 security incidents had root causes directly tied to the platform migration:

1. **INC-2025-902:** SSH key from pre-migration period still valid on GPU inference cluster
2. **INC-2025-904:** Tenant routing error in new K8s pipeline orchestrator — cross-sector data leak
3. **INC-2025-905:** Compromised container image in new K8s ingestion pipeline
4. **INC-2025-906:** Default Grafana admin credentials not changed in new observability stack

---

**Reviewed by:** Victor Osman, VP Engineering
**Date:** January 10, 2026
