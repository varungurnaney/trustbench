# Access Control Policy

**Document ID:** POL-IAM-001
**Version:** 3.2
**Effective Date:** January 15, 2025
**Owner:** IT Security Team
**Classification:** Internal

---

## 1. Purpose

This policy establishes the requirements for managing logical access to NovaTech Solutions' information systems, applications, and data in alignment with the company's security objectives and regulatory requirements.

## 2. Scope

This policy applies to all employees, contractors, and third-party personnel who access NovaTech Solutions' production systems, internal applications, corporate network, and cloud infrastructure (AWS).

## 3. Access Provisioning

### 3.1 New User Access

- All access requests must be submitted via the ServiceNow ticketing system.
- Requests must include: business justification, requested role/permissions, and manager approval.
- The IT Security team reviews and provisions access within 2 business days of approved request.
- Users are assigned role-based access following the principle of least privilege.

### 3.2 Role Definitions

Access roles are defined as follows:

| Role | Description | Approval Required |
|------|-------------|-------------------|
| Standard User | Email, internal wiki, project tools | Manager |
| Developer | Code repositories, staging environments | Manager + Engineering Lead |
| Production Access | Production servers, databases | Manager + VP Engineering + Security |
| Administrator | Full system administration | CISO approval |

### 3.3 Privileged Access

- Privileged accounts (root, admin) are managed through CyberArk PAM.
- Shared accounts are prohibited. All privileged access must be tied to individual users.
- Privileged sessions are recorded and retained for 12 months.

## 4. Authentication

### 4.1 Password Requirements

- Minimum 12 characters
- Must include uppercase, lowercase, numbers, and special characters
- Passwords expire every 90 days
- Last 12 passwords cannot be reused

### 4.2 Multi-Factor Authentication

Multi-factor authentication (MFA) is required for:
- VPN access
- Cloud console access (AWS)
- Email access from non-corporate devices

## 5. Access Reviews

### 5.1 Periodic Reviews

Access reviews are conducted quarterly by system owners to verify that user access remains appropriate and aligned with job responsibilities.

### 5.2 Review Process

- System owners receive a list of current users and their assigned roles.
- Owners verify each user's continued need for access.
- Inappropriate or excessive access is revoked within 5 business days.
- Review completion is documented and retained.

## 6. Access Revocation

### 6.1 Termination

- Upon employee termination, HR notifies IT via email.
- IT disables the user's Active Directory account.
- Access to all systems should be removed in a timely manner.

### 6.2 Role Changes

- When an employee changes roles, the previous manager is responsible for notifying IT of any access that should be removed.

## 7. Monitoring

- Failed login attempts are logged and monitored.
- After 5 consecutive failed attempts, the account is locked for 30 minutes.
- Security team reviews authentication logs weekly.

## 8. Exceptions

Exceptions to this policy may be granted by the CISO on a case-by-case basis. All exceptions must be documented with a risk assessment and compensating controls.

---

**Approved by:** James Morton, CISO
**Next Review Date:** January 2026
