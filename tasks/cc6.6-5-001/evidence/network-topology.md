# Apex Fintech — Network Architecture Overview

**Document ID:** APXF-INFRA-DOC-023  
**Last Updated:** November 1, 2025  
**Author:** Raj Patel, Principal Infrastructure Engineer  
**Classification:** Internal — Confidential

---

## Architecture Summary

Apex Fintech operates a multi-VPC AWS architecture across two regions (us-east-1 primary, us-west-2 DR). This document describes the production network topology as of November 2025.

## VPC Layout

### Production VPC (10.100.0.0/16) — us-east-1

| Subnet | CIDR | Availability Zone | Purpose |
|--------|------|-------------------|---------|
| prod-public-1a | 10.100.1.0/24 | us-east-1a | NAT Gateways, Bastion (deprecated) |
| prod-public-1b | 10.100.2.0/24 | us-east-1b | NAT Gateways |
| prod-app-1a | 10.100.10.0/24 | us-east-1a | Application services (EKS node group) |
| prod-app-1b | 10.100.11.0/24 | us-east-1b | Application services (EKS node group) |
| prod-data-1a | 10.100.20.0/24 | us-east-1a | RDS PostgreSQL primary, ElastiCache |
| prod-data-1b | 10.100.20.0/24 | us-east-1b | RDS PostgreSQL standby |
| prod-admin-1a | 10.100.5.0/24 | us-east-1a | Internal admin services |

### Staging VPC (10.200.0.0/16) — us-east-1

Mirrors production topology with smaller instance sizes. Used for pre-production validation.

### Management VPC (10.50.0.0/16) — us-east-1

| Subnet | CIDR | Purpose |
|--------|------|---------|
| mgmt-tools-1a | 10.50.1.0/24 | Jenkins, ArgoCD, Terraform runners |
| mgmt-monitoring-1a | 10.50.10.0/24 | Splunk indexers, Grafana, Prometheus |
| mgmt-security-1a | 10.50.20.0/24 | Vault, security scanning tools |

## Traffic Flow — External Requests

```
Client → CloudFront (CDN/DDoS) → AWS WAF → API Gateway (Kong) → Internal ALB → EKS Services
```

All external API traffic follows this path without exception. Kong API Gateway handles:
- OAuth 2.0 token validation
- Rate limiting (1000 req/min per client)
- Request schema validation
- API versioning (/v1, /v2)
- Request/response logging

**Traffic volume (November 2025):** ~4.2M requests/day through the API Gateway.

## Traffic Flow — Admin API

```
SRE Workstation → Tailscale VPN → Internal ALB (prod-admin-1a) → Admin API Service (10.100.5.20:8443)
```

The admin API service runs in the prod-admin-1a subnet and is accessible only via the VPN tunnel. This service does NOT route through Kong API Gateway or the WAF.

The admin API handles:
- Circuit breaker state management
- Feature flag overrides
- Service mesh routing updates
- EKS pod scaling overrides
- Database connection pool monitoring

**Traffic volume (November 2025):** ~12,500 requests/day to the admin API. All source IPs are within the Tailscale VPN CIDR (100.64.0.0/10).

The admin API was established in March 2024 after a Kong API Gateway outage (INC-2024-0312) caused a 47-minute production outage. The SRE team was unable to manage circuit breakers or routing during the Gateway outage, extending the incident duration. Post-incident review (PIR-2024-0312) recommended a Gateway-independent administrative path.

## Traffic Flow — VPN Administrative Access

All SSH, kubectl, and console access to production systems requires Tailscale VPN:

1. Engineer authenticates to Tailscale via Okta SSO + YubiKey MFA
2. Tailscale assigns an IP in 100.64.0.0/10
3. VPN ACLs restrict access based on Okta group membership
4. All VPN sessions logged to Splunk with 180-day retention

## Inter-VPC Connectivity

| Source VPC | Destination VPC | Method | Permitted Traffic |
|-----------|----------------|--------|-------------------|
| Management → Production | VPC Peering (pcx-0a1b2c3d) | CI/CD deployments, monitoring agents |
| Management → Staging | VPC Peering (pcx-4e5f6g7h) | CI/CD deployments, monitoring agents |
| Production → Management | VPC Peering (pcx-0a1b2c3d) | Log shipping (Splunk forwarders), metrics |
| Staging ↔ Production | NONE | No direct connectivity permitted |

## DNS Architecture

- Route 53 private hosted zones for internal service discovery
- External DNS: api.apexfintech.com → CloudFront → Kong
- Internal DNS: *.internal.apexfintech.net → Internal ALBs
- Admin DNS: admin-api.internal.apexfintech.net → Admin ALB (10.100.5.20)

## Certificate Management

- External TLS: ACM-managed certificates for CloudFront and ALB (auto-renewal)
- mTLS: HashiCorp Vault PKI engine issues internal service certificates
- Certificate rotation: 90-day lifecycle enforced by Vault policies
- **Note:** No centralized certificate inventory is currently maintained. Certificate status is tracked per-service in individual Vault PKI mounts. A consolidated inventory dashboard is on the Q1 2026 infrastructure roadmap.

---

*Last reviewed by: Marcus Chen, VP of Infrastructure — November 1, 2025*
