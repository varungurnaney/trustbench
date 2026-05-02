# Zenith Cloud — Enterprise Risk Management Framework

**Document ID:** ZC-GRC-POL-003  
**Version:** 4.1  
**Effective Date:** February 1, 2025  
**Last Reviewed:** February 1, 2025  
**Owner:** Linda Okafor, Chief Risk Officer  
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy establishes the enterprise risk management (ERM) framework for Zenith Cloud Inc., ensuring that risks to the organization's objectives, operations, and information systems are systematically identified, assessed, treated, monitored, and reported. This framework supports compliance with SOC 2 Trust Services Criteria CC3.1 (Risk Identification and Assessment).

## 2. Scope

This policy applies to all Zenith Cloud business units, information systems, third-party relationships, and personnel. It covers operational, strategic, compliance, financial, and information security risks.

## 3. Risk Appetite Statement

Zenith Cloud maintains a **moderate** risk appetite for operational and strategic risks, and a **low** risk appetite for information security and compliance risks. Specifically:

- **Information Security Risks:** Zenith Cloud will not accept risks rated **Critical** without explicit Board of Directors approval. **High** risks require CISO and CRO joint approval with documented compensating controls.
- **Compliance Risks:** Zero tolerance for known regulatory violations. Identified compliance gaps must be remediated within 90 days.
- **Operational Risks:** Moderate appetite, balanced against business objectives. Service availability targets of 99.95% inform acceptable operational risk levels.
- **Strategic Risks:** Moderate appetite, evaluated quarterly against business growth targets.

## 4. Risk Assessment Methodology

### 4.1 Risk Rating Matrix

Zenith Cloud uses a 5x5 likelihood-impact matrix:

**Likelihood Scale:**
| Rating | Description | Probability |
|--------|-------------|-------------|
| 1 — Rare | Unlikely to occur within 3 years | <5% |
| 2 — Unlikely | Could occur within 2-3 years | 5-20% |
| 3 — Possible | Could occur within 1-2 years | 20-50% |
| 4 — Likely | Expected to occur within 1 year | 50-80% |
| 5 — Almost Certain | Expected to occur within 6 months | >80% |

**Impact Scale:**
| Rating | Description | Financial Impact | Operational Impact |
|--------|-------------|-----------------|-------------------|
| 1 — Negligible | Minimal impact | <$10K | No service impact |
| 2 — Minor | Limited impact | $10K-$100K | <1 hour service degradation |
| 3 — Moderate | Noticeable impact | $100K-$1M | 1-8 hours service degradation |
| 4 — Major | Significant impact | $1M-$10M | 8-48 hours service outage |
| 5 — Catastrophic | Severe, potentially existential | >$10M | >48 hours outage, data breach, regulatory action |

**Risk Rating Calculation:**

| | Impact 1 | Impact 2 | Impact 3 | Impact 4 | Impact 5 |
|---|---------|---------|---------|---------|---------|
| **Likelihood 5** | Medium | High | High | Critical | Critical |
| **Likelihood 4** | Medium | Medium | High | High | Critical |
| **Likelihood 3** | Low | Medium | Medium | High | High |
| **Likelihood 2** | Low | Low | Medium | Medium | Medium |
| **Likelihood 1** | Low | Low | Low | Medium | Medium |

### 4.2 Assessment Frequency

- **Comprehensive Risk Assessment:** Conducted **annually**, typically in Q1, covering all identified risk domains. The comprehensive assessment includes interviews with business unit leaders, threat landscape analysis, and control effectiveness evaluation.
- **Quarterly Risk Reviews:** The Security Governance Committee (SGC) conducts quarterly reviews of the risk register to identify changes in risk levels, new risks, and control effectiveness.
- **Event-Driven Assessments:** Triggered by significant events including security incidents, major architecture changes, regulatory changes, M&A activity, or significant market shifts.

### 4.3 Risk Register Requirements

The risk register must contain, at minimum:
- Unique risk identifier
- Risk title and description
- Risk owner (named individual)
- Likelihood and impact ratings (pre- and post-control)
- Current risk rating
- Treatment strategy (Accept, Mitigate, Transfer, Avoid)
- Assigned controls and their effectiveness
- Residual risk rating
- Review date and next review date
- Change history with justification for any rating changes

## 5. Risk Treatment

### 5.1 Treatment Strategies

| Strategy | When Applied | Approval Required |
|----------|-------------|-------------------|
| **Accept** | Residual risk within appetite; cost of mitigation exceeds risk impact | CRO for Medium; CISO + CRO for High; Board for Critical |
| **Mitigate** | Controls can reduce risk to acceptable levels | Risk Owner |
| **Transfer** | Risk can be shifted via insurance or contract | CRO + CFO |
| **Avoid** | Activity creating the risk can be eliminated | Business Unit VP + CRO |

### 5.2 Rating Change Requirements

Any change to a risk's likelihood or impact rating MUST include:
- Documented justification referencing specific control changes, threat intelligence, or incident data
- Before/after comparison of the risk rating
- Approval from the risk owner and the CRO
- Review by the SGC at the next quarterly meeting

## 6. Governance and Reporting

### 6.1 Security Governance Committee (SGC)

The SGC meets quarterly and is responsible for:
- Reviewing the risk register and approving rating changes
- Evaluating risk treatment progress
- Identifying emerging risks
- Reporting to the Board's Audit Committee on risk posture

**SGC Members:**
- Linda Okafor, Chief Risk Officer (Chair)
- Rajesh Mehta, CISO
- Tom Harrington, VP Engineering
- Susan Park, VP Product
- David Cho, General Counsel
- External: Maria Santos, Independent Risk Advisor

### 6.2 Board Reporting

The CRO presents a risk summary to the Board's Audit Committee semi-annually, including:
- Top 10 risks by residual rating
- Risk trend analysis
- Emerging risk landscape
- Compliance risk status

## 7. Emerging Risk Identification

Zenith Cloud maintains an emerging risk identification process that includes:
- Quarterly threat landscape briefings from external intelligence providers
- Industry peer benchmarking through ISAC membership
- Technology horizon scanning for new threat vectors
- Regulatory change monitoring

---

*Approved by: Board of Directors — January 28, 2025*
