# Orion Cloud Services — Incident Response Plan Overview

**Document ID:** IRP-2025-v3.1
**Effective Date:** April 1, 2025
**Owner:** Security Operations Team
**Classification:** Internal

---

## 1. Purpose

This document provides an overview of Orion Cloud Services' Incident Response Plan (IRP). The full IRP is maintained as a controlled document in Confluence and is reviewed quarterly by the Security Operations team.

## 2. Incident Classification

Incidents are classified into four severity levels:

| Severity | Description | Response Time | Escalation |
|----------|-------------|---------------|------------|
| SEV-1 (Critical) | Data breach, service outage affecting all customers | 15 minutes | CISO + CEO immediately |
| SEV-2 (High) | Partial service degradation, suspected intrusion | 30 minutes | CISO within 1 hour |
| SEV-3 (Medium) | Isolated security event, single-customer impact | 2 hours | Security lead within 4 hours |
| SEV-4 (Low) | Minor policy violation, failed attack attempt | 24 hours | Weekly security review |

## 3. Response Team

- **Incident Commander:** Rotating on-call SRE engineer
- **Security Lead:** Erik Lindberg, Head of Security
- **Communications Lead:** Marketing team for external communications
- **Legal Counsel:** External counsel (Baker McKenzie) for breach notification

## 4. Notification Requirements

- **Internal:** All SEV-1 and SEV-2 incidents reported to leadership within 1 hour
- **Regulatory:** GDPR breach notification to supervisory authority within 72 hours (if applicable)
- **Customer:** Affected customers notified within 48 hours of confirmed data breach
- **Data Subjects:** Individual notification without undue delay if high risk to rights and freedoms

## 5. Post-Incident Review

All SEV-1 and SEV-2 incidents require a post-incident review within 5 business days. Root cause analysis and remediation actions are tracked in Jira.

## 6. Testing

The incident response plan is tested annually through tabletop exercises. The last tabletop exercise was conducted on September 15, 2025.
