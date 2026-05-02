# Cobalt Systems -- Backup and Recovery Policy

**Document ID:** CS-POL-BKP-004  
**Version:** 3.2  
**Effective Date:** 2025-01-15  
**Last Reviewed:** 2025-07-10  
**Owner:** Marcus Chen, VP of Infrastructure  
**Approved By:** Diana Reeves, CISO  

---

## 1. Purpose

This policy defines the backup and recovery requirements for all Cobalt Systems production infrastructure, ensuring data availability and business continuity in accordance with SOC 2 Trust Services Criteria A1.2.

## 2. Scope

This policy applies to all production systems, databases, and application data hosted in Cobalt Systems' primary data center (us-east-1) and disaster recovery site (us-west-2), including:

- PostgreSQL database clusters (cs-db-prod-01 through cs-db-prod-06)
- Application file storage (S3 buckets: cs-prod-assets, cs-prod-uploads, cs-prod-configs)
- Configuration management repositories
- Certificate and secrets stores (HashiCorp Vault cluster)

## 3. Backup Requirements

### 3.1 Full Backups

All production databases and file systems shall receive **daily full backups** initiated at 02:00 UTC. Full backups must complete within the designated maintenance window (02:00 -- 06:00 UTC).

### 3.2 Incremental Backups and Write-Ahead Logging

To achieve the Recovery Point Objective (RPO), PostgreSQL Write-Ahead Log (WAL) archiving shall be enabled on all database clusters. WAL segments are archived continuously to cross-region storage (us-west-2) with a maximum archive lag of 15 minutes.

Incremental file system backups run every 4 hours at 06:00, 10:00, 14:00, 18:00, and 22:00 UTC.

### 3.3 Recovery Objectives

| Objective | Target | Measurement |
|-----------|--------|-------------|
| Recovery Point Objective (RPO) | 4 hours | Maximum data loss in a failure scenario |
| Recovery Time Objective (RTO) | 4 hours | Maximum time to restore service |

### 3.4 Backup Encryption

All backups are encrypted at rest using AES-256 encryption. Encryption keys are managed through HashiCorp Vault and rotated quarterly. Backups in transit use TLS 1.3.

### 3.5 Cross-Region Storage

Backup data is replicated to the disaster recovery region (us-west-2) within 1 hour of backup completion. Cross-region replication status is monitored by CloudWatch alarms with SNS notification to the on-call infrastructure team.

## 4. Backup Retention

| Backup Type | Retention Period |
|-------------|-----------------|
| Daily full backups | 30 days |
| WAL archives | 7 days |
| Incremental backups | 7 days |
| Monthly consolidated backups | 12 months |
| Annual backups | 7 years |

## 5. Restore Testing

### 5.1 Quarterly Restore Tests

A full restore test shall be performed **quarterly** in the disaster recovery environment. The test must validate:

- Successful restoration of the most recent full backup
- Data integrity verification via checksum comparison
- Restoration completes within the defined RTO (4 hours)
- Application functionality validation post-restore

### 5.2 Restore Test Documentation

Each restore test must produce a report documenting:
- Date and time of test
- Backup set used for restoration
- Time to complete restoration
- Data integrity check results
- Any issues encountered and their resolution
- Sign-off by the Infrastructure Lead

## 6. Failure Handling

### 6.1 Backup Failure Response

In the event of a backup failure:
1. The automated monitoring system (PagerDuty integration) shall alert the on-call engineer within 5 minutes
2. The on-call engineer shall investigate and initiate a re-run within 2 hours
3. If the re-run fails, escalation to the Infrastructure Lead is required
4. All backup failures and resolutions must be logged in the backup management system

### 6.2 Exception Process

Backup failures that cannot be resolved within the standard process require a formal exception approved by the CISO. The exception must document:
- Root cause of the failure
- Compensating controls in place
- Risk assessment
- Planned remediation timeline

## 7. Capacity Management

Backup storage capacity shall be monitored continuously. Alerts shall trigger when storage utilization exceeds 70% capacity. Capacity planning reviews should be conducted semi-annually to project future storage needs based on data growth trends.

## 8. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| VP of Infrastructure | Policy owner, capacity planning oversight |
| Infrastructure Lead | Restore test execution, backup system maintenance |
| On-Call Engineer | Backup failure response, re-run execution |
| CISO | Exception approval, policy review |

## 9. Policy Review

This policy is reviewed annually or upon significant infrastructure changes, whichever comes first.

---

*Document Classification: Internal Use Only*
