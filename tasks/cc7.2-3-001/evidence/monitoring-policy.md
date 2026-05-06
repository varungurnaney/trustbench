# Cascade Systems — Security Monitoring Policy

**Document ID:** CAS-SEC-POL-009
**Version:** 2.2
**Effective Date:** January 15, 2025
**Owner:** Derek Hall, Director of Security Operations
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy defines requirements for security monitoring, SIEM integration, and anomaly detection across all Cascade Systems production infrastructure.

## 2. Scope

All production services deployed in AWS (us-east-1, eu-west-1) supporting the Cascade customer data platform.

## 3. SIEM Integration

### 3.1 Coverage Requirement

All production services MUST be integrated with the centralized SIEM (Splunk Cloud) within **7 business days** of production deployment.

### 3.2 Integration Validation

SIEM integration is considered complete when:
- Application logs, access logs, and audit logs are ingested
- Log ingestion is verified in Splunk (search returns results for the new service)
- At least one service-specific alert rule is configured
- Integration is documented in the SIEM Coverage Tracker

### 3.3 Log Retention

| Log Type | Retention Period |
|----------|-----------------|
| Application logs | 90 days |
| Authentication logs | 365 days |
| Audit logs | 365 days |
| CloudTrail | 365 days |
| VPC Flow Logs | 90 days |

## 4. Alert Configuration

### 4.1 Required Alert Categories

Every production service must have alerts configured for:
- Error rate anomalies
- Authentication failures
- Data access anomalies (for data-handling services)
- Availability and health check failures

### 4.2 Response SLAs

| Severity | Response SLA | Coverage |
|----------|-------------|----------|
| Critical | 15 minutes | 24/7 |
| High | 30 minutes | 24/7 |
| Medium | 4 hours | Business hours |
| Low | Next business day | Business hours |

## 5. Monitoring Coverage Audits

A quarterly monitoring coverage audit must reconcile the SIEM service inventory against the deployment registry (ServiceNow CMDB) to identify gaps.

---

**Approved by:** Megan Torres, CISO
