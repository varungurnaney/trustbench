# Third-Party Vendor Risk Management Policy

**Document ID:** POL-VRM-004
**Version:** 2.8
**Effective Date:** January 15, 2025
**Owner:** Security & Compliance
**Approved By:** Elena Vasquez, CISO

---

## 1. Purpose

This policy establishes requirements for managing third-party vendor risks at Arctura Systems Inc., ensuring that vendor relationships do not introduce unacceptable risk to company or customer data.

## 2. Vendor Classification

| Tier | Criteria | Assessment Requirements |
|------|----------|------------------------|
| Critical | Processes customer PII, has production access, or provides core infrastructure | Annual SOC 2 review, annual security questionnaire, quarterly business review |
| High | Accesses customer data (including pseudonymized), integrates with production | Annual SOC 2 review, biennial security questionnaire |
| Medium | Accesses internal systems only | Security questionnaire at onboarding, biennial review |
| Low | No system or data access | Contractual review only |

## 3. Data Processing Agreements

### 3.1 Requirement

A Data Processing Agreement (DPA) must be executed before granting any vendor access to personal data. This applies to all vendors classified as Critical or High tier, and any Medium or Low tier vendor that processes personal data.

### 3.2 DPA Contents

All DPAs must specify:
- Categories of personal data processed
- Purpose of processing
- Data subject categories
- Data retention and deletion requirements
- Sub-processor notification obligations
- Data breach notification within 72 hours

### 3.3 DPA Tracking

The Security & Compliance team maintains a DPA tracker documenting all executed agreements, renewal dates, and amendment history.

## 4. Ongoing Monitoring

### 4.1 SOC 2 Report Review

- Critical vendors: SOC 2 Type II report reviewed annually within 90 days of issuance.
- High vendors: SOC 2 Type II report reviewed annually within 120 days.

### 4.2 Business Reviews

- Critical vendors: quarterly business review.
- High vendors: semi-annual business review.

## 5. Contractual Requirements

All vendor contracts must include:
- Data protection and privacy obligations
- Right to audit
- Security incident notification within 72 hours
- Data return or destruction on termination

## 6. Vendor Offboarding

- Access revoked within 5 business days
- Data return/destruction confirmed in writing
- DPA tracker updated

---

**Next Review Date:** January 2026
