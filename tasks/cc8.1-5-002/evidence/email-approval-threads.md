# CAB Email Approval Threads -- Q4 2025

---

## CHG-806: Database connection pool tuning

**Thread initiated:** November 11, 2025 9:15 AM ET
**Subject:** [CAB Async] CHG-806 — Database connection pool tuning — Medium Risk

**From:** Sanjay Reddy
**To:** Patricia Okafor, Michael Chen, Anya Volkov

> Team — CAB meeting is cancelled today (Veterans Day). We have one change pending review:
>
> **CHG-806:** Database connection pool tuning
> - Risk: Medium
> - Developer: Raj Kumar
> - Testing: Staging validated, 98.2% pass rate
> - Rollback plan: Revert pool config to previous values via Ansible
> - Impact: Potential latency improvement for high-concurrency queries
>
> Please review the ServiceNow ticket and respond with your approval or concerns by EOD Tuesday Nov 12.
>
> — Sanjay

**Reply 1 — Patricia Okafor** (Nov 11, 10:42 AM ET):
> Reviewed. Connection pool changes are low-impact with easy rollback. Approved.

**Reply 2 — Michael Chen** (Nov 11, 2:18 PM ET):
> Reviewed the ticket. No security implications for pool size adjustment. Approved.

**Reply 3 — Anya Volkov** (Nov 12, 12:30 PM ET):
> Test results look clean. Approved.

**Result:** 4/4 CAB members approved. Change deployed Nov 13.

---

## CHG-808: Webhook delivery retry with exponential backoff

**Thread initiated:** November 25, 2025 10:00 AM ET
**Subject:** [CAB Async] CHG-808 — Webhook retry with backoff — Medium Risk

**From:** Sanjay Reddy
**To:** Patricia Okafor, Michael Chen, Anya Volkov

> Team — No CAB meeting this week (Thanksgiving). One change pending:
>
> **CHG-808:** Add webhook delivery retry with exponential backoff
> - Risk: Medium
> - Developer: Derek Kim
> - Testing: Staging validated, 97.9% pass rate
> - Rollback plan: Disable retry via feature flag
> - Impact: Improved webhook reliability for integrations
>
> Please respond with approval or concerns by EOD Wednesday Nov 26.
>
> — Sanjay

**Reply 1 — Patricia Okafor** (Nov 25, 11:30 AM ET):
> Reviewed. Feature flag rollback is solid. Approved.

**Reply 2 — Michael Chen** (Nov 26, 9:15 AM ET):
> Reviewed. No security concerns with retry logic. Approved.

**Result:** 3/4 CAB members approved (Anya Volkov did not respond — out of office for Thanksgiving). Quorum met (VP Eng + 2 others).

---

## CHG-810: Rate limiting for public GraphQL endpoint

**Thread initiated:** December 9, 2025 3:00 PM ET
**Subject:** [CAB Async] CHG-810 — GraphQL rate limiting — High Risk

**From:** Sanjay Reddy
**To:** Patricia Okafor, Michael Chen, Anya Volkov

> Team — CAB meeting was cancelled today due to company all-hands. We have a High-risk change pending:
>
> **CHG-810:** Add rate limiting to public GraphQL endpoint
> - Risk: High
> - Developer: Raj Kumar
> - Testing: Staging validated, 98.5% pass rate. Security review completed.
> - Rollback plan: Disable rate limiting via WAF rule revert
> - Impact: Prevents API abuse; may affect high-volume customers if limits too aggressive
>
> This is High risk — please review the full ServiceNow ticket and security review before approving. Respond by EOD Thursday Dec 11.
>
> — Sanjay

**Reply 1 — Patricia Okafor** (Dec 10, 10:00 AM ET):
> Reviewed ticket and security review doc. Rate limits look reasonable (1000 req/min per API key). WAF rollback is fast. Approved.

**Reply 2 — Michael Chen** (Dec 11, 11:45 AM ET):
> Reviewed security implications. Rate limiting configuration looks solid. No bypass vectors identified. Approved.

**Result:** 3/4 CAB members approved (Anya Volkov on PTO, did not respond). Quorum met (VP Eng + 2 others).
