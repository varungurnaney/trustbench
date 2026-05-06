# Post-Mortem Report: INC-2025-804

**Incident:** Ransomware on File Processing Cluster
**Severity:** SEV-1
**Incident Commander:** Nina Petrovich, Director of Security
**Post-Mortem Author:** Jennifer Walsh, Senior Security Engineer
**Post-Mortem Date:** November 24, 2025

---

## 1. Incident Timeline

| Timestamp (UTC) | Event |
|-----------------|-------|
| 2025-11-18 02:10 | CrowdStrike Falcon detects Conti ransomware variant on file-proc-node-07. Automatic isolation triggered. |
| 2025-11-18 02:14 | CrowdStrike detects same signature on file-proc-node-09 and file-proc-node-12. Both isolated. |
| 2025-11-18 02:18 | PagerDuty alerts SRE on-call (Raj Patel) and Security on-call (Jennifer Walsh) |
| 2025-11-18 02:22 | Jennifer Walsh acknowledges. Confirms 3 nodes isolated. Begins triage. |
| 2025-11-18 02:30 | Nina Petrovich (IC) paged. Declares SEV-1. War room opened. |
| 2025-11-18 02:45 | Blast radius assessment: only 3 processing nodes affected. Production database, customer storage, and API servers unaffected. |
| 2025-11-18 02:55 | Containment confirmed. Processing pipeline paused. All worker node credentials rotated. |
| 2025-11-18 06:00 | Entry vector identified: compromised Docker base image from public Docker Hub. Image `node:18-alpine-20251115` contained embedded loader. |
| 2025-11-18 10:00 | All internal Docker images scanned. Only the 3 processing nodes used the compromised base image (auto-updated via CI pipeline on Nov 17). |
| 2025-11-18 14:00 | Clean nodes rebuilt from verified base images. Processing pipeline restarted. |
| 2025-11-18 18:00 | Customer impact assessment: 847 documents in processing queue were delayed 12 hours. No documents lost or encrypted — ransomware was caught before encryption completed on 2 of 3 nodes. |
| 2025-11-19 10:00 | Node file-proc-node-07 forensic analysis complete. Ransomware encrypted 23 files on local temp storage — all recoverable from processing queue. |
| 2025-11-19 14:00 | Incident resolved. Processing backlog cleared. Enhanced monitoring in place. |

## 2. Root Cause Analysis (5-Whys)

1. **Why was ransomware executed on the processing nodes?** The Docker base image `node:18-alpine-20251115` contained a malicious loader in the entrypoint that downloaded Conti ransomware from a C2 server.
2. **Why was a compromised Docker Hub image used?** The CI pipeline was configured to pull `node:18-alpine` with the `latest` tag, which resolved to the compromised version published November 15.
3. **Why did the pipeline use mutable tags?** Docker image pinning policy existed but was not enforced in CI configuration. The pipeline used convenience tags (`latest`, date-based) rather than digest-pinned images.
4. **Why was the compromised image not detected before deployment?** Docker image scanning (Trivy) was configured for CVE detection only, not for malware or unexpected binary detection. The loader was not in any CVE database.
5. **Why was there no runtime detection before CrowdStrike caught it?** Container runtime security (Falco or similar) was not deployed on processing nodes. CrowdStrike caught the ransomware at the execution stage, but earlier detection (at the image pull or container start stage) would have prevented execution entirely.

## 3. Impact Assessment

- **Systems:** 3 file processing nodes (file-proc-node-07, -09, -12)
- **Customer documents:** 847 documents delayed ~12 hours. No documents lost, encrypted, or exfiltrated.
- **Customer impact:** 127 enterprise customers experienced delayed document processing. No data breach.
- **Financial impact:** ~$15K in engineer time. No customer credits required (processing SLA allows 24-hour window).
- **Ransomware encryption:** 23 temp files encrypted on node-07. All recoverable from queue. Nodes -09 and -12 were isolated before encryption started.

## 4. Remediation Actions Taken

1. Compromised Docker image removed from internal registry cache
2. All CI pipelines updated to use digest-pinned base images
3. 3 processing nodes wiped and rebuilt from verified images
4. Worker node credentials rotated
5. Processing queue replayed for the 847 delayed documents

## 5. Preventive Action Items

| ID | Action Item | Owner | Priority | Target Date | Status |
|----|-------------|-------|----------|-------------|--------|
| PM-804-AI-01 | Enforce Docker image digest pinning across all CI pipelines (not just processing) | DevOps Team (lead: Raj Patel) | Critical | 2025-12-05 | Complete (HLX-PM-2341) |
| PM-804-AI-02 | Deploy container runtime security (Falco) on all processing and worker nodes | Jennifer Walsh | High | 2025-12-20 | Complete (HLX-PM-2342) |
| PM-804-AI-03 | Add malware scanning to Docker image pipeline (beyond CVE-only Trivy) | Jennifer Walsh | High | 2025-12-15 | Complete (HLX-PM-2343) |
| PM-804-AI-04 | Implement Docker Hub image allowlist — only approved base images permitted | DevOps Team | High | 2026-01-15 | In Progress (HLX-PM-2344) |
| PM-804-AI-05 | Deploy private Docker registry to proxy and scan all external images | DevOps Team | Medium | 2026-02-01 | In Progress (HLX-PM-2345) |
| PM-804-AI-06 | Implement container image provenance verification (Sigstore/Cosign) | Security Ops | Medium | 2026-02-15 | Not Started |
| PM-804-AI-07 | Conduct supply chain security training for engineering team | Security Ops | Medium | 2026-01-31 | Not Started |
| PM-804-AI-08 | Add network egress restrictions on processing nodes — block all outbound except approved registries and APIs | Network Team | High | 2026-01-15 | Not Started |
| PM-804-AI-09 | Review and harden all CI/CD pipeline configurations for supply chain risks | Security Ops + DevOps | High | 2026-01-31 | Not Started |

## 6. Detection Improvement Recommendations

- CrowdStrike detected ransomware execution within 4 minutes — EDR was effective post-execution.
- Gap: No detection at the supply chain level. Image was pulled November 17, ransomware executed November 18. A 24-hour window where the compromised image was in the pipeline undetected.
- Recommendation: Implement image scanning at pull time (before CI pipeline uses the image) and at runtime (Falco rules for unexpected process execution in containers).

---

**Reviewed by:** Lars Eriksson, CISO
**Review Date:** November 25, 2025
**Sign-off:** Approved
