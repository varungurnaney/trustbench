# Software Development Lifecycle (SDLC) Policy

**Document ID:** POL-SDLC-007
**Version:** 4.2
**Effective Date:** January 5, 2025
**Owner:** Engineering Operations
**Classification:** Internal

---

## 1. Purpose

This policy defines Vantage Analytics' SDLC practices to ensure software is developed with appropriate processing integrity, security, and quality controls.

## 2. Scope

Applies to all software and data processing pipelines developed by Vantage Analytics engineering teams.

## 3. Development Standards

### 3.1 Version Control

All code is stored in GitLab. Merge requests require at least one approving review.

### 3.2 Code Review

All merge requests require peer code review. Reviewers verify business logic, error handling, and test adequacy.

## 4. Static Analysis

### 4.1 SAST Integration

SonarQube SAST scans run on every merge request. The following quality gate applies:

| Severity | Policy |
|----------|--------|
| Critical | Block merge — must be fixed |
| High | Must be resolved within 30 calendar days |
| Medium | Must be resolved within 90 calendar days |
| Low | Best effort |

### 4.2 False Positive Management

SAST findings confirmed as false positives must be documented with:

- Technical justification explaining why the finding is not exploitable
- Confirmation by a member of the Application Security team
- Entry in the SAST Exception Register with the finding ID and justification

Findings with approved false positive determinations are excluded from SLA tracking.

### 4.3 Escalation

High-severity findings not resolved within the SLA and without an approved false positive determination must be escalated to the Engineering VP.

## 5. Deployment

### 5.1 Pipeline Stages

1. Build and unit tests
2. SAST scan
3. Staging deployment and integration tests
4. Production approval
5. Production deployment
6. Post-deploy verification

### 5.2 Change Approval

All production deployments require Release Manager approval.

## 6. Processing Integrity

### 6.1 Input Validation

All external inputs must be validated. Processing must reject malformed inputs with descriptive error codes.

### 6.2 Data Integrity

Critical pipelines implement record count reconciliation and checksum verification at pipeline boundaries.

---

**Approved by:** Diana Chen, VP Engineering
**Next Review Date:** January 2026
