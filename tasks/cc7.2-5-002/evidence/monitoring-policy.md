# Cobalt Labs — Security Monitoring and Detection Policy

**Document ID:** CBT-SEC-POL-005
**Version:** 3.1
**Effective Date:** January 15, 2025
**Owner:** Helen Park, CISO
**Classification:** Internal — Confidential

---

## 1. Purpose

This policy defines requirements for security monitoring, threat detection, and alert management across all Cobalt Labs infrastructure supporting the developer tools platform.

## 2. Scope

All production systems in GCP (us-central1, europe-west1) supporting Cobalt Labs' CI/CD platform, artifact registry, and developer collaboration tools.

## 3. SIEM and Detection Platform

### 3.1 Platform

Cobalt Labs uses Google Chronicle Security Operations as its SIEM and detection platform.

### 3.2 Detection Rules

Cobalt Labs maintains a minimum of 200 active detection rules organized into the following categories:
- Authentication anomalies (brute force, credential stuffing, impossible travel, MFA bypass)
- Authorization violations (privilege escalation, unauthorized resource access)
- Data exfiltration indicators (bulk downloads, unusual API usage, DNS tunneling)
- Supply chain threats (artifact tampering, dependency confusion, build pipeline manipulation)
- Infrastructure anomalies (resource creation, configuration drift, cryptocurrency mining)
- Insider threat indicators (off-hours access, bulk data access, privilege abuse)

### 3.3 Rule Lifecycle

- New rules: Deployed in "detect-only" mode for 14 days, then promoted to alerting
- Rule modifications: Require peer review and Security Operations Lead approval
- Rule disablement: Requires CISO approval, documented compensating control, 60-day maximum
- Rule retirement: Requires threat model review confirming the attack vector is no longer relevant

## 4. Alert Management

### 4.1 Response SLAs

| Severity | SLA | Coverage |
|----------|-----|----------|
| Critical | 10 minutes | 24/7 |
| High | 30 minutes | 24/7 |
| Medium | 4 hours | Business hours |
| Low | Next business day | Business hours |

### 4.2 Alert Tuning

- Monthly review of false positive rates per rule category
- Rules exceeding 30% false positive rate must be tuned within 10 business days
- Tuning changes documented in the Detection Engineering Log
- No rule may be disabled solely to reduce alert volume

## 5. Detection Coverage Requirements

### 5.1 MITRE ATT&CK Coverage

Detection rules must provide coverage for the following MITRE ATT&CK tactics at minimum:
- Initial Access (T1190, T1078)
- Execution (T1059, T1204)
- Persistence (T1098, T1136)
- Privilege Escalation (T1068, T1548)
- Defense Evasion (T1562, T1070)
- Credential Access (T1110, T1528)
- Lateral Movement (T1021, T1534)
- Exfiltration (T1041, T1567)

### 5.2 Supply Chain Detection

Given Cobalt Labs' role as a CI/CD platform provider, supply chain attack detection is a critical priority:
- Build pipeline integrity monitoring
- Artifact registry access anomaly detection
- Dependency resolution monitoring
- Code signing verification

## 6. Monitoring Coverage

All production services must be integrated with Chronicle within 3 business days of deployment.

---

**Approved by:** Marcus Reid, CTO
