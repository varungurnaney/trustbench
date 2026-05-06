# Incident Response Policy

**Document ID:** SEC-POL-IRP-005
**Version:** 3.1
**Effective Date:** February 1, 2025
**Owner:** Security Operations, Meridian Analytics
**Classification:** Confidential

---

## 1. Purpose

This policy establishes the incident response requirements for Meridian Analytics to ensure timely and effective handling of security incidents affecting the company's financial analytics SaaS platform.

## 2. Severity Definitions

| Severity | Name | Definition |
|----------|------|-----------|
| SEV-1 | Critical | Confirmed data breach, ransomware, or complete platform unavailability |
| SEV-2 | High | Unauthorized system access, partial outage (>20% customer impact), credential compromise |
| SEV-3 | Medium | Suspicious activity, failed intrusion attempts, minor service degradation |
| SEV-4 | Low | Policy violations, blocked threats, informational security events |

## 3. Response SLAs

### 3.1 Initial Triage

| Severity | Triage SLA | Coverage |
|----------|-----------|----------|
| SEV-1 | 15 minutes | 24/7/365 |
| SEV-2 | 30 minutes | 24/7/365 |
| SEV-3 | 4 hours | Business hours (M-F 8AM-6PM PT) |
| SEV-4 | Next business day | Business hours |

### 3.2 Containment SLAs

| Severity | Containment SLA |
|----------|----------------|
| SEV-1 | 1 hour from triage |
| SEV-2 | 4 hours from triage |
| SEV-3 | 24 hours from triage |
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

- SEV-1: Post-mortem due within 3 business days of incident resolution.
- SEV-2: Post-mortem due within 5 business days of incident resolution.
- SEV-3: Post-mortem at Incident Commander discretion.
- SEV-4: Not required.

### 4.2 Required Contents

Every post-mortem (SEV-1 and SEV-2) must include:

1. **Incident timeline** with timestamps (detection, triage, containment, eradication, recovery)
2. **Root cause analysis** using 5-Whys methodology
3. **Impact assessment** (systems affected, data exposure scope, customer count, financial impact)
4. **Remediation actions taken** during the incident
5. **Preventive action items** — each with an assigned owner, priority, and target completion date
6. **Detection improvement recommendations** — how to detect this type of incident faster in the future

### 4.3 Action Item Tracking

- All action items from post-mortems must be created as Jira tickets in the SEC-PM project within 2 business days of post-mortem completion.
- Each action item ticket must reference the originating incident ID.
- Action items are reviewed in the weekly Security Operations standup every Tuesday.
- Items overdue by more than 14 calendar days are escalated to the CISO.

## 5. Customer Notification

### 5.1 Notification Requirements

- SEV-1 (data breach): Affected customers notified within 72 hours of breach confirmation.
- SEV-2 (service impact): Status page updated within 1 hour of incident declaration.
- Regulatory notifications handled per applicable requirements (GDPR, CCPA, contractual).

### 5.2 Notification Records

All customer and regulatory notifications must be logged in the incident ticket with: notification method, recipient list, timestamp, and content summary.

## 6. Incident Tracking

### 6.1 Incident Register

All confirmed incidents are logged in the Incident Register (Jira project: SEC-INC) with:
- Incident ID (INC-YYYY-NNN format)
- Detection timestamp
- Triage timestamp
- Containment timestamp
- Resolution timestamp
- Severity level
- Brief description
- Post-mortem status and link
- Action items count and completion status

---

**Approved by:** Christine Park, CEO
**Approval Date:** January 28, 2025
**Next Review Date:** February 2026
