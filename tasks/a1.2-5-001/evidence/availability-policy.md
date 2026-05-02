# System Availability and Recovery Policy

**Document ID:** POL-AV-002
**Version:** 2.1
**Effective Date:** April 1, 2025
**Owner:** SRE Team

---

## 1. Purpose

This policy defines the availability, backup, and recovery requirements for NexGen Platform's production systems.

## 2. Availability Targets

| System | SLA | Measurement |
|--------|-----|-------------|
| Core API | 99.95% uptime | Monthly, excluding scheduled maintenance |
| Web Application | 99.9% uptime | Monthly |
| Database (PostgreSQL) | 99.99% uptime | Monthly |
| Background Workers | 99.5% uptime | Monthly |

## 3. Backup Requirements

### 3.1 Database Backups

- **Full backup:** Daily at 02:00 UTC
- **Incremental backup:** Every 4 hours
- **WAL archiving:** Continuous (point-in-time recovery capability)
- **Retention:** 30 days for daily, 7 days for incremental, 7 days for WAL archives
- **Storage:** Encrypted at rest (AES-256) in a separate GCS bucket in a different region

### 3.2 Application and Configuration Backups

- All application configuration stored in Git (version controlled).
- Infrastructure-as-code (Terraform) stored in Git.
- Secrets stored in Google Secret Manager (versioned, auto-backed up by GCP).

### 3.3 Backup Verification

- Automated backup integrity checks run daily — verify backup file completeness and checksums.
- Full restore test performed quarterly to a staging environment.
- Restore test results documented and retained for audit.

## 4. Disaster Recovery

- **RTO:** 4 hours for core API, 8 hours for all other systems.
- **RPO:** 4 hours (aligned with incremental backup frequency).
- DR site: GCP us-east1 (primary: us-central1).
- DR failover tested semi-annually.

## 5. Incident Response for Availability Events

- P1 availability incidents escalated per the Incident Response Plan.
- Automated monitoring alerts via Datadog for latency, error rate, and uptime.
- Status page (status.nexgenplatform.com) updated within 15 minutes of confirmed outage.

---

**Approved by:** Lisa Fernandez, VP Engineering
**Next Review Date:** April 2026
