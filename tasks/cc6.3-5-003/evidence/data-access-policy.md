# Meridian Insights — Data Access and DLP Policy

**Document ID:** POL-DLP-2025-002
**Version:** 2.8
**Effective Date:** January 15, 2025
**Last Review:** October 1, 2025
**Owner:** Patricia Wolfe, Chief Information Security Officer
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy establishes requirements for data access authorization and data loss prevention (DLP) controls at Meridian Insights. As a business intelligence services provider handling enterprise client data, preventing unauthorized bulk data access and export is critical to client trust and contractual obligations.

## 2. Scope

Applies to all employees, contractors, and service accounts accessing Meridian data systems including production databases (PostgreSQL), data warehouses (Redshift), analytics platforms (Looker), and file storage (S3).

## 3. Data Classification

| Classification | Examples |
|---------------|----------|
| Restricted | Client PII, credentials, payment data |
| Confidential | Client engagement data, analytics results, financial records |
| Internal | Product data, project docs |
| Public | Marketing, published reports |

## 4. Access Authorization

### 4.1 Least Privilege

All access follows least-privilege principles. Users receive minimum permissions for their specific duties.

### 4.2 RBAC

Predefined roles. Custom permissions require CISO exception.

### 4.3 Approval Chain

- Internal: Manager
- Confidential: Manager + Data Owner
- Restricted: Manager + Data Owner + Privacy Officer + CISO

## 5. Data Loss Prevention Controls

### 5.1 Bulk Export Authorization

Any export of data from production or warehouse environments to external storage (S3 export, CSV download, API bulk retrieval) requires prior approval:

- Exports under 1,000 rows: Manager approval via ServiceNow
- Exports 1,000 - 10,000 rows: Data Owner approval
- Exports over 10,000 rows: Data Owner + CISO approval

Approval must be obtained prior to export execution.

### 5.2 Automated DLP Alerting

The DLP system generates alerts for:

- Queries returning more than 10,000 rows from Restricted or Confidential tables
- SELECT INTO or COPY operations to external destinations
- Data access outside normal business hours (7 AM - 7 PM EST) for non-service accounts

### 5.3 Alert Response

All DLP alerts must be reviewed by a Security Analyst within 4 hours. The analyst must:

1. Verify the query context and business justification
2. Check for a corresponding export approval ticket
3. Escalate to CISO if no justification or approval exists
4. Document the disposition in the DLP alert log

### 5.4 DLP Technology

DLP enforcement is implemented through:

- PostgreSQL query audit logging (pgAudit extension)
- Amazon Redshift query monitoring rules
- S3 bucket policies with export event triggers
- CloudWatch alerting with SNS notification to the SOC

## 6. Access Reviews

Quarterly reviews within 15 business days. Monthly review of DLP alert trends by CISO.

## 7. Monitoring

All data access logged with 18-month retention. DLP alerts retained for 24 months. Weekly DLP trend report reviewed by Security Operations.

## 8. Exceptions

CISO-approved with compensating controls. Maximum 6 months. Reviewed quarterly.

---

**Approved by:** Patricia Wolfe, CISO
**Next Review Date:** January 2026
