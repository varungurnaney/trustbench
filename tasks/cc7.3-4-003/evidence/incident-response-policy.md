# Incident Response Policy

**Document ID:** POL-SEC-IRP-004
**Version:** 2.8
**Effective Date:** April 1, 2025
**Owner:** Security Engineering, Stratosphere AI
**Classification:** Internal — Restricted

---

## 1. Purpose

This policy defines the incident response procedures for Stratosphere AI, a provider of enterprise AI model training and inference services. The policy covers detection, response, containment, communication, and recovery for all security incidents.

## 2. Severity Levels

| Level | Name | Definition |
|-------|------|-----------|
| P1 | Critical | Active data exfiltration, ransomware, model poisoning, or full platform outage |
| P2 | Major | Unauthorized access to training data or model artifacts, partial outage (>25% impact), credential compromise |
| P3 | Moderate | Suspicious activity, failed attacks, minor service degradation |
| P4 | Minor | Policy violations, blocked threats, informational |

## 3. Response SLAs

### 3.1 Triage

| Severity | SLA | Coverage |
|----------|-----|----------|
| P1 | 15 minutes | 24/7/365 |
| P2 | 30 minutes | 24/7/365 |
| P3 | 4 hours | Business hours (M-F 9AM-6PM PT) |
| P4 | Next business day | Business hours |

### 3.2 Containment

| Severity | SLA |
|----------|-----|
| P1 | 1 hour |
| P2 | 4 hours |
| P3 | 24 hours |
| P4 | Best effort |

### 3.3 Resolution

| Severity | Target |
|----------|--------|
| P1 | 24 hours |
| P2 | 72 hours |
| P3 | 1 week |
| P4 | 2 weeks |

## 4. Roles and Responsibilities

| Role | Primary | Backup |
|------|---------|--------|
| Incident Commander | Wei Zhang, Head of Security | Sanjay Krishnan, Security Engineering Lead |
| Technical Lead | Natasha Volkov, Principal SRE | Omar Hassan, Staff Platform Engineer |
| Forensics | Sanjay Krishnan | Wei Zhang |
| Communications | Emily Barton, VP Customer Success | Legal (external counsel) |
| Executive Sponsor | Tom Richardson, CEO | Wei Zhang |

## 5. Post-Mortem Requirements

### 5.1 Timelines

- P1: Due within 3 business days of resolution.
- P2: Due within 5 business days of resolution.
- P3/P4: Not required.

### 5.2 Content Requirements

Post-mortems must include:
1. Complete incident timeline (UTC timestamps)
2. Root cause analysis (5-Whys)
3. Impact assessment (systems, data, customers, models affected)
4. For AI-specific incidents: model integrity verification results
5. Preventive action items with owners and target dates
6. Detection improvement recommendations

### 5.3 Action Item Governance

- Action items entered in Linear (project: SEC-PM) within 2 business days.
- Reviewed weekly in Thursday Security Standup.
- Items overdue >14 days escalated to Head of Security.
- Items overdue >30 days escalated to CEO.

## 6. Customer Communication

### 6.1 Notification SLAs

- P1 (data breach): Affected customers notified within 72 hours of confirmation.
- P2 (service impact): Status page updated within 30 minutes. Customer email within 24 hours.
- Model integrity incidents: Affected customers notified within 48 hours with model retraining timeline.

### 6.2 Status Page

Maintained at status.stratosphere-ai.com. Updated automatically from PagerDuty for infrastructure incidents. Manual updates for security incidents by Communications Lead.

## 7. Evidence Preservation

- P1/P2: Full disk images, GPU memory state capture, training data access logs (120-day lookback), model checkpoint diffs.
- Chain of custody with SHA-256 hashes.
- Evidence stored in isolated S3 bucket with write-once policy.

## 8. Plan Testing

- Semi-annual tabletop exercises (March and September).
- Annual red team engagement with external firm.
- Tabletop scenarios must cover at least one AI-specific incident type per year (model poisoning, training data exfiltration, prompt injection).

---

**Approved by:** Tom Richardson, CEO
**Approval Date:** March 28, 2025
**Next Review Date:** April 2026
