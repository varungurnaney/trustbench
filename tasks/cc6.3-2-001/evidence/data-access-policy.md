# Zenith Software — Data Access Authorization Policy

**Document ID:** POL-DA-2025-008
**Version:** 3.0
**Effective Date:** January 15, 2025
**Last Review:** October 1, 2025
**Owner:** Mei Lin Chang, Chief Information Security Officer
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy establishes requirements for authorizing, managing, and monitoring access to Zenith Software's data assets. All data access must follow least-privilege principles with segregation of duties enforced for sensitive operations.

## 2. Data Classification

All Zenith data is classified into the following categories:

| Classification | Description | Examples | Access Approval |
|---------------|-------------|----------|-----------------|
| Restricted | Highly sensitive data requiring maximum protection | Customer PII, payment data, authentication credentials | CISO + Data Owner |
| Confidential | Business-sensitive data | Financial records, contracts, employee data | Data Owner + Manager |
| Internal | General business data | Project plans, internal communications | Manager |
| Public | Publicly available information | Marketing materials, published APIs | Self-service |

### 2.1 Table Classifications

| Schema.Table | Classification |
|-------------|---------------|
| zenith_prod.customers | Restricted |
| zenith_prod.payment_transactions | Restricted |
| zenith_prod.user_credentials | Restricted |
| zenith_prod.orders | Confidential |
| zenith_prod.products | Internal |
| zenith_prod.invoices | Confidential |
| zenith_prod.audit_log | Restricted |
| zenith_analytics.customer_metrics | Confidential |
| zenith_analytics.revenue_reports | Confidential |
| zenith_analytics.product_usage | Internal |

## 3. Access Authorization Principles

### 3.1 Least Privilege and RBAC

All data access is managed through predefined roles. Users are granted the minimum permissions required for their job function.

| Role | Allowed Permissions | Scope |
|------|-------------------|-------|
| app-read | SELECT | Application-specific tables |
| app-readwrite | SELECT, INSERT, UPDATE | Application-specific tables |
| qa-analyst | SELECT | Production read-only for testing verification |
| data-analyst | SELECT | Analytics schema + masked production views |
| dba-admin | ALL PRIVILEGES | All schemas (restricted to DBA team) |
| svc-application | SELECT, INSERT, UPDATE | Application-specific tables |

### 3.2 Destructive Operations

Destructive operations (DELETE, TRUNCATE, DROP) on production tables classified as Restricted are prohibited for non-DBA roles. All destructive operations require:

- Written approval from the Data Owner
- Change management ticket (CHG record)
- Execution by a DBA during a scheduled maintenance window
- Pre-execution backup verification

### 3.3 Segregation of Duties

Finance department personnel must not have direct write access to financial transaction tables (payment_transactions, invoices, revenue_reports). Finance team members may only have read access; all write operations must flow through the application layer with audit logging.

Development personnel must not have direct write access to production databases.

### 3.4 Data Masking

Non-DBA, non-application roles accessing Restricted tables must use masked views that redact PII fields (SSN, credit card numbers, email addresses).

## 4. Access Lifecycle

### 4.1 Provisioning

Access requests via ServiceNow. Provisioned within 2 business days. Approval chain per data classification level.

### 4.2 Quarterly Reviews

System owners review all database access grants quarterly. Excessive or inappropriate access revoked within 5 business days.

### 4.3 Revocation

Access revoked within 24 hours of termination. Role change triggers access re-evaluation.

## 5. Service Accounts

### 5.1 Governance

All service accounts must have a designated human owner, documented business purpose, and be included in quarterly reviews.

### 5.2 Credential Management

Service account credentials rotated every 90 days. Static credentials prohibited where alternatives exist.

## 6. Exceptions

CISO-approved with compensating controls. Time-bound to 6 months. Documented in exception register.

---

**Approved by:** Mei Lin Chang, CISO
**Next Review Date:** January 2026
