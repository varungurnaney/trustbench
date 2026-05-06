# Physical Security Policy

**Document ID:** POL-PS-022
**Version:** 3.8
**Effective Date:** March 15, 2025
**Owner:** Security and Facilities
**Classification:** Internal

---

## 1. Purpose

This policy establishes Meridian Software's physical security requirements to protect personnel, facilities, equipment, and information assets from unauthorized access, theft, damage, and environmental hazards.

## 2. Scope and Facility Description

### 2.1 Corporate Office

Meridian Software's corporate office is located at 900 Commerce Boulevard, Suite 400, Portland, OR 97201.

### 2.2 Building Context

The corporate office is located in a multi-tenant Class A office building ("Commerce Tower"). Meridian occupies the entire 4th floor (Suite 400). The building is shared with approximately 15 other tenants across 12 floors. Building common areas (lobby, elevators, stairwells, parking garage, loading dock) are managed by Greystone Property Management.

### 2.3 Data Center

Meridian's production infrastructure is hosted at SecureVault Colocation, 12000 Data Park Drive, Hillsboro, OR.

## 3. Access Control Architecture

### 3.1 Security Zones

| Zone | Classification | Controlled By |
|------|---------------|--------------|
| Building Lobby | Public (business hours) | Greystone Property Management |
| Building Elevators/Stairs | Semi-Public | Greystone Property Management |
| Suite 400 Entrance | Controlled | Meridian (AP-SUITE-01) |
| General Office | Controlled | Meridian badge access |
| Server Room | Restricted | Meridian badge + PIN (AP-SRV-01) |
| Executive Suite | Restricted | Meridian badge (AP-EXEC-01) |

### 3.2 Meridian-Controlled Access Points

Badge access is enforced at the 4th floor suite entrance (AP-SUITE-01). All Meridian-controlled access points use the Genetec Security Center platform with HID SEOS credentials. The suite entrance (AP-SUITE-01) is the primary perimeter control for all Meridian space.

### 3.3 Building-Level Access

Meridian relies on property management building access controls as the first layer of physical security. The building lobby is open during business hours (6:00 AM to 8:00 PM) for tenant and visitor access. After 8:00 PM, building access requires a property management key card issued to each tenant's employees.

### 3.4 Access Points Detail

| Access Point | Location | Authentication |
|-------------|----------|---------------|
| AP-SUITE-01 | 4th floor suite entrance | HID SEOS badge |
| AP-SRV-01 | Server room door | HID SEOS badge + 4-digit PIN |
| AP-EXEC-01 | Executive suite | HID SEOS badge |
| AP-BACK-01 | Suite rear exit (emergency) | Alarmed push bar, badge for re-entry |

## 4. Badge Management

### 4.1 Employee Badges

Issued within 1 business day of start date. Access levels per approved Access Authorization Form.

### 4.2 Badge Types

| Type | Prefix | Access |
|------|--------|--------|
| Employee | B- | Per authorization |
| Contractor | CTR- | Per work order scope |
| Visitor | VIS- | Suite entrance only, escorted |

### 4.3 Termination

Badge deactivation within 4 hours of HR notification. Physical badge collected during exit.

### 4.4 Quarterly Review

All badge access reviewed quarterly by Security Manager.

## 5. Surveillance

### 5.1 CCTV

Axis cameras at suite entrance, server room door, hallways, and emergency exit. 24/7 recording.

### 5.2 Retention

90-day retention on Milestone XProtect. Incident footage preserved until case closure.

### 5.3 Monitoring

Business hours: reception desk monitors suite entrance camera. After hours: motion alerts to on-call.

## 6. Visitor Management

### 6.1 Pre-Registration and Escort

All visitors pre-registered and escorted. Visitors restricted to General Office zone.

### 6.2 Check-In

Government-issued photo ID required. Temporary badge issued.

### 6.3 Badge Return

Badges returned at departure. Unreturned badges deactivated same day, incident report filed.

## 7. After-Hours Access

### 7.1 Business Hours

Monday–Friday, 7:00 AM to 7:00 PM Pacific Time.

### 7.2 After-Hours

Requires manager-approved After-Hours Access Request.

### 7.3 On-Call

Documented on-call rotations approved by Infrastructure Director grant automatic after-hours access.

## 8. Colocation Data Center

### 8.1 Provider Oversight

Meridian relies on SecureVault Colocation for physical security of the data center facility. SecureVault maintains a SOC 2 Type II report covering physical security controls.

### 8.2 Annual Audit

Meridian shall conduct annual physical security audits of the colocation provider, conducted by Meridian personnel or a qualified third party, to verify that the provider's physical controls meet Meridian's requirements. Audits must include verification of access list accuracy, cabinet lock integrity, CCTV coverage, and environmental controls. This audit is independent of and in addition to the provider's SOC 2 report.

### 8.3 Access Management

Only authorized Meridian personnel may access SecureVault cabinets. The authorized access list is reviewed quarterly and updated within 24 hours of personnel changes. Cabinet lock codes are rotated semi-annually.

## 9. Environmental Controls

### 9.1 Server Room Standards

Temperature maintained between 64-75°F. Humidity maintained between 40-60%.

### 9.2 Monitoring

Temperature and humidity sensors report to the Schneider Electric BMS. Alerts trigger when temperature exceeds 77°F or humidity exceeds 55%.

### 9.3 Sensor Calibration

All environmental monitoring sensors shall be calibrated every 6 months by a qualified technician. Calibration records must be maintained for 3 years.

### 9.4 Fire Suppression

FM-200 clean agent fire suppression in server room. System tested annually per NFPA 2001.

---

**Approved by:** Kathryn Delgado, CISO
**Approved by:** Ian Foster, Infrastructure Director
**Next Review Date:** March 2026
