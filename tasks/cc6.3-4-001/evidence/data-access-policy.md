# Aurora Labs — Data Access Authorization Policy

**Document ID:** POL-DAP-2024-003
**Version:** 3.2
**Effective Date:** January 15, 2024
**Last Review:** October 1, 2025
**Owner:** Priya Venkatesh, Chief Information Security Officer
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy establishes the requirements for authorizing, managing, and monitoring access to Aurora Labs data assets across all environments. It ensures that access is granted on a least-privilege basis, segregation of duties is enforced, and data exposure is minimized through appropriate technical controls.

## 2. Scope

This policy applies to all Aurora Labs employees, contractors, and third-party service providers who access Aurora Labs data systems, including but not limited to:

- Production databases (MongoDB Atlas clusters)
- Data warehouses (Snowflake)
- Application-layer data stores (Redis, Elasticsearch)
- File storage systems (AWS S3)
- Analytics platforms (Looker, internal dashboards)

## 3. Access Authorization Principles

### 3.1 Least Privilege

All data access shall be granted on a least-privilege basis. Users and service accounts must be provisioned with the minimum permissions necessary to perform their assigned duties. Broad or unrestricted access to production data is prohibited unless explicitly approved through the exception process (Section 7).

### 3.2 Segregation of Duties

No single individual shall possess access that allows them to both modify and approve changes to sensitive data. Specifically:

- Users with write access to financial data collections (`billing`, `invoices`, `revenue_records`, `payment_transactions`) must not simultaneously hold administrative or approval privileges on the same collections.
- Database administrators must not have application-level write access to business-critical data without a secondary approver.
- Development personnel must not have direct write access to production databases.

### 3.3 Role-Based Access Control (RBAC)

Access shall be managed through predefined roles aligned to job functions. Custom or ad-hoc permissions are prohibited. All roles must be documented in the Aurora Labs RBAC Matrix (maintained by IT Security) and reviewed quarterly.

## 4. Data Loss Prevention (DLP) Controls

### 4.1 Production Data Protection

All production environments must implement the following DLP controls:

- Field-level encryption for PII fields (SSN, payment card numbers, health records)
- Query audit logging with a minimum retention period of 12 months
- Data masking for any non-production access to production data replicas
- Automated alerts for bulk data export operations exceeding 10,000 records

### 4.2 Data Masking Requirements

Non-production environments that receive production data replicas must apply data masking to the following field categories:

- Personally Identifiable Information (PII)
- Payment Card Industry (PCI) data
- Protected Health Information (PHI)
- Authentication credentials and API keys

Data masking must be applied at the replication layer before data is written to non-production storage.

## 5. Access Certification

### 5.1 Quarterly Access Certification

All data access privileges must be reviewed and certified by the respective system owner on a quarterly basis. Certification must be completed within **14 calendar days** of the certification period opening.

### 5.2 Certification Process

1. IT Security generates an access report for each system at the start of each quarter.
2. System owners review current access grants against the RBAC Matrix.
3. System owners certify, modify, or revoke access as appropriate.
4. IT Security validates certifications and closes the review cycle.

### 5.3 Late Certification

Systems with certifications completed more than **14 calendar days** after the certification period opens are flagged as non-compliant. Repeated late certifications (two consecutive quarters) trigger an escalation to the CISO.

## 6. Service Accounts and Automation

### 6.1 Service Account Requirements

All service accounts must:

- Have a designated human owner documented in the service account registry
- Be scoped to the minimum permissions required for the automated workflow
- Have credentials rotated every 90 days
- Be reviewed as part of the quarterly access certification process

### 6.2 Contractor and Temporary Accounts

Contractor and temporary employee accounts must:

- Have a defined expiration date, not to exceed the contract end date or 90 days, whichever is shorter
- Be provisioned through the same RBAC process as full-time employees
- Be deprovisioned within 24 hours of contract termination

## 7. Exception Process

Exceptions to this policy may be granted by the CISO under the following conditions:

1. A formal exception request is submitted via the GRC portal
2. Compensating controls are identified and documented
3. The exception is time-bound (maximum 12 months)
4. The exception is reviewed and reauthorized at each quarterly access certification

All active exceptions are maintained in the Aurora Labs Exception Register.

## 8. Monitoring and Enforcement

IT Security maintains continuous monitoring of data access patterns and will investigate anomalies including:

- Access outside normal business hours without prior authorization
- Bulk data retrieval operations
- Privilege escalation attempts
- Access from unrecognized IP addresses or devices

## 9. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 3.2 | 2025-10-01 | P. Venkatesh | Updated DLP requirements, added data masking section |
| 3.1 | 2025-04-15 | P. Venkatesh | Clarified segregation of duties for financial collections |
| 3.0 | 2024-01-15 | M. Torres | Major revision — added RBAC, DLP, and certification sections |
