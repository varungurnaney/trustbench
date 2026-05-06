# Meridian SaaS — System Boundary and Access Control Policy

**Document ID:** MRD-SEC-POL-011
**Version:** 3.2
**Effective Date:** January 1, 2025
**Owner:** Karen Wu, CISO
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy establishes the requirements for defining, protecting, and monitoring Meridian SaaS system boundaries to prevent unauthorized access from external threats.

## 2. Scope

All production infrastructure hosted in AWS (us-east-1, us-west-2, eu-west-1) including all customer-facing and internal services.

## 3. Boundary Architecture

### 3.1 Traffic Flow Requirements

All production traffic — both customer-facing and internal — MUST traverse the following boundary stack:
1. AWS CloudFront (DDoS protection, edge caching)
2. AWS WAF (application-layer threat detection)
3. Kong API Gateway (authentication, rate limiting, schema validation, audit logging)
4. Internal ALB (load distribution to backend services)

No production service shall accept traffic that bypasses any layer of this boundary stack.

### 3.2 Internal Services

Internal services (admin tools, dashboards, support utilities) are production services and are subject to the same boundary requirements as customer-facing services. Internal services must also require:
- VPN connectivity (Tailscale)
- SSO authentication (Okta)
- Role-based access control

### 3.3 API Gateway Responsibilities

The Kong API Gateway is the single enforcement point for:
- Authentication token validation
- API schema enforcement
- Rate limiting per client/IP
- Request payload size limits
- Centralized audit logging of all API calls
- Anomaly detection (unusual request patterns)

## 4. Exception Process

### 4.1 Requirements

Exceptions to Section 3.1 require:
- VP-level or above approval
- CISO acknowledgment
- Documented compensating controls
- Quarterly review
- Maximum 12-month duration

### 4.2 Exception Register

All active exceptions must be maintained in the Security Exception Register with compensating controls verified quarterly.

## 5. Monitoring

### 5.1 Boundary Monitoring

All boundary traversals are logged and monitored:
- CloudFront access logs retained 90 days
- WAF logs forwarded to Splunk
- Kong API Gateway logs forwarded to Splunk with 365-day retention
- Boundary bypass attempts trigger immediate alert to security on-call

## 6. Annual Penetration Testing

External penetration testing must be conducted annually to validate boundary controls. The pentest scope must include all publicly accessible endpoints and any exception-granted bypass paths.

---

**Approved by:** David Nakamura, CTO
