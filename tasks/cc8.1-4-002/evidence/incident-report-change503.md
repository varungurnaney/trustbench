# Incident Report: CHANGE-503 Rollback

**Incident ID:** INC-2025-0891
**Date:** October 21, 2025
**Severity:** P2
**Status:** Resolved

---

## Summary

CHANGE-503 (GraphQL subscriptions for real-time dashboard) was deployed to production at 14:00 ET on October 21. Within 15 minutes, the error rate on `/api/subscriptions` spiked to 4.7%, exceeding the 2% rollback threshold defined in the change management policy Section 3.6.

## Timeline

- **14:00 ET** -- CHANGE-503 deployed to production by SRE team
- **14:12 ET** -- Datadog alert: error rate on /api/subscriptions at 3.1%
- **14:18 ET** -- Error rate reached 4.7%. On-call SRE (Derek Santos) initiated rollback
- **14:26 ET** -- Rollback completed. Error rate returned to baseline (0.2%)
- **14:30 ET** -- Post-rollback health checks passed. Incident resolved
- **14:45 ET** -- Change owner (Omar Hassan) confirmed service restored

## Root Cause

WebSocket connection pooling under production load exceeded staging environment capacity. The staging environment has 2 Kubernetes nodes vs. production's 12 nodes, causing connection pool exhaustion to manifest only at production scale. The issue was not detectable in staging with the current environment configuration.

## Corrective Actions

1. CHANGE-504 created to fix connection pooling with backpressure handling
2. Engineering to evaluate staging environment parity for WebSocket workloads
3. Load test updated to simulate 2x production traffic for WebSocket-heavy changes

## Impact

- Duration: 30 minutes
- Affected users: ~450 concurrent dashboard users experienced real-time data delays
- Data loss: None
- Revenue impact: None
