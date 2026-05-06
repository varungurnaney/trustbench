# Board of Directors — Annual Security Posture Report

**Presented by:** Victoria Santos, CISO
**Date:** January 15, 2026 (covering 2025 performance)
**Classification:** Board Confidential
**Organization:** Wavecrest Financial Services

---

## 1. Executive Summary

Wavecrest Financial Services' information security program achieved its strongest performance year in 2025. All six key security metrics exceeded targets for the first time. The security function successfully completed a tool rationalization initiative that reduced tooling costs by 28% while improving detection and response capabilities. SOC 2 Type II audit fieldwork was completed in Q4 with no findings to date.

The 15.1% overall budget decrease from 2024 reflected deliberate operational efficiencies, not reduced commitment to security. Personnel investment increased 5.1%, and all security team positions are fully staffed (24 FTEs, zero open positions). The 2026 budget proposal includes a 4.8% increase.

---

## 2. Key Performance Indicators — Annual Summary

| Metric | 2024 | 2025 | Target | Trend |
|--------|------|------|--------|-------|
| MTTD (hours) | 3.8 | 2.1 | < 4.0 | Improved 45% |
| MTTR (hours) | 7.2 | 4.9 | < 8.0 | Improved 32% |
| Critical Vuln SLA | 100% | 100% | 100% | Maintained |
| High Vuln SLA | 91% | 96% | 95% | Improved |
| Training Completion | 94.2% | 97.4% | 95% | Improved |
| Phishing Click Rate | 7.8% | 4.3% | < 8% | Improved 45% |
| Critical Vendor Coverage | 100% | 100% | 100% | Maintained |

**Year-over-year improvement observed across all metrics.** MTTD and phishing click rate showed the most dramatic improvements, attributed to SIEM correlation rule enhancements and targeted training programs.

---

## 3. Notable Incidents

### INC-2025-019: Insider Threat — Compliance Analyst

- **Detection:** UEBA anomaly detected unauthorized access pattern
- **Impact:** 47 client records accessed outside role scope; no exfiltration
- **Root Cause:** Analyst researching personal investment opportunities using client data
- **Outcome:** Employee terminated; ABAC implementation approved for compliance database
- **Ethics Program Note:** Initially reported through anonymous ethics hotline by colleague

### INC-2025-041: Supply Chain — Compromised NPM Package

- **Detection:** SCA scanning detected malicious package in build pipeline
- **Impact:** No production deployment; caught in CI/CD
- **Root Cause:** Typosquatting attack on legitimate dependency
- **Outcome:** Package blocklist updated; dependency pinning enforced

### INC-2025-057: Phishing — Executive Targeting

- **Detection:** Email security gateway + employee reporting
- **Impact:** No compromise; CFO reported suspicious email within 3 minutes
- **Root Cause:** Business email compromise attempt targeting wire transfer
- **Outcome:** Domain blocklisted; executive awareness training refreshed

---

## 4. Budget Performance

### 2025 Actuals vs Budget

| Category | Budget | Actual | Variance |
|----------|--------|--------|----------|
| Personnel | $4,100,000 | $4,050,000 | -$50,000 (vacancy savings) |
| Tools | $1,200,000 | $1,180,000 | -$20,000 |
| External Services | $600,000 | $575,000 | -$25,000 |
| Training | $150,000 | $145,000 | -$5,000 |
| Contingency | $150,000 | $0 | -$150,000 (unused) |
| **Total** | **$6,200,000** | **$5,950,000** | **-$250,000** |

**Commentary:** Came in $250K under budget, primarily from unused contingency reserve and minor savings across categories. This is a sign of effective budget planning, not underspending. All planned initiatives were completed.

### Budget Trend

| Year | Budget | Actual | Headcount |
|------|--------|--------|-----------|
| 2022 | $5.1M | $4.8M | 18 |
| 2023 | $6.0M | $5.7M | 20 |
| 2024 | $7.3M | $7.1M | 22 |
| 2025 | $6.2M | $5.95M | 24 |
| 2026 (proposed) | $6.5M | — | 25 |

**Note:** 2024 budget was the peak due to significant one-time investments: SIEM platform migration ($400K), endpoint detection deployment ($250K), and cloud security posture management implementation ($200K). These were project costs, not recurring. The 2025 "decrease" is primarily the absence of these one-time project costs plus the operational efficiencies from the tools they enabled.

---

## 5. Governance Summary

- **SRGC Meetings:** 4 of 4 quarterly meetings held. Full quorum at all meetings.
- **Policy Reviews:** 12 of 12 policies reviewed on schedule.
- **Risk Register:** Reviewed quarterly. 3 new risks identified and accepted/mitigated.
- **Exceptions:** 4 active exceptions with documented compensating controls. All reviewed within lifecycle.
- **Ethics Program:** 8 ethics reports received and processed. 1 substantiated insider case resulted in termination. Whistleblower program demonstrably functional.

---

## 6. 2026 Priorities

1. Complete SOC 2 Type II certification (report expected February 2026)
2. Implement ABAC for compliance database (in progress)
3. Deploy backup market data providers (API diversification)
4. Begin ISO 27001 readiness assessment
5. Evaluate zero trust architecture for trading platform
6. Hire security data engineer (approved in 2026 budget)

---

## 7. Questions for the Board

1. Does the Board have any concerns about the CISO reporting structure?
2. Does the Board support the ISO 27001 certification timeline (target: 2027)?
3. Are there any risk areas the Board would like deeper analysis on?

---

**Presented by:** Victoria Santos, CISO
**Date:** January 15, 2026
