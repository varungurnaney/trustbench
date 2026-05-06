# Software Development Lifecycle (SDLC) Policy

**Document ID:** POL-SDLC-003
**Version:** 5.1
**Effective Date:** January 15, 2025
**Owner:** Engineering Operations
**Classification:** Internal

---

## 1. Purpose

This policy defines the Software Development Lifecycle practices for Arcadia Data Systems to ensure software quality, security, and processing integrity.

## 2. Scope

Applies to all software developed or maintained by Arcadia Data Systems engineering teams.

## 3. Development Process

All development follows a trunk-based development model with short-lived feature branches. Pull requests require at least one approving review before merge.

## 4. Quality Gates

### 4.1 Static Analysis

SonarQube SAST scans run on every pull request. The following quality gate applies:

| Severity | Policy |
|----------|--------|
| Critical | Block merge — must be fixed before merge |
| High | Must be resolved within 30 calendar days of detection |
| Medium | Must be resolved within 90 calendar days |
| Low | Best effort |

### 4.2 Code Review

All pull requests require at least one approved review from a team member who did not author the code.

### 4.3 Testing

Unit test coverage must be >= 80% for modified files. Integration tests run on merge to main.

## 5. Deployment

All deployments are automated through GitHub Actions. Staging deployment is mandatory before production promotion.

## 6. Processing Integrity

### 6.1 Input Validation

All API endpoints must validate input against defined schemas. Invalid inputs must return appropriate error codes without processing.

### 6.2 Data Integrity

Critical data processing pipelines must implement record count reconciliation and checksum verification.

---

**Approved by:** Thomas Reed, VP Engineering
**Next Review Date:** January 2026
