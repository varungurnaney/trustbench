# Change Management Policy

**Document ID:** POL-CHG-014
**Version:** 5.0
**Effective Date:** January 15, 2025
**Owner:** Engineering
**Approved By:** Andrea Ruiz, VP Engineering

---

## 1. Purpose

This policy governs all changes to Crestline SaaS production systems to ensure controlled, authorized, and tested modifications that maintain service integrity.

## 2. Change Categories

| Category | Description | Approval | Deployment Window |
|----------|-------------|----------|--------------------|
| Standard | Pre-approved per catalog | None | Business hours |
| Normal | Non-routine changes | CAB approval | Tuesday-Thursday 10:00-16:00 ET |
| Emergency | Active incident remediation | VP Eng verbal + retro CAB within 72 hours | Any time |

## 3. Change Request Process

### 3.1 Submission

All changes must be submitted in Jira (project: CHANGE) with:
- Description and business justification
- Risk classification (Low / Medium / High / Critical)
- Rollback plan
- Affected systems

### 3.2 Testing Requirements

All Normal and Emergency changes must include testing evidence prior to production deployment:
- Staging environment deployment and validation
- Automated test suite results (minimum 95% pass rate)
- Test results attached to the Jira ticket
- High/Critical risk changes additionally require load testing results

### 3.3 CAB Approval

Weekly CAB meeting on Mondays at 11:00 AM ET.
- Members: VP Engineering (Chair), Director of SRE, Security Lead, QA Lead
- Quorum: 3 of 4 members including VP Engineering
- All Normal changes require CAB approval before deployment

### 3.4 Segregation of Duties

- Developers must not deploy their own changes to production
- Production deployments executed by SRE team only
- Peer review required for all code changes (GitHub PR approval)

### 3.5 Post-Implementation Verification

- Change owner verifies deployment within 1 hour
- Automated health checks must pass
- Post-implementation sign-off recorded in Jira

### 3.6 Rollback

If post-deployment health checks fail or error rate exceeds 2% above baseline, rollback must be initiated within 15 minutes. Successful rollbacks are documented in the change ticket and reviewed at next CAB meeting.

## 4. Standard Change Catalog

| ID | Change Type | Conditions |
|----|-------------|------------|
| SC-001 | OS patches (non-kernel) | Auto-rollback enabled |
| SC-002 | Certificate rotations | Automated via cert-manager |
| SC-003 | Minor dependency updates | All CI tests pass |

---

**Next Review Date:** January 2026
