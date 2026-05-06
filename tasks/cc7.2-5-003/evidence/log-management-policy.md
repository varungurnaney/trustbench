# Aether Insurance — Log Management and Retention Policy

**Document ID:** ATH-SEC-POL-012
**Version:** 2.8
**Effective Date:** February 1, 2025
**Owner:** Robert Chen, CISO
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy defines requirements for log collection, retention, integrity, and review across all Aether Insurance production systems to support security monitoring, incident investigation, and regulatory compliance.

## 2. Scope

All production systems in AWS (us-east-1, eu-west-1) supporting Aether Insurance's policy management, claims processing, and underwriting platforms.

## 3. Log Retention Requirements

### 3.1 Minimum Retention Periods

| Log Category | Minimum Retention | Rationale |
|-------------|-------------------|-----------|
| Authentication and access logs | 3 years | Regulatory (state insurance regulations) |
| Audit logs (data access, modifications) | 7 years | Regulatory (SOX, state record retention) |
| Application logs | 1 year | Operational and security investigation |
| Infrastructure logs (CloudTrail, VPC Flow) | 3 years | Security investigation and compliance |
| Transaction logs (policy, claims) | 7 years | Regulatory (state insurance regulations) |
| Security event logs (SIEM alerts, IDS) | 3 years | Incident investigation |

### 3.2 Retention Enforcement

- All log retention periods are enforced via automated lifecycle policies
- Logs must not be deleted or modified before their retention period expires
- Retention compliance is verified quarterly via automated audit
- Exceptions to retention periods require CISO and Chief Compliance Officer (CCO) joint approval

### 3.3 Storage Tiers

- Hot (searchable, < 1 second query): 90 days
- Warm (queryable, < 4 hours): 1 year
- Cold (archival, restoration within 24 hours): Remainder of retention period
- All tiers encrypted at rest with AWS KMS customer-managed keys

## 4. Log Integrity

### 4.1 Tamper Protection

- CloudTrail log file validation enabled (digest files)
- SIEM indexes are append-only with no delete capability
- S3 Object Lock (compliance mode) for cold storage archives

### 4.2 Log Forwarding

All logs must be forwarded to the SIEM (Splunk) via encrypted channels (TLS 1.3).

## 5. SIEM Integration

### 5.1 Coverage

All production services must be integrated with Splunk within 5 business days of deployment.

### 5.2 Alert Configuration

Every service must have alerts for: error anomalies, authentication failures, data access anomalies, and availability monitoring.

## 6. Log Review

### 6.1 Daily Review

Security Operations must conduct daily log review of SIEM dashboards, documented with reviewer name and timestamp.

### 6.2 Weekly Privileged Activity Review

Weekly review of privileged account activity, administrative changes, and data access patterns.

## 7. Exception Process

Exceptions require CISO and CCO joint approval, documented compensating controls, and 6-month maximum duration.

---

**Approved by:** Sandra Morales, CCO
