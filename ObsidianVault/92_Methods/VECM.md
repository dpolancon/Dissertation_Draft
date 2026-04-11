---
title: VECM (Vector Error Correction Model)
type: method
tags: [method, econometrics, VECM, cointegration]
appears_in: [ch1, ch2]
---

# VECM — Vector Error Correction Model

## Definition
A VAR model in differences augmented with error correction terms (ECTs) that capture the long-run cointegrating relationships. Each ECT represents adjustment speed toward one cointegrating equilibrium.

## Identification in the Dissertation
- **Rank r**: determined by Johansen trace/max-eigenvalue tests
- **Admissibility**: cointegrating vector must satisfy theoretical sign restrictions (e.g., negative loading on excess capacity)
- **Over-identification**: restriction tests (LR tests on β) verify structural interpretation

## Key Diagnostic Tests
- Osterwald-Lenum (1992) critical values for rank
- Hansen-Johansen (1999) parameter constancy (used in S3)
- Bootstrap LR tests (Cavaliere 2015, 2018) — needed for heteroskedastic residuals

## Role in the Dissertation
- [[ch1_S3_S2_VECM_Replication]] — System-level VECM for Shaikh's CU identification
- [[ch2_S4_US_StageA_MPF]] — MPF cointegration system
- [[ch2_S2_5_Peripheral_Extension]] — Threshold VECM for Chile's BoP regime switch

## Key References
[[Johansen1995]] · [[Johansen1991]] · [[HansenJohansen1999]] · [[Cavaliere2015]] · [[Cavaliere2018]]
