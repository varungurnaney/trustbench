# Privacy Impact Assessment — Solaris Automated Underwriting Decision Engine

**PIA Reference:** PIA-SOL-2025-003
**Assessment Date:** February 15, 2025
**Assessor:** Claire Donovan, Senior Privacy Analyst
**Reviewed by:** Sean Gallagher, DPO
**Status:** Current
**Next Review:** February 15, 2026

---

## 1. Processing Description

**System:** Solaris Automated Underwriting Engine (SAUE) v3.2
**Purpose:** Automated assessment of insurance applications to determine risk scores, premium pricing, and coverage eligibility decisions.
**Decision Outputs:** APPROVE (policy issued automatically), CONDITIONAL (policy issued with conditions/exclusions), DECLINE (application rejected).

**Data Inputs:**
The SAUE processes the following data elements as features in the underwriting model:

From applicant (PROC-001, PROC-004):
- Age, gender, address (postcode), occupation
- Property details (home) or vehicle details (motor)
- Health questionnaire responses (health products only)
- Claims history (self-declared)
- Coverage amount and deductible preferences

From LexisNexis (PROC-006):
- Motor vehicle record: licence status, penalty points, driving offences (5-year history)
- CLUE report: prior claims (5-year loss history, all insurers)
- Property loss history (home products)

From TransUnion (PROC-007):
- Credit score (numerical)
- Credit history length
- Payment behavior indicators (late payments, defaults in past 3 years)
- Bankruptcy/insolvency records

**Processing Volume:**
- Approximately 15,000 applications processed per month
- 78% approved automatically, 10% conditionally approved, 12% declined

## 2. Automated Decision-Making Assessment

**Is this solely automated processing?** Yes. The initial coverage decision is made entirely by the SAUE without human intervention.

**Does it produce legal or similarly significant effects?** Yes. A decline decision denies the applicant insurance coverage, which can have significant financial and practical consequences (e.g., inability to drive legally without motor insurance, mortgage requirements for home insurance).

**GDPR Article 22 applicability:** Article 22(1) is engaged. The processing involves solely automated decision-making that produces significant effects on data subjects.

**Applicable exemption:** Article 22(2)(a) — the decision is necessary for entering into a contract between the data subject and the controller (insurance contract).

**Safeguards required under Article 22(3):**
- Right to obtain human intervention
- Right to express point of view
- Right to contest the decision

**Current implementation of safeguards:**
- Human review available ON APPEAL ONLY — applicant must affirmatively request human review via email to underwriting@solarisinsurance.eu or phone
- Applicant can provide additional information or context during appeal
- Appeal process involves senior underwriter reviewing model decision
- Average appeal processing time: 15 business days
- Appeal success rate: 23% (decision overturned)

## 3. Transparency Assessment

**Current privacy policy disclosure (Section 3):** "We use risk assessment tools to evaluate insurance applications."

**Assessment:** This disclosure is INSUFFICIENT. The privacy policy does not:
1. Use the term "automated decision-making" or "profiling"
2. Explain that coverage decisions are made without human review
3. Provide meaningful information about the logic of the algorithm
4. Explain the significance and envisaged consequences
5. Inform applicants of their right to human review under Art. 22(3)

**Recommendation:** UPDATE PRIVACY POLICY to include Article 22 disclosures with:
- Clear statement that underwriting decisions are solely automated
- Description of data inputs and their role in the decision
- Information about how to request human review
- Explanation of appeal process and timeline

**Management Response (March 5, 2025):** "Acknowledged. Privacy policy update scheduled for Q3 2025. Interim: decline notification emails include mention of appeal right." As of December 2025, the privacy policy has not been updated.

## 4. Model Explainability

**Explainability capability:** SHAP (SHapley Additive exPlanations) values are computed for each decision. The underwriting dashboard displays:
- Top 5 contributing factors for each decision
- Positive/negative contribution of each factor
- Comparison to approval threshold
- Feature importance rankings

**Current use:** Explainability features are used internally by the underwriting team for model monitoring and audit. They are NOT currently used to generate individual explanations for data subjects.

**Recommendation:** Use SHAP explanations to provide meaningful individual decision explanations in response to Art. 22(3) requests and Art. 15(1)(h) access requests.

## 5. Risk Assessment

| Risk | Likelihood | Impact | Risk Level |
|------|------------|--------|------------|
| Applicant denied coverage without understanding why | High | High | **Critical** |
| Discriminatory outcomes from biased training data | Medium | Critical | **Critical** |
| Third-party enrichment data (LexisNexis, TransUnion) inaccurate | Medium | High | **High** |
| Health data used in automated decisions without explicit Art. 9 consent | Medium | High | **High** |
| No meaningful human review unless applicant specifically requests | High | Medium | **High** |
| Privacy notice does not reflect automated decision-making practices | High | Medium | **High** |

## 6. Mitigations Applied

1. Appeal mechanism available (but only on request)
2. SHAP explainability computed for all decisions (but not shared with applicants)
3. Quarterly model fairness audits checking for demographic bias
4. Model retrained quarterly with updated training data
5. Decline notification email includes sentence: "If you believe this decision was made in error, you may request a review by contacting our underwriting team."
6. Senior underwriter conducts manual review of 5% random sample of approvals and declines monthly

## 7. Outstanding Actions

| Action | Priority | Owner | Target Date | Status |
|--------|----------|-------|-------------|--------|
| Update privacy policy with Art. 22 disclosures | High | Privacy Team | Q3 2025 | OVERDUE — not completed |
| Implement automated SHAP explanation in decline notifications | High | Engineering | Q4 2025 | OVERDUE — not started |
| Conduct Art. 9 legal basis review for health data in SAUE | Medium | Legal | Q3 2025 | OVERDUE — not started |
| Develop bias testing framework for protected characteristics | Medium | Data Science | Q1 2026 | On track |
