# Backup and Recovery Policy

**Document ID:** POL-BKP-007
**Version:** 2.6
**Effective Date:** March 1, 2025
**Owner:** Infrastructure Engineering
**Approved By:** David Chen, CISO

---

## 1. Purpose

This policy defines backup and recovery requirements for Apex Digital Inc. to ensure data availability and business continuity.

## 2. Scope

All production systems including:
- PostgreSQL database clusters (apex-db-prod-01 through apex-db-prod-04)
- Application file storage (S3: apex-prod-assets, apex-prod-uploads)
- Configuration and secrets (HashiCorp Vault)

## 3. Recovery Objectives

| Objective | Target |
|-----------|--------|
| RPO | 4 hours |
| RTO | 4 hours (240 minutes) |

## 4. Backup Schedule

### 4.1 Daily Full Backups

Daily full backups at 02:00 UTC within maintenance window (02:00-06:00 UTC).

### 4.2 WAL Archiving

Continuous WAL archiving with maximum 15-minute lag.

### 4.3 Incremental Backups

Incremental file system backups every 4 hours.

## 5. Restore Testing

### 5.1 Quarterly Restore Tests

Full restore test performed quarterly in DR environment. Each test must validate:
1. Successful restoration of the most recent full backup
2. Data integrity verification via SHA-256 checksum comparison
3. Restoration completes within the defined RTO (4 hours)
4. Application functionality validation post-restore (API health checks, background job processing, user authentication flow)

### 5.2 Documentation

Each test produces a report documenting timing details, integrity results, issues encountered, and sign-off by Infrastructure Lead.

## 6. Failure Handling

PagerDuty alert within 5 minutes. On-call re-run within 2 hours. Escalation if re-run fails.

## 7. Retention

| Type | Retention |
|------|-----------|
| Daily | 30 days |
| Monthly | 12 months |
| Annual | 7 years |

---

**Next Review Date:** March 2026
