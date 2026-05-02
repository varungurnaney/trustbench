# Third-Party Vendor Risk Management Policy

**Document ID:** POL-VRM-002
**Version:** 2.5
**Effective Date:** March 1, 2025
**Owner:** Security & Compliance

---

## 1. Purpose

This policy establishes requirements for assessing, monitoring, and managing risks associated with third-party vendors that access, process, or store Quantum SaaS Inc. data.

## 2. Vendor Classification

| Tier | Criteria | Assessment Requirements |
|------|----------|------------------------|
| Critical | Processes customer PII, has production access, or provides infrastructure | Annual SOC 2 Type II report review, annual security assessment, quarterly business review |
| High | Accesses internal data, integrates with production systems | Annual SOC 2 Type II (or equivalent) review, annual security questionnaire |
| Medium | Accesses internal systems with no customer data | Security questionnaire at onboarding, biennial review |
| Low | No system access, no data access | Contractual review only |

## 3. Onboarding Requirements

Before granting a vendor access to any system or data:
- Security questionnaire completed and reviewed
- Data Processing Agreement (DPA) or Business Associate Agreement (BAA) signed
- SOC 2 Type II report reviewed (Critical and High tier)
- Vendor registered in the vendor management platform (Vanta)
- Risk rating assigned and documented

## 4. Ongoing Monitoring

### 4.1 SOC 2 Report Review

- Critical vendors: SOC 2 Type II report reviewed annually within 90 days of report issuance.
- Report review must document: scope adequacy, any qualified opinions, complementary user entity controls (CUECs), subservice organizations, and exceptions or findings.
- Reports with qualified opinions or significant findings require risk assessment and remediation tracking.

### 4.2 Subservice Organization Monitoring

- Vendors using subservice organizations (e.g., cloud infrastructure providers) must disclose all subservice organizations.
- The inclusive method is preferred for SOC 2 reports. If carve-out method is used, Quantum must independently assess the subservice organization.
- Changes to subservice organizations must be communicated within 30 days.

### 4.3 Business Reviews

- Critical vendors: quarterly business review covering SLA performance, incident history, and security posture changes.
- Business reviews documented in Vanta.

## 5. Contractual Requirements

All vendor contracts must include:
- Data protection and privacy obligations
- Right to audit
- Incident notification within 72 hours
- Data return/destruction on termination
- Insurance requirements (for Critical/High tier)

## 6. Vendor Termination

- Upon vendor termination, all access is revoked within 5 business days.
- Vendor confirms data return/destruction in writing.
- Termination documented in Vanta.

---

**Approved by:** Natasha Okonkwo, CISO
**Next Review Date:** March 2026
