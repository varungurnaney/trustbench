# Security Steering Committee — Meeting Minutes

**Organization:** Atherton SaaS Inc.

---

## Q3 2025 Meeting — July 23, 2025

**Meeting ID:** SSC-2025-Q3
**Date:** July 23, 2025
**Time:** 2:00 PM - 3:30 PM EST
**Location:** Conference Room A / Zoom
**Chair:** Nathan Cross, CISO

### Attendees

| Name | Title | Present |
|------|-------|---------|
| Emily Zhang | CEO | Yes |
| Nathan Cross | CISO | Yes |
| Mark Sullivan | VP IT Operations | Yes |
| Priya Dasgupta | GRC Manager | Yes |
| Sarah Kim | CHRO | No (on leave) |

### Quorum

4 of 5 members present. Quorum met.

### Agenda

1. Q2 2025 Security Metrics Review
2. SOC 2 Type II Audit Status Update
3. Vendor Risk Assessment Results
4. Budget Review — H1 Actuals vs Plan

### Discussion

#### 1. Q2 Security Metrics Review

Nathan presented the Q2 security metrics report. Key highlights discussed:

- **MTTD:** Q2 average was 3.6 hours, within the 4-hour target. Committee noted the improvement from Q1 (4.2 hours). Nathan credited the new SIEM correlation rules.
- **MTTR:** Q2 average was 5.8 hours, well within the 8-hour target. No concerns raised.

Committee acknowledged the metrics were on track. No further discussion on the remaining metrics (vulnerability remediation, training completion, policy exceptions).

**Decision:** Metrics accepted. No action required.

#### 2. SOC 2 Type II Audit Status

Nathan provided an update on SOC 2 readiness:

- External auditor (Baker Tilly) confirmed for October start date
- Evidence collection 70% complete
- Two open remediation items: shared service accounts and logging gaps in staging
- Expected completion: December 2025

**Decision:** Approved timeline. Nathan to resolve open items by September 30.

#### 3. Vendor Risk Assessment Results

Priya presented vendor risk assessment results for the 8 critical vendors:

- 6 vendors rated Satisfactory
- 1 vendor (DataFlow Analytics) rated Needs Improvement — missing SOC 2 report
- 1 vendor (CloudSync) rated High Risk — security incident in May 2025

**Decision:** Approved remediation plan for CloudSync. Priya to obtain SOC 2 report from DataFlow Analytics by August 31.

#### 4. Budget Review

Nathan presented H1 budget actuals:

- Security budget: $2.1M allocated for 2025
- H1 spending: $980K (46.7% of annual budget)
- On track for full-year spend

**Decision:** No budget adjustments needed.

### Action Items

| ID | Action | Owner | Due Date |
|----|--------|-------|----------|
| AI-Q3-001 | Resolve SOC 2 remediation items | Nathan Cross | 2025-09-30 |
| AI-Q3-002 | Obtain DataFlow Analytics SOC 2 report | Priya Dasgupta | 2025-08-31 |
| AI-Q3-003 | Complete CloudSync remediation plan | Priya Dasgupta | 2025-09-15 |

### Next Meeting

October 22, 2025

---

## Q2 2025 Meeting — April 16, 2025

**Meeting ID:** SSC-2025-Q2
**Date:** April 16, 2025
**Time:** 2:00 PM - 3:30 PM EST
**Location:** Conference Room A / Zoom
**Chair:** Nathan Cross, CISO

### Attendees

| Name | Title | Present |
|------|-------|---------|
| Emily Zhang | CEO | Yes |
| Nathan Cross | CISO | Yes |
| Mark Sullivan | VP IT Operations | Yes |
| Priya Dasgupta | GRC Manager | Yes |
| Sarah Kim | CHRO | Yes |

### Quorum

5 of 5 members present. Quorum met.

### Agenda

1. Q1 2025 Security Metrics Review
2. Annual Policy Review Status
3. Security Awareness Program Update
4. 2025 Penetration Test Planning

### Discussion

#### 1. Q1 Security Metrics Review

Nathan presented the Q1 metrics:

- **MTTD:** 4.2 hours — slightly above the 4-hour target. Nathan explained the spike was due to a logging gap during AWS migration in February.
- **MTTR:** 6.1 hours — within target.

Committee discussed detection performance. Emily asked about plans to improve MTTD. Nathan outlined the SIEM enhancement project planned for Q2.

No discussion of vulnerability remediation rates, training completion, or policy exceptions.

**Decision:** Metrics acknowledged. Nathan to provide SIEM improvement update at Q3 meeting.

#### 2. Annual Policy Review Status

Nathan reported that the annual policy review cycle was underway:

- 4 of 12 policies reviewed and updated (Access Control, Encryption, Acceptable Use, Code of Conduct)
- 8 policies pending review, including the Information Security Policy (Tier 1)
- Target: all reviews complete by end of Q2

**Decision:** Approved review timeline. Nathan to prioritize Tier 1 policy review.

#### 3. Security Awareness Training

Sarah presented training completion rates:

- Q1 overall: 92.3% completion
- New hire onboarding: 100%
- Phishing simulation click rate: 8.2% (target < 10%)

**Decision:** Training program on track. Continue monthly phishing simulations.

#### 4. Penetration Test Planning

Nathan outlined the 2025 penetration test scope:

- External pentest: May 2025 (NovaSec Consulting)
- Internal pentest: August 2025 (NovaSec Consulting)
- Scope includes production web applications, APIs, and cloud infrastructure

**Decision:** Approved scope and timeline.

### Action Items

| ID | Action | Owner | Due Date |
|----|--------|-------|----------|
| AI-Q2-001 | Complete SIEM correlation rules upgrade | Nathan Cross | 2025-06-30 |
| AI-Q2-002 | Complete Tier 1 policy review | Nathan Cross | 2025-06-30 |
| AI-Q2-003 | Schedule external penetration test | Nathan Cross | 2025-05-15 |

### Next Meeting

July 23, 2025

---

**Minutes prepared by:** Lisa Chen, Executive Assistant to CISO
