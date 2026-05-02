# Vertex AI Corp -- Annual Risk Assessment Report 2025

**Document ID:** VAC-RSK-AR-2025  
**Version:** 1.0  
**Assessment Period:** January - February 2025  
**Report Date:** March 15, 2025  
**Prepared By:** Rajesh Patel, Chief Risk Officer  
**Reviewed By:** Elena Vasquez, CISO  
**Approved By:** Security Governance Committee (SGC), March 28, 2025  

---

## 1. Executive Summary

This report presents the findings of Vertex AI Corp's 2025 Annual Risk Assessment, conducted in accordance with the Risk Management Policy (VAC-POL-RSK-003). The assessment covered 15 risk categories across the organization and identified 18 risks requiring active management.

Key highlights:
- 2 risks classified as Critical (RISK-006: Ransomware, RISK-014: Cross-border data transfer)
- 7 risks classified as High
- 6 risks classified as Medium
- 3 risks classified as Low (not included in active register)
- Overall risk posture: **Moderate** (improved from Elevated in 2024)

## 2. Assessment Methodology

### 2.1 Approach

The risk assessment employed a combination of:
- Structured interviews with business unit leaders and technical leads
- Review of incident data from the previous 12 months
- Threat intelligence analysis (CrowdStrike Intelligence, CISA advisories)
- Industry benchmarking (Verizon DBIR 2024, IBM Cost of a Data Breach 2024)
- Review of regulatory landscape changes
- Control effectiveness testing results

### 2.2 Participants

| Name | Role | Department |
|------|------|------------|
| Elena Vasquez | CISO | Information Security |
| Rajesh Patel | CRO | Risk Management |
| Thomas Wright | VP Engineering | Engineering |
| Amara Osei | VP Product | Product |
| Patricia Holloway | General Counsel | Legal |
| Robert Tanaka | CFO | Finance |
| David Kim | Director of IT | IT Operations |
| Sarah Chen | SOC Manager | Security Operations |
| Michael Torres | Head of Compliance | Compliance |

## 3. Risk Categories Assessed

The following 15 risk categories were evaluated in this assessment:

### 3.1 Information Security Risks
- **Unauthorized Access:** Risk of unauthorized access to systems and data through compromised credentials, privilege escalation, or access control failures
- **Data Breach / Exfiltration:** Risk of sensitive data being accessed or exfiltrated by external or internal threat actors
- **Malware / Ransomware:** Risk of malware infection impacting system availability and data integrity
- **Phishing / Social Engineering:** Risk of credential compromise through phishing campaigns or social engineering attacks
- **Cloud Security:** Risk of data exposure or service disruption due to cloud misconfigurations

### 3.2 Technology Risks
- **Infrastructure Failure:** Risk of production system outages due to hardware, software, or network failures
- **Software Vulnerabilities:** Risk of exploitation of known or zero-day vulnerabilities in applications and infrastructure
- **Database / Performance:** Risk of system performance degradation impacting service availability
- **API Security:** Risk of API-related vulnerabilities or single points of failure

### 3.3 Regulatory and Compliance Risks
- **Data Privacy (GDPR/CCPA):** Risk of non-compliance with data privacy regulations
- **Cross-Border Data Transfer:** Risk of regulatory action related to international data transfers

### 3.4 Operational Risks
- **Incident Response:** Risk of inadequate incident response capability
- **Business Email Compromise:** Risk of financial fraud through email-based attacks
- **Key Personnel:** Risk of knowledge loss due to staff turnover

### 3.5 Third-Party Risks
- **Vendor Risk:** Risk of vendor service disruption or data breach impacting Vertex AI Corp

## 4. Key Findings

### 4.1 Critical Risks

**RISK-006: Ransomware Attack**
- Likelihood: 4 (Likely) | Impact: 5 (Catastrophic) | Rating: 20 (Critical)
- Rationale: Increased targeting of AI/ML companies observed in threat intelligence. Vertex AI Corp's data assets (training datasets, model weights, customer data) are high-value targets.
- Treatment: Multi-layered defense strategy including EDR, network segmentation, immutable backups, and Mandiant IR retainer.

**RISK-014: Cross-Border Data Transfer Compliance**
- Likelihood: 4 (Likely) | Impact: 5 (Catastrophic) | Rating: 20 (Critical)
- Rationale: Ongoing regulatory uncertainty post-Schrems II. EU customers represent 30% of revenue. New EU-US Data Privacy Framework may face legal challenges.
- Treatment: Risk accepted with CISO and Board approval. SCCs and supplementary measures in place. Insurance coverage for regulatory fines.

### 4.2 Emerging Trends

1. **Ransomware-as-a-Service (RaaS)** groups increasingly targeting technology companies
2. **Cloud misconfiguration** remains a leading cause of data breaches
3. **Regulatory fragmentation** across US states creating compliance complexity
4. **Third-party risk** amplified by interconnected supply chains

## 5. Risk Treatment Summary

| Classification | Count | Mitigate | Transfer | Accept | Avoid |
|---------------|-------|----------|----------|--------|-------|
| Critical | 2 | 1 | 0 | 1 | 0 |
| High | 7 | 7 | 0 | 0 | 0 |
| Medium | 6 | 6 | 0 | 0 | 0 |
| **Total** | **15** | **14** | **0** | **1** | **0** |

Note: RISK-005 (Vendor Disruption) uses a combined Mitigate + Transfer strategy.

## 6. Comparison to Prior Year

| Metric | 2024 | 2025 | Trend |
|--------|------|------|-------|
| Total Active Risks | 14 | 18 | +4 new risks identified |
| Critical Risks | 1 | 2 | +1 (added RISK-014) |
| High Risks | 6 | 7 | +1 |
| Risks with Active Treatment | 12 | 15 | +3 |
| Average Risk Score | 11.2 | 10.8 | Slight improvement |

## 7. Recommendations

1. Increase frequency of ransomware tabletop exercises to monthly for the incident response team
2. Implement additional cloud configuration guardrails through infrastructure-as-code policies
3. Complete vendor security assessment cycle for all critical vendors by Q2 2025
4. Enhance key personnel risk mitigation through expanded cross-training program
5. Monitor EU regulatory developments regarding the EU-US Data Privacy Framework
6. Evaluate cyber insurance coverage adequacy given increased risk profile

## 8. Next Steps

- Q2 2025: Implement SGC-approved treatment plan updates
- Q3 2025: Mid-year risk register review
- Q4 2025: Quarterly SGC risk review
- Q1 2026: Next annual risk assessment

## 9. Approval

| Name | Role | Date | Signature |
|------|------|------|-----------|
| Rajesh Patel | CRO | 2025-03-15 | Approved |
| Elena Vasquez | CISO | 2025-03-20 | Approved |
| SGC Members | Committee | 2025-03-28 | Unanimously Approved |

---

*Document Classification: Internal -- Confidential*
