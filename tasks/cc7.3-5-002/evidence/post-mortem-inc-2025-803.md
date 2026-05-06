# Post-Mortem: INC-2025-803

**Incident:** API Rate Limiting Bypass / Cross-Tenant Document Listing
**Severity:** SEV-2
**IC:** Carlos Mendez
**Author:** Carlos Mendez
**Date:** November 12, 2025

---

The API rate limiter was bypassed by an external researcher who discovered that rotating API keys within a session reset the rate limit counter, allowing enumeration of document IDs across tenant boundaries. The issue was in the rate limiting middleware which keyed on API key rather than tenant ID + IP combination. We patched the rate limiter to key on tenant ID and deployed the fix. No customer documents were actually accessed — only document IDs were enumerable.

**Action Items:**
1. Review all API middleware for similar tenant isolation gaps — Carlos Mendez — High — Dec 15
2. Add automated cross-tenant access testing to CI pipeline — Engineering — Medium — Jan 15
3. Implement API abuse detection alerting — Security Ops — Medium — Jan 31

---

Reviewed by: Marco DeLuca
Review Status: Returned for revision — November 14, 2025
Revision Notes: "Post-mortem does not meet Section 4.2 quality standards. Missing: incident timeline with timestamps, 5-Whys root cause analysis, quantified impact assessment (how many tenants affected, how many document IDs exposed), remediation details, detection improvement recommendations. Please revise and resubmit."
