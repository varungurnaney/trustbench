# Stratos Cloud Solutions — Access Control Policy

**Document ID:** POL-AC-2025-003
**Version:** 3.8
**Effective Date:** February 1, 2025
**Last Review:** October 15, 2025
**Owner:** Wei Zhang, Chief Information Security Officer
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy defines the requirements for managing logical access to Stratos Cloud Solutions information systems and data assets across all environments.

## 2. Scope

This policy applies to all Stratos employees, contractors, and third-party service providers accessing Stratos information systems, including:

- Cloud infrastructure (AWS, us-east-1 and eu-west-1 regions)
- SaaS applications (Okta, Salesforce, Jira, Confluence, GitHub)
- Production databases (Amazon RDS PostgreSQL, Amazon DynamoDB)
- Monitoring infrastructure (Datadog, PagerDuty)

## 3. Access Provisioning and Identity Management

### 3.1 Identity Provider

All human user authentication is managed through Okta as the centralized identity provider. Direct application authentication is prohibited except where documented in the exception register.

### 3.2 Access Requests

Access requests must be submitted through the ServiceNow catalog (ACC-REQ-STRATOS). Each request requires:

- Business justification
- Role selection from the approved RBAC matrix
- Manager approval
- Data Owner approval for systems containing customer data

### 3.3 Privileged Access Management

Privileged access to production systems is managed through CyberArk:

- Just-in-time (JIT) access with maximum 2-hour session duration
- All privileged sessions are recorded and retained for 24 months
- Dual approval required (Manager + CISO)
- Privileged credentials rotated after each session checkout

### 3.4 Service Account Management

Service accounts must:

- Be registered in the Stratos CMDB with a designated human owner
- Use workload identity federation where supported
- Have credentials rotated every 90 days
- Follow the naming convention: svc-{application}-{function}

## 4. Authentication Controls

### 4.1 Multi-Factor Authentication

MFA is required for all Okta-authenticated sessions. Approved methods:

- FIDO2 security keys (required for administrators)
- Okta Verify with push notification
- TOTP-based authenticator apps

SMS-based authentication is prohibited.

### 4.2 Password Policy

- Minimum 14 characters with complexity requirements
- 90-day expiration cycle
- 20-password history enforcement
- Account lockout after 5 failed attempts (15-minute duration)

## 5. Access Reviews

### 5.1 Quarterly Reviews

System owners conduct quarterly access reviews within 15 business days of initiation. Reviews include:

- Verification of user access against current job function
- Identification of dormant accounts (no activity > 60 days)
- Validation of service account ownership
- Sign-off documented in ServiceNow

### 5.2 Privileged Access Reviews

Monthly review by CISO of all privileged access grants, including:

- Session recording spot-checks
- JIT access usage patterns
- Emergency access usage review

## 6. Access Revocation

### 6.1 Employee Termination

- HR triggers automated offboarding in ServiceNow
- Okta account suspended within 4 hours of termination notification
- AWS IAM access keys deactivated within 24 hours
- CyberArk credentials rotated immediately
- Physical badges collected on last working day

### 6.2 Contractor Offboarding

Contractor accounts are deprovisioned within 24 hours of contract end date. Accounts must have automated expiration dates set at provisioning time.

## 7. Monitoring and Logging

- All authentication events logged to Datadog with 12-month retention
- Failed login monitoring with automated SOC alerts (threshold: 10 failures in 10 minutes)
- Privileged session recordings in CyberArk (24-month retention)
- Weekly authentication anomaly review by Security Operations

## 8. Exceptions

Exceptions require CISO approval with documented compensating controls, time-bound to a maximum of 6 months, and reviewed quarterly.

---

**Approved by:** Wei Zhang, CISO
**Approved Date:** February 1, 2025
**Next Review Date:** February 2026
