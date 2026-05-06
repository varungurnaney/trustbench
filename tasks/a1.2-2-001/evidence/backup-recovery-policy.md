# Backup and Recovery Policy

**Document ID:** POL-BKP-003
**Version:** 2.5
**Effective Date:** February 1, 2025
**Owner:** Infrastructure Engineering
**Approved By:** Sandra Nguyen, CISO

---

## 1. Purpose

This policy defines backup and recovery requirements for Pinnacle SaaS Inc. to ensure data availability and business continuity in accordance with SOC 2 A1.2.

## 2. Scope

All production systems including:
- PostgreSQL database clusters (pin-db-prod-01 through pin-db-prod-04)
- Application file storage (S3: pin-prod-assets, pin-prod-uploads)
- Configuration management and secrets (HashiCorp Vault)

## 3. Recovery Objectives

| Objective | Target | Measurement |
|-----------|--------|-------------|
| Recovery Point Objective (RPO) | 4 hours | Maximum data loss in a failure scenario |
| Recovery Time Objective (RTO) | 4 hours | Maximum time to restore service |

## 4. Backup Schedule

### 4.1 Daily Full Backups

Production databases receive daily full backups at 02:00 UTC. Backups must complete within the maintenance window (02:00-06:00 UTC).

### 4.2 Continuous WAL Archiving

PostgreSQL WAL segments archived continuously to cross-region storage with maximum 15-minute lag.

### 4.3 Incremental Backups

Incremental file system backups every 4 hours at 06:00, 10:00, 14:00, 18:00, 22:00 UTC.

## 5. Backup Encryption

AES-256 encryption at rest via AWS KMS. TLS 1.3 in transit.

## 6. Restore Testing

### 6.1 Quarterly Restore Tests

Full restore test performed quarterly in the DR environment. Tests must validate:
- Successful restoration of most recent backup
- Data integrity via checksum comparison
- Restoration within defined RTO
- Application functionality post-restore

### 6.2 Documentation

Each test produces a report with timing details, integrity results, and sign-off.

## 7. Failure Handling

On-call engineer alerted within 5 minutes via PagerDuty. Re-run initiated within 2 hours. Escalation to Infrastructure Lead if re-run fails.

---

**Next Review Date:** February 2026
