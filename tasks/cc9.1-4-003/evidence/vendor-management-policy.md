# Third-Party Vendor Risk Management Policy

**Document ID:** POL-VRM-006
**Version:** 2.4
**Effective Date:** February 15, 2025
**Owner:** Governance, Risk & Compliance
**Approved By:** Diane Kowalski, CISO

---

## 1. Purpose

This policy defines the vendor risk management framework for Solaris Tech Inc. to identify, assess, and mitigate risks arising from third-party vendor relationships.

## 2. Vendor Classification

| Tier | Criteria | Assessment Requirements |
|------|----------|------------------------|
| Critical | Processes customer PII, has production access, or provides core infrastructure | Annual SOC 2 review, annual risk assessment, quarterly business review |
| High | Accesses internal data, integrates with production systems, or processes operational data | Annual SOC 2 review, annual risk assessment, semi-annual business review |
| Medium | Accesses internal systems with no customer data | Security questionnaire at onboarding, biennial review |
| Low | No system or data access | Contractual review only |

## 3. Onboarding

Before engaging a vendor:
- Security questionnaire completed
- DPA executed (if processing personal data)
- SOC 2 report reviewed (Critical and High tier)
- Initial risk assessment completed
- Vendor registered in vendor management platform

## 4. Ongoing Monitoring

### 4.1 SOC 2 Report Review

- Critical and High vendors: SOC 2 report reviewed annually within 90 days of issuance.
- Reviews must document scope, opinion type, CUECs, and subservice organizations.

### 4.2 Business Reviews

- Critical vendors: quarterly business review.
- High vendors: semi-annual business review.

### 4.3 Annual Risk Assessments

All Critical and High tier vendors shall undergo an annual risk assessment. The assessment must evaluate:
- Data access scope and sensitivity
- Security control effectiveness
- Incident history
- Financial stability
- Regulatory compliance posture

### 4.4 Scope Change Reassessment

When a vendor's data access, system integration, or service scope changes materially, a risk assessment refresh must be completed within 30 days of the scope change. Material changes include:
- Access to new data categories (e.g., internal-only to customer data)
- New system integrations
- Geographic expansion of data processing
- Changes to subservice organizations

## 5. Contractual Requirements

All vendor contracts must include:
- Data protection obligations
- Right to audit
- Incident notification within 72 hours
- Data return/destruction on termination

---

**Next Review Date:** February 2026
