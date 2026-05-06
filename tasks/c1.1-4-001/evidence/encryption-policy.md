# Data Protection and Encryption Policy

**Document ID:** POL-ENC-002
**Version:** 3.0
**Effective Date:** January 15, 2025
**Owner:** Information Security Team
**Classification:** Internal
**Organization:** Bridgeport Financial Technologies

---

## 1. Purpose

This policy establishes the requirements for protecting confidential data through encryption controls across all Bridgeport Financial Technologies environments.

## 2. Scope

This policy applies to all systems, databases, and communication channels that process, store, or transmit data classified as Confidential or Restricted. This includes production, staging, and internal environments.

## 3. Data Classification

| Level | Description | Encryption Requirement |
|-------|-------------|----------------------|
| Public | Non-sensitive | None |
| Internal | Business operations data | Encryption in transit required |
| Confidential | Customer data, business IP | Encryption in transit and at rest |
| Restricted | PII, financial data, credentials | Encryption in transit and at rest; field-level encryption |

## 4. Encryption Standards

### 4.1 Data in Transit

- All external-facing endpoints must use TLS 1.2 or higher.
- All internal endpoints handling Confidential or Restricted data must use TLS 1.2 or higher.
- Internal endpoints handling only Internal or Public data within a private VPC may use unencrypted HTTP if approved via the exception process (Section 9).

### 4.2 Data at Rest

- All production databases must have encryption at rest enabled (AWS RDS encryption or equivalent).
- S3 buckets must use SSE-KMS with customer-managed keys for Confidential/Restricted data.
- EBS volumes must be encrypted.

### 4.3 Minimum Algorithm Standards

- Symmetric: AES-256 (AES-128 acceptable only for non-Restricted data with documented justification)
- Asymmetric: RSA-2048 or ECDSA P-256 minimum
- Hashing: SHA-256 or higher (SHA-1 and MD5 prohibited)

### 4.4 Key Rotation

- KMS customer-managed keys must be rotated annually (automatic rotation enabled).
- Application-level encryption keys must be rotated every 12 months.
- Emergency key rotation must be performed within 24 hours of a suspected key compromise.

## 5. Key Management

- AWS KMS is the approved key management service.
- Application secrets stored in AWS Secrets Manager with automatic rotation enabled.
- Hard-coding keys or secrets in source code is prohibited.
- Key access is restricted and logged via CloudTrail.

## 6. Certificate Management

- Production certificates must be from a publicly trusted CA.
- Certificate expiration monitoring must be automated with 30-day advance alerts.
- Internal certificates issued via Bridgeport Private CA with 1-year validity.

## 7. Cloud Storage

- All S3 buckets must have public access blocked at the account level.
- Versioning must be enabled for buckets containing Confidential or Restricted data.
- Lifecycle policies must be configured for data retention compliance.

## 8. Monitoring and Compliance

- Quarterly encryption posture reviews conducted by the Security team.
- AWS Config rules enforce encryption requirements on new resources.
- Non-compliant resources are flagged and must be remediated within 30 days.

## 9. Exceptions

- Exceptions must be requested via the Security Exception Request form.
- CISO approval is required for all exceptions.
- Each exception must include: risk assessment, compensating controls, and expiration date.
- Exceptions are reviewed quarterly and must be renewed or the risk remediated.

---

**Approved by:** Daniel Park, CISO
**Next Review Date:** January 2026
