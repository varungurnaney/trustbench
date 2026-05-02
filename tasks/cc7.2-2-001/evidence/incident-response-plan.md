# Incident Response Plan

**Document ID:** POL-IR-001
**Version:** 3.0
**Effective Date:** July 1, 2025
**Owner:** Security Operations
**Classification:** Confidential

---

## 1. Purpose

This plan establishes procedures for detecting, responding to, and recovering from security incidents at Pinnacle SaaS Inc.

## 2. Definitions

- **Security Event:** An observable occurrence relevant to information security.
- **Security Incident:** A security event that has been assessed as having an actual adverse effect on confidentiality, integrity, or availability.
- **Severity Levels:**
  - **P1 (Critical):** Data breach, ransomware, complete system outage
  - **P2 (High):** Unauthorized access to production, partial outage
  - **P3 (Medium):** Suspicious activity, failed intrusion attempts
  - **P4 (Low):** Policy violations, phishing (no credential compromise)

## 3. Detection

### 3.1 Monitoring Sources

| Source | Tool | Alert Routing |
|--------|------|---------------|
| Infrastructure logs | Datadog | #alerts-infra Slack channel |
| Application logs | Datadog | #alerts-app Slack channel |
| AWS CloudTrail | Datadog | #alerts-security Slack channel |
| Endpoint detection | CrowdStrike | Security team email |
| Email security | Proofpoint | IT team email |
| Vulnerability scans | Qualys | Weekly report to Security Lead |

### 3.2 Alert Triage

- P1/P2 alerts are triaged within 15 minutes during business hours.
- On-call SRE responds to P1 alerts 24/7 within 30 minutes.
- P3/P4 alerts are reviewed during the next business day.

## 4. Response Procedures

### 4.1 Incident Commander

For P1/P2 incidents, the Security Lead assumes Incident Commander role.

### 4.2 Response Timeline

| Phase | P1 | P2 | P3 | P4 |
|-------|----|----|----|----|
| Triage | 15 min | 15 min | Next business day | Next business day |
| Containment | 1 hour | 4 hours | 48 hours | 1 week |
| Eradication | 24 hours | 72 hours | 1 week | 2 weeks |
| Recovery | 48 hours | 1 week | 2 weeks | Best effort |

### 4.3 Communication

- Internal: Status updates posted to #incident-response Slack channel every 30 minutes during active P1 incidents.
- Customer notification: For data breaches affecting customer data, customers are notified within 72 hours per contractual SLAs.
- Regulatory: Legal team handles regulatory notification requirements.

### 4.4 Evidence Preservation

- All logs relevant to the incident are exported and preserved.
- Memory dumps and disk images are captured for P1 incidents.
- Chain of custody is maintained for forensic evidence.

## 5. Post-Incident

### 5.1 Post-Mortem

- P1/P2 incidents require a written post-mortem within 5 business days.
- Post-mortem includes: timeline, root cause, impact assessment, and action items.
- Post-mortems are reviewed by the Security Governance Committee monthly.

### 5.2 Lessons Learned

- Action items from post-mortems are tracked in Jira.
- Detection rules are updated based on incident learnings.

## 6. Plan Testing

The incident response plan is tested annually through a tabletop exercise facilitated by the Security Lead. Results are documented and presented to executive leadership.

## 7. Roles and Responsibilities

| Role | Responsibility |
|------|----------------|
| Security Lead | Incident Commander for P1/P2; owns the IRP |
| SRE On-Call | First responder for infrastructure alerts |
| Engineering Lead | Technical escalation point |
| Legal | Regulatory notification and external communications |
| VP Engineering | Executive escalation for P1 incidents |
| HR | Insider threat incidents |

## 8. Contact List

Maintained separately in the Security Operations Runbook (internal wiki). Updated quarterly by the Security Lead.

---

**Approved by:** Maria Santos, VP Engineering
**Next Review Date:** July 2026
