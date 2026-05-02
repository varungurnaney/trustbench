# Aurora Labs — Encryption Standards Policy

**Document ID:** POL-ENC-2024-001
**Version:** 2.1
**Effective Date:** March 1, 2024
**Last Review:** September 15, 2025
**Owner:** Derek Huang, VP of Engineering
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy defines the encryption standards and requirements for protecting Aurora Labs data at rest and in transit across all systems and environments.

## 2. Encryption at Rest

### 2.1 Database Encryption

All production databases must employ encryption at rest using AES-256 or equivalent:

- **MongoDB Atlas**: Encrypted Storage Engine with customer-managed keys (AWS KMS)
- **Snowflake**: Tri-Secret Secure (Snowflake-managed + customer-managed keys)
- **Redis**: At-rest encryption enabled via AWS ElastiCache encryption

### 2.2 File Storage

- All S3 buckets must use SSE-S3 (AES-256) or SSE-KMS encryption
- Server-side encryption must be enforced via bucket policies that deny unencrypted uploads
- EBS volumes attached to EC2 instances must be encrypted using AWS KMS

### 2.3 Key Management

- Encryption keys are managed through AWS Key Management Service (KMS)
- Key rotation is automated on a 365-day cycle
- Key access is restricted to the Security Engineering team
- Key usage is logged via AWS CloudTrail

## 3. Encryption in Transit

### 3.1 External Communications

- All external-facing endpoints must use TLS 1.2 or higher
- TLS 1.3 is preferred for all new deployments
- SSL certificates are managed through AWS Certificate Manager (ACM)
- Certificate expiration monitoring is automated with 30-day advance alerts

### 3.2 Internal Communications

- Inter-service communication within VPCs must use TLS 1.2 or higher
- mTLS is required for service-to-service authentication in the production environment
- Internal certificate authority is operated via AWS Private CA

### 3.3 Prohibited Protocols

The following are explicitly prohibited:
- SSL 2.0, SSL 3.0
- TLS 1.0, TLS 1.1
- Unencrypted HTTP for any data transmission containing sensitive information

## 4. Cryptographic Standards

### 4.1 Approved Algorithms

| Use Case | Algorithm | Minimum Key Length |
|----------|-----------|-------------------|
| Symmetric encryption | AES | 256 bits |
| Asymmetric encryption | RSA | 2048 bits |
| Key exchange | ECDHE | P-256 or higher |
| Hashing | SHA-2 | SHA-256 or higher |
| Password hashing | bcrypt | Cost factor 12 |

### 4.2 Deprecated Algorithms

The following algorithms must not be used for new implementations and must be migrated away from within 12 months of this policy's effective date:

- MD5 (any use)
- SHA-1 (any use)
- DES / 3DES
- RC4
- RSA keys shorter than 2048 bits

## 5. Compliance and Monitoring

- Monthly automated scans verify encryption configurations across all environments
- Non-compliant resources are flagged in the security dashboard and must be remediated within 30 days
- Encryption compliance is reported to the CISO as part of the monthly security metrics

## 6. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 2.1 | 2025-09-15 | D. Huang | Added mTLS requirements for production services |
| 2.0 | 2024-03-01 | D. Huang | Major revision — consolidated encryption standards |
| 1.0 | 2023-06-15 | M. Torres | Initial release |
