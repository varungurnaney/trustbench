# Change Management Policy

**Document ID:** POL-CHG-002
**Version:** 2.0
**Effective Date:** March 1, 2025
**Owner:** Engineering

---

## 1. Purpose

This policy governs all changes to Orion Health's production systems, infrastructure, and applications to ensure stability, security, and compliance.

## 2. Scope

All changes to production environments, including application deployments, infrastructure modifications, database schema changes, and configuration updates.

## 3. Change Categories

| Category | Description | Approval Required |
|----------|-------------|-------------------|
| Standard | Pre-approved routine changes (e.g., OS patches on schedule) | None (pre-approved) |
| Normal | Non-routine changes with known impact | Change Advisory Board (CAB) |
| Emergency | Urgent fixes for production incidents | VP Engineering (retrospective CAB review within 48 hours) |

## 4. Change Request Process

### 4.1 Submission

All change requests must be submitted via Jira with:
- Description of the change
- Business justification
- Impact assessment
- Rollback plan

### 4.2 Review and Approval

- Standard changes: auto-approved per the Standard Change Catalog.
- Normal changes: reviewed at weekly CAB meeting (Tuesdays at 2pm).
- Emergency changes: verbal approval from VP Engineering; Jira ticket created retroactively.

### 4.3 Implementation

- Changes are deployed by the requesting engineer.
- All deployments use the CI/CD pipeline (GitHub Actions → staging → production).

### 4.4 Post-Implementation

- The change owner verifies the deployment was successful.
- Any issues are reported to the CAB.

## 5. Rollback

All changes must include a documented rollback plan. If a change causes a production incident, the rollback plan must be executed within 30 minutes.

## 6. Documentation

All changes are tracked in Jira. The Jira ticket serves as the record of the change including approval, implementation, and verification.

---

**Approved by:** Daniel Park, VP Engineering
**Next Review Date:** March 2026
