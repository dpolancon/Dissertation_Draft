---
title: "Ch2 S4 — Stage C: Investment Function (US) — RETIRED"
type: subsection
chapter: 2
latex_source: Chapter2/Chapter2_ProfitRate_Investment.tex
latex_label: sssec:stageC_us
status: retired
scope: US
retired_date: 2026-04-09
retired_reason: "ARDL (~164 lines) dropped for advisor-friendliness and causal identification failure: N=26 regression cannot establish the institutional causality the chapter claims. Causal work reassigned to §2.3 Causal Inference Strategy (Collier 2011, Mahoney 2000, Mahoney 2004). The accounting floor argument (β_j=1 baseline, nested restrictions) is preserved in §2.3."
tags: [ch2, StageC, investment, ARDL, US, retired]
---

# Stage C: Investment Function — RETIRED (2026-04-09)

This section was removed from Chapter 2 on 2026-04-09.

## What was here

ARDL(1,2,1,1,1) long-run investment function for US Fordist period (N=26, 1948–1973). Key results that are now cited in Conclusion and §2.3 only:

- β̂_μ = +0.639 (p=0.002) — demand channel dominant long-run recapitalization signal
- β̂_{Py/PK} = −0.451 (p=0.031) — relative price channel significant
- β̂_{Br} = −0.089 (p=0.227) — technology channel not independently significant
- ECT = −0.374 — 37.4% disequilibrium correction per year; half-life 1.48 years
- Wald test: demand channel operates as independent signal over supply-side composite (t=3.895, p=0.001)

## Why it was dropped

1. **Causal identification failure** — ARDL tests behavioral departure from the accounting floor (β_j=1), not whether demand activation caused profitability outcomes or vice versa. The institutional causality the chapter claims requires process tracing, not regression.
2. **Asymmetric coverage** — Stage C was US-only; Chile was deferred indefinitely. Replacing with Mahoney (2000/2004) enables symmetric causal inference across both cases.
3. **Word budget** — ~164 lines removed; chapter length advisor-friendly.

## Where the intellectual content went

- Accounting floor argument (β_j=1 benchmark) → [[ch2_S2_3_Behavioral_Identification]] §Accounting Floor Benchmark
- Nested restriction hierarchy (Robinson-Keynes / Bhaduri-Marglin / Foley-Michl) → [[ch2_S2_3_Behavioral_Identification]]
- β̂_μ = +0.639 numerical anchor → preserved in Conclusion ¶2 as descriptive result only (not as causal claim)
- Causal architecture → [[ch2_S2_3_Behavioral_Identification]] Three-Method Architecture

## Links

- [[ch2_S2_3_Behavioral_Identification]] (successor)
- [[ch2_S4_US_StageB_Profitability]]
- [[identification_boundary]]
