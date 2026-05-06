# Annual Risk Assessment Report -- 2025

**Document ID:** RPT-RSK-2025-001
**Date:** March 15, 2025
**Prepared by:** Derek Palmer, Chief Risk Officer
**Approved by:** Risk Committee (March 20, 2025)

---

## 1. Executive Summary

This report documents the findings of Skyline Health Inc.'s 2025 annual comprehensive risk assessment covering all risk domains per the Risk Management Policy (POL-RSK-016). The assessment identified 12 risks across 5 categories.

## 2. Assessment Methodology

- Interviews with business unit leaders (8 interviews conducted)
- Threat landscape analysis incorporating HITRUST CSF and NIST CSF
- Control effectiveness evaluation
- Industry peer benchmarking (Health-ISAC)
- Regulatory change monitoring

## 3. Risk Categories Assessed

1. Information Security
2. HIPAA / Regulatory Compliance
3. Technology and Infrastructure
4. Third-Party / Vendor Risk
5. Operational Resilience

## 4. Key Findings

### 4.1 Information Security
- Unauthorized database access risk: Controls effective. Recommend CyberArk upgrade to v13.
- Insider threat (clinician access): Break-the-glass controls effective. UBA alerting needs tuning.
- Cloud misconfiguration: Wiz CSPM deployment improved posture. 94% auto-remediation rate.
- Ransomware: Tabletop exercises showing improvement. Immutable backups tested successfully.

### 4.2 HIPAA / Regulatory Compliance
- PHI breach via API: API security gateway controls effective. Quarterly pentests ongoing.
- Breach notification timeline: Drill results within compliance window.
- State privacy laws: OneTrust platform updated. Monitoring ongoing.

### 4.3 Technology and Infrastructure
- Platform outage: DR capabilities strong. RTO within target.
- Clinical data integrity: Checksums and audits effective.
- Legacy HL7v2: Migration to FHIR R4 planned. Virtual patching interim measure.

### 4.4 Third-Party / Vendor Risk
- BA breach risk: BAA enforcement and monitoring in place. Assessment completion rate 80%.

### 4.5 Operational Resilience
- Key person dependency: Cross-training program effective.

## 5. Risks NOT Assessed (Out of Scope)

The following risk domains were not included in this assessment as they are addressed by separate programs:
- Financial risk (covered by CFO financial risk program)
- Market risk (not applicable -- SaaS platform)

## 6. Recommendations

1. Complete FHIR R4 migration to retire HL7v2 interfaces
2. Upgrade CyberArk to v13 for improved session recording
3. Expand BA assessment program to cover all 10 critical associates
4. Conduct ad hoc assessment if HIPAA 2.0 rulemaking is finalized

## 7. Next Assessment

Scheduled for Q1 2026 (March 2026).

---

*Classification: Confidential -- Internal Use Only*
