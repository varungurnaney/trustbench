# Incident Response Policy

**Document ID:** SEC-IRP-2025-002
**Version:** 3.4
**Effective Date:** March 1, 2025
**Owner:** Information Security, Beacon Health Technologies
**Classification:** Confidential — HIPAA Covered

---

## 1. Purpose

This policy governs how Beacon Health Technologies detects, responds to, contains, and recovers from security incidents affecting the company's healthcare analytics platform and protected health information (PHI).

## 2. Regulatory Context

As a HIPAA Business Associate, Beacon is required to report breaches of unsecured PHI to covered entity customers within 60 days of discovery. This IRP integrates HIPAA Breach Notification Rule requirements alongside SOC 2 CC7.3 controls.

## 3. Severity Classification

| Severity | Name | Definition |
|----------|------|-----------|
| SEV-1 | Critical | Confirmed PHI breach, ransomware, complete platform outage |
| SEV-2 | High | Unauthorized system access, suspected PHI exposure, partial outage (>15% customers) |
| SEV-3 | Medium | Suspicious activity, failed intrusion, minor service degradation |
| SEV-4 | Low | Policy violations, blocked attacks, informational |

## 4. Response SLAs

### 4.1 Triage

| Severity | Triage SLA | Coverage |
|----------|-----------|----------|
| SEV-1 | 10 minutes | 24/7/365 |
| SEV-2 | 20 minutes | 24/7/365 |
| SEV-3 | 2 hours | Business hours (M-F 8AM-5PM CT) |
| SEV-4 | Next business day | Business hours |

### 4.2 Containment

| Severity | Containment SLA |
|----------|----------------|
| SEV-1 | 30 minutes |
| SEV-2 | 2 hours |
| SEV-3 | 12 hours |
| SEV-4 | Best effort |

### 4.3 Resolution

| Severity | Resolution Target |
|----------|------------------|
| SEV-1 | 12 hours |
| SEV-2 | 48 hours |
| SEV-3 | 5 business days |
| SEV-4 | 10 business days |

## 5. Post-Mortem Requirements

### 5.1 Applicability

- SEV-1: Mandatory post-mortem within 3 business days of resolution.
- SEV-2: Mandatory post-mortem within 5 business days of resolution.
- SEV-3/SEV-4: Post-mortem not required unless the incident was initially classified at a higher severity and later downgraded.
- **False positives:** Incidents that are investigated and determined to be false positives (no actual security event occurred) do not require post-mortems. The incident ticket should be updated with the false positive determination and closed.

### 5.2 Required Content

Post-mortems must include:
1. Timeline with UTC timestamps
2. Root cause analysis (5-Whys)
3. Impact assessment including PHI exposure determination
4. HIPAA breach risk assessment (if PHI potentially involved)
5. Preventive action items with owners and deadlines
6. Detection improvement recommendations

### 5.3 Action Items

- Entered in Jira (BHT-PM project) within 2 business days.
- Reviewed weekly in Security Operations standup.
- Overdue items (>14 days) escalated to CISO.

## 6. Communication

### 6.1 Internal

- SEV-1: War room bridge + Slack updates every 10 minutes.
- SEV-2: Slack updates every 30 minutes.

### 6.2 External — Customers

- PHI breach: Covered entity customers notified within 48 hours of breach confirmation.
- Service disruption: Status page updated within 20 minutes of declaration.

### 6.3 Regulatory

- HIPAA: Breach notification to HHS within 60 days of discovery.
- State laws: Legal team coordinates state-specific notifications.

## 7. Evidence Preservation

- SEV-1/SEV-2: Disk images, memory dumps, logs (180-day lookback for PHI incidents).
- SHA-256 hash and chain of custody for all evidence.
- 7-year retention per HIPAA requirements.

## 8. Plan Testing

- Quarterly tabletop exercises (HIPAA requirement).
- Annual simulated incident exercise with external firm.
- Results documented with corrective actions tracked in Jira.

---

**Approved by:** Dr. Sandra Kim, CEO
**Approval Date:** February 25, 2025
**Next Review Date:** March 2026
