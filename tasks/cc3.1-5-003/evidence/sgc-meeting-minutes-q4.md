# SGC Meeting Minutes -- Q4 2025

**Date:** October 15, 2025
**Attendees:** Priya Sharma (CISO), David Chen (CRO), Rebecca Liu (VP Eng), James Okafor (GC), Dr. Anna Kowalski (Independent Risk Advisor)
**Quorum:** Met (5/5)

---

## 1. Risk Register Review

Reviewed all 12 risks in the register. All review dates are current. No overdue reviews. Key updates:

- CD-RISK-003 (Ransomware): Tabletop exercise results presented. Detection time improved to 12 minutes. Treatment controls operating effectively.
- CD-RISK-007 (Cloud misconfiguration): Wiz auto-remediated 6 misconfigurations in Q4. No manual intervention required.
- CD-RISK-008 (Phishing): Click rate down to 2.7% from 4.1% in Q3. FIDO2 MFA rollout 92% complete.

No rating changes proposed. All risks within appetite thresholds.

## 2. Emerging Risk Discussion

Priya raised several emerging risk topics based on recent discussions in the #security-intel Slack channel:

### 2.1 AI-Powered Social Engineering

Priya noted that the security team has been monitoring AI-generated deepfake voice and video phishing attacks in the #security-intel Slack channel. Several team members shared threat intelligence articles and FS-ISAC advisories. Rebecca mentioned a customer inquiry about Cirrus Data's preparedness for AI-augmented attacks. Priya stated the team believes existing controls (KnowBe4 training, Proofpoint email filtering, FIDO2 MFA) provide reasonable protection but acknowledged that deepfake voice calls are a new vector not covered by current training scenarios.

**Decision:** No formal emerging risk assessment to be conducted at this time. Priya to ask the security team to add AI social engineering scenarios to the next KnowBe4 campaign. Topic to be monitored via Slack discussions.

### 2.2 Quantum Computing Threat to Cryptography

David shared an article from the #security-intel Slack channel about NIST post-quantum cryptography standards finalization. Rebecca noted that Cirrus Data uses AES-256 and RSA-2048 for data encryption. James asked whether quantum computing represents a near-term risk. Dr. Kowalski stated the consensus view is 5-10 year timeline for cryptographically relevant quantum computers but recommended beginning a post-quantum readiness assessment.

**Decision:** No formal risk assessment at this time. Rebecca to assign a security architect to review NIST PQC standards and prepare a brief for Q1 2026. Not added to risk register.

### 2.3 EU AI Act Compliance Implications

James noted that the EU AI Act entered into force in August 2024 with phased compliance dates. Several Cirrus Data customers use the platform's analytics features for automated decision-making that could fall under the AI Act's high-risk classification. A thread in the #compliance-updates Slack channel discussed potential implications. James stated the legal team has reviewed the regulation at a high level but no formal impact assessment has been conducted.

**Decision:** James to monitor regulatory developments. No formal risk assessment initiated. Not added to risk register.

## 3. Formal Emerging Risk Documentation

Dr. Kowalski raised a concern about the emerging risk identification process. She noted that while the #security-intel and #compliance-updates Slack channels generate valuable discussion, the current practice does not align with the formal process documented in policy Section 6:

> "The policy requires quarterly threat intelligence briefings in a documented report format, technology horizon scanning as a formal semi-annual report, and formal risk assessments within 30 days of identification. What I'm seeing is informal Slack discussions with no documented threat intelligence report, no technology horizon scanning report, and no formal emerging risk assessments initiated despite identifying three substantive emerging risks today. The Slack discussions are a good input source, but they don't satisfy the documentation requirements in Section 6."

Priya acknowledged the gap and stated the team has been prioritizing operational work over formal documentation. She committed to producing a formal Threat Intelligence Briefing for Q1 2026 and asked David to draft a process for converting Slack-identified emerging risks into formal assessments.

David noted that the FS-ISAC industry risk survey (policy Section 6.1, item 4 — annual participation) was not completed in 2025 due to staffing constraints.

**Action Items:**
1. Priya: Produce formal Threat Intelligence Briefing for Q1 2026
2. David: Draft emerging risk conversion process (Slack → formal assessment)
3. Rebecca: Assign security architect for PQC readiness brief
4. James: EU AI Act monitoring — report back at Q1 2026 SGC
