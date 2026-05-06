# Change Management Policy

**Document ID:** POL-CHG-024
**Version:** 3.0
**Effective Date:** February 15, 2025
**Owner:** Engineering
**Approved By:** Hana Otsuki, VP Engineering

---

## 1. Purpose

This policy governs all changes to Prism Health Technologies production systems to ensure controlled and authorized modifications that maintain patient data integrity, system availability, and HIPAA compliance.

## 2. Change Categories

| Category | Description | Approval | Deployment Window |
|----------|-------------|----------|--------------------|
| Standard | Pre-approved per Standard Change Catalog | None required | Business hours or maintenance window |
| Normal | Non-routine changes | CAB approval | Saturday 01:00-05:00 UTC |
| Emergency | Active Sev 1/2 remediation | VP Eng + Compliance Officer dual approval; retro CAB within 3 business days | Any time |

## 3. Change Request Process

### 3.1 Submission

All Normal and Emergency changes require a Jira ticket (project: CHG) with:
- Description, scope, and business justification
- Risk classification (Low / Medium / High / Critical)
- Impact assessment including affected PHI data flows
- Rollback plan
- Testing evidence

Standard changes must be logged in Jira but do not require the full submission template.

### 3.2 Testing

- All Normal changes must be tested in staging environment
- Automated test suite must pass with minimum 96% pass rate
- Changes affecting PHI data flows require data integrity validation
- Test results attached to Jira

### 3.3 CAB

Weekly meeting on Wednesdays at 11:00 AM ET.
- Members: VP Engineering (Chair), Director of SRE, Security & Compliance Lead, Clinical Data Manager
- Quorum: VP Engineering + 2 other members

### 3.4 Segregation of Duties

- Developer must not approve or deploy their own change
- SRE team executes all production deployments
- Peer review required for code changes

### 3.5 Post-Implementation

- Verification within 1 hour
- PHI data integrity check for changes affecting patient data
- Sign-off in Jira

## 4. Standard Change Catalog

Pre-approved changes that follow documented, repeatable procedures:

| ID | Change Type | Conditions | Scope Limitation |
|----|-------------|------------|-----------------|
| SC-001 | OS security patches (non-kernel) | Auto-rollback enabled; applied during maintenance window | Patches published by OS vendor only |
| SC-002 | SSL/TLS certificate renewal | Automated via cert-manager; no manual intervention | Standard certificate rotation only |
| SC-003 | Dependency updates (patch versions only) | All CI tests pass; no API changes; patch version only (x.y.Z) | Third-party library patch updates only |
| SC-004 | Monitoring alert threshold adjustments | PagerDuty/Datadog configuration only | Alert configuration changes; no new integrations |
| SC-005 | Log rotation and retention updates | Configuration-only; no code changes | Retention period changes within approved range (30-365 days) |

### 4.1 Standard Change Catalog Governance

The Standard Change Catalog is reviewed semi-annually by the CAB. Changes to the catalog (adding, modifying, or removing entries) require CAB approval.

Any change that does not clearly fall within the scope and conditions of a catalog entry must be submitted as a Normal change.

---

**Next Review Date:** February 2026
