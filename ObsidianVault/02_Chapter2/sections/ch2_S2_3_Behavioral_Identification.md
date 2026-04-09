---
title: "Ch2 S2.3 — Causal Inference Strategy"
type: subsection
chapter: 2
latex_source: Chapter2/Chapter2_ProfitRate_Investment.tex
latex_label: subsec:causal_inference
latex_section: "\\subsection{Causal Inference Strategy}"
status: rewritten
scope: comparative
assessment_grade: B+
keywords: [process-tracing, causal-inference, small-N, comparative-historical, accounting-floor]
contribution: "Grounds the chapter's causal claims in Collier (2011) process tracing, Mahoney (2000) small-N causal inference, and Mahoney (2004) comparative-historical relational analysis — replacing the dropped ARDL Stage C with a methodologically stronger causal architecture that operates *on* the decomposition rather than alongside it"
tags: [ch2, causal-inference, process-tracing, comparative-historical, methodology]
updated: 2026-04-09
---

# S2.3: Causal Inference Strategy

## What This Section Does

The accounting decomposition identifies *which* channels moved the profit rate. This section establishes *why* — the institutional causal architecture of the Fordist settlement — using three complementary methods that operate on the decomposition as their outcome variable.

## Three-Method Architecture

### 1. Within-Case Process Tracing — Collier (2011)

Observable implications of demand-activation as containment mechanism:

- Single-channel contractions in functional period → concentrated in μ̂
- Multi-channel contractions including μ̂ → disproportionately deep
- 1966–70 → uniquely exhibits simultaneous multi-channel contraction with demand as dominant weight
- Temporal ordering and mechanism signatures provided by the decomposition

### 2. Cross-Case Small-N Causal Analysis — Mahoney (2000)

Tests whether structural conditions identified for US operate as **necessary conditions** in Chilean case:

- If BoP-binding is sufficient for transforming technological stagnation tendency into structural crisis → Chile should exhibit: mechanization trap → financial fragility → external crisis
- This escalation sequence must be present *independently* of the distributional channel
- The two cases are not parallel applications — they are a necessary-condition test

### 3. Comparative-Historical Relational Analysis — Mahoney (2004)

Places both cases within world-system articulation through Bretton Woods:

- Gold-dollar standard creates **asymmetric exposure** to P_Y/P_K shock
- US: one-sided (capital goods price compression only)
- Chile: two-sided (copper price collapse + dollar float simultaneously)
- The 1972–74 episode is one world-monetary event with structurally differentiated effects — NOT two instances of the same shock

## Accounting Floor Benchmark

The log-linearized accumulation identity is exact: ln g_K = ln χ + ln π + ln μ + ln B

When χ is constant → β_j = 1 for all j (unit elasticities = accounting floor, not behavioral claim). Every departure from unity = behavioral content attributable to institutional structure.

Nested restrictions (following Basu 2017):

- Robinson-Keynes: η_j = 0 for all j
- Bhaduri-Marglin type: η_3 = 0
- Foley-Michl (fully disaggregated): all β_j free

The comparative-historical method identifies which specification is consistent with observable implications in each case — NOT by estimating a stand-alone investment function.

## Decision Log Entry (2026-04-09)

ARDL Stage C dropped. Reason: did not carry causal weight (single-equation behavioral regression on N=26 cannot establish the institutional causality the chapter claims); created word-budget problem (advisor-friendliness). Causal work reassigned to process tracing + small-N comparative + comparative-historical relational. Accounting floor argument (β_j = 1 baseline) retained as methodological benchmark.

## Peripheral Twist (Cosmic Historian annotation, 2026-04-09)

The most important contribution of dropping Stage C is NOT the word budget — it is that the causal inference strategy now operates *symmetrically* across both cases. The ARDL was US-only (Chile was deferred indefinitely). Process tracing + Mahoney small-N + relational Mahoney can handle both cases from their *structural* positions:

- US: process tracing reads the decomposition chronologically through the functional/structural crisis distinction
- Chile: small-N necessary-condition logic tests whether BoP-binding converts technological stagnation into crisis independently
- Both: the relational world-monetary frame (Bretton Woods asymmetry) is the connection that makes them one study rather than two

This is a **periphery-first methodological redesign** — the causal architecture no longer treats Chile as the case that US ARDL applies to. Chile's structural position (BoP-constrained) now *generates* the causal test that the US case alone cannot provide.

## Cross-Chapter Handoff to Ch3

The causal inference strategy establishes:

- BoP constraint as necessary structural condition (Mahoney 2000 test)
- Bretton Woods asymmetric transmission as world-monetary articulation (Mahoney 2004 relational frame)
- These are EXACTLY the structural objects Ch3's leverage ratio formalizes

The K5 closer of both Stage B sections (US and Chile) explicitly names the unresolved object: "the direction of the institutional causality... is the object Chapter 3 must address." The causal inference strategy is the methodological bridge, not a closure.

## Links

- [[ch2_S2_Analytical_Framework]]
- [[ch2_S4_US_StageB_Profitability]]
- [[ch2_S4_Chile]]
- [[ch3_S3_2_BoP_Dynamics_Leverage]]
- [[BoP_constraint]]
- [[identification_boundary]]
- [[over_accumulation]]
