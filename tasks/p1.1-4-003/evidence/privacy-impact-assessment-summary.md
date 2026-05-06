# Verdant Fintech — Privacy Impact Assessment Summary

**Prepared by:** Privacy Team
**Last Updated:** December 2025
**PIA Policy Reference:** All privacy impact assessments are reviewed annually per Verdant Fintech Privacy Governance Framework v1.2 (PGF-2023-001).

---

## PIA Register

### PIA-2025-001: Core Platform Data Processing
- **Scope:** Collection and processing of user account data, financial profiles, and usage analytics through the Verdant platform
- **Assessment Date:** January 15, 2025
- **Next Review Date:** January 15, 2026
- **Assessor:** Lisa Chen (Privacy Counsel)
- **Risk Rating:** Medium
- **Key Risks Identified:**
  - Financial profile data (income, goals, risk tolerance) is sensitive and requires enhanced access controls
  - Usage analytics may create detailed behavioral profiles — mitigated by data minimization practices
  - User-generated financial data (budgets, goals) is highly personal
- **Mitigations Applied:**
  - Role-based access control limiting financial data access to authorized personnel only
  - Data minimization: only collect data necessary for requested features
  - Encryption at rest (AES-256) for all financial data
  - Quarterly access reviews for financial data systems
- **Status:** Current

### PIA-2025-002: Plaid Bank Account Aggregation Integration
- **Scope:** Integration with Plaid for bank account linking, credential handling, and transaction data retrieval
- **Assessment Date:** October 12, 2023
- **Next Review Date:** October 12, 2024
- **Assessor:** David Park (Privacy Analyst)
- **Risk Rating:** High
- **Key Risks Identified:**
  - Bank credential transmission through Plaid Link creates significant data exposure risk
  - Persistent OAuth token storage enables ongoing data access without re-authentication
  - Transaction history (12 months) provides comprehensive financial behavioral profile
  - Plaid sub-processor chain creates extended data exposure surface
  - Loss or compromise of Plaid integration credentials could expose all linked accounts
- **Mitigations Applied:**
  - Plaid Link SDK handles credential entry (credentials never touch Verdant servers)
  - OAuth tokens encrypted with HSM-managed keys
  - Transaction data refreshed daily but only 12-month window retained
  - Plaid SOC 2 Type II report reviewed annually
  - Incident response plan includes Plaid credential rotation procedures
- **Status:** OVERDUE FOR REVIEW — last assessed October 2023, review due October 2024. Review has not been completed as of December 2025.

### PIA-2025-003: Experian Credit Score Integration
- **Scope:** Collection of SSN and transmission to Experian for credit score retrieval and ongoing monitoring
- **Assessment Date:** August 1, 2024
- **Next Review Date:** August 1, 2025
- **Assessor:** Lisa Chen (Privacy Counsel)
- **Risk Rating:** High
- **Key Risks Identified:**
  - SSN collected at credit check enrollment and transmitted to Experian via encrypted API
  - SSN stored in Verdant HSM-encrypted database for ongoing credit monitoring
  - SSN is the highest-sensitivity PII element processed by Verdant
  - Compromise of SSN storage would constitute a critical breach
  - Regulatory requirements vary by state for SSN handling
- **Mitigations Applied:**
  - SSN encrypted with dedicated HSM key (separate from general encryption keys)
  - Access to SSN data limited to 3 named individuals with MFA + approval workflow
  - SSN transmitted to Experian via mTLS with certificate pinning
  - SSN masked in all logs and support tools (only last 4 digits visible)
  - Breach notification plan specific to SSN exposure drafted
- **Status:** Review due August 2025 — review initiated but not yet completed as of December 2025. Review in progress by Lisa Chen.

### PIA-2025-004: Braze Marketing Automation Integration
- **Scope:** Sharing of user profile and financial behavioral data with Braze for marketing campaign targeting
- **Assessment Date:** February 1, 2025
- **Next Review Date:** February 1, 2026
- **Assessor:** David Park (Privacy Analyst)
- **Risk Rating:** Medium
- **Key Risks Identified:**
  - Financial goal data and behavioral segments shared with Braze create detailed financial profiles in a marketing platform
  - Segments like 'high-saver' and 'investment-curious' derived from financial data could be used for inappropriate targeting
  - Braze data retention may exceed Verdant's retention policies
  - Financial behavioral data in a marketing context may surprise users who did not expect financial data used for marketing
- **Mitigations Applied:**
  - Financial amounts not shared (only goal categories, not specific dollar amounts)
  - Braze data retention aligned with Verdant retention schedule via DPA
  - Marketing consent required before email campaigns
  - Segment definitions reviewed quarterly by Privacy Team
- **Status:** Current

### PIA-2025-005: Internal Analytics Pipeline
- **Scope:** Processing of anonymized usage analytics for product improvement and business intelligence
- **Assessment Date:** March 15, 2025
- **Next Review Date:** March 15, 2026
- **Assessor:** David Park (Privacy Analyst)
- **Risk Rating:** Low
- **Key Risks Identified:**
  - Re-identification risk from granular usage data combined with financial profiles
  - Analytics data retained longer than primary data (see retention schedule)
- **Mitigations Applied:**
  - User IDs replaced with pseudonymous identifiers in analytics pipeline
  - k-anonymity checks on exported analytics datasets
  - Access limited to data team (5 individuals)
- **Status:** Current
