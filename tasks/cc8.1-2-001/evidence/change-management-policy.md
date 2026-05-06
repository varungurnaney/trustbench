# Change Management Policy

**Document ID:** POL-CHG-009
**Version:** 3.0
**Effective Date:** April 1, 2025
**Owner:** Engineering
**Approved By:** Lisa Nguyen, VP Engineering

---

## 1. Purpose

This policy governs all changes to NovaCrest Technologies production systems, infrastructure, and applications to ensure stability, security, and compliance with SOC 2 Trust Services Criteria.

## 2. Scope

All changes to production environments, including application deployments, infrastructure modifications, database schema changes, network configuration updates, and third-party integration changes.

## 3. Change Categories

| Category | Description | Approval Required | Implementation Window |
|----------|-------------|-------------------|-----------------------|
| Standard | Pre-approved routine changes per Standard Change Catalog | None (pre-approved) | Business hours |
| Normal | Non-routine changes with assessed impact | CAB approval | Maintenance window (Sunday 01:00-05:00 UTC) |
| Emergency | Urgent production fixes for active Severity 1/2 incidents | VP Engineering verbal + retrospective CAB within 72 hours | Any time |

## 4. Change Request Process

### 4.1 Submission

All change requests must be submitted via ServiceNow (module: Change Management) with:
- Description and scope of the change
- Business justification
- Impact assessment (systems, users, data)
- Rollback plan
- Risk classification (Low / Medium / High / Critical)

### 4.2 Peer Review

All code changes require at least one peer review approval from a qualified engineer who is not the author. Peer review must be completed in GitHub before merge.

### 4.3 Testing

Prior to production deployment, changes should be validated in the staging environment. Testing in staging is recommended to confirm that the change functions as expected and does not introduce regressions.

For High and Critical risk changes, Security team review is required.

### 4.4 Approval

- Standard changes: auto-approved per the Standard Change Catalog.
- Normal changes: reviewed and approved at the weekly CAB meeting (Thursdays at 3pm ET).
- Emergency changes: VP Engineering verbal approval; ServiceNow ticket created retroactively.

### 4.5 Deployment

All deployments use the CI/CD pipeline (GitHub Actions → staging → production). Production deployments are executed by the SRE team.

### 4.6 Post-Implementation Review

Change owner verifies successful deployment within 2 hours. Post-implementation verification is recorded in the ServiceNow ticket.

## 5. Standard Change Catalog

The following changes are pre-approved and do not require CAB review:

| ID | Change Type | Conditions |
|----|-------------|------------|
| SC-001 | OS security patches (non-kernel) | Applied during maintenance window; auto-rollback enabled |
| SC-002 | SSL/TLS certificate renewal | Automated via cert-manager |
| SC-003 | Log rotation policy updates | Configuration-only; no code changes |
| SC-004 | Dependency updates (minor/patch versions) | Passes all CI tests; no API changes |
| SC-005 | Feature flag toggle (enable/disable) | Pre-approved features only; monitored for 30 minutes post-toggle |
| SC-006 | CDN cache invalidation | Performed via Cloudflare dashboard or API |
| SC-007 | Database index optimization | Non-blocking operations only; executed during low-traffic hours |
| SC-008 | Monitoring threshold adjustments | Datadog/PagerDuty alert configuration changes |
| SC-009 | Firewall rule updates for known services | Pre-approved IP ranges and port configurations |

## 6. Change Advisory Board (CAB)

The CAB consists of:
- VP Engineering (Chair)
- Director of SRE
- Security Engineering Lead
- Product Manager (for customer-impacting changes)

Quorum: VP Engineering + at least 2 other members.

## 7. Change Freeze

Code freezes are enforced during:
- 48 hours before and after major releases
- Holiday periods (Thanksgiving week, December 23 - January 3)

Emergency changes during freeze require CISO approval.

## 8. Rollback

All changes must include a documented rollback plan. Rollback must be initiated within 30 minutes if post-deployment health checks fail.

---

**Next Review Date:** April 2026
