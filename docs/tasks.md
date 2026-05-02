# Task Reference

All tasks currently in TrustBench, with evidence structure, planted findings, and complexity notes.

---

## cc6.1-1-002 — Access Control Policy Review

| Field | Value |
|-------|-------|
| Control | CC6.1 (Logical Access Security) |
| Difficulty | D1 |
| Category | detection |
| Scoring | detection_only |
| Evidence | 1 document |
| Findings | 4 gaps |

**Evidence:**
- `access-control-policy.md` — NovaTech Solutions access control policy (policy)

**Findings:**

| ID | Type | Severity | Finding |
|----|------|----------|---------|
| F-001 | gap | high | No SLA for access revocation on termination — policy says "timely manner" |
| F-002 | gap | high | MFA not required for production servers or databases |
| F-003 | gap | medium | Access review evidence format, storage, retention not specified |
| F-004 | gap | medium | Role change revocation depends solely on manager notification |

**Complexity:** Minimal. Single document, all gaps visible on careful reading. No cross-referencing needed. Tests whether the model reads a policy and identifies missing elements against CC6.1 requirements.

---

## cc6.1-3-001 — Logical Access Cross-Reference

| Field | Value |
|-------|-------|
| Control | CC6.1 (Logical Access Security) |
| Difficulty | D3 |
| Category | cross_reference |
| Scoring | detection_and_precision |
| Evidence | 6 documents |
| Findings | 9 gaps |

**Evidence:**
- `access-control-policy.md` — Meridian Cloud Systems access control policy (policy)
- `aws-iam-credential-report.csv` — IAM users, key rotation dates, MFA status (config)
- `access-review-log-q4-2025.csv` — quarterly access review completion records (log)
- `terminations-q4-2025.csv` — employee terminations with Okta disable dates (log)
- `okta-mfa-policies.json` — sign-on policy configuration with 3 priority-ordered policies (config)
- `service-account-inventory.csv` — service account ownership, review dates (spreadsheet)

**Findings:**

| ID | Type | Severity | Finding | Cross-ref needed |
|----|------|----------|---------|-----------------|
| F-001 | gap | critical | jenkins-legacy: stale IAM key (2+ years), unowned, unreviewed | IAM report + SA inventory |
| F-002 | gap | high | legacy-monitoring: key rotation 9 months overdue, unowned | IAM report + SA inventory |
| F-003 | gap | high | david.kim: direct IAM console user, policy prohibits this | IAM report + policy §3.3 |
| F-004 | gap | high | Tom Bradley: Okta disabled 7 days after termination (4-hour SLA) | terminations + policy §6.1 |
| F-005 | gap | medium | Priya Sharma: Okta disabled 3 days after termination | terminations + policy §6.1 |
| F-006 | gap | high | Okta default policy has requireFactor=false, contradicts policy | Okta config + policy §4.2 |
| F-007 | gap | medium | Okta access review: 23 business days (15-day SLA), 5 flagged but 3 revoked | access review + policy §5.1 |
| F-008 | gap | medium | backup-s3-sync: two active keys, one unrotated for 2 years | IAM report |
| F-009 | gap | high | Direct IAM users not included in access review scope (only SSO reviewed) | access review + IAM report |

**Complexity:** Moderate. Every finding requires comparing at least two documents. The Okta JSON config requires parsing a priority-ordered policy chain to understand the default fallback. The termination findings require date arithmetic. The access review scope gap requires noticing what's absent (direct IAM users) from the review log. This is the task that saturated at 100% for 6 frontier models.

---

## cc6.1-4-001 — Service Accounts with Exceptions and Noise

| Field | Value |
|-------|-------|
| Control | CC6.1 (Logical Access Security) |
| Difficulty | D4 |
| Category | red_herring |
| Scoring | f1 |
| Evidence | 3 documents + 2 noise |
| Findings | 1 red herring, 3 gaps |

**Evidence:**
- `access-control-policy.md` — Vantage Corp access control policy (policy)
- `gcp-service-accounts.json` — 6 GCP service accounts with key status, workload identity bindings, IAM roles (config)
- `exception-register.csv` — 4 CISO-approved exceptions with compensating controls, expiration dates (exception_register)

**Noise:**
- `business-continuity-plan-summary.md` — BCP executive summary, irrelevant to CC6.1
- `vendor-risk-assessment-q4.csv` — vendor SOC 2 report status, irrelevant to CC6.1

**Findings:**

| ID | Type | Severity | Finding | Why it's hard |
|----|------|----------|---------|--------------|
| F-001 | red_herring | low | legacy-etl has manual key — but VEXC-2025-004 is a valid, active CISO exception | Model must check exception register before flagging |
| F-002 | gap | critical | terraform-import has roles/editor, exception expired April 2025, SA still active 9 months later | Must cross-ref exception register expiration date |
| F-003 | gap | high | monitoring-agent key used after exception expired Dec 10 (key used Dec 28) | Date comparison: exception expiry vs last-used date |
| F-004 | gap | medium | legacy-etl exception claims compensating controls but key never rotated since 2023 | Exception is valid but compensating controls aren't operating |

**Complexity:** High. The red herring (F-001) tests whether the model checks the exception register before flagging a service account with a manual key. F-002 and F-003 require comparing exception expiration dates against the service account activity dates. F-004 is the subtlest — the exception itself is valid, but the compensating controls it claims (key rotation, Vault storage) aren't evidenced in the actual key data (key created 2023, never rotated). The noise documents test whether the model stays focused on CC6.1.

---

## cc6.3-3-001 — Data Access Authorization Cross-Reference

| Field | Value |
|-------|-------|
| Control | CC6.3 (Access Authorization) |
| Difficulty | D3 |
| Category | cross_reference |
| Scoring | detection_and_precision |
| Evidence | 3 documents |
| Findings | 5 gaps |

**Evidence:**
- `authorization-policy.md` — ClearView Analytics data access authorization policy (policy)
- `aws-rds-access-grants.json` — PostgreSQL role grants, privileges, role memberships (config)
- `data-access-requests-q4.csv` — Jira access request tickets with approval chains (log)

**Findings:**

| ID | Type | Severity | Finding | Cross-ref needed |
|----|------|----------|---------|-----------------|
| F-001 | gap | high | developer_debug role has full read-write to all production tables, only manager approval (needs CISO) | DB grants + access requests + policy §3.1 |
| F-002 | gap | high | evan.smith has both developer_debug and etl_pipeline roles (segregation violation), no expiration | DB grants (role memberships) + access requests |
| F-003 | gap | high | analytics_readonly has production access, policy says analysts use read-only replica with PII masking | DB grants + policy §3.4 |
| F-004 | gap | medium | marketing_integration syncs to HubSpot — likely >1,000 records, needs CISO approval for bulk export | DB grants + access requests + policy §3.2 |
| F-005 | gap | medium | developer_debug granted by postgres superuser in 2023, never re-authorized under current policy | DB grants (granted_by + date) + policy effective date |

**Complexity:** Moderate. Requires understanding PostgreSQL grant structures (role memberships, ALL TABLES grants). F-002 requires noticing one user has two roles in the role_memberships array. F-003 requires comparing the policy's description of the analytics workflow against the actual database grants. F-004 requires inferring that a continuous HubSpot sync exceeds the 1,000-record bulk export threshold. F-005 requires noticing the grant predates the current policy.

---

## cc7.2-2-001 — Incident Response Plan Review

| Field | Value |
|-------|-------|
| Control | CC7.2 (Monitoring & Anomaly Detection) |
| Difficulty | D2 |
| Category | detection |
| Scoring | detection_only |
| Evidence | 1 document |
| Findings | 4 gaps |

**Evidence:**
- `incident-response-plan.md` — Pinnacle SaaS incident response plan (policy)

**Findings:**

| ID | Type | Severity | Finding |
|----|------|----------|---------|
| F-001 | gap | high | P2 incidents (including "unauthorized access to production") have no after-hours coverage |
| F-002 | gap | medium | Qualys vulnerability scan results delivered as weekly report, not real-time alerts |
| F-003 | gap | medium | No database activity monitoring in the monitoring stack |
| F-004 | gap | low | IRP tested annually via single tabletop exercise only |

**Complexity:** Low-moderate. F-001 is the subtlest — it's buried in a table showing P1 gets 24/7 on-call but P2 only gets "business hours" triage, and the model must recognize that P2 includes serious security events. F-002 requires comparing Qualys's delivery method (weekly report) against the real-time alerting of all other monitoring sources. F-003 requires noticing what's absent from a list. F-004 is an industry-knowledge question about testing frequency expectations.

---

## cc7.2-5-001 — Monitoring & Alerting Judgment

| Field | Value |
|-------|-------|
| Control | CC7.2 (Monitoring & Anomaly Detection) |
| Difficulty | D5 |
| Category | judgment |
| Scoring | f1 |
| Evidence | 3 documents + 1 noise |
| Findings | 5 gaps |

**Evidence:**
- `monitoring-policy.md` — Helix Data Systems security monitoring and alerting policy (policy)
- `alert-summary-q4-2025.csv` — 3 months of alert data: 8 alert rules × 3 months = 24 rows with counts, FP rates, triage times (log)
- `monitoring-coverage-review-q4.json` — quarterly review showing 2 coverage gaps, 1 disabled alert rule, 3 new services deployed (report)

**Noise:**
- `penetration-test-summary.md` — annual pentest executive summary, not directly relevant to CC7.2 monitoring controls

**Findings:**

| ID | Type | Severity | Finding | Why it requires judgment |
|----|------|----------|---------|------------------------|
| F-001 | gap | high | Two production services deployed without monitoring (25+ and 80+ days past 5-day SLA) | Clear finding, but model must cross-ref coverage review against policy SLA |
| F-002 | gap | high | S3 bulk access alert at 95-97% FP rate for 3 months (policy threshold: 30%, 2-week tuning SLA) | Model must calculate FP rates from the CSV data and compare against policy threshold |
| F-003 | gap | medium | Brute force alert SLA adherence dropped to 96% in December during attack spike | Judgment: is 96% acceptable? Misses were during high-volume periods suggesting capacity, not process failure |
| F-004 | gap | medium | SQL injection detection rule disabled for 2 months with CISO approval and WAF compensating control | Judgment: CISO approved with compensating control — is this acceptable or still a gap? |
| F-005 | gap | medium | 5 impossible travel alerts in December marked "requires investigation" and never resolved | Model must notice the unresolved status and assess whether these could be real security events |

**Complexity:** High. The alert summary CSV requires numerical reasoning — calculating false positive percentages from raw counts, comparing across months to identify trends, and computing SLA adherence rates. F-003 and F-004 are genuine judgment calls where reasonable auditors would disagree. F-005 requires noticing a specific status value ("requires investigation") in a dense CSV and understanding its implications. This task produced the widest score spread in our benchmarks (91% to 43%).

---

## cc8.1-1-001 — Change Management Policy Review

| Field | Value |
|-------|-------|
| Control | CC8.1 (Change Management) |
| Difficulty | D1 |
| Category | detection |
| Scoring | detection_only |
| Evidence | 1 document |
| Findings | 3 gaps |

**Evidence:**
- `change-management-policy.md` — Orion Health change management policy (policy)

**Findings:**

| ID | Type | Severity | Finding |
|----|------|----------|---------|
| F-001 | gap | high | No segregation of duties — requesting engineer also deploys to production |
| F-002 | gap | high | No testing requirement before production deployment (staging mentioned but no gate) |
| F-003 | gap | medium | Emergency change process: verbal approval only, retroactive ticket with no time limit |

**Complexity:** Minimal. Single document with straightforward gaps. F-001 is stated explicitly in the policy ("deployed by the requesting engineer"). F-002 requires noticing the absence of a testing gate despite staging being mentioned. F-003 requires recognizing that verbal approval is not auditable.

---

## cc8.1-4-001 — Change Management with Red Herrings and Calendar Math

| Field | Value |
|-------|-------|
| Control | CC8.1 (Change Management) |
| Difficulty | D4 |
| Category | red_herring |
| Scoring | f1 |
| Evidence | 3 documents + 2 noise |
| Findings | 2 red herrings, 6 gaps |

**Evidence:**
- `change-management-policy.md` — Stratos Inc. change management policy with freeze periods, CAB quorum rules, segregation requirements (policy)
- `change-log-q4-2025.csv` — 15 changes with developer, approver, deployer, risk rating, dates, testing evidence, post-implementation status (log)
- `cab-meeting-minutes-q4.md` — 10 CAB meetings with attendees, quorum status, and retrospective reviews (report)

**Noise:**
- `sdlc-overview.md` — SDLC methodology overview, not relevant to CC8.1 control testing
- `incident-log-q4-2025.csv` — Q4 incidents, related to changes but not a CC8.1 evidence artifact

**Findings:**

| ID | Type | Severity | Finding | Why it's hard |
|----|------|----------|---------|--------------|
| F-001 | red_herring | low | CHG-414: emergency DB failover during holiday freeze | Looks like a freeze violation, but CISO approval was obtained via Slack and retrospective CAB completed. Policy explicitly allows this. |
| F-002 | red_herring | low | CHG-415: deployed Dec 20 (first day of holiday freeze) | Approved at Dec 16 CAB meeting, scheduled before freeze began. Not a new approval during freeze. |
| F-003 | gap | high | CHG-410: log4j patch during Thanksgiving freeze without CISO approval, outside maintenance window | Standard change during freeze — policy requires CISO approval for ALL changes during freeze |
| F-004 | gap | high | CHG-411: retrospective CAB review 6 business days later (policy says 48 business hours) | Requires interpreting "48 business hours" and counting business days between Dec 1 and Dec 9 |
| F-005 | gap | high | CHG-407 + CHG-411: developers deployed their own emergency changes (segregation violation) | Must compare developer column vs deployer column for each change against policy §3.3 |
| F-006 | gap | high | CHG-409: approved at CAB without quorum, Security Lead absent for a high-risk change | Must cross-ref change log (high risk) against CAB minutes (2/3 attendees, no quorum) |
| F-007 | gap | medium | CHG-409: post-implementation verification missing (post_impl_verified = No) | Simple field check, but on the same change with other issues |
| F-008 | gap | medium | CHG-412: security review performed by the same person who developed the change | Must notice the developer and security reviewer are both maya.jackson |

**Complexity:** High. The two red herrings are the core challenge — both involve changes during the holiday freeze, but one has valid CISO approval and the other was pre-approved before the freeze. The model must distinguish between these and the real freeze violation (CHG-410). F-004 requires calendar math (counting business days). F-005 requires column-by-column comparison across the CSV. F-006 requires cross-referencing the change log's risk rating against CAB meeting attendance. The noise documents test whether the model stays focused on CC8.1 evidence. This task exposed keyword scoring limitations in the original run.

---

## cc9.1-4-001 — Vendor Management with Exception Register

| Field | Value |
|-------|-------|
| Control | CC9.1 (Vendor Risk Mitigation) |
| Difficulty | D4 |
| Category | red_herring |
| Scoring | f1 |
| Evidence | 3 documents + 1 noise |
| Findings | 2 red herrings, 4 gaps |

**Evidence:**
- `vendor-management-policy.md` — Quantum SaaS vendor risk management policy with tier definitions, SOC 2 review requirements, subservice org monitoring rules (policy)
- `vendor-inventory.csv` — 14 vendors with tier, SOC 2 status, DPA, subservice orgs, review dates (spreadsheet)
- `vendor-exception-register.csv` — 2 CISO-approved exceptions for DataRobot and HubSpot (exception_register)

**Noise:**
- `data-classification-policy.md` — data classification levels, not directly relevant to CC9.1

**Findings:**

| ID | Type | Severity | Finding | Why it's hard |
|----|------|----------|---------|--------------|
| F-001 | red_herring | low | DataRobot: Critical vendor without SOC 2 report | VEXC-2025-001: active CISO exception, new vendor, SOC 2 expected Q1 2026, compensating controls documented |
| F-002 | red_herring | low | HubSpot: High vendor, SOC 2 not provided despite requests | VEXC-2025-002: active CISO exception, alternative assessment completed, ISO 27001 confirmed |
| F-003 | gap | high | Stripe uses carve-out method for GCP — no independent assessment per policy §4.2 | Requires understanding SOC 2 inclusive vs carve-out methodology and noticing GCP is not independently assessed |
| F-004 | gap | high | Snowflake SOC 2 review pending — Critical vendor processing PII operating without current review | Must check review status column and interpret "Pending" against 90-day SLA |
| F-005 | gap | medium | No business reviews for High-tier vendors (SendGrid, HubSpot, Zendesk, Amplitude) | Technically compliant (policy only requires for Critical) but a control design weakness for PII-handling vendors |
| F-006 | gap | medium | Multiple vendors use carve-out for GCP/AWS with no independent subservice org assessment | Broader pattern of F-003 across Amplitude, SendGrid, Lattice |

**Complexity:** High. The red herrings are the hardest test in the benchmark — DataRobot and HubSpot look like clear policy violations (Critical/High vendor without SOC 2 on file). The model must check the exception register, verify the exceptions are current, and assess whether the compensating controls are adequate. GPT-4o failed both of these. F-003 requires SOC 2-specific knowledge about inclusive vs carve-out report methodology — a domain concept that mid-tier models don't reliably understand. F-005 is a judgment call: the policy is technically met, but the control design is weak for vendors handling customer PII.

---

## Summary

| Task | Control | D | Category | Evidence | Noise | Gaps | Red Herrings | Key Skill Tested |
|------|---------|---|----------|----------|-------|------|--------------|-----------------|
| cc6.1-1-002 | CC6.1 | 1 | detection | 1 | 0 | 4 | 0 | Policy reading |
| cc7.2-2-001 | CC7.2 | 2 | detection | 1 | 0 | 4 | 0 | Careful reading, noticing absences |
| cc6.1-3-001 | CC6.1 | 3 | cross_reference | 6 | 0 | 9 | 0 | Multi-document cross-referencing |
| cc6.3-3-001 | CC6.3 | 3 | cross_reference | 3 | 0 | 5 | 0 | DB grant analysis, approval chain validation |
| cc6.1-4-001 | CC6.1 | 4 | red_herring | 3 | 2 | 3 | 1 | Exception register validation, date comparison |
| cc8.1-4-001 | CC8.1 | 4 | red_herring | 3 | 2 | 6 | 2 | Holiday freeze reasoning, calendar math, CSV column comparison |
| cc9.1-4-001 | CC9.1 | 4 | red_herring | 3 | 1 | 4 | 2 | SOC 2 carve-out methodology, exception validation |
| cc8.1-1-001 | CC8.1 | 1 | detection | 1 | 0 | 3 | 0 | Policy reading |
| cc7.2-5-001 | CC7.2 | 5 | judgment | 3 | 1 | 5 | 0 | Numerical reasoning, materiality assessment, trend analysis |
| a1.2-5-001 | A1.2 | 5 | judgment | 3 | 0 | 4 | 0 | Backup log analysis, RTO trending, evidence sufficiency |
