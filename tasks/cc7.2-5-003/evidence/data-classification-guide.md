# Aether Insurance — Data Classification Quick Reference

**Last Updated:** September 2025

## Classification Levels

| Level | Description | Examples | Retention |
|-------|-------------|----------|-----------|
| **Restricted** | Regulated personal/financial data | SSN, bank accounts, medical records | Per regulatory requirement |
| **Confidential** | Business-sensitive data | Underwriting models, pricing algorithms, internal financials | 7 years |
| **Internal** | General business data | Internal communications, project documentation | 3 years |
| **Public** | Publicly available data | Marketing materials, public filings | 1 year minimum |

## System Classification

| System | Classification | Data Types |
|--------|---------------|------------|
| Policy Management | Restricted | Policyholder PII, policy terms, premium data |
| Claims Processing | Restricted | Claim details, medical records, payment data |
| Underwriting Engine | Confidential | Risk models, applicant data, decision rationale |
| Claims Adjudication Engine | Restricted | Adjudication decisions, override records, dispute data |
| Customer Portal | Restricted | Customer login, policy views, claim submissions |
| Admin Portal | Confidential | Administrative actions, configuration changes |
| Notification Service | Internal | Delivery receipts, message metadata |
