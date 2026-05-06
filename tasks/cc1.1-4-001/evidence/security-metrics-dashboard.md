# Security Metrics Dashboard — 2025 Annual Summary

**Report Period:** January 1 - December 31, 2025
**Prepared by:** GRC Team
**Distribution:** ISGC Members
**Classification:** Internal
**Organization:** Crestwood Dynamics

---

## KPI Summary

### KPI 1: Security Incident Volume

| Quarter | P1 | P2 | P3 | P4 | Total | Trend |
|---------|----|----|----|----|-------|-------|
| Q1 2025 | 0 | 2 | 8 | 23 | 33 | -- |
| Q2 2025 | 1 | 3 | 12 | 28 | 44 | Up |
| Q3 2025 | 0 | 1 | 6 | 19 | 26 | Down |
| Q4 2025 | 0 | 2 | 9 | 21 | 32 | Stable |
| **2025 Total** | **1** | **8** | **35** | **91** | **135** | -- |

**Analysis:** Q2 spike driven by phishing campaign targeting engineering team (INC-2025-062 was a P1 ransomware attempt). Q3/Q4 volumes returned to baseline after enhanced email filtering deployed.

### KPI 2: Vulnerability Remediation SLA Compliance

| Quarter | Critical (72h) | High (30d) | Medium (90d) | Low (180d) |
|---------|---------------|------------|--------------|------------|
| Q1 2025 | 100% | 92% | 85% | 78% |
| Q2 2025 | 100% | 88% | 82% | 75% |
| Q3 2025 | 85% | 90% | 80% | 72% |
| Q4 2025 | 100% | 94% | 88% | 80% |

**Analysis:** Q3 critical SLA miss (85%) caused by CVE-2025-38921 in payment module requiring coordinated multi-service deployment. Compensating WAF rules deployed within 4 hours.

### KPI 3: Security Awareness Training Completion

| Quarter | Target | Actual | Status |
|---------|--------|--------|--------|
| Q1 2025 | 95% | 93.2% | Below Target |
| Q2 2025 | 95% | 96.1% | On Target |
| Q3 2025 | 95% | 94.8% | Below Target |
| Q4 2025 | 95% | 97.3% | On Target |

**Analysis:** Full-year average 95.4%. Q1 and Q3 misses driven by new hire onboarding delays in Engineering.

### KPI 4: Phishing Simulation Click Rate

| Quarter | Campaigns | Avg Click Rate | Target | Status |
|---------|-----------|----------------|--------|--------|
| Q1 2025 | 3 | 7.8% | < 10% | On Target |
| Q2 2025 | 3 | 12.4% | < 10% | Off Target |
| Q3 2025 | 3 | 6.2% | < 10% | On Target |
| Q4 2025 | 3 | 5.9% | < 10% | On Target |

**Analysis:** Q2 spike (12.4%) attributed to sophisticated phishing template mimicking internal HR portal. Targeted re-training deployed for repeat clickers. Improvement sustained in Q3/Q4.

### KPI 5: Third-Party Risk Assessment Coverage

| Category | Total Vendors | Assessed | Coverage | Target |
|----------|--------------|----------|----------|--------|
| Critical | 12 | 12 | 100% | 100% |
| High | 28 | 26 | 92.9% | 95% |
| Medium | 45 | 34 | 75.6% | 80% |
| Low | 83 | 41 | 49.4% | 50% |

**Analysis:** High-risk vendor coverage slightly below target (92.9% vs 95%). Two vendors (DataStream Analytics and NorthPoint Consulting) have outstanding assessment questionnaires. Follow-ups sent November 2025.

---

**Prepared by:** Compliance Team, GRC
**Date:** January 10, 2026
