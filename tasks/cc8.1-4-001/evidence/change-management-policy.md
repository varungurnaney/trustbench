# Change Management Policy

**Document ID:** POL-CHG-005
**Version:** 4.0
**Effective Date:** May 1, 2025
**Owner:** Engineering

---

## 1. Purpose

This policy governs all changes to Stratos Inc. production systems to ensure stability, security, and auditability.

## 2. Change Categories

| Category | Description | Approval | Implementation Window |
|----------|-------------|----------|-----------------------|
| Standard | Pre-approved routine changes per Standard Change Catalog | None required | Business hours |
| Normal | Non-routine changes with planned impact | CAB approval (weekly Tuesday meeting) | Scheduled maintenance window (Saturday 02:00-06:00 UTC) |
| Emergency | Urgent production fixes for active incidents | VP Engineering verbal + retrospective CAB review within 48 business hours | Any time |

## 3. Change Request Process

### 3.1 Submission

All changes require a Jira ticket (project: CHG) with:
- Description and scope of change
- Impact assessment
- Risk rating (Low / Medium / High / Critical)
- Rollback plan
- Testing evidence (test results, QA sign-off)

### 3.2 Approval

- Normal changes: Approved at weekly CAB meeting. Quorum: VP Engineering + Security Lead + at least one other CAB member.
- Emergency changes: VP Engineering verbal approval. Jira ticket created retroactively. Retrospective CAB review within 48 business hours.
- All approvals recorded in Jira ticket comments with approver name and timestamp.

### 3.3 Segregation of Duties

- The engineer who develops a change must not be the same person who approves it.
- Code changes require peer review (GitHub PR approval from a different engineer).
- Production deployments are executed by the SRE team, not the development team.

### 3.4 Testing

- All Normal changes must include evidence of testing in a staging environment.
- Test results are attached to the Jira ticket.
- Changes with risk rating High or Critical require Security team review before deployment.

### 3.5 Post-Implementation Review

- Change owner verifies successful deployment within 2 hours.
- Any issues are escalated per the incident response plan.
- Post-implementation verification is recorded in the Jira ticket.

## 4. Standard Change Catalog

The following are pre-approved and do not require CAB review:

| ID | Change Type | Conditions |
|----|-------------|------------|
| SC-001 | OS security patches (non-kernel) | Applied during maintenance window; auto-rollback enabled |
| SC-002 | SSL certificate renewal | Automated via cert-manager; no manual steps |
| SC-003 | Log retention policy updates | Configuration-only; no code changes |
| SC-004 | Dependency updates (minor/patch) | Passes all CI tests; no API changes |

## 5. Change Freeze

- Code freezes are enforced 48 hours before and after major releases.
- Holiday freezes: November 25-30 (Thanksgiving week) and December 20-January 2 (end of year).
- Emergency changes during freeze periods require CISO approval in addition to VP Engineering.

---

**Approved by:** Derek Huang, VP Engineering
**Next Review Date:** May 2026
