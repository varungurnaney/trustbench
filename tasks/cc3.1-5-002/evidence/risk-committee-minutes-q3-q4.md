# Risk Committee Meeting Minutes

---

## Q3 2025 Meeting -- July 1, 2025

**Attendees:** Diane Crawford (CISO), Brian Nakamura (CRO), Angela Torres (VP Eng), Samuel Osei (GC), Katherine Park (CFO)
**Quorum:** Met (5/5)

### Agenda Items

**1. Risk Register Review**

Reviewed all 12 risks. Key discussions:

- **PC-RISK-003 (Ransomware):** Brian flagged that the residual rating of 12 (High) exceeds the information security risk appetite of Medium (≤9). This represents an appetite breach. The CrowdStrike EDR and immutable backups reduce impact but the likelihood remains elevated (residual likelihood = 3). Diane proposed deploying Illumio micro-segmentation to reduce lateral movement risk, which should reduce residual likelihood from 3 to 2, bringing the residual rating to 8 (within appetite).
  - **Action:** Angela to procure and deploy Illumio. Target completion: Q4 2025.
  - **Status:** Appetite breach acknowledged. Remediation plan approved.

- **PC-RISK-005 (GDPR DSR compliance):** Samuel reported that the residual rating of 6 (Medium) exceeds the compliance appetite of Low (≤4). The automated DSR portal works but manual data discovery steps introduce accuracy risk. Proposed solution: deploy BigID automated data discovery to improve response completeness.
  - **Action:** Samuel to initiate BigID procurement. Target completion: Q3 2025.
  - **Status:** Appetite breach acknowledged. Remediation plan approved.

- **PC-RISK-008 (Phishing):** Noted residual rating of 9 is at the upper boundary of the Medium (≤9) appetite threshold. Diane recommended monitoring closely. Click rate trending down but still above 3%.

**2. Emerging Risks**
- AI-powered phishing attacks discussed. No new risk added at this time -- monitoring through ISAC intelligence feeds.

---

## Q4 2025 Meeting -- October 8, 2025

**Attendees:** Diane Crawford (CISO), Brian Nakamura (CRO), Angela Torres (VP Eng), Samuel Osei (GC), Katherine Park (CFO)
**Quorum:** Met (5/5)

### Agenda Items

**1. Risk Register Review**

Reviewed all 12 risks. Key discussions:

- **PC-RISK-003 (Ransomware) -- Appetite Breach Update:** Angela reported that Illumio micro-segmentation deployment is delayed. Vendor implementation team has a backlog and cannot begin installation until January 2026. Residual rating remains 12 (High), still exceeding appetite. Brian asked if this constitutes a second quarter of appetite breach without resolution. Diane confirmed it does. Brian recommended either: (a) request a formal exception per policy Section 3.4, or (b) escalate to the Board. Diane stated she believes the delay is temporary and a formal exception is premature given the active remediation plan. The committee agreed to continue monitoring and revisit at the Q1 2026 meeting. No formal exception was requested. No Board escalation was initiated.

- **PC-RISK-005 (GDPR DSR) -- Appetite Breach Update:** Samuel reported that BigID contract negotiations are taking longer than expected. The procurement team is negotiating enterprise licensing terms. No deployment date yet. Residual rating remains 6 (Medium), still exceeding compliance appetite of Low (≤4). This is the second consecutive quarter of appetite breach for this risk. Brian noted that per policy Section 3.4, if not remediated within one quarter, the Risk Committee must either approve a formal exception or escalate to the Board. Samuel stated he expects the contract to be signed by end of November. Katherine asked whether the 60-day compliance risk remediation window (Section 3.2) has been exceeded. Samuel confirmed the appetite breach was first identified in Q2 (April 15) and it is now October — approximately 6 months. No formal exception was requested. No Board escalation was initiated.

- **PC-RISK-008 (Phishing):** Residual rating remains 9. Click rate improved to 3.1%. At the boundary of appetite threshold. No action required.

**2. Emerging Risks**
- Discussed potential HIPAA 2.0 rulemaking. Samuel to monitor.
- AI deepfake voice phishing noted as emerging threat. Diane to assess.

---

## Q4 2025 Ad Hoc Update -- December 15, 2025

**Format:** Email update from CRO to Risk Committee members (not a formal meeting)

**Subject:** Q4 2025 Risk Register Status Update

> Team -- Quick update on the two appetite breaches:
>
> **PC-RISK-003 (Ransomware):** Illumio contract signed December 1. Implementation kickoff scheduled January 8, 2026. Expected deployment completion: March 2026. Residual rating remains 12. Appetite breach now in its third quarter.
>
> **PC-RISK-005 (GDPR DSR):** BigID contract signed November 28. Deployment kickoff scheduled January 15, 2026. Expected deployment completion: February 2026. Residual rating remains 6. Appetite breach now in its third quarter (since Q2 2025).
>
> Both remain unresolved heading into Q1 2026. I recommend we discuss formal exceptions or Board escalation at the Q1 2026 Risk Committee meeting.
>
> — Brian Nakamura, CRO
