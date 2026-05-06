# System Maintenance Policy

**Document ID:** POL-MAINT-017
**Version:** 4.0
**Effective Date:** January 30, 2025
**Owner:** IT Operations
**Classification:** Internal

---

## 1. Purpose

This policy defines Apex Infrastructure Group's system maintenance practices for all technology components.

## 2. Scope

All production, staging, corporate systems and physical infrastructure.

## 3. Maintenance Windows

### 3.1 Standard Windows

| Window | Schedule | Notification |
|--------|----------|-------------|
| MW-PROD | Saturday 02:00-06:00 UTC | 48 hours advance notice |
| MW-NET | Wednesday 02:00-04:00 UTC | 48 hours advance notice |
| MW-EQUIP | First Saturday 08:00-14:00 UTC | 1 week advance notice |

### 3.2 Emergency Maintenance

Emergency maintenance outside windows requires CISO or CTO approval. Change ticket created retroactively within 4 hours. Post-incident review within 72 hours.

## 4. Patching

### 4.1 SLAs

| Severity | SLA |
|----------|-----|
| Critical | 14 days |
| High | 30 days |
| Medium | 90 days |
| Low | 180 days |

### 4.2 Patch Windows

Critical/High patches deployed in the next available MW-PROD or via emergency window. Medium/Low patches bundled into monthly patch cycles.

## 5. Equipment Maintenance

### 5.1 Schedule

| Equipment | Interval |
|-----------|----------|
| UPS | Quarterly |
| HVAC | Monthly |
| Generators | Quarterly |
| Fire Suppression | Semi-annually |
| PDUs | Quarterly |

### 5.2 Overdue Thresholds

| Days Overdue | Action |
|-------------|--------|
| 1-30 | Notify owner |
| 31-60 | Escalate to IT Director |
| 61-90 | Escalate to CTO, risk assessment required |
| 90+ | CTO must approve continued operation |

## 6. Vendor Maintenance

### 6.1 Approved Vendors

Only vendors on the Approved Vendor List may perform maintenance.

### 6.2 Vendor Access

Remote sessions via CyberArk PAM with session recording. On-site work supervised by Apex employee. All activities logged in Vendor Access Log.

### 6.3 Vendor Agreements

Agreements must be current and reviewed annually before renewal.

### 6.4 Vendor SLAs

Vendor response and resolution SLAs are defined in each vendor agreement. Vendor SLA breaches must be documented and escalated to the vendor account manager.

## 7. Maintenance Reporting

### 7.1 Monthly Reports

Monthly maintenance reports must include:

- All maintenance activities performed
- Patch compliance rates by severity
- Equipment maintenance compliance
- Overdue items with justification
- Vendor SLA compliance

### 7.2 Quarterly Reviews

Quarterly maintenance program reviews conducted by the IT Director to assess overall program health, identify trends, and address systemic issues.

---

**Approved by:** Sandra Mitchell, CTO
**Next Review Date:** January 2026
