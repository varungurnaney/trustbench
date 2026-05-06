# Quorum Digital — Data Access Authorization Policy

**Document ID:** POL-DA-2025-001
**Version:** 1.4
**Effective Date:** June 1, 2025
**Owner:** IT Department
**Classification:** Internal

---

## 1. Purpose

This policy establishes guidelines for managing access to Quorum Digital's data systems and applications. It ensures that data access is properly authorized and managed throughout the employee lifecycle.

## 2. Scope

This policy applies to all Quorum Digital employees and contractors who access company data systems, including:

- Production databases (MySQL, PostgreSQL)
- Cloud storage (AWS S3)
- SaaS applications (Salesforce, HubSpot, Jira)
- Internal file shares and document repositories
- Analytics platforms (Looker, Tableau)

## 3. Access Authorization

### 3.1 Role-Based Access

Access to data systems is managed through role-based access control. Roles are defined and aligned to department needs. The following standard roles are maintained:

| Role | Access Level | Approval Required |
|------|-------------|-------------------|
| Standard User | Read access to department data | Manager |
| Power User | Read-write access to department data | Manager + Director |
| Administrator | Full access to assigned systems | VP + IT Director |
| Service Account | Automated system access | IT Director |

### 3.2 Access Request Process

All data access requests must be submitted through the IT Service Desk. Requests must include:

- Name and department of the requestor
- System(s) and role requested
- Business justification
- Manager approval

IT provisions access within 3 business days of approved request.

### 3.3 Contractor Access

Contractors are granted access based on their Statement of Work. Contractor access is provisioned for the duration of the engagement.

## 4. Data Protection

### 4.1 Production Data

Production databases contain sensitive data including customer information. Access to production data requires VP approval.

### 4.2 Data Exports

Data exports from production systems must be approved by the data owner. Exported data must be stored in approved locations only.

### 4.3 Non-Production Environments

Development and staging environments should use synthetic or anonymized data where possible.

## 5. Access Reviews

### 5.1 Periodic Reviews

Data access is reviewed quarterly by IT. Reviews confirm that current access remains appropriate for each user's role.

### 5.2 Review Documentation

Review results are documented and retained for 12 months.

## 6. Access Revocation

### 6.1 Employee Termination

Upon termination, all data access is revoked. HR notifies IT upon employee departure. IT disables accounts within 24 hours of notification.

### 6.2 Contractor Offboarding

Contractor access is removed at the end of the engagement period. IT verifies removal within 48 hours of contract end date.

## 7. Monitoring

Data access patterns are monitored for anomalies. Suspicious activity is reported to the IT Director for investigation.

## 8. Exceptions

Exceptions to this policy require written approval from the IT Director with documented business justification.

---

**Approved by:** Craig Hoffman, IT Director
**Next Review Date:** June 2026
