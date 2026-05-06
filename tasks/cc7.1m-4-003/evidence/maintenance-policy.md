# System Maintenance Policy

**Document ID:** POL-MAINT-011
**Version:** 3.4
**Effective Date:** February 10, 2025
**Owner:** IT Operations
**Classification:** Internal

---

## 1. Purpose

This policy defines Keystone Data Services' maintenance practices for all system components.

## 2. Scope

All production, staging, and corporate systems.

## 3. Maintenance Windows

| Window | Schedule | Systems |
|--------|----------|---------|
| MW-PROD | Saturday 02:00-06:00 UTC | Production servers, databases |
| MW-NET | Wednesday 02:00-04:00 UTC | Network equipment |

## 4. Patching

### 4.1 SLAs

| Severity | SLA |
|----------|-----|
| Critical | 14 days |
| High | 30 days |
| Medium | 90 days |
| Low | 180 days |

### 4.2 Patch Exceptions

Patches that cannot be applied within SLA require a documented exception with:

- Business justification explaining why the patch cannot be applied
- Risk assessment of the unpatched vulnerability
- Compensating controls in place
- Planned remediation date
- CISO or IT Director approval

### 4.3 Vendor Dependency

When a patch is unavailable because the vendor has not released a fix, the organization must:

1. Document the vendor's acknowledgment of the issue and expected release timeline
2. Implement available compensating controls
3. Monitor for interim mitigations (workarounds, configuration changes)
4. File a patch exception per Section 4.2

## 5. Vendor Maintenance

### 5.1 Approved Vendors

Only approved vendors may perform maintenance. Vendor access requires CyberArk PAM with session recording.

### 5.2 Vendor Agreements

All vendor maintenance agreements must be current and reviewed annually.

## 6. Documentation

All maintenance documented with date, systems, work performed, and personnel.

---

**Approved by:** Diana Costa, IT Director
**Next Review Date:** February 2026
