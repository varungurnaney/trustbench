# Cobalt Systems -- Disaster Recovery Site Information

**Document ID:** CS-INF-DR-002  
**Version:** 2.1  
**Last Updated:** 2025-09-20  

---

## 1. DR Site Overview

Cobalt Systems maintains a warm disaster recovery site in AWS us-west-2 (Oregon) region as the secondary site for all production workloads hosted in the primary us-east-1 (N. Virginia) region.

## 2. Infrastructure Specifications

### 2.1 Compute Resources

| Resource | Primary (us-east-1) | DR (us-west-2) |
|----------|---------------------|-----------------|
| Application Servers | 12x m6i.2xlarge | 6x m6i.2xlarge (scaled on activation) |
| Database Servers | 6x r6i.4xlarge | 3x r6i.4xlarge (read replicas active) |
| Load Balancers | 2x ALB | 1x ALB (pre-configured) |
| Cache Layer | 3x ElastiCache r6g.xlarge | 2x ElastiCache r6g.xlarge |

### 2.2 Network Configuration

- **VPC CIDR:** 10.20.0.0/16
- **Transit Gateway:** tgw-0a1b2c3d4e5f67890 (cross-region peering)
- **VPN Tunnels:** 2x IPSec tunnels to corporate network (vpn-dr-01, vpn-dr-02)
- **DNS Failover:** Route 53 health checks with 60-second failover TTL
- **Direct Connect:** 1x 10 Gbps dedicated connection via Equinix Portland

### 2.3 Storage

- **S3 Cross-Region Replication:** Enabled for all production buckets
- **EBS Snapshots:** Replicated daily to us-west-2
- **EFS:** Cross-region replication for shared file systems

## 3. Activation Procedures

### 3.1 Failover Trigger Criteria

Failover to the DR site is triggered when:
1. Primary site is unreachable for > 15 minutes
2. Declared by the VP of Infrastructure or CISO
3. Planned maintenance requiring > 4 hours of downtime

### 3.2 Failover Steps

1. Confirm primary site status via independent monitoring (StatusCake, Pingdom)
2. Activate DR runbook in PagerDuty (Runbook: CS-DR-ACTIVATE-001)
3. Scale DR compute resources to full production capacity via Auto Scaling
4. Promote database read replicas to primary
5. Update Route 53 DNS records to point to DR ALB
6. Verify application health checks pass
7. Notify stakeholders via incident communication channel

### 3.3 Estimated Failover Time

- **Automated (DNS-based):** 5-10 minutes
- **Full manual failover:** 30-45 minutes
- **Including database promotion:** 45-60 minutes

## 4. DR Testing Schedule

Full DR failover tests are conducted semi-annually:
- **H1 Test:** Scheduled for March
- **H2 Test:** Scheduled for September

Last successful test: September 14, 2025. Failover completed in 38 minutes.

## 5. Contact Information

| Role | Name | Phone |
|------|------|-------|
| DR Coordinator | Marcus Chen | +1 (415) 555-0142 |
| Network Lead | Priya Sharma | +1 (415) 555-0187 |
| Database Lead | James Liu | +1 (415) 555-0203 |
| On-Call Escalation | PagerDuty | cobalt-infra-oncall |

---

*Document Classification: Internal Use Only*
