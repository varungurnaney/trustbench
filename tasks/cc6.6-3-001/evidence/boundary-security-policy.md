# Nimbus Analytics — System Boundary and Service Mesh Security Policy

**Document ID:** POL-SEC-2025-003
**Version:** 2.0
**Effective Date:** March 1, 2025
**Owner:** Sanjay Patel, Director of Platform Engineering
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy establishes the requirements for securing Nimbus Analytics' system boundaries through network segmentation, mutual TLS authentication between all production services, and encryption of data in transit.

## 2. Scope

This policy applies to all production microservices running in the Nimbus Analytics Kubernetes clusters (EKS) across us-east-1 and eu-west-1, including all internal service-to-service communication.

## 3. Service Mesh and Mutual TLS

### 3.1 mTLS Requirement

All production service-to-service communication MUST use mutual TLS (mTLS) authentication. This is enforced through the Istio service mesh with PeerAuthentication set to STRICT mode.

Requirements:
- Every production service must have an Istio sidecar proxy injected
- PeerAuthentication policy must be set to STRICT (no plaintext fallback)
- Client certificates are issued by the internal PKI (HashiCorp Vault)
- Certificate rotation occurs every 72 hours automatically via Vault Agent
- Services that cannot present a valid client certificate are rejected at the mesh layer

### 3.2 Certificate Management

- All service certificates are issued by HashiCorp Vault PKI engine (pki-nimbus-prod)
- Certificate chain: Vault Root CA → Vault Intermediate CA → Service Certificate
- OCSP stapling is enabled for all service certificates
- Certificate revocation is handled via Vault CRL distribution

### 3.3 Exceptions

Any service that cannot support mTLS must obtain a formal exception via the GRC exception process, including:
- Business justification
- Compensating controls
- Time-bound remediation plan
- CISO approval

## 4. Network Segmentation

### 4.1 Kubernetes Network Policies

All production namespaces must have Kubernetes NetworkPolicies that:
- Default deny all ingress traffic
- Explicitly allow only required service-to-service communication
- Restrict egress to approved external endpoints

### 4.2 Namespace Isolation

Each product domain has a dedicated Kubernetes namespace:
- `analytics-core` — Core analytics processing
- `data-ingestion` — Data pipeline and ingestion services
- `customer-api` — Customer-facing API services
- `internal-tools` — Internal administration and tooling
- `ml-platform` — Machine learning model serving

## 5. External Boundary Controls

### 5.1 Ingress

All external traffic enters through the AWS ALB Ingress Controller with:
- TLS 1.3 termination
- AWS WAF with OWASP Core Rule Set
- Rate limiting at 1,000 requests per minute per IP

### 5.2 Egress

Outbound traffic from production clusters is restricted via:
- Istio egress gateway with allowlisted destinations
- DNS-based filtering via CoreDNS policies

## 6. Policy Review

This policy is reviewed semi-annually. Next review: September 2025.

---

**Approved by:** Lisa Tanaka, CISO
**Approval Date:** February 28, 2025
