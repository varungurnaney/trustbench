# System Maintenance Policy

**Document ID:** POL-MAINT-003
**Version:** 3.1
**Effective Date:** January 10, 2025
**Owner:** IT Operations
**Classification:** Internal

---

## 1. Purpose

This policy defines Ridgeline Systems' system maintenance practices for all infrastructure and application components.

## 2. Scope

All production systems, staging environments, and corporate infrastructure managed by Ridgeline Systems.

## 3. Maintenance Windows

### 3.1 Standard Maintenance Windows

| Window | Day | Time (UTC) | Systems |
|--------|-----|------------|---------|
| MW-PROD-1 | Saturday | 02:00 - 06:00 | Production servers, databases |
| MW-PROD-2 | Wednesday | 02:00 - 04:00 | Production network equipment |
| MW-CORP | Sunday | 00:00 - 06:00 | Corporate infrastructure |
| MW-DB | Saturday | 04:00 - 08:00 | Database maintenance (index rebuilds, statistics) |

### 3.2 Maintenance Window Requirements

- All planned maintenance must be performed within designated maintenance windows
- Maintenance activities must be completed before the window closes
- Maintenance outside designated windows requires emergency change approval (Section 6)
- Stakeholders must be notified at least 48 hours before planned maintenance

## 4. Patching

### 4.1 Patch Schedule

| Severity | SLA | Deployment Window |
|----------|-----|-------------------|
| Critical | 14 calendar days | Emergency (any time with approval) |
| High | 30 calendar days | Next available MW-PROD |
| Medium | 90 calendar days | Monthly patch cycle (first Saturday) |
| Low | 180 calendar days | Quarterly patch cycle |

### 4.2 Patch Testing

All patches must be tested in staging before production deployment.

### 4.3 Patch Records

All patch deployments must be recorded with: date/time, system, patch ID, deployer, change ticket, and result.

## 5. Vendor Maintenance

Vendor maintenance activities must occur within designated maintenance windows unless emergency authorization is granted.

## 6. Emergency Maintenance

Emergency maintenance outside maintenance windows requires approval from the IT Director or designee. All emergency maintenance must be documented with justification.

---

**Approved by:** Helen Santos, IT Director
**Next Review Date:** January 2026
