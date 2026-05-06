# Security Metrics Report — Q3 2025

**Report Period:** July 1 - September 30, 2025
**Prepared by:** Security Operations Team
**Distribution:** Security Steering Committee
**Classification:** Internal
**Organization:** Atherton SaaS Inc.

---

## Executive Summary

This report presents the five key security metrics as defined in the Information Security Policy (Section 6) for Q3 2025. Overall security posture remains strong with improvements in detection and response times, though vulnerability remediation compliance has declined.

---

## Metric 1: Mean Time to Detect (MTTD)

| Month | MTTD (hours) | Target | Status |
|-------|-------------|--------|--------|
| July 2025 | 2.3 | < 4 hours | On Target |
| August 2025 | 1.8 | < 4 hours | On Target |
| September 2025 | 3.1 | < 4 hours | On Target |
| **Q3 Average** | **2.4** | **< 4 hours** | **On Target** |

**Trend:** Improved from Q2 average of 3.6 hours. New SIEM correlation rules deployed in July contributed to faster detection.

---

## Metric 2: Mean Time to Respond (MTTR)

| Month | MTTR (hours) | Target | Status |
|-------|-------------|--------|--------|
| July 2025 | 6.2 | < 8 hours | On Target |
| August 2025 | 4.5 | < 8 hours | On Target |
| September 2025 | 12.4 | < 8 hours | Off Target |
| **Q3 Average** | **7.7** | **< 8 hours** | **On Target** |

**Trend:** September spike caused by INC-2025-089 (ransomware attempt on staging environment). Response required coordination with external forensics firm. Excluding this outlier, average was 5.4 hours.

**Note:** September's MTTR exceeded the 8-hour target. Root cause was weekend detection when on-call engineer was on PTO without backup coverage.

---

## Metric 3: Vulnerability Remediation Compliance Rate

| Severity | Total Vulns | Remediated On Time | Overdue | Compliance Rate | Target |
|----------|-------------|--------------------|---------|--------------------|--------|
| Critical | 8 | 6 | 2 | 75% | 100% |
| High | 34 | 24 | 10 | 70.6% | 95% |
| Medium | 127 | 89 | 38 | 70.1% | 80% |
| Low | 203 | 142 | 61 | 70.0% | 70% |

**Trend:** Critical vulnerability compliance dropped from 100% in Q2 to 75% in Q3. Two critical CVEs (CVE-2025-31247 and CVE-2025-33891) affecting the payment processing module were not remediated within the 72-hour window due to complex dependency chains requiring coordinated deployment.

**Risk Note:** Both overdue critical vulnerabilities were remediated within 7 days and compensating controls (WAF rules) were deployed within 24 hours.

---

## Metric 4: Security Awareness Training Completion Rate

| Department | Eligible | Completed | Rate | Target |
|-----------|----------|-----------|------|--------|
| Engineering | 68 | 62 | 91.2% | 95% |
| Product | 24 | 24 | 100% | 95% |
| Sales | 41 | 38 | 92.7% | 95% |
| Operations | 33 | 33 | 100% | 95% |
| Finance | 18 | 18 | 100% | 95% |
| HR | 12 | 12 | 100% | 95% |
| Executive | 8 | 6 | 75% | 95% |
| **Total** | **204** | **193** | **94.6%** | **95%** |

**Trend:** Overall completion rate slightly below target. Engineering department has 6 overdue completions (new hires in onboarding). Executive team has 2 overdue completions — CTO and CFO have not completed the Q3 refresher module.

---

## Metric 5: Policy Exceptions Status

| Exception ID | Policy | Requestor | Approved Date | Expiry Date | Status | Compensating Controls |
|-------------|--------|-----------|---------------|-------------|--------|----------------------|
| EXC-2025-001 | POL-ENC-003 | DevOps | 2025-02-15 | 2025-08-15 | Expired — Not Renewed | WAF + IP allowlist |
| EXC-2025-002 | POL-ACC-001 | Engineering | 2025-03-01 | 2025-09-01 | Expired — Remediated | Service account MFA bypass |
| EXC-2025-003 | POL-VUL-001 | Platform Team | 2025-06-10 | 2025-12-10 | Active | Legacy system — no patch available, network isolated |
| EXC-2025-004 | POL-ENC-003 | Data Team | 2025-07-01 | 2026-01-01 | Active | Internal analytics — TLS termination at load balancer |
| EXC-2025-005 | POL-ACC-001 | QA | 2025-08-20 | 2025-11-20 | Active | Shared test account — isolated test environment |

**Summary:** 5 exceptions tracked. 2 expired (1 remediated, 1 expired without renewal — needs follow-up). 3 active with documented compensating controls.

**Note:** EXC-2025-001 expired August 15 without renewal or remediation. Follow-up required with DevOps to determine current status.

---

**Prepared by:** Alex Rivera, Senior Manager, Security Operations
**Date:** October 8, 2025
