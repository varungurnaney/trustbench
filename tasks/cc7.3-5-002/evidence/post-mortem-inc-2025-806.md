# Post-Mortem: INC-2025-806

**Incident:** DDoS Attack on Collaboration API
**Severity:** SEV-2
**IC:** Nina Petrovich
**Author:** Nina Petrovich
**Date:** December 17, 2025

---

## 1. Incident Timeline

| Timestamp (UTC) | Event |
|-----------------|-------|
| 2025-12-10 18:00 | Cloudflare alerts on anomalous traffic spike — 4.5M requests/second targeting real-time sync endpoints |
| 2025-12-10 18:08 | Cloudflare DDoS protection auto-engaged. Traffic scrubbing active. |
| 2025-12-10 18:15 | SRE on-call (Raj Patel) acknowledges PagerDuty. Nina Petrovich (IC) notified. SEV-2 declared. |
| 2025-12-10 18:20 | Initial assessment: ~15% of legitimate real-time sync requests experiencing elevated latency (200-500ms vs normal 50ms). Collaboration sessions not disrupted. |
| 2025-12-10 18:30 | Containment confirmed: Cloudflare rate limiting rules tightened. Botnet source IPs identified — 12,000 unique IPs across 3 ASNs. Challenge page activated for suspicious traffic. |
| 2025-12-10 19:00 | Attack volume reduced to 800K req/s. Customer impact minimal — latency returned to normal. |
| 2025-12-10 21:00 | Attack subsided to baseline levels. Monitoring maintained. |
| 2025-12-11 08:00 | Incident resolved. 24-hour monitoring window initiated. No further attack waves. |

## 2. Root Cause Analysis (5-Whys)

1. **Why did the DDoS attack affect service?** The real-time sync endpoints were not individually rate-limited — Cloudflare rate limiting was applied at the domain level, allowing the sync endpoints to absorb disproportionate traffic before domain-level thresholds triggered.
2. **Why were sync endpoints not individually rate-limited?** Rate limiting configuration had not been updated since the sync feature was launched in Q2 2025. The original Cloudflare configuration predated the sync feature.
3. **Why was the configuration not updated when sync launched?** No security review was included in the sync feature launch checklist. The feature went through functional QA but not security architecture review.
4. **Why was security review not in the launch checklist?** The feature launch process does not include a mandatory security review gate for infrastructure-level concerns (Cloudflare configuration, rate limiting, etc.).
5. **Why is there no security review gate?** The change management process covers code-level changes but not infrastructure configuration changes associated with new features.

## 3. Impact Assessment

- **Service impact:** ~15% of real-time sync requests experienced elevated latency (200-500ms) for approximately 30 minutes.
- **Customer impact:** Collaboration sessions remained functional. No data loss. Users may have noticed slight delay in document sync.
- **Duration:** Active attack phase: ~3 hours. Customer impact window: ~30 minutes (until rate limiting engaged).
- **Data exposure:** None. DDoS only — no data access or unauthorized activity.
- **Financial:** Minimal. Cloudflare costs for traffic scrubbing within existing contract.

## 4. Remediation Actions Taken

1. Cloudflare rate limiting tightened on sync endpoints
2. Botnet source ASNs added to challenge list
3. Real-time sync endpoints added to DDoS protection priority list

## 5. Preventive Action Items

| ID | Action Item | Owner | Priority | Target Date | Status |
|----|-------------|-------|----------|-------------|--------|
| PM-806-AI-01 | Add per-endpoint rate limiting for all customer-facing API endpoints in Cloudflare | SRE Team (Raj Patel) | High | 2025-12-31 | Complete (HLX-PM-2380) |
| PM-806-AI-02 | Add mandatory security infrastructure review to new feature launch checklist | Security Ops (Marco DeLuca) | Medium | 2026-01-31 | Complete (HLX-PM-2381) |

## 6. Detection Improvement

- Cloudflare detected the DDoS within 8 minutes — adequate for this attack type.
- Recommendation: None — existing detection and auto-mitigation were effective.

---

**Reviewed by:** Marco DeLuca, Security Operations Manager
**Review Date:** December 17, 2025
**Sign-off:** Approved
