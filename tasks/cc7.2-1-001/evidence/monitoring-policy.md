# Beacon Health — Security Monitoring and Alerting Policy

**Document ID:** BHC-SEC-POL-004
**Version:** 1.3
**Effective Date:** April 1, 2025
**Owner:** Information Security Team
**Classification:** Internal

---

## 1. Purpose

This policy establishes requirements for monitoring Beacon Health's production systems to detect anomalies, security events, and operational issues in a timely manner.

## 2. Scope

This policy applies to all production systems, applications, and infrastructure components supporting Beacon Health's electronic health records (EHR) platform.

## 3. Monitoring Sources

### 3.1 Log Collection

The following log sources must be collected and forwarded to the centralized logging platform (Elastic Stack):

- Application logs from all production services
- Web server access logs (nginx)
- Authentication logs from Okta SSO
- AWS CloudTrail API activity logs
- VPC Flow Logs
- Database query logs (slow query log only)

### 3.2 Infrastructure Monitoring

Infrastructure health is monitored via Datadog:
- CPU, memory, disk, and network utilization
- Container health and restart events
- Load balancer health checks
- RDS instance performance metrics

## 4. Alerting

### 4.1 Alert Categories

Alerts are configured for the following categories:
- Application errors exceeding threshold (>1% error rate over 5 minutes)
- Infrastructure resource exhaustion (>90% CPU or memory)
- SSL certificate expiration (30-day warning)
- Failed login attempts exceeding threshold (>10 failures per account per hour)
- Unusual geographic access patterns

### 4.2 Alert Routing

- Critical alerts: PagerDuty → on-call SRE (24/7)
- Warning alerts: Slack #ops-alerts → engineering team (business hours)
- Informational alerts: Elastic dashboards → reviewed weekly

### 4.3 Alert Response

The on-call SRE is responsible for triaging and responding to alerts. Critical alerts must be acknowledged within 30 minutes. All other alerts are addressed during business hours.

## 5. Log Review

Security-relevant logs should be reviewed periodically to identify potential threats or anomalies.

## 6. Metrics and Reporting

Monthly security metrics are reported to the CISO:
- Alert volume by category
- Mean time to acknowledge for critical alerts
- System uptime percentage

## 7. Policy Review

This policy is reviewed annually by the Information Security Team.

---

**Approved by:** Diane Marshall, CISO
**Next Review Date:** April 2026
