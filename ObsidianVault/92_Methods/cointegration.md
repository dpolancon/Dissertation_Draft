---
title: Cointegration
type: method
tags: [method, econometrics, time-series, core]
appears_in: [ch1, ch2]
---

# Cointegration

## Definition
Two or more I(1) series are cointegrated if a linear combination of them is I(0) — i.e., they share a common stochastic trend. The cointegrating vector identifies the long-run equilibrium relationship.

## Role in the Dissertation
| Location | Use |
|---------|-----|
| [[ch1_S3_S0_Faithful_Replication]] | Bounds test for cointegration between capital intensity and productivity |
| [[ch1_S3_S2_VECM_Replication]] | System-level cointegration rank test (Johansen trace/max-eigenvalue) |
| [[ch2_S4_US_StageA_MPF]] | MPF cointegration: `[ln(Br), ln(k)]` — identifies θ |
| [[ch2_S2_5_Peripheral_Extension]] | Two cointegrating vectors for Chile: capacity frontier + BoP equilibrium |

## Methods Used
- Bounds test (Pesaran 2001) — [[bounds_test]]
- Johansen VECM — [[VECM]]
- ARDL-ECM — [[ARDL]]

## Key References
[[Johansen1995]] · [[Pesaran2001]] · [[Engle1987]]
