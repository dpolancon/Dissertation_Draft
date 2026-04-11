---
title: "Ch1 S3 — Critical Replication Studies on Shaikh's Cointegration"
type: section
chapter: 1
latex_source: Chapter1/Chapter1_CriticalReplication.tex
latex_label: sec:critical_replication
latex_section: "\\section{Critical Replication Studies on Shaikh's Approach to Cointegration}"
latex_lines: "L844–2525"
status: stub
scope: theoretical
assessment_grade: B
contribution: C2_critical_replication
keywords: [ARDL, VECM, bounds-test, specification-grid, overaccumulation]
tags: [ch1, replication, cointegration, Shaikh, ARDL, VECM]
---

# S3: Critical Replication Studies on Shaikh's Approach to Cointegration

## Section Architecture

The replication proceeds in four stages, each releasing one constraint maintained by the previous:

| Stage | Constraint released | Core question | Lines |
|-------|-------------------|---------------|-------|
| S3.1 | — | What is Shaikh's identification strategy? | L858–1069 |
| S3.2 | — | What data does the replication use? | L1070–1209 |
| **S0** | Fixed specification | Can the published result be reproduced? | L1210–1427 |
| **S1** | ARDL lag order | Is the ARDL(2,4) failure idiosyncratic? | L1428–1690 |
| **S2** | Single-equation | Is the long-run restriction a system property? | L1691–2283 |
| **S3** | Full sample | Is the identification temporally stable? | L2284–2404 |
| Discussion | — | Synthesis across stages | L2405–2419 |

## Section Opening (L844–857)

> **Source:** `Chapter1/Chapter1_CriticalReplication.tex:L844–857`

Section header and inline comment block setting notation conventions for the section:

- Shaikh derivation: `a, b, c, θ ≡ 1+c` (Shaikh's `d ≡ θ`)
- ARDL levels: `φ_i` (y lags), `ψ_j` (k lags), `c_0, c_1`, `δ_h` (dummies)
- ECM SR dynamics: `γ^y_i (Δy)`, `γ^k_j (Δk)`, `λ_y/λ_k` (levels)
- LR equation: `â, b̂, θ̂, d̂_h`

**Notes on notation:**

## Discussion Paragraph (L2410–2418)

> **Source:** `Chapter1/Chapter1_CriticalReplication.tex:L2410–2418`
>
> "Table~[S_closure] collects the evidence across the four replication studies. The architecture moves from procedural reproduction (S0) through specification sensitivity (S1) to system identification (S2) and temporal stability (S3), each stage releasing one constraint maintained by the previous and documenting its effect on θ̂ and the admissibility landscape."

**Argument:**  
**Key claim:**  
**Tables:** `Chapter1/tables/S_closure.tex`

## Subsection Notes

- [[ch1_S3_1_Shaikh_Identification]]
- [[ch1_S3_2_Data_Measurement]]
- [[ch1_S3_S0_Faithful_Replication]]
- [[ch1_S3_S1_ARDL_Specification]]
- [[ch1_S3_S2_VECM_Replication]]
- [[ch1_S3_S3_Temporal_Composition]]
- [[ch1_S3_Discussion]]

## Links
[[Ch1_Editorial_Assessment]]

- [[Chapter1_MOC]]
- [[cointegration]] · [[VECM]] · [[ARDL]] · [[bounds_test]]
- [[ObsidianVault/91_Concepts/capacity_utilization]] · [[transformation_elasticity]]
- [[critical_replication]] · [[Shaikh2016]] · [[Pesaran2001]]
