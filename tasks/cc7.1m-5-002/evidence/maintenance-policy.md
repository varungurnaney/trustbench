# System Maintenance Policy

**Document ID:** POL-MAINT-015
**Version:** 3.8
**Effective Date:** February 20, 2025
**Owner:** IT Operations
**Classification:** Internal

---

## 1. Purpose

This policy defines Aegis Platform Services' system maintenance practices.

## 2. Scope

All production and corporate systems.

## 3. Maintenance Windows

| Window | Schedule |
|--------|----------|
| MW-PROD | Saturday 02:00-06:00 UTC |
| MW-NET | Wednesday 02:00-04:00 UTC |

## 4. Patching

### 4.1 SLAs

| Severity | SLA |
|----------|-----|
| Critical | 14 days |
| High | 30 days |
| Medium | 90 days |
| Low | 180 days |

### 4.2 Vendor Dependency

When a patch SLA cannot be met because the vendor has not released a fix:

1. The vulnerability must be documented with vendor tracking reference
2. Compensating controls must be implemented and documented
3. The vendor's expected release timeline must be obtained and tracked
4. A formal patch exception must be filed per Section 4.3
5. The exception must be reviewed monthly until the patch is available
6. **Interim mitigations:** The organization must actively pursue and implement any available interim mitigations including workarounds, configuration hardening, network isolation, and enhanced monitoring

### 4.3 Patch Exceptions

Exceptions require:

- CISO approval for Critical/High, IT Director for Medium/Low
- Documented compensating controls
- Monthly review
- Maximum exception duration: 6 months (renewable with re-approval)

### 4.4 Escalation

Patches overdue by more than 2x the SLA without an approved exception must be escalated to the CTO.

## 5. Vendor Agreements

All vendor maintenance agreements must be current. Agreements reviewed annually.

## 6. Equipment Maintenance

Quarterly preventive maintenance for UPS, generators, PDUs. Monthly for HVAC. Overdue maintenance escalated per threshold table.

---

**Approved by:** William Torres, CTO
**Next Review Date:** February 2026
