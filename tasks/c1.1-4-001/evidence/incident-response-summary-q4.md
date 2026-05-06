# Incident Response Summary — Q4 2025

**Document ID:** RPT-IR-Q4-2025
**Prepared by:** Security Operations Center
**Date:** January 5, 2026
**Classification:** Internal

---

## Executive Summary

During Q4 2025, the Bridgeport Financial Technologies SOC processed 247 security alerts, resulting in 12 confirmed incidents. No data breaches or customer data exposures occurred during the period. All incidents were resolved within SLA.

## Incident Statistics

| Severity | Count | Avg Resolution Time | SLA Target | SLA Met |
|----------|-------|-------------------|------------|---------|
| P1 - Critical | 0 | N/A | 4 hours | N/A |
| P2 - High | 2 | 3.5 hours | 8 hours | Yes |
| P3 - Medium | 4 | 18 hours | 48 hours | Yes |
| P4 - Low | 6 | 3.2 days | 5 business days | Yes |

## Notable Incidents

### INC-2025-089 (P2) — Unauthorized SSH Key Added to Staging Server
- **Date:** October 18, 2025
- **Description:** Unauthorized SSH key detected on staging-api-01 during routine configuration audit.
- **Root Cause:** Former contractor's deployment script added a personal SSH key during an automated deployment.
- **Resolution:** Key removed, contractor access fully revoked, deployment scripts audited.
- **Remediation:** Implemented automated SSH key inventory scanning via CrowdStrike.

### INC-2025-102 (P2) — DLP Alert: Bulk Customer List Emailed Externally
- **Date:** November 12, 2025
- **Description:** DLP rule DLP-EMAIL-003 triggered when sales team member attempted to email a CSV with 2,400 customer email addresses to a personal Gmail account.
- **Root Cause:** Employee intended to work from home and was unaware of the DLP policy.
- **Resolution:** Email blocked by DLP. Employee counseled. No data left the organization.
- **Remediation:** Enhanced security awareness training for sales team.

### INC-2025-115 (P3) — Expired Internal Certificate Caused Jenkins Outage
- **Date:** December 3, 2025
- **Description:** Jenkins CI server certificate (CERT-INT-010) expired, causing a 4-hour CI/CD pipeline outage.
- **Root Cause:** Internal certificate had no auto-renewal and monitoring alert was misconfigured.
- **Resolution:** Certificate manually renewed. Monitoring alert corrected.
- **Remediation:** Added all internal certificates to Cert-Manager automated renewal pipeline.

## Trends

- Alert volume decreased 8% from Q3 (268 alerts)
- False positive rate: 31% (target: <25%) — improvement actions planned for Q1 2026
- Mean time to detect: 12 minutes (target: <15 minutes)
- No repeat incidents from previous quarters

---

**Reviewed by:** Daniel Park, CISO
