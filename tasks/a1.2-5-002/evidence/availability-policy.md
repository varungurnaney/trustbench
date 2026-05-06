# Availability and Disaster Recovery Policy

**Document ID:** POL-AVAIL-002
**Version:** 3.1
**Effective Date:** January 1, 2025
**Owner:** Infrastructure Engineering
**Approved By:** Lisa Nakamura, CISO

---

## 1. Purpose

This policy defines availability, backup, and disaster recovery requirements for Zenith Cloud Inc. to meet SOC 2 A1.2 Trust Services Criteria.

## 2. Scope

All production Tier 1 services:
- Customer-facing API (api.zenithcloud.io)
- Web application (app.zenithcloud.io)
- Authentication service (auth.zenithcloud.io)
- Payment processing service
- Background job processing (data pipeline, notifications, billing)

## 3. Recovery Objectives and DR Design

### 3.1 Recovery Targets

| Objective | Target |
|-----------|--------|
| RPO | 1 hour |
| RTO | 4 hours (240 minutes) |
| Availability SLA | 99.95% monthly |

### 3.2 Service Restoration Definition

Service restoration is defined as: all Tier 1 services fully operational in the DR environment, accepting production traffic, with data consistency verified and no degraded functionality.

### 3.3 DR Environment

The DR environment (us-west-2) maintains warm standby infrastructure capable of assuming full production load within the RTO window. Components include:
- RDS Multi-AZ with cross-region read replicas (continuous replication)
- Kubernetes cluster in warm standby configuration
- S3 cross-region replication
- ElastiCache warm standby

### 3.4 DNS Failover

DNS failover is managed via Route 53 health checks with expected propagation within 15 minutes. Health checks evaluate all Tier 1 service endpoints at 30-second intervals.

## 4. Backup Requirements

### 4.1 Daily Full Backups

Daily full backups at 02:00 UTC.

### 4.2 WAL Archiving

Continuous PostgreSQL WAL archiving with maximum 15-minute lag.

### 4.3 Incremental Backups

Incremental backups every 4 hours.

## 5. DR Testing

### 5.1 Quarterly DR Failover Tests

A full DR failover test shall be conducted quarterly. Tests must:
1. Initiate failover from primary to DR region
2. Validate database promotion and data consistency
3. Confirm all Tier 1 services operational in DR
4. Verify service restoration within RTO
5. Document issues and remediation actions

### 5.2 Test Documentation

Each test produces a report with detailed timeline, issues encountered, and sign-off.

## 6. Backup Retention

| Type | Retention |
|------|-----------|
| Daily | 30 days |
| WAL | 7 days |
| Monthly | 12 months |

---

**Next Review Date:** January 2026
