# Incident Response Policy

**Document ID:** IRP-2025-007
**Version:** 4.0
**Effective Date:** February 1, 2025
**Owner:** Security Operations, Clearpoint Financial Software
**Classification:** Confidential

---

## 1. Purpose

This policy defines the incident response requirements for Clearpoint Financial Software, a provider of portfolio management and trading analytics to institutional investors. Given the sensitive nature of financial data processed, this policy incorporates requirements from SOC 2, SEC regulation, and customer contractual obligations.

## 2. Severity Classification

| Severity | Name | Definition |
|----------|------|-----------|
| SEV-1 | Critical | Confirmed breach of customer financial data, ransomware, complete platform outage |
| SEV-2 | High | Unauthorized access to production, suspected data exposure, partial outage (>15% impact) |
| SEV-3 | Medium | Suspicious activity, minor degradation, failed attacks |
| SEV-4 | Low | Policy violations, blocked threats |

## 3. Response SLAs

| Severity | Triage | Containment | Resolution | Coverage |
|----------|--------|-------------|------------|----------|
| SEV-1 | 10 min | 30 min | 12 hours | 24/7 |
| SEV-2 | 20 min | 2 hours | 48 hours | 24/7 |
| SEV-3 | 4 hours | 24 hours | 5 days | Business hours |
| SEV-4 | Next day | Best effort | 10 days | Business hours |

## 4. Customer Notification

### 4.1 Notification Requirements

- **Confirmed data breach (SEV-1):** Affected customers notified within 48 hours of breach confirmation. Notification must include: nature of the breach, data types affected, containment actions taken, and remediation steps.
- **Suspected data exposure (SEV-2):** If investigation confirms data was accessed but exposure is uncertain, customers must be notified within 72 hours with a preliminary assessment.
- **Service disruption (SEV-1/SEV-2):** Status page updated within 15 minutes. Customer account managers contacted within 1 hour for affected accounts.

### 4.2 Notification Decision Authority

- The decision to notify customers is made by the Incident Commander in consultation with the Head of Legal.
- For incidents where breach confirmation is uncertain, the Incident Commander may defer notification for up to 72 hours to allow investigation to determine scope and impact.
- After 72 hours of investigation, a notification decision must be made regardless of investigation completion status.

### 4.3 Notification Records

All notifications logged in incident ticket: method, recipient list, timestamp, content, and acknowledgment status.

## 5. Post-Mortem Requirements

### 5.1 Timelines and Content

- SEV-1: Post-mortem within 3 business days. Must include: timeline, root cause (5-Whys), impact assessment, customer impact determination, remediation actions, preventive action items, detection improvements.
- SEV-2: Post-mortem within 5 business days. Same content requirements.
- SEV-3/SEV-4: Not required.

### 5.2 Action Item Governance

- Entered in Jira (CPF-PM) within 2 business days of post-mortem.
- Weekly review in Security Operations standup.
- 14-day escalation to CISO. 30-day escalation to CEO.

## 6. Evidence Preservation

- SEV-1/SEV-2: Full forensic artifacts (disk images, memory dumps, network captures, logs with 180-day lookback).
- Financial data incidents: Additional preservation of trade logs, order books, and position snapshots.
- Chain of custody with SHA-256 hashes. 7-year retention.

## 7. Plan Testing

- Quarterly tabletop exercises.
- Annual red team engagement.
- At least one financial-data-specific scenario per year.

---

**Approved by:** Victoria Chen, CEO
**Approval Date:** January 29, 2025
**Next Review Date:** February 2026
