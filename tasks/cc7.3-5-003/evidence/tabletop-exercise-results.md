# IRP Tabletop Exercise — Results Summary

**Exercise Date:** March 18, 2025
**Facilitator:** Nathan Reeves, CISO
**Classification:** Internal

---

## 1. Exercise Details

- **Scenario:** Supply chain compromise — malicious update to a critical third-party data enrichment API used by financial services customers.
- **Duration:** 2 hours
- **Participants:**

| Name | Role | Attendance |
|------|------|-----------|
| Nathan Reeves | CISO | Present (Facilitator) |
| Leah Winters | Security Operations Manager | Present |
| Victor Osman | VP Engineering | Present |
| Daniel Cho | Principal SRE | Present |
| Samantha Lee | Head of Legal | Present |
| Rebecca Torres | CEO | Present |
| Grace Kim | VP Customer Success | Present |

## 2. Scenario Walkthrough

### Phase 1: Detection (10:00 - 10:25)
- **Inject:** Customer reports anomalous data in their financial analytics dashboard. Data enrichment API responses contain unexpected fields.
- **Discussion:** Team identified monitoring gaps — no integrity checks on third-party API responses. Agreed that detection would likely come from customer reports rather than internal monitoring.

### Phase 2: Triage & Containment (10:25 - 11:00)
- **Inject:** Investigation reveals the data enrichment API was compromised 3 days ago. All financial customer data processed in the last 3 days may contain manipulated values.
- **Discussion:** Team debated whether to immediately shut down the enrichment pipeline (impacting all customers) or implement selective filtering. Agreed on full pipeline halt within 15 minutes of confirmation.
- **Observation:** No pre-built playbook for third-party API compromise. Team improvised containment steps.

### Phase 3: Communication (11:00 - 11:30)
- **Inject:** 4 hedge fund clients demanding immediate updates. 2 clients threatening regulatory complaints.
- **Discussion:** Legal team confirmed 48-hour customer notification SLA. Customer Success to contact affected clients within 2 hours of confirmation.
- **Observation:** Status page template does not include a category for "data integrity" incidents — only "availability" and "latency."

### Phase 4: Recovery & Lessons Learned (11:30 - 12:00)
- **Discussion:** Recovery requires re-processing 3 days of data with verified API responses. Estimated 8-12 hours.
- **Observation:** No documented procedure for bulk data reprocessing in the IRP.

## 3. Action Items

| Item | Owner | Due Date | Status |
|------|-------|----------|--------|
| Create third-party API compromise runbook | Leah Winters | April 30, 2025 | Complete |
| Add "data integrity" category to status page | Customer Success | April 15, 2025 | Complete |
| Implement API response integrity checking (hash validation) | Engineering | June 30, 2025 | Complete |
| Add bulk data reprocessing procedure to IRP | Daniel Cho | May 15, 2025 | Complete |

## 4. Overall Assessment

The team demonstrated strong communication and decision-making during the exercise. Key gaps identified were around third-party supply chain scenarios and data integrity incident handling. All action items targeted for completion by June 2025.

## 5. Observations on IRP Currency

**Note:** This exercise was conducted using IRP v2.3 (March 2025) and the pre-migration VM-based architecture. The exercise scenario assumed the monolithic data pipeline and single-region deployment. Since this exercise, the platform has undergone a complete migration to Kubernetes (Phase 1-6, June-December 2025), added healthcare and retail customer sectors, and changed the monitoring stack. The IRP has not been updated to reflect these changes, and no additional tabletop exercise has been conducted to validate the IRP against the new architecture.

---

**Approved by:** Rebecca Torres, CEO
**Date:** March 22, 2025
