# Post-Mortem Report: INC-2025-404

**Incident:** Ransomware on Production File Processing Worker
**Severity:** SEV-1
**Incident Commander:** Yuki Tanaka, Director of Security
**Post-Mortem Author:** David Okafor, Senior Security Engineer
**Post-Mortem Date:** November 18, 2025

---

## 1. Incident Timeline

| Timestamp (UTC) | Event |
|-----------------|-------|
| 2025-11-12 02:33 | CrowdStrike Falcon detects LockBit 3.0 execution on worker node `file-proc-w07`. Automatic network isolation triggered. |
| 2025-11-12 02:36 | PagerDuty pages SRE on-call (Mei Lin) and Security on-call (David Okafor) |
| 2025-11-12 02:41 | David Okafor acknowledges. Confirms auto-isolation. Declares SEV-1. |
| 2025-11-12 02:45 | Yuki Tanaka (IC) joins war room. Blast radius assessment begins. |
| 2025-11-12 03:00 | 3 additional worker nodes scanned — no lateral movement detected |
| 2025-11-12 03:20 | Containment confirmed. Affected worker node isolated. CI/CD credentials rotated. |
| 2025-11-12 06:00 | Entry vector identified: compromised container image from internal registry. Image `vcs-fileproc:2.4.1` contained embedded reverse shell in entrypoint script. |
| 2025-11-12 10:00 | All container images in internal registry scanned. Only `vcs-fileproc:2.4.1` compromised. |
| 2025-11-12 14:00 | Registry access logs reviewed. Image was pushed by service account `ci-builder-prod` at 2025-11-11T22:15:00Z. |
| 2025-11-13 10:00 | Root cause confirmed: CI pipeline compromise via stolen GitHub PAT token. |
| 2025-11-13 20:00 | Incident resolved. Clean image `vcs-fileproc:2.4.2` deployed. Enhanced monitoring active. |

## 2. Root Cause Analysis (5-Whys)

1. **Why was ransomware executed?** The container image `vcs-fileproc:2.4.1` contained a reverse shell in its entrypoint that downloaded and executed LockBit.
2. **Why was the image compromised?** An attacker used a stolen GitHub Personal Access Token to modify the CI pipeline and inject malicious code into the build process.
3. **Why was the PAT stolen?** Developer Ben Nakamura's GitHub PAT was exposed in a public gist he created for a code snippet. The PAT had `repo` and `workflow` scopes.
4. **Why did the PAT have broad scopes?** No policy existed restricting PAT scope or requiring fine-grained tokens. Developers self-provisioned PATs without security review.
5. **Why was the compromised image not detected before deployment?** Container image scanning (Trivy) was configured but only scanned for known CVEs, not embedded malware or suspicious entrypoint modifications.

## 3. Impact Assessment

- **Systems affected:** 1 worker node (file-proc-w07). No lateral movement.
- **Data exposure:** None. Worker node processes file conversions but does not store customer data persistently. In-flight files were encrypted by ransomware but restored from upload queue.
- **Service impact:** File processing delayed approximately 2 hours while worker was replaced. Customer-facing upload/download unaffected.
- **Financial impact:** ~$12K in engineering time.

## 4. Remediation Actions Taken

1. Compromised container image removed from registry
2. Ben Nakamura's GitHub PAT revoked. Public gist deleted.
3. All developer GitHub PATs audited and excessive-scope tokens revoked
4. Clean image built and deployed
5. CI/CD service account credentials rotated

## 5. Preventive Action Items

| ID | Action Item | Owner | Priority | Target Date | Status |
|----|-------------|-------|----------|-------------|--------|
| PM-404-AI-01 | Implement container image signing and verification (Cosign/Sigstore) | DevOps Team | Critical | 2025-12-15 | In Progress |
| PM-404-AI-02 | Add malware scanning to container image pipeline (beyond CVE-only Trivy) | David Okafor | High | 2025-12-20 | In Progress |
| PM-404-AI-03 | Enforce fine-grained GitHub PATs — deprecate classic PATs org-wide | Carlos Rivera | High | 2026-01-15 | Not Started |
| PM-404-AI-04 | Implement GitHub secret scanning for PATs in public repositories and gists | David Okafor | High | 2025-12-10 | Complete |
| PM-404-AI-05 | Deploy CI pipeline integrity monitoring — alert on unexpected workflow modifications | DevOps Team | Medium | 2026-01-31 | Not Started |
| PM-404-AI-06 | Conduct developer security training on credential hygiene and PAT management | Security Ops | Medium | 2026-02-15 | Not Started |
| PM-404-AI-07 | Add second security on-call engineer for overnight/weekend coverage | Margaret Holloway (CISO) | High | 2026-01-01 | Not Started |
| PM-404-AI-08 | Implement runtime container behavior monitoring (Falco) on all worker nodes | SRE Team | Medium | 2026-02-28 | Not Started |
| PM-404-AI-09 | Establish container registry access alerting — notify security on any image push outside CI pipeline | David Okafor | High | 2025-12-31 | In Progress |

## 6. Detection Improvement Recommendations

- CrowdStrike detected ransomware execution within 3 minutes — EDR was effective post-execution.
- Gap: No detection at the supply chain level. The compromised image was pushed ~4 hours before execution. Image integrity verification would have blocked deployment.
- Gap: GitHub PAT exposure was not detected. Secret scanning for public gists should be enabled.

---

**Reviewed by:** Yuki Tanaka, Director of Security
**Review Date:** November 20, 2025
