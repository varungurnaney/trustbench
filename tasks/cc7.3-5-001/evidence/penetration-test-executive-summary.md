# Annual Penetration Test — Executive Summary

**Engagement:** Clearpoint Financial Software Annual Security Assessment
**Firm:** Redline Security Partners
**Test Period:** August 12-30, 2025
**Report Date:** September 15, 2025
**Classification:** Confidential

---

## 1. Scope

- External network perimeter
- Customer-facing web applications (portfolio dashboard, reporting API, trading analytics)
- Internal network (from assumed breach position)
- API security assessment
- Social engineering (phishing simulation)

## 2. Summary of Findings

| Severity | Count | Remediated | Open |
|----------|-------|-----------|------|
| Critical | 1 | 1 | 0 |
| High | 4 | 3 | 1 |
| Medium | 7 | 5 | 2 |
| Low | 12 | 8 | 4 |
| Informational | 9 | N/A | N/A |

## 3. Critical Finding (Remediated)

**PT-2025-001:** SQL injection vulnerability in reporting API endpoint `/api/v2/reports/custom`. Parameterized queries not used for custom date range filters. Exploitable to extract arbitrary database records.

**Remediation:** Parameterized queries implemented. Input validation added. Deployed August 18, 2025. Verified by retest August 19.

**Note:** This same endpoint was exploited in INC-2025-704 (November 2025) via a different injection vector (nested JSON payload in report filter, not the date range parameter that was patched). The August remediation was incomplete — it addressed the specific vector found but did not comprehensively secure all input parameters.

## 4. Open High Finding

**PT-2025-005:** Excessive S3 bucket permissions — customer-reports bucket allows GetObject for any authenticated IAM role in the AWS account, not scoped to specific service roles.

**Status:** Remediation in progress. Target date: November 30, 2025. (Note: This was the underlying vulnerability exploited in INC-2025-705 in December 2025.)

## 5. Overall Assessment

Clearpoint's security posture is **adequate with improvements needed**. Critical and high findings require prompt remediation. The SQL injection finding, while remediated for the specific vector, suggests a broader pattern of insufficient input validation in the reporting API.

---

**Prepared by:** Ethan Clarke, Principal Security Consultant, Redline Security Partners
