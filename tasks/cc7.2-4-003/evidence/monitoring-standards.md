# Zenith Commerce — Security Monitoring Standards

**Document ID:** ZEN-SEC-STD-008
**Version:** 2.5
**Effective Date:** March 1, 2025
**Owner:** Patricia Okonkwo, Director of Security Operations
**Classification:** Internal — Confidential

---

## 1. Purpose

This document defines the security monitoring standards for Zenith Commerce's e-commerce platform, including log collection, SIEM integration, alert management, and monitoring coverage requirements.

## 2. Scope

All production systems in AWS (us-east-1, eu-west-1) supporting the Zenith Commerce marketplace platform.

## 3. SIEM Integration

### 3.1 Platform

Zenith Commerce uses Datadog Security Monitoring as its SIEM platform.

### 3.2 Integration SLA

New production services must be integrated with Datadog Security Monitoring within **3 business days** of deployment.

### 3.3 Required Log Sources

All production services must forward:
- Application logs (structured JSON)
- Access/request logs
- Authentication and authorization logs
- Error logs with stack traces

### 3.4 Log Retention

- Hot storage (searchable): 30 days
- Warm storage (archive, queryable within 4 hours): 1 year
- Cold storage (S3 archive): 7 years

## 4. Alert Configuration

### 4.1 Minimum Alert Rules Per Service

Every production service must have at minimum:
- Error rate anomaly detection (baseline + 3 standard deviations)
- Authentication failure threshold (>5 failures in 10 minutes per account)
- Latency anomaly detection (p99 > 2x baseline)
- Availability monitoring (health check failure for >2 minutes)

### 4.2 Response SLAs

| Severity | SLA | Coverage |
|----------|-----|----------|
| P1 (Critical) | 5 minutes | 24/7 |
| P2 (High) | 15 minutes | 24/7 |
| P3 (Medium) | 1 hour | Business hours |
| P4 (Low) | 8 hours | Business hours |

### 4.3 Alert Routing

- P1/P2: PagerDuty → dual-pager (Security + SRE on-call)
- P3: Slack #security-events → Security Operations (business hours)
- P4: Datadog dashboard → reviewed in daily standup

### 4.4 False Positive Management

Alert rules with false positive rates exceeding 20% must be tuned within 5 business days. Tuning changes documented in the Datadog Audit Trail.

## 5. Monitoring Coverage Validation

### 5.1 Continuous Reconciliation

A daily automated job reconciles the Datadog service catalog against the AWS resource inventory (via AWS Config). New services detected without Datadog agents trigger a P3 alert.

### 5.2 Quarterly Audit

Manual quarterly audit of monitoring coverage including:
- Service inventory reconciliation
- Alert rule completeness per service
- Log retention compliance
- False positive rate review

## 6. Third-Party Service Monitoring

### 6.1 Requirement

Critical third-party services (payment processors, CDN, DNS) must be monitored via synthetic checks with alerting for availability and latency degradation.

---

**Approved by:** Raj Malhotra, CTO
