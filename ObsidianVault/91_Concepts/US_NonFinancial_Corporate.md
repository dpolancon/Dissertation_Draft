---
title: US Non-Financial Corporate Sector
type: concept
tags: [analytical-unit, US, NFC, profit-rate, Fordism]
appears_in: [ch2]
scope: US
---

# US Non-Financial Corporate Sector (NFC)

## Definition

The **US Non-Financial Corporate (NFC) sector** is the primary analytical unit for Chapters 1 and 2. It comprises all US corporations whose principal activity is non-financial production — manufacturing, mining, utilities, trade, and services — as classified by the Bureau of Economic Analysis (BEA) in the National Income and Product Accounts (NIPA).

BEA NIPA Table 1.14 provides the aggregate profit rate, output, and capital stock series for this sector. The BEA Fixed Assets Tables provide the capital stock disaggregated by asset type (structures vs. equipment), which is essential for the Weibull retirement distribution estimation in Stage A.

## Why this unit

The NFC sector is the appropriate unit for:

1. **Profit rate analysis (Ch2 Stage B):** Excludes financial sector profits (which reflect claims redistribution rather than value creation) and unincorporated business (which lacks clean capital stock measurement).

2. **Capacity utilization (Ch1):** Shaikh's original ARDL uses aggregate NFC output and capital; the replication maintains this boundary.

3. **Investment function (Ch2 Stage C):** Corporate investment is the macro-level decision variable that connects the profit rate to accumulation dynamics.

## Time span

The primary Fordist sample: **1947–1978** (peak-to-trough of the profit rate).
Extended sample for structural analysis: **1940–2024** (Table B3).

## Key series

| Variable | Source | Series |
|----------|--------|--------|
| Nominal profit rate r_t | BEA NIPA 1.14 | Corporate profits / current-cost net capital |
| Capital stock K_t | BEA Fixed Assets | Geometric/GPIM/Weibull |
| Output Y_t | BEA NIPA 1.14 | Corporate sector value added |
| Wage share ω_t | BEA NIPA 1.14 | Compensation / value added |
| Capacity utilization μ̂_t | Estimated via MPF | Stage A identification |

## Measurement controversies

- **Capital stock:** Straight-line vs. geometric vs. Weibull retirement — see [[ch2_App_Weibull_Retirement]] and the Weibull retirement appendix.
- **Profit rate numerator:** Pre-tax vs. post-tax; with or without IVA/CCA adjustments.
- **Sector boundary:** NFC vs. total corporate vs. total private — Shaikh uses NFC; this dissertation follows that choice.

## Contrast with Chilean case

The Chilean analytical unit is the **peripheral economy as a whole**, not a sector. See [[Chile_Peripheral]] for the contrast. The key structural difference: the Chilean MPF is BoP-constrained (import-dependent capital formation), whereas the US NFC sector faces no binding external constraint over the Fordist sample.

## Links

[[profit_rate]] · [[ObsidianVault/91_Concepts/capacity_utilization]] · [[transformation_elasticity]] · [[Fordism]] · [[Chile_Peripheral]]
[[ch2_S3_1_Data_US]] · [[ch2_S4_US_StageA_MPF]] · [[ch2_S4_US_StageB_Profitability]] · [[ch2_S4_US_StageC_Investment]]
