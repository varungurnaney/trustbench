# Physical Security Policy

**Document ID:** POL-PS-025
**Version:** 4.1
**Effective Date:** April 1, 2025
**Owner:** Security Operations
**Classification:** Internal

---

## 1. Purpose

This policy establishes Prism Analytics' physical security requirements to protect personnel, facilities, equipment, and information assets from unauthorized physical access, theft, damage, and environmental hazards.

## 2. Scope

### 2.1 Corporate Office

Prism Analytics' corporate office is located at 2600 Research Park Drive, Suite 500, San Jose, CA 95138.

### 2.2 Data Center

Production infrastructure is hosted at Citadel Colocation, 8800 Mission Boulevard, Fremont, CA 94538.

## 3. Access Control System

### 3.1 Platform

Genetec Security Center with HID SEOS readers at all controlled access points.

### 3.2 Security Zones

| Zone | Classification | Access Control |
|------|---------------|---------------|
| Building Lobby | Semi-Public | Building management key card (business hours open) |
| Suite 500 Entrance | Controlled | Prism badge (AP-SUITE-01) |
| General Office | Controlled | Suite entrance badge |
| Server Room | Restricted | Badge + PIN (AP-SRV-01) |
| Network Closet | Restricted | Badge (AP-NET-01) |
| Executive Area | Restricted | Badge (AP-EXEC-01) |

## 4. Badge Management

### 4.1 Employee Badges

Issued within 1 business day of start date per approved Access Authorization Form (AAF).

### 4.2 Badge Types

| Type | Prefix | Identifier |
|------|--------|-----------|
| Employee | B- | Blue badge with photo |
| Contractor | CTR- | Yellow badge, CONTRACTOR label |
| Visitor | VIS- | Red badge, VISITOR label |

### 4.3 Termination

Badge deactivated within 4 business hours of HR notification. Badge physically collected during exit.

### 4.4 Contractor Lifecycle

Contractor badges activated on or after contract start date. Deactivated within 1 business day of contract end. Monthly contractor access review by Security Manager.

### 4.5 Access Modifications

Changes require new AAF. Restricted zone additions require Infrastructure Director approval.

### 4.6 Quarterly Access Review

The Security Manager conducts a comprehensive review of all active badge authorizations within 15 business days of each quarter's end. The review verifies:
- All active badges correspond to current employees or active contractors
- Access levels are appropriate for current job function
- No stale access (unused badges over 90 days)
- Terminated employee badges are confirmed deactivated

Flagged items must be resolved (access revoked or justified) within 5 business days of the review completion.

## 5. Surveillance

### 5.1 CCTV

Axis cameras at suite entrance, server room, network closet, hallways, and emergency exit. 24/7 recording at 1080p, 15fps.

### 5.2 Retention

90-day retention on Milestone XProtect VMS. Incident footage preserved until investigation closure.

### 5.3 Monitoring

Business hours: reception desk. After hours: motion alerts to on-call Security.

## 6. Visitor Management

### 6.1 Pre-Registration

All visitors must be pre-registered by the host employee via the visitor management system at least 24 hours in advance.

#### 6.1.1 Walk-In Exception

Walk-in visitors (not pre-registered) require real-time approval from the Security Manager before check-in proceeds. The Security Manager's approval must be documented in the visitor log.

### 6.2 Check-In

Government-issued photo ID required. Identity verified against pre-registration or walk-in approval. Temporary badge issued.

### 6.3 Escort

All visitors escorted by host employee at all times. Visitors restricted to General Office zone unless Infrastructure Director approves Restricted zone escorted access.

### 6.4 Badge Return

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

Prism relies on Citadel Colocation for data center physical security. Citadel maintains a SOC 2 Type II report.

### 8.2 Annual Audit

Prism shall conduct annual physical security audits of the colocation provider. Audits must be an independent Prism-initiated audit that verifies Prism-specific controls including authorized access list accuracy, cabinet lock rotation, and Prism-dedicated CCTV coverage. This is in addition to reviewing the provider's SOC 2 report.

### 8.3 Access Management

Only authorized Prism personnel may access Citadel cabinets. Access list reviewed quarterly. Cabinet locks rotated semi-annually.

## 9. Environmental Controls

### 9.1 Standards

Server room: 64-75°F, 40-60% humidity.

### 9.2 Monitoring

Schneider Electric sensors with alerts at >77°F or >55% humidity.

### 9.3 Sensor Calibration

Environmental sensors calibrated every 6 months. Records maintained 3 years.

### 9.4 Fire Suppression

FM-200 system tested annually per NFPA 2001.

---

**Approved by:** Karen Yamamoto, Security Manager
**Approved by:** Thomas Ng, CISO
**Next Review Date:** April 2026
