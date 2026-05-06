# Board of Directors — Security Posture Briefing

**Presented by:** Angela Morrison, CEO / Richard Tanaka, CISO
**Date:** September 18, 2025
**Classification:** Board Confidential
**Organization:** Crestwood Dynamics

---

## Agenda

1. Executive Summary
2. Security Program Maturity
3. Key Risk Areas
4. Incident Summary
5. Compliance Status
6. Budget and Investment
7. Recommendations

---

## 1. Executive Summary

Crestwood Dynamics' information security program continues to mature. The security team has made significant progress on the SOC 2 Type II readiness initiative, with external audit scheduled for Q4 2025. Key achievements in H1 2025 include deployment of enhanced SIEM correlation rules, completion of vendor migration for the legacy payment gateway, and a reduction in phishing click rates.

Areas requiring attention include the Q2 governance gap (committee quorum not achieved), a ransomware attempt in Q2 (successfully contained), and two vendor risk assessments still outstanding.

---

## 2. Security Program Maturity

| Domain | 2024 Score | 2025 Score | Target | Status |
|--------|-----------|-----------|--------|--------|
| Governance | 3.2 / 5.0 | 3.5 / 5.0 | 4.0 | Improving |
| Risk Management | 3.0 / 5.0 | 3.4 / 5.0 | 4.0 | Improving |
| Access Control | 3.8 / 5.0 | 4.1 / 5.0 | 4.0 | On Target |
| Data Protection | 3.5 / 5.0 | 3.7 / 5.0 | 4.0 | Improving |
| Incident Response | 3.3 / 5.0 | 3.8 / 5.0 | 4.0 | Improving |
| Vendor Management | 2.8 / 5.0 | 3.2 / 5.0 | 3.5 | Improving |

**Overall Maturity:** 3.5 / 5.0 (up from 3.1 in 2024)

---

## 3. Key Risk Areas

### 3.1 Ransomware / Destructive Attacks

- Risk Level: High
- Q2 ransomware attempt (INC-2025-062) targeting staging environment was contained
- No data exfiltration or production impact
- Root cause: compromised contractor credentials
- Remediation: mandatory MFA for all contractor accounts, enhanced EDR deployment

### 3.2 Third-Party / Supply Chain

- Risk Level: Medium-High
- 2 of 28 high-risk vendors have outstanding assessments
- CloudSync incident in May 2025 prompted enhanced vendor monitoring
- Vendor risk management standard updated in May

### 3.3 Regulatory Compliance

- Risk Level: Medium
- SOC 2 Type II readiness at 85%
- Two open remediation items: shared service accounts and staging logging gaps
- Expected to be audit-ready by October 2025

---

## 4. Incident Summary (H1 2025)

| Metric | H1 2025 | H1 2024 | Change |
|--------|---------|---------|--------|
| Total Incidents | 77 | 62 | +24% |
| P1 Incidents | 1 | 0 | +1 |
| P2 Incidents | 5 | 3 | +2 |
| MTTD (avg) | 3.9 hrs | 5.2 hrs | -25% |
| MTTR (avg) | 5.9 hrs | 8.4 hrs | -30% |

**Notable:** Detection and response times improved significantly despite higher incident volume. The increase in incidents is attributed to better detection capability, not increased threat activity.

---

## 5. Compliance Status

| Framework | Status | Next Milestone |
|-----------|--------|----------------|
| SOC 2 Type II | In Progress | Auditor engagement October 2025 |
| HIPAA | Compliant | Annual assessment due Q1 2026 |
| GDPR | Compliant | DPA reviews ongoing |
| CCPA | Compliant | Annual review scheduled Q4 2025 |

### Policy Review Status

- 11 of 12 policies reviewed and updated on schedule in 2025
- 1 policy overdue: Whistleblower Policy (POL-WB-001) — GC office delayed due to merger due diligence
- CISO has flagged to GC for prioritization

---

## 6. Budget and Investment

| Category | 2025 Budget | H1 Actuals | % Utilized |
|----------|------------|------------|------------|
| Personnel | $1,800,000 | $890,000 | 49.4% |
| Tools & Technology | $850,000 | $410,000 | 48.2% |
| Training | $150,000 | $62,000 | 41.3% |
| External Services | $400,000 | $215,000 | 53.8% |
| **Total** | **$3,200,000** | **$1,577,000** | **49.3%** |

**Note:** H1 spending on track with budget. External services slightly above plan due to forensics engagement for INC-2025-062.

---

## 7. Recommendations

1. **Resolve whistleblower policy review** — Prioritize with GC office by end of Q3
2. **Complete outstanding vendor assessments** — Two high-risk vendors need assessment by Q4
3. **Formalize Q2 governance remediation** — Establish backup meeting procedures to prevent future quorum failures
4. **Increase security headcount** — Request 2 additional FTEs for 2026 to support SOC 2 continuous compliance

---

**Questions from Board:**

- Board member J. Henderson asked about the contractor credential compromise timeline. CISO confirmed detection within 4 hours, containment within 8 hours. Board satisfied with response.
- Board Chair requested quarterly updates continue and asked for whistleblower policy resolution by next board meeting (December 2025).

---

**Minutes taken by:** Corporate Secretary
**Distribution:** Board Members Only
