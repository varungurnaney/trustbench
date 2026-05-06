# Data Protection Policy

**Document ID:** POL-DP-006
**Version:** 3.4
**Effective Date:** January 1, 2025
**Owner:** Security Architecture Team
**Classification:** Internal
**Organization:** Nextera Health Analytics

---

## 1. Purpose

This policy establishes requirements for protecting the confidentiality of data processed by Nextera Health Analytics, a healthcare analytics company processing Protected Health Information (PHI) and Personally Identifiable Information (PII) on behalf of healthcare provider clients.

## 2. Scope

All data systems, networks, and communication channels within Nextera Health Analytics that process, store, or transmit PHI, PII, or other confidential business data.

## 3. Regulatory Context

Nextera Health Analytics is subject to:
- HIPAA Security Rule (45 CFR Part 164)
- SOC 2 Type II (Confidentiality and Security criteria)
- State health data privacy laws (varies by client jurisdiction)
- BAA (Business Associate Agreement) obligations with all healthcare provider clients

## 4. Data Classification

| Level | Description | Examples | Encryption Requirement |
|-------|-------------|----------|----------------------|
| Public | Non-sensitive | Marketing, public research | None |
| Internal | Business operations | Internal reports, HR data | Transit encryption |
| Confidential | Business-sensitive | Financial, contracts | Transit + at-rest |
| Restricted | PHI, PII, credentials | Patient data, provider data | Transit + at-rest + field-level |

## 5. Encryption Requirements

### 5.1 Data in Transit — External

All external network communications must use TLS 1.2 or higher. No exceptions.

### 5.2 Data in Transit — Internal

- All internal communications carrying Restricted data (PHI/PII) must be encrypted using TLS 1.2 or higher.
- The Kubernetes production cluster uses Istio service mesh with mTLS in STRICT mode for all in-cluster traffic.
- Internal communications carrying only Internal-classified data are recommended but not required to use encryption.
- Confidential data internal communications should use TLS where technically feasible.

### 5.3 Data at Rest

- All databases must have encryption at rest enabled (RDS encryption, or equivalent).
- Field-level encryption using AES-256 is required for all PHI and PII data elements.
- S3 buckets must use SSE-KMS with customer-managed keys for Restricted and Confidential data.

### 5.4 HIPAA Addressable Specification

Per HIPAA Security Rule § 164.312(e)(1), encryption of data in transit is an "addressable" specification. Nextera's risk assessment has determined that encryption is "reasonable and appropriate" for all PHI transmissions. Therefore, encryption is required for all PHI in transit — this addressable specification is implemented, not documented-and-declined.

## 6. Key Management

- AWS KMS with customer-managed keys for all infrastructure encryption
- Application keys managed in HashiCorp Vault
- Annual key rotation for KMS CMKs (automatic)
- 12-month rotation for application keys
- Key rotation must be completed within 7 calendar days of scheduled date (no grace period for PHI-related keys)

## 7. Certificate Management

- External certificates from DigiCert or AWS ACM
- Internal certificates via Nextera Private CA (AWS Private CA)
- 30-day advance expiration alerts mandatory
- Auto-renewal required for all production certificates

## 8. Monitoring

- Quarterly encryption posture assessments
- AWS Config rules enforce encryption on resource creation
- Non-compliant resources must be remediated within 14 days or have a CISO-approved exception

## 9. Exceptions

- CISO approval required
- HIPAA risk assessment required for any exception involving PHI data
- Maximum exception duration: 6 months for PHI-related exceptions
- Quarterly review of all active exceptions

---

**Approved by:** Dr. Michael Reeves, CISO
**Next Review Date:** January 2026
