# Physical Security Policy

**Document ID:** POL-PS-030
**Version:** 5.0
**Effective Date:** May 1, 2025
**Owner:** Security Operations
**Classification:** Internal

---

## 1. Purpose

This policy establishes Atlas Cloud Services' physical security requirements to protect personnel, facilities, equipment, and information assets from unauthorized physical access, theft, damage, and environmental hazards.

## 2. Scope

### 2.1 Corporate Office

Atlas Cloud Services' corporate office is located at 1800 Technology Plaza, Suite 420, Seattle, WA 98101.

### 2.2 Building Context

The corporate office is located in Technology Plaza, a 14-story Class A multi-tenant office building managed by Cascade Property Group. Atlas occupies Suite 420 on the 4th floor. The building houses approximately 20 tenants across all floors.

### 2.3 Data Center

Production infrastructure is hosted at NorthStar Data Centers, 4500 Columbia Way, Tukwila, WA 98188.

## 3. Access Control Architecture

### 3.1 Security Zones

| Zone | Classification | Controlled By |
|------|---------------|--------------|
| Building Lobby | Semi-Public | Cascade Property Group |
| Building Elevators | Semi-Controlled | Cascade Property Group (badge reader at 4th floor elevator lobby) |
| Building Stairwells | Uncontrolled | Fire code — no badge restriction |
| 4th Floor Elevator Lobby | Controlled | Cascade Property Group (AP-ELEV-04) |
| Suite 420 Entrance | Controlled | Atlas (AP-SUITE-01) |
| General Office | Controlled | Atlas badge access |
| Server Room | Restricted | Atlas badge + PIN (AP-SRV-01) |
| Network Closet | Restricted | Atlas badge (AP-NET-01) |
| Executive Area | Restricted | Atlas badge (AP-EXEC-01) |

### 3.2 Atlas-Controlled Access Points

| Access Point | Location | Authentication |
|-------------|----------|---------------|
| AP-SUITE-01 | Suite 420 entrance | HID SEOS badge |
| AP-SRV-01 | Server room | HID SEOS badge + 4-digit PIN |
| AP-NET-01 | Network closet | HID SEOS badge |
| AP-EXEC-01 | Executive area | HID SEOS badge |
| AP-BACK-01 | Emergency exit | Alarmed push bar |

### 3.3 Building-Level Access

The building lobby is open during business hours (6:00 AM to 9:00 PM) without badge requirements. After 9:00 PM, building entrance requires a Cascade Property Group access card. Cascade issues building cards to Atlas employees along with their Atlas badge.

### 3.4 Stairwell Access

The building stairwell is accessible from all floors without badge requirements due to fire code egress regulations. Stairwell doors on each floor are unlocked from the stairwell side (push to exit for fire egress) and from the hallway side (for re-entry to stairwell). This means any person in the building can travel between floors via the stairwell without badge authentication.

### 3.5 Compensating Controls for Building Access Gaps

Atlas has requested property management install stairwell readers on floors 3-5 — request pending since July 2025. In the interim, Atlas relies on AP-SUITE-01 as the primary physical access barrier. CCTV camera CAM-01 monitors the 4th floor hallway outside Suite 420 to detect unauthorized loitering.

## 4. Badge Management

### 4.1 Employee Badges

Issued within 1 business day of start date per Access Authorization Form.

### 4.2 Badge Types

| Type | Prefix | Access |
|------|--------|--------|
| Employee | B- | Per authorization |
| Contractor | CTR- | Per work order |
| Visitor | VIS- | Suite entrance only, escorted |

### 4.3 Termination

Badge deactivated within 4 business hours of HR notification. Physical badge collected during exit process.

### 4.4 Quarterly Access Review

Security Manager reviews all active badges quarterly within 15 business days of quarter end. Flagged items resolved within 5 business days.

## 5. Surveillance

### 5.1 CCTV

Axis cameras at: 4th floor hallway (CAM-01), suite entrance (CAM-02), server room door (CAM-03), main hallway (CAM-04), emergency exit (CAM-05). 24/7 recording at 1080p.

### 5.2 Retention

90-day retention on Milestone XProtect. Incident footage preserved until case closure.

### 5.3 Monitoring

Business hours: reception monitors suite entrance. After hours: motion alerts to on-call.

## 6. Visitor and Vendor Management

### 6.1 Pre-Registration

All visitors pre-registered 24 hours in advance. Walk-ins require Security Manager approval.

### 6.2 Check-In

Government photo ID verified at reception. Temporary badge issued.

### 6.3 Escort

All visitors escorted at all times. Host employee maintains visual contact.

### 6.4 Restricted Zone Access

Visitors may only access Restricted zones (server room, network closet, executive area) with written pre-approval from the Infrastructure Director. The approval must be documented in the visitor log.

### 6.5 Badge Return

Badges returned at departure. Unreturned badges deactivated same day, incident report filed.

## 7. After-Hours Access

### 7.1 Business Hours

Monday–Friday, 7:00 AM to 7:00 PM Pacific Time.

### 7.2 After-Hours

Manager-approved After-Hours Access Request required.

### 7.3 On-Call

Documented on-call rotations approved by Infrastructure Director grant automatic after-hours access.

## 8. Colocation Data Center

### 8.1 Provider Oversight

Atlas relies on NorthStar Data Centers for physical security. NorthStar maintains SOC 2 Type II certification.

### 8.2 Annual Audit

Atlas shall conduct annual physical security audits of the colocation provider, conducted by Atlas personnel or a qualified third party. This audit is required in addition to the provider's SOC 2 report and must verify Atlas-specific controls including authorized access list accuracy, cabinet lock rotation compliance, and dedicated CCTV row coverage.

### 8.3 Access Management

Only authorized Atlas personnel may access NorthStar cabinets. Access list reviewed quarterly. Cabinet locks rotated semi-annually.

## 9. Environmental Controls

### 9.1 Standards

Server room: 64-75°F, 40-60% humidity.

### 9.2 Monitoring

Schneider Electric sensors with alerts at >77°F or >55% humidity.

### 9.3 Sensor Calibration

Environmental sensors calibrated every 6 months by qualified technician. Records maintained 3 years.

### 9.4 Fire Suppression

FM-200 system tested annually per NFPA 2001.

---

**Approved by:** Nathan Reeves, CISO
**Approved by:** Raj Kapoor, Infrastructure Director
**Next Review Date:** May 2026
