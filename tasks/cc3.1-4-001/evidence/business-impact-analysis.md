# Vertex AI Corp -- Business Impact Analysis Summary

**Document ID:** VAC-BIA-2025-001  
**Version:** 2.0  
**Last Updated:** 2025-08-15  
**Owner:** David Kim, Director of IT  
**Approved By:** Robert Tanaka, CFO  

---

## 1. Purpose

This Business Impact Analysis (BIA) identifies critical business processes and quantifies the operational and financial impacts of disruption. The BIA supports business continuity planning and disaster recovery prioritization.

## 2. Critical Business Processes

### 2.1 Tier 1 -- Mission Critical (RTO: 4 hours, RPO: 1 hour)

| Process | System Dependencies | Revenue Impact (per hour) | Owner |
|---------|---------------------|--------------------------|-------|
| Customer AI Platform | Production API cluster, ML inference engines, PostgreSQL primary | $45,000 | Amara Osei |
| Customer Data Ingestion | Kafka clusters, ETL pipelines, S3 storage | $28,000 | Thomas Wright |
| Authentication & Authorization | Okta SSO, CyberArk PAM, Active Directory | $45,000 (blocks all systems) | Elena Vasquez |

### 2.2 Tier 2 -- Business Critical (RTO: 8 hours, RPO: 4 hours)

| Process | System Dependencies | Revenue Impact (per hour) | Owner |
|---------|---------------------|--------------------------|-------|
| Model Training Pipeline | GPU cluster (p4d instances), MLflow, S3 model registry | $12,000 | Thomas Wright |
| Customer Portal | Web application, PostgreSQL replica, CDN | $8,500 | Amara Osei |
| Billing & Invoicing | Stripe integration, PostgreSQL financial DB, reporting engine | $6,000 | Robert Tanaka |

### 2.3 Tier 3 -- Important (RTO: 24 hours, RPO: 24 hours)

| Process | System Dependencies | Revenue Impact (per hour) | Owner |
|---------|---------------------|--------------------------|-------|
| Internal Communications | Slack, Google Workspace, Zoom | $2,000 (productivity loss) | David Kim |
| HR & Payroll | BambooHR, ADP | $500 | HR Director |
| Development Environment | GitHub, CI/CD (GitLab), staging clusters | $3,000 (productivity loss) | Thomas Wright |

## 3. Maximum Tolerable Downtime (MTD)

| Tier | MTD | Financial Impact Threshold |
|------|-----|---------------------------|
| Tier 1 | 8 hours | $360,000 |
| Tier 2 | 24 hours | $204,000 |
| Tier 3 | 72 hours | $180,000 |

## 4. Dependencies and Single Points of Failure

### 4.1 Infrastructure Dependencies
- **AWS us-east-1:** Primary hosting region for all Tier 1 systems
- **Equinix DC5:** Network interconnection point for corporate network
- **Cloudflare:** CDN and DDoS protection for all public-facing services

### 4.2 Identified Single Points of Failure
1. Kafka cluster leader election during region failover (mitigated by cross-region replication)
2. CyberArk vault server -- HA pair, but recovery procedure requires manual intervention
3. DNS propagation delay during DR activation (mitigated by low TTL settings)

## 5. Recovery Prioritization

In a disaster scenario, systems shall be recovered in the following order:
1. Authentication infrastructure (Okta, AD)
2. Database clusters (PostgreSQL primary)
3. API and inference engines
4. Customer-facing portal
5. Internal tools and communication

## 6. Annual Review

This BIA is reviewed annually in conjunction with the DR planning cycle. Last tabletop validation: September 14, 2025.

---

*Document Classification: Internal -- Confidential*
