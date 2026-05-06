# Polaris Financial — System Uptime Report Q4 2025

**Period:** October 1 — December 31, 2025
**Generated:** January 2, 2026

## Summary

| Metric | Value |
|--------|-------|
| Overall Uptime | 99.97% |
| Total Downtime | 13 minutes |
| Planned Maintenance Windows | 4 |
| Unplanned Incidents | 1 |

## Unplanned Incident

- **Date:** November 8, 2025
- **Duration:** 13 minutes
- **Impact:** Customer API latency spike (p99 > 2s)
- **Root Cause:** EKS node autoscaler lag during traffic surge
- **Resolution:** Manual node scaling + autoscaler configuration update

## Planned Maintenance

| Date | Window | Duration | Description |
|------|--------|----------|-------------|
| Oct 12 | 02:00-04:00 UTC | 45 min | RDS engine upgrade |
| Nov 2 | 02:00-04:00 UTC | 30 min | EKS cluster version upgrade |
| Nov 30 | 02:00-04:00 UTC | 60 min | Network firewall rule deployment |
| Dec 21 | 02:00-04:00 UTC | 20 min | SSL certificate rotation |
