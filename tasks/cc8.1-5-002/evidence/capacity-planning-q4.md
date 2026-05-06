# Infrastructure Capacity Planning Report -- Q4 2025

**Generated:** January 3, 2026
**Period:** October 1 - December 31, 2025

---

## Compute Capacity

| Resource | Current Usage | Peak Usage | Capacity | Headroom |
|----------|--------------|-----------|----------|----------|
| Kubernetes Nodes | 28 | 34 (Dec peak) | 50 | 32% |
| CPU (avg) | 42% | 67% | 100% | 33% |
| Memory (avg) | 58% | 73% | 100% | 27% |

## Storage

| System | Current | Growth Rate | Capacity | Months Remaining |
|--------|---------|-------------|----------|-----------------|
| PostgreSQL | 2.1 TB | 80 GB/month | 4 TB | 24 months |
| Elasticsearch | 890 GB | 120 GB/month | 2 TB | 9 months |
| Redis Cluster | 32 GB | 2 GB/month | 64 GB | 16 months |

## Recommendations

1. Plan Elasticsearch capacity expansion by Q2 2026
2. Monitor Redis memory growth after session migration (CHG-809)
3. Consider spot instances for non-critical batch workloads

---

*Report prepared by SRE team. Contact: sre@apexcloud.io*
