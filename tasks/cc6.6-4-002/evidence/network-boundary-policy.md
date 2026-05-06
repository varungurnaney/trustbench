# Stratos Payments — Network Boundary and Segmentation Policy

**Document ID:** STR-SEC-POL-014
**Version:** 3.1
**Effective Date:** February 1, 2025
**Owner:** Elena Vasquez, CISO
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy defines requirements for network boundary protection, environment segmentation, and traffic control for all Stratos Payments production systems handling payment card and financial data.

## 2. Scope

All AWS infrastructure across us-east-1 and eu-central-1 regions, including production, staging, and development environments.

## 3. Environment Segmentation

### 3.1 VPC Isolation

Production, staging, and development environments MUST reside in separate VPCs with no direct network peering between them.

- **Production VPC** (10.10.0.0/16) — Payment processing, customer data, APIs
- **Staging VPC** (10.20.0.0/16) — Pre-release validation with synthetic data
- **Development VPC** (10.30.0.0/16) — Engineering sandbox
- **Management VPC** (10.40.0.0/16) — CI/CD, monitoring, logging infrastructure

### 3.2 Cross-Environment Access

Cross-environment network access is prohibited by default. Any cross-environment connectivity requires:
1. Formal exception with business justification
2. Risk assessment documenting threat vectors
3. Compensating controls documented and verified
4. CISO approval
5. Maximum 6-month duration with re-authorization

### 3.3 VPC Peering Rules

VPC peering connections are restricted to:
- Management VPC may peer with Production VPC for monitoring and log aggregation only (ports 9090, 9200, 5044)
- No peering between Production and Staging/Development
- No peering between Staging and Development

## 4. Ingress Controls

### 4.1 WAF Requirements

All public-facing HTTPS endpoints must be protected by AWS WAF with:
- OWASP Core Rule Set
- Bot detection rules
- Rate limiting (500 requests/minute/IP for APIs, 2000 requests/minute/IP for static content)
- Custom rules for PCI DSS compliance

### 4.2 API Gateway

All external API traffic must transit through the Kong API Gateway, which provides:
- Request authentication and authorization
- Schema validation
- Rate limiting and throttling
- Request/response logging

## 5. Encryption in Transit

### 5.1 All production traffic must use TLS 1.3
### 5.2 Internal service mesh uses Linkerd with mTLS in strict mode
### 5.3 Database connections must use TLS with server certificate validation
### 5.4 Certificate rotation: 90-day maximum lifetime via Vault PKI

## 6. Egress Controls

### 6.1 Egress Filtering

All outbound traffic from production VPC must pass through the NAT Gateway with:
- DNS-based egress filtering via Route 53 Resolver rules
- Allowlisted external destinations maintained in the Egress Allowlist Registry
- All egress traffic logged and forwarded to SIEM

### 6.2 Direct Internet Access

Direct internet access (bypassing NAT Gateway) is prohibited for all production instances.

## 7. Exception Process

Exceptions must be documented in the Security Exception Register with quarterly review.

---

**Approved by:** Carlos Mendez, CTO
**Approval Date:** January 28, 2025
