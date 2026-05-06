# Data Protection and Encryption Policy

**Document ID:** POL-ENC-001
**Version:** 2.1
**Effective Date:** March 1, 2025
**Owner:** Information Security Team
**Classification:** Internal
**Organization:** Crestline Data Systems

---

## 1. Purpose

This policy establishes the requirements for encrypting and protecting confidential data processed, transmitted, and stored by Crestline Data Systems in alignment with regulatory and contractual obligations.

## 2. Scope

This policy applies to all employees, contractors, and third-party vendors who handle data classified as Confidential or Restricted within Crestline Data Systems' environments, including cloud infrastructure (AWS), on-premises data centers, and endpoint devices.

## 3. Data Classification

### 3.1 Classification Levels

| Level | Description | Examples |
|-------|-------------|----------|
| Public | Non-sensitive, freely distributable | Marketing materials, public docs |
| Internal | Business information, low risk if disclosed | Internal memos, org charts |
| Confidential | Business-critical data requiring protection | Customer data, financial records |
| Restricted | Highest sensitivity, regulatory implications | PII, PHI, payment card data |

### 3.2 Classification Responsibility

Data owners are responsible for classifying data at the point of creation. The Data Governance team reviews classifications annually.

## 4. Encryption Standards

### 4.1 Data in Transit

All data classified as Confidential or Restricted must be encrypted in transit using:

- TLS 1.2 or higher for all HTTPS communications
- IPSec or WireGuard for VPN tunnels
- SFTP or SCP for file transfers (FTP is prohibited)

Internal service-to-service communications within the production VPC should use mutual TLS (mTLS) where feasible.

### 4.2 Endpoint Encryption

- All company-issued laptops must have full-disk encryption enabled (BitLocker for Windows, FileVault for macOS).
- Mobile devices accessing corporate email must have device-level encryption.
- USB storage devices are prohibited for Confidential or Restricted data.

### 4.3 Email Encryption

- Emails containing Confidential or Restricted data must use S/MIME or Microsoft 365 Message Encryption.
- DLP rules in Microsoft 365 scan outbound emails for sensitive data patterns.

## 5. Key Management

### 5.1 Key Generation

- Encryption keys must be generated using FIPS 140-2 validated cryptographic modules.
- AWS KMS is the approved key management service for cloud workloads.

### 5.2 Key Storage

- Keys must never be stored alongside the data they protect.
- Application-level keys must be stored in AWS Secrets Manager or HashiCorp Vault.
- Hard-coding encryption keys in source code is strictly prohibited.

### 5.3 Key Access

- Access to encryption keys is restricted to authorized personnel on a need-to-know basis.
- Key access is logged and auditable via AWS CloudTrail.

## 6. Certificate Management

### 6.1 TLS Certificates

- Production TLS certificates must be issued by a publicly trusted Certificate Authority.
- Certificate validity must not exceed 398 days per CA/Browser Forum requirements.
- Certificates must use a minimum key size of RSA 2048-bit or ECDSA P-256.

### 6.2 Internal Certificates

- Internal certificates are issued via the Crestline Private CA managed in AWS Private CA.
- Internal certificate validity is limited to 1 year.

## 7. Prohibited Practices

- Use of deprecated algorithms: MD5, SHA-1, DES, 3DES, RC4
- Transmission of Confidential or Restricted data over unencrypted channels
- Storage of encryption keys in plaintext configuration files
- Use of self-signed certificates in production environments

## 8. Compliance and Monitoring

- The Security Operations team monitors for encryption compliance using automated scanning tools.
- Quarterly reviews of encryption posture are conducted by the CISO.
- Non-compliance is reported as a security incident and tracked to remediation.

## 9. Exceptions

Exceptions to this policy must be approved by the CISO in writing, documented in the Exception Register with compensating controls, and reviewed quarterly.

---

**Approved by:** Rachel Nguyen, CISO
**Next Review Date:** March 2026
