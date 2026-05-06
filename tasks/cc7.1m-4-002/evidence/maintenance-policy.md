# System Maintenance Policy

**Document ID:** POL-MAINT-009
**Version:** 3.2
**Effective Date:** January 15, 2025
**Owner:** IT Operations
**Classification:** Internal

---

## 1. Purpose

This policy defines Bastion Technologies' system maintenance practices.

## 2. Scope

All production systems, network infrastructure, and physical equipment.

## 3. Maintenance Windows

| Window | Schedule | Systems |
|--------|----------|---------|
| MW-PROD | Saturday 02:00-06:00 UTC | Production servers, databases |
| MW-NET | Wednesday 02:00-04:00 UTC | Network equipment |
| MW-EQUIP | First Saturday of each month, 06:00-12:00 UTC | Physical equipment (UPS, HVAC, generators) |

## 4. Patching

### 4.1 Patch SLAs

| Severity | SLA |
|----------|-----|
| Critical | 14 days |
| High | 30 days |
| Medium | 90 days |
| Low | 180 days |

### 4.2 Patch Testing

All patches tested in staging before production deployment.

## 5. Equipment Maintenance

### 5.1 Preventive Maintenance Schedule

| Equipment | Maintenance Interval | Activities |
|-----------|---------------------|------------|
| UPS Systems | Quarterly | Battery load test, visual inspection, firmware check |
| HVAC Units | Monthly | Filter replacement, temperature calibration |
| Diesel Generators | Quarterly | Test run (30 min), fuel level check, oil and filter change |
| Fire Suppression | Semi-annually | Agent level check, detector calibration, panel test |
| Network Equipment | Annually | Physical inspection, cable management, fan cleaning |

### 5.2 Maintenance Records

All equipment maintenance must be recorded with date, equipment ID, work performed, technician, result, and next scheduled date.

### 5.3 Overdue Maintenance

Equipment maintenance overdue by more than 30 days must be escalated to the IT Director. Equipment with maintenance overdue by more than 90 days must be assessed for operational risk.

## 6. Change Management

All maintenance requires a change ticket. Emergency maintenance requires CISO or IT Director approval.

## 7. Vendor Maintenance

Only approved vendors may perform maintenance. Vendor access per Section 6.2 of the Access Control Policy.

---

**Approved by:** Clara Rodriguez, IT Director
**Next Review Date:** January 2026
