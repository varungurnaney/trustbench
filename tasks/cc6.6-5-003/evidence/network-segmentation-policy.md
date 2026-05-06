# Crestline AI — Network Segmentation and Boundary Security Policy

**Document ID:** CRT-SEC-POL-007
**Version:** 2.6
**Effective Date:** February 1, 2025
**Owner:** Anita Rao, CISO
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy establishes requirements for network segmentation, environment isolation, and system boundary protection for all Crestline AI infrastructure.

## 2. Scope

All AWS infrastructure across us-east-1 and eu-west-1 supporting Crestline AI's machine learning platform.

## 3. Environment Isolation

### 3.1 Principle

Production and non-production environments MUST be logically isolated to prevent unauthorized access, data leakage, and cross-environment contamination. Isolation is achieved through separate VPCs, separate IAM boundaries, and network access controls.

### 3.2 VPC Architecture

Each environment must operate in its own dedicated VPC:
- Production VPC — Customer-facing services, ML inference endpoints, customer data stores
- Staging VPC — Pre-release testing with synthetic data
- Development VPC — Engineering development and experimentation

### 3.3 Cross-Environment Restrictions

- No VPC peering between production and non-production environments
- No shared subnets between environments
- No shared security groups between environments
- No shared database instances between environments

### 3.4 Shared Services

Shared services (monitoring, logging, CI/CD) must reside in a dedicated management VPC with controlled, audited access to production.

## 4. Ingress and WAF Controls

All public-facing endpoints must be protected by AWS WAF with managed rule groups and custom rate limiting. API traffic must transit the API Gateway (AWS API Gateway) for authentication and authorization.

## 5. Encryption in Transit

### 5.1 All external traffic: TLS 1.3 mandatory
### 5.2 All internal traffic: mTLS via Istio service mesh in STRICT mode
### 5.3 Database connections: TLS 1.3 with certificate pinning

## 6. Egress Controls

Production egress restricted to allowlisted destinations via NAT Gateway with DNS filtering.

## 7. Exception Process

Exceptions require CISO approval, documented compensating controls, 6-month maximum duration, and quarterly review.

---

**Approved by:** James Park, CTO
