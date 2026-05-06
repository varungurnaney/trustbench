# Backup and Data Protection Policy

**Document ID:** POL-BKP-001
**Version:** 1.2
**Effective Date:** June 1, 2025
**Owner:** IT Operations
**Classification:** Internal

---

## 1. Purpose

This policy defines the requirements for backing up production data at Cirrus Labs Inc. to protect against data loss.

## 2. Scope

This policy applies to all production databases, application servers, and file storage systems hosted in the Cirrus Labs AWS environment (us-east-1).

## 3. Backup Schedule

### 3.1 Daily Full Backups

All production databases shall receive daily full backups initiated at 02:00 UTC. Backups are performed using AWS Backup.

### 3.2 File System Backups

Application file storage (S3 buckets) shall be backed up daily via cross-region replication to us-west-2.

## 4. Backup Encryption

All backups are encrypted at rest using AES-256 encryption managed through AWS KMS. Backups in transit use TLS 1.2 or higher.

## 5. Backup Retention

| Backup Type | Retention Period |
|-------------|-----------------|
| Daily backups | 30 days |
| Monthly backups | 12 months |

## 6. Backup Storage

Backups are stored in a separate AWS account dedicated to backup storage. Cross-account access is restricted to the backup service role.

## 7. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| IT Operations Lead | Backup schedule management |
| Cloud Engineer | Backup infrastructure maintenance |
| CISO | Policy approval |

## 8. Policy Review

This policy is reviewed annually.

---

**Approved by:** Thomas Grant, CISO
**Next Review Date:** June 2026
