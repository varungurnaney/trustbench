# Vertex Data — Perimeter Security and Boundary Protection Policy

**Document ID:** VTX-SEC-POL-006
**Version:** 2.4
**Effective Date:** March 15, 2025
**Owner:** Tomoko Ishikawa, Director of Security
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy defines requirements for protecting Vertex Data's system perimeter, including ingress/egress controls, DDoS protection, and intrusion detection across all production environments.

## 2. Scope

All GCP infrastructure in us-central1 and europe-west1, including:
- Production GKE clusters
- Cloud SQL instances
- Cloud Storage buckets
- Cloud Load Balancers
- Cloud Armor WAF policies

## 3. Ingress Controls

### 3.1 Load Balancer and WAF

All public-facing endpoints must be served through Google Cloud Load Balancer with Cloud Armor security policies:
- OWASP ModSecurity Core Rule Set
- DDoS protection (Google Cloud Armor Adaptive Protection)
- Geographic restrictions per data residency requirements
- Custom rate limiting rules

### 3.2 API Gateway

All customer-facing API traffic must route through Apigee API Gateway providing:
- OAuth 2.0 / API key validation
- Request schema validation
- Quota management per API key
- Request/response audit logging

### 3.3 Ingress Controller

GKE clusters use the Istio ingress gateway with:
- mTLS termination for internal traffic
- JWT validation for service-to-service authentication
- Network policies enforcing namespace isolation

## 4. IDS/IPS Requirements

### 4.1 Cloud IDS

Google Cloud IDS must be deployed on all production VPC networks with:
- Threat detection signatures updated automatically
- High-confidence alerts forwarded to SIEM within 5 minutes
- Weekly signature update review by Security Operations

### 4.2 Alert Response

IDS alerts must be triaged within the SLAs defined in the incident response plan.

## 5. Egress Controls

### 5.1 NAT Gateway

All production egress must route through Cloud NAT with logging enabled.

### 5.2 Egress Policy

Only approved external destinations are permitted via firewall rules. Unapproved egress is blocked by default-deny egress rules.

## 6. Network Segmentation

### 6.1 VPC Architecture

Vertex Data uses a Shared VPC model:
- Host project: vtx-network-host
- Service projects: vtx-prod, vtx-staging, vtx-dev
- Subnet isolation enforced via firewall rules and VPC Service Controls

### 6.2 VPC Service Controls

VPC Service Controls perimeters must protect:
- Cloud SQL instances
- Cloud Storage buckets containing customer data
- BigQuery datasets

## 7. Policy Review

Reviewed quarterly. Next review: June 2025.

---

**Approved by:** Ryan Choi, CTO
