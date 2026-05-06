# Customer Sector Onboarding Timeline

**Prepared by:** Customer Success, Prism Data Platform
**Date:** January 5, 2026
**Classification:** Internal

---

## 1. Sector Expansion History

Prism Data Platform historically served only financial services customers. In 2025, the company expanded into healthcare and retail sectors.

## 2. Financial Services (Existing)

| Customer | Onboarded | Data Types | Regulatory Requirements |
|----------|-----------|-----------|------------------------|
| Apex Capital Management | January 2023 | Trade data, market feeds, portfolio positions | SEC, FINRA, SOX |
| Meridian Investments | March 2023 | Order flow, risk analytics | SEC, FINRA |
| Northfield Quantitative | June 2023 | Algorithmic trading signals, backtesting data | SEC, FINRA |
| Summit Wealth Partners | February 2024 | Client portfolio data, performance reporting | SEC, SOX |
| Blackridge Asset Management | September 2024 | Multi-asset trading data, compliance feeds | SEC, FINRA, MiFID II |
| Heritage Trust Company | January 2025 | Trust account data, estate analytics | SEC, FDIC |

## 3. Healthcare (New — 2025)

| Customer | Onboarded | Data Types | Regulatory Requirements |
|----------|-----------|-----------|------------------------|
| Lakeview Health System | April 2025 | Patient flow analytics, de-identified clinical data | HIPAA, HITECH |
| Coastal Medical Group | May 2025 | Claims processing, appointment scheduling data | HIPAA |
| Mountain View Regional Hospital | July 2025 | Emergency department analytics, bed management | HIPAA, HITECH |

## 4. Retail (New — 2025)

| Customer | Onboarded | Data Types | Regulatory Requirements |
|----------|-----------|-----------|------------------------|
| GreenLeaf Grocers | August 2025 | POS transaction streams, inventory analytics | PCI DSS |
| Metro Department Stores | October 2025 | Customer purchase analytics, loyalty program data | PCI DSS, CCPA |

## 5. Multi-Sector Incident Response Considerations

With customers across financial services, healthcare, and retail, incidents may now require:
- Simultaneous notification to multiple regulatory bodies (SEC, HIPAA, PCI DSS council)
- Different notification timelines per sector (HIPAA: 60 days, SEC: varies, PCI: 72 hours)
- Sector-specific data handling during forensic investigation
- Cross-sector data isolation verification (critical after INC-2025-904)

## 6. IRP Sector Coverage Assessment

The current IRP (v2.3, March 2025) was written when Prism served only financial services customers. The policy references:
- "Financial data" and "trading analytics" throughout
- SEC and FINRA notification requirements
- No mention of HIPAA, PCI DSS, or multi-sector incident scenarios
- No procedure for cross-sector data isolation verification
- No multi-regulatory notification coordination procedure

---

**Reviewed by:** Grace Kim, VP Customer Success
**Date:** January 6, 2026
