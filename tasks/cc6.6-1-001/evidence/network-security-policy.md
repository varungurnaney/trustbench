# Orion Health — Network Security Policy

**Document ID:** POL-NET-2024-008
**Version:** 1.4
**Effective Date:** January 15, 2025
**Owner:** Marcus Chen, VP of Engineering
**Classification:** Internal

---

## 1. Purpose

This policy establishes the requirements for securing Orion Health's network infrastructure, controlling access to production systems, and protecting patient health information (PHI) in transit across all environments.

## 2. Scope

This policy applies to all Orion Health network infrastructure hosted in AWS (us-east-1, us-west-2), including:
- Virtual Private Clouds (VPCs)
- Security groups and NACLs
- Load balancers
- VPN connections
- Inter-service communication

## 3. Network Architecture

### 3.1 Environments

Orion Health operates the following environments:
- **Production** — Patient-facing application and API services
- **Staging** — Pre-release validation
- **Development** — Engineering sandbox

### 3.2 Subnet Design

Each environment uses the following subnet layout:
- **Public subnets** — Application Load Balancers and NAT gateways
- **Private subnets** — Application containers and databases

### 3.3 Firewall and Access Control

All inbound traffic from the public internet must pass through an Application Load Balancer with TLS termination. Direct access to application instances from the internet is prohibited.

Security group rules must follow least privilege principles. Rules must specify the minimum ports and source ranges required.

## 4. Encryption in Transit

### 4.1 External Traffic

All external-facing endpoints must use TLS 1.2 or higher. Certificates are managed via AWS Certificate Manager.

### 4.2 Internal Traffic

Internal service-to-service communication should use encrypted channels where feasible.

## 5. VPN Access

Administrative access to production infrastructure requires a VPN connection with multi-factor authentication. VPN sessions are logged and retained for 90 days.

## 6. Monitoring

VPC Flow Logs are enabled for all VPCs and forwarded to the SIEM for analysis.

## 7. Policy Review

This policy is reviewed annually by the VP of Engineering.

---

**Approved by:** Marcus Chen, VP of Engineering
**Next Review Date:** January 2026
