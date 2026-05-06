# Cloud Infrastructure Summary

**Document ID:** DOC-INF-001
**Last Updated:** October 2025

---

## 1. AWS Architecture

Orion Cloud operates a multi-region AWS architecture:

| Region | Purpose | Services |
|--------|---------|----------|
| us-east-1 (N. Virginia) | Primary production | EC2, RDS, S3, ElastiCache |
| us-west-2 (Oregon) | Disaster recovery and backup storage | S3, RDS read replicas |

## 2. Redundancy Design

- Application tier: Auto Scaling Groups across 3 AZs in us-east-1
- Database tier: Multi-AZ RDS with synchronous replication
- Storage: S3 with cross-region replication to us-west-2
- CDN: CloudFront with global edge locations

## 3. Network Architecture

- VPC with public, private, and data subnets
- Transit Gateway for cross-region connectivity
- Direct Connect for on-premises integration
- AWS PrivateLink for service-to-service communication

## 4. Security

- GuardDuty enabled in all regions
- AWS Config rules for compliance monitoring
- CloudTrail enabled with multi-region trail

---

*This document is for reference only. Full architecture documentation maintained in Confluence.*
