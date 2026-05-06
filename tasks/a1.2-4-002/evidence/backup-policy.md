# Backup and Recovery Policy

**Document ID:** POL-BKP-006
**Version:** 3.0
**Effective Date:** January 1, 2025
**Owner:** Infrastructure Engineering
**Approved By:** Angela Morrison, CISO

---

## 1. Purpose

This policy defines backup and recovery requirements for Orion Cloud Inc. production infrastructure.

## 2. Scope

All production systems including:
- PostgreSQL database clusters (oc-db-prod-01 through oc-db-prod-06)
- Application file storage (S3: oc-prod-assets, oc-prod-uploads)
- Configuration management (HashiCorp Vault)
- Certificate store (oc-cert-store)

## 3. Backup Requirements

### 3.1 Daily Full Backups

Daily full backups initiated at 02:00 UTC. Must complete within the maintenance window (02:00-06:00 UTC).

### 3.2 Incremental Backups

Incremental file system backups every 4 hours at 06:00, 10:00, 14:00, 18:00, 22:00 UTC.

### 3.3 WAL Archiving

PostgreSQL WAL archiving enabled on all clusters. WAL segments archived continuously with maximum 15-minute lag.

### 3.4 Recovery Objectives

| Objective | Target |
|-----------|--------|
| RPO | 4 hours |
| RTO | 4 hours |

### 3.5 Backup Verification

All backups must have SHA-256 checksum verification completed before being marked as successful. Backups failing checksum verification must be re-run.

## 4. Encryption

AES-256 at rest via AWS KMS. TLS 1.3 in transit. Encryption keys rotated quarterly.

## 5. Retention

| Type | Retention |
|------|-----------|
| Daily full | 30 days |
| Incremental | 7 days |
| WAL | 7 days |
| Monthly | 12 months |
| Annual | 7 years |

## 6. Failure Handling

### 6.1 Response Procedures

1. PagerDuty alert within 5 minutes of failure
2. On-call engineer investigates and initiates re-run within 2 hours
3. If re-run fails, escalate to Infrastructure Lead
4. All failures logged in backup management system

### 6.2 Exception Process

Failures that cannot be resolved require a formal CISO-approved exception documenting root cause, compensating controls, risk assessment, and remediation timeline.

## 7. Restore Testing

Quarterly full restore test in DR environment validating restoration success, data integrity, and RTO compliance.

## 8. Capacity Management

Storage monitored continuously. Alerts at 70% utilization. Semi-annual capacity planning reviews.

---

**Next Review Date:** January 2026
