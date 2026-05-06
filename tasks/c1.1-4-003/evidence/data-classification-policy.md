# Data Classification and Handling Policy

**Document ID:** POL-DCH-004
**Version:** 3.1
**Effective Date:** March 15, 2025
**Owner:** Data Governance Office
**Classification:** Internal
**Organization:** Pinnacle Analytics Group

---

## 1. Purpose

This policy establishes requirements for classifying, labeling, handling, and disposing of data at Pinnacle Analytics Group to protect confidential information and maintain compliance with SOC 2 confidentiality criteria.

## 2. Scope

All data created, collected, processed, transmitted, stored, or disposed of by Pinnacle Analytics Group, in all formats (digital and physical) and across all environments.

## 3. Classification Levels

| Level | Description | Handling Requirements |
|-------|-------------|----------------------|
| Public | Non-sensitive, approved for external distribution | No restrictions |
| Internal | General business information | Encrypted in transit; access restricted to employees |
| Confidential | Business-sensitive, customer data | Encrypted in transit and at rest; access logged; need-to-know basis |
| Restricted | PII, financial data, credentials, health data | Encrypted in transit and at rest; field-level encryption; DLP monitoring; access logged and alerted |

## 4. Data Inventory

### 4.1 Data Inventory Requirement

All systems processing Confidential or Restricted data must be registered in the Data Asset Inventory with:
- Data owner
- Data classification
- Retention period
- Encryption status
- Access control mechanism

### 4.2 Data Asset Inventory Review

The Data Governance Office reviews the Data Asset Inventory quarterly to ensure completeness and accuracy.

## 5. Encryption Requirements

### 5.1 Data in Transit

- All Confidential and Restricted data must be encrypted in transit using TLS 1.2 or higher.
- Internal microservice communication handling Restricted data must use mTLS.

### 5.2 Data at Rest

- All Confidential and Restricted data must be encrypted at rest using AES-256.
- Database-level encryption must be enabled for all production databases.
- Field-level encryption is required for all Restricted PII columns.

### 5.3 Data in Use

- Restricted data must not be displayed in application logs.
- Query result caching of Restricted data is prohibited unless the cache is encrypted.

## 6. Data Handling Procedures

### 6.1 Data Transfer

- External transfers of Confidential or Restricted data require Data Owner approval.
- Transfers must use encrypted channels (SFTP, TLS-encrypted APIs, PGP-encrypted files).
- Unencrypted email is prohibited for Confidential or Restricted data.

### 6.2 Data Retention

- Data must be retained only as long as required by business need or regulatory obligation.
- Retention periods are defined per data classification in the Data Retention Schedule.
- Expired data must be securely deleted within 30 days of retention period expiration.

### 6.3 Data Disposal

- Digital data: Cryptographic erasure or secure overwrite (NIST 800-88 compliant).
- Physical media: Cross-cut shredding or certified destruction vendor.
- Disposal must be logged with date, method, and responsible party.

## 7. DLP Controls

- DLP rules must be configured for all data egress channels.
- DLP rules must be updated within 30 days of any new egress channel being introduced.
- DLP incidents are triaged by the SOC within 4 hours.

## 8. Exceptions

All exceptions require CISO approval, documented risk assessment, compensating controls, and quarterly review.

---

**Approved by:** Thomas Chen, CISO
**Next Review Date:** March 2026
