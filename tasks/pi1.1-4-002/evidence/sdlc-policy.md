# Software Development Lifecycle (SDLC) Policy

**Document ID:** POL-SDLC-009
**Version:** 3.5
**Effective Date:** February 1, 2025
**Owner:** Engineering Operations
**Classification:** Internal

---

## 1. Purpose

This policy establishes Horizon Data Corp's SDLC requirements to maintain processing integrity across all data processing systems.

## 2. Scope

Applies to all applications and data pipelines developed by Horizon Data Corp.

## 3. Code Review

### 3.1 Peer Review Requirements

All merge requests require at least one approving review from a developer who did not author the code. Reviews must verify correctness of business logic, input validation, error handling, and test adequacy.

### 3.2 Security-Sensitive Review

Changes to authentication, authorization, cryptography, or data processing logic require an additional review from the Application Security team.

## 4. Static Analysis

### 4.1 Quality Gate

SonarQube SAST scans run on every merge request:

| Severity | SLA |
|----------|-----|
| Critical | Block merge |
| High | 30 calendar days |
| Medium | 90 calendar days |
| Low | Best effort |

### 4.2 False Positive Process

False positive determinations require documented justification and AppSec team confirmation. Approved exceptions are logged in the SAST Exception Register.

## 5. Input Validation

### 5.1 Validation Requirements

All external-facing API endpoints must validate inputs against OpenAPI schemas. Backend services must validate all inter-service messages against Protobuf or Avro schemas.

### 5.2 Validation Testing

Input validation tests must cover boundary conditions, type mismatches, oversized payloads, and injection patterns.

## 6. Deployment

All deployments follow the CI/CD pipeline: build, test, staging deployment, staging validation, production approval, production deployment. Staging validation is mandatory.

---

**Approved by:** Ryan Foster, CTO
**Next Review Date:** February 2026
