# Prism Cloud — Network Security and System Boundary Protection Policy

**Document ID:** POL-NET-2024-012
**Version:** 2.3
**Effective Date:** April 1, 2024
**Last Review:** September 1, 2025
**Owner:** Dmitri Petrov, Director of Security Engineering
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy defines the requirements for protecting Prism Cloud system boundaries through network segmentation, traffic filtering, encryption, and monitoring. It ensures that all production systems are isolated from non-production environments and that external-facing services are protected by appropriate security controls.

## 2. Scope

This policy applies to all Prism Cloud network infrastructure, including:

- Virtual Private Clouds (VPCs) across all AWS regions
- Security groups and network access control lists (NACLs)
- Load balancers and reverse proxies
- Web Application Firewalls (WAF)
- VPN and Direct Connect connections
- Inter-service communication channels

## 3. Network Segmentation

### 3.1 Environment Isolation

Production, staging, and development environments must be deployed in separate VPCs with no direct network connectivity between them. Specifically:

- **Production VPC** (vpc-prod-0x8a3f): Contains all production workloads, databases, and supporting services
- **Staging VPC** (vpc-staging-0x4b2e): Contains staging/pre-production workloads for validation testing
- **Development VPC** (vpc-dev-0x7c1d): Contains development workloads and sandbox environments

Cross-environment traffic is prohibited unless explicitly approved through the exception process (Section 8) with documented compensating controls.

### 3.2 Internal Segmentation

Within each environment, network segmentation must be implemented using security groups and subnets:

- **Public subnets**: Limited to load balancers, NAT gateways, and bastion hosts
- **Application subnets**: Application servers, accessible only from load balancers and bastion hosts
- **Data subnets**: Databases and data stores, accessible only from application subnets
- **Management subnets**: Monitoring, logging, and CI/CD infrastructure

### 3.3 Security Group Rules

Security group rules must follow these principles:

- Default deny — all inbound traffic is denied unless explicitly permitted
- Least privilege — rules must specify the minimum required ports and source IP ranges
- No rules permitting 0.0.0.0/0 on non-public-facing ports
- All rules must include a description documenting the business justification
- Security group rules are reviewed quarterly as part of the network security audit

## 4. Web Application Firewall (WAF)

### 4.1 WAF Requirements

All public-facing HTTP/HTTPS endpoints must be protected by AWS WAF with the following minimum rule sets:

- AWS Managed Rules — Core Rule Set (CRS)
- AWS Managed Rules — Known Bad Inputs
- AWS Managed Rules — SQL Injection
- Rate limiting (maximum 2,000 requests per 5 minutes per IP)
- Custom geo-blocking rules as defined by the Security team

### 4.2 WAF Monitoring

- WAF logs must be forwarded to the SIEM (Splunk) for analysis
- Blocked request alerts are reviewed daily by the Security Operations team
- WAF rule effectiveness is reported monthly

## 5. Encryption in Transit

### 5.1 External Traffic

All external-facing endpoints must terminate TLS 1.2 or higher. TLS 1.3 is required for all new deployments as of January 1, 2025.

### 5.2 Inter-Service Communication

All inter-service communication within production VPCs must be encrypted:

- Service-to-service calls must use HTTPS (TLS 1.2 or higher)
- gRPC services must use TLS-encrypted channels
- Database connections must use TLS-encrypted connections
- Unencrypted HTTP is prohibited for any inter-service communication in production

### 5.3 TLS Configuration Standards

- Minimum TLS version: 1.2 for existing services, 1.3 for new deployments
- Preferred cipher suites: TLS_AES_256_GCM_SHA384, TLS_CHACHA20_POLY1305_SHA256
- Certificate management via AWS Certificate Manager (ACM) for external certificates and AWS Private CA for internal certificates
- Certificate expiration monitoring with 30-day advance alerting

## 6. VPN and Remote Access

- Administrative access to production infrastructure requires VPN connection
- VPN connections use IKEv2 with AES-256 encryption
- Multi-factor authentication (MFA) is required for all VPN connections
- VPN session logs are retained for 12 months

## 7. Monitoring and Detection

### 7.1 Network Monitoring

- VPC Flow Logs are enabled for all VPCs and retained for 12 months
- AWS GuardDuty is enabled for threat detection across all accounts
- Network traffic anomaly detection alerts are configured in Splunk

### 7.2 Quarterly Network Security Audit

A quarterly audit of network configurations must be performed by the Security Engineering team, including:

- Review of all security group rules
- Verification of WAF configurations on public endpoints
- TLS configuration scan across all endpoints
- Cross-environment connectivity verification

## 8. Exception Process

Exceptions to this policy may be requested through the Prism Cloud GRC portal and must be approved by the Director of Security Engineering. Exceptions require:

1. Documented business justification
2. Risk assessment
3. Compensating controls that mitigate the identified risk
4. Time-bound duration (maximum 12 months)
5. Quarterly review and reauthorization

## 9. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 2.3 | 2025-09-01 | D. Petrov | Updated TLS requirements, added WAF monitoring section |
| 2.2 | 2025-03-15 | D. Petrov | Added internal segmentation requirements |
| 2.0 | 2024-04-01 | D. Petrov | Major revision — added WAF requirements, VPN standards |
| 1.0 | 2023-08-01 | K. Yamamoto | Initial release |
