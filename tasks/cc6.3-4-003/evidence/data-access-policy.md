# Vertex Financial — Data Access Authorization Policy

**Document ID:** POL-DAP-2025-011
**Version:** 3.5
**Effective Date:** February 1, 2025
**Last Review:** October 15, 2025
**Owner:** Catherine Reeves, Chief Information Security Officer
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy defines the requirements for authorizing and managing access to Vertex Financial's data assets. As a fintech company in PCI-DSS scope, all access to cardholder data must comply with PCI-DSS requirements in addition to SOC 2 criteria.

## 2. Data Classification

| Classification | Description | Examples |
|---------------|-------------|----------|
| PCI Restricted | Cardholder data subject to PCI-DSS | Card numbers, CVV, expiration dates, cardholder names |
| Restricted | Non-PCI highly sensitive data | SSN, bank account numbers, authentication credentials |
| Confidential | Business-sensitive | Financial reports, contracts, employee data |
| Internal | General business | Project plans, internal docs |
| Public | Published | Marketing, public APIs |

## 3. Access Authorization

### 3.1 RBAC Requirements

All Snowflake data warehouse access is managed through predefined roles:

| Role | Scope | Approval | Notes |
|------|-------|----------|-------|
| ANALYST_READONLY | SELECT on assigned schemas | Manager + Data Owner | Standard analyst access |
| MARKETING_ANALYTICS | SELECT on marketing and customer behavior data | Manager + Data Owner | No PCI data access |
| RISK_ANALYTICS | SELECT on risk models and transaction summaries | Manager + Data Owner + CISO | Aggregated data only |
| DATA_ENGINEER | SELECT, INSERT, UPDATE on ETL schemas | Manager + Data Owner | ETL development |
| DBA_ADMIN | ALL PRIVILEGES | CISO + CTO | Maximum 2 named individuals |
| ACCOUNTADMIN | Snowflake system administration | CISO + CTO + Board | Restricted to DBA team only |

Custom roles require CISO exception approval.

### 3.2 Least Privilege

All access follows least-privilege principles. Users receive minimum permissions for their specific duties.

### 3.3 Segregation of Duties

- Risk team personnel must not have administrative database privileges
- Marketing personnel must not access raw PCI data
- Finance personnel write access to financial tables requires dual approval

## 4. PCI Data Protection

### 4.1 Cardholder Data Access

Direct access to cardholder data tables requires:

- PCI-DSS annual certification
- Data Owner + CISO + Privacy Officer approval
- Justified business need documented in access request

### 4.2 Data Masking

All non-DBA roles accessing PCI-scoped tables must use dynamic data masking to redact card numbers, CVV, and expiration dates. Masking is enforced at the Snowflake column-level security policy layer.

### 4.3 DLP Controls

Automated alerts for:

- Queries returning more than 10,000 rows from PCI tables
- Bulk export operations from any Restricted classification table
- Access to PCI tables outside business hours (6 AM - 8 PM EST)

## 5. Service Accounts

### 5.1 Governance

Service accounts must be scoped to the minimum privileges required for the automated workflow. Broad roles (SYSADMIN, ACCOUNTADMIN) are prohibited for service accounts.

### 5.2 Ownership

All service accounts must have a designated human owner in the service account registry.

## 6. Access Reviews

Quarterly reviews within 14 calendar days. PCI-scoped access reviewed monthly.

## 7. Exceptions

CISO-approved with compensating controls. Maximum 6 months. Reviewed quarterly.

---

**Approved by:** Catherine Reeves, CISO
**Next Review Date:** February 2026
