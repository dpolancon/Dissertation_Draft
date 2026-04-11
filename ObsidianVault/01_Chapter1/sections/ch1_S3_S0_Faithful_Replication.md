---
title: "Ch1 S3-S0 — Faithful Replication of the Capacity Benchmark"
type: subsection
chapter: 1
latex_source: Chapter1/Chapter1_CriticalReplication.tex
latex_label_current: subsec:S0_shaikh_replication
latex_label_canonical: ch1:subsec:S0_shaikh_replication
latex_section: "\\subsection{Stage S0: Faithful Replication of the Capacity Benchmark}"
latex_lines: "L1210–1427"
status: stub
scope: theoretical
assessment_grade: B+
contribution: C2_critical_replication
priority: done
keywords: [bounds-test, PSS, deflator-opacity, wrong-test-statistic]
tags: [ch1, S0, replication, bounds-test, ARDL, deflator, theta]
---

# S3-S0: Faithful Replication of the Capacity Benchmark

## §P1 — The Replication Problem: Missing Documentation (L1213–1231)

> **Source:** `Chapter1/Chapter1_CriticalReplication.tex:L1213–1231`
>
> "This critical replication develops four replication studies, departing from Study S0, which subjects Shaikh's ARDL(2,4) to its first level of scrutiny: can his published coefficient table be recovered under current-release data, and under which variable combination within his own data environment? The exercise faces an immediate obstacle. Shaikh's Appendix 6.8 does not document which series correspond to the regression variables... An internal annotation in the Appendix 6.8 spreadsheet — visible in the worksheet metadata but not in the printed tables — states explicitly that the data underlying the capacity utilization measurement exercise is not documented."

**Argument:**

**Key claim:** The replicator must reconstruct the specification from indirect evidence — coefficient magnitudes, fit statistics, and the long-run multiplier denominator `(1 - Σγ̂_i)`.

**Links:** [[critical_replication]] · [[Shaikh2016]]

---

## §P2 — The Deflator Opacity (L1234–1248)

> **Source:** `Chapter1/Chapter1_CriticalReplication.tex:L1234–1248`
>
> "A further opacity concerns the deflator. Shaikh advocates a common-deflator rule throughout *Capitalism*: both output and capital are deflated by the same price index to preserve profit-rate consistency and eliminate the relative price channel... Yet his Appendix 6.8 workbook contains no output-side price deflator... A systematic search of all worksheets, including hidden rows and columns, confirms that the workbook provides only two candidate price indices: p^IG (implicit deflator of corporate gross investment) and p^KN (implicit deflator of the GPIM-adjusted net capital stock)."

**Argument:**

**Key claim:** The replication proceeds iteratively across all logically available combinations of output measure, capital stock concept, and deflator.

**Links:** [[Shaikh2016]] · [[ch1_App_Data_Shaikh]]

---

## §P3 — The Closest Match: Candidate C3 (L1250–1262)

> **Source:** `Chapter1/Chapter1_CriticalReplication.tex:L1250–1262`
>
> "The closest replication — candidate C3, using y_t = ln(GVAcorp_t / p^KN_t) and k_t = ln(K^G_t / p^KN_t) without a deterministic trend — matches Shaikh's two primary diagnostics within rounding: the long-run multiplier denominator 1 - Σγ̂_i = 0.096 against his published 0.095, and RMSE = 0.017 against his 0.016. More strikingly, the short-run capital-stock lag pattern — alternating in sign across L0 through L4 at magnitudes of the same order as Shaikh's (4.38, −11.75, 12.39, −6.35, 1.41) versus (5.09, −14.28, 15.71, −8.30, 1.85) — is reproduced structurally by no other candidate combination."

**Argument:**

**Key claim:** Structural match confirms Shaikh's implicit common deflator is p^KN — an internal GPIM construction, not an externally imported price series.

**Tables:** [[tab_S0_table1]] (`ch1:tab:S0_table1`)

**Links:** [[transformation_elasticity]] · [[Shaikh2016]]

---

## §P4 — Long-run Multipliers and Near-Unit-Root Boundary (L1274–1286)

> **Source:** `Chapter1/Chapter1_CriticalReplication.tex:L1274–1286`
>
> "Long-run multipliers reported in Panel B are estimated as ratios whose denominator, 1 - Σγ̂_i, is the complement of output's own long-run self-multiplier... at 1 - Σγ̂_i = 0.096 each period's output shock amplifies approximately tenfold before dissipating. Standard errors are computed via the delta method; the proximity of the denominator to zero places the system near the unit root boundary, making these standard errors conservative lower bounds on true long-run uncertainty. Under the replication, θ̂ = 0.720 is significant at the 1% level (t = 11.8)."

**Argument:**

**Key claim:** Near-zero denominator makes θ̂ point estimates structurally unstable — a problem S1 addresses by exhausting the admissible ARDL space.

**Links:** [[ARDL]] · [[transformation_elasticity]] · [[Pesaran2001]]

---

## §P5 — Residual Gap in θ̂: Two Sources (L1288–1302)

> **Source:** `Chapter1/Chapter1_CriticalReplication.tex:L1288–1302`
>
> "Despite the structural match, a residual gap in the point estimate of the long-run elasticity remains: θ̂ = 0.720 against Shaikh's published 0.661. Two sources account for this. First, Shaikh's workbook carries a corrected release of Appendix 6.8 that post-dates the original publication... Second, Shaikh does not report the canonical initial gross capital stock value K^G_1947; the replication uses 170.58 Bn, but any departure from Shaikh's undisclosed value propagates through the GPIM recursion into every subsequent period's capital stock."

**Argument:**

**Key claim:** The residual gap is data-vintage and undisclosed initial conditions — not specification error.

**Links:** [[ch1_App_Data_Shaikh]] · [[transformation_elasticity]]

---

## §P6 — Trend Exclusion (L1304–1317)

> **Source:** `Chapter1/Chapter1_CriticalReplication.tex:L1304–1317`
>
> "Shaikh does not discuss the exclusion of a trend term in Appendix 6.7, despite having introduced an autonomous component in his theoretical exposition of the capacity function. The reason for its absence is empirically transparent: across every deflator and capital-stock combination, the trend is either statistically insignificant or — when the deflator introduces its own secular path — produces catastrophic collinearity with ln K_t, collapsing θ̂ to negative values... The trend exclusion is therefore not an arbitrary design choice but a restriction enforced by the data under the correct variable specification."

**Argument:**

**Key claim:** Trend exclusion is data-enforced, not arbitrary — critical for [[ch1_S2_4_Accounting_Constraints]] admissible closure discussion.

**Links:** [[ARDL]] · [[bounds_test]]

---

## §P7 — Bounds Test Results: Partition by Case (L1332–1366)

> **Source:** `Chapter1/Chapter1_CriticalReplication.tex:L1332–1366`
>
> "The findings partition sharply by case, not by specification. Cases 2 and 3 fail for every specification at every conventional significance level... Case 1 — no intercept, no drift, the closure closest to the unbalanced growth formulation — is the only case where evidence of cointegration can be found. The AIC winner ARDL(3,3) produces the strongest F-bound statistic (F = 3.87 > I(1) = 3.34, p = 0.066); Shaikh's ARDL(2,4) follows marginally (F = 3.35 > I(1) = 3.33, p = 0.099)."

**Argument:**

**Key claim:** Cointegrating evidence survives **only** under Case 1 — the unbalanced growth closure. Case 2 (where Shaikh's normalization is internally coherent) finds nothing.

**Tables:** [[tab_S0_table2]] (`ch1:tab:S0_table2`)

**Links:** [[bounds_test]] · [[cointegration]] · [[over_accumulation]] · [[ch1_App_Accumulation_Dynamics_UG]]

---

## §P8 — Shaikh's Wrong Test Statistic (L1359–1366)

> **Source:** `Chapter1/Chapter1_CriticalReplication.tex:L1359–1366`
>
> "The F(10, 50) = 6257 statistic in Appendix Table 6.7.14 of Shaikh (2016) is the standard OLS goodness-of-fit test — the joint null that all coefficients are zero — not the PSS bounds test, which examines the 2-restriction null H_0: φ_1 = φ_2 = 0 on the lagged levels in the ECM reparameterization. Shaikh declares no PSS case and evaluates the wrong test statistic. The cointegrating evidence he claims has no valid inferential basis as reported."

**Argument:**

**Key claim:** Shaikh's reported bounds test is invalid — F(10,50)=6257 is the OLS omnibus F, not the PSS 2-restriction test. This is the central critical finding of S0.

**Links:** [[bounds_test]] · [[critical_replication]] · [[Pesaran2001]] · [[Shaikh2016]]

---

## §P9 — What S0 Establishes (L1391–1419)

> **Source:** `Chapter1/Chapter1_CriticalReplication.tex:L1391–1419`
>
> "The replication faces an immediate obstacle: Shaikh's Appendix 6.8 provides no variable definitions, no deflator specification, and no initial capital stock value... The closest variable combination (C3) recovers his two primary diagnostics within rounding. The trend is excluded by the data: across every variable combination a significant trend collapses θ̂ to negative values through collinearity with k_t... Admissibility fails on Shaikh's own terms. The F(10,50)=6257 he reports is the OLS goodness-of-fit statistic, not the PSS 2-restriction bounds test; he declares no deterministic case. Under proper bound testing, evidence of cointegration survives only under Case 1 (F = 3.35 > I(1) = 3.33; t = -2.51, p = 0.062)."
>
> "Three questions pass to the following replication study. (Q1) Is there any specification under an ARDL model that might solve Shaikh's caveats here documented? (Q2) Is the ARDL framework the adequate cointegration empirical strategy to deliver stable and robust estimations of the transformation elasticity? (Q3) Testing for the stability of parameters, interpreted as regime change of θ(Λ) → θ'(Λ') a plausible theoretical framework to steer an empirical strategy?"

**Argument:**

**Key claim:** S0 establishes the canonical base. Q1 → S1, Q2 → S2, Q3 → S3.

**Figures:** [[fig_S0_cu_fan]] (`ch1:fig:S0_cu_fan`)

**Links:** [[ch1_S3_S1_ARDL_Specification]] · [[ch1_S3_S2_VECM_Replication]] · [[ch1_S3_S3_Temporal_Composition]]

---

## Assets

| Type | Vault ref | LaTeX label (canonical) | File | Paragraph |
|------|-----------|------------------------|------|-----------|
| table | [[tab_S0_table1]] | `ch1:tab:S0_table1` | `Chapter1/tables/S0_table1.tex` | §P3 |
| table | [[tab_S0_table2]] | `ch1:tab:S0_table2` | `Chapter1/tables/S0_table2.tex` | §P7 |
| figure | [[fig_S0_cu_fan]] | `ch1:fig:S0_cu_fan` | `Chapter1/figures/fig_S0_cu_fan.pdf` | §P9 |

## Links
[[Ch1_Editorial_Assessment]]

- [[ch1_S3_Critical_Replication]]
- [[bounds_test]] · [[ARDL]] · [[cointegration]]
- [[ObsidianVault/91_Concepts/capacity_utilization]] · [[transformation_elasticity]] · [[over_accumulation]]
- [[critical_replication]] · [[Shaikh2016]] · [[Pesaran2001]]
- [[ch1_App_Data_Shaikh]] · [[ch1_App_Critical_Replication_Results]]
