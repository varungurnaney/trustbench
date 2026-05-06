# Contribute a Task to TrustBench

You don't need to write code. If you've written an audit finding, you can write a TrustBench task.

## What we need from you

Think of a real control failure you've seen in an audit — a gap that made it into a report. Now describe:

1. **What control was being tested?** (e.g., "SOC 2 CC6.1 — Logical Access" or "ISO 27001 A.9.2 — User Access Management")
2. **What evidence would an auditor review?** (e.g., "access control policy, IAM credential export, termination log")
3. **What was the gap?** (e.g., "terminated employee's access wasn't revoked for 7 days despite a 24-hour SLA")
4. **What made it tricky?** Was there an exception that partially covered it? Was it a judgment call? Did you have to cross-reference two documents to find it?

You can submit this as a GitHub issue using the template below, or email it to us. We'll turn it into a task with synthetic evidence — your real org's data stays private.

## The ask (copy-paste this into a GitHub issue)

```
### Control
[Framework and control ID, e.g., "SOC 2 CC6.1" or "ISO 27001 A.9.2.1"]

### Scenario (1-2 sentences)
[What's the audit scenario? e.g., "A company claims quarterly access reviews but the review log shows one system was reviewed 3 weeks late, and the reviewer was the same person who manages the system."]

### Evidence an auditor would review
- [Document 1, e.g., "Access control policy"]
- [Document 2, e.g., "Access review completion log"]
- [Document 3, e.g., "Employee role assignments"]

### The gap(s)
1. [Gap 1, e.g., "Review completed 3 weeks past the 15-business-day SLA"]
2. [Gap 2, e.g., "Reviewer is the same person who manages the system — self-review"]

### Is there a red herring? (optional)
[Something that looks like a gap but has a valid explanation, e.g., "One system shows no review, but it was decommissioned mid-quarter with documented CISO approval"]

### How hard is this? (pick one)
- [ ] Easy — the gap is obvious from reading one document
- [ ] Medium — you need to compare two documents to see it
- [ ] Hard — there's a red herring, noise, or a judgment call involved

### What would a good auditor say vs a bad one?
[e.g., "A good auditor would note the self-review as a segregation issue. A bad auditor would flag the decommissioned system as a missing review."]
```

## Test it yourself first

Before submitting, you can test whether an LLM would catch your scenario. Paste this prompt into ChatGPT or Claude along with your evidence:

```
You are a compliance auditor performing a SOC 2 Type II readiness assessment.

Control under review: [paste the control ID and description]

Evidence provided:

[Paste your policy document here]

---

[Paste your config/log/spreadsheet here]

---

[Paste any additional evidence here]

Instructions: Review all provided evidence and assess compliance with the control above. For each finding, provide:
1. A short title
2. Which section of the document it relates to
3. Why it's a gap (what's missing or insufficient)
4. Severity (Critical / High / Medium / Low)
```

If the model catches your gap — good, it's a valid task. If the model misses it — even better, it's a hard task.

## What we do with your submission

1. We create synthetic evidence documents based on your scenario (your real company data is never used)
2. We plant the gaps with detection keywords
3. We add it to the benchmark and run it against 6 models
4. You get credited in [CONTRIBUTORS.md](CONTRIBUTORS.md)

## Examples of good submissions

**Easy (D1):** "The change management policy says changes are deployed by the requesting engineer. That's a segregation of duties violation — anyone reading the policy should catch it."

**Medium (D3):** "The vendor management policy requires annual SOC 2 review for critical vendors. The vendor inventory shows a critical vendor whose SOC 2 report expired 4 months ago. You need to compare the policy against the vendor spreadsheet."

**Hard (D4-D5):** "A service account has a manually created key, which violates the workload identity policy. But the exception register has a CISO-approved exception with compensating controls. The exception is valid — but the compensating controls claim the key is rotated quarterly, and the key metadata shows it hasn't been rotated in 18 months. So the exception exists but the compensating controls aren't operating."
