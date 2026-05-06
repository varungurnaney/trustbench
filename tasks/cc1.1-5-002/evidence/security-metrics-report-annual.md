# Security Metrics — Annual Summary 2025

**Report Period:** January 1 - December 31, 2025
**Prepared by:** GRC Team
**Distribution:** Information Security Committee
**Classification:** Internal
**Organization:** Northgate Logistics Technology

---

## Metric 1: Security Incident Trends

### Volume by Quarter

| Quarter | P1 | P2 | P3 | P4 | Total | MTTD (hrs) | MTTR (hrs) |
|---------|----|----|----|----|-------|-----------|-----------|
| Q1 2025 | 0 | 1 | 7 | 18 | 26 | 3.1 | 6.2 |
| Q2 2025 | 0 | 2 | 9 | 22 | 33 | 2.9 | 5.4 |
| Q3 2025 | 1 | 1 | 6 | 15 | 23 | 2.8 | 6.1 |
| Q4 2025 | 0 | 1 | 8 | 20 | 29 | 2.6 | 5.8 |
| **Annual** | **1** | **5** | **30** | **75** | **111** | **2.85** | **5.88** |

**Target:** MTTD < 4 hours, MTTR < 8 hours. Both targets met every quarter.

**Notable Incident:** INC-2025-034 (Q3 P1) — supply chain compromise attempt via compromised npm package in fleet telemetry service. Detected within 2 hours by SCA scanning. Contained within 4 hours. No data exfiltration.

---

## Metric 2: Vulnerability Remediation SLA Compliance

| Quarter | Critical (72h) | High (14d) | Medium (90d) | Low (180d) | Overall |
|---------|---------------|------------|--------------|------------|---------|
| Q1 2025 | 100% | 92% | 84% | 76% | 88% |
| Q2 2025 | 100% | 95% | 88% | 79% | 91% |
| Q3 2025 | 100% | 93% | 86% | 75% | 89% |
| Q4 2025 | 100% | 97% | 90% | 82% | 92% |

**Target:** Critical 100%, High 95%, Medium 85%, Low 75%.

**Analysis:** Critical SLA maintained at 100% all year. High SLA slightly below target in Q1 and Q3. Q4 showed improvement across all categories following deployment of automated patching for non-critical workloads.

---

## Metric 3: Security Awareness Training Completion

| Quarter | Target | Actual | Phishing Click Rate | Click Rate Target |
|---------|--------|--------|---------------------|-------------------|
| Q1 2025 | 95% | 97.2% | 6.8% | < 10% |
| Q2 2025 | 95% | 96.5% | 7.2% | < 10% |
| Q3 2025 | 95% | 98.1% | 5.4% | < 10% |
| Q4 2025 | 95% | 97.8% | 4.9% | < 10% |

**Analysis:** Training completion exceeded target every quarter. Phishing click rate trending down — Q4 at 4.9% is the lowest in company history.

---

## Metric 4: Third-Party Risk Assessment Coverage

| Vendor Tier | Total | Assessed | Coverage | Target |
|-------------|-------|----------|----------|--------|
| Critical | 8 | 8 | 100% | 100% |
| High | 22 | 21 | 95.5% | 95% |
| Medium | 38 | 30 | 78.9% | 80% |
| Low | 65 | 29 | 44.6% | 40% |

**Analysis:** Critical and High tier targets met. Medium tier slightly below target (78.9% vs 80%). One medium vendor (FleetView Analytics) assessment delayed due to vendor responsiveness. Follow-up in progress.

---

## Metric 5: Policy Exception Status

| Exception ID | Policy | Status | Risk | Compensating Controls | Notes |
|-------------|--------|--------|------|----------------------|-------|
| EXC-2025-001 | POL-ACC-007 | Active | Medium | PAM + session recording | Legacy fleet management admin access. Migration Q2 2026. |
| EXC-2025-002 | POL-ENC-007 | Expired — Remediated | Low | VPN tunnel | Internal API HTTP traffic. TLS deployed August 2025. |
| EXC-2025-003 | POL-VRM-007 | Active | High | Enhanced SLA monitoring | Sole-source GPS vendor without SOC 2 report. Contractual remediation clause added. |
| EXC-2025-004 | POL-LOG-007 | Active | Medium | Compensating alerting | Fleet IoT devices — limited log storage. Alerts forwarded to SIEM. |

**Summary:** 4 exceptions tracked. 1 remediated. 3 active with documented compensating controls. All reviewed by CISO within exception lifecycle.

---

## Metric 6: Regulatory Compliance Status

| Framework | Status | Last Assessment | Next Milestone |
|-----------|--------|-----------------|----------------|
| SOC 2 Type II | In Progress | Q4 2025 (Baker Tilly) | Report expected Q1 2026 |
| GDPR | Compliant | March 2025 (DPO review) | Annual assessment Q1 2026 |
| DOT Cybersecurity | Under Review | N/A — new requirement | Gap assessment due Q1 2026 |
| ISO 27001 | Not Certified | N/A | Evaluation for 2026 certification |
| PCI DSS | Compliant (SAQ-A) | July 2025 | Annual renewal July 2026 |

---

**Prepared by:** Amanda Lin, GRC Director
**Date:** January 8, 2026
