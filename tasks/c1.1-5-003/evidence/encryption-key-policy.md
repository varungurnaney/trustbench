# Encryption Key Lifecycle Policy

**Document ID:** POL-KEY-007
**Version:** 2.8
**Effective Date:** March 1, 2025
**Owner:** Security Engineering
**Classification:** Internal
**Organization:** Arbor Data Platforms

---

## 1. Purpose

This policy defines the requirements for managing encryption keys throughout their lifecycle at Arbor Data Platforms, ensuring confidential data remains protected through proper key management practices.

## 2. Scope

All cryptographic keys used to protect data classified as Confidential or Restricted across Arbor Data Platforms' infrastructure and applications.

## 3. Key Types and Standards

| Key Type | Algorithm | Minimum Strength | Use Case |
|----------|-----------|-----------------|----------|
| Database field encryption | AES-256-GCM | 256-bit | PII column encryption |
| Storage encryption | AES-256 | 256-bit | S3, EBS, RDS encryption |
| Transport encryption | ECDHE + AES | 128-bit minimum | TLS session keys |
| API payload encryption | AES-256-GCM | 256-bit | Inter-service encrypted payloads |
| Backup encryption | AES-256 | 256-bit | Backup file encryption |

## 4. Key Rotation Requirements

### 4.1 Rotation Schedule

| Key Category | Maximum Rotation Period | Method | Tolerance |
|-------------|----------------------|--------|-----------|
| AWS KMS CMKs | 365 days | Automatic (AWS-managed) | 0 days (automatic) |
| Application encryption keys | 365 days | Manual via Secrets Manager | 7 calendar days |
| Database field-encryption keys | 365 days | Manual with re-encryption | 14 calendar days |
| PGP/GPG partner exchange keys | 730 days | Manual with partner coordination | 30 calendar days |
| SSH infrastructure keys | 180 days | Automated via Teleport | 0 days (automatic) |

### 4.2 Rotation Tolerance

The "tolerance" column defines the maximum allowable delay beyond the scheduled rotation date:

- Rotations completed within the tolerance window are considered **on-time**.
- Rotations completed beyond the tolerance window are considered **late** and require:
  - Root cause documentation
  - CISO notification within 24 hours of exceeding tolerance
  - Corrective action plan
  - Post-incident review if the key protects Restricted data

### 4.3 Rotation Procedure for Database Field-Encryption Keys

1. Generate new key version in Secrets Manager
2. Deploy application update supporting dual-key decryption (old + new key)
3. Execute re-encryption batch job to re-encrypt all records with new key
4. Verify re-encryption completeness (row count validation)
5. Remove old key from application configuration after 30-day coexistence
6. Schedule old key deletion after 90-day retention

### 4.4 Emergency Rotation

If a key compromise is suspected:
- Immediate CISO notification
- Emergency rotation initiated within 4 hours
- Compromised key disabled (not deleted)
- Full re-encryption within 48 hours
- Incident report within 5 business days

## 5. Key Destruction

- KMS keys: 30-day pending deletion
- Application keys: Soft-delete with 90-day recovery window
- Physical media: NIST 800-88 compliant destruction

## 6. Monitoring and Compliance

### 6.1 Key Rotation Dashboard

- Automated dashboard tracks all key rotation schedules and compliance
- Dashboard reviewed weekly by Security Engineering Lead
- Overdue rotations generate automated Slack alerts to #security-ops channel

### 6.2 Quarterly Key Management Audit

- CISO reviews all key rotation compliance quarterly
- Any keys with outstanding rotation delays are escalated
- Audit report retained for 3 years

## 7. Exceptions

- CISO approval with documented risk assessment
- Maximum 6-month exception duration
- Quarterly review of all active exceptions
- No exceptions for emergency rotation requirements

---

**Approved by:** Patricia Hawkins, CISO
**Next Review Date:** March 2026
