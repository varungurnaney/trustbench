# CAB Meeting Minutes -- Q4 2025

## October 7, 2025
**Attendees:** Nathan Cole (VP Eng), Yuki Tanaka (Security Lead), Raj Mehta (SRE Director)
**Quorum:** Met (3/4)

- CHG-701: Approved. Dashboard widget upgrade. Low risk.

## October 14, 2025
**Attendees:** Nathan Cole (VP Eng), Yuki Tanaka (Security Lead), Raj Mehta (SRE Director), Diana Ford (Eng Manager)
**Quorum:** Met (4/4)

- CHG-702: Approved. RBAC for reporting module. High risk. Security review confirmed access control model follows least-privilege principle.

## October 21, 2025
**Attendees:** Nathan Cole (VP Eng), Yuki Tanaka (Security Lead), Raj Mehta (SRE Director)
**Quorum:** Met (3/4)

- CHG-703: Approved. Data aggregation rounding fix. Medium risk.

## November 4, 2025
**Attendees:** Nathan Cole (VP Eng), Yuki Tanaka (Security Lead), Raj Mehta (SRE Director), Diana Ford (Eng Manager)
**Quorum:** Met (4/4)

- CHG-704 retrospective: SQL injection emergency fix. Dual approval from VP Eng and CISO confirmed. Emergency process followed correctly. Root cause: parameterized query not used in report export module added in Q3. Action: code review checklist updated to include SQL injection checks.
- CHG-705: Approved. JWT session migration. High risk. Security review confirmed token signing and expiry handling.

## November 11, 2025
**Attendees:** Nathan Cole (VP Eng), Yuki Tanaka (Security Lead), Raj Mehta (SRE Director)
**Quorum:** Met (3/4)

- CHG-706: Approved. Data export API. High risk. Security review completed. CAB discussed deployment timeline -- customer contract requires delivery by November 15. Nathan proposed deploying Thursday instead of Saturday maintenance window. CAB voted to approve a business justification exception for a Tuesday-Thursday deployment window per Section 5.

## December 9, 2025
**Attendees:** Nathan Cole (VP Eng), Yuki Tanaka (Security Lead), Diana Ford (Eng Manager)
**Quorum:** Met (3/4)

- CHG-708 retrospective: Auth token expiry emergency fix. Discussed at length. Nathan acknowledged that CISO approval was not obtained -- Yuki Tanaka was unreachable at 3:00 AM. Nathan approved alone. Additionally, developer (Anika Patel) deployed the change because the SRE on-call engineer (Raj Mehta) did not respond to page. Yuki noted that the dual approval requirement exists specifically for high-severity situations and should not be bypassed. CAB recommended: (1) establish a secondary CISO delegate for after-hours emergencies, (2) ensure SRE on-call rotation has backup coverage.
- CHG-709: Approved. Database sharding phase 1. High risk. Load testing and security review completed.
