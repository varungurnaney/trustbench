# Security Monitoring and Alerting Policy

**Document ID:** POL-MON-003
**Version:** 3.0
**Effective Date:** June 1, 2025
**Owner:** Security Operations

---

## 1. Purpose

This policy defines security monitoring, alerting, and response requirements for Helix Data Systems.

## 2. Monitoring Coverage

All production systems must be monitored for security-relevant events. Required monitoring sources:

| Source | Tool | Retention | Alert Routing |
|--------|------|-----------|---------------|
| Infrastructure metrics | Datadog | 15 months | PagerDuty → on-call SRE |
| Application logs | Datadog Logs | 12 months | PagerDuty → on-call SRE |
| AWS CloudTrail | Datadog SIEM | 12 months | PagerDuty → Security team |
| WAF logs | AWS WAF → Datadog | 12 months | PagerDuty → Security team |
| Endpoint detection | CrowdStrike | 12 months | CrowdStrike console → Security team |
| Vulnerability scans | Qualys | 12 months | Email report → Security Lead (weekly) |
| DNS queries | Datadog | 90 days | SIEM correlation |

## 3. Alert Configuration

### 3.1 Alert Severity

| Severity | Description | Response SLA |
|----------|-------------|-------------|
| Critical | Active exploitation, data exfiltration, ransomware | 15 minutes, 24/7 |
| High | Unauthorized access, privilege escalation, anomalous admin activity | 30 minutes, 24/7 |
| Medium | Suspicious patterns, brute force attempts, policy violations | 4 hours, business hours |
| Low | Informational, compliance events, configuration drift | Next business day |

### 3.2 Required Alert Rules

The following alerts must be configured and active:

1. **Authentication anomalies**: 5+ failed logins in 10 minutes, impossible travel, login from new country
2. **Privilege escalation**: IAM policy changes, new admin role assignments, root account usage
3. **Data exfiltration indicators**: Unusual S3 bucket access patterns, bulk API data retrieval (>10,000 records), large outbound data transfers (>1GB)
4. **Infrastructure changes**: Security group modifications, VPC changes, new EC2 instances in production
5. **Application security**: SQL injection patterns, XSS attempts, API authentication failures

### 3.3 Alert Tuning

- Alert rules are reviewed monthly by the Security team.
- False positive rates above 30% for any rule require tuning within 2 weeks.
- Suppressed or disabled alerts require CISO approval and documentation.

## 4. Alert Response

### 4.1 Triage

- On-call personnel acknowledge alerts within the response SLA.
- Acknowledged alerts are triaged as: True Positive, False Positive, or Requires Investigation.
- True positives are escalated per the incident response plan.
- False positives are documented and fed back into alert tuning.

### 4.2 Documentation

- All Critical and High alerts must have a triage note within 1 hour of acknowledgment.
- Monthly alert summary reports are produced by the Security team and reviewed by the CISO.

## 5. Monitoring Coverage Reviews

- Monitoring coverage is reviewed quarterly against the asset inventory.
- Any new production service must have monitoring configured within 5 business days of deployment.
- Coverage gaps are tracked in Jira and reported to the CISO.

---

**Approved by:** Olivia Nash, CISO
**Next Review Date:** June 2026
