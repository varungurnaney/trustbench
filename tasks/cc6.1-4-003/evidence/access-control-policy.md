# Helios Data Systems — Access Control Policy

**Document ID:** POL-AC-2024-007
**Version:** 5.0
**Effective Date:** January 1, 2025
**Last Review:** October 1, 2025
**Owner:** Anil Kapoor, Chief Information Security Officer
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy establishes requirements for managing logical access to Helios Data Systems information systems, with emphasis on privileged access management and emergency access procedures.

## 2. Scope

This policy applies to all Helios employees, contractors, and third-party personnel accessing Helios production systems, cloud infrastructure (AWS), databases (Amazon RDS, Amazon DynamoDB), and SaaS applications.

## 3. Identity and Access Management

### 3.1 Identity Provider

All human user authentication is managed through Okta SSO. Direct application authentication is prohibited.

### 3.2 Access Provisioning

- All access requests submitted via ServiceNow (catalog item: ACC-HELIOS-001)
- RBAC-based provisioning aligned to job function
- Manager approval required; Data Owner + CISO approval for privileged roles
- Provisioning completed within 2 business days

## 4. Authentication

### 4.1 MFA Requirements

MFA is mandatory for all Okta-authenticated sessions. Approved methods: FIDO2 security keys (required for privileged users), Okta Verify push, TOTP applications. SMS-based MFA is prohibited.

### 4.2 Password Policy

Minimum 16 characters, complexity enforcement, 90-day rotation, 24-password history, lockout after 5 failures.

## 5. Privileged Access Management

### 5.1 CyberArk Privileged Access

All privileged access to production systems must be brokered through CyberArk PAM:

- Just-in-time (JIT) access with a maximum session duration of 2 hours
- Each checkout must reference an approved ServiceNow ticket (RITM or CHG number)
- All sessions are recorded and retained for 24 months
- Credentials are rotated after each session checkout
- Dual approval (Manager + CISO) required for privileged checkouts
- CyberArk enforces automatic session termination at the maximum duration

### 5.2 Privileged Access Reviews

Monthly review of all privileged access sessions by the CISO, including:

- Validation of ticket references for each checkout
- Session recording spot-checks (minimum 10% sample)
- Identification of anomalous usage patterns

## 6. Access Reviews and Revocation

### 6.1 Quarterly Access Reviews

System owners conduct quarterly reviews within 15 business days. Dormant accounts (no activity > 45 days) flagged for revocation.

### 6.2 Termination

Okta suspended within 4 hours; all privileged credentials rotated immediately; AWS IAM removed within 24 hours.

## 7. Emergency (Break-Glass) Access

### 7.1 Applicability

Break-glass access is reserved for SEV-1 and SEV-2 production incidents where normal privileged access channels are unavailable or insufficient.

### 7.2 Break-Glass Procedure

1. Requestor contacts CISO and VP Engineering for dual verbal authorization
2. Break-glass credential retrieved from CyberArk vault "HELIOS-BREAKGLASS-PROD"
3. PagerDuty incident ID recorded at time of checkout
4. All actions during break-glass session are logged to a separate immutable audit trail
5. Post-incident review of all break-glass actions must be completed within 5 business days
6. Break-glass credentials are rotated immediately after session completion
7. Post-incident review must document: systems accessed, actions taken, data exposed, and justification

### 7.3 Root Account Usage

AWS root account usage is permitted only via the break-glass procedure. Root credentials are stored in a physical safe with dual-custody controls.

## 8. Monitoring

- All authentication events logged to Splunk (12-month retention)
- CyberArk session recordings retained 24 months
- Break-glass usage triggers immediate PagerDuty alert to CISO
- Weekly privilege usage reports reviewed by Security Operations

## 9. Exceptions

CISO-approved exceptions with compensating controls, time-bound to 6 months maximum, reviewed quarterly.

---

**Approved by:** Anil Kapoor, CISO
**Approved Date:** January 1, 2025
**Next Review Date:** January 2026
