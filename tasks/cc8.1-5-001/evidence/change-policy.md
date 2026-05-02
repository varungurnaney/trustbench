# Beacon SaaS — Change Management Policy

**Document ID:** POL-CHG-2024-007
**Version:** 4.0
**Effective Date:** February 1, 2024
**Last Review:** August 15, 2025
**Owner:** Natasha Volkov, VP of Engineering
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy establishes the change management process for all modifications to Beacon SaaS production systems, including application code, infrastructure configurations, database schemas, and third-party integrations. The goal is to ensure that changes are authorized, tested, and deployed in a controlled manner to minimize risk to service availability and data integrity.

## 2. Scope

This policy applies to all changes affecting:

- Beacon SaaS application (web, API, mobile backends)
- Production infrastructure (AWS, Kubernetes clusters)
- Database schemas and migrations
- Third-party integration configurations
- DNS and network configurations
- Security configurations (IAM, security groups, WAF rules)

## 3. Change Classification

### 3.1 Standard Changes

Pre-approved, low-risk changes that follow documented procedures. Examples:
- Dependency version updates (patch level)
- Configuration parameter adjustments within approved ranges
- Routine certificate rotations

Standard changes do not require CAB approval but must be logged.

### 3.2 Normal Changes

Changes that modify application behavior, infrastructure topology, or security configurations. Normal changes must follow the full change management process outlined in Section 4.

### 3.3 Emergency Changes (Hotfixes)

Changes required to restore service or mitigate an active security incident. Emergency changes may follow an expedited process as described in Section 5.

## 4. Normal Change Management Process

### 4.1 Change Request

All normal changes must be documented in the Beacon SaaS change management system (Jira) with:

- Description of the change and business justification
- Risk assessment (Low / Medium / High)
- Rollback plan
- Affected systems and services
- Estimated deployment window

### 4.2 Peer Review

All code changes require at least one peer review approval from a qualified engineer who is not the author of the change. Peer review must be completed in the version control system (GitHub) before merge.

### 4.3 Staging Environment Testing

All normal changes must be deployed to the staging environment and pass the following validation steps before production deployment:

1. Automated integration test suite must pass with 100% of critical tests and 98% overall pass rate
2. Manual smoke testing by the change author or designated QA engineer
3. Performance regression testing for changes flagged as High risk
4. Staging deployment must be stable for a minimum of 2 hours before production promotion

### 4.4 Change Advisory Board (CAB) Approval

Normal changes classified as Medium or High risk require approval from the Change Advisory Board prior to production deployment. The CAB meets weekly on Tuesdays at 10:00 AM ET and consists of:

- VP of Engineering (Chair)
- Director of SRE
- Security Engineering Lead
- Product Manager (for customer-impacting changes)

CAB approval must be documented in the change ticket prior to deployment.

### 4.5 Production Deployment

Production deployments must:

- Occur during approved deployment windows (Tuesday through Thursday, 10:00 AM - 4:00 PM ET)
- Be executed using the automated CI/CD pipeline (GitHub Actions)
- Include automated health checks post-deployment
- Have the change author or designated on-call engineer available for 1 hour post-deployment

### 4.6 Rollback Criteria

A rollback must be initiated if any of the following occur within 1 hour of deployment:

- Error rate exceeds 1% above pre-deployment baseline
- P95 latency exceeds 200% of pre-deployment baseline
- Automated health checks fail
- Customer-reported incidents related to the change

## 5. Emergency Change (Hotfix) Process

Emergency changes are permitted when:

- A production incident is actively impacting customers (Severity 1 or 2)
- A critical security vulnerability requires immediate remediation

Emergency changes must still satisfy:

1. Peer review by at least one qualified engineer
2. Automated unit and integration tests must pass
3. Post-deployment validation within 30 minutes

Emergency changes may bypass:

- Staging environment testing (if time-critical)
- CAB approval (retrospective CAB review required within 5 business days)
- Deployment window restrictions

All emergency changes must be logged and reviewed at the next CAB meeting with a root cause analysis documenting why the emergency process was invoked.

## 6. Deployment Metrics and Reporting

Engineering leadership reviews the following metrics monthly:

- Deployment frequency
- Change failure rate (target: < 5%)
- Mean time to recovery (MTTR) for failed deployments
- Rollback frequency (escalation trigger: > 2 rollbacks per quarter)
- CAB approval compliance rate

## 7. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 4.0 | 2025-08-15 | N. Volkov | Updated CAB composition, added rollback criteria metrics |
| 3.5 | 2025-02-01 | N. Volkov | Added staging stability window requirement |
| 3.0 | 2024-02-01 | N. Volkov | Major revision — formalized CAB process, added emergency change section |
