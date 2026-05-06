# Vendor Risk Assessment Summary — Q4 2025

**Prepared by:** Compliance Team, Vantage Cloud Systems
**Date:** January 5, 2026
**Classification:** Internal

---

## 1. Overview

This report summarizes the vendor risk assessment activities conducted during Q4 2025 (October 1 - December 31, 2025) for Vantage Cloud Systems' critical third-party service providers.

## 2. Vendor Assessment Status

| Vendor | Service | Risk Tier | Assessment Status | Last Assessment | Next Due |
|--------|---------|-----------|-------------------|-----------------|----------|
| AWS | Cloud Infrastructure | Critical | Complete | 2025-10-15 | 2026-04-15 |
| CrowdStrike | EDR/Endpoint Security | Critical | Complete | 2025-11-01 | 2026-05-01 |
| Splunk | SIEM/Log Management | Critical | Complete | 2025-10-20 | 2026-04-20 |
| Okta | Identity Provider | Critical | Complete | 2025-09-15 | 2026-03-15 |
| GitHub | Source Code Management | High | Complete | 2025-11-10 | 2026-05-10 |
| Datadog | Application Monitoring | High | Complete | 2025-10-25 | 2026-04-25 |
| PagerDuty | Incident Alerting | High | Complete | 2025-12-01 | 2026-06-01 |
| Twilio | Customer Notifications | Medium | Complete | 2025-11-15 | 2026-11-15 |
| DocuSign | Contract Management | Low | Complete | 2025-12-10 | 2026-12-10 |

## 3. Key Findings

### 3.1 AWS
- SOC 2 Type II report reviewed (period ending June 2025). No qualified opinions.
- Bridge letter obtained covering July-September 2025.
- Complementary user entity controls (CUECs) mapped to Vantage internal controls.

### 3.2 CrowdStrike
- SOC 2 Type II report reviewed. No exceptions noted.
- Falcon agent version compliance verified: 98.5% of endpoints running latest stable version.

### 3.3 Splunk
- SOC 2 Type II report reviewed. One observation noted regarding log retention configuration defaults. Mitigated by Vantage custom retention policy (90 days hot, 365 days archive).

### 3.4 GitHub
- SOC 2 Type II report reviewed. No qualified opinions.
- Note: Vantage identified a GitHub PAT exposure incident in November (INC-2025-404). This is a Vantage-side issue, not a GitHub platform vulnerability.

## 4. Remediation Tracking

All vendor-related findings are tracked in the Compliance Findings Register. No open critical findings as of Q4 2025.

## 5. Next Steps

- Q1 2026: Okta assessment due (March 2026).
- Annual vendor risk re-tiering scheduled for February 2026.

---

**Reviewed by:** Diane Marsh, Head of Compliance
**Date:** January 8, 2026
