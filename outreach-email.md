# Outreach Email

**Subject:** TrustBench: A compliance auditing benchmark for LLMs — seeking feedback on task design

---

Hi [Name],

I'm Varun Gurnaney. I built TrustBench, an open benchmark for evaluating LLMs on security compliance auditing. Your work on [SWE-bench / CyBench / CyberGym / AIReg-Bench] directly informed the design. I'd appreciate your feedback on the approach.

**The problem.** GRC teams are using LLMs for SOC 2 evidence review, gap analysis, and audit prep. Every compliance AI vendor claims automation. There's no standardized test to verify these claims. AIReg-Bench covers EU AI Act with 120 samples — nothing exists for SOC 2, ISO 27001, HIPAA, or PCI-DSS at the multi-document, multi-evidence-type level that real audits require.

**What I built.** 20 tasks across 8 SOC 2 controls at 5 difficulty levels. Each task gives the model synthetic audit evidence (policies, IAM configs, access logs, termination records, exception registers) with planted compliance gaps. D4-D5 tasks (75% of the benchmark) include red herrings with valid exceptions, noise documents, and materiality judgment calls. Scoring is keyword-based F1 — deterministic, no LLM-as-judge.

**Key findings from 120 runs (6 models x 20 tasks):**
- Sonnet 4.6 leads at 82%, Opus 4.7 at 72%, GPT-5.5 at 71%
- Three judgment tasks average below 28% — no model above 40%
- Recall is commodity; precision (not over-reporting) separates models
- F1 systematically penalizes thorough models that report legitimate extra findings — a known limitation I document in the paper
- Change management is easiest (88% avg). Vendor/risk judgment is hardest (24% avg)

**What I'd like feedback on:**
1. Is the task design sound? Do the D5 judgment tasks represent genuine compliance ambiguity?
2. Is keyword-based F1 the right scoring approach, given the over-reporting penalty issue?
3. What would make this useful to the research community?

Draft paper (IEEE format), leaderboard, and all code/tasks are at:
- Paper: https://github.com/varungurnaney/trustbench/blob/main/TrustBench_Paper.pdf
- Site: https://varungurnaney.github.io/trustbench/
- Repo: https://github.com/varungurnaney/trustbench

The schema is framework-agnostic — ISO 27001 and HIPAA task sets need only new task files, no harness changes. Looking for collaborators with audit experience to contribute tasks.

Thanks for your time.

Varun Gurnaney

---

## Who to send to

**Benchmark researchers:**
- Andy K. Zhang (Stanford CRFM) — CyBench lead. Email likely on his Stanford profile or the CyBench paper.
- Carlos E. Jimenez (Princeton) — SWE-bench lead. carlos_jimenez@princeton.edu (on paper).
- Zhun Wang (UC Berkeley SunBLAZE) — CyberGym lead. Email on the paper.
- Tom Sherborne (Cambridge) — AIReg-Bench. Email on the paper.

**GRC / compliance academics:**
- Search for professors publishing on "automated compliance," "GRC automation," "AI auditing" at business schools and CS departments. Key venues: USENIX Security, IEEE S&P, ACM CCS (for security compliance), and ISACA Journal (for practitioner audience).

**Industry:**
- Anthropic trust & safety / evals team — tag @AnthropicAI on X with the results, or email their research contact.
- OpenAI evals team — their models are benchmarked; they track external evals.
- Drata, Vanta, Secureframe — GRC platform companies who would want to benchmark their AI features against this.

## Customization per recipient

- For **Andy Zhang (CyBench):** "Your subtask decomposition pattern and first-solve-time difficulty calibration informed our D1-D5 design."
- For **Carlos Jimenez (SWE-bench):** "TrustBench follows SWE-bench's pattern of structured tasks with deterministic evaluation, adapted for compliance rather than code. The F1 scoring parallels your test-suite pass/fail approach."
- For **Zhun Wang (CyberGym):** "Your dual verification approach (crash vulnerable, not crash patched) inspired our red herring design — findings must be real gaps, not exceptions."
- For **Tom Sherborne (AIReg-Bench):** "TrustBench extends your work to multi-document evidence packages with technical configs, operational logs, and exception registers — the full audit evidence stack."
