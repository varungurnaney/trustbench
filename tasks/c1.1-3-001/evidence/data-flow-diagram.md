# Crestline Data Systems — Data Flow Diagram (Restricted Data)

**Document ID:** ARCH-DFD-002
**Version:** 5.1
**Last Updated:** November 10, 2025
**Author:** Marcus Rivera, Principal Architect
**Classification:** Internal

---

## 1. Overview

This document describes the data flows involving Restricted data (PII, payment data) within Crestline Data Systems' production environment. All flows were documented as part of the annual Data Protection Impact Assessment (DPIA).

## 2. Data Ingestion Flows

### 2.1 Customer Registration

```
Customer Browser → [TLS 1.3] → CloudFront CDN → [TLS 1.3] → ALB → [TLS 1.2] → app.crestline.com
    → Application Encryption Layer (AES-256-GCM) → crestline_prod.users table
    PII encrypted at field level before database write
```

### 2.2 Payment Processing

```
Customer Browser → [TLS 1.3] → payments.crestline.com → [TLS 1.2] → Stripe API
    Card data never touches Crestline servers (Stripe.js tokenization)
    Only Stripe token stored in crestline_prod.payment_methods
```

### 2.3 Partner Data Import

```
Partner SFTP Upload → partner-sftp.crestline.com (SSH/SFTP)
    → S3 Landing Bucket (SSE-KMS encrypted) → Lambda Processor
    → crestline_prod.partner_data table (field-level encryption applied)
```

## 3. Internal Data Flows

### 3.1 Analytics Pipeline (Nightly ETL)

```
crestline_prod.users → Nightly ETL Job (AWS Glue)
    → crestline_analytics.customer_profiles
    → crestline_analytics.engagement_events

NOTE: ETL job copies email and phone fields for analytics query performance.
Analytics team has read-only access to crestline_analytics database.
```

### 3.2 Customer Support Access

```
Support Portal → [TLS 1.2] → admin-api.crestline.com
    → Application decrypts PII on-demand for authorized support agents
    → Decrypted data displayed in browser, never cached or exported
```

### 3.3 Reporting Pipeline

```
crestline_analytics → Metabase BI Tool (grafana.crestline.net:3000)
    → Aggregated reports (no PII in reports)
    → PDF export to S3 reporting bucket (SSE-S3 encrypted)
```

## 4. Data Export Flows

### 4.1 REST API Exports

```
Authorized API Client → [TLS 1.2/1.3] → api.crestline.com/api/v2/*
    → API Gateway (rate limited, authenticated via OAuth 2.0)
    → Application decrypts requested PII fields
    → JSON response over TLS
    DLP Rule DLP-API-001 monitors bulk exports (>1000 records)
```

### 4.2 GraphQL API Exports (NEW — Launched October 2025)

```
Authorized API Client → [TLS 1.3] → api.crestline.com/graphql
    → Apollo GraphQL Server (authenticated via OAuth 2.0)
    → Supports nested queries with pagination (cursor-based)
    → Can query users { email, phone, address } with connections
    → JSON response over TLS
    
NOTE: GraphQL API supports batch queries via query aliases and 
      connection pagination. A single query can retrieve all user 
      PII by paginating through the users connection. Rate limiting 
      is per-query, not per-record, so bulk extraction is possible 
      within rate limits.
```

### 4.3 SFTP Partner Exports

```
Scheduled Export Job → Encrypted CSV (PGP) → partner-sftp.crestline.com
    → Partner retrieves via SFTP
    Exports logged in CloudTrail and reviewed weekly
```

## 5. Data Deletion

### 5.1 Customer Deletion Requests (GDPR/CCPA)

```
Customer Request → Support Ticket → Privacy Team Review
    → Deletion Job: crestline_prod (hard delete) + crestline_analytics (hard delete)
    → Backup retention: 30 days (encrypted backups auto-expire)
    → Confirmation sent to customer within 30 days
```

---

**Reviewed by:** Rachel Nguyen, CISO — November 12, 2025
**Next Review:** November 2026
