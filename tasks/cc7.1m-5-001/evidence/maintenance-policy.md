# System Maintenance Policy

**Document ID:** POL-MAINT-013
**Version:** 4.2
**Effective Date:** January 25, 2025
**Owner:** IT Operations
**Classification:** Internal

---

## 1. Purpose

This policy defines Sentinel Infrastructure Corp's maintenance practices for all system components including servers, network equipment, databases, and physical infrastructure.

## 2. Scope

All production, staging, and corporate systems and physical infrastructure.

## 3. Maintenance Windows

| Window | Schedule | Systems |
|--------|----------|---------|
| MW-PROD | Saturday 02:00-06:00 UTC | Production servers, databases |
| MW-NET | Wednesday 02:00-04:00 UTC | Network equipment |
| MW-EQUIP | First Saturday, 08:00-14:00 UTC | Physical equipment |

## 4. Patching

### 4.1 Patch SLAs

| Severity | SLA |
|----------|-----|
| Critical | 14 days |
| High | 30 days |
| Medium | 90 days |
| Low | 180 days |

### 4.2 Patch Deployment

Patches tested in staging before production. Monthly patch cycles for Medium/Low. Emergency process for Critical/High.

## 5. Equipment Maintenance

### 5.1 Preventive Maintenance Schedule

| Equipment | Interval | Activities |
|-----------|----------|------------|
| UPS Systems | Quarterly (90 days) | Battery load test (30 min at 80% load), visual inspection, firmware check |
| HVAC Units | Monthly | Filter replacement, temperature/humidity calibration |
| Diesel Generators | Quarterly (90 days) | 30-min load test at 75% capacity, oil change, filter replacement, coolant check |
| Fire Suppression | Semi-annually | Agent level check, detector calibration, panel test |
| PDUs | Quarterly (90 days) | Thermal imaging, load balance verification, firmware check |

### 5.2 Overdue Maintenance Thresholds

| Days Overdue | Action Required |
|-------------|-----------------|
| 1-30 days | Notify equipment owner. Schedule within next maintenance window. |
| 31-60 days | Escalate to IT Director. Provide written justification for delay. |
| 61-90 days | Escalate to CTO. Operational risk assessment required. |
| 90+ days | Equipment classified as "Maintenance Non-Compliant." CTO must approve continued operation. Documented risk acceptance required. |

### 5.3 Equipment Operational Status

Equipment that is functioning normally does NOT exempt it from preventive maintenance requirements. Preventive maintenance is designed to detect degradation before failure occurs. Equipment may test normally while developing latent issues (e.g., battery cells with reduced capacity, generator fuel contamination, HVAC refrigerant leaks) that only manifest under stress or over time.

## 6. Change Management

All maintenance requires a change ticket. Emergency maintenance requires CISO/CTO approval.

## 7. Vendor Maintenance

Approved vendors only. Remote sessions via CyberArk PAM. Agreements reviewed annually.

---

**Approved by:** Roger Bennett, CTO
**Next Review Date:** January 2026
