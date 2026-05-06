# Data Retention Policy

**Document ID:** POL-DR-001
**Version:** 2.0
**Effective Date:** April 1, 2025
**Owner:** Legal & Compliance
**Approved By:** Sarah Blackwell, General Counsel

---

## 1. Purpose

This policy defines data retention requirements for Keystone Data Inc. to ensure compliance with legal, regulatory, and contractual obligations.

## 2. Retention Schedule

| Data Category | Retention Period | Basis |
|---------------|-----------------|-------|
| Customer transaction records | 7 years | SOX, state regulations |
| Financial reporting data | 7 years | SOX, SEC requirements |
| Customer PII | Duration of service + 2 years | Privacy policy, CCPA |
| Employee records | Duration of employment + 5 years | Labor regulations |
| Audit logs | 3 years | SOC 2, internal policy |
| Marketing data | 2 years after last interaction | Privacy policy |
| Internal communications | 3 years | Corporate governance |

## 3. Legal Holds

When a legal hold is issued, it supersedes standard retention periods. Data subject to a legal hold must not be deleted, modified, or destroyed until the hold is released by the General Counsel.

## 4. Data Destruction

Upon expiration of the retention period (and absence of legal hold), data must be securely destroyed using approved methods:
- Electronic data: cryptographic erasure or secure deletion
- Physical media: NIST 800-88 compliant destruction

## 5. Application-Level Retention

Application databases implement retention through automated archival processes:
- Active data retained in primary database
- Data exceeding active retention moved to archive tables
- Archive data retained per schedule above
- Expired archive data purged by scheduled jobs

## 6. Backup Retention

Backup retention is governed by the Backup and Recovery Policy (POL-BKP-008).

---

**Next Review Date:** April 2026
