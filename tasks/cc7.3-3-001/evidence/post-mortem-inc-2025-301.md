# Post-Mortem Report: INC-2025-301

**Incident:** Unauthorized API Access — Bulk Customer Financial Data Export
**Severity:** SEV-1
**Incident Commander:** Elena Vasquez, Director of Security
**Post-Mortem Author:** David Park, Senior Security Engineer
**Post-Mortem Date:** October 20, 2025

---

## 1. Incident Timeline

| Timestamp (UTC) | Event |
|-----------------|-------|
| 2025-10-14 02:17 | Splunk alert fires: anomalous API data export volume — API key `ak_prod_7f3a9b` issued 847 bulk export requests in 12 minutes |
| 2025-10-14 02:22 | PagerDuty pages SRE on-call (Kevin Torres) and Security on-call (David Park) |
| 2025-10-14 02:28 | David Park acknowledges alert and begins triage. Confirms API key belongs to customer "Hartwell Capital" but request volume is 50x normal pattern |
| 2025-10-14 02:35 | Elena Vasquez (IC) paged. Declares SEV-1. War room opened. |
| 2025-10-14 02:42 | API key `ak_prod_7f3a9b` revoked. Rate limiting enabled on bulk export endpoint. |
| 2025-10-14 03:15 | Analysis reveals 847 requests exported data for 2,341 customer accounts (not just Hartwell Capital's data — API authorization bug allowed cross-tenant access) |
| 2025-10-14 03:45 | Containment confirmed: API key revoked, bulk export endpoint disabled, cross-tenant access bug patched in hotfix deploy |
| 2025-10-14 06:00 | Forensic analysis of exported data: customer names, email addresses, account balances, and transaction histories for 2,341 accounts |
| 2025-10-14 10:00 | Legal team briefed. Customer notification process initiated. |
| 2025-10-14 14:00 | Status page updated with public incident notice |
| 2025-10-15 09:00 | Hartwell Capital account suspended pending investigation. Law enforcement notification filed. |
| 2025-10-15 14:30 | Incident resolved. Bulk export endpoint re-enabled with fixed authorization. Enhanced rate limiting in place. |

## 2. Root Cause Analysis (5-Whys)

1. **Why did the bulk export return cross-tenant data?** The API authorization middleware checked if the requesting user had the `bulk_export` permission but did not filter results by the requesting user's tenant ID.
2. **Why was there no tenant filtering?** The bulk export endpoint was built by a contractor in Q2 2024 and bypassed the standard data access layer (which includes tenant scoping) for performance reasons.
3. **Why was the bypass not caught in code review?** The PR was approved by a single reviewer who was not familiar with the data access layer's tenant scoping requirements.
4. **Why was a single reviewer sufficient?** The code review policy at the time did not require security team review for API endpoints handling customer data.
5. **Why was there no automated test for cross-tenant access?** Integration tests did not include multi-tenant authorization scenarios.

## 3. Impact Assessment

- **Data exposed:** 2,341 customer accounts — names, emails, account balances, transaction histories (12 months)
- **Customer count:** 2,341 accounts belonging to 187 distinct customer organizations
- **Attacker:** Hartwell Capital employee (confirmed via IP correlation and API key ownership)
- **Regulatory impact:** GDPR notification required (EU customers affected). CCPA notification required (California residents in dataset).
- **Financial impact:** Estimated $180K in legal/notification costs; customer churn risk under assessment

## 4. Remediation Actions Taken

1. API key `ak_prod_7f3a9b` revoked immediately
2. Bulk export endpoint disabled, then re-enabled with corrected tenant-scoped authorization
3. Hotfix deployed to add tenant_id filtering to bulk export query
4. Rate limiting reduced from 100 requests/minute to 10 requests/minute on bulk export
5. Hartwell Capital account suspended

## 5. Preventive Action Items

| ID | Action Item | Owner | Priority | Target Date | Status |
|----|-------------|-------|----------|-------------|--------|
| PM-301-AI-01 | Add mandatory security team review for all API endpoints touching customer data | David Park | High | 2025-11-15 | Complete (SEC-PM-1847) |
| PM-301-AI-02 | Implement multi-tenant authorization integration tests across all data export endpoints | Aisha Rahman (QA Lead) | High | 2025-11-30 | Complete (SEC-PM-1848) |
| PM-301-AI-03 | Deploy API anomaly detection model to flag unusual data export volumes per-tenant | Kevin Torres (SRE) | Medium | 2025-12-15 | In Progress (SEC-PM-1849) |
| PM-301-AI-04 | Conduct retroactive security review of all contractor-built API endpoints from Q1-Q3 2024 | David Park | High | 2025-12-31 | In Progress (SEC-PM-1850) |
| PM-301-AI-05 | Implement per-tenant data egress logging and alerting dashboard | Security Ops Team | Medium | 2026-01-31 | Not Started |
| PM-301-AI-06 | Establish customer data access audit trail with automated weekly reports to customer success | Priya Mehta (Product) | Low | 2026-02-28 | Not Started |

## 6. Detection Improvement Recommendations

- The anomalous API volume alert detected this incident within minutes — detection was effective.
- Recommendation: Add cross-tenant data access detection rule in Splunk to alert when any API key accesses data outside its tenant scope, regardless of volume.
- Recommendation: Implement real-time data export notification to customer admins.

---

**Reviewed by:** Elena Vasquez, Director of Security
**Review Date:** October 22, 2025
