# Luminos EdTech — Penetration Test Executive Summary

**Test Period:** October 1-14, 2025
**Testing Firm:** CyberGuard Security Ltd
**Report ID:** PEN-2025-LUM-003
**Classification:** Confidential

---

## Scope

External and internal penetration testing of the Luminos Learning Platform:
- External web application testing (learn.luminos.io, www.luminos.io, api.luminos.io)
- AWS infrastructure review (eu-west-2)
- API security testing (REST API endpoints)
- Mobile application testing (iOS and Android)

## Summary of Findings

| Severity | Count |
|----------|-------|
| Critical | 0 |
| High | 1 |
| Medium | 3 |
| Low | 5 |
| Informational | 8 |

## High Severity Finding

**VULN-001: Insecure Direct Object Reference (IDOR) in Course Progress API**
- Endpoint: GET /api/v2/users/{user_id}/progress
- An authenticated user can access another user's course progress by modifying the user_id parameter
- Impact: Unauthorized access to other learners' course completion and quiz score data
- Recommendation: Implement authorization checks to ensure users can only access their own progress data
- Remediation Status: Fixed (October 20, 2025)

## Medium Severity Findings

- VULN-002: Missing rate limiting on authentication endpoint (Fixed October 18, 2025)
- VULN-003: Verbose error messages exposing internal stack traces (Fixed October 22, 2025)
- VULN-004: Session token not invalidated on password change (Remediation in progress)

## Conclusion

The overall security posture of the Luminos platform is satisfactory. The critical IDOR vulnerability was promptly remediated. Remaining medium and low findings are being tracked in the remediation plan with target completion by December 31, 2025.
