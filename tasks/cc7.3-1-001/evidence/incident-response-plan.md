# Incident Response Plan

**Document ID:** IRP-2025-001
**Version:** 2.1
**Effective Date:** March 15, 2025
**Owner:** Security Operations Team
**Classification:** Internal — Confidential

---

## 1. Purpose and Scope

This Incident Response Plan (IRP) establishes the procedures for NovaBridge Technologies to detect, assess, respond to, and recover from security incidents affecting the company's SaaS platform and supporting infrastructure.

**Scope:** All production systems, staging environments, corporate IT, and third-party integrations used in the delivery of NovaBridge's customer-facing analytics platform.

## 2. Definitions

- **Security Event:** Any observable occurrence in a system or network that is relevant to information security.
- **Security Incident:** A security event that has been confirmed to adversely affect the confidentiality, integrity, or availability of NovaBridge systems or data.
- **Data Breach:** A security incident resulting in unauthorized access to, or disclosure of, customer data or personally identifiable information (PII).

### 2.1 Severity Classification

| Severity | Definition | Examples |
|----------|-----------|----------|
| P1 — Critical | Active data breach, ransomware, complete platform outage | Customer database exfiltration, crypto-ransomware on production hosts |
| P2 — High | Unauthorized access to production, partial outage affecting >10% of customers | Compromised admin credentials, API gateway failure |
| P3 — Medium | Suspicious activity under investigation, limited service degradation | Anomalous login patterns, single-tenant performance issue |
| P4 — Low | Policy violations, unsuccessful attack attempts | Failed phishing attempts, port scan activity |

## 3. Incident Response Team

### 3.1 Team Composition

| Role | Primary | Backup |
|------|---------|--------|
| Incident Commander | Derek Huang, Director of Security | Amanda Foster, Sr. Security Engineer |
| Technical Lead | Ryan Okonkwo, Principal SRE | Lisa Tran, Staff Engineer |
| Forensics Lead | Sarah Mitchell, Security Analyst | Derek Huang |
| Executive Sponsor | James Whitfield, CTO | Nadia Petrov, VP Engineering |

### 3.2 On-Call Rotation

- **24/7 on-call SRE:** Rotates weekly among 4 SREs. Monitored via PagerDuty.
- **Security on-call:** Derek Huang and Amanda Foster alternate weekly.
- **Escalation path:** SRE on-call -> Security on-call -> Incident Commander -> Executive Sponsor.

## 4. Detection and Triage

### 4.1 Detection Sources

| Source | Tool | Alert Channel |
|--------|------|---------------|
| Infrastructure metrics | Datadog | PagerDuty (P1/P2), #alerts-infra Slack (P3/P4) |
| Application logs | Splunk | PagerDuty (P1/P2), #alerts-app Slack (P3/P4) |
| Cloud audit logs (AWS CloudTrail) | Splunk | #alerts-security Slack |
| Endpoint detection | SentinelOne | Security team email + PagerDuty (Critical) |
| Email gateway | Mimecast | IT helpdesk queue |
| WAF events | Cloudflare | #alerts-security Slack |

### 4.2 Triage SLAs

| Severity | Initial Triage | Containment Start | Resolution Target |
|----------|---------------|-------------------|-------------------|
| P1 | 15 minutes | 1 hour | 24 hours |
| P2 | 30 minutes | 4 hours | 72 hours |
| P3 | 4 hours | 24 hours | 1 week |
| P4 | Next business day | Best effort | 2 weeks |

## 5. Response Procedures

### 5.1 Containment

Upon confirming a security incident:

1. Incident Commander declares incident severity and opens a dedicated Slack channel (#inc-YYYY-NNN).
2. Technical Lead assesses blast radius and begins containment:
   - Network isolation of affected systems
   - Credential rotation for compromised accounts
   - Firewall rule updates to block attacker IPs
3. All containment actions are logged in the incident ticket (Jira project: SEC).

### 5.2 Eradication

1. Forensics Lead identifies root cause and attack vector.
2. Technical Lead removes malicious artifacts, patches vulnerabilities, and verifies system integrity.
3. Forensics Lead confirms eradication is complete before recovery begins.

### 5.3 Recovery

1. Systems are restored from known-good backups or rebuilt from infrastructure-as-code.
2. Technical Lead performs smoke testing before returning systems to production.
3. Enhanced monitoring is enabled for 72 hours post-recovery.
4. Incident Commander confirms recovery is complete and closes the incident channel.

## 6. Evidence Preservation

### 6.1 Requirements

- For P1/P2 incidents: Full disk images, memory dumps, network packet captures, and relevant log exports must be collected within 4 hours of incident declaration.
- For P3/P4 incidents: Relevant log exports and screenshots are sufficient.
- All evidence is stored in a dedicated S3 bucket (s3://novabridge-ir-evidence/) with versioning enabled and access restricted to the IR team.

### 6.2 Chain of Custody

- Each evidence item is logged with: collector name, collection time, hash (SHA-256), and storage location.
- Evidence access is logged via CloudTrail.

## 7. Post-Incident Activities

### 7.1 Post-Mortem Reports

- P1 incidents: Post-mortem due within 3 business days of resolution.
- P2 incidents: Post-mortem due within 5 business days of resolution.
- P3/P4 incidents: Post-mortem optional, at Incident Commander's discretion.

### 7.2 Post-Mortem Contents

Each post-mortem report must include:
1. Incident timeline (detection through resolution)
2. Root cause analysis (using 5-Whys or Fishbone method)
3. Impact assessment (systems affected, data exposed, customer impact)
4. Remediation actions taken
5. Preventive action items with owners and due dates

### 7.3 Action Item Tracking

- All action items from post-mortems are tracked in Jira (project: SEC-PM).
- Action items are reviewed weekly in the Security Operations standup.
- Overdue action items are escalated to the Executive Sponsor after 30 days.

## 8. Plan Testing and Maintenance

### 8.1 Testing

- The IRP is tested annually through a tabletop exercise.
- Exercise scenarios are developed by the Incident Commander.
- Results and improvement recommendations are documented.

### 8.2 Plan Updates

- The IRP is reviewed and updated at least annually or after any P1 incident.
- Changes require approval from the CTO.

---

**Approved by:** James Whitfield, CTO
**Approval Date:** March 10, 2025
**Next Review Date:** March 2026
