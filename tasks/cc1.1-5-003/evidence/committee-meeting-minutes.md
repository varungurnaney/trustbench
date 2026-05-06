# Security & Risk Governance Committee — 2025 Meeting Minutes

**Organization:** Wavecrest Financial Services

---

## Q1 Meeting — March 12, 2025

**Meeting ID:** SRGC-2025-Q1
**Date:** March 12, 2025 | 10:00 AM - 12:00 PM EST
**Location:** Board Room / Zoom
**Chair:** Eleanor Walsh (Independent Board Member)

### Attendance

| Member | Present | Voting |
|--------|---------|--------|
| Eleanor Walsh — Board Member | Yes | Yes |
| James Chen — CEO | Yes | Yes |
| Victoria Santos — CISO | Yes | Yes |
| Patrick Liu — CFO | Yes | Yes |
| Renata Kovac — CCO | Yes | Yes |
| Michael Torres — CTO (Observer) | Yes | No |
| Aisha Patel — GRC Director (Secretary) | Yes | No |

**Quorum:** 5 of 5 voting members. Quorum met.

### Discussion

#### 1. CISO Security Posture Report

Victoria presented Q4 2024 metrics:
- MTTD: 2.4 hours (target < 4 hours) — On Target
- MTTR: 5.2 hours (target < 8 hours) — On Target
- Vulnerability remediation: Critical 100%, High 94%, Medium 82%
- Training completion: 96.8%
- Phishing click rate: 5.1% (target < 8%)
- Vendor assessments: Critical 100%, High 93%

Eleanor asked about the High vulnerability remediation rate (94% vs 95% target). Victoria explained 2 high vulnerabilities in the trading platform required coordinated weekend deployment. Patrick asked about cost implications of the weekend deployment — Victoria confirmed it was within budget.

#### 2. Enterprise Risk Register

3 new risks identified:
- RSK-2025-001: AI model risk (new ML-based fraud detection system)
- RSK-2025-002: Third-party API concentration risk (80% of market data from 2 providers)
- RSK-2025-003: Regulatory pressure on operational resilience (SEC proposed rules)

**Decision:** Accepted RSK-2025-001 as Medium with quarterly monitoring. Accepted RSK-2025-002 as High — Victoria to develop diversification plan. RSK-2025-003 deferred to CCO for regulatory analysis.

#### 3. 2025 Security Budget Review

Victoria presented the 2025 security budget:
- Total: $6.2M (down from $7.3M in 2024, a 15.1% decrease)
- Personnel: $4.1M (up 5.1% — 2 new hires plus merit increases)
- Tools: $1.2M (down 28% — tool rationalization initiative completed)
- External services: $600K (down 33% — brought threat hunting in-house)
- Training: $150K (down 12% — consolidated training vendors)
- Contingency: $150K (new line item — 2.4% reserve)

Patrick noted the headline decrease was misleading given the personnel increase. The tool and services reductions were the result of a deliberate rationalization effort Victoria initiated in Q3 2024 to eliminate redundant tools and bring mature capabilities in-house.

Michael (CTO, observer) confirmed that from a technology perspective, no security capability was lost — the SIEM consolidation and in-house threat hunting were improvements, not cuts.

Eleanor asked Victoria directly: "Are you confident this budget provides adequate resources for the security program?" Victoria responded: "Yes. The reductions are in areas where we have achieved operational maturity. The personnel increase — which is where the real capability resides — reflects continued investment. The contingency line is new and provides a buffer we lacked in 2024."

**Decision:** Budget endorsed unanimously. Patrick to finalize in corporate budget.

#### 4. Policy Review Pipeline

Victoria reported 12 policies due for review in 2025. 3 completed in Q1. On schedule.

**Decision:** Acknowledged.

### Action Items

| ID | Action | Owner | Due |
|----|--------|-------|-----|
| AI-Q1-001 | Develop API concentration risk diversification plan | Victoria Santos | June 30, 2025 |
| AI-Q1-002 | Complete SEC operational resilience gap analysis | Renata Kovac | May 31, 2025 |

---

## Q2 Meeting — June 18, 2025

**Meeting ID:** SRGC-2025-Q2
**Date:** June 18, 2025 | 10:00 AM - 12:00 PM EST
**Chair:** Eleanor Walsh

### Attendance

| Member | Present | Voting |
|--------|---------|--------|
| Eleanor Walsh | Yes | Yes |
| James Chen | Yes | Yes |
| Victoria Santos | Yes | Yes |
| Patrick Liu | No (board committee conflict) | Yes |
| Renata Kovac | Yes | Yes |
| Michael Torres (Observer) | Yes | No |
| Aisha Patel (Secretary) | Yes | No |

**Quorum:** 4 of 5 voting members. Quorum met.

### Discussion

#### 1. CISO Security Posture Report

Q1 2025 metrics:
- MTTD: 2.1 hours — On Target
- MTTR: 4.8 hours — On Target
- Vulnerability remediation: Critical 100%, High 96%, Medium 85%
- Training completion: 97.4%
- Phishing click rate: 4.3%
- Vendor assessments: Critical 100%, High 96%

All metrics on target. Eleanor noted the improvement trend across all categories.

#### 2. Incident: INC-2025-019 — Insider Threat Detection

Victoria briefed on INC-2025-019: a compliance analyst was found to have accessed 47 client records outside their role scope over a 3-week period. Detected by UEBA anomaly detection. Investigation by Internal Audit and Legal determined no data exfiltration — the analyst was conducting personal research on companies they were considering for personal investment, using client records as a shortcut. Employee terminated for policy violation (Code of Conduct Section 3.2 — confidentiality and conflicts of interest).

Eleanor asked whether this represented a systemic access control gap. Victoria explained: the analyst had legitimate access to the compliance database but was accessing records for clients they were not assigned to. Current RBAC is role-based, not client-based. Victoria proposed implementing attribute-based access control (ABAC) for the compliance database to restrict access to assigned clients only.

Renata noted this was also reported through the ethics hotline by the analyst's colleague, demonstrating the whistleblower program is working.

**Decision:** Approved ABAC implementation for compliance database. Target completion Q4 2025.

#### 3. API Concentration Risk Update

Victoria presented the diversification plan for AI-Q1-001. Identified 2 additional market data providers as backup. Implementation plan for Q3/Q4 2025. Cost: $180K incremental.

**Decision:** Approved diversification plan. Patrick to approve funding in absentia (email confirmation received June 20).

#### 4. Policy Review Pipeline

7 of 12 policies reviewed. On schedule.

### Action Items

| ID | Action | Owner | Due |
|----|--------|-------|-----|
| AI-Q2-001 | Implement ABAC for compliance database | Victoria Santos | December 31, 2025 |
| AI-Q2-002 | Deploy backup market data providers | Platform Team | October 31, 2025 |

---

## Q3 Meeting — September 17, 2025

**Meeting ID:** SRGC-2025-Q3
**Date:** September 17, 2025 | 10:00 AM - 12:00 PM EST
**Chair:** Eleanor Walsh

### Attendance

All 5 voting members plus CTO observer and Secretary present. Full attendance.

### Discussion

#### 1. CISO Security Posture Report

Q2 2025 metrics: All on target. Continued improvement in MTTD (1.9 hours). Victoria highlighted: "This is the first quarter where every metric exceeded its target."

#### 2. SOC 2 Type II Audit Preparation

Victoria reported SOC 2 readiness at 90%. Baker Tilly engaged for Q4 fieldwork. Two observations from readiness assessment:
- Observation 1: Policy review cycle language should specify calendar year vs rolling 12 months (currently says "annual")
- Observation 2: CISO administrative reporting to CTO should be documented with independence protections (already in charter but should be cross-referenced in policy)

Eleanor noted both observations were process maturity items, not control deficiencies.

**Decision:** Victoria to address both observations in Q4 policy updates.

#### 3. Budget Mid-Year Review

Patrick presented mid-year actuals:
- Total spend: $2.95M of $6.2M (47.6%)
- On track. No budget amendments needed.
- Contingency reserve: $150K untouched.

Patrick offered commentary: "The 15% headline decrease from 2024 has not impacted security posture — metrics have improved across the board. This was a well-executed rationalization, not a budget cut."

#### 4. Policy Review Pipeline

10 of 12 policies reviewed. Remaining 2 on track for Q4.

### Action Items

| ID | Action | Owner | Due |
|----|--------|-------|-----|
| AI-Q3-001 | Address SOC 2 readiness observations in Q4 policy updates | Victoria Santos | December 15, 2025 |
| AI-Q3-002 | Complete ABAC implementation for compliance database | Victoria Santos | December 31, 2025 |

---

## Q4 Meeting — December 10, 2025

**Meeting ID:** SRGC-2025-Q4
**Date:** December 10, 2025 | 10:00 AM - 1:00 PM EST (includes executive session)
**Chair:** Eleanor Walsh

### Attendance

All 5 voting members plus CTO observer and Secretary present. Full attendance.

### Discussion

#### 1. CISO Security Posture Report

Q3 2025 metrics: All on target for fourth consecutive quarter. Annual metrics summary to be presented to full Board in January 2026.

#### 2. SOC 2 Audit Progress

Baker Tilly fieldwork 80% complete. No findings or exceptions to date. Expected report issuance: February 2026.

#### 3. 2026 Security Budget Proposal

Victoria proposed $6.5M for 2026 (4.8% increase over 2025):
- Personnel: $4.4M (+7.3% — 1 new security data engineer + merit)
- Tools: $1.15M (-4.2% — further rationalization)
- External services: $580K (-3.3% — stable)
- Training: $170K (+13.3% — increased certification support)
- Contingency: $200K (+33% — increased reserve)

Patrick noted the budget was sustainable and represented appropriate investment.

**Decision:** Endorsed 2026 budget proposal. Patrick to include in corporate budget submission.

#### 4. Annual Policy Review Summary

12 of 12 policies reviewed in 2025. All current. Victoria addressed the SOC 2 readiness observations:
- Updated policy review cycle language to specify "within 12 months of last approval"
- Added CISO independence cross-reference to information security policy

**Decision:** Approved policy updates.

#### 5. Executive Session (Management Excused)

Management (Victoria, Michael, Aisha) excused at 12:00 PM.

*Executive session minutes maintained separately by Board Secretary. Summary: Committee assessed CISO effectiveness as "Exceeds Expectations." Noted strong metrics improvement, successful tool rationalization, and effective incident response. No concerns about CISO independence or CTO relationship. Recommended continued dual reporting structure.*

### Action Items

| ID | Action | Owner | Due |
|----|--------|-------|-----|
| AI-Q4-001 | Finalize 2026 budget in corporate submission | Patrick Liu | January 15, 2026 |
| AI-Q4-002 | Present annual metrics to full Board | Victoria Santos | January Board meeting |

---

**Minutes compiled by:** Aisha Patel, GRC Director
