# Meridian SaaS — Network Architecture Document

**Document ID:** MRD-ARCH-005
**Version:** 2.1
**Last Updated:** November 15, 2025
**Author:** Platform Engineering Team

---

## 1. Overview

Meridian SaaS operates a multi-region AWS deployment serving 2,400 enterprise customers. The architecture uses a layered boundary model with CloudFront, WAF, Kong API Gateway, and internal ALBs.

## 2. Standard Traffic Flow

```
Internet → CloudFront → WAF → Kong API Gateway → Internal ALB → Backend Services
```

All 14 customer-facing services follow this standard path:
- Customer Dashboard (dashboard.meridian.io)
- Customer API (api.meridian.io)
- Webhook Receiver (webhooks.meridian.io)
- Partner Portal (partners.meridian.io)
- ... [10 additional microservices]

## 3. Internal Admin Tool

### 3.1 Purpose

The Internal Admin Tool (admin.internal.meridian.io:8443) provides Meridian support engineers and SRE team members access to:
- Customer account management (suspend/unsuspend, plan changes)
- Feature flag management (enable/disable per customer)
- Data export requests (customer data extraction for legal/compliance)
- System configuration (rate limits, circuit breakers, scaling parameters)
- Audit log viewer (query customer activity logs)

### 3.2 Traffic Flow

The admin tool uses a **direct path** that bypasses CloudFront, WAF, and Kong API Gateway:

```
Tailscale VPN → Internal ALB (admin-internal-alb) → Admin Service
```

This architecture was implemented when the admin tool was built in 2022. At that time, Kong was not yet deployed. When Kong was introduced in 2023, the admin tool was not migrated to the standard boundary path because:
- The admin tool uses WebSocket connections for real-time audit log streaming, which Kong did not support at the time
- The admin tool's authentication is handled directly by the service via Okta SAML integration
- Migration was deprioritized relative to customer-facing features

### 3.3 Admin Tool Access Controls

- **Network**: Accessible only via Tailscale VPN (100.64.0.0/10 CIDR)
- **Authentication**: Okta SAML SSO with MFA enforced
- **Authorization**: RBAC with 3 roles (viewer, operator, admin) managed in Okta groups
- **Audit Logging**: All admin actions logged to a dedicated CloudWatch log group (meridian-admin-audit) with 365-day retention
- **Session Management**: 4-hour session timeout, re-authentication required

### 3.4 Kong WebSocket Support

As of Kong Gateway 3.4 (released August 2024), WebSocket proxying is fully supported. The admin tool has not been migrated.

## 4. Traffic Statistics (Q4 2025)

| Endpoint | Daily Requests | Path |
|----------|---------------|------|
| Customer Dashboard | 4,200,000 | Standard (CloudFront → WAF → Kong → ALB) |
| Customer API | 18,500,000 | Standard (CloudFront → WAF → Kong → ALB) |
| Admin Tool | 8,200 | Direct (VPN → Internal ALB) |
| All other services | 6,800,000 | Standard |

Admin tool traffic represents 0.03% of total production traffic.

## 5. Security Exception

Exception SEC-EXC-2024-018 was filed in March 2024 for the admin tool boundary bypass. Status: Active. Last reviewed: September 2025. Next review: March 2026.
