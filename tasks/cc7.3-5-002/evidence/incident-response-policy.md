# Incident Response Policy

**Document ID:** IRP-POL-2025-009
**Version:** 3.5
**Effective Date:** January 15, 2025
**Owner:** Security Operations, Helix Collaboration
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy defines the incident response procedures for Helix Collaboration, a provider of enterprise collaboration and document management SaaS to Fortune 500 companies.

## 2. Severity Classification

| Severity | Name | Definition |
|----------|------|-----------|
| SEV-1 | Critical | Confirmed data breach, ransomware, complete platform unavailability |
| SEV-2 | High | Unauthorized access, suspected data exposure, >20% customer impact |
| SEV-3 | Medium | Suspicious activity, minor degradation, failed attacks |
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

- SEV-1: Post-mortem due within 3 business days of resolution.
- SEV-2: Post-mortem due within 5 business days of resolution.
- SEV-3/SEV-4: Not required.

### 4.2 Quality Standards

Every SEV-1 and SEV-2 post-mortem must include:

1. **Complete incident timeline** — Detection, triage, escalation, containment, eradication, and recovery with UTC timestamps. Gaps in the timeline must be explained.
2. **Root cause analysis** — Using 5-Whys methodology. Each "why" must be specific and evidence-based, not speculative.
3. **Impact assessment** — Quantified where possible: number of systems affected, customer accounts impacted, data records exposed, service downtime duration.
4. **Remediation actions taken** — What was done during the incident to contain and resolve it.
5. **Preventive action items** — Minimum of 3 action items. Each must have: assigned owner (named individual), priority (Critical/High/Medium/Low), target completion date, and Jira ticket reference.
6. **Detection improvement recommendations** — How detection of this incident type could be improved.

### 4.3 Post-Mortem Review

- All SEV-1 post-mortems reviewed by CISO within 2 business days of submission.
- SEV-2 post-mortems reviewed by Security Operations Manager.
- Reviewer must sign off or return with revision requests.
- Reviewer sign-off recorded in the post-mortem document.

### 4.4 Action Item Governance

- Entered in Jira (HLX-PM) within 2 business days.
- Reviewed weekly in Monday Security Standup.
- 14-day overdue escalation to CISO.
- 30-day overdue escalation to CTO.

## 5. Communication

### 5.1 Customer Notification

- Data breach: Affected enterprise customers notified within 48 hours via secure portal and direct contact with customer CISO.
- Service disruption: Status page (status.helix-collab.com) updated within 15 minutes.

### 5.2 Regulatory

- GDPR: DPO notifies supervisory authority within 72 hours.
- Contractual: Customer-specific SLAs reviewed and notifications coordinated.

## 6. Evidence Preservation

- SEV-1/SEV-2: Full forensic image set, logs (120-day lookback).
- Chain of custody with SHA-256 hashes. 7-year retention.

## 7. Plan Testing

- Semi-annual tabletop exercises (February and August).
- Annual red team engagement.

---

**Approved by:** Diana Nakamura, CTO
**Approval Date:** January 10, 2025
**Next Review Date:** January 2026
