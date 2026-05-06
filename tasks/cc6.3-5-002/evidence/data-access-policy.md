# NovaBridge Technologies — Data Access Policy

**Document ID:** POL-DA-2025-015
**Version:** 3.0
**Effective Date:** March 1, 2025
**Last Review:** September 15, 2025
**Owner:** Angela Foster, Chief Information Security Officer
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy establishes requirements for authorizing and managing access to NovaBridge Technologies data assets, with specific provisions for contractor data access governance.

## 2. Scope

Applies to all employees, contractors, and third parties accessing NovaBridge data systems including production databases (PostgreSQL), analytics platforms (Redshift), and SaaS applications.

## 3. Data Classification

| Classification | Examples | Access Approval |
|---------------|----------|-----------------|
| Restricted | Customer PII, credentials, payment data | CISO + Data Owner + Privacy Officer |
| Confidential | Financial records, contracts, analytics | Data Owner + Manager |
| Internal | Product catalogs, feature usage, project docs | Manager |
| Public | Marketing, published APIs | Self-service |

## 4. Access Authorization

### 4.1 Least Privilege

All access follows least-privilege principles. Minimum permissions for specific job duties only.

### 4.2 RBAC

Predefined roles aligned to job functions. Custom roles prohibited without CISO exception.

### 4.3 Segregation of Duties

Write access to financial data requires dual approval. Development and production access segregated.

## 5. Employee Access

### 5.1 Provisioning

ServiceNow-based requests with approval chain per data classification. Provisioned within 2 business days.

### 5.2 Reviews

Quarterly access reviews by system owners within 15 business days.

## 6. Contractor Access

### 6.1 Pre-Provisioning Requirements

Before any data access is provisioned for a contractor, the following must be in place:

- Executed NDA on file in the NovaBridge NDA Register
- Active Statement of Work (SOW) with defined scope and end date
- Contractor sponsor identified (NovaBridge hiring manager)
- Background check completed

All contractors must have an executed NDA on file before data access is provisioned.

### 6.2 Individual Accountability

Each contractor must have an individual database account. Shared accounts for contractor teams are prohibited. All contractor activity must be attributable to a named individual for audit purposes.

### 6.3 Access Duration and Revocation

Contractor data access must be time-limited:

- Access duration must not exceed the SOW end date
- Access must be revoked within 48 hours of SOW completion or contract end date
- Contractor sponsor is responsible for notifying IT of SOW completion
- Monthly review of active contractor access by IT Security

### 6.4 NDA Requirements

All contractor NDAs must:

- Cover all data classifications the contractor may access
- Include specific data handling and return/destruction obligations
- Be reviewed annually to ensure terms remain appropriate and the contractor's data handling obligations are current
- Be retained for 7 years after contractor engagement ends

### 6.5 Contractor Access Reviews

Active contractor access is reviewed monthly by the contractor's NovaBridge sponsor. Reviews must verify:

- SOW is still active
- Access scope remains appropriate for current project phase
- NDA is current and on file
- No data exports outside approved channels

## 7. Monitoring

All data access logged with 18-month retention. Automated alerts for bulk queries (>10,000 records). Contractor access patterns reviewed weekly.

## 8. Exceptions

CISO-approved with compensating controls. Maximum 6 months. Reviewed quarterly.

---

**Approved by:** Angela Foster, CISO
**Next Review Date:** March 2026
