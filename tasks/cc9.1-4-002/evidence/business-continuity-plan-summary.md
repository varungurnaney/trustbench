# Business Continuity Plan Summary

**Document ID:** DOC-BCP-001
**Version:** 2.0
**Last Updated:** September 2025

---

## 1. Overview

Prism Data Inc. maintains a comprehensive business continuity plan to ensure continued operations during disruptive events.

## 2. Disaster Recovery Sites

| Site | Location | Purpose |
|------|----------|---------|
| Primary | us-east-1 (N. Virginia) | Production workloads |
| DR | us-west-2 (Oregon) | Failover site |

## 3. Recovery Objectives

- **RTO:** 4 hours for Tier 1 services
- **RPO:** 1 hour for database systems

## 4. Annual DR Test

The most recent DR failover test was conducted August 15, 2025. All Tier 1 services failed over successfully within 3 hours 20 minutes.

## 5. Key Dependencies

- AWS multi-region architecture
- Cross-region database replication
- Route 53 health checks for DNS failover

---

**Approved by:** Marcus Webb, CISO
