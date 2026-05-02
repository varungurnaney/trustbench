# Task Reference

20 tasks across 8 SOC 2 controls. 13 are D4-D5 (red herrings, noise, judgment). Results from 3 models: GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6.

## Results Summary

| Task | D | GPT-5.5 | Opus 4.7 | Sonnet 4.6 | Hardest skill tested |
|------|---|---------|----------|------------|---------------------|
| cc6.1-1-002 | 1 | — | — | — | Policy reading |
| cc7.2-2-001 | 2 | — | — | — | Noticing absences in a table |
| cc8.1-1-001 | 1 | — | — | — | Policy reading |
| cc6.1-3-001 | 3 | 100% | 100% | 100% | Cross-referencing 6 documents |
| cc6.3-3-001 | 3 | — | — | — | PostgreSQL grant analysis |
| cc6.1-4-001 | 4 | — | — | — | Exception register validation |
| cc6.3-4-001 | 4 | 60% | 57% | 67% | Segregation of duties in DB roles |
| cc6.6-4-001 | 4 | 100% | 57% | 100% | Firewall rule exceptions |
| cc7.2-4-001 | 4 | 86% | 67% | 89% | Decommissioned service red herring |
| cc8.1-4-001 | 4 | 100% | 80% | 92% | Holiday freeze calendar math |
| cc9.1-4-001 | 4 | 100% | 67% | 73% | SOC 2 carve-out methodology |
| a1.2-4-001 | 4 | 100% | 62% | 100% | Backup failure with WAL compensating control |
| cc3.1-4-001 | 4 | 86% | 62% | 73% | Risk register with Board-approved exception |
| cc6.1-5-001 | 5 | 89% | 67% | 83% | Weekend termination SLA ambiguity |
| cc7.2-5-001 | 5 | 100% | 91% | 67% | Alert false positive rate materiality |
| cc8.1-5-001 | 5 | 73% | 91% | 83% | 94% test pass rate with documented flaky tests |
| a1.2-5-001 | 5 | — | — | — | Backup trending toward RTO breach |
| cc3.1-5-001 | 5 | 57% | 40% | 55% | Risk downgrade without justification |
| cc6.6-5-001 | 5 | 18% | 33% | 55% | Admin API boundary bypass materiality |
| cc9.1-5-001 | 5 | 33% | 40% | 36% | Vendor incident with 3-week data uncertainty |

---

## D4 Tasks — Red Herring Filtering

### cc6.3-4-001 — Data Access Authorization
**Company:** Aurora Labs | **Best: Sonnet 67%** | **Spread: 57-67%**

A MongoDB database has a `data-analytics` role with broad production read access. The exception register shows a valid CISO exception with data masking as a compensating control. The model must not flag this.

Real gaps: a user (`j.morrison`) with both read and write roles on financial collections (segregation violation), Looker access certification completed 21 days late, a contractor account (`r.santos`) with no expiration date, and an ownerless service account (`svc-etl-snowflake`) whose migration exception expired.

**Why models struggle:** All three models over-reported (precision 40-50%). The data access domain produces many observations that look like findings — every broad permission triggers a "least privilege" instinct. Distinguishing "this is broad but approved" from "this is broad and ungoverned" requires checking the exception register.

### cc6.6-4-001 — System Boundaries
**Company:** Prism Cloud | **Best: Sonnet/GPT-5.5 100%** | **Spread: 57-100%**

A security group rule allows traffic between staging and production VPCs. This looks like a segmentation failure, but the exception register documents a CISO-approved data sync workflow with IP allowlisting, encrypted tunnel, and audit logging as compensating controls.

Real gaps: a webhook receiver endpoint missing WAF, an internal notification service using unencrypted HTTP, a security group allowing 0.0.0.0/0 on port 9200 (Elasticsearch), and an internal endpoint handling PII over TLS 1.2 instead of 1.3.

**Why Opus struggled (57%):** Found all 4 gaps but reported 10 total findings, including flagging the red herring despite the exception register. It also noted several best-practice recommendations that inflated the finding count.

### cc7.2-4-001 — Monitoring
**Company:** Atlas Cloud | **Best: Sonnet 89%** | **Spread: 67-89%**

A legacy batch reconciliation service isn't in the SIEM. This looks like a coverage gap, but the exception register shows it was decommissioned on October 30 with approved monitoring exemption.

Real gaps: a new real-time collaboration service deployed November 15 that's still not in the SIEM 47 days later (5-day SLA), two critical alert SLA breaches during concurrent major incidents, no evidence of monthly alert tuning reviews, and no documentation of daily log reviews.

**Why models score differently:** GPT-5.5 (86%) missed the daily log review gap but had perfect precision. Sonnet (89%) found everything with only 1 extra finding. Opus (67%) found everything but reported too many extras.

### cc8.1-4-001 — Change Management
**Company:** Stratos Inc. | **Best: GPT-5.5 100%** | **Spread: 80-100%**

15 changes in Q4. Two red herrings involving the holiday freeze: CHG-414 (emergency DB failover during freeze — CISO approved via Slack) and CHG-415 (deployed December 20, the freeze start date — but pre-approved at the December 16 CAB meeting).

Real gaps: CHG-410 (log4j patch during Thanksgiving freeze without CISO approval), CHG-411 (retrospective CAB review 6 business days late), CHG-407/CHG-411 (developers deployed their own emergency changes — segregation violation), CHG-409 (approved without CAB quorum — Security Lead absent for a high-risk change), CHG-409 (missing post-implementation verification), CHG-412 (security review by the same person who developed the change).

**Why this task exposed a scoring issue:** The original keywords ("freeze", "approved") matched incidentally throughout any change management assessment. After tightening to entity-specific keywords ("CHG-415", "rate limit thresholds"), Opus went from a false 80% to a true 80% and Sonnet went from 86% to 92%. This is documented in the leaderboard as a keyword scoring limitation.

### cc9.1-4-001 — Vendor Management
**Company:** Quantum SaaS | **Best: GPT-5.5 100%** | **Spread: 18-100%**

14 vendors across 4 tiers. DataRobot (Critical, no SOC 2 report) and HubSpot (High, SOC 2 not provided) both look like policy violations. Both have CISO-approved exceptions in the exception register with compensating controls.

Real gaps: Stripe uses the carve-out method for GCP as a subservice organization with no independent assessment (requires SOC 2 methodology knowledge), Snowflake SOC 2 review pending on a Critical vendor processing PII, no business reviews for High-tier vendors processing customer data, and multiple vendors with unassessed carved-out subservice organizations.

**Why GPT-4o scored 18%:** It flagged both red herrings as findings without checking the exception register AND missed the carve-out gaps. The subservice organization carve-out vs. inclusive method distinction is SOC 2-specific domain knowledge that smaller models lack.

### a1.2-4-001 — Backup & Recovery
**Company:** Cobalt Systems | **Best: Sonnet/GPT-5.5 100%** | **Spread: 62-100%**

92 days of backup logs with 3 failures. The November 8 failure has no re-run (48-hour gap), but the exception register shows CISO acknowledgment with WAL archiving confirmed as compensating control.

Real gaps: December 1 failure re-run took 6 hours (exceeds 2-hour re-run SLA), restore time trending from 3h 15m to 3h 50m with only 10-minute margin to 4-hour RTO, no incremental backup logs provided to verify RPO claim, and backup sizes growing with no capacity planning documented.

**Why Opus scored 62%:** Found all gaps (100% recall) but reported 9 total findings. It flagged the November 8 failure as a finding despite the exception register, and added observations about backup encryption verification and cross-region replication testing.

### cc3.1-4-001 — Risk Assessment
**Company:** Vertex AI Corp | **Best: GPT-5.5 86%** | **Spread: 62-86%**

18-item risk register. RISK-014 is rated Critical with treatment "Accept" — looks like an unmitigated critical risk. But the exception register shows Board approval (BR-2025-012), legal analysis, insurance coverage, and quarterly reviews.

Real gaps: three risks (RISK-008, 009, 013) not reviewed within the quarterly cycle (6-9 months overdue), two risks (RISK-016, 017) with no assigned owner, annual risk assessment missing AI/ML and supply chain risk categories, and the assessment itself is 9 months old.

**Why GPT-5.5 scored highest (86%):** It correctly dismissed the red herring AND had perfect precision — only reported findings that matched planted gaps. But it missed the risk assessment staleness gap (75% recall). Opus found everything (100% recall) but over-reported (44% precision).

---

## D5 Tasks — Judgment Calls

### cc6.1-5-001 — Logical Access
**Company:** Nimbus Health | **Best: GPT-5.5 89%** | **Spread: 67-89%**

180 active Okta users vs. 178 in HR records — 2 unmatched accounts (service accounts? ghost accounts?). The AWS access review was done by James Chen, who also manages AWS (self-review). Derek Chung was terminated Friday at 5pm, Okta disabled Monday 9am — 64 calendar hours but only ~1 business hour over the 24-hour SLA if weekends are excluded. One access review completed 2 days late. Contractor accounts show no evidence of expiration dates.

**What separates models:** GPT-5.5 (89%) handled the weekend SLA ambiguity well and didn't over-report. Sonnet (83%) was more thorough but added extra findings. Opus (67%) found everything but reported too many observations as findings. The weekend termination question is a genuine judgment call — calendar hours vs. business hours changes whether this is a finding.

### cc7.2-5-001 — Monitoring
**Company:** Helix Data Systems | **Best: GPT-5.5 100%** | **Spread: 43-100%**

3 months of alert data across 8 rules. The S3 bulk access alert has a 95-97% false positive rate all quarter (policy threshold: 30%, tuning SLA: 2 weeks). Brute force alert SLA adherence dropped to 96% during an attack spike. SQL injection detection was disabled for 2 months with CISO approval and WAF compensating control. 5 impossible travel alerts in December marked "requires investigation" and never resolved.

**The widest D5 spread before the new tasks.** GPT-5.5 achieved perfect precision. GPT-4o reported 18 findings, treating every data point as a finding. The core skill tested: can the model distinguish "this metric is interesting" from "this is an audit finding"?

### cc8.1-5-001 — Change Management
**Company:** Beacon SaaS | **Best: Opus 91%** | **Spread: 73-91%**

20 deployments in Q4. One deployment had a 94% test pass rate — the 6% failures were documented flaky tests with remediation tickets. A hotfix skipped staging but was peer-reviewed and tested in a canary environment. Two rollbacks occurred in the quarter. One deployment was approved by the engineering manager instead of CAB because the weekly meeting was cancelled.

**Opus's best task (91%).** It correctly assessed the 94% pass rate as a finding (flaky tests indicate CI reliability issues even if documented), while GPT-5.5 (73%) was more lenient and missed it. This task tests whether models have calibrated judgment about software engineering practices — not just compliance checkbox checking.

### cc3.1-5-001 — Risk Assessment
**Company:** Zenith Cloud | **Best: GPT-5.5 57%** | **Spread: 40-57%**

22-item risk register. Two risks were downgraded from High to Medium during Q4 — one has "improved controls" in the SGC minutes but no documentation of which controls improved. The risk register was last comprehensively updated 11 months ago (annual requirement). The SGC reviewed only the top 10 of 22 risks. One risk has likelihood=2, impact=5 — rated "Medium" on the 5x5 matrix but arguably understates catastrophic-impact scenarios.

**The second-hardest task in the benchmark (avg 51%).** Every finding requires a materiality judgment. Is reviewing 10 of 22 risks "quarterly review" or a scope gap? Is 11 months "annual"? Does the matrix rating reflect actual risk when the impact is catastrophic? No model scored above 57%.

### cc6.6-5-001 — System Boundaries
**Company:** Apex Fintech | **Best: Sonnet 55%** | **Spread: 18-55%**

An internal admin API is exposed directly without going through the API gateway — used by SRE for emergency debugging, restricted to VPN, and documented as an accepted risk in the Q3 penetration test. 0.3% of traffic bypasses the gateway (all from VPN CIDR). The Q3 pentest covers the observation period boundary question. No mTLS certificate inventory was provided despite the policy claiming mTLS everywhere.

**The hardest task in the benchmark (avg 35%).** GPT-5.5 scored 18% — it found only the mTLS evidence gap and had 14% precision. Sonnet (55%) found 3 of 4 findings. Opus (33%) found 2 but over-reported heavily. The admin API question is the core challenge: it violates the boundary policy, but it's VPN-restricted, accepted risk, and only 0.3% of traffic. Every model handles this differently.

### cc9.1-5-001 — Vendor Management
**Company:** Onyx Data | **Best: Opus 40%** | **Spread: 33-40%**

A critical vendor (PrestoServe) had a security incident in November. They notified within 72 hours (meeting the contractual SLA), contained it in 48 hours, but couldn't confirm whether customer data was compromised for 3 weeks. Another vendor (Cloudmatic) has a qualified opinion on CC6.1 in their SOC 2 report — the review notes acknowledge it but no follow-up risk assessment was documented (policy requires one). PrestoServe's quarterly business review is 10 days overdue.

**The hardest task in the benchmark (avg 36%).** Every finding requires vendor risk judgment: Does meeting the 72-hour SLA excuse 3 weeks of data exposure uncertainty? Should customers have been notified during the uncertainty period? Is acknowledging a qualified opinion sufficient without a risk assessment? No model scored above 40%.

---

## Difficulty Distribution

| Level | Tasks | Avg F1 (best model) | What it tests |
|-------|-------|---------------------|---------------|
| D1-D2 | 3 | ~100% | Basic policy reading |
| D3 | 2 | 100% (saturated) | Multi-document cross-referencing |
| D4 | 7 | 90% (GPT-5.5) | Red herrings + exception registers + noise |
| D5 | 6 | 62% (varies) | Materiality judgment — no single right answer |

D5 tasks are where the benchmark has the most room. The two hardest tasks (cc6.6-5-001 at 35% avg, cc9.1-5-001 at 36% avg) show that even frontier models struggle with genuine compliance judgment calls.
