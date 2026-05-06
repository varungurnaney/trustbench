# CAB Meeting Minutes -- Q4 2025

## October 1, 2025
**Attendees:** Marcus Webb (VP Eng), Priya Sharma (Security Lead), Tom Nakamura (Platform Eng Lead)
**Quorum:** Met (3/3)

- CHG-301: Approved. Billing template update, low risk. No concerns.

## October 8, 2025
**Attendees:** Marcus Webb (VP Eng), Priya Sharma (Security Lead), Rachel Gonzalez (Dev Lead)
**Quorum:** Met (3/3)

- CHG-302: Approved. MFA implementation for admin portal. High risk. Security review completed by Priya -- no findings. Rollback plan reviewed.

## October 15, 2025
**Attendees:** Marcus Webb (VP Eng), Priya Sharma (Security Lead), Tom Nakamura (Platform Eng Lead)
**Quorum:** Met (3/3)

- CHG-303: Approved. PII migration to encrypted datastore. High risk. Security review confirmed data flow analysis complete. Priya noted encryption-at-rest and in-transit verified.

## October 22, 2025
**Attendees:** Marcus Webb (VP Eng), Priya Sharma (Security Lead), James Liu (Dev Lead)
**Quorum:** Met (3/3)

- CHG-304: Approved. Timezone bug fix. Low risk.

## October 29, 2025
**Attendees:** Marcus Webb (VP Eng), David Okonkwo (Security Eng), Tom Nakamura (Platform Eng Lead)
**Quorum:** Met (3/3)

- CHG-305: Approved. PostgreSQL upgrade. High risk. Security review by David confirmed no known CVEs in PG16 at time of review.

## November 5, 2025
**Attendees:** Marcus Webb (VP Eng), Tom Nakamura (Platform Eng Lead)
**Quorum:** NOT MET (2/3 -- Security Lead absent, team at offsite training)

- CHG-306: Approved. Webhook endpoint for partner integrations. High risk. Marcus noted that the security team is at offsite training this week and the security review has not been completed. Marcus approved the change citing business urgency -- partner launch deadline of November 15. Action item: security team to perform a post-deployment review when available.

## November 12, 2025
**Attendees:** Marcus Webb (VP Eng), Priya Sharma (Security Lead), Tom Nakamura (Platform Eng Lead)
**Quorum:** Met (3/3)

- CHG-307 retrospective: OpenSSL emergency patch reviewed. Root cause: CVE-2025-31337 critical vuln. Emergency process followed correctly. Approved retroactively.
- Action item from Nov 5: Priya noted that post-deployment security review of CHG-306 (webhook endpoint) has not yet been scheduled. Marcus to follow up with Sarah.

## November 19, 2025
**Attendees:** Marcus Webb (VP Eng), Priya Sharma (Security Lead), Rachel Gonzalez (Dev Lead)
**Quorum:** Met (3/3)

- CHG-308: Approved. Notification service refactor. Medium risk.

## November 26, 2025
**Attendees:** Marcus Webb (VP Eng), David Okonkwo (Security Eng), Tom Nakamura (Platform Eng Lead)
**Quorum:** Met (3/3)

- CHG-309: Approved. OAuth2 PKCE flow. High risk. Security review by David confirmed PKCE implementation follows RFC 7636.

## December 10, 2025
**Attendees:** Marcus Webb (VP Eng), Priya Sharma (Security Lead), James Liu (Dev Lead)
**Quorum:** Met (3/3)

- CHG-311: Approved. SSO SAML integration. High risk. Security review confirmed SAML assertion validation, replay protection, and signature verification.
- Priya raised that the post-deployment security review for CHG-306 (webhook endpoint) was still not completed. Marcus acknowledged and committed to scheduling it before year-end.

## December 17, 2025
**Attendees:** Marcus Webb (VP Eng), Priya Sharma (Security Lead), Tom Nakamura (Platform Eng Lead)
**Quorum:** Met (3/3)

- CHG-312: Approved. Audit logging schema migration. Medium risk.
- Year-end review: 12 changes processed in Q4. One change (CHG-306) deployed without security review -- post-deployment review still pending.
