# Redstone Capital Partners — Security Function Organization

**Document ID:** ORG-SEC-005
**Version:** 2.1
**Effective Date:** April 1, 2025
**Classification:** Internal

---

## Executive Leadership Structure

```
CEO — Margaret Chen
├── CFO — William Park
│   ├── Finance & Accounting
│   └── Internal Audit — Director, James Liu
├── CTO — David Harrington
│   ├── VP of Engineering — Samantha Wells
│   │   ├── Application Development (6 teams, 42 engineers)
│   │   ├── Platform Engineering (8 engineers)
│   │   └── QA & Release Engineering (6 engineers)
│   ├── CISO — Rebecca Torres
│   │   ├── Security Operations — Director, Marcus Greene
│   │   │   ├── SOC Team (6 analysts, 24/7 coverage)
│   │   │   ├── Incident Response (3 FTEs)
│   │   │   └── Threat Intelligence (2 FTEs)
│   │   ├── GRC — Director, Amanda Singh
│   │   │   ├── Compliance Analysts (3 FTEs)
│   │   │   └── Risk Analysts (2 FTEs)
│   │   ├── Security Architecture — Principal Architect, Carlos Mendez
│   │   └── Application Security — Manager, Yuki Tanaka
│   │       ├── AppSec Engineers (3 FTEs)
│   │       └── Security Champions Program (embedded in dev teams)
│   └── VP of IT Operations — Kevin O'Brien
│       ├── Infrastructure (5 FTEs)
│       ├── Cloud Operations (4 FTEs)
│       ├── Help Desk (4 FTEs)
│       └── Database Administration (3 FTEs)
├── COO — Patricia Freeman
│   ├── Client Operations
│   └── Compliance — Chief Compliance Officer, Helen Zhao
├── General Counsel — Robert Kline
│   ├── Corporate Legal
│   └── Privacy — Data Protection Officer, Eva Mueller (London)
└── CHRO — Michael Davis
    ├── HR Operations
    ├── Talent Acquisition
    └── Learning & Development
```

## CTO Role Scope and Security Oversight Context

The CTO (David Harrington) oversees three direct reports: VP of Engineering, CISO, and VP of IT Operations.

**Important context regarding CTO's day-to-day involvement:**

David Harrington's role at Redstone Capital Partners is primarily strategic and architecture-focused. He joined in 2019 from a CTO role at a mid-size fintech company. His day-to-day activities include:

- Technology strategy and roadmap planning
- Vendor and build-vs-buy decisions
- Board and investor technology presentations
- Architecture review board participation (monthly)
- Cross-functional coordination with COO on operational technology

David does **not** participate in:

- Day-to-day IT operations (managed by VP of IT Operations Kevin O'Brien)
- Production incident response (managed by CISO Rebecca Torres)
- Code reviews or deployment approvals (managed by VP of Engineering Samantha Wells)
- Security tool selection or configuration (CISO authority)

**CISO Independence Indicators:**

| Indicator | Status |
|-----------|--------|
| CISO direct report to CTO | Yes |
| CTO involved in day-to-day IT operations | No |
| CTO involved in production security decisions | No |
| CISO has deployment halt authority | Yes (policy Section 3.2) |
| CISO has independent Board access | Yes (quarterly Board Risk Committee) |
| CISO budget proposed independently | Yes (then reviewed by CTO, approved by CFO) |
| CTO has overridden CISO security recommendation | No recorded instances |
| CISO chairs SGC | No (CEO chairs) |

## Security Function Key Metrics

| Metric | Value |
|--------|-------|
| Total Security FTEs | 22 (including CISO) |
| Security-to-Company Ratio | 1:18 (400 total employees) |
| Security Budget | $4.8M (2025) |
| Security Budget as % of IT Budget | 14.2% |
| Previous Year Security Budget | $5.6M (2024) |
| Budget Change | -14.3% year-over-year |
| Budget Reduction Reason | Infrastructure optimization savings + renegotiated vendor contracts |
| CISO Tenure | 4 years (joined March 2021) |
| Average Security Team Tenure | 2.8 years |
| Open Positions | 1 (Threat Intelligence Analyst — open since August 2025) |

## Security Governance Committee Composition

| Role | Name | Title |
|------|------|-------|
| Chair | Margaret Chen | CEO |
| Member | Rebecca Torres | CISO |
| Member | William Park | CFO |
| Member | Patricia Freeman | COO |
| Member | Helen Zhao | Chief Compliance Officer |
| Observer | David Harrington | CTO (non-voting observer) |

**Note:** The CTO attends SGC meetings as a non-voting observer. This structure was implemented in 2023 on the recommendation of the Board Risk Committee to enhance CISO independence. The CTO provides technical context when requested but does not vote on security policy decisions.

---

**Prepared by:** HR Operations
**Last Updated:** April 1, 2025
**Next Update Due:** April 2026
