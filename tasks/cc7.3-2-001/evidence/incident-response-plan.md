# Incident Response Plan

**Document ID:** SEC-IRP-003
**Version:** 4.2
**Effective Date:** January 1, 2025
**Owner:** Chief Information Security Officer
**Classification:** Internal — Restricted

---

## 1. Purpose

This Incident Response Plan (IRP) defines how Crestfield Data Solutions detects, responds to, contains, remediates, and recovers from security incidents. The plan ensures that Crestfield meets its obligations to customers, regulators, and stakeholders regarding the protection of sensitive data processed through its B2B data integration platform.

## 2. Scope

This plan applies to all Crestfield production systems (AWS us-east-1 and eu-west-1 regions), corporate IT infrastructure, employee endpoints, and third-party integrations involved in processing customer data.

## 3. Severity Levels

| Level | Name | Definition | Examples |
|-------|------|-----------|----------|
| P1 | Critical | Active data exfiltration, ransomware execution, or complete platform outage | Confirmed breach with customer PII exposed, CryptoLocker on production database server |
| P2 | Major | Unauthorized access to production systems, suspected data exposure, or service degradation affecting >25% of customers | Compromised engineer SSH key used to access production, suspicious bulk API data export, primary database failover |
| P3 | Moderate | Anomalous activity under active investigation, minor service degradation | Unusual CloudTrail activity from known IP, single-tenant latency spike |
| P4 | Minor | Policy violations, blocked attacks, informational alerts | Failed phishing attempt (no credential compromise), blocked malware download, vulnerability scan from external IP |

## 4. Roles and Responsibilities

### 4.1 Incident Response Team

| Role | Primary Assignee | Backup |
|------|-----------------|--------|
| Incident Commander (IC) | Kathryn Velasco, CISO | Marcus Webb, Security Engineering Manager |
| Technical Lead | Daniel Reeves, Principal SRE | Priya Sundaram, Staff Platform Engineer |
| Forensic Analyst | Tomoko Ishida, Sr. Security Analyst | Marcus Webb |
| Communications Lead | Rachel Torres, VP Customer Success | Gregory Dawson, Head of Legal |
| Executive Sponsor | Nathan Cross, CEO | Kathryn Velasco, CISO |

### 4.2 RACI Matrix

| Activity | IC | Tech Lead | Forensics | Comms Lead | Exec Sponsor |
|----------|-----|-----------|-----------|------------|--------------|
| Severity Declaration | A/R | C | C | I | I |
| Containment Decisions | A | R | C | I | I |
| Root Cause Analysis | I | C | A/R | I | I |
| External Communication | C | I | I | A/R | A |
| Post-Mortem Authorship | A | R | R | I | I |

## 5. Detection and Initial Response

### 5.1 Monitoring Stack

Crestfield maintains the following monitoring and alerting capabilities:

- **SIEM:** Splunk Enterprise (on-premises) ingesting logs from all production services, AWS CloudTrail, VPC Flow Logs, and endpoint telemetry.
- **EDR:** CrowdStrike Falcon deployed on all endpoints (servers and workstations).
- **Cloud Security:** AWS GuardDuty, AWS Security Hub, and custom CloudWatch alarms.
- **Application Monitoring:** Datadog APM with custom security-relevant metrics.
- **Email Security:** Microsoft Defender for Office 365 with advanced threat protection.
- **Network Monitoring:** Zeek (network metadata) and Suricata (IDS) on production VPCs.

### 5.2 Alert Routing and On-Call

**P1 Alerts:**
- Routed to PagerDuty with 24/7 on-call SRE and Security on-call simultaneously.
- SRE on-call rotation: 4 engineers, weekly rotation, 5-minute acknowledgment SLA.
- Security on-call rotation: 2 security engineers (Tomoko Ishida and Marcus Webb), bi-weekly rotation.
- Automatic escalation to Incident Commander if not acknowledged within 10 minutes.

**P2 Alerts:**
- Routed to PagerDuty during business hours (Monday-Friday, 8:00 AM - 6:00 PM ET).
- After-hours P2 alerts are queued and reviewed at the start of the next business day.
- Business-hours SLA: 30-minute triage by the security team.

**P3 Alerts:**
- Posted to #security-alerts Slack channel.
- Reviewed during daily security standup (10:00 AM ET, Monday-Friday).

**P4 Alerts:**
- Logged in Splunk. Reviewed as part of weekly threat intelligence summary.

## 6. Response Procedures

### 6.1 Incident Declaration

When a security event is confirmed as an incident:
1. Incident Commander is notified and declares severity.
2. A dedicated incident Slack channel is created (#inc-YYYY-NNN).
3. A Jira ticket is created in the SEC project with severity label.
4. War room video bridge is opened for P1/P2 incidents.

### 6.2 Containment

| Severity | Containment SLA | Authorized Actions |
|----------|----------------|-------------------|
| P1 | 1 hour | Network isolation, credential revocation, service shutdown, DNS sinkhole |
| P2 | 4 hours | Account lockout, API key rotation, firewall rule insertion, service throttling |
| P3 | 24 hours | Access review, log export, enhanced monitoring |
| P4 | Best effort | Ticket creation, policy reminder to affected user |

### 6.3 Eradication

1. Forensic Analyst identifies all compromised systems and attack vectors.
2. Technical Lead coordinates patching, malware removal, and configuration hardening.
3. Forensic Analyst verifies eradication through IOC scanning and integrity checks.

### 6.4 Recovery

1. Systems restored from verified backups or rebuilt from infrastructure-as-code (Terraform).
2. Recovery validation: smoke tests, integrity checks, and customer-facing functionality verification.
3. Enhanced monitoring enabled for 7 calendar days post-recovery.
4. Incident Commander approves return to normal operations.

## 7. Communication

### 7.1 Internal Communication

- P1: Status updates to #incident-response Slack every 15 minutes during active response.
- P2: Status updates every 30 minutes during business hours.
- P3/P4: Updates as significant new information is available.
- Executive briefing within 2 hours of P1 declaration.

### 7.2 Customer Communication

- **P1 (confirmed data breach):** Affected customers notified within 72 hours of breach confirmation via email from Communications Lead. Status page updated immediately.
- **P2 (service degradation):** Status page updated within 1 hour. Customer-facing post-incident summary within 5 business days.
- **P3/P4:** No customer notification unless specifically requested by Incident Commander.

### 7.3 Regulatory Notification

- GDPR: Data Protection Officer (Gregory Dawson) submits notification to relevant supervisory authority within 72 hours of confirming a personal data breach.
- CCPA: Written notification to affected California residents within the statutory timeframe.
- Contractual: Customer contracts reviewed for specific notification SLAs; Comms Lead coordinates.

## 8. Evidence Preservation

### 8.1 Collection Requirements

| Severity | Evidence Requirements |
|----------|---------------------|
| P1 | Full disk images, memory dumps, network captures, all relevant logs (90-day lookback) |
| P2 | Relevant logs (30-day lookback), screenshots, access logs for compromised accounts |
| P3/P4 | Relevant log exports, alert screenshots |

### 8.2 Storage and Chain of Custody

- Evidence stored in s3://crestfield-ir-evidence/ with AES-256 encryption and versioning.
- Each evidence artifact logged with: collector, timestamp, SHA-256 hash, and storage path.
- Access restricted to IR team via IAM policy. Access logged via CloudTrail.
- Evidence retained for 7 years per legal hold policy.

## 9. Post-Incident Activities

### 9.1 Post-Mortem Requirements

| Severity | Post-Mortem Due | Mandatory Sections |
|----------|----------------|-------------------|
| P1 | 3 business days after resolution | Timeline, root cause, impact, remediation, 5-Whys, action items |
| P2 | 5 business days after resolution | Timeline, root cause, impact, action items |
| P3 | 10 business days (optional, IC discretion) | Summary, root cause, action items |
| P4 | Not required | N/A |

### 9.2 Action Item Tracking

- All post-mortem action items logged in Jira project SEC-PM.
- Each action item assigned to an owner with a target completion date.
- Overdue items reviewed in weekly Security Operations meeting.
- Items overdue by more than 14 calendar days escalated to CISO.

### 9.3 Lessons Learned

- Post-mortems reviewed in monthly Security Governance Committee meeting.
- Detection rules updated based on incident findings.
- IRP updated if process gaps are identified during post-mortem review.

## 10. Plan Testing and Maintenance

### 10.1 Testing Schedule

- **Annual tabletop exercise:** Facilitated by CISO, with participation from all IR team members and executive sponsor.
- **Bi-annual purple team exercise:** Conducted with external penetration testing firm to validate detection and response capabilities.
- Results documented and improvement action items tracked in Jira.

### 10.2 Plan Maintenance

- IRP reviewed annually or after any P1 incident.
- Changes approved by CISO and CEO.
- Version history maintained in Confluence.

---

**Approved by:** Nathan Cross, CEO
**Approval Date:** December 20, 2024
**Next Review Date:** January 2026
