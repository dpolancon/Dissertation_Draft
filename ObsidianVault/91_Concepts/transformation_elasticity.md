---
title: Transformation Elasticity (θ)
type: concept
tags: [concept, technical-change, MPF, core]
appears_in: [ch1, ch2]
---

# Transformation Elasticity (θ)

## Definition
The elasticity of real capital productivity `Br` with respect to capital intensity `k = K/Yn`:

`θ = d ln(Br) / d ln(k)`

Equivalently: the slope of the Mechanization Possibility Frontier (MPF) in log space.

## Interpretation
- `θ = 1`: mechanization expands productive capacities exactly proportionally — no over-accumulation tendency
- `θ < 1`: each unit of deepening mechanization raises capital productivity less than proportionally — structural over-accumulation
- `θ > 1`: increasing returns to mechanization (unlikely in mature capitalism)

## Empirical Identification
θ is recovered from the cointegrating vector of the system:
`[ln(Br), ln(k)] ~ I(1)` with cointegrating rank r=1

The cointegrating vector `[1, -θ]` identifies the MPF slope.

## Role in the Dissertation
| Location | Use |
|---------|-----|
| [[ch1_S3_S1_ARDL_Specification]] | θ identified via ARDL specification geometry |
| [[ch2_S2_4_Structural_Identification_Theta]] | Central identification object |
| [[ch2_S4_US_StageA_MPF]] | θ estimated for US NFC sector (near but below 1) |
| [[ch2_App_Theta_Identification]] | Full technical appendix |

## Related Concepts
[[mechanization_possibility_frontier]] · [[over_accumulation]] · [[ObsidianVault/91_Concepts/capacity_utilization]] · [[capital_productivity]] · [[distributive_conflict]] · [[harrodian_knife_edge]] · [[wage_share_dynamics]] · [[regime_classification]] · [[ch2_S2_5_Peripheral_Extension]] · [[eq_theta_omega]] · [[eq_cl_theta]]

## Key References
[[Shaikh2016]] · [[ch1_S3_S2_VECM_Replication]] · [[ch2_S2_4_Structural_Identification_Theta]] · [[ch2_S4_US_StageA_MPF]] · [[ch2_S4_Chile]]
