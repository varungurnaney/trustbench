# Annual Penetration Test — Executive Summary

**Vendor:** SecurePoint Labs
**Test Period:** September 15-30, 2025
**Scope:** External network, web application, API endpoints
**Report Date:** October 10, 2025

## Results Summary

| Severity | Findings | Remediated |
|----------|----------|------------|
| Critical | 0 | N/A |
| High | 1 | Yes (Oct 20) |
| Medium | 3 | 2 remediated, 1 accepted risk |
| Low | 5 | 3 remediated, 2 accepted risk |

## High Finding

**H-1: API endpoint exposed internal server version headers**
- Risk: Information disclosure aiding targeted attacks
- Remediation: Server headers stripped in nginx config (CHG-404)
- Verified: Re-tested October 25 — resolved

## Accepted Risks

- M-3: TLS 1.0 enabled on legacy partner integration endpoint (sunset planned Q1 2026)
- L-4: Verbose error messages in staging environment (staging is not in scope for SOC 2)
- L-5: Missing HSTS preload on marketing subdomain (non-production)

---

*Full report available under NDA from SecurePoint Labs.*
