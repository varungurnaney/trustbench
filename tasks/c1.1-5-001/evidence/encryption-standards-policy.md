# Encryption Standards Policy

**Document ID:** POL-ENC-005
**Version:** 4.2
**Effective Date:** February 1, 2025
**Owner:** Security Architecture Team
**Classification:** Internal
**Organization:** Vanguard Risk Solutions

---

## 1. Purpose

This policy defines the minimum encryption standards for Vanguard Risk Solutions to protect confidential information across all environments, ensuring compliance with SOC 2 confidentiality criteria, PCI DSS requirements, and contractual obligations.

## 2. Scope

All encryption implementations across Vanguard Risk Solutions' infrastructure, applications, and communications.

## 3. Encryption Algorithm Requirements

### 3.1 Symmetric Encryption

| Data Classification | Minimum Standard | Preferred Standard |
|---------------------|-----------------|-------------------|
| Restricted (PII, payment data) | AES-256 | AES-256-GCM |
| Confidential (customer data) | AES-256 | AES-256-GCM |
| Internal (business data) | AES-128 | AES-256-GCM |
| Public | None required | N/A |

### 3.2 Asymmetric Encryption

- RSA: Minimum 2048-bit (4096-bit for certificate signing)
- ECDSA: P-256 or P-384
- Key exchange: ECDHE preferred, DHE 2048-bit minimum

### 3.3 Hashing

- SHA-256 minimum for all cryptographic hashing
- SHA-1 and MD5 prohibited for security purposes (MD5 acceptable for non-security checksums)
- PBKDF2, bcrypt, or Argon2 for password hashing

## 4. Data in Transit

### 4.1 External Communications

- TLS 1.2 minimum for all external-facing endpoints
- TLS 1.3 preferred for new deployments
- HSTS required for all web applications
- Cipher suite: ECDHE key exchange, AES-GCM preferred

### 4.2 Internal Communications

- Service-to-service communication handling Restricted or Confidential data must use TLS 1.2 or higher
- Service mesh (Istio) provides automatic mTLS for all pod-to-pod communication in Kubernetes clusters
- Legacy non-containerized services must implement TLS individually

### 4.3 East-West Traffic

- All traffic within the production Kubernetes cluster is encrypted via Istio service mesh mTLS (enforced in STRICT mode)
- Traffic between the Kubernetes cluster and non-containerized legacy services must use TLS 1.2+
- Traffic between services in the internal management VPC handling only Internal-classified data is encrypted via VPC-level IPSec (AWS site-to-site VPN between VPCs)

## 5. Data at Rest

### 5.1 Database Encryption

- RDS instances: Encryption enabled with KMS customer-managed keys
- Field-level encryption: Required for all Restricted data columns using AES-256-GCM

### 5.2 Object Storage

- S3: SSE-KMS with customer-managed keys for Confidential/Restricted data
- S3: SSE-S3 acceptable for Internal-classified data

### 5.3 Volume Encryption

- All EBS volumes must be encrypted
- All EFS file systems must be encrypted

## 6. Key Management

### 6.1 Key Rotation

- KMS CMKs: Annual automatic rotation
- Application encryption keys: Rotated every 12 months
- Rotation must be completed within 14 calendar days of the scheduled rotation date
- Rotation delays beyond 14 days require CISO notification and documented justification

### 6.2 Key Storage

- AWS KMS for infrastructure keys
- HashiCorp Vault for application secrets
- No keys in source code, configuration files, or documentation

## 7. Compliance and Monitoring

- AWS Config rules enforce encryption on new resources
- Quarterly encryption posture review
- Annual penetration test includes encryption validation

## 8. Exceptions

Exceptions require CISO approval, documented compensating controls, and quarterly review.

---

**Approved by:** Laura Mitchell, CISO
**Next Review Date:** February 2026
