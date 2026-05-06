# Incident Response Policy

**Document ID:** IRP-POL-2025-001
**Version:** 5.0
**Effective Date:** January 15, 2025
**Owner:** Security Operations, Vantage Cloud Systems
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy defines how Vantage Cloud Systems responds to security incidents affecting the company's enterprise cloud storage and collaboration platform.

## 2. Severity Classification

| Severity | Name | Definition |
|----------|------|-----------|
| SEV-1 | Critical | Active data breach, ransomware execution, or total platform outage |
| SEV-2 | High | Unauthorized system access, suspected data exposure, or degradation affecting >20% of users |
| SEV-3 | Medium | Suspicious activity under investigation, minor service impact |
| SEV-4 | Low | Policy violations, blocked attacks, informational events |

## 3. Response SLAs

### 3.1 Triage SLAs

| Severity | Triage SLA | Coverage |
|----------|-----------|----------|
| SEV-1 | 15 minutes | 24/7/365 |
| SEV-2 | 30 minutes | 24/7/365 |
| SEV-3 | 4 hours | Business hours (M-F 9AM-6PM ET) |
| SEV-4 | Next business day | Business hours |

### 3.2 Containment SLAs

| Severity | Containment SLA |
|----------|----------------|
| SEV-1 | 1 hour |
| SEV-2 | 4 hours |
| SEV-3 | 24 hours |
| SEV-4 | Best effort |

### 3.3 Resolution Targets

| Severity | Resolution Target |
|----------|------------------|
| SEV-1 | 24 hours |
| SEV-2 | 72 hours |
| SEV-3 | 1 week |
| SEV-4 | 2 weeks |

## 4. Post-Mortem Requirements

### 4.1 Timelines

- SEV-1: Post-mortem due within 3 business days of resolution.
- SEV-2: Post-mortem due within 5 business days of resolution.
- SEV-3/SEV-4: At Incident Commander's discretion.

### 4.2 Required Sections

All SEV-1 and SEV-2 post-mortems must include:
1. Incident timeline with UTC timestamps
2. Root cause analysis (5-Whys)
3. Impact assessment (systems, data, customers affected)
4. Remediation actions taken
5. Preventive action items with assigned owner, priority, and target date
6. Detection improvement recommendations

### 4.3 Action Item Tracking

- Action items entered in Jira project VCS-PM within 2 business days of post-mortem.
- Reviewed weekly in Tuesday Security Operations standup.
- Items overdue >14 days escalated to CISO.

## 5. Communication

### 5.1 Internal

- P1: Updates every 15 minutes in #incident-war-room Slack.
- P2: Updates every 30 minutes.

### 5.2 External

- Data breach: Customer notification within 72 hours of confirmation per contractual SLAs.
- Service disruption: Status page updated within 30 minutes of SEV-1/SEV-2 declaration.
- Regulatory: DPO handles GDPR/CCPA notifications within statutory deadlines.

## 6. Evidence Preservation

- SEV-1/SEV-2: Full disk images, memory dumps, log exports (90-day lookback).
- Chain of custody maintained with SHA-256 hashes and collector attribution.
- Evidence stored in s3://vantage-ir-evidence/ with versioning and access logging.

## 7. Plan Testing

- Annual tabletop exercise with full IR team.
- Semi-annual purple team exercise with external firm.
- Results documented with improvement action items.

---

**Approved by:** Robert Langston, CEO
**Approval Date:** January 12, 2025
**Next Review Date:** January 2026
