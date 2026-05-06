# Pinnacle Financial Services — Access Control Policy

**Document ID:** POL-AC-2025-001
**Version:** 4.1
**Effective Date:** March 15, 2025
**Last Review:** September 30, 2025
**Owner:** Sandra Mitchell, Chief Information Security Officer
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy establishes the requirements for managing logical access to Pinnacle Financial Services' information systems, applications, and data. It applies to all environments including production, staging, development, and disaster recovery.

## 2. Scope

This policy applies to all Pinnacle Financial Services employees, contractors, temporary workers, and third-party personnel who access Pinnacle information systems, including:

- Core banking platform (Temenos T24)
- Cloud infrastructure (AWS)
- Customer data stores (PostgreSQL, Redis)
- Internal applications (ServiceNow, Confluence, Jira)
- Communication platforms (Microsoft 365, Slack)

## 3. Access Provisioning

### 3.1 New User Access

All access requests must be submitted through the ServiceNow Access Request workflow (catalog item: ACC-REQ-001). Requests must include:

- Business justification
- Requested role from the approved RBAC matrix
- Manager approval
- Data Owner approval for Confidential or Restricted data access

Access is provisioned within 2 business days of final approval.

### 3.2 Role Definitions

Access roles are managed through the Pinnacle RBAC Matrix (maintained by IT Security). Custom or ad-hoc permissions are prohibited.

**Table 3-1: Access Provisioning Requirements by User Type**

| User Type | Identity Provider | Approval Chain | Access Duration | Notes |
|-----------|------------------|----------------|-----------------|-------|
| Full-Time Employee | Okta SSO | Manager + Data Owner | Indefinite (subject to quarterly review) | Standard onboarding |
| Temporary Employee | Okta SSO | Manager + HR + Data Owner | Contract duration (max 12 months) | Auto-expiration required |
| Contractor (on-site) | Okta SSO | Manager + Vendor Manager + Data Owner | SOW duration (max 6 months) | Quarterly re-certification |
| Contractor (remote) | Okta SSO or Client VPN ^3 | Manager + Vendor Manager | SOW duration | See footnote 3 |
| Third-Party Integration | API Key / OAuth | Data Owner + CISO | 12 months (renewable) | Annual review required |

^1 All roles require minimum Manager approval.
^2 Temporary employees require HR validation of contract dates.
^3 Contractors accessing via client-provided VPN tunnel are exempt from MFA where the contractor's home organization enforces equivalent authentication controls.

### 3.3 Privileged Access

Privileged accounts are managed through CyberArk Privileged Access Manager:

- All privileged sessions are recorded and retained for 18 months
- Privileged access requires dual approval (Manager + CISO)
- Just-in-time (JIT) access is enforced with a maximum session duration of 4 hours
- Privileged credentials are rotated after every use

## 4. Authentication

### 4.1 Password Requirements

All human user accounts must comply with the following password standards:

- Minimum 16 characters
- Must include uppercase, lowercase, numbers, and special characters
- Passwords expire every 90 days
- Last 24 passwords cannot be reused
- Account lockout after 5 consecutive failed attempts (30-minute lockout duration)

### 4.2 Multi-Factor Authentication

Multi-factor authentication is required for all users accessing Pinnacle systems. Acceptable MFA methods include:

- FIDO2 hardware security keys (preferred)
- Okta Verify push notifications
- TOTP authenticator applications

SMS-based MFA is prohibited.

### 4.3 Session Management

- Idle session timeout: 15 minutes for production systems, 30 minutes for non-production
- Concurrent sessions limited to 3 per user
- Session tokens expire after 8 hours regardless of activity

## 5. Access Reviews

### 5.1 Quarterly Access Reviews

Access reviews are conducted quarterly by system owners. Reviews must be completed within 15 business days of initiation. The review process includes:

1. IT Security generates an access report for each system
2. System owners review current access against the RBAC matrix
3. Inappropriate or excessive access is revoked within 5 business days
4. Review completion is documented with sign-off in ServiceNow

### 5.2 Privileged Access Reviews

Privileged access is reviewed monthly by the CISO. Reviews include:

- Verification of business need for each privileged account
- Review of privileged session recordings (sample-based)
- Confirmation of JIT access enforcement

## 6. Access Revocation

### 6.1 Termination

Upon employee termination:

- HR triggers automated offboarding workflow in ServiceNow
- Okta account is suspended within 4 hours of termination notification
- All AWS IAM bindings are removed within 24 hours
- CyberArk privileged credentials are rotated immediately
- Physical access badges are collected on the last day

### 6.2 Role Changes

When an employee changes roles:

- The previous manager submits an access modification request
- IT Security reviews and adjusts access within 5 business days
- Previous role access is revoked before new role access is granted

## 7. Incident and Emergency Procedures

### 7.1 Suspicious Activity Response

Failed login attempts exceeding 10 in a 15-minute window trigger an automated alert to the SOC.

### 7.2 Compromised Credential Response

If a credential is suspected compromised:

- SOC immediately disables the account
- CISO is notified within 30 minutes
- Forensic review initiated within 2 hours

### 7.3 Emergency Access Procedure

In the event of a critical production incident (Severity 1 or Severity 2):

- Any member of the SRE team may invoke emergency access using the break-glass procedure
- Emergency access is obtained by checking out the shared emergency credential from CyberArk vault "PFS-EMERGENCY-PROD"
- The requestor must reference an active PagerDuty incident (incident ID required at checkout)
- Emergency access grants full administrative privileges to the production environment
- Post-incident review of actions taken during emergency access is recommended within 5 business days
- The SRE team lead is responsible for ensuring the incident report includes a summary of systems accessed

## 8. Service Accounts and Non-Human Identities

### 8.1 Service Account Governance

All service accounts must:

- Be registered in the Pinnacle CMDB with a designated human owner
- Have a documented business purpose
- Be included in the quarterly access review process
- Be named using the convention: svc-{application}-{function}

### 8.2 API Keys and Tokens

- API keys for third-party integrations are managed through AWS Secrets Manager
- Keys are rotated every 90 days
- Key usage is logged and monitored

## 9. Monitoring and Logging

- All authentication events are logged to Splunk with a 12-month retention period
- Failed authentication attempts are monitored in real-time by the SOC
- Privileged session recordings are stored in CyberArk with 18-month retention
- Weekly authentication anomaly reports are reviewed by IT Security

## 10. Exceptions

Exceptions to this policy may be granted by the CISO under the following conditions:

1. A formal exception request is submitted via ServiceNow (catalog item: SEC-EXC-001)
2. Compensating controls are identified and documented
3. The exception is time-bound (maximum 6 months)
4. The exception is reviewed at each quarterly access review

All active exceptions are maintained in the Pinnacle Security Exception Register.

---

**Approved by:** Sandra Mitchell, CISO
**Approved Date:** March 15, 2025
**Next Review Date:** March 2026
