# Data Access Authorization Policy

**Document ID:** POL-DAA-001
**Version:** 2.3
**Effective Date:** August 1, 2025
**Owner:** Data Governance Team

---

## 1. Purpose

This policy defines the authorization requirements for accessing customer data at ClearView Analytics.

## 2. Data Classification

| Level | Description | Examples | Authorization Required |
|-------|-------------|----------|----------------------|
| Public | Non-sensitive business data | Marketing materials | None |
| Internal | Business operational data | Revenue reports, roadmap | Manager approval |
| Confidential | Customer PII and business data | Customer names, emails, usage analytics | Data Owner + Manager + Privacy Officer |
| Restricted | Sensitive PII and financial data | SSN, payment info, health data | Data Owner + CISO + Legal |

## 3. Authorization Controls

### 3.1 Database Access

- All customer database access requires an approved Jira ticket with business justification.
- Read-only access to Confidential data requires Data Owner approval.
- Write access to any customer database requires CISO approval.
- All database queries against customer tables are logged in the audit trail.

### 3.2 Data Export Controls

- Bulk data exports (>1,000 records) require Data Owner + CISO approval.
- Exports to external systems require Privacy Officer review.
- All exports are logged and include a data classification tag.

### 3.3 API Access

- API keys for customer data endpoints are issued per-service, not per-developer.
- API rate limits are enforced: 1,000 requests/minute for internal services, 100 requests/minute for partner integrations.
- All API access to customer data is authenticated via OAuth 2.0 with scoped permissions.

### 3.4 Analytics and Reporting

- Analysts access customer data through a read-only analytics replica.
- The analytics replica masks PII fields (email, phone, name) by default.
- Unmasked access requires Privacy Officer approval and is time-limited to 30 days.

## 4. Review and Audit

- Data access authorizations are reviewed quarterly.
- The Data Governance team produces a monthly access report.
- Anomalous access patterns are escalated to the Security team.

---

**Approved by:** Karen Liu, Chief Privacy Officer
**Next Review Date:** August 2026
