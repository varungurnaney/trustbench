# Apex Fintech — System Boundary and Network Security Policy

**Document ID:** APXF-SEC-POL-009  
**Version:** 3.2  
**Effective Date:** January 15, 2025  
**Last Reviewed:** January 15, 2025  
**Owner:** Marcus Chen, VP of Infrastructure  
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy defines the system boundary requirements and network security controls for all Apex Fintech production, staging, and management environments. It ensures that all external and internal network communications are properly controlled, monitored, and secured in accordance with SOC 2 Trust Services Criteria.

## 2. Scope

This policy applies to all Apex Fintech information systems, network infrastructure, cloud environments (AWS us-east-1 and us-west-2 regions), and personnel responsible for system administration.

## 3. System Boundary Architecture

### 3.1 Network Segmentation

Apex Fintech maintains a segmented network architecture consisting of three isolated Virtual Private Clouds (VPCs):

| VPC | CIDR Range | Purpose |
|-----|-----------|---------|
| Production VPC | 10.100.0.0/16 | All customer-facing services, databases, and application workloads |
| Staging VPC | 10.200.0.0/16 | Pre-production testing and QA environments |
| Management VPC | 10.50.0.0/16 | Administrative tools, CI/CD pipelines, monitoring, and logging infrastructure |

Inter-VPC communication is restricted via VPC peering with explicit route table entries. No transitive routing is permitted.

### 3.2 DMZ Architecture

All customer-facing traffic MUST traverse the Demilitarized Zone (DMZ) architecture:

1. **CloudFront CDN** — Edge-level DDoS protection and static asset delivery
2. **AWS Web Application Firewall (WAF)** — Layer 7 filtering with OWASP Top 10 rule sets
3. **API Gateway (Kong Enterprise)** — Rate limiting, authentication, request validation, and API versioning
4. **Internal Application Load Balancers** — Service routing within the production VPC

**No production service shall be directly accessible from the public internet without traversing the WAF and API Gateway.**

### 3.3 Service-to-Service Communication

All internal service-to-service communication within the production VPC MUST use mutual TLS (mTLS) authentication:

- Certificate issuance is managed by the internal Apex Fintech PKI (HashiCorp Vault)
- Certificates are rotated every 90 days
- Services without valid mTLS certificates are rejected at the service mesh layer (Istio)
- mTLS enforcement is configured via Istio PeerAuthentication policies set to STRICT mode

### 3.4 Administrative Access

All administrative access to production and management systems MUST traverse the VPN:

- **VPN Provider:** Tailscale (WireGuard-based)
- **VPN CIDR:** 100.64.0.0/10
- **Authentication:** SSO via Okta with hardware-based MFA (YubiKey)
- **Session Duration:** Maximum 8 hours, re-authentication required

### 3.5 Emergency Administrative Access

In the event of a production emergency requiring direct system access, the SRE team may utilize the internal administrative API endpoint:

- **Endpoint:** admin-api.internal.apexfintech.net (10.100.5.20:8443)
- **Access:** Restricted to VPN CIDR range (100.64.0.0/10) only
- **Authentication:** mTLS client certificate + Okta SSO
- **Purpose:** Emergency debugging, circuit breaker management, service mesh configuration overrides
- **Note:** This endpoint does not traverse the API Gateway; traffic is routed directly to the admin API service via internal ALB

The emergency admin API was deployed to provide the SRE team with a reliable path to manage production systems during API Gateway outages or degraded performance events.

## 4. Boundary Protection Controls

### 4.1 Firewall Rules

- Default deny on all Security Groups and Network ACLs
- Allowlists are maintained per-service and reviewed monthly
- Changes to firewall rules require approval from the Security Engineering team via Jira ticket (workflow: SEC-FIREWALL)

### 4.2 Intrusion Detection

- AWS GuardDuty enabled across all accounts and regions
- Suricata IDS deployed on NAT Gateway traffic
- Alert routing to PagerDuty for critical severity findings

### 4.3 Penetration Testing

Apex Fintech conducts external penetration testing on a **quarterly basis** using an approved third-party vendor:

- **Current Vendor:** CyberShield Assessments LLC
- **Scope:** All internet-facing services, VPN endpoints, and DMZ infrastructure
- **Remediation SLA:** Critical — 7 days, High — 30 days, Medium — 90 days, Low — Next quarter
- **Reports are reviewed by:** VP of Infrastructure and CISO within 5 business days of delivery

### 4.4 Boundary Monitoring

- All ingress/egress traffic is logged to the centralized SIEM (Splunk)
- API Gateway access logs retained for 365 days
- VPN connection logs retained for 180 days
- Anomalous traffic patterns trigger automated alerts (threshold: >2 standard deviations from 30-day baseline)

## 5. Exceptions

Any deviation from this policy requires a formal exception approved by the CISO and documented in the Security Exception Register (Jira project: SEC-EXC). Exceptions are reviewed quarterly and must include:

- Business justification
- Compensating controls
- Risk acceptance sign-off
- Expiration date (maximum 12 months)

## 6. Review and Updates

This policy is reviewed annually, or upon significant changes to the network architecture. The next scheduled review is January 2026.

---

*Approved by: Sarah Nakamura, CISO — January 15, 2025*
