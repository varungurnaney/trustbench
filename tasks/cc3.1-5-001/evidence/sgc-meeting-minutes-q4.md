# Security Governance Committee — Q4 2025 Quarterly Meeting Minutes

**Meeting Date:** December 18, 2025  
**Location:** Virtual (Zoom) — Recording available in GRC SharePoint  
**Duration:** 90 minutes (2:00 PM — 3:30 PM EST)  
**Document ID:** ZC-SGC-MIN-2025-Q4

---

## Attendees

| Name | Title | Status |
|------|-------|--------|
| Linda Okafor | Chief Risk Officer (Chair) | Present |
| Rajesh Mehta | CISO | Present |
| Tom Harrington | VP Engineering | Present |
| Susan Park | VP Product | Present |
| David Cho | General Counsel | Present |
| Maria Santos | Independent Risk Advisor | Present |

**Quorum:** Achieved (6 of 6 members present)

---

## Agenda

1. Review of Q3 action items
2. Top 10 risk register review
3. Risk rating change proposals
4. Q4 incident summary
5. Emerging risk discussion
6. Action items and next steps

---

## 1. Review of Q3 Action Items

| Action Item | Owner | Status |
|-------------|-------|--------|
| Complete air-gapped backup implementation | Rajesh Mehta | Completed — August 2025 |
| Update vendor security assessment questionnaire | Linda Okafor | Completed — September 2025 |
| Conduct tabletop exercise for ransomware scenario | Rajesh Mehta | Completed — October 2025 |
| Evaluate AI governance policy draft | Susan Park | In Progress — Expected Q1 2026 |

---

## 2. Top 10 Risk Register Review

The committee reviewed the top 10 risks by residual risk rating. Discussion highlights:

### ZC-RISK-001: Ransomware Attack on Production Infrastructure
- **Current Rating:** Medium (Likelihood 2, Impact 5)
- **Discussion:** Rajesh reported successful completion of air-gapped backup architecture in August. DR recovery test demonstrated full restoration within RTO. Committee agreed current rating is appropriate.
- **Decision:** Maintain at Medium.

### ZC-RISK-002: Cloud Misconfiguration Exposing Customer Data
- **Current Rating:** Previously High, proposed Medium
- **Discussion:** Rajesh proposed downgrade from High to Medium based on improved controls. Noted that Wiz CSPM deployment has been fully operational since July 2025 and IaC scanning catches misconfigurations pre-deployment.
- **Decision:** Approved downgrade to Medium.

### ZC-RISK-003: Key Personnel Dependency — Platform Engineering
- **Current Rating:** Medium (Likelihood 3, Impact 3)
- **Discussion:** Tom noted that cross-training program is ongoing but the two principal engineers (Anil Desai and James Wu) still hold critical institutional knowledge. Runbook documentation is approximately 60% complete.
- **Decision:** Maintain at Medium. Tom to provide completion timeline for runbook documentation.

### ZC-RISK-004: Third-Party Data Breach via SaaS Vendor
- **Current Rating:** Medium (Likelihood 2, Impact 4)
- **Discussion:** Linda noted the Snowflake industry incident in mid-2024 validates this risk. Zenith Cloud's credential rotation and SSO integration provide good protection.
- **Decision:** Maintain at Medium.

### ZC-RISK-006: DDoS Attack Degrading Service Availability
- **Current Rating:** Medium (Likelihood 2, Impact 3)
- **Discussion:** No significant change. AWS Shield Advanced continues to mitigate volumetric attacks effectively.
- **Decision:** Maintain at Medium.

### ZC-RISK-007: Insider Threat — Malicious Data Exfiltration
- **Current Rating:** Medium (Likelihood 2, Impact 5)
- **Discussion:** Rajesh noted that quarterly access reviews are current. DLP alerts show low false-positive rate after Q3 tuning.
- **Decision:** Maintain at Medium.

### ZC-RISK-008: Supply Chain Compromise via Open-Source Dependency
- **Current Rating:** Medium (Likelihood 2, Impact 3)
- **Discussion:** Tom mentioned recent xz-utils incident in the industry as a reminder of this risk. Snyk scanning is effective but doesn't cover all risk vectors.
- **Decision:** Maintain at Medium.

### ZC-RISK-011: API Authentication Bypass Vulnerability
- **Current Rating:** Medium (Likelihood 1, Impact 5)
- **Discussion:** Rajesh noted the Q3 pentest found no authentication bypass vulnerabilities. Bug bounty program has not received any critical submissions in Q4.
- **Decision:** Maintain at Medium.

### ZC-RISK-015: Phishing Attack Compromising Employee Credentials
- **Current Rating:** Previously High, proposed Medium
- **Discussion:** Rajesh proposed downgrade from High to Medium. Cited FIDO2 MFA rollout completion and improved phishing simulation results (click rate dropped from 8% to 2.1% over 12 months).
- **Decision:** Approved downgrade to Medium.

### ZC-RISK-021: AI Model Training Data Leakage
- **Current Rating:** Medium (Likelihood 2, Impact 3)
- **Discussion:** Susan noted the AI governance policy is still in draft. Currently, no customer data is used in model training, but the AI product roadmap for 2026 will introduce AI-powered features that will process customer data.
- **Decision:** Maintain at Medium. Susan to expedite AI governance policy finalization.

---

## 3. Risk Rating Change Proposals

Two risk rating changes were proposed and approved during this meeting:

### Change 1: ZC-RISK-002 — Cloud Misconfiguration
- **Previous Rating:** High (Likelihood 3, Impact 5)
- **New Rating:** Medium (Likelihood 2, Impact 5)
- **Justification:** Improved controls — Wiz CSPM and IaC scanning
- **Approved by:** Committee unanimous vote

### Change 2: ZC-RISK-015 — Phishing Attack
- **Previous Rating:** High (Likelihood 4, Impact 3)
- **New Rating:** Medium (Likelihood 2, Impact 3)
- **Justification:** Improved controls — FIDO2 MFA and security awareness training
- **Approved by:** Committee unanimous vote

---

## 4. Q4 Incident Summary

Rajesh provided a summary of Q4 security incidents:

- **Total Incidents:** 3 (1 Medium, 2 Low)
- **INC-2025-Q4-001 (Medium):** Unauthorized access attempt to staging environment via compromised developer API key. Detected by Datadog anomaly detection within 4 minutes. Key revoked, no data access confirmed. Root cause: developer committed API key to public GitHub repository.
- **INC-2025-Q4-002 (Low):** False positive WAF block affecting legitimate customer traffic for 12 minutes. WAF rule tuned.
- **INC-2025-Q4-003 (Low):** Employee laptop lost during travel. Laptop was encrypted (FileVault), remote wiped within 2 hours. No data exposure.

No incidents triggered risk rating changes.

---

## 5. Emerging Risk Discussion

Maria Santos (Independent Risk Advisor) led a brief discussion on emerging risks:

- **AI-Powered Attack Vectors:** Noted increasing sophistication of AI-generated phishing and social engineering. Committee acknowledged this is partially addressed by FIDO2 MFA but noted the need to monitor.
- **Regulatory Landscape:** David Cho noted upcoming EU AI Act requirements and potential US federal privacy legislation. No immediate action required but monitoring continues.

**Note:** No formal emerging risk assessment was conducted during this meeting. Maria recommended scheduling a dedicated emerging risk workshop in Q1 2026 to address AI-specific threats, supply chain resilience in the context of geopolitical tensions, and quantum computing readiness.

---

## 6. Action Items

| # | Action Item | Owner | Due Date |
|---|-------------|-------|----------|
| 1 | Complete runbook documentation (target 100%) | Tom Harrington | March 31, 2026 |
| 2 | Finalize AI governance policy | Susan Park | February 28, 2026 |
| 3 | Schedule Q1 2026 emerging risk workshop | Linda Okafor | January 31, 2026 |
| 4 | Conduct Q1 2026 comprehensive risk assessment | Linda Okafor | March 15, 2026 |
| 5 | Present semi-annual risk report to Audit Committee | Linda Okafor | January 2026 |

---

## Next Meeting

Q1 2026 SGC Quarterly Meeting — Scheduled for March 2026

---

*Minutes prepared by: Linda Okafor, CRO*  
*Minutes approved by: All SGC members — December 20, 2025*
