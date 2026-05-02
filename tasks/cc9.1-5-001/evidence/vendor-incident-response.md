# Onyx Data — Vendor Security Incident Report: PrestoServe Analytics

**Incident ID:** OD-VINC-2025-003  
**Vendor:** PrestoServe Analytics (OD-V-016)  
**Vendor Tier:** Critical  
**Report Date:** December 15, 2025  
**Author:** Angela Torres, VP GRC  
**Classification:** Confidential — Restricted Distribution

---

## 1. Incident Timeline

| Date/Time (UTC) | Event |
|-----------------|-------|
| November 8, 2025 14:22 | PrestoServe Security Operations Center (SOC) detects anomalous database query patterns on their multi-tenant analytics cluster |
| November 8, 2025 15:10 | PrestoServe confirms unauthorized access to analytics processing infrastructure via compromised service account credential |
| November 8, 2025 16:45 | PrestoServe initiates incident response; compromised credential revoked; affected systems isolated |
| November 8, 2025 18:30 | **PrestoServe notifies Onyx Data** via the designated security contact (security-incidents@onyxdata.com). Notification received 4 hours and 8 minutes after initial detection — **within 72-hour contractual requirement** |
| November 8, 2025 19:00 | Onyx Data CISO (James Whitfield) briefed. GRC team logs incident in Vendor Incident Tracker |
| November 9, 2025 08:00 | Onyx Data/PrestoServe joint call. PrestoServe provides initial scope assessment: attacker accessed the shared analytics processing layer. Customer data tenant isolation is being validated |
| November 9, 2025 14:00 | PrestoServe confirms the compromised service account had read access to the multi-tenant query processing engine. The attacker executed approximately 340 queries over a 6-hour window before detection |
| November 10, 2025 10:00 | **PrestoServe engages Mandiant** for forensic investigation. Estimated completion: 2-3 weeks |
| November 10, 2025 16:00 | Onyx Data internal impact assessment meeting. James Whitfield (CISO), Angela Torres (VP GRC), Michael Zhang (CEO), David Reeves (General Counsel) |
| November 10, 2025 — November 28, 2025 | **Uncertainty period:** PrestoServe cannot confirm or deny whether Onyx Data customer data was accessed. Forensic analysis of query logs is ongoing. PrestoServe states: "Due to the volume of queries and the multi-tenant architecture, we are unable to definitively determine which tenant data was accessed until the forensic analysis is complete." |
| November 15, 2025 | PrestoServe provides interim update: 340 queries executed, approximately 60% appear to be system/metadata queries, 40% targeted tenant data tables. Tenant-level attribution requires further analysis |
| November 22, 2025 | PrestoServe provides weekly update: forensic analysis narrowing scope. 12 of their 47 tenants have been cleared. Onyx Data is not yet among the cleared tenants |
| November 28, 2025 16:00 | **PrestoServe/Mandiant deliver final forensic report.** Conclusion: Onyx Data tenant data was **not accessed**. The 340 queries targeted 3 other tenants' data. Onyx Data's data partition was not queried. Confidence level: High (based on comprehensive query log analysis and database audit logs) |
| December 1, 2025 | Onyx Data receives formal written confirmation from PrestoServe CEO and Mandiant |
| December 5, 2025 | Onyx Data closes vendor incident. Post-incident review scheduled for January 2026 |

## 2. Impact Assessment

### 2.1 Data Impact
- **Confirmed Onyx Data customer data compromise:** None
- **Data types potentially at risk during uncertainty period:** Customer behavioral analytics data (page views, feature usage, session data), customer identifiers (user IDs, email addresses), organization names
- **Volume potentially at risk:** Approximately 2.3 million customer records stored in PrestoServe analytics platform

### 2.2 Operational Impact
- No disruption to Onyx Data services
- PrestoServe analytics platform was offline for 4 hours during incident containment (November 8, 16:45 — 20:45 UTC). Analytics features were degraded but non-critical.
- Analytics data pipeline was fully restored by November 9, 08:00 UTC

### 2.3 Vendor Control Assessment
- **Detection:** PrestoServe SOC detected anomalous queries within 48 minutes of first malicious query execution — demonstrates effective monitoring
- **Containment:** Compromised credential revoked and systems isolated within 2 hours and 23 minutes of detection — demonstrates effective incident response
- **Notification:** Onyx Data notified within 4 hours and 8 minutes of initial detection — within 72-hour contractual SLA
- **Root Cause:** Compromised service account credential. The credential was a long-lived API key (not rotated since March 2025) used by PrestoServe's internal data pipeline. The key was exposed in a PrestoServe developer's personal GitHub repository (public repo, accidental commit on October 29, 2025). The key was discovered and used by the attacker approximately 10 days later.

## 3. Customer Communication Decision

### 3.1 Decision During Uncertainty Period (November 10-28)

During the meeting on November 10, the following decision was made:

**Decision: Do not notify customers during the uncertainty period.**

**Rationale documented by David Reeves (General Counsel):**
- No confirmed data compromise
- Notification of unconfirmed potential exposure could cause unnecessary alarm
- PrestoServe forensic investigation expected to conclude within 3 weeks
- Onyx Data's contractual obligations to customers require notification within 72 hours of "confirmed" data breach, not potential exposure
- Regulatory requirements (state breach notification laws) triggered only upon confirmed unauthorized access to PII
- If forensic analysis confirms Onyx Data data was accessed, notification timeline begins at confirmation

**Dissent noted:** Angela Torres (VP GRC) recommended proactive customer notification, noting that 3 weeks of uncertainty with 2.3 million records potentially at risk represents a material concern. Torres recommended a general advisory to customers about a vendor security event without confirming data compromise. The committee voted 3-1 to defer notification pending forensic results.

### 3.2 Post-Confirmation Communication

Following Mandiant's confirmation that Onyx Data customer data was not accessed:
- No customer notification sent (no data compromise confirmed)
- Incident logged for inclusion in annual SOC 2 management assertion
- Board briefed on December 8, 2025

## 4. Remediation and Follow-Up

### 4.1 PrestoServe Remediation Actions
1. All long-lived API keys rotated (completed November 9)
2. Mandatory credential scanning on all developer repositories (implemented November 15)
3. Service account credentials migrated to short-lived tokens with 24-hour rotation (target: January 2026)
4. Enhanced tenant isolation — dedicated query execution contexts per tenant (target: February 2026)

### 4.2 Onyx Data Actions
| # | Action | Owner | Status | Due Date |
|---|--------|-------|--------|----------|
| 1 | Review PrestoServe contract for additional security requirements | David Reeves | In Progress | January 15, 2026 |
| 2 | Evaluate alternative analytics vendors | Angela Torres | Not Started | February 28, 2026 |
| 3 | Conduct post-incident review with PrestoServe | Angela Torres | Scheduled | January 10, 2026 |
| 4 | Review Onyx Data's customer notification thresholds policy | David Reeves | Not Started | January 31, 2026 |
| 5 | Request PrestoServe SOC 2 bridge letter covering incident period | Angela Torres | In Progress | January 15, 2026 |

---

*Report reviewed by: James Whitfield, CISO — December 15, 2025*  
*Distribution: Executive Leadership Team, Board of Directors (summary)*
