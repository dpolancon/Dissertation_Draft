---
title: Bounds Test (Pesaran 2001)
type: method
tags: [method, econometrics, cointegration, bounds-test]
appears_in: [ch1]
---

# Bounds Test for Cointegration

## Definition
Pesaran, Shin, and Smith (2001) procedure for testing the null of no cointegration in an ARDL model, valid when regressors are I(0), I(1), or a mix. The F-statistic is compared to two bounds: I(0) lower bound and I(1) upper bound.

- F > I(1) upper bound → reject null of no cointegration
- F < I(0) lower bound → cannot reject null
- F in between → inconclusive

## Admissibility in Stage S0
A specification is *admissible* in the dissertation if:
1. The bounds test rejects the null (cointegration confirmed)
2. The cointegrating vector has correct theoretical signs
3. Residuals are white noise

## Key References
[[Pesaran2001]] · [[ch1_S3_S0_Faithful_Replication]] · [[ARDL]]
