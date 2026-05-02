# Atlas Cloud — System Uptime Report Q4 2025

**Report Period:** October 1, 2025 — December 31, 2025  
**Generated:** January 2, 2026  
**Author:** Infrastructure Operations Team  
**Classification:** Internal

---

## Overall Platform Availability

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| **Overall Platform Uptime** | 99.95% | 99.97% | Exceeded |
| **API Gateway Uptime** | 99.99% | 99.99% | Met |
| **Database Availability** | 99.95% | 99.96% | Exceeded |
| **Authentication Service** | 99.99% | 99.98% | Below Target |

## Monthly Breakdown

### October 2025
- **Uptime:** 99.99%
- **Total Downtime:** 4 minutes 22 seconds
- **Incidents:** 1 minor (INC-2025-Q4-014 — EC2 instance launched outside IaC pipeline, no customer impact)

### November 2025
- **Uptime:** 99.98%
- **Total Downtime:** 8 minutes 41 seconds
- **Incidents:** 2 minor incidents; credential stuffing attack mitigated with no service impact; red team exercise caused brief false alarm

### December 2025
- **Uptime:** 99.94%
- **Total Downtime:** 26 minutes 12 seconds
- **Incidents:** RDS Multi-AZ failover (INC-2025-Q4-041) caused 37-second failover + 90 seconds of elevated error rates; eu-west-1 latency issue (INC-2025-Q4-045) impacted EU customers for approximately 22 minutes

## Service-Level Breakdown

| Service | Uptime | Incidents |
|---------|--------|-----------|
| api-gateway | 99.99% | 0 |
| user-auth-service | 99.98% | 1 (latency spike during DB failover) |
| payment-processor | 99.99% | 0 |
| customer-data-api | 99.96% | 1 (DB failover) |
| notification-service | 99.99% | 0 |
| reporting-engine | 99.97% | 0 |
| file-storage-service | 99.99% | 0 |
| search-indexer | 99.98% | 0 |
| background-worker | 99.99% | 0 |
| admin-dashboard | 100.00% | 0 |
| data-pipeline | 99.99% | 0 |
| real-time-collab-service | 99.95% | 1 (WebSocket connection reset during scaling) |
| ml-inference-engine | 99.97% | 0 |

## SLA Compliance

All customer SLAs were met during Q4 2025. No SLA credits were issued.

---

*Report approved by: Derek Owens, CTO — January 3, 2026*
