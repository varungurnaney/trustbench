# Physical Security Policy

**Document ID:** POL-PS-007
**Version:** 4.2
**Effective Date:** February 15, 2025
**Owner:** Security Operations
**Classification:** Internal

---

## 1. Purpose

This policy establishes Helios Systems' requirements for physical access controls to protect facilities, equipment, and information assets from unauthorized access, theft, damage, and interference.

## 2. Scope

This policy applies to all Helios Systems facilities including the corporate office at 1450 Meridian Parkway, Raleigh, NC, and the disaster recovery site at 3200 Commerce Way, Charlotte, NC.

## 3. Access Control System

### 3.1 Badge Access System

Helios Systems uses the Genetec Synergis access control system with HID iCLASS SE proximity readers installed at all controlled entry points. The system logs all badge swipe events including timestamp, badge ID, access point, and grant/deny result.

### 3.2 Access Points

| Access Point | Location | Zone | Reader Type |
|-------------|----------|------|------------|
| AP-MAIN-01 | Main lobby entrance | General Office | HID iCLASS SE |
| AP-MAIN-02 | Rear employee entrance | General Office | HID iCLASS SE |
| AP-FLOOR2-01 | 2nd floor stairwell | General Office | HID iCLASS SE |
| AP-FLOOR3-01 | 3rd floor elevator lobby | General Office | HID iCLASS SE |
| AP-SRV-01 | Server room A | Restricted | HID iCLASS SE + PIN |
| AP-SRV-02 | Server room B | Restricted | HID iCLASS SE + PIN |
| AP-NET-01 | Network closet | Restricted | HID iCLASS SE |
| AP-EXEC-01 | Executive suite | Restricted | HID iCLASS SE |
| AP-DOCK-01 | Loading dock | General Office | HID iCLASS SE |

## 4. Badge Management

### 4.1 Issuance

Badges are issued by the Facilities team upon receipt of a completed Access Request Form (ARF) approved by the employee's direct manager. Restricted zone access requires additional approval from the Security Manager.

### 4.2 Badge Types

| Badge Type | Color | Access Level |
|-----------|-------|-------------|
| Employee | Blue | Per ARF authorization |
| Contractor | Yellow | Per contract scope, sponsor required |
| Visitor | Orange | Lobby only, must be escorted |
| Executive | Silver | All zones |

### 4.3 Termination and Deactivation

Upon notification of employee separation (voluntary or involuntary), the Facilities team must deactivate the employee's badge within 24 hours of the termination effective date. The badge must be physically collected by the departing employee's manager or HR representative on the last day of employment. Deactivation is logged in the access control system.

### 4.4 Quarterly Access Review

All badge access authorizations are reviewed quarterly by the Security Manager in coordination with department heads. Stale access (employees who have not used their badge in 90+ days) is flagged for review.

## 5. Surveillance

### 5.1 CCTV System

Helios Systems operates a Milestone XProtect VMS with 24 IP cameras covering all entry points, hallways, server rooms, and parking areas. Cameras record at 1080p, 15 fps.

### 5.2 Monitoring

CCTV feeds are monitored during business hours by the reception security desk. After-hours monitoring uses motion-detection alerts sent to the on-call Facilities team member.

### 5.3 Retention

All CCTV footage shall be retained for a minimum of 90 days. Footage related to security incidents shall be preserved indefinitely until the incident investigation is closed.

## 6. Visitor Management

### 6.1 Registration

All visitors must be pre-registered by the host employee via the visitor management portal at least 24 hours in advance. Walk-in visitors require real-time approval from the host employee.

### 6.2 Check-In

Visitors present government-issued photo ID at reception. The receptionist verifies identity against the pre-registration record and issues a temporary visitor badge.

### 6.3 Escort

All visitors must be escorted by the host employee at all times while on premises. Visitors must not be left unattended in any area.

### 6.4 Check-Out

Visitor badges are returned at reception upon departure. The receptionist logs the departure time. Badges not returned by end of business are flagged and deactivated.

## 7. Environmental Controls

### 7.1 Server Room Environmental Monitoring

Temperature and humidity sensors in server rooms A and B report to the Schneider Electric EcoStruxure platform. Alerts trigger at temperature above 78F or humidity above 60%.

---

## Appendix A: System Configuration Summary

| System | Parameter | Configured Value |
|--------|-----------|-----------------|
| Genetec Synergis | Badge format | HID iCLASS SE 32-bit |
| Genetec Synergis | Failed attempt lockout | 3 attempts, 15-minute lockout |
| Genetec Synergis | Anti-passback | Enabled, hard anti-passback |
| Milestone XProtect | Recording resolution | 1080p |
| Milestone XProtect | Frame rate | 15 fps |
| Milestone XProtect | Retention period | 30 days |
| Milestone XProtect | Motion detection sensitivity | Medium |
| Schneider EcoStruxure | Temperature alert threshold | 78°F |
| Schneider EcoStruxure | Humidity alert threshold | 60% |

---

**Approved by:** Jonathan Park, CISO
**Approved by:** Lisa Brennan, VP of Operations
**Next Review Date:** February 2026
