# Change Management Policy

**Document ID:** POL-CHG-011
**Version:** 3.2
**Effective Date:** March 15, 2025
**Owner:** Engineering
**Approved By:** Marcus Webb, VP Engineering

---

## 1. Purpose

This policy governs all changes to Helios Data Systems production systems to ensure stability, security, and auditability in compliance with SOC 2 Trust Services Criteria.

## 2. Change Categories

| Category | Description | Approval | Implementation Window |
|----------|-------------|----------|-----------------------|
| Standard | Pre-approved routine changes per catalog | None required | Business hours |
| Normal | Non-routine changes | CAB approval at weekly meeting | Maintenance window (Saturday 02:00-06:00 UTC) |
| Emergency | Urgent fixes for active Sev 1/2 incidents | VP Engineering verbal + retrospective CAB within 48 hours | Any time |

## 3. Change Request Process

### 3.1 Submission

All changes require a Jira ticket (project: CHG) with:
- Description and scope
- Risk classification (Low / Medium / High / Critical)
- Impact assessment
- Rollback plan
- Testing evidence

### 3.2 Security Review

Changes with risk classification **High** or **Critical** require a security review by the Security Engineering team prior to CAB approval. The security review must include:
- Threat modeling for the proposed change
- Review of authentication and authorization impacts
- Data flow analysis for changes involving customer data
- Confirmation that no new vulnerabilities are introduced

Security review sign-off is documented in the Jira ticket as a comment from a Security Engineering team member.

### 3.3 CAB Approval

- Normal changes: Reviewed at weekly CAB meeting (Wednesdays at 10am ET).
- Quorum: VP Engineering + Security Lead + at least one other member.
- Emergency changes: VP Engineering verbal approval. Retrospective CAB within 48 hours.

### 3.4 Testing

All Normal changes must be tested in the staging environment before production deployment. Test results are attached to the Jira ticket.

### 3.5 Segregation of Duties

- The developer of a change must not approve their own change.
- Production deployments are executed by the Platform Engineering team, not the development team.

### 3.6 Post-Implementation

Change owner verifies deployment within 1 hour. Verification recorded in Jira.

---

**Next Review Date:** March 2026
