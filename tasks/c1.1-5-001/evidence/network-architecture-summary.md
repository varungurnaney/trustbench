# Network Architecture Summary — Encryption Posture

**Document ID:** ARCH-NET-003
**Version:** 2.0
**Last Updated:** December 1, 2025
**Author:** Sandra Patel, Principal Network Architect
**Classification:** Internal
**Organization:** Vanguard Risk Solutions

---

## 1. Overview

This document summarizes the network architecture and encryption posture for Vanguard Risk Solutions' cloud infrastructure. All production workloads run on AWS in the us-east-1 region.

## 2. Network Segmentation

### 2.1 VPC Architecture

| VPC | Purpose | CIDR | Data Classification |
|-----|---------|------|-------------------|
| vpc-prod | Production workloads | 10.0.0.0/16 | Restricted/Confidential |
| vpc-staging | Staging/QA | 10.1.0.0/16 | Internal |
| vpc-mgmt | Management and monitoring | 10.2.0.0/16 | Internal |
| vpc-data | Data pipeline and analytics | 10.3.0.0/16 | Confidential |

### 2.2 VPC Peering

- vpc-prod ↔ vpc-data: Peered for analytics pipeline access to production data
- vpc-prod ↔ vpc-mgmt: Peered for monitoring and log collection
- vpc-staging ↔ vpc-mgmt: Peered for staging monitoring

## 3. East-West Traffic Encryption

### 3.1 Kubernetes Cluster (vpc-prod)

All production microservices run in an EKS cluster with Istio service mesh:

- **Istio mTLS Mode:** STRICT (enforced for all pod-to-pod communication)
- **Certificate Authority:** Istio citadel with automatic certificate rotation
- **Protocol:** TLS 1.3 with automatic key rotation
- **Coverage:** 100% of in-cluster traffic

Services in the mesh:
- Customer API (Restricted data)
- Billing Service (Restricted data)
- Notification Service (Confidential data)
- Analytics Ingestion (Confidential data)
- User Management (Restricted data)

### 3.2 Legacy Non-Containerized Services

Three legacy services run on EC2 instances outside the Kubernetes cluster:

| Service | Host | VPC | Data Handled | TLS Status |
|---------|------|-----|-------------|------------|
| Legacy Reporting Engine | legacy-rpt-01 | vpc-data | Confidential (aggregated reports) | TLS 1.2 enabled |
| Partner SFTP Gateway | sftp-gw-01 | vpc-prod | Confidential (partner files) | SSH/SFTP |
| Internal Admin Console | admin-console-01 | vpc-mgmt | Internal (system config) | TLS 1.2 enabled |

### 3.3 Cross-VPC Traffic (vpc-prod ↔ vpc-data)

Traffic between the production Kubernetes cluster and the data analytics pipeline in vpc-data traverses VPC peering:

- **Current encryption:** None at the network layer. VPC peering traffic is not encrypted by default in AWS.
- **Application-layer encryption:** The analytics ingestion service in the Kubernetes cluster sends data to the analytics pipeline in vpc-data via a REST API over HTTP (port 8080). The application does not implement TLS for this internal connection.
- **Data in transit:** Customer analytics events including user_id, event_type, and session_data. Classified as Confidential.
- **Compensating control argument:** Traffic stays within AWS backbone and never traverses the public internet. VPC peering connections are private and logically isolated.
- **Risk assessment:** AWS states VPC peering traffic "is not encrypted by default" but remains on the AWS private network. NIST and SOC 2 do not explicitly require encryption of traffic within a cloud provider's private network, but industry best practices increasingly recommend it.

### 3.4 Cross-VPC Traffic (vpc-prod ↔ vpc-mgmt)

Traffic between production and management VPCs:

- **Current encryption:** TLS 1.2 for all monitoring agents (Datadog, CloudWatch)
- **Data in transit:** System metrics, logs (sanitized — no PII)
- **Classification:** Internal

## 4. North-South Traffic

All ingress traffic enters through AWS ALB with TLS 1.2+ termination. All egress to third-party APIs uses TLS 1.2+. No exceptions.

## 5. DNS and Certificate Infrastructure

- Public DNS: Route 53 with DNSSEC enabled
- Internal DNS: Route 53 Private Hosted Zones
- Certificate management: AWS Certificate Manager (ACM) for ALB certs, cert-manager for Kubernetes ingress, Istio citadel for service mesh

---

**Reviewed by:** Laura Mitchell, CISO — December 5, 2025
