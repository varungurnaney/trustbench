# Software Development Lifecycle (SDLC) Policy

**Document ID:** POL-SDLC-017
**Version:** 3.8
**Effective Date:** March 1, 2025
**Owner:** Engineering Operations
**Classification:** Internal

---

## 1. Purpose

This policy defines Atlas Integration Corp's SDLC practices for maintaining processing integrity in data integration and ETL systems.

## 2. Scope

All data integration pipelines, ETL processes, and API integration services developed by Atlas Integration Corp.

## 3. Code Review

### 3.1 Standard Review

All pull requests require at least one approving review. Reviewers verify data transformation logic, error handling, and schema compatibility.

### 3.2 Data Pipeline Review

Changes to data transformation logic, schema mappings, or ETL configurations require review by both a developer and a data engineer.

## 4. Static Analysis

### 4.1 SAST Quality Gate

SonarQube scans on every PR. Critical blocks merge. High within 30 days. Medium within 90 days.

### 4.2 Data Quality Rules

Data quality rules are defined in Great Expectations and version-controlled alongside pipeline code. Rule changes follow the same review process as code changes.

## 5. Deployment

### 5.1 Standard Pipeline

Build, test, SAST, staging deploy, staging validation, production approval, production deploy, post-deploy verification.

### 5.2 Staging Validation for Data Pipelines

Data pipeline changes must be validated in staging using a representative sample dataset. Validation must confirm:

- Record count preservation (source in = destination out)
- Schema conformance (all output fields match expected types and formats)
- Transformation accuracy (sample records manually verified)
- Null handling (null/empty values processed according to specification)
- Idempotency (re-running the pipeline produces the same result)

## 6. Processing Integrity

### 6.1 Input Validation

All inbound data feeds validated against Avro/Protobuf schemas at ingestion. Malformed records are quarantined to a dead-letter queue for manual review.

### 6.2 Data Reconciliation

All production pipelines implement daily reconciliation checks:

- Record count: source count must match destination count within 0.01% tolerance
- Checksum: SHA-256 checksums computed on key fields must match
- Completeness: all expected source files/feeds must be received before processing begins

### 6.3 Dead Letter Queue

Records that fail validation or processing are routed to a dead-letter queue (DLQ). DLQ monitoring alerts when queue depth exceeds 100 records. DLQ records must be reviewed and resolved within 48 hours.

---

**Approved by:** Patricia Herrera, VP Engineering
**Next Review Date:** March 2026
