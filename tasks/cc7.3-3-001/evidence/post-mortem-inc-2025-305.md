# Post-Mortem Report: INC-2025-305

**Incident:** Ransomware Detected on Build Server
**Severity:** SEV-1
**Incident Commander:** Elena Vasquez, Director of Security
**Post-Mortem Author:** Marcus Chen, Security Operations Manager
**Post-Mortem Date:** December 5, 2025

---

## 1. Incident Timeline

| Timestamp (UTC) | Event |
|-----------------|-------|
| 2025-11-28 03:41 | CrowdStrike Falcon detects ransomware execution on build server `build-prod-03`. Automatic network isolation triggered. |
| 2025-11-28 03:44 | PagerDuty alert to SRE on-call (Jamal Wright) and Security on-call (David Park) |
| 2025-11-28 03:58 | David Park acknowledges. Confirms CrowdStrike auto-isolated the host. Begins triage. |
| 2025-11-28 04:05 | Elena Vasquez (IC) paged. Declares SEV-1. War room opened. |
| 2025-11-28 04:15 | Containment confirmed: host isolated, all build pipelines paused, credential rotation initiated for CI/CD service accounts |
| 2025-11-28 06:00 | Forensic analysis: ransomware variant identified as LockBit 3.0. Entry vector: compromised npm package in build dependency |
| 2025-11-28 08:30 | Blast radius assessment complete: only build-prod-03 affected. No lateral movement detected. Production systems unaffected. |
| 2025-11-28 12:00 | Build server wiped and rebuilt from infrastructure-as-code. CI/CD pipeline dependencies audited. |
| 2025-11-28 18:00 | Compromised npm package identified: `event-stream-utils@2.1.4` — malicious postinstall script added in version 2.1.4 (published Nov 26) |
| 2025-11-29 10:00 | All build dependencies pinned to verified versions. Package lock integrity checks added to CI pipeline. |
| 2025-11-29 22:00 | Incident resolved. Build pipelines restored. Enhanced monitoring confirmed operational. |

## 2. Root Cause Analysis (5-Whys)

1. **Why was ransomware executed on the build server?** A malicious npm package (`event-stream-utils@2.1.4`) ran a postinstall script that downloaded and executed the LockBit payload.
2. **Why was the malicious package installed?** The build pipeline used `npm install` without a lockfile integrity check, and the package's version range (`^2.0.0`) automatically pulled the compromised version 2.1.4.
3. **Why didn't the build server prevent execution of unknown binaries?** Application whitelisting was not enabled on build servers — only production servers have execution controls.
4. **Why was application whitelisting not on build servers?** Build servers were considered internal-only and lower risk. Security hardening standards applied to production but not build infrastructure.
5. **Why did the compromised package go undetected?** No software composition analysis (SCA) tool was scanning build dependencies for known-malicious packages in real-time.

## 3. Impact Assessment

- **Systems affected:** Single build server (build-prod-03). No production systems compromised.
- **Data exposure:** None confirmed. Build server contained source code and CI/CD credentials (rotated within 30 minutes).
- **Service impact:** Build pipelines paused for approximately 19 hours. No customer-facing impact.
- **Customer impact:** None — production services remained available throughout.
- **Financial impact:** Approximately $8K in engineer time for investigation and rebuild.

## 4. Remediation Actions Taken

1. Build server isolated automatically by CrowdStrike (within 3 minutes of detection)
2. All CI/CD service account credentials rotated
3. Build server wiped and rebuilt from Terraform
4. Compromised npm package removed from all projects
5. Package versions pinned with lockfile integrity verification

## 5. Preventive Action Items

| ID | Action Item | Owner | Priority | Target Date | Status |
|----|-------------|-------|----------|-------------|--------|
| PM-305-AI-01 | Deploy Snyk or Socket.dev for real-time SCA scanning of build dependencies | David Park | Critical | 2025-12-20 | In Progress (SEC-PM-1892) |
| PM-305-AI-02 | Enable application whitelisting on all build servers (not just production) | Jamal Wright (SRE) | High | 2025-12-31 | Not Started |
| PM-305-AI-03 | Implement npm package provenance verification in CI pipeline | Build Engineering | High | 2026-01-15 | Not Started |
| PM-305-AI-04 | Extend security hardening baseline to cover build and staging infrastructure | Marcus Chen | Medium | 2026-01-31 | Not Started |
| PM-305-AI-05 | Conduct supply chain security training for all engineering staff | Security Ops | Medium | 2026-02-15 | Not Started |
| PM-305-AI-06 | Evaluate private npm registry to proxy and scan all external packages | DevOps Team | Medium | 2026-02-28 | Not Started |
| PM-305-AI-07 | Implement build server network segmentation — restrict outbound to approved registries only | Network Engineering | High | 2026-01-15 | Not Started |
| PM-305-AI-08 | Add ransomware-specific detection rules for build infrastructure to Splunk | David Park | High | 2025-12-15 | Complete (SEC-PM-1893) |

## 6. Detection Improvement Recommendations

- CrowdStrike detected and isolated the ransomware within 3 minutes — EDR detection was excellent.
- Gap: No detection at the supply chain level. The malicious package was installed 2 days before execution. SCA scanning would have caught the known-malicious package signature.
- Recommendation: Implement build-time dependency scanning that blocks builds if any dependency has known vulnerabilities or malicious indicators.

---

**Reviewed by:** Elena Vasquez, Director of Security
**Review Date:** December 8, 2025
