---
title: ARDL (Autoregressive Distributed Lag Model)
type: method
tags: [method, econometrics, ARDL, bounds-test]
appears_in: [ch1, ch2]
---

# ARDL — Autoregressive Distributed Lag Model

## Definition
A single-equation time-series model that includes lags of both the dependent variable and the regressors. Used for bounds-test cointegration and for estimating investment functions.

## Uses in the Dissertation
| Location | Application |
|---------|------------|
| [[ch1_S3_S0_Faithful_Replication]] | Pesaran bounds test in ARDL form — S0 faithful replication |
| [[ch1_S3_S1_ARDL_Specification]] | S1: Specification geometry — global frontier of admissible ARDL specs |
| [[ch2_S4_US_StageC_Investment]] | Investment function estimation (Stage C) |

## Specification Geometry (S1)
The S1 stage maps the full information criterion (AIC/BIC) surface across all (p, q) lag combinations — the "global frontier" of admissible specifications. The focal specification minimizes IC subject to admissibility constraints.

## Key References
[[Pesaran2001]] · [[Natsiopoulos2024]] · [[AhnReinsel1988]]
