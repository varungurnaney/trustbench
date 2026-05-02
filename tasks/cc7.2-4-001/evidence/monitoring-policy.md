# Atlas Cloud — Security Monitoring and Anomaly Detection Policy

**Document ID:** AC-SEC-POL-012  
**Version:** 3.0  
**Effective Date:** April 1, 2025  
**Last Reviewed:** April 1, 2025  
**Owner:** Priya Kapoor, CISO  
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy defines the requirements for security monitoring, log management, anomaly detection, and alert response for all Atlas Cloud production systems. It ensures that security events are detected, analyzed, and responded to in a timely manner consistent with SOC 2 Trust Services Criteria CC7.2.

## 2. Scope

This policy applies to all Atlas Cloud production information systems, infrastructure components, applications, and services. It covers:
- All services deployed in the production AWS environment (us-east-1, eu-west-1)
- All Kubernetes workloads in production EKS clusters
- All databases, message queues, and storage services
- All network devices and security appliances

## 3. SIEM Requirements

### 3.1 Coverage

All production services, infrastructure components, and security tools MUST be integrated with the centralized SIEM platform (Splunk Enterprise).

**Integration SLA for new services:**
- New production services must be integrated with the SIEM within **5 business days** of production deployment
- Integration includes: application logs, access logs, error logs, and audit logs
- Integration validation: confirmed log ingestion and at least one test alert generated

**Exceptions:**
- Services undergoing active decommission (with approved decommission ticket) are exempt from SIEM integration requirements
- Non-production environments (staging, development) are recommended but not required

### 3.2 Log Sources

The following log types MUST be ingested into Splunk:

| Log Source | Collection Method | Retention |
|-----------|-------------------|-----------|
| AWS CloudTrail | S3 → Splunk HEC | 365 days |
| VPC Flow Logs | CloudWatch → Splunk | 90 days |
| EKS Audit Logs | Fluent Bit → Splunk | 180 days |
| Application Logs | Fluent Bit sidecar → Splunk | 90 days |
| AWS GuardDuty | EventBridge → Splunk | 365 days |
| WAF Logs | Kinesis → Splunk | 90 days |
| Database Audit Logs (RDS) | CloudWatch → Splunk | 180 days |
| Authentication Logs (Okta) | Okta API → Splunk | 365 days |
| Endpoint Detection (CrowdStrike) | Falcon API → Splunk | 180 days |

### 3.3 Log Integrity

- All log streams must use TLS 1.2+ for transmission
- Splunk indexes are configured with immutable retention (no deletion before retention period expires)
- Log source health monitoring: alerts trigger if any log source stops sending data for >15 minutes

## 4. Alert Management

### 4.1 Alert Response SLAs

| Alert Severity | Response SLA | Description |
|---------------|-------------|-------------|
| **Critical** | **15 minutes** | Active intrusion, data exfiltration, ransomware execution, production database unauthorized access |
| **High** | 1 hour | Suspicious authentication patterns, privilege escalation attempts, malware detection |
| **Medium** | 4 hours | Policy violations, configuration drift, unusual API patterns |
| **Low** | Next business day | Informational security events, scan results, compliance alerts |

Response SLA is measured from alert generation in Splunk to first human acknowledgment in PagerDuty.

### 4.2 Alert Routing

- Critical and High alerts: PagerDuty → On-call Security Engineer (24/7 rotation)
- Medium alerts: Slack #security-alerts channel → Security Operations team (business hours)
- Low alerts: Splunk dashboard → reviewed during daily log review

### 4.3 Alert Tuning

Alert rules and thresholds must be reviewed and tuned **monthly** to reduce false positives and ensure detection effectiveness. The alert tuning process includes:

1. Review of false positive rates per alert rule
2. Adjustment of thresholds based on 30-day baseline
3. Addition of new detection rules based on threat intelligence
4. Documentation of tuning changes in the Alert Rule Change Log
5. Approval by the Security Operations Lead

### 4.4 Alert Rule Inventory

Atlas Cloud maintains a minimum of 150 active alert rules across the following categories:
- Authentication anomalies (brute force, impossible travel, credential stuffing)
- Privilege escalation and unauthorized access
- Data exfiltration indicators (large data transfers, unusual API calls)
- Infrastructure anomalies (resource creation, configuration changes)
- Malware and endpoint threats
- Network anomalies (port scanning, lateral movement)
- Compliance violations (unencrypted data, policy overrides)

## 5. Daily Log Review

### 5.1 Requirements

The Security Operations team must conduct a **daily log review** of SIEM data, covering:
- Summary of alerts generated in the prior 24 hours
- Review of authentication anomaly dashboard
- Review of high-privilege activity dashboard
- Review of data access patterns dashboard
- Check for log source health issues

### 5.2 Documentation

Daily log reviews must be documented with:
- Reviewer name and timestamp
- Summary of findings (or confirmation of no anomalies)
- Any escalation actions taken
- Sign-off by the reviewing analyst

## 6. Monitoring Coverage Validation

### 6.1 Quarterly Coverage Audit

The Security Operations team must conduct a quarterly audit of SIEM coverage to verify:
- All production services are integrated
- All required log sources are actively ingesting
- Alert rules cover the required categories
- Retention periods are enforced

### 6.2 Service Inventory Reconciliation

The SIEM service inventory must be reconciled with the CMDB (ServiceNow) quarterly to identify:
- New services not yet integrated
- Decommissioned services that should be removed
- Services with degraded log ingestion

## 7. Metrics and Reporting

The Security Operations team reports the following metrics monthly to the CISO:
- SIEM coverage percentage (target: 100% of production services)
- Mean time to acknowledge (MTTA) for Critical and High alerts
- Alert volume and false positive rate by category
- Log source health score (percentage of sources ingesting without gaps)

## 8. Exceptions

Exceptions to SIEM integration or alert response requirements must be documented in the Security Exception Register with:
- Business justification
- Compensating controls
- Risk acceptance by the CISO
- Expiration date (maximum 6 months)

---

*Approved by: Derek Owens, CTO — March 28, 2025*
