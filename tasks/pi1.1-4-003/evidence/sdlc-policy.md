# Software Development Lifecycle (SDLC) Policy

**Document ID:** POL-SDLC-011
**Version:** 4.0
**Effective Date:** January 20, 2025
**Owner:** Engineering Operations
**Classification:** Internal

---

## 1. Purpose

This policy defines the SDLC practices for Cascade Systems to maintain processing integrity, quality, and security in all software deliveries.

## 2. Scope

All software and data processing systems developed by Cascade Systems engineering teams.

## 3. Code Review

### 3.1 Mandatory Review

All pull requests require at least one approving review. The reviewer must not be the author.

### 3.2 Emergency Changes

Emergency hotfixes may be deployed without pre-merge review if authorized by the VP Engineering or CTO. Emergency changes must receive a post-deploy review within 48 hours of deployment. The post-deploy review must be documented with findings and any required follow-up actions.

## 4. Static Analysis

### 4.1 SAST Policy

SonarQube SAST runs on every PR:

| Severity | SLA |
|----------|-----|
| Critical | Block merge |
| High | 30 calendar days |
| Medium | 90 calendar days |
| Low | Best effort |

## 5. Deployment

### 5.1 Standard Deployment

Build, SAST, staging deployment, staging validation (24-hour minimum), production approval, production deploy, post-deploy verification.

### 5.2 Configuration Management

All application configuration is managed through Infrastructure-as-Code (Terraform) stored in version control. Configuration drift between staging and production must not exceed 5% of configuration parameters. Drift above 5% requires immediate investigation and remediation within 48 hours.

## 6. Processing Integrity

### 6.1 Input Validation

All external inputs validated against schemas. Malformed inputs rejected with error codes.

### 6.2 Data Integrity

Critical pipelines implement record count reconciliation at pipeline boundaries.

---

**Approved by:** Amanda Torres, VP Engineering
**Next Review Date:** January 2026
