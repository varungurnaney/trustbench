# Software Development Lifecycle (SDLC) Policy

**Document ID:** POL-SDLC-001
**Version:** 3.2
**Effective Date:** February 1, 2025
**Owner:** Engineering Operations
**Classification:** Internal
**Last Reviewed:** January 15, 2025

---

## 1. Purpose

This policy defines the Software Development Lifecycle practices for Meridian Software Inc. to ensure that software is developed, tested, and deployed in a manner that meets quality and security objectives.

## 2. Scope

This policy applies to all software developed, maintained, or modified by Meridian Software engineering teams, including internal tools, customer-facing applications, APIs, and microservices.

## 3. Development Phases

### 3.1 Requirements Gathering

All new features and changes must begin with a documented requirements phase. Product managers create user stories in Jira with acceptance criteria. Security requirements are captured using the STRIDE threat modeling framework for features involving authentication, authorization, or data handling.

### 3.2 Design

Architectural decisions are documented in Architecture Decision Records (ADRs) stored in Confluence. Design reviews are conducted for features that introduce new services, modify data schemas, or change authentication flows. The Security Architecture team participates in design reviews for features flagged as security-relevant.

### 3.3 Development

Developers follow the Meridian Coding Standards Guide (DOC-CS-001). All code is stored in GitHub Enterprise repositories. Feature branches follow the naming convention `feature/<ticket-id>-<description>`. Developers are expected to write unit tests for new code with a target of 80% line coverage.

### 3.4 Testing

#### 3.4.1 Unit Testing

Unit tests are executed automatically in the CI pipeline on every commit. Builds fail if coverage drops below 75% for modified files.

#### 3.4.2 Integration Testing

Integration tests run nightly against the staging environment. Test results are published to the QA dashboard in Datadog.

#### 3.4.3 Security Testing

Static Application Security Testing (SAST) is integrated into the CI pipeline using SonarQube. Dynamic Application Security Testing (DAST) scans are performed quarterly against staging using OWASP ZAP.

### 3.5 Deployment

Production deployments follow the release management process defined in Section 5. All deployments are executed through the CI/CD pipeline. Manual deployments to production are not permitted.

### 3.6 Maintenance

Post-deployment monitoring is performed using Datadog APM. Bug reports are triaged within 24 hours of submission. Critical production bugs are addressed through the hotfix process defined in Section 5.3.

## 4. Quality Assurance

### 4.1 Definition of Done

A user story is considered complete when:

- All acceptance criteria are met
- Unit tests pass with adequate coverage
- Integration tests pass
- SAST scan shows no new Critical or High findings
- Documentation is updated
- Product owner has accepted the feature

### 4.2 Quality Gates

The CI/CD pipeline enforces the following gates:

| Gate | Criteria | Enforcement |
|------|----------|-------------|
| Build | Compilation succeeds | Blocking |
| Unit Tests | All tests pass, coverage >= 75% | Blocking |
| SAST | No new Critical findings | Blocking |
| DAST | No Critical findings (quarterly) | Advisory |
| Linting | Code style compliance | Advisory |

## 5. Release Management

### 5.1 Release Schedule

Production releases follow a biweekly sprint cadence. Release candidates are tagged on Wednesday, deployed to staging Thursday, and promoted to production the following Monday.

### 5.2 Change Approval

All production changes require approval from the Release Manager. Changes are documented in the Change Management system (ServiceNow) with a Change Request ticket.

### 5.3 Hotfix Process

Critical production issues may be addressed through the hotfix process:

- Hotfix branch created from the production tag
- Fix implemented and tested
- Deployed through the standard CI/CD pipeline
- Backported to the main development branch

### 5.4 Rollback

All deployments include a documented rollback plan. Database migrations must be backward-compatible to support rollback within 30 minutes.

## 6. Security Requirements

### 6.1 Secure Coding

Developers complete annual secure coding training. The Meridian Secure Coding Guidelines (DOC-SCG-001) are maintained by the Application Security team.

### 6.2 Dependency Management

Third-party dependencies are scanned using Snyk on every build. Critical dependency vulnerabilities block the build pipeline. A Software Bill of Materials (SBOM) is generated for each release.

### 6.3 Secrets Management

Application secrets are stored in HashiCorp Vault. Hardcoded secrets detected by git-secrets pre-commit hooks are blocked from being committed.

## 7. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| Engineering Manager | Sprint planning, resource allocation, quality oversight |
| Developers | Code development, unit testing, documentation |
| QA Engineers | Integration testing, regression testing, test automation |
| Release Manager | Release coordination, change approval, deployment oversight |
| Security Engineers | SAST/DAST configuration, security review of flagged features |

## 8. Compliance

Non-compliance with this policy is reported to the Engineering VP. Repeated violations may result in corrective action.

## 9. Policy Review

This policy is reviewed annually or upon significant changes to the development process.

---

**Approved by:** Karen Liu, VP Engineering
**Next Review Date:** February 2026
