# Third-Party Vendor Risk Management Policy

**Document ID:** POL-VRM-005
**Version:** 3.0
**Effective Date:** March 1, 2025
**Owner:** Security & Compliance
**Approved By:** Marcus Webb, CISO

---

## 1. Purpose

This policy establishes requirements for assessing, monitoring, and managing risks associated with third-party vendors at Prism Data Inc.

## 2. Vendor Classification

| Tier | Criteria | Assessment Requirements |
|------|----------|------------------------|
| Critical | Processes customer PII, has production access, or provides core infrastructure | Annual SOC 2 Type II review, annual security assessment, quarterly business review |
| High | Accesses internal data, integrates with production systems, or processes security-sensitive data | Annual SOC 2 Type II (or equivalent) review, annual security questionnaire |
| Medium | Accesses internal systems with no customer data | Security questionnaire at onboarding, biennial review |
| Low | No system access, no data access | Contractual review only |

## 3. Onboarding Requirements

Before granting a vendor access to any system or data:
- Security questionnaire completed and reviewed
- Data Processing Agreement (DPA) executed
- SOC 2 Type II report reviewed (Critical and High tier)
- Vendor registered in Vanta
- Risk tier assigned and documented

## 4. Ongoing Monitoring

### 4.1 SOC 2 Report Review

- Critical vendors: SOC 2 report reviewed annually within 90 days of issuance.
- High vendors: SOC 2 report reviewed annually within 120 days of issuance.
- Reports with qualified opinions require risk assessment.

### 4.2 Business Reviews

- Critical vendors: quarterly business review covering SLA performance, incident history, and security posture.
- Business reviews documented in Vanta.

### 4.3 Exception Process

Vendors that cannot provide a SOC 2 report may be granted an exception by the CISO. Exceptions must document:
- Reason for the exception
- Compensating controls in place
- Risk assessment
- Expiration date (maximum 6 months)
- Renewal requirements

Expired exceptions must be renewed or the vendor must provide the required assessment before continued operation.

## 5. Contractual Requirements

All vendor contracts must include:
- Data protection and privacy obligations
- Right to audit
- Incident notification within 72 hours
- Data return/destruction on termination
- Insurance requirements (Critical/High tier)

---

**Next Review Date:** March 2026
