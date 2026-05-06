# Backup and Recovery Policy

**Document ID:** POL-BKP-005
**Version:** 2.8
**Effective Date:** January 15, 2025
**Owner:** Infrastructure Engineering
**Approved By:** Patricia Morales, CISO

---

## 1. Purpose

This policy defines the backup and recovery requirements for Nexus Platforms Inc. production infrastructure to ensure data availability and business continuity.

## 2. Scope

All production systems including:
- PostgreSQL database clusters (nx-db-prod-01 through nx-db-prod-04)
- Application file storage (S3: nx-prod-assets, nx-prod-uploads, nx-prod-configs)
- Configuration management (HashiCorp Vault cluster)

## 3. Backup Schedule

### 3.1 Daily Full Backups

All production databases and file systems receive daily full backups initiated at 02:00 UTC. Full backups must complete within the maintenance window (02:00-06:00 UTC).

### 3.2 Incremental Backups

Incremental file system backups run every 4 hours at 06:00, 10:00, 14:00, 18:00, and 22:00 UTC. Incremental backups capture all changes since the last full or incremental backup.

### 3.3 WAL Archiving

PostgreSQL Write-Ahead Log (WAL) archiving is enabled on all database clusters. WAL segments are archived continuously to cross-region storage (us-west-2) with a maximum archive lag of 15 minutes. WAL archiving provides point-in-time recovery capability.

## 4. Recovery Objectives

| Objective | Target | Measurement |
|-----------|--------|-------------|
| Recovery Point Objective (RPO) | 4 hours | Maximum data loss in a failure scenario |
| Recovery Time Objective (RTO) | 4 hours | Maximum time to restore service |

## 5. Backup Encryption

AES-256 encryption at rest via AWS KMS. TLS 1.3 for all backup data in transit. Encryption keys rotated quarterly.

## 6. Backup Retention

| Backup Type | Retention |
|-------------|-----------|
| Daily full | 30 days |
| Incremental | 7 days |
| WAL archives | 7 days |
| Monthly consolidated | 12 months |

## 7. Restore Testing

Full restore test performed quarterly in the DR environment. Tests validate restoration success, data integrity, and RTO compliance.

## 8. Failure Handling

Backup failures trigger PagerDuty alert within 5 minutes. On-call engineer investigates and initiates re-run within 2 hours.

## 9. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| VP Infrastructure | Policy owner |
| Infrastructure Lead | Restore test execution |
| On-Call Engineer | Backup failure response |
| CISO | Policy approval |

---

**Next Review Date:** January 2026
