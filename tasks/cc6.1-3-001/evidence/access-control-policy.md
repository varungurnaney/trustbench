# Access Control Policy

**Document ID:** POL-SEC-003
**Version:** 4.1
**Effective Date:** September 1, 2025
**Owner:** Information Security Team
**Classification:** Internal
**Last Reviewed:** December 15, 2025

---

## 1. Purpose

This policy establishes mandatory requirements for managing logical access to Meridian Cloud Systems' information assets. It ensures access is granted based on business need, enforced through technical controls, and verified through periodic review.

## 2. Scope

This policy applies to all personnel (employees, contractors, temporary workers) accessing Meridian production systems, cloud infrastructure (AWS), SaaS applications, source code repositories, databases, and internal tools.

## 3. Access Provisioning

### 3.1 Onboarding

- All access requests are initiated through Jira Service Management (JSM) upon HR onboarding trigger.
- Requests require documented business justification and manager approval before provisioning.
- Access is provisioned using role-based access control (RBAC) aligned to job function.
- Provisioning must be completed within 48 hours of approved request.
- Users must complete security awareness training before receiving production access.

### 3.2 Role Definitions

| Role | Systems | Approval Chain |
|------|---------|----------------|
| Standard User | Google Workspace, Confluence, Jira | Manager |
| Developer | GitHub, staging environments, CI/CD | Manager + Engineering Director |
| SRE / DevOps | AWS Console, Kubernetes, Terraform | Manager + VP Engineering + CISO |
| Database Admin | RDS, DynamoDB, Redshift | Manager + VP Engineering + CISO |
| Security Admin | IAM, CloudTrail, GuardDuty, SIEM | CISO |

### 3.3 Privileged Access

- All privileged access is brokered through AWS SSO with federated identity from Okta.
- Direct IAM user accounts in AWS are prohibited for human users.
- Root account credentials are secured in a physical safe; usage requires two-person authorization and is logged in CloudTrail.
- Break-glass accounts exist for emergency access; usage triggers an automatic PagerDuty alert and requires post-incident review within 24 hours.

### 3.4 Contractor and Temporary Access

- Contractor accounts must have an expiration date set at provisioning, not to exceed 90 days.
- Extensions require re-approval from the sponsoring manager and security review.
- Contractor access is limited to specific project resources; broad roles are prohibited.

## 4. Authentication

### 4.1 Identity Provider

- Okta is the centralized identity provider for all Meridian systems.
- All SaaS and internal applications must integrate with Okta SSO via SAML 2.0 or OIDC.
- Local application accounts are prohibited unless a documented exception exists.

### 4.2 Multi-Factor Authentication

MFA via Okta Verify (push notification or TOTP) is required for:
- All Okta-authenticated sessions (enforced at IdP level)
- AWS Console access (enforced via AWS SSO MFA policy)
- VPN connections
- GitHub (enforced at organization level)
- Any system accessing production data

### 4.3 Password and Credential Standards

- Minimum 14 characters for interactive accounts.
- API keys and service account credentials are stored in AWS Secrets Manager with automatic rotation every 90 days.
- SSH keys must be Ed25519; RSA keys below 4096 bits are rejected by policy.

## 5. Access Reviews

### 5.1 Quarterly Access Reviews

- System owners conduct quarterly access reviews for all production systems, cloud IAM, and SaaS applications.
- Reviews must be completed within 15 business days of initiation.
- Review evidence (screenshots, exported user lists, owner sign-off) is retained in Confluence for 3 years.

### 5.2 Review Process

1. IT Security generates current access lists from each system.
2. System owners verify each user's continued business need.
3. Users with no valid business need are flagged for removal.
4. Flagged access is revoked within 5 business days.
5. System owner signs off on the completed review in JSM ticket.

### 5.3 Privileged Access Reviews

- Privileged accounts (SRE, DBA, Security Admin) are reviewed monthly by the CISO.
- Review includes verification of role appropriateness and activity audit.

## 6. Access Revocation

### 6.1 Termination

- HR initiates an automated offboarding workflow in JSM upon termination decision.
- IT disables the Okta account within 4 hours of termination notification.
- Disabling Okta automatically revokes SSO access to all federated applications.
- IT explicitly revokes any non-federated access (local accounts, API keys, SSH keys) within 24 hours.
- Termination checklist must be completed and signed off by IT Security within 48 hours.

### 6.2 Role Changes

- Role changes trigger an access review via automated HR-to-JSM workflow.
- Previous role access is revoked before new role access is provisioned (revoke-before-grant).
- Completed role change reviews are documented in JSM.

## 7. Monitoring and Logging

- All authentication events are forwarded to Datadog SIEM.
- Failed login attempts trigger alerts after 3 consecutive failures.
- Anomalous access patterns (impossible travel, off-hours privileged access) generate automated alerts.
- CloudTrail logs all AWS API activity; logs are immutable and retained for 12 months.
- Weekly access anomaly reports are reviewed by IT Security.

## 8. Service Accounts and Non-Human Identities

- Service accounts must be registered in the CMDB with a designated owner.
- Service accounts are included in quarterly access reviews.
- Service account credentials rotate automatically via AWS Secrets Manager.
- Service accounts must follow least-privilege; wildcard IAM policies are prohibited.

## 9. Exceptions

- Exceptions require CISO approval with documented risk assessment and compensating controls.
- Exceptions are logged in the GRC tool (Drata) with a maximum duration of 6 months.
- Active exceptions are reviewed quarterly by the Security Governance Committee.

---

**Approved by:** Sarah Chen, CISO
**Next Review Date:** June 2026
