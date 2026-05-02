# Business Continuity Plan — Executive Summary

**Document ID:** POL-BCP-001
**Version:** 1.2
**Effective Date:** January 2025

## Overview

Vantage Corp maintains a business continuity plan to ensure critical business functions can continue during and after a disaster. The plan covers:

- **RTO (Recovery Time Objective):** 4 hours for critical systems
- **RPO (Recovery Point Objective):** 1 hour for production databases
- **Backup Frequency:** Hourly incremental, daily full
- **Backup Storage:** Cross-region replication (us-central1 → us-east1)
- **DR Site:** GCP us-east1 region (cold standby)

## Testing

- DR failover tested semi-annually.
- Last test: September 2025 — successful failover in 3.5 hours.
- Next test: March 2026.

## Key Contacts

- DR Coordinator: Raj Patel (SRE Lead)
- Executive Sponsor: VP Engineering

---

**Approved by:** Tom Reeves, CISO
