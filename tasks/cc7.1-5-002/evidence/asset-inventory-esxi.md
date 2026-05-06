# ESXi Host Asset Inventory — Production Cluster

**Last Updated:** December 15, 2025
**Source:** vCenter Server (vcenter-prod.prismdata.internal)
**Classification:** Internal

---

## Cluster: PROD-CLUSTER-01

| Host | IP Address | ESXi Version | VMs Hosted | Status | Last Patched |
|------|-----------|-------------|-----------|--------|-------------|
| esxi-prod-06 | 10.70.0.42 | 8.0 U3b | 12 | Active | 2025-10-15 |
| esxi-prod-07 | 10.70.0.43 | 8.0 U3b | 14 | Active | 2025-10-15 |
| esxi-prod-08 | 10.70.0.44 | 8.0 U3b | 11 | Active | 2025-10-15 |
| esxi-prod-09 | 10.70.0.45 | 8.0 U2c | 15 | Active | 2025-03-20 |
| esxi-prod-10 | 10.70.0.46 | 8.0 U3b | 13 | Active | 2025-10-15 |

## Notes

- esxi-prod-09 is the only host still on ESXi 8.0 U2c (all others upgraded to U3b in October 2025)
- esxi-prod-09 hosts 15 VMs including:
  - customer-data-api (3 instances)
  - analytics-pipeline (2 instances)
  - payment-processor (1 instance)
  - notification-service (2 instances)
  - search-indexer (2 instances)
  - background-worker (3 instances)
  - monitoring-agent (1 instance)
  - log-aggregator (1 instance)
- vMotion migration of all 15 VMs requires sequential migration due to bandwidth constraints
- Estimated migration time: 6-8 hours depending on VM memory utilization
- Host evacuation maintenance window approved for January 11, 2026 (pending VULN-8501 remediation)

## Cluster Configuration

| Setting | Value |
|---------|-------|
| DRS | Enabled (fully automated) |
| HA | Enabled (host monitoring) |
| vMotion Network | 10.70.101.0/24 (10Gbps) |
| Management Network | 10.70.100.0/24 (1Gbps) |
| Storage | NetApp FAS9500 (NFS) |
