# TrustBench Task Expansion Plan

255 tasks across 17 compliance themes, 15 tasks per theme (3 at each difficulty level D1-D5).

## How to read this document

For each theme:
- **What auditors actually check** — the real audit procedures
- **Evidence artifacts** — document types that would appear in a real audit
- **3x D1 tasks** — obvious gaps in single documents
- **3x D2 tasks** — subtle gaps requiring careful reading
- **3x D3 tasks** — cross-referencing multiple documents
- **3x D4 tasks** — red herrings, exceptions, noise documents
- **3x D5 tasks** — materiality judgment, auditor disagreement
- **Success criteria** — what a correct response looks like at each level

---

## 1. Access Control (SOC 2 CC6.1-CC6.3 / ISO A.5.15-A.5.18 / FedRAMP AC)

**What auditors check:** User provisioning/deprovisioning, role-based access, least privilege, MFA enforcement, privileged access management, access reviews.

**Evidence artifacts:** Access control policy, IAM credential reports (AWS/GCP/Azure), Okta/Entra user exports, MFA enrollment reports, PAM tool exports (CyberArk/BeyondTrust), access review completion logs, termination records with disable timestamps, role-permission matrices.

### D1 — Single Document, Obvious Gap
1. **No MFA for production.** Policy lists MFA requirements for VPN, email, cloud console — but omits production servers and databases. Gap is stated in the policy text.
2. **Shared admin account.** Policy prohibits shared accounts but Section 4.2 describes a shared "deploy-admin" account used by the ops team. Contradiction within same document.
3. **No access review frequency.** Policy says "periodic access reviews" but never defines the frequency — no quarterly/annual requirement specified.

### D2 — Single Document, Subtle Gap
1. **Termination SLA buried in appendix.** Policy body says "prompt revocation" but Appendix B defines "prompt" as 72 hours — most auditors expect 24 hours or less. The gap is in the appendix, not the body.
2. **Contractor exception in a table footnote.** Access requirements table has a footnote: "Contractor accounts exempt from quarterly review per HR agreement." This exempts a high-risk population from a key control.
3. **Emergency access without post-review.** Break-glass procedure described in detail but no requirement for post-incident review of what was accessed. Buried in a 40-line procedure section.

### D3 — Cross-Reference, Multiple Documents
1. **Policy says SSO-only, IAM report shows direct users.** Policy prohibits direct IAM users. AWS credential report shows 3 human users with console passwords. Access review log only covers SSO users. Three documents, three gaps.
2. **Terminated employee still in IAM.** Termination log shows employee left Oct 15. IAM report generated Nov 30 still shows their active access key (last used Oct 16). HR says terminated, IT didn't revoke.
3. **MFA policy vs Okta config.** Policy claims MFA for all sessions. Okta sign-on policy export shows default policy with requireFactor=false — any new app falls through without MFA.

### D4 — Red Herrings, Exceptions, Noise
1. **Service account with manual key — valid exception.** Looks like a policy violation, but exception register has CISO approval with compensating controls (IP allowlist, Vault storage, daily audit). Red herring. Real gap: a different service account with an expired exception.
2. **Contractor without quarterly review — but they terminated.** Contractor shows no Q4 review. Looks like a gap, but termination log shows they left in Q3. Red herring. Real gap: active contractor with no review.
3. **Root account used — but for authorized infra change.** CloudTrail shows root login. Looks critical, but change log shows authorized break-glass for infrastructure migration with two-person sign-off. Red herring. Real gap: a different privileged action with no documentation.

### D5 — Materiality Judgment
1. **Weekend termination SLA.** Employee terminated Friday 5pm, access disabled Monday 9am. 64 calendar hours, but only ~1 business hour past 24-hour SLA. Is weekend time counted? Auditors disagree.
2. **Self-review of access.** AWS admin reviewed their own AWS access during the quarterly review. Policy doesn't explicitly prohibit self-review. Segregation issue or acceptable when reviewer is the system owner?
3. **96% SLA adherence on terminations.** 24 of 25 terminations met SLA. One missed by 48 hours during holiday week. Is 96% acceptable operational performance or a control deficiency?

**Success criteria:**
- D1-D2: Model identifies the specific gap with reference to the document section
- D3: Model cross-references at least 2 documents to identify the inconsistency
- D4: Model checks the exception register before flagging, correctly dismisses red herrings
- D5: Model acknowledges the ambiguity, presents both interpretations, states a reasoned position

---

## 2. Change Management (SOC 2 CC8.1 / ISO A.8.32 / FedRAMP CM)

**What auditors check:** Change authorization, testing before deployment, segregation (developer ≠ deployer), CAB approval, rollback plans, post-implementation verification, emergency change procedures.

**Evidence artifacts:** Change management policy, change request log (Jira/ServiceNow CSV), CAB meeting minutes, deployment logs with timestamps, test results/QA sign-offs, rollback documentation, standard change catalog.

### D1
1. **Developer deploys own code.** Policy says developer deploys to production — no independent deployer. Segregation violation.
2. **No rollback plan required.** Change process describes submission, approval, deployment — no rollback plan step.
3. **Emergency changes with no retroactive approval.** Emergency process allows verbal approval with no requirement for documented retroactive CAB review.

### D2
1. **Standard change catalog too broad.** SC-004 covers "dependency updates (minor/patch)" but the change log shows a major version upgrade (React 18→19) categorized as standard. The catalog definition is too loose.
2. **Testing requirement says "recommended" not "required."** Policy Section 4.3: "Testing in staging is recommended before production deployment." Recommended ≠ required — no control.
3. **CAB quorum defined but never enforced.** Policy requires 3 members. CAB minutes show 6 of 10 meetings had only 2 attendees. Gap is in comparing the policy definition against the actual minutes pattern.

### D3
1. **Change approved without security review on high-risk change.** Policy requires security review for High/Critical. Change log shows a high-risk change approved at a CAB meeting. CAB minutes show Security Lead was absent. Three documents needed.
2. **Change deployed outside maintenance window.** Policy says Saturday 02:00-06:00 UTC. Change log shows deployment at 14:00 UTC on Wednesday. The change was categorized "Standard" to bypass the window restriction.
3. **Post-implementation verification missing.** Change log shows post_impl_verified = "No" for a completed change. Policy requires verification within 2 hours. Change is marked "Completed" despite missing this step.

### D4
1. **Emergency change during holiday freeze — valid CISO approval.** Red herring: change has documented CISO approval via Slack. Real gap: a different change during freeze with no CISO approval.
2. **Change deployed on freeze start date — pre-approved.** Red herring: approved at CAB meeting 4 days before freeze. Real gap: retrospective CAB review that exceeded the 48-hour SLA by 4 days.
3. **Failed deployment looks bad but rollback succeeded.** Red herring: deployment failed and rolled back within 15 minutes per procedure. Real gap: a successful deployment with no testing evidence attached. Noise document: SDLC overview.

### D5
1. **94% test pass rate with documented flaky tests.** 6% failures are known flaky tests with Jira tickets. Is this acceptable or should flaky tests be fixed before deploying?
2. **Hotfix skipped staging but was peer-reviewed.** Emergency fix bypassed staging environment but had PR approval and was tested in canary. Policy requires staging. Is the compensating control adequate?
3. **Two rollbacks in one quarter.** 2 of 20 deployments were rolled back. Is this a systemic quality issue or normal operations? The rollbacks were unrelated and each was handled per procedure.

---

## 3. Risk Assessment (SOC 2 CC3.1-CC3.4 / ISO A.5.7 / FedRAMP RA)

**What auditors check:** Annual risk assessment, risk register maintenance, likelihood/impact ratings, risk treatment plans, risk ownership, risk acceptance process, emerging risk identification.

**Evidence artifacts:** Risk management policy, risk register (CSV/spreadsheet), annual risk assessment report, risk treatment plans, Security Governance Committee meeting minutes, risk appetite statement, exception register for risk acceptances.

### D1
1. **No risk appetite statement.** Policy describes the risk assessment process but never defines acceptable risk levels or risk appetite.
2. **Risk register has no owner column.** 15 risks listed but no assigned owner for any of them — no accountability.
3. **No emerging risk process.** Policy covers existing risk identification but has no process for identifying new/emerging risks (AI, supply chain, etc.).

### D2
1. **Risk rated "Low" despite critical impact.** RISK-007 has likelihood=1, impact=5 on the 5x5 matrix, yielding "Medium" by formula — but the impact is catastrophic (complete data breach). The matrix may understate the risk.
2. **Annual assessment date approaching expiry.** Assessment dated February — by December it's 10 months old. Still within the annual window, but barely. Auditors may question currentness.
3. **Risk treatment plan says "mitigate" but lists no controls.** RISK-012 treatment is "Mitigate" with mitigation description left blank. The plan exists but has no substance.

### D3
1. **Risk register vs control mapping gap.** Risk register lists 18 risks. Control mapping document only maps 14 to specific controls. 4 risks have no controls assigned. Requires comparing two documents.
2. **Three risks overdue for quarterly review.** Risk register shows last_review dates. Policy requires quarterly review. Three risks haven't been reviewed in 6+ months. Requires comparing dates against policy SLA.
3. **SGC reviewed 10 of 22 risks.** Meeting minutes show "top 10 risks reviewed." Risk register has 22 entries. 12 risks were not reviewed. Requires comparing meeting scope against register.

### D4
1. **Critical risk accepted — valid Board approval.** RISK-014 rated Critical with treatment "Accept." Looks wrong, but exception register shows Board approval, legal analysis, insurance coverage, quarterly review cycle. Red herring. Real gap: 3 overdue risk reviews.
2. **Risk downgrade with SGC approval — but no documentation of what changed.** Minutes say "approved downgrade based on improved controls." No evidence of which controls improved. Red herring if you only read the minutes; gap if you ask for supporting evidence.
3. **New risk category missing but company claims it's covered.** No "AI/ML" risk category, but the company argues existing "data processing" risks cover AI. Judgment on whether the argument holds. Noise: business impact analysis document.

### D5
1. **Is 10/22 risk review sufficient?** SGC reviewed "top 10" risks quarterly. Policy says "quarterly risk review." Is reviewing 45% of risks a "quarterly review"? Depends on interpretation.
2. **Risk assessment 11 months old.** Annual requirement, assessment dated January, now December. Technically still within the annual window. But is a nearly-year-old assessment still reflective of the current environment?
3. **Risk matrix methodology question.** Impact=5 (catastrophic) with likelihood=1 (rare) rates as "Medium." Should catastrophic-impact risks always be treated as High regardless of likelihood? The matrix is mathematically correct but arguably flawed.

---

## 4. Incident Response (SOC 2 CC7.3-CC7.5 / ISO A.5.24-A.5.28 / FedRAMP IR)

**What auditors check:** IR plan existence and completeness, roles and responsibilities, communication procedures, evidence preservation, post-incident review, plan testing, notification SLAs.

**Evidence artifacts:** Incident response plan, incident log (CSV), post-mortem reports, tabletop exercise records, communication templates, escalation matrix, mean-time-to-detect/respond metrics, customer notification records.

### D1
1. **No communication plan.** IRP covers detection, containment, eradication, recovery — but no section on communicating to customers, regulators, or executives during an incident.
2. **No plan testing.** IRP is comprehensive but has no section on testing/exercising the plan. No tabletop exercises, no simulations documented.
3. **No evidence preservation requirements.** Plan describes responding to incidents but not preserving forensic evidence — no chain of custody, no log retention during incidents.

### D2
1. **P2 severity has no after-hours coverage.** IRP gives P1 24/7 on-call but P2 only business-hours triage. P2 includes "unauthorized access to production" — a serious security event that could wait overnight.
2. **Post-mortem SLA buried in appendix.** Plan says post-mortems are "encouraged." Appendix C says "required within 5 business days for P1/P2." The requirement exists but is easy to miss.
3. **Escalation matrix has a single point of failure.** All P1 escalations go to the Security Lead. No backup listed. If the Security Lead is unavailable, the escalation path is undefined.

### D3
1. **Incident log shows SLA breach.** IRP defines 15-minute P1 triage SLA. Incident log shows a P1 with 45 minutes to first response. Post-mortem for that incident doesn't mention the SLA miss.
2. **Post-mortem action items not tracked.** Post-mortem says "improve alert coverage for X." Incident log 2 months later shows the same alert gap caused another incident. Action item was never completed.
3. **Tabletop exercise tested wrong scenario.** IRP covers data breach, ransomware, DDoS. Tabletop exercise only tested DDoS. No evidence of testing data breach or ransomware response — the two highest risks.

### D4
1. **Incident SLA miss during major outage — valid concurrent incident exception.** Two P1s occurred simultaneously. Second P1 missed SLA because the team was working the first. Red herring if concurrent incidents are documented. Real gap: a P1 that missed SLA on a normal day with no explanation.
2. **Old incident without post-mortem — but it was a false positive.** Incident log shows a P2 with no post-mortem. Looks like a gap, but the incident notes say "false positive — automated alert, no actual incident." Red herring. Real gap: actual P2 incident with no post-mortem.
3. **Plan testing is "overdue" — but the plan was just updated.** Plan was rewritten in November, testing is annual, last test was for the old plan in June. Testing the old plan doesn't validate the new one. Is this a gap or is 1 month since rewrite too soon to test?

### D5
1. **Customer notification timing.** Data breach contained in 4 hours. Investigation took 3 weeks to confirm 200 customers affected. Company notified customers at week 3. Should they have notified earlier with "potential" impact language, or was waiting for confirmation the right call?
2. **Post-mortem quality vs existence.** Post-mortem exists but is 3 sentences: "Alert fired, team responded, issue fixed." No root cause, no action items, no timeline. Is a perfunctory post-mortem better than none? Does it satisfy the control?
3. **Annual plan testing frequency.** IRP tested via tabletop in June. Major platform change occurred in September. Should the plan be re-tested after significant changes, or does annual suffice?

---

## 5. Vendor / Supply Chain (SOC 2 CC9.1-CC9.2 / ISO A.5.19-A.5.23 / FedRAMP SA, SR)

**What auditors check:** Vendor risk assessment, SOC 2/ISO 27001 report review, contractual requirements (DPA, right-to-audit, incident notification), subservice organization monitoring, ongoing vendor monitoring, vendor termination procedures.

**Evidence artifacts:** Vendor management policy, vendor inventory (CSV), SOC 2 report review notes, DPA/BAA tracker, vendor risk assessment questionnaires, exception register for vendor exceptions, vendor incident communications, business review records, subservice organization disclosures.

### D1
1. **No right-to-audit clause required.** Vendor policy lists contractual requirements but omits right-to-audit clause.
2. **No vendor risk tiering.** Policy treats all vendors the same — no Critical/High/Medium/Low classification based on data access or system integration.
3. **No vendor offboarding process.** Policy covers onboarding and monitoring but has no section on vendor termination — revoking access, data return/destruction.

### D2
1. **SOC 2 report review says "clean opinion" but the report has a qualified opinion.** Review notes say "reviewed, clean opinion." The actual report summary mentions one qualified opinion on CC6.1. Reviewer may not have read carefully.
2. **Vendor SLA for incident notification is 30 days.** Buried in a contract summary table: vendor's incident notification SLA is 30 calendar days. Industry standard and most policies require 72 hours.
3. **Annual reassessment date lapsed.** Vendor inventory shows last_assessment for a Critical vendor was 14 months ago. Policy says annual. The lapse is visible only if you check the dates.

### D3
1. **Vendor uses carve-out for subservice org — no independent assessment.** Policy requires independent assessment for carved-out subservice orgs. Vendor SOC 2 review notes show carve-out method for GCP. No GCP assessment on file. Three documents.
2. **DPA tracker doesn't match vendor inventory.** Vendor inventory lists 16 vendors. DPA tracker has 13 signed agreements. 3 vendors process data without a DPA. Two documents to compare.
3. **SOC 2 report expired, renewal not tracked.** Vendor inventory shows SOC 2 report period ended 5 months ago. No new report received. Review notes show no follow-up. Policy requires current reports.

### D4
1. **Critical vendor without SOC 2 — valid exception with compensating controls.** DataRobot is new (onboarded 3 months ago), exception register shows CISO approval with security questionnaire, encryption, SOW-limited access. Red herring. Real gap: different vendor with expired exception.
2. **Vendor had a security incident — but met notification SLA.** Vendor notified within 72 hours per contract. Looks compliant. But the investigation took 3 weeks to determine if customer data was affected. Real gap: no risk assessment documented after the incident.
3. **Vendor ISO 27001 certified — used as SOC 2 substitute.** Policy requires SOC 2 for Critical vendors. Vendor has ISO 27001 but not SOC 2. Exception register shows CISO accepted ISO 27001 as equivalent. Red herring if exception is valid. Real gap: vendor with neither SOC 2 nor ISO 27001.

### D5
1. **Vendor contained incident in 48 hours but 3-week data uncertainty.** Met contractual SLAs. But customers were potentially exposed for 3 weeks without notification. Should the company have notified its own customers during the vendor's investigation?
2. **Qualified SOC 2 opinion — acknowledged but no risk assessment.** Policy says "reports with qualified opinions require risk assessment." Review notes say "qualified opinion on CC6.1 noted." No separate risk assessment. Is acknowledgment sufficient?
3. **Business review 10 days overdue.** Quarterly business review for a Critical vendor is 10 days past the due date at end of the observation period. Minor scheduling issue or a control failure?

---

## 6. Data Protection / Encryption (SOC 2 C1.1-C1.2, CC6.7 / ISO A.8.11-A.8.12 / FedRAMP SC)

**What auditors check:** Encryption at rest, encryption in transit, key management, data classification, DLP controls, data masking, certificate management.

**Evidence artifacts:** Encryption policy, TLS configuration audit (CSV), certificate inventory, key management procedures, data classification policy, DLP rule configuration, cloud storage encryption settings (JSON), database encryption status.

### D1
1. **No encryption at rest requirement.** Policy covers encryption in transit (TLS) but doesn't mention encryption at rest for databases or object storage.
2. **No key rotation schedule.** Key management procedure describes key generation and storage but no rotation requirements — keys could be used indefinitely.
3. **Data classification exists but has no handling requirements.** Classification defines 4 levels (Public/Internal/Confidential/Restricted) but doesn't specify encryption, access, or storage requirements for each level.

### D2
1. **TLS 1.0 enabled on a partner endpoint.** TLS config shows 14 endpoints on TLS 1.3, one internal endpoint on TLS 1.2, and one partner integration endpoint on TLS 1.0. The TLS 1.0 endpoint is buried in row 16.
2. **Certificate expiring in 30 days.** Certificate inventory shows one cert expiring in 30 days with no auto-renewal configured. All others have auto-renewal via cert-manager.
3. **S3 bucket encryption is AES-128 not AES-256.** Policy specifies AES-256. Cloud storage config shows one bucket using AES-128 (SSE-S3 default). The difference is in a JSON field.

### D3
1. **Policy says all PII encrypted, database shows unencrypted columns.** Encryption policy requires all PII encrypted at rest. Database schema export shows email and phone columns are not encrypted — only SSN and payment fields are. Two documents.
2. **DLP rules don't cover a new data channel.** DLP policy covers email, USB, cloud storage. Data flow diagram shows a new API export to a partner system. No DLP rule covers API exports. Three documents.
3. **Key rotation overdue.** Key management procedure says 90-day rotation. KMS key inventory shows a production encryption key last rotated 7 months ago. Two documents.

### D4
1. **Unencrypted internal endpoint — valid exception for performance.** Internal analytics pipeline uses unencrypted gRPC for latency reasons. Exception register shows CISO approval with compensating controls (VPC-internal only, no PII in transit, network segmentation). Red herring. Real gap: a different internal service handling PII over unencrypted HTTP with no exception.
2. **TLS 1.2 on internal endpoint — accepted risk.** TLS config shows one internal endpoint on TLS 1.2. Policy says TLS 1.3 required. Exception register covers this with planned upgrade date. Red herring. Real gap: the planned upgrade date was 3 months ago and the upgrade hasn't happened.
3. **Certificate inventory discrepancy — noise.** Certificate inventory shows 45 certs. A separate infrastructure report mentions 47 endpoints. The 2 "missing" certs are for decommissioned services. Noise: the infrastructure report is irrelevant to encryption controls.

### D5
1. **AES-128 vs AES-256 — material?** One backup storage bucket uses AES-128 instead of policy-required AES-256. AES-128 is still considered cryptographically secure. Is this a finding or an observation?
2. **Internal traffic encryption.** All external traffic is encrypted. Internal east-west traffic between microservices in the same VPC is unencrypted. Policy says "all data in transit." VPC is a trust boundary. Do internal services in a private network need encryption?
3. **Key rotation was 2 weeks late.** 90-day rotation policy, key was rotated at 104 days. It was rotated, just late. Material deficiency or operational variance?

---

## 7. Monitoring / Logging (SOC 2 CC7.1-CC7.2 / ISO A.8.15-A.8.16 / FedRAMP AU)

**What auditors check:** Log collection completeness, log retention, SIEM coverage, alert configuration, alert response SLAs, log review, monitoring of privileged activity, anomaly detection.

**Evidence artifacts:** Monitoring policy, SIEM coverage report, alert rule inventory, alert response log, log retention configuration, monitoring coverage review, exception register for monitoring gaps.

### D1
1. **No log retention period defined.** Policy requires logging but doesn't specify how long logs are retained.
2. **No privileged activity monitoring.** Policy covers general authentication monitoring but doesn't specifically address monitoring of admin/root actions.
3. **No alert tuning process.** Alert rules exist but there's no documented process for tuning false positives or reviewing alert effectiveness.

### D2
1. **Weekly vulnerability scan review.** All other monitoring sources alert in real-time. Qualys vulnerability scan results go to a weekly email report. A critical vulnerability could sit for 7 days.
2. **Alert SLA defined only for Critical.** Policy defines 15-minute SLA for Critical alerts. High, Medium, Low have "as appropriate" — no measurable SLA.
3. **Database monitoring absent from coverage list.** SIEM coverage includes infrastructure, application, cloud API, endpoint, email — but not database activity. Buried in a table of 8 monitoring sources.

### D3
1. **New service deployed without monitoring.** SIEM coverage report shows 18 of 20 services integrated. Service deployment log shows 2 new services deployed in the observation period. Coverage review confirms they missed the 5-day SLA. Three documents.
2. **Alert false positive rate exceeds threshold.** Alert summary CSV shows S3 bulk access alert at 95% FP rate for 3 months. Policy threshold is 30%, tuning SLA is 2 weeks. Tuning ticket was created but never resolved.
3. **Log retention config doesn't match policy.** Policy says 12-month retention. Log storage configuration JSON shows CloudTrail at 12 months but application logs at 90 days and database audit logs at 30 days.

### D4
1. **Decommissioned service not in SIEM — valid exception.** Service appears in SIEM coverage gap list. Exception register shows it was decommissioned with approved monitoring exemption. Red herring. Real gap: an active service deployed 47 days ago still not in SIEM.
2. **SQL injection alert disabled — CISO approved with WAF compensating control.** Alert disabled due to 100% FP rate (all blocked by WAF). CISO approved with compensating control documented. Red herring — or is it? If WAF is bypassed, no secondary detection exists. Judgment overlap with D5.
3. **Alert SLA miss during major incident — concurrent response.** Two Critical alerts fired simultaneously. Second alert missed SLA because team was responding to first. Red herring. Real gap: a Critical alert that missed SLA on a normal day.

### D5
1. **96% alert SLA adherence — acceptable?** 285 of 298 alerts acknowledged within SLA. 13 missed during a coordinated brute force attack (high volume). Is 96% acceptable during abnormal conditions?
2. **5 impossible travel alerts unresolved.** Alert triage shows 5 "requires investigation" alerts that were never resolved by end of quarter. They might be real security events or false positives. No SLA in policy for resolving investigations.
3. **Monthly alert tuning — no evidence of reviews.** Policy says monthly review. No log review records provided. The control might be operating, but without evidence, it can't be verified. Is absence of evidence a finding?

---

## 8-17 remaining themes follow the same pattern. Each uses the same 5-level structure:

## 8. Business Continuity (A1.1-A1.3 / ISO A.5.29-A.5.30 / FedRAMP CP)
**Artifacts:** BCP/DRP, backup logs, restore test results, DR failover test records, RPO/RTO definitions, capacity planning docs.
*Scenarios: backup failures with WAL compensating controls, RTO trending toward breach, DR test that didn't cover all critical systems, restore test on non-production data, failover test that revealed 30-minute gap.*

## 9. Physical Security (CC6.4-CC6.5 / ISO A.7.1-A.7.14 / FedRAMP PE)
**Artifacts:** Physical security policy, badge access logs, visitor logs, data center audit reports, CCTV retention records, environmental monitoring logs.
*Scenarios: tailgating incident, badge access not revoked for terminated employee, visitor unescorted in server room, environmental sensor calibration overdue, data center shared with another tenant.*

## 10. HR Security (CC1.4-CC1.5 / ISO A.6.1-A.6.6 / FedRAMP PS, AT)
**Artifacts:** HR security policy, background check completion records, security awareness training completion log, acceptable use policy acknowledgments, role-change access review records.
*Scenarios: background check completed after access was granted, training completion at 85% (15% not completed), employee changed roles with no access review, contractor without AUP acknowledgment, security training content not updated in 2 years.*

## 11. Asset Management (CC6.1 / ISO A.5.9-A.5.14 / FedRAMP CM-8)
**Artifacts:** Asset inventory, CMDB export, data classification register, asset ownership assignments, asset disposal records.
*Scenarios: shadow IT not in CMDB, assets with no owner, classification mismatch between CMDB and data handling procedures, decommissioned asset still in inventory, BYOD devices accessing production data without MDM.*

## 12. Vulnerability Management (CC7.1 / ISO A.8.8 / FedRAMP RA-5, SI-2)
**Artifacts:** Vulnerability management policy, scan reports (Qualys/Nessus CSV), patch management records, remediation SLA tracking, risk acceptance register for unfixed vulns.
*Scenarios: 90-day Critical remediation SLA with one vuln at 120 days, scan coverage missing a new subnet, vulnerability accepted without compensating controls, patch applied but not validated, scanning frequency reduced during code freeze.*

## 13. Network Security (CC6.6 / ISO A.8.20-A.8.23 / FedRAMP SC-7)
**Artifacts:** Network security policy, firewall rules (JSON), VPC/subnet configs, network diagrams, WAF configuration, DNS security settings.
*Scenarios: overly permissive security group (0.0.0.0/0), missing WAF on public endpoint, staging-to-production network path, unencrypted inter-service traffic, admin API exposed without gateway.*

## 14. Privacy (P1.1-P1.8 / ISO A.5.34 / FedRAMP PT)
**Artifacts:** Privacy policy, consent management records, data retention schedule, DSAR (data subject access request) log, privacy impact assessments, data processing records.
*Scenarios: retention schedule says 2 years but data exists from 5 years ago, DSAR response took 45 days (30-day GDPR requirement), consent collected but no mechanism to withdraw, processing activity without documented legal basis, analytics tracking without user notice.*

## 15. Governance (CC1-CC2, CC5 / ISO A.5.1-A.5.6 / FedRAMP PL, PM)
**Artifacts:** Information security policy, security committee charter, committee meeting minutes, policy review records, organizational chart for security function, security metrics reports.
*Scenarios: CISO reports to CTO not CEO/Board (independence question), security policy not reviewed in 18 months, security committee met 2 of 4 required quarterly meetings, security budget not documented, no security metrics reported to leadership.*

## 16. System Integrity (PI1.1-PI1.5 / ISO A.8.9, A.8.25 / FedRAMP SI)
**Artifacts:** SDLC policy, code review records, static analysis scan results, deployment pipeline config, input validation rules, data integrity checks.
*Scenarios: code deployed without peer review, static analysis findings not remediated, input validation bypass on one API endpoint, data integrity check runs weekly not daily as policy states, configuration drift between staging and production.*

## 17. Maintenance (CC7.1 / ISO A.7.13 / FedRAMP MA)
**Artifacts:** Maintenance policy, maintenance window schedule, patching records, equipment maintenance logs, vendor maintenance agreements.
*Scenarios: OS patch applied outside maintenance window, maintenance performed by unauthorized vendor technician, remote maintenance session not logged, equipment maintenance overdue by 6 months, emergency maintenance without change ticket.*

---

## Implementation Priority

### Phase 1 (highest value — fills zero-coverage gaps)
1. Incident Response (0 tasks → 15)
2. Data Protection / Encryption (0 tasks → 15)
3. Vulnerability Management (0 tasks → 15)
4. Privacy (0 tasks → 15)

### Phase 2 (expands partial coverage)
5. Access Control (4 tasks → 15)
6. Change Management (3 tasks → 15)
7. Risk Assessment (2 tasks → 15)
8. Vendor / Supply Chain (2 tasks → 15)
9. Monitoring / Logging (3 tasks → 15)

### Phase 3 (new areas)
10. HR Security (0 → 15)
11. Business Continuity (2 → 15)
12. Physical Security (0 → 15)
13. Governance (0 → 15)
14. Network Security (2 → 15)
15. Asset Management (0 → 15)
16. System Integrity (0 → 15)
17. Maintenance (0 → 15)

### Effort estimate
- D1 tasks: ~30 min each (1 document, 3-4 gaps)
- D2 tasks: ~45 min each (1 document, careful gap placement)
- D3 tasks: ~1.5 hours each (3+ documents, cross-references)
- D4 tasks: ~2 hours each (3+ docs, red herrings, noise, exception register)
- D5 tasks: ~2.5 hours each (3+ docs, judgment calls, ambiguity design)

Total: ~255 tasks × ~1.5 hours avg = ~380 hours of authoring work.

With LLM-assisted drafting (LLM generates evidence docs, human reviews and calibrates): ~255 × 30 min = ~130 hours.
