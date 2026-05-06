# Crestline AI — Infrastructure Cost Optimization Review Q3 2025

**Prepared by:** Platform Engineering Team
**Date:** October 5, 2025
**Reviewed by:** James Park, CTO

---

## 1. GPU Instance Consolidation

### Background

Crestline AI's ML training workloads require p4d.24xlarge GPU instances at $32.77/hour. Peak training demand exceeds dedicated production capacity during model retraining cycles (monthly, 3-5 day duration).

### Decision: Shared VPC for GPU Overflow

Rather than maintaining idle GPU capacity in the production VPC (estimated $47,000/month in idle costs), the Platform Engineering team created a shared compute VPC (crestline-shared-compute) that:

1. Hosts staging workloads on standard compute instances
2. Hosts production ML training overflow on GPU instances when production capacity is exhausted
3. Consolidates GPU reservations into a single VPC for better Reserved Instance utilization

### Cost Savings

| Item | Monthly Cost Before | Monthly Cost After | Savings |
|------|-------------------|-------------------|---------|
| Production GPU (dedicated) | $94,000 | $62,000 | $32,000 |
| Staging compute | $8,200 | $8,200 | $0 |
| Shared VPC overhead | $0 | $1,400 | -$1,400 |
| **Total** | **$102,200** | **$71,600** | **$30,600** |

Annual savings: approximately $367,200.

### Security Controls Implemented

- Separate subnets for staging and production ML overflow workloads
- Security groups restrict cross-subnet communication (staging cannot reach ML overflow subnets)
- Production ML overflow instances use the same IAM roles as production ML instances
- VPC Flow Logs enabled on all subnets
- Kubernetes namespace isolation between staging and production ML pods

### Risk Assessment

The security team reviewed this architecture and noted:
- Staging and production workloads share the same VPC network boundary
- A vulnerability in a staging workload could theoretically be used to pivot to production ML overflow subnets via the shared VPC network
- Security group rules mitigate this risk by restricting inter-subnet traffic
- Exception SEC-EXC-2025-012 was filed and approved by CISO

## 2. Other Optimizations

- Savings Planes applied to production EKS nodes: $12,400/month savings
- S3 Intelligent-Tiering on archival data: $3,200/month savings
- RDS reserved instances: $5,800/month savings
