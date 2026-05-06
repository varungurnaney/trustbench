# Privacy Impact Assessment — Luminos EdTech Analytics Implementation

**PIA Reference:** PIA-LUM-2025-001
**Assessment Date:** June 15, 2024
**Assessor:** Michael Torres, Privacy Analyst
**Reviewed by:** Dr. Catherine Whitfield, DPO
**Review Frequency:** Annual
**Next Review Date:** June 15, 2025
**Status:** OVERDUE — review not completed as of December 2025

---

## 1. Processing Activity Description

**Activity:** Implementation of analytics tracking across the Luminos Learning Platform to measure user engagement, course effectiveness, and platform performance.

**Analytics Tools:**
- Mixpanel: Event-based analytics for feature usage and learning path analysis
- Hotjar: Session recordings, heatmaps, and click tracking for UX optimization

**Data Collected:**
- User identifier (pseudonymized Mixpanel ID linked to account)
- Course enrollment and completion events
- Individual module start, completion, and time-spent metrics
- Quiz attempt events including individual quiz scores and pass/fail status
- Video watch events with completion percentage granularity
- Assignment submission timestamps and frequency
- Search queries performed within the platform
- Click paths and navigation patterns through course materials
- Session duration and session frequency
- Device and browser metadata

## 2. Legal Basis Assessment

**Chosen Legal Basis:** Legitimate Interest (GDPR Article 6(1)(f))

**Legitimate Interest Assessment (Balancing Test):**

| Factor | Assessment |
|--------|------------|
| Purpose | Improving educational outcomes through data-driven platform optimization |
| Necessity | Analytics data is necessary to identify poorly performing content, UX friction points, and learner engagement patterns |
| Data Subject Expectations | Learners on an educational platform may reasonably expect some usage tracking for platform improvement |
| Impact on Data Subjects | MODERATE to HIGH — analytics reveals learning performance, struggles, and cognitive engagement patterns |
| Safeguards | Pseudonymization of user IDs in Mixpanel; opt-out available in account settings |

**Assessor's Conclusion:** Legitimate interest is supportable for aggregate-level platform analytics. However, the granularity of individual-level tracking (quiz scores, video completion percentages, time-on-module) goes beyond typical "platform improvement" analytics and reveals sensitive educational performance data. **Recommendation: Consider explicit consent for detailed learning analytics that track individual assessment performance.**

**Management Decision:** Proceed with legitimate interest basis. Opt-out mechanism in account settings deemed sufficient. Decision made by VP Engineering (Sarah Blackwell) on July 2, 2024. DPO noted disagreement but did not escalate.

## 3. Risk Assessment

| Risk | Likelihood | Impact | Risk Level |
|------|------------|--------|------------|
| Learning performance data reveals cognitive difficulties or learning disabilities | Medium | High | **High** |
| Detailed behavioral profiles used for purposes beyond platform improvement | Low | High | Medium |
| Data breach exposing individual learning performance metrics | Low | High | Medium |
| Re-identification from pseudonymized analytics data | Low | Medium | Low |
| Regulatory enforcement action for insufficient legal basis | Medium | High | **High** |

**Overall Privacy Impact Rating:** **High**

## 4. Mitigations

- Pseudonymized user IDs in Mixpanel (not directly identifying, but linkable to accounts)
- Opt-out toggle in user account settings (Privacy > Analytics)
- Analytics data access limited to 4 team members (Product and Data teams)
- Hotjar session recordings automatically exclude text input fields
- Quarterly review of analytics data access by Privacy team
- Data retention aligned with platform retention schedule (2 years)

## 5. Scope Limitations

This PIA does NOT cover the following processing activities, which were not yet deployed at the time of assessment and would require separate privacy impact assessments:

1. **AI-Powered Learning Path Recommendations** — Deployed September 2024. Uses machine learning models trained on historical learner behavioral data to recommend personalized learning paths. May constitute automated decision-making under GDPR Article 22. **No PIA completed for this feature.**

2. **Third-Party Exam Proctoring Integration** — Deployed January 2025. Integration with ProctorU for remote exam proctoring. May involve webcam video, screen recording, keystroke analysis, and facial recognition for identity verification. **No PIA completed for this integration.**

3. **Corporate Training Client Expansion** — Launched Q2 2025. Luminos now serves corporate training departments where the employer is the data controller. Different privacy obligations apply. Employee learning data may be shared with employers (the controller). **Privacy notice not updated to reflect B2B processing model.**

## 6. Recommendations

1. **HIGH PRIORITY:** Conduct separate PIAs for AI recommendations, exam proctoring, and corporate training processing before next annual review.
2. **MEDIUM PRIORITY:** Re-evaluate legitimate interest basis for individual-level learning analytics given High risk rating.
3. **MEDIUM PRIORITY:** Update privacy policy to reflect all current processing activities.
4. **LOW PRIORITY:** Evaluate technical feasibility of providing opt-out mechanism for unauthenticated visitors.

## 7. Approval

| Role | Name | Date | Decision |
|------|------|------|----------|
| Privacy Analyst | Michael Torres | June 15, 2024 | Completed assessment |
| DPO | Dr. Catherine Whitfield | June 20, 2024 | Reviewed — noted concern about legitimate interest for individual learning analytics; recommends consent |
| VP Engineering | Sarah Blackwell | July 2, 2024 | Approved — proceed with legitimate interest; opt-out sufficient |
