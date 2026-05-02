# Onyx Data — Vendor Risk Management Policy

**Document ID:** OD-GRC-POL-007  
**Version:** 2.4  
**Effective Date:** March 1, 2025  
**Last Reviewed:** March 1, 2025  
**Owner:** Angela Torres, VP of Governance, Risk & Compliance  
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy establishes the vendor risk management framework for Onyx Data Inc., ensuring that risks associated with third-party service providers are identified, assessed, monitored, and mitigated in accordance with SOC 2 Trust Services Criteria CC9.1. All vendors that process, store, or transmit Onyx Data customer information, or that provide critical infrastructure services, are subject to this policy.

## 2. Scope

This policy applies to all third-party vendors, service providers, contractors, and business partners that:
- Process, store, or access Onyx Data customer data
- Provide critical infrastructure services (hosting, networking, authentication)
- Have logical or physical access to Onyx Data systems
- Provide software components integrated into Onyx Data products

## 3. Vendor Classification

Vendors are classified into tiers based on data access and operational criticality:

| Tier | Criteria | Examples |
|------|----------|---------|
| **Critical** | Processes customer PII/financial data; single point of failure for core service delivery; >$500K annual spend | Cloud infrastructure, payment processors, primary database providers |
| **High** | Accesses customer metadata or aggregated data; supports important but not mission-critical functions | Analytics platforms, monitoring tools, CDN providers |
| **Medium** | Limited or no customer data access; supports internal operations | HR systems, collaboration tools, development tools |
| **Low** | No data access; commodity services | Office supplies, facilities management |

## 4. Vendor Assessment Requirements

### 4.1 Initial Assessment (New Vendors)

All new vendors classified as Critical or High must complete:
- Onyx Data Security Questionnaire (OD-SQ-v3) — 127 questions covering security controls, data handling, incident response, and business continuity
- Review of most recent SOC 2 Type II report (or equivalent: ISO 27001, SOC 1)
- Data processing agreement (DPA) execution for vendors handling customer data
- Legal review of contractual terms including liability, indemnification, and termination rights

### 4.2 Ongoing Assessment

| Tier | SOC 2 Report Review | Security Questionnaire | Business Review | Continuous Monitoring |
|------|---------------------|----------------------|-----------------|----------------------|
| **Critical** | Annual — within 90 days of report issuance | At onboarding + material change | Quarterly | Vendor risk monitoring (BitSight) |
| **High** | Annual — within 90 days of report issuance | At onboarding + every 2 years | Semi-annual | Vendor risk monitoring (BitSight) |
| **Medium** | Every 2 years | At onboarding | Annual | N/A |
| **Low** | Not required | Not required | Not required | N/A |

### 4.3 SOC 2 Report Review Requirements

When reviewing vendor SOC 2 reports, the GRC team must:
1. Verify the report covers the relevant service and period
2. Review the auditor's opinion for qualifications or exceptions
3. Document any complementary user entity controls (CUECs)
4. **Reports with qualified opinions require a formal risk assessment documenting the nature of the qualification, potential impact on Onyx Data, and any compensating controls or remediation commitments from the vendor**
5. Review management responses to any exceptions noted
6. File the review notes in the vendor management tracker

## 5. Contractual Requirements

All Critical and High vendor contracts must include:

### 5.1 Security Clauses
- Right to audit (annual, with 30 days' notice)
- Security incident notification within **72 hours** of discovery
- Data breach notification with details of scope, affected data, and remediation steps
- Data encryption requirements (at rest and in transit)
- Access control requirements (least privilege, MFA)
- Subprocessor notification and approval

### 5.2 Service Level Agreements
- Uptime targets appropriate to vendor tier
- Incident response SLAs
- Data return/deletion upon contract termination

### 5.3 Termination and Exit
- 90-day data portability period upon termination
- Certification of data deletion within 30 days of contract end
- Transition assistance obligations

## 6. Vendor Incident Management

### 6.1 Vendor Incident Notification

Upon receiving notification of a vendor security incident:
1. GRC team logs the incident in the Vendor Incident Tracker within 4 hours
2. CISO assesses potential impact to Onyx Data operations and customer data
3. Legal reviews notification obligations to customers and regulators
4. Customer communication decision within 48 hours of confirmed customer data impact
5. Post-incident review with vendor within 30 days

### 6.2 Vendor Incident Escalation

| Impact Level | Description | Escalation |
|-------------|-------------|------------|
| **Confirmed customer data compromise** | Vendor confirms Onyx Data customer data was accessed or exfiltrated | Immediate: CISO, CEO, Legal, Board notification |
| **Potential customer data exposure** | Vendor cannot confirm or deny customer data was affected | Within 24 hours: CISO, Legal, customer comms team |
| **No customer data impact** | Vendor confirms incident did not affect Onyx Data data | Standard logging, review at next vendor business review |

## 7. Governance and Reporting

- Vendor risk posture reported to the Security Committee quarterly
- Critical vendor incidents reported to the Board within 24 hours
- Annual vendor risk summary included in SOC 2 management assertion

## 8. Exceptions

Exceptions to this policy require written approval from the CISO and VP GRC, documented in the exception register with:
- Business justification
- Compensating controls
- Risk acceptance by the vendor relationship owner
- Expiration date (maximum 6 months, renewable)

---

*Approved by: Michael Zhang, CEO — February 28, 2025*
