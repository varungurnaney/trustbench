# Vendor Risk Management Policy

**Document ID:** POL-VRM-008
**Version:** 3.5
**Effective Date:** January 15, 2025
**Owner:** Security & Compliance
**Approved By:** Robert Tanaka, CISO

---

## 1. Purpose

This policy defines the vendor risk management framework for NovaBridge Inc. with emphasis on subservice organization monitoring and third-party risk mitigation.

## 2. Vendor Classification

| Tier | Criteria | Assessment Requirements |
|------|----------|------------------------|
| Critical | Processes customer PII, has production access, or provides core infrastructure | Annual SOC 2 review, quarterly business review, annual security assessment |
| High | Accesses customer data (including pseudonymized), integrates with production systems | Annual SOC 2 review, semi-annual business review |
| Medium | Accesses internal systems only | Security questionnaire at onboarding, biennial review |
| Low | No system or data access | Contractual review only |

## 3. Onboarding

Before granting vendor access:
- Security questionnaire completed
- DPA executed (if processing personal data)
- SOC 2 report reviewed (Critical and High)
- Subservice organizations identified and assessed
- Risk tier assigned

## 4. Subservice Organization Monitoring

### 4.1 Subservice Organization Identification

During each SOC 2 report review, the reviewer must identify all subservice organizations listed in the vendor's report and compare them against the vendor inventory. Any discrepancies must be investigated.

### 4.2 Change Notification Requirements

Vendor contracts require notification of subservice organization changes within 30 days. This includes:
- Addition of new subservice organizations
- Removal of existing subservice organizations
- Changes in the method of presenting subservice organizations (inclusive vs. carve-out)

### 4.3 Independent Assessment of Carved-Out Subservice Organizations

When a vendor's SOC 2 report uses the carve-out method for a subservice organization, NovaBridge must independently assess the carved-out subservice organization within 60 days of identification. Assessment options include:
- Reviewing the subservice organization's own SOC 2 report
- Conducting a security questionnaire with the subservice org
- Leveraging NovaBridge's own direct assessment (if NovaBridge is also a customer of the subservice org)

### 4.4 SOC 2 Report Review

- Critical vendors: SOC 2 report reviewed annually within 90 days of issuance.
- High vendors: SOC 2 report reviewed annually within 120 days of issuance.

## 5. Contractual Requirements

All vendor contracts must include:
- Data protection obligations
- Right to audit
- Subservice organization change notification within 30 days
- Incident notification within 72 hours
- Data return/destruction on termination

---

**Next Review Date:** January 2026
