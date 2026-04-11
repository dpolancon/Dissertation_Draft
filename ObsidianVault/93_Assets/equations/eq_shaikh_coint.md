---
type: asset
asset_type: equation
latex_label_current: eq:shaikh_coint
latex_label_canonical: ch1:eq:shaikh_coint
chapter: 1
scope: theoretical
used_in: [ch1_S3_1_Shaikh_Identification, ch1_S3_S0_Faithful_Replication]
status: stub
---

# Equation — Shaikh's Cointegrating Relation

**LaTeX label (canonical):** `ch1:eq:shaikh_coint`
**Form:** `log(y) = a + b·log(k) + θ·log(e)`

Where:
- `y` — output (or productive capacity)
- `k` — capital stock
- `e` — exploitation rate (proxy for reserve-army pressure)
- `θ` — transformation elasticity (the identification target)
- `a, b` — intercept and capital elasticity

## Economic interpretation

The cointegrating relation expresses the long-run equilibrium between output, capital, and the exploitation rate. The coefficient θ identifies the transformation elasticity: how output responds to changes in the rate of exploitation at the frontier of accumulation.

θ < 1 → over-accumulation (capital grows faster than output); θ > 1 → under-accumulation.

## Identification

θ is identified from the long-run multiplier recovered from the ARDL levels equation. The ARDL approach is valid when variables are I(1) or I(0), mixed; the bounds test (PSS 2001) tests for the existence of the cointegrating relation before interpreting θ.

## Notes

## Used in

[[ch1_S3_1_Shaikh_Identification]] · [[ch1_S3_S0_Faithful_Replication]] · [[transformation_elasticity]] · [[cointegration]]
