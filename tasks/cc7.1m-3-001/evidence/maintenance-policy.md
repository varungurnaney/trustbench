# System Maintenance Policy

**Document ID:** POL-MAINT-005
**Version:** 4.0
**Effective Date:** January 20, 2025
**Owner:** IT Operations
**Classification:** Internal

---

## 1. Purpose

This policy defines Silverline Industries' system maintenance practices to ensure continued availability, security, and performance of all system components.

## 2. Scope

All production systems, network equipment, physical infrastructure, and vendor-managed components.

## 3. Maintenance Windows

### 3.1 Standard Windows

| Window | Schedule | Systems |
|--------|----------|---------|
| MW-PROD | Saturday 02:00-06:00 UTC | Production servers |
| MW-NET | Wednesday 02:00-04:00 UTC | Network equipment |
| MW-CORP | Sunday 00:00-06:00 UTC | Corporate infrastructure |

### 3.2 All planned maintenance must occur within designated windows.

## 4. Patching

### 4.1 Patch SLAs

| Severity | SLA |
|----------|-----|
| Critical | 14 days |
| High | 30 days |
| Medium | 90 days |
| Low | 180 days |

## 5. Vendor Maintenance

### 5.1 Vendor Access Requirements

Third-party vendors performing maintenance on Silverline Industries systems must comply with the following requirements:

1. **Active agreement:** Vendor must be covered by a current, signed maintenance agreement
2. **Advance notice:** Vendor must provide at least 48 hours advance notice for planned maintenance
3. **Escort requirement:** All on-site vendor maintenance activities must be supervised by a Silverline Technologies employee at all times
4. **Remote access logging:** All remote vendor maintenance sessions must be conducted through the designated vendor access portal (CyberArk Vendor PAM) with full session recording enabled. Session recordings are retained for 90 days.
5. **Access logging:** All vendor maintenance activities — both on-site and remote — must have corresponding entries in the Vendor Access Log documenting: date/time, vendor name, technician name, systems accessed, work performed, and supervising Silverline employee (for on-site) or session recording ID (for remote)
6. **Credential management:** Vendor credentials are provisioned for the duration of the maintenance activity only and revoked upon completion

### 5.2 Vendor Approval List

Only vendors on the Approved Vendor List maintained by the Procurement team may perform maintenance on Silverline systems. The list is reviewed quarterly.

## 6. Documentation

All maintenance activities must be documented with date, time, systems, work performed, and personnel.

---

**Approved by:** Victor Marsh, IT Director
**Next Review Date:** January 2026
