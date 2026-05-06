# Helios Data Systems — Network Architecture Overview

**Document ID:** DOC-ARCH-2025-002
**Version:** 3.1
**Last Updated:** November 15, 2025
**Owner:** Marcus Webb, VP Engineering
**Classification:** Internal — Confidential

---

## 1. Overview

Helios Data Systems operates a multi-region AWS infrastructure spanning us-east-1 (primary) and us-west-2 (disaster recovery).

## 2. VPC Architecture

### 2.1 Production VPC (vpc-prod-east-1)
- CIDR: 10.0.0.0/16
- Public subnets: 10.0.1.0/24, 10.0.2.0/24 (ALB, NAT Gateway)
- Private subnets: 10.0.10.0/24, 10.0.11.0/24 (EKS worker nodes)
- Database subnets: 10.0.20.0/24, 10.0.21.0/24 (RDS, ElastiCache)
- No internet gateway on database subnets

### 2.2 Staging VPC (vpc-staging-east-1)
- CIDR: 10.1.0.0/16
- Peered to Production VPC for integration testing (restricted to port 443 only)

### 2.3 Management VPC (vpc-mgmt-east-1)
- CIDR: 10.2.0.0/16
- Bastion hosts, monitoring agents, CyberArk connectors
- VPN gateway for admin access (Cisco AnyConnect)

## 3. Security Groups

| Group | Inbound | Outbound | Attached To |
|-------|---------|----------|-------------|
| sg-alb-prod | 443 from 0.0.0.0/0 | 8080 to sg-eks-prod | Application Load Balancer |
| sg-eks-prod | 8080 from sg-alb-prod | 5432 to sg-rds-prod, 6379 to sg-redis-prod | EKS worker nodes |
| sg-rds-prod | 5432 from sg-eks-prod, sg-mgmt | None | RDS PostgreSQL |
| sg-redis-prod | 6379 from sg-eks-prod | None | ElastiCache Redis |
| sg-mgmt | 22 from VPN, 443 from VPN | All to vpc-prod-east-1 | Bastion hosts |

## 4. DNS and CDN

- Route 53 for DNS management
- CloudFront for static asset delivery
- WAF attached to CloudFront and ALB distributions

## 5. Monitoring

- Datadog for APM and infrastructure monitoring
- CloudWatch for AWS-native metrics
- PagerDuty for on-call alerting
- Splunk for security log aggregation

---

**Approved by:** Marcus Webb, VP Engineering
