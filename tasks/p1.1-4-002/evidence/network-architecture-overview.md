# Nextera Health — Network Architecture Overview

**Document ID:** NET-ARCH-2025-v2
**Last Updated:** September 2025
**Owner:** Infrastructure Team

---

## Overview

Nextera Health operates a multi-tier cloud architecture on AWS in the eu-west-2 (London) region with disaster recovery in eu-west-1 (Dublin).

## Architecture Tiers

### 1. Edge Layer
- **CDN:** Cloudflare Enterprise (caching, DDoS protection, WAF)
- **DNS:** Cloudflare DNS with DNSSEC enabled
- **SSL/TLS:** Cloudflare-managed certificates, TLS 1.3 minimum

### 2. Application Layer
- **Compute:** AWS ECS Fargate (containerized microservices)
- **Load Balancing:** AWS ALB with health checks every 30 seconds
- **API Gateway:** AWS API Gateway for external API endpoints
- **Container Registry:** AWS ECR

### 3. Data Layer
- **Primary Database:** AWS RDS PostgreSQL 15.4 (Multi-AZ deployment)
- **Cache:** AWS ElastiCache Redis 7.0
- **Object Storage:** AWS S3 (encrypted with SSE-KMS)
- **Search:** AWS OpenSearch for health content search

### 4. Security Layer
- **Network Segmentation:** VPC with public/private/data subnets
- **Security Groups:** Principle of least privilege, no 0.0.0.0/0 inbound rules
- **VPN:** AWS Client VPN for administrative access
- **WAF:** Cloudflare WAF + AWS WAF (defense in depth)

## Monitoring
- Datadog APM for application performance monitoring
- AWS CloudWatch for infrastructure metrics
- PagerDuty for alerting and on-call management

## Compliance
- All health data encrypted at rest (AES-256 via AWS KMS)
- All data remains within UK/EU AWS regions
- Network flow logs retained for 12 months
