# Vertex Financial — Data Retention and Archival Policy

**Document ID:** POL-DR-2025-004
**Version:** 2.0
**Effective Date:** March 1, 2025
**Owner:** Catherine Reeves, Chief Information Security Officer
**Classification:** Internal

---

## 1. Purpose

This policy defines the retention periods and archival procedures for Vertex Financial data assets to comply with regulatory requirements and business needs.

## 2. Retention Schedules

| Data Category | Retention Period | Archival Method | Regulatory Basis |
|--------------|-----------------|-----------------|------------------|
| Transaction records | 7 years | Glacier Deep Archive | PCI-DSS, SOX |
| Cardholder data | Duration of relationship + 1 year | Encrypted archival | PCI-DSS |
| Audit logs | 24 months | S3 Intelligent Tiering | SOC 2, PCI-DSS |
| Employee records | Duration of employment + 7 years | Encrypted archival | FLSA, state law |
| Customer communications | 5 years | S3 Standard | FINRA |
| Marketing data | 3 years | S3 Intelligent Tiering | Business need |

## 3. Archival Procedures

### 3.1 Automated Archival

- Monthly automated archival job runs on the 1st of each month
- Data exceeding retention period moved to Glacier Deep Archive
- Archival confirmation report generated and reviewed by Data Governance team

### 3.2 Deletion

- Data past retention period is permanently deleted from archive
- Deletion requires dual approval (Data Owner + CISO)
- Deletion certificate generated for compliance records

## 4. Legal Hold

Data subject to legal hold is exempt from routine deletion. Legal holds are managed by the Legal department and communicated to IT within 24 hours of hold initiation.

## 5. Compliance

Monthly compliance report generated showing retention adherence across all data categories. Deviations escalated to CISO.

---

**Approved by:** Catherine Reeves, CISO
