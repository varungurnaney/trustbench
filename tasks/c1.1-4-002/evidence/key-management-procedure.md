# Encryption Key Management Procedure

**Document ID:** SOP-KM-001
**Version:** 2.5
**Effective Date:** April 1, 2025
**Owner:** Security Engineering Team
**Classification:** Confidential
**Organization:** Halcyon Cloud Services

---

## 1. Purpose

This procedure defines the operational processes for managing encryption keys throughout their lifecycle at Halcyon Cloud Services, including generation, distribution, rotation, revocation, and destruction.

## 2. Scope

This procedure covers all encryption keys used across Halcyon Cloud Services' environments:

- AWS KMS Customer Managed Keys (CMKs)
- Application-level encryption keys (stored in AWS Secrets Manager)
- TLS certificate private keys
- SSH keys for infrastructure access
- PGP keys for partner data exchange

## 3. Key Generation

### 3.1 Standards

- All symmetric keys must be AES-256 unless an approved exception exists for AES-128.
- Key generation must use FIPS 140-2 Level 2 validated HSMs (AWS CloudHSM or KMS).
- Custom key generation code is prohibited — only approved KMS/HSM APIs are permitted.

### 3.2 Key Naming Convention

Format: `hcs-{environment}-{service}-{purpose}-{year}`
Example: `hcs-prod-payments-encryption-2025`

## 4. Key Rotation

### 4.1 Rotation Schedule

| Key Type | Rotation Frequency | Method | Owner |
|----------|-------------------|--------|-------|
| AWS KMS CMKs | Annual (automatic) | AWS KMS automatic rotation | Security Engineering |
| Application encryption keys | Every 12 months | Manual rotation via Secrets Manager | Application Owner + Security Engineering |
| TLS certificate keys | On certificate renewal | Automated via cert-manager | DevOps |
| SSH keys | Every 6 months | Automated via Teleport | Infrastructure Team |
| PGP keys for partners | Every 24 months | Manual exchange with partner | Integrations Team |

### 4.2 Rotation Process — Application Keys

1. Security Engineering generates new key version in Secrets Manager.
2. Application Owner deploys application with dual-key read support (old + new).
3. Re-encryption batch job runs to re-encrypt data with new key.
4. Application Owner confirms re-encryption complete.
5. Old key version disabled after 30-day coexistence period.
6. Old key version deleted after 90-day retention period.

### 4.3 Emergency Key Rotation

In the event of suspected key compromise:

1. Security team initiates emergency rotation within 24 hours.
2. Compromised key is immediately disabled (not deleted, for forensic purposes).
3. New key generated and deployed.
4. Re-encryption of all affected data within 72 hours.
5. Incident report filed per IRP.

### 4.4 Rotation Tracking

Key rotations are tracked in the Key Rotation Log (maintained in the Security Engineering Confluence space). Each rotation entry must include:

- Key identifier
- Previous rotation date
- Current rotation date
- Performed by
- Verification method
- Sign-off by Security Engineering lead

## 5. Key Storage and Access

### 5.1 Storage Requirements

- KMS keys are stored within the AWS KMS service (never exported).
- Application keys are stored in AWS Secrets Manager with encryption enabled.
- Keys must never be stored in: source code, configuration files, email, chat messages, or documentation.

### 5.2 Access Control

- KMS key policies follow least-privilege model.
- Application key access restricted to service roles via IAM policies.
- Human access to keys requires Security Engineering approval and is logged.
- Break-glass access procedure requires two-person authorization (Security Engineering + CISO).

## 6. Key Revocation and Destruction

### 6.1 Revocation

Keys are revoked when:
- The key has reached end of life
- The key is suspected compromised
- The associated system is decommissioned

### 6.2 Destruction

- KMS keys are scheduled for deletion with 30-day waiting period.
- Application keys in Secrets Manager are deleted after confirming no active references.
- Destruction is logged and auditable.

## 7. Compliance Monitoring

- AWS Config rule `kms-cmk-rotation-enabled` enforces automatic rotation on all CMKs.
- Monthly review of key inventory and rotation status by Security Engineering.
- Quarterly key management audit by the CISO.

---

**Approved by:** Jennifer Torres, CISO
**Next Review Date:** April 2026
