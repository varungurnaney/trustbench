# Polaris Financial — Security Monitoring and Event Management Policy

**Document ID:** POL-SEC-MON-003
**Version:** 4.0
**Effective Date:** January 1, 2025
**Owner:** Andre Williams, CISO
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy establishes requirements for comprehensive security monitoring, event correlation, and anomaly detection across all Polaris Financial production systems.

## 2. Scope

All production systems across AWS (us-east-1, eu-west-1) supporting Polaris Financial's investment management platform.

## 3. SIEM Requirements

### 3.1 Coverage

All production services must be integrated with the SIEM (Splunk Enterprise Security) within 5 business days of deployment.

### 3.2 Log Sources

Required log types:
- Application logs, access logs, audit logs
- Authentication logs (Azure AD)
- AWS CloudTrail, VPC Flow Logs, GuardDuty
- Database activity logs
- WAF logs
- Endpoint detection (CrowdStrike)

### 3.3 Log Retention

| Log Type | Retention |
|----------|-----------|
| Authentication / Audit | 7 years (regulatory) |
| Application | 1 year |
| CloudTrail | 7 years |
| VPC Flow Logs | 1 year |

## 4. Alert Management

### 4.1 Alert Severity and SLAs

| Severity | Response SLA | Coverage |
|----------|-------------|----------|
| Critical | 10 minutes | 24/7 |
| High | 30 minutes | 24/7 |
| Medium | 2 hours | Business hours |
| Low | Next business day | Business hours |

### 4.2 Alert Tuning

Alert rules must be reviewed monthly. False positive rates exceeding 25% require tuning within 10 business days. Tuning changes must be documented in the Alert Tuning Log and approved by the Security Operations Lead.

### 4.3 Disabled Alert Rules

No alert rule may be disabled without:
- Documented justification
- CISO approval
- Compensating detection control
- Maximum 90-day disable period
- Re-evaluation before re-enabling

## 5. Privileged Activity Monitoring

### 5.1 Scope

The following privileged activities must be monitored with real-time alerting:
- Root/admin account usage
- IAM policy modifications
- Security group changes
- Database admin operations
- Production configuration changes
- Data export operations exceeding 1GB

### 5.2 Review

Privileged activity reports must be reviewed weekly by the Security Operations Lead with sign-off documentation.

## 6. Daily Log Review

Daily SIEM dashboard review must be conducted and documented with:
- Reviewer name, timestamp
- Findings summary
- Sign-off

---

**Approved by:** Lisa Chang, CFO (Regulatory Compliance Sponsor)
