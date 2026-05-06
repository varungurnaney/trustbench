# Business Continuity Plan — Annual Test Results

**Document ID:** BCP-TEST-2025
**Test Date:** September 18, 2025
**Facilitator:** Diane Marsh, Head of Compliance
**Classification:** Internal

---

## 1. Test Overview

Vantage Cloud Systems conducted its annual Business Continuity Plan (BCP) test on September 18, 2025. The test simulated a complete AWS us-east-1 region failure requiring failover to the us-west-2 disaster recovery site.

## 2. Test Participants

| Name | Role | Attendance |
|------|------|-----------|
| Robert Langston | CEO | Present |
| Margaret Holloway | CISO | Present |
| Yuki Tanaka | Director of Security | Present |
| Carlos Rivera | Security Operations Manager | Present |
| James Wu | VP Engineering | Present |
| Mei Lin | Senior SRE | Present |
| Diane Marsh | Head of Compliance | Present (Facilitator) |

## 3. Test Scenario

**Scenario:** At 10:00 AM ET, a widespread AWS us-east-1 outage occurs. All production services in the primary region become unavailable. The team must execute the DR failover plan.

## 4. Results Summary

| Objective | Target | Actual | Status |
|-----------|--------|--------|--------|
| DR declaration time | 15 minutes | 12 minutes | Pass |
| DNS failover initiation | 30 minutes | 28 minutes | Pass |
| Core platform availability in DR | 2 hours | 1 hour 45 minutes | Pass |
| Customer notification | 1 hour | 52 minutes | Pass |
| Full service restoration | 4 hours | 3 hours 20 minutes | Pass |

## 5. Observations

1. DNS failover was smooth — Route 53 health checks worked as expected.
2. Database replication lag was 45 seconds — within acceptable RTO.
3. Two microservices required manual configuration in DR region (file-processor and notification-service).
4. Customer notification template was slightly outdated — referenced old support email.

## 6. Action Items

| Item | Owner | Due Date | Status |
|------|-------|----------|--------|
| Automate DR config for file-processor and notification-service | James Wu | 2025-11-15 | Complete |
| Update customer notification templates | Diane Marsh | 2025-10-15 | Complete |
| Schedule next BCP test | Diane Marsh | 2026-09-01 | Planned |

---

**Approved by:** Robert Langston, CEO
**Date:** September 25, 2025
