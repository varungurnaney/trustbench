# Orion Health Systems — Data Access Authorization Policy

**Document ID:** POL-DAP-2025-003
**Version:** 4.0
**Effective Date:** January 1, 2025
**Last Review:** October 1, 2025
**Owner:** Dr. Sarah Kim, Chief Information Security Officer
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy establishes requirements for authorizing access to Orion Health Systems data assets. As a healthcare technology company handling Protected Health Information (PHI), all data access must comply with HIPAA requirements in addition to SOC 2 Trust Services Criteria.

## 2. Data Classification

| Classification | Description | Examples | PHI |
|---------------|-------------|----------|-----|
| Restricted | Maximum protection — PHI and credentials | Patient records, prescriptions, SSN, credentials | Yes |
| Confidential | Business-sensitive, non-PHI | Financial records, contracts, employee data | No |
| Internal | General business data | Project plans, internal docs | No |
| Public | Published information | Marketing, public APIs | No |

## 3. Access Authorization

### 3.1 Approved RBAC Matrix

| Role | Permissions | Scope | Approval Required |
|------|------------|-------|-------------------|
| app-readonly | SELECT | Application-specific tables | Manager |
| app-readwrite | SELECT, INSERT, UPDATE | Application-specific tables | Manager + Data Owner |
| bi-reporting | SELECT | Cross-schema reporting tables | Data Owner + CISO |
| data-scientist | SELECT | Analytics views (masked PHI) | Manager + Privacy Officer |
| dba-admin | ALL PRIVILEGES | All schemas | CISO + CTO |
| svc-application | SELECT, INSERT, UPDATE | Application-specific tables | Data Owner |

Custom roles not listed in this matrix are prohibited. Any role outside this matrix requires CISO approval through the exception process (Section 7).

### 3.2 Access Request Process

All data access requests must be submitted through ServiceNow (catalog: DATA-ACCESS-ORH):

- **Internal/Public data:** Manager approval
- **Confidential data:** Manager + Data Owner approval
- **Restricted/PHI data:** Manager + Data Owner + Privacy Officer + CISO approval

Access is provisioned within 2 business days of complete approval chain.

### 3.3 Least Privilege

All access must follow least-privilege principles. Users receive only the minimum permissions necessary for their specific job duties. Broad or unrestricted access is prohibited unless approved through the exception process.

### 3.4 Segregation of Duties

- Users with write access to clinical data must not have administrative privileges
- Finance personnel must not have write access to billing tables
- Development personnel must not have write access to production

## 4. PHI Protection

### 4.1 PHI Access Controls

Access to PHI requires:

- Role-based access through the approved RBAC matrix
- Minimum necessary standard — access only to PHI elements needed for the specific function
- Audit logging of all PHI access (18-month retention)
- Annual PHI access training certification

### 4.2 De-identification

Non-clinical roles accessing PHI tables must use de-identified views with field-level masking applied at the database layer.

## 5. Service Accounts

### 5.1 Governance

All service accounts must have a designated human owner, scoped to minimum permissions, and included in quarterly access reviews.

### 5.2 Temporary Elevated Access

Temporary elevated access for service accounts requires CISO exception approval and must be time-bound.

## 6. Access Reviews

Quarterly reviews by Data Owners within 14 calendar days. Late reviews escalated to CISO.

## 7. Exception Process

CISO-approved with documented compensating controls. Maximum 6-month duration. Reviewed quarterly.

---

**Approved by:** Dr. Sarah Kim, CISO
**Next Review Date:** January 2026
