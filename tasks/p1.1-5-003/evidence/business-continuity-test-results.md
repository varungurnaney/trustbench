# Solaris Insurance — Business Continuity Test Results

**Test Date:** October 18, 2025
**Test Type:** Tabletop Exercise + Partial Technical Failover
**Facilitator:** Brian Nolan, Head of Operations
**Participants:** Engineering, Claims, Operations, Customer Support leadership

---

## Scenario

Simulated complete failure of the primary AWS eu-west-1 (Dublin) region requiring failover to disaster recovery site in eu-central-1 (Frankfurt).

## Objectives

1. Validate RTO (Recovery Time Objective): 4 hours
2. Validate RPO (Recovery Point Objective): 1 hour
3. Test communication and escalation procedures
4. Verify data integrity after failover

## Results

| Objective | Target | Actual | Status |
|-----------|--------|--------|--------|
| RTO | 4 hours | 3 hours 15 minutes | PASS |
| RPO | 1 hour | 45 minutes | PASS |
| Communication escalation | 15 minutes to leadership | 12 minutes | PASS |
| Data integrity check | Zero data loss | Zero data loss confirmed | PASS |

## Key Observations

1. DNS failover completed within 8 minutes (automated Route 53 health checks)
2. Database replica promotion to primary completed in 22 minutes
3. Application services healthy in DR region within 2 hours 40 minutes
4. Customer-facing services restored progressively: quote engine first, then policy management, then claims portal
5. SMS notifications to affected policyholders sent within 45 minutes of incident declaration

## Action Items

| Item | Owner | Due Date |
|------|-------|----------|
| Automate application service deployment in DR region | Engineering | December 2025 |
| Add claims portal to priority-1 restoration group | Operations | November 2025 |
| Update runbook with Frankfurt-specific configuration | SRE | November 2025 |

## Overall Assessment

Business continuity capabilities meet defined RTO and RPO targets. DR failover process is well-documented and rehearsed. Recommend annual full failover test and semi-annual tabletop exercises.
