# Data Classification and Protection Policy

**Document ID:** POL-DCP-003
**Version:** 4.0
**Effective Date:** February 1, 2025
**Owner:** Data Governance Team
**Classification:** Internal
**Organization:** Crestline Data Systems

---

## 1. Purpose

This policy establishes requirements for classifying, labeling, and protecting data based on sensitivity to ensure Crestline Data Systems meets its confidentiality obligations to customers, regulators, and business partners.

## 2. Scope

This policy applies to all data created, received, processed, or stored by Crestline Data Systems across all environments including production databases, cloud storage, SaaS applications, and endpoint devices.

## 3. Classification Framework

### 3.1 Classification Levels

| Level | Description | Encryption Requirement |
|-------|-------------|----------------------|
| Public | Non-sensitive, freely distributable | None required |
| Internal | Business data, low disclosure risk | Encryption in transit required |
| Confidential | Business-critical, customer data | Encryption in transit and at rest required |
| Restricted | PII, PHI, payment data, credentials | Encryption in transit and at rest required; field-level encryption for PII columns |

### 3.2 PII Data Elements

The following are classified as Restricted and require field-level encryption in all database storage:

- Social Security Numbers (SSN)
- Date of birth
- Email addresses
- Phone numbers
- Physical addresses
- Financial account numbers
- Government-issued ID numbers

### 3.3 Data Ownership

Each data element must have a designated Data Owner responsible for classification accuracy and protection compliance.

## 4. Protection Requirements

### 4.1 Database Storage

- All Restricted data columns must use AES-256 field-level encryption via the application encryption layer.
- Encryption keys for field-level encryption are managed in AWS KMS with customer-managed keys (CMK).
- Database-level encryption (TDE or AWS RDS encryption) must be enabled for all databases containing Confidential or Restricted data.

### 4.2 Cloud Storage

- S3 buckets containing Confidential or Restricted data must have SSE-KMS encryption enabled with customer-managed keys.
- Public access must be blocked at the bucket and account level.
- Object-level logging must be enabled for Restricted data buckets.

### 4.3 Data Exports

- All data exports containing Restricted data must be encrypted before transmission.
- Automated exports must use encrypted channels (SFTP, TLS-encrypted API calls).
- Manual exports of Restricted data require Data Owner approval and must be encrypted with PGP or equivalent.

## 5. Data Loss Prevention

### 5.1 DLP Coverage

DLP rules must be configured to detect and prevent unauthorized transmission of Restricted data across:

- Email (Microsoft 365 DLP)
- Cloud storage uploads (CASB - Netskope)
- Web uploads and paste operations (Endpoint DLP)
- API data exports (API Gateway DLP rules)
- Database query result sets exceeding threshold (Database Activity Monitoring)

### 5.2 DLP Response Actions

- Alert: Notify the Security Operations Center for review
- Block: Prevent transmission and notify the user and their manager
- Quarantine: Hold content for Security team review before release

## 6. Data Flow Documentation

All systems processing Restricted data must have documented data flow diagrams reviewed annually. New data flows involving Restricted data require Data Protection Impact Assessment (DPIA) approval.

## 7. Compliance

Non-compliance with this policy will be treated as a security incident and escalated per the Incident Response Plan.

---

**Approved by:** Rachel Nguyen, CISO
**Next Review Date:** February 2026
