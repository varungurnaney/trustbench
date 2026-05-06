# Cascade Analytics — Access Control Policy

**Document ID:** POL-AC-2025-014
**Version:** 3.5
**Effective Date:** March 1, 2025
**Last Review:** September 15, 2025
**Owner:** Rebecca Thornton, Chief Information Security Officer
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy establishes the requirements for managing logical access to Cascade Analytics information systems. Cascade handles customer PII for enterprise analytics engagements, making access control critical to data protection obligations.

## 2. Scope

This policy applies to all Cascade employees, contractors, and third-party personnel accessing:

- Identity provider (Okta)
- Cloud infrastructure (AWS)
- SaaS applications (Jira, Confluence, Slack, Datadog, PagerDuty, Zoom, GitHub)
- Production databases (Amazon RDS PostgreSQL, Amazon Redshift)
- Customer data processing platform (Cascade DataEngine)

## 3. Access Provisioning

### 3.1 Identity Provider

All human user authentication managed through Okta SSO. Direct application authentication prohibited.

### 3.2 Access Requests

ServiceNow-based access request workflow. RBAC provisioning with Manager approval. Data Owner + CISO approval for customer data access.

### 3.3 Contractor Access

Contractor accounts must:

- Have a defined expiration date aligned to contract end date
- Be sponsored by a Cascade hiring manager
- Be reviewed monthly by the contractor's sponsor
- Be deprovisioned within 24 hours of contract termination

## 4. Authentication

### 4.1 MFA

MFA required for all Okta sessions. FIDO2 keys for privileged users. SMS prohibited.

### 4.2 Password Policy

Minimum 14 characters, 90-day rotation, account lockout after 5 failures.

## 5. Access Reviews

### 5.1 Quarterly Access Reviews

All system access must be reviewed quarterly. Reviews must be completed within 15 business days of initiation. Reviews may be performed by system owners or designated independent reviewers.

### 5.2 Review Requirements

Reviewers must verify each user's continued need for access by:

1. Confirming the user is still employed or under active contract
2. Verifying the access level matches the user's current role
3. Flagging dormant accounts (no login activity exceeding 90 days) for revocation
4. Identifying privilege accumulation from role changes
5. Validating service account ownership and continued business need

### 5.3 Review Evidence

Each review must produce documented evidence including:

- List of all accounts reviewed
- Disposition for each account (certified, modified, revoked, flagged)
- Reviewer signature and completion date
- Remediation tracking for identified issues

### 5.4 Review Oversight

IT Security performs quality assurance on a sample of completed reviews each quarter. QA checks include:

- Verification that the reviewer applied the criteria in Section 5.2
- Cross-reference of review results against HR data
- Spot-check of dormant account identification

## 6. Access Revocation

### 6.1 Termination

Okta suspended within 24 hours. All cloud access removed within 24 hours. CyberArk credentials rotated immediately.

### 6.2 Contractor Offboarding

Contractor accounts deprovisioned within 24 hours of contract end date per Section 3.3.

## 7. Monitoring

All authentication events logged to Splunk (12-month retention). Failed login monitoring. Weekly anomaly review.

## 8. Exceptions

CISO-approved with compensating controls. Time-bound to 6 months. Reviewed quarterly.

---

**Approved by:** Rebecca Thornton, CISO
**Next Review Date:** March 2026
