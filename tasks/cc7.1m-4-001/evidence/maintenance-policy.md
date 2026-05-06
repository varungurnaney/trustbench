# System Maintenance Policy

**Document ID:** POL-MAINT-007
**Version:** 3.6
**Effective Date:** February 1, 2025
**Owner:** IT Operations
**Classification:** Internal

---

## 1. Purpose

This policy defines Ironclad Services' system maintenance practices for infrastructure, applications, and vendor-managed components.

## 2. Scope

All production systems, network equipment, and physical infrastructure managed by Ironclad Services.

## 3. Maintenance Windows

### 3.1 Standard Windows

| Window | Schedule | Systems |
|--------|----------|---------|
| MW-PROD | Saturday 02:00-06:00 UTC | Production servers, databases |
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

## 5. Change Management

### 5.1 Change Tickets

All maintenance activities require a change ticket (ServiceNow) that includes: description of work, systems affected, risk assessment, rollback plan, and approval.

### 5.2 Emergency Changes

Emergency maintenance without a pre-approved change ticket requires:

1. Verbal authorization from CISO, CTO, or IT Director
2. Change ticket created retroactively within 4 hours
3. Post-incident review within 72 hours

## 6. Vendor Maintenance

### 6.1 Approved Vendor List

Only vendors on the Approved Vendor List may perform maintenance. The list is maintained by Procurement and reviewed quarterly.

**Current Approved Vendor List (as of January 2025):**

| Vendor | Scope | Agreement Expiry |
|--------|-------|-----------------|
| Dell Technologies | Server hardware, SAN storage | March 2026 |
| Cisco Systems | Network switches, routers | June 2026 |
| Fortinet | Firewalls, IPS | September 2026 |
| VMware (Broadcom) | Hypervisor, vCenter | December 2025 |
| Oracle | Database licensing and support | March 2026 |
| Schneider Electric | UPS, PDU, cooling | December 2026 |

### 6.2 Vendor Access

- Remote vendor sessions via CyberArk Vendor PAM with session recording
- On-site vendor work supervised by Ironclad employee
- All vendor activities documented in Vendor Access Log

### 6.3 Unauthorized Vendor Access

Maintenance performed by vendors not on the Approved Vendor List is a policy violation that must be reported to the IT Director within 24 hours.

---

**Approved by:** Nathan Cross, IT Director
**Next Review Date:** February 2026
