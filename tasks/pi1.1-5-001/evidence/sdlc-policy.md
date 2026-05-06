# Software Development Lifecycle (SDLC) Policy

**Document ID:** POL-SDLC-013
**Version:** 5.0
**Effective Date:** January 10, 2025
**Owner:** Engineering Operations
**Classification:** Internal

---

## 1. Purpose

This policy defines Nexus Cloud Platform's SDLC practices to ensure processing integrity, security, and quality across all software systems.

## 2. Scope

Applies to all applications, data pipelines, and infrastructure configurations managed by Nexus Cloud Platform.

## 3. Development Standards

### 3.1 Code Review

All pull requests require at least one approving review before merge. Security-sensitive changes require AppSec team review.

### 3.2 Static Analysis

SonarQube SAST scans run on every PR:

| Severity | SLA |
|----------|-----|
| Critical | Block merge |
| High | 30 calendar days |
| Medium | 90 calendar days |
| Low | Best effort |

## 4. Deployment

### 4.1 Pipeline Stages

Build, SAST, staging deploy, staging validation (24-hour minimum), production approval, production deploy, post-deploy verification.

### 4.2 Environment Parity

Staging and production environments are managed through Infrastructure-as-Code (Terraform). Configuration parity between staging and production is a critical processing integrity control — code validated in staging must behave identically in production.

**Configuration drift tolerance:** Configuration drift between staging and production must not exceed 5% of total configuration parameters. Any drift above 5% is classified as a Critical finding and must be remediated within 24 hours.

**Drift reporting:** Configuration drift scans run weekly. Results are reported to the Platform Engineering team lead.

**Acceptable drift:** Known and documented differences (e.g., environment-specific endpoints, log levels, resource scaling parameters) must be recorded in the Environment Parity Exception Register with justification.

### 4.3 Change Freeze

During change freeze periods, only Critical production fixes may be deployed. All freeze-period deployments require CTO approval.

## 5. Processing Integrity

### 5.1 Input Validation

All external inputs must be validated against defined schemas.

### 5.2 Data Integrity

Critical pipelines implement record count reconciliation. Batch processing completeness is verified with source-destination record count matching.

### 5.3 Error Handling

Processing errors are logged and categorized. Failed transactions must not be silently dropped.

---

**Approved by:** Katherine Walsh, VP Engineering
**Next Review Date:** January 2026
