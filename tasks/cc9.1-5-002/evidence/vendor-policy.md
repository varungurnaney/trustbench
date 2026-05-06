# Vendor Risk Management Policy

**Document ID:** POL-VRM-007
**Version:** 3.2
**Effective Date:** January 1, 2025
**Owner:** Governance, Risk & Compliance
**Approved By:** Lakshmi Patel, CISO

---

## 1. Purpose

This policy establishes the vendor risk management framework for Vega Solutions Inc. to ensure third-party vendor relationships are managed in accordance with SOC 2 Trust Services Criteria and organizational risk appetite.

## 2. Vendor Classification

| Tier | Criteria | Assessment Requirements |
|------|----------|------------------------|
| Critical | Processes customer PII, has production access, or provides core infrastructure | Annual SOC 2 review within 90 days of issuance, annual security assessment, quarterly business review |
| High | Accesses internal data, integrates with production systems | Annual SOC 2 review within 120 days of issuance, biennial security questionnaire |
| Medium | Accesses internal systems with no customer data | Security questionnaire at onboarding |
| Low | No system or data access | Contractual review only |

## 3. Onboarding

Before granting vendor access:
- Security questionnaire completed and reviewed
- DPA executed (if processing personal data)
- SOC 2 report reviewed (Critical and High)
- Initial risk assessment completed (Critical)
- Vendor registered in Vanta

## 4. Ongoing Monitoring

### 4.1 SOC 2 Report Review

- Critical vendors: SOC 2 report reviewed annually within 90 days of report issuance.
- High vendors: SOC 2 report reviewed annually within 120 days of report issuance.
- Reviews must document: scope adequacy, opinion type, qualified opinions, CUECs, subservice organizations, and exceptions.

### 4.2 CUEC Validation

Complementary User Entity Controls (CUECs) identified in vendor SOC 2 reports must be validated by the relevant internal team within 30 days of SOC 2 review completion. Validation results must be documented in the SOC 2 review tracker.

### 4.3 Qualified Opinion Handling

Reports with qualified opinions require a formal risk assessment within 30 days of review, documenting:
- Nature of the qualification
- Potential impact on Vega Solutions data and operations
- Compensating controls in place at Vega Solutions
- Vendor remediation commitments and timeline
- Risk acceptance or remediation requirements

### 4.4 Business Reviews

- Critical vendors: quarterly business review covering SLA performance, incident history, and security posture.
- High vendors: semi-annual business review.

## 5. Contractual Requirements

All vendor contracts must include:
- Data protection and privacy obligations
- Right to audit
- Incident notification within 72 hours
- Data return/destruction on termination
- Cyber insurance (Critical and High)

## 6. Vendor Offboarding

- Access revoked within 5 business days
- Data return/destruction confirmed in writing
- Documented in Vanta

---

**Next Review Date:** January 2026
