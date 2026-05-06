# Software Development Lifecycle (SDLC) Policy

**Document ID:** POL-SDLC-015
**Version:** 4.1
**Effective Date:** February 15, 2025
**Owner:** Engineering Operations
**Classification:** Internal

---

## 1. Purpose

This policy defines Quantum Data Solutions' SDLC practices to ensure processing integrity across all software systems that handle financial transaction processing.

## 2. Scope

Applies to all applications developed by Quantum Data Solutions, with enhanced requirements for systems classified as Tier 1 (financial transaction processing, customer data management, regulatory reporting).

## 3. Code Review

### 3.1 Standard Review

All pull requests require at least one approving review from a qualified reviewer (not the author). For Tier 1 systems, two approving reviews are required, with at least one from a Senior Engineer or above.

### 3.2 Emergency Change Process

Emergency production fixes may bypass pre-merge review requirements under the following conditions:

1. **Authorization:** Must be authorized by VP Engineering, CTO, or on-call Engineering Director
2. **Scope limitation:** Change must be limited to the minimum necessary to resolve the production incident
3. **Post-deploy review:** A comprehensive post-deploy review must be completed within 24 hours of deployment
4. **Post-deploy review requirements:** The post-deploy review must include:
   - Correctness verification of the fix
   - Regression risk assessment
   - Test coverage analysis
   - Identification of follow-up actions
   - Sign-off by a Senior Engineer who was not involved in the emergency fix
5. **Documentation:** An incident post-mortem must be filed within 72 hours linking the emergency change to the incident

### 3.3 Consequences

Emergency changes without completed post-deploy reviews are escalated to the VP Engineering weekly. Three or more incomplete reviews in a quarter trigger a corrective action plan review by the CTO.

## 4. Static Analysis

### 4.1 SAST Requirements

SonarQube scans on every PR. Critical blocks merge. High must be resolved within 30 days.

## 5. Deployment

### 5.1 Standard Pipeline

Build, test, SAST, staging deploy, staging validation (24 hours), production approval (2 approvers for Tier 1), production deploy, post-deploy verification.

### 5.2 Environment Parity

Staging and production configurations managed through Terraform. Configuration drift tolerance: 5%.

## 6. Processing Integrity

### 6.1 Input Validation

All financial transaction inputs validated against schema with format, range, and business rule checks.

### 6.2 Data Reconciliation

All financial transaction pipelines implement source-to-destination record count reconciliation. Daily reconciliation reports are reviewed by the Finance Operations team. Discrepancies over $0.01 trigger investigation.

### 6.3 Audit Trail

All financial transactions maintain a complete, immutable audit trail including timestamps, operator identity, and before/after values for all state changes.

---

**Approved by:** Michael Chang, VP Engineering
**Next Review Date:** February 2026
