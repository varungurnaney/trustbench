# Change Management Policy

**Document ID:** POL-CHG-021
**Version:** 4.0
**Effective Date:** March 1, 2025
**Owner:** Engineering
**Approved By:** Sanjay Reddy, VP Engineering

---

## 1. Purpose

This policy governs all changes to Apex Cloud Solutions production systems to ensure controlled, authorized, and auditable modifications in compliance with SOC 2 Trust Services Criteria.

## 2. Change Categories

| Category | Description | Approval | Deployment Window |
|----------|-------------|----------|--------------------|
| Standard | Pre-approved per catalog | None required | Business hours |
| Normal | Non-routine changes | CAB approval | Wednesday-Friday 10:00-16:00 ET |
| Emergency | Active Sev 1/2 remediation | VP Eng verbal + retro CAB within 5 business days | Any time |

## 3. Change Request Process

### 3.1 Submission

All changes require a ServiceNow ticket with:
- Description and scope
- Risk classification (Low / Medium / High / Critical)
- Impact assessment
- Rollback plan
- Testing evidence

### 3.2 Testing

All Normal changes must pass:
- Staging environment validation
- Automated test suite (minimum 97% pass rate)
- Test results recorded in ServiceNow

High/Critical risk: Security review required.

### 3.3 Change Advisory Board

The CAB meets weekly on Tuesdays at 2:00 PM ET to review and approve Normal changes.

**CAB Membership:**
- Sanjay Reddy, VP Engineering (Chair)
- Patricia Okafor, Director of SRE
- Michael Chen, Security Engineering Lead
- Anya Volkov, QA Director

**Quorum:** VP Engineering + at least 2 other CAB members must be present.

**CAB Responsibilities:**
- Review change requests for completeness and risk assessment accuracy
- Approve or reject changes based on risk, impact, and testing evidence
- Review emergency change retrospectives
- Track change success metrics

All approvals must be documented in the ServiceNow change ticket with individual member approval and timestamp.

### 3.4 Segregation of Duties

- Developer must not approve or deploy their own change
- Production deployments executed by SRE team
- Peer review required (GitHub PR approval)

### 3.5 Post-Implementation

- Verification within 2 hours
- Post-deployment monitoring for 24 hours
- Sign-off recorded in ServiceNow

## 4. Change Freeze

Holiday freeze: December 20 - January 5. Emergency changes only with CISO approval.

---

**Next Review Date:** March 2026
