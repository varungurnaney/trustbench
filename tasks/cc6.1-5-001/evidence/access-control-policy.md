# Nimbus Health -- Access Control Policy

**Document ID:** NH-POL-AC-005  
**Version:** 3.1  
**Effective Date:** 2025-02-01  
**Last Reviewed:** 2025-08-20  
**Owner:** Kenji Nakamura, Director of Information Security  
**Approved By:** Dr. Alison Crawford, CISO  

---

## 1. Purpose

This policy defines the requirements for logical access controls across all Nimbus Health information systems, ensuring that access to protected health information (PHI), production systems, and corporate resources is appropriately managed in accordance with SOC 2 Trust Services Criteria CC6.1 and HIPAA Security Rule requirements.

## 2. Scope

This policy applies to all employees, contractors, temporary staff, and third-party service providers who access Nimbus Health information systems, including:

- Production cloud infrastructure (AWS us-east-1, us-west-2)
- Clinical data platforms and analytics systems
- Corporate applications (Slack, Google Workspace, Jira, Confluence)
- Source code repositories (GitHub Enterprise)
- Database systems (PostgreSQL, MongoDB Atlas)
- CI/CD pipelines (GitLab CI)

## 3. Identity and Access Management

### 3.1 Single Sign-On (SSO)

All Nimbus Health applications must be integrated with **Okta** as the centralized identity provider. Direct application authentication (local accounts) is prohibited for any system that supports SSO/SAML/OIDC integration.

Okta Configuration:
- **Okta Tenant:** nimbus-health.okta.com
- **Directory Integration:** Azure AD (nimbus-health.onmicrosoft.com) synced bi-directionally
- **Provisioning:** SCIM-based automated provisioning for supported applications
- **Session Policy:** 12-hour session lifetime, re-authentication required after 30 minutes of inactivity

### 3.2 Multi-Factor Authentication (MFA)

MFA is **required** for all Okta-authenticated sessions. Acceptable MFA factors:
- Okta Verify (push notification) -- preferred
- FIDO2/WebAuthn hardware keys (YubiKey 5 series)
- TOTP authenticator apps (Google Authenticator, Authy)

SMS-based MFA is **not permitted** due to SIM swapping risks.

### 3.3 Contractor Access

Contractor accounts must:
- Be created with a designated expiration date aligned with the contract end date
- Include the suffix `-contractor` in the Okta username (e.g., `jsmith-contractor@nimbus-health.com`)
- Be limited to only the applications required for their specific engagement
- Be reviewed monthly by the contractor's Nimbus Health sponsor

### 3.4 Service Accounts

All service accounts and non-human identities must be:
- Managed through **CyberArk Privileged Access Management** (CyberArk PAM)
- Assigned to an individual owner responsible for the account's lifecycle
- Rotated credentials every 90 days (automated via CyberArk)
- Documented in the CyberArk vault with purpose, owner, and associated systems

## 4. Access Provisioning

### 4.1 Access Request Process

All access requests must follow this workflow:
1. User submits request via ServiceNow (catalog item: "Access Request")
2. Manager approval (automatic for role-based standard access packages)
3. Application owner approval (for privileged or non-standard access)
4. IT Operations provisioning via Okta SCIM or manual assignment
5. Confirmation notification sent to requester and manager

### 4.2 Least Privilege Principle

Access must be granted based on the principle of least privilege:
- Users receive only the minimum permissions required for their role
- Role-based access control (RBAC) profiles are defined for each department
- Elevated or privileged access requires additional approval and justification
- Standing privileged access is limited; just-in-time (JIT) access via CyberArk is preferred

## 5. Access Reviews

### 5.1 Quarterly Access Reviews

Access reviews shall be conducted **quarterly** for all production systems. Each review must:

- Be completed within 15 business days of initiation
- Be performed by an authorized reviewer (typically the application owner or delegate)
- Verify that all active accounts are associated with current employees or authorized contractors
- Validate that access levels are appropriate for current job responsibilities
- Identify and remediate any unauthorized or excessive access
- Be documented with reviewer name, date, findings, and remediation actions

### 5.2 Systems Subject to Quarterly Review

| System | Reviewer | Review Quarter |
|--------|----------|---------------|
| AWS Console (Production) | Cloud Infrastructure Lead | Q1, Q2, Q3, Q4 |
| PostgreSQL (Clinical DB) | Database Administration Lead | Q1, Q2, Q3, Q4 |
| MongoDB Atlas | Data Platform Lead | Q1, Q2, Q3, Q4 |
| GitHub Enterprise | Engineering Manager | Q1, Q2, Q3, Q4 |
| CyberArk PAM | Security Operations Lead | Q1, Q2, Q3, Q4 |
| Okta (Admin Console) | IAM Team Lead | Q1, Q2, Q3, Q4 |
| Salesforce | Sales Operations Manager | Q1, Q2, Q3, Q4 |
| Snowflake | Data Engineering Lead | Q1, Q2, Q3, Q4 |
| Jira/Confluence | IT Operations Manager | Q1, Q2, Q3, Q4 |
| Google Workspace | IT Operations Manager | Q1, Q2, Q3, Q4 |
| Stripe (Billing) | Finance Systems Lead | Q1, Q2, Q3, Q4 |
| PagerDuty | SRE Lead | Q1, Q2, Q3, Q4 |

## 6. Access Termination

### 6.1 Employee Termination

Upon notification of employee termination (voluntary or involuntary):

1. HR notifies IT Operations and Information Security via automated BambooHR webhook
2. Okta account must be **disabled within 24 hours** of the termination effective date
3. All active sessions must be terminated immediately upon Okta account disablement
4. Access to sensitive systems (AWS, databases, CyberArk) confirmed revoked
5. Company-managed devices collected or remotely wiped
6. Termination completion logged in ServiceNow with confirmation timestamp

### 6.2 Contractor Offboarding

Contractor access must be revoked:
- On the contract end date (automated via Okta account expiration)
- Immediately upon early contract termination
- Within 24 hours of sponsor notification

## 7. Privileged Access Management

### 7.1 CyberArk Implementation

CyberArk PAM is used for all privileged access:
- **Vault:** cyberark-vault-prod-01.nimbus-health.internal
- **PVWA:** https://pam.nimbus-health.com
- **PSM:** Session recording enabled for all privileged sessions
- **Password Rotation:** Every 90 days for service accounts, after each use for breakglass accounts

### 7.2 Breakglass Procedures

Emergency access (breakglass) accounts are available for critical system recovery:
- Stored in CyberArk with dual-control access (two approvers required)
- Usage triggers immediate PagerDuty alert to Security Operations
- All breakglass sessions are recorded and reviewed within 24 hours

## 8. Monitoring and Logging

- All authentication events are logged to Splunk (index: nimbus_auth_events)
- Failed authentication attempts trigger alerting after 5 consecutive failures
- Privileged session recordings retained for 12 months
- Access review completion status monitored via ServiceNow dashboard

## 9. Policy Review

This policy is reviewed annually or upon significant changes to the identity management infrastructure.

---

*Document Classification: Internal -- Restricted*  
*HIPAA Security Rule: 45 CFR 164.312(a)(1), 164.312(d)*
