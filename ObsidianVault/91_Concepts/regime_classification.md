---
title: Regime Classification (BoP Binding / Non-Binding)
type: concept
tags: [concept, Chile, BoP, TVECM, threshold, regime-switching]
appears_in: [ch2]
---

# Regime Classification: BoP Binding vs. Non-Binding

## Definition
A year-by-year classification of the Chilean economy's BoP constraint status, derived from the Threshold VECM (TVECM) Stage A estimation. Two regimes:

| Regime | Condition | Interpretation |
|--------|-----------|----------------|
| **Regime 1 — Non-binding** | ECT_m > γ̂ = −0.1394 | Import equilibrium; BoP constraint slack; normal adjustment speed |
| **Regime 2 — Binding** | ECT_m ≤ γ̂ = −0.1394 | BoP constrained; import overshooting; shadow price active; slow adjustment |

## Threshold Identification
The threshold γ̂ = −0.1394 is estimated from the CLS-TVECM (Stage A, Chile). It separates two adjustment regimes in the cointegrating relation for import propensity:

- **Regime 1 (non-binding):** `α_R1 = −0.091` — normal error-correction speed
- **Regime 2 (binding):** `α_R2 = −0.017` — 5.5× slower adjustment; shadow price of imports is strictly positive; BoP constraint binding

## BoP-Binding Years (1940–1978)
Years where ECT_m ≤ −0.1394:
1941–42, 1944–46, 1948–50, 1953, 1961–62, 1965–66, 1973–74

These cluster in: early ISI transitions, mid-ISI BoP crises, and the 1973–74 coup/stabilization shock.

## Shadow Price and Structural Suppression
In Regime 2, the BoP constraint imposes a shadow price on imported capital goods. This shadow price enters the effective profit share: `π_eff = π − λξφ`, reducing the profitability of mechanization. The result is structural suppression of θ_CL below its center-case value — chronic over-accumulation is the equilibrium state when BoP binding years dominate.

## Role in the Dissertation
The regime classification is the bridge between Stage A (structural identification) and Stage B (profitability decomposition). It:
1. Confirms the peripheral extension is empirically operative (Regime 2 recurs)
2. Periodizes the ISI arc by BoP tension episodes
3. Validates that θ_CL < 1 throughout is not an artifact but a structural condition

## Related Concepts
[[BoP_constraint]] · [[transformation_elasticity]] · [[over_accumulation]] · [[distributive_conflict]] · [[eq_cl_theta]] · [[Chile_Peripheral]] · [[structural_mediation]]

## Key References
[[ch2_S4_Chile]] · [[ch2_S2_5_Peripheral_Extension]] · [[ch2_App_Chile_CU_Estimation]] · [[FfrenchDavis2002]]
