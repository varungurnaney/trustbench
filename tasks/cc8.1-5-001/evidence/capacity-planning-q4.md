# Beacon SaaS — Infrastructure Capacity Planning Report Q4 2025

**Report ID:** RPT-CAP-2025-Q4
**Prepared By:** Infrastructure Engineering Team
**Date:** January 3, 2026
**Classification:** Internal

---

## 1. Executive Summary

Infrastructure capacity utilization remained within acceptable thresholds throughout Q4 2025. Peak utilization occurred during Black Friday (November 28, 2025) at 72% of provisioned compute capacity. No capacity-related incidents were recorded during the quarter.

## 2. Compute Resources

### 2.1 Kubernetes Cluster (EKS — us-east-1)

| Metric | October | November | December | Target |
|--------|---------|----------|----------|--------|
| Average CPU utilization | 38% | 42% | 35% | < 70% |
| Peak CPU utilization | 55% | 72% | 48% | < 85% |
| Average memory utilization | 45% | 51% | 43% | < 75% |
| Peak memory utilization | 62% | 78% | 56% | < 90% |
| Node count (average) | 24 | 28 | 22 | Auto-scaled |
| Pod count (average) | 186 | 215 | 178 | N/A |

### 2.2 Autoscaling Events

- **October**: 3 scale-up events, 2 scale-down events
- **November**: 8 scale-up events (4 during Black Friday week), 5 scale-down events
- **December**: 2 scale-up events, 4 scale-down events (holiday traffic reduction)

All autoscaling events completed within SLA (< 5 minutes for scale-up).

## 3. Database Resources

### 3.1 MongoDB Atlas (aurora-prod-east-1 equivalent)

| Metric | October | November | December | Target |
|--------|---------|----------|----------|--------|
| Average connections | 420 | 485 | 390 | < 1000 |
| Peak connections | 580 | 710 | 520 | < 1500 |
| Storage utilization | 62% | 65% | 68% | < 80% |
| Average query latency (p50) | 12ms | 15ms | 11ms | < 50ms |
| IOPS utilization | 35% | 48% | 32% | < 70% |

Storage growth rate: ~1% per month. Projected to reach 80% threshold in Q3 2026.

### 3.2 Redis Cache

| Metric | October | November | December | Target |
|--------|---------|----------|----------|--------|
| Memory utilization | 55% | 62% | 53% | < 80% |
| Cache hit rate | 94.2% | 93.8% | 94.5% | > 90% |
| Eviction rate | 0.01% | 0.02% | 0.01% | < 0.1% |

## 4. Network and CDN

### 4.1 CloudFront CDN

| Metric | October | November | December |
|--------|---------|----------|----------|
| Total requests (millions) | 245 | 312 | 228 |
| Cache hit ratio | 92.3% | 91.8% | 93.1% |
| Bandwidth (TB) | 18.4 | 24.1 | 16.9 |
| Error rate (4xx/5xx) | 0.3% | 0.4% | 0.2% |

### 4.2 Load Balancer (ALB)

- Average request rate: 2,400 req/sec
- Peak request rate: 5,800 req/sec (Black Friday)
- No capacity-related errors during the quarter

## 5. Cost Analysis

| Category | Q3 2025 | Q4 2025 | Change |
|----------|---------|---------|--------|
| Compute (EKS) | $42,300 | $45,100 | +6.6% |
| Database (MongoDB Atlas) | $18,500 | $19,200 | +3.8% |
| Database (Redis) | $4,200 | $4,200 | 0% |
| CDN (CloudFront) | $3,800 | $4,500 | +18.4% |
| Storage (S3) | $2,100 | $2,300 | +9.5% |
| **Total** | **$70,900** | **$75,300** | **+6.2%** |

Cost increase is attributable to Black Friday traffic and natural data growth. Within budget projections.

## 6. Recommendations for Q1 2026

1. **Database storage**: Plan for MongoDB Atlas storage tier upgrade by Q2 2026 to accommodate growth trajectory
2. **Reserved instances**: Evaluate Savings Plans for baseline EKS node capacity (estimated 15-20% cost savings)
3. **CDN optimization**: Implement additional cache rules for API responses to improve hit ratio
4. **Redis upgrade**: Evaluate migration to Redis 7.x for improved memory efficiency

## 7. Approval

| Role | Name | Date |
|------|------|------|
| Director of SRE | Tomás Reyes | 2026-01-03 |
| VP of Engineering | Natasha Volkov | 2026-01-05 |
