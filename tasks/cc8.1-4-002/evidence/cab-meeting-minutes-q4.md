# CAB Meeting Minutes -- Q4 2025

## October 6, 2025
**Attendees:** Andrea Ruiz (VP Eng), Derek Santos (SRE Director), Mei Lin (Security Lead), Carlos Vega (QA Lead)
**Quorum:** Met (4/4)

- CHANGE-501: Approved. Onboarding flow update. Medium risk.

## October 13, 2025
**Attendees:** Andrea Ruiz (VP Eng), Derek Santos (SRE Director), Mei Lin (Security Lead), Carlos Vega (QA Lead)
**Quorum:** Met (4/4)

- CHANGE-502: Approved. Kafka migration. High risk. Load testing results reviewed -- throughput within SLA targets.

## October 20, 2025
**Attendees:** Andrea Ruiz (VP Eng), Derek Santos (SRE Director), Mei Lin (Security Lead)
**Quorum:** Met (3/4)

- CHANGE-503: Approved. GraphQL subscriptions. High risk. Load test results reviewed.

## October 27, 2025
**Attendees:** Andrea Ruiz (VP Eng), Derek Santos (SRE Director), Mei Lin (Security Lead), Carlos Vega (QA Lead)
**Quorum:** Met (4/4)

- CHANGE-503 rollback review: Discussed rollback of GraphQL subscriptions on Oct 21. Error rate exceeded 2% threshold. Rollback executed in 8 minutes per procedure. Root cause: WebSocket connection pooling under production load not reproducible in staging. Derek noted this highlights staging environment fidelity gaps for WebSocket workloads.
- CHANGE-504: Approved. GraphQL subscription fix. High risk. New load test at 2x production traffic included.

## November 3, 2025
**Attendees:** Andrea Ruiz (VP Eng), Derek Santos (SRE Director), Carlos Vega (QA Lead)
**Quorum:** Met (3/4)

- CHANGE-505: Approved. Redis 7.2 upgrade. Medium risk.

## November 10, 2025
**Attendees:** Andrea Ruiz (VP Eng), Derek Santos (SRE Director), Mei Lin (Security Lead)
**Quorum:** Met (3/4)

- CHANGE-506: Approved. SCIM provisioning endpoint. High risk. Mei confirmed security implications reviewed in discussion. Note: formal testing evidence not yet attached to Jira ticket at time of approval. Lisa indicated test results would be uploaded before deployment.

## November 17, 2025
**Attendees:** Andrea Ruiz (VP Eng), Derek Santos (SRE Director), Mei Lin (Security Lead), Carlos Vega (QA Lead)
**Quorum:** Met (4/4)

- CHANGE-507 retrospective: curl CVE patch. Emergency process followed correctly. Approved retroactively.

## November 24, 2025
**Attendees:** Andrea Ruiz (VP Eng), Derek Santos (SRE Director), Carlos Vega (QA Lead)
**Quorum:** Met (3/4)

- CHANGE-508: Approved. Stripe webhook verification. Medium risk.

## December 1, 2025
**Attendees:** Andrea Ruiz (VP Eng), Derek Santos (SRE Director), Mei Lin (Security Lead), Carlos Vega (QA Lead)
**Quorum:** Met (4/4)

- CHANGE-509: Approved. DB read replica failover. High risk. Failover RTO of 12 seconds demonstrated in staging.

## December 8, 2025
**Attendees:** Andrea Ruiz (VP Eng), Derek Santos (SRE Director), Mei Lin (Security Lead)
**Quorum:** Met (3/4)

- CHANGE-510: Approved. K8s node pool scaling. Medium risk.

## December 15, 2025
**Attendees:** Andrea Ruiz (VP Eng), Derek Santos (SRE Director), Mei Lin (Security Lead), Carlos Vega (QA Lead)
**Quorum:** Met (4/4)

- CHANGE-510 rollback review: Pod scheduling failures caused by node affinity conflict. Rollback in 6 minutes. Root cause documented.
- CHANGE-511: Approved. Node affinity fix. Medium risk.
