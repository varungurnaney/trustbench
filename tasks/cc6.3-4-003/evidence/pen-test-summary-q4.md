# Vertex Financial — Q4 2025 Penetration Test Executive Summary

**Report ID:** RPT-PT-2025-Q4
**Assessment Period:** November 10 - November 28, 2025
**Testing Firm:** CyberEdge Security Partners
**Classification:** Confidential

---

## 1. Scope

External and internal penetration testing of Vertex Financial's production infrastructure including:

- Public-facing web applications (api.vertexfinancial.com, portal.vertexfinancial.com)
- Internal network infrastructure
- Cloud infrastructure (AWS us-east-1)
- Snowflake data warehouse (external access points only)

## 2. Summary of Findings

| Severity | Count | Remediated | Open |
|----------|-------|------------|------|
| Critical | 0 | N/A | 0 |
| High | 1 | 1 | 0 |
| Medium | 3 | 2 | 1 |
| Low | 5 | 3 | 2 |
| Informational | 8 | N/A | N/A |

## 3. Key Findings

### 3.1 High — Resolved
**H-001:** Insecure direct object reference (IDOR) in transaction history API endpoint. Remediated November 20, 2025.

### 3.2 Medium — Open
**M-003:** TLS 1.0 still enabled on legacy payment gateway integration endpoint (legacy-gateway.vertexfinancial.com). Migration to TLS 1.3 scheduled for Q1 2026.

## 4. Overall Assessment

Vertex Financial's external attack surface is well-managed. The single high-severity finding was identified and remediated within the testing window. No critical vulnerabilities were identified.

---

**Report prepared by:** CyberEdge Security Partners
**Lead Assessor:** Michael Torres, OSCP
