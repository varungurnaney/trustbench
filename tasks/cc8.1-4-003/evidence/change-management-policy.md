# Change Management Policy

**Document ID:** POL-CHG-017
**Version:** 3.1
**Effective Date:** February 1, 2025
**Owner:** Engineering
**Approved By:** Nathan Cole, VP Engineering

---

## 1. Purpose

This policy governs all changes to Meridian Analytics production systems to ensure controlled, authorized, and auditable modifications.

## 2. Change Categories

| Category | Description | Approval | Deployment Window |
|----------|-------------|----------|--------------------|
| Standard | Pre-approved per catalog | None | Business hours |
| Normal | Non-routine changes | CAB approval | Saturday 02:00-06:00 UTC |
| Emergency | Active Sev 1/2 remediation | VP Eng + CISO dual approval; retro CAB within 5 business days | Any time |

## 3. Change Request Process

### 3.1 Submission

All changes require a Jira ticket with:
- Description and scope
- Risk classification (Low / Medium / High / Critical)
- Rollback plan
- Testing evidence

### 3.2 Testing

- All Normal changes must be tested in staging and pass automated test suite
- Test results attached to Jira ticket
- High/Critical risk: security review required by Security Engineering

### 3.3 CAB

Weekly meeting on Tuesdays at 2pm ET.
- Members: VP Engineering (Chair), SRE Director, Security Lead, Engineering Manager
- Quorum: VP Engineering + 2 other members

### 3.4 Segregation of Duties

- Developer must not approve or deploy their own change
- Production deployments by SRE team only

### 3.5 Post-Implementation

- Verification within 2 hours
- Automated monitoring for 24 hours post-deployment
- Sign-off in Jira

## 4. Emergency Changes

Emergency changes require dual verbal approval from VP Engineering AND CISO. This is a higher bar than standard emergency processes because Meridian Analytics handles financial data subject to regulatory requirements.

Retrospective CAB review must occur within 5 business days.

## 5. Maintenance Windows

All Normal changes must be deployed during the Saturday 02:00-06:00 UTC maintenance window unless a business justification exception is approved by the CAB.

---

**Next Review Date:** February 2026
