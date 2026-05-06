# Incident Response Policy

**Document ID:** SEC-IRP-2025-011
**Version:** 2.3
**Effective Date:** March 1, 2025
**Owner:** Security Operations, Prism Data Platform
**Classification:** Confidential

---

## 1. Purpose

This policy defines the incident response procedures for Prism Data Platform, a real-time data streaming and analytics provider serving enterprise customers across financial services, healthcare, and retail sectors.

## 2. Severity Classification

| Severity | Name | Definition |
|----------|------|-----------|
| SEV-1 | Critical | Confirmed data breach, ransomware, complete platform outage |
| SEV-2 | High | Unauthorized access, suspected data exposure, >20% customer impact |
| SEV-3 | Medium | Suspicious activity, minor degradation, failed intrusions |
| SEV-4 | Low | Policy violations, blocked threats, informational |

## 3. Response SLAs

| Severity | Triage | Containment | Resolution | Coverage |
|----------|--------|-------------|------------|----------|
| SEV-1 | 15 min | 1 hour | 24 hours | 24/7 |
| SEV-2 | 30 min | 4 hours | 72 hours | 24/7 |
| SEV-3 | 4 hours | 24 hours | 1 week | Business hours |
| SEV-4 | Next day | Best effort | 2 weeks | Business hours |

## 4. Post-Mortem Requirements

### 4.1 Timelines

- SEV-1: Within 3 business days.
- SEV-2: Within 5 business days.
- SEV-3/SEV-4: Not required.

### 4.2 Content

Post-mortems must include: timeline, root cause (5-Whys), impact assessment, remediation actions, preventive action items (min 3, with owner/priority/date), detection improvements.

### 4.3 Action Item Governance

- Jira (PDP-PM) within 2 business days.
- Weekly review in Thursday Security Standup.
- 14-day overdue escalation to CISO.

## 5. Communication

### 5.1 Customer Notification

- Data breach: Affected customers notified within 48 hours.
- Service disruption: Status page updated within 15 minutes.
- Sector-specific: HIPAA, PCI, financial regulatory notifications as applicable.

## 6. Evidence Preservation

- SEV-1/SEV-2: Full forensic artifacts (disk, memory, network, logs — 120-day lookback).
- Streaming data incidents: Kafka topic snapshots and consumer offset logs preserved.
- Chain of custody with SHA-256 hashes. 7-year retention.

## 7. Plan Testing and Maintenance

### 7.1 Testing Schedule

- The IRP is tested annually through a tabletop exercise facilitated by the CISO.
- The tabletop exercise must include representatives from Security, Engineering, SRE, Legal, and Customer Success.
- Exercise scenarios should cover at least one multi-sector incident (affecting customers in different regulated industries simultaneously).
- Results documented with improvement action items tracked in Jira.

### 7.2 Plan Updates

- IRP reviewed annually or after any SEV-1 incident.
- Updates approved by CISO and CEO.
- Version history maintained in Confluence.

### 7.3 Post-Major-Change Review

- After significant platform changes (new architecture components, new customer sectors, major infrastructure migrations), the CISO should evaluate whether an additional IRP review or test is warranted.
- This evaluation is advisory — no mandatory action is required.

---

**Approved by:** Rebecca Torres, CEO
**Approval Date:** February 25, 2025
**Next Review Date:** March 2026
