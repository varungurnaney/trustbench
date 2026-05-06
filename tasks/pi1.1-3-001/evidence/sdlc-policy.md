# Software Development Lifecycle (SDLC) Policy

**Document ID:** POL-SDLC-005
**Version:** 3.0
**Effective Date:** March 1, 2025
**Owner:** Engineering Operations
**Classification:** Internal

---

## 1. Purpose

This policy defines the SDLC practices for Pinnacle Cloud Services to ensure software is developed, tested, and deployed with appropriate processing integrity controls.

## 2. Scope

Applies to all applications developed and maintained by Pinnacle Cloud Services, including the customer-facing SaaS platform, internal tools, and data processing pipelines.

## 3. Development Standards

### 3.1 Version Control

All source code is stored in GitHub Enterprise. Feature branches are created from the main branch and merged via pull requests with at least one approving review.

### 3.2 Code Review

All changes require peer code review before merge. Reviewers must verify:

- Business logic correctness
- Error handling completeness
- Input validation coverage
- Test adequacy

### 3.3 Static Analysis

SonarQube scans run on every pull request. Critical findings block merge. High findings must be resolved within 30 days.

## 4. Testing Requirements

### 4.1 Unit Testing

All new code must include unit tests. Coverage must be >= 80% for modified files.

### 4.2 Integration Testing

Integration tests run against the staging environment after each staging deployment. All integration tests must pass before production promotion.

### 4.3 Staging Validation

**All code changes must be deployed to staging and validated before production deployment.** Staging must mirror the production environment configuration. Minimum staging validation period is 24 hours before production promotion. The QA team must sign off on staging deployment before production promotion is authorized.

## 5. Deployment Pipeline

### 5.1 Pipeline Architecture

The deployment pipeline consists of the following mandatory stages:

1. **Build** — Compile, run unit tests, SAST scan
2. **Staging Deploy** — Deploy to staging environment
3. **Staging Validation** — Integration tests + QA sign-off (minimum 24 hours)
4. **Production Approval** — Release Manager approval required
5. **Production Deploy** — Automated deployment to production
6. **Post-Deploy Verification** — Smoke tests and monitoring check

### 5.2 Environment Parity

Staging and production environments must maintain configuration parity. Infrastructure-as-Code (Terraform) ensures environment consistency. Configuration drift between staging and production must be reviewed and resolved within 48 hours.

### 5.3 Hotfix Process

Critical production issues may bypass the standard staging validation period (24 hours) but must still be deployed to staging first and pass integration tests. Hotfix deployments require VP Engineering approval.

## 6. Processing Integrity

### 6.1 Input Validation

All external inputs must be validated against defined schemas before processing.

### 6.2 Data Reconciliation

Batch processing jobs must implement record count reconciliation. Discrepancies trigger alerts to the operations team.

### 6.3 Error Handling

Processing errors must be logged, categorized, and made visible in the monitoring dashboard. Failed transactions must not be silently dropped.

---

**Approved by:** Marcus Webb, VP Engineering
**Next Review Date:** March 2026
