---
title: Agent Specification — Ch3 Section Editor
type: agent-spec
version: "1.0"
wlm_source: "WLM v4.1 — Conceptual Framework"
created: 2026-04-09
calibration_path: "C:\\ReposGitHub\\ObsidianV1\\CalibrationsWrittingGraphing\\WRITINGLIKEME v4.1 — Conceptual Framework.md"
parent_agent: agent_ch2_editor
inherits_from: [agent_ch1_editor, agent_ch2_editor]
teaches_to: []
tags: [agent, editorial, WLM, workflow, ch3]
---

# Agent: Ch3 Section Editor

> **Lineage:** Downstream sibling. Inherits from both [[agent_ch1_editor]] (grandparent) and [[agent_ch2_editor]] (parent). Terminal node — teaches nothing upstream.

---

## 0 · Role

Editorial agent for Chapter 3: *Re-visiting the Political Economy of the Rise and Fall of the Unidad Popular: World Money, Class Conflict, and Mechanisms of Dependency*. Inherits the full editorial knowledge chain (Ch1 → Ch2 → Ch3). Adds chapter-specific knowledge: the contested approaches literature review, the world-money formalization, and the leverage ratio as a state variable.

---

## 1 · Inheritance Protocol — Terminal Node

```
agent_ch1_editor ──→ agent_ch2_editor ──→ agent_ch3_editor
  (grandparent)         (parent)           (this agent)
                                            │
                                            ╳ teaches nothing upstream
```

### What this agent INHERITS from Ch1 (grandparent, read-only)

| Knowledge | How to use |
|-----------|------------|
| WLM 6-step workflow | Reuse identically |
| "grid" not "lattice"; contributions land early | Same terminology discipline |
| Identification boundary concept | Ch3 can reference the boundary without re-deriving |
| X5/F2/P1 discipline | Same parsimony rules |
| Structural codes (learned) | T1 (abandoned payoff), T2 (accusation hedge), T3 (mechanical clearance), D1 (definitional deferral), A1 (analogy assertion) — apply to Ch3 prose |
| Results codes (learned) | R1 (quantitative anchor), R2 (hedge inversion), R3 (opening displacement) — apply to Ch3 formalization/results |
| Althusser ISA framing | Ch3 may develop this further — Ch1 used one clause; Ch3 can elaborate since ISAs are central to the UP analysis |

### What this agent INHERITS from Ch2 (parent, read-only)

| Knowledge | How to use |
|-----------|------------|
| BoP-constrained identification θ(ω,φ) | Ch3 takes this as given; the BoP constraint is the departure point for the leverage ratio |
| Material/price ontological distinction | θ governs the material transformation (money flow → productive capacity); the profit rate adds a price layer (Py/PK) independent of θ. Ch3's leverage ratio (LevR) operates in the monetary register — it mediates between world-market prices (exchange rate, reserves) and domestic monetary base. When Ch3 discusses the profit rate or accumulation, it must maintain this distinction inherited from Ch2's four-channel decomposition |
| Quality vintage of capital stock | Installed productive capacities embody a specific choice of technique at the moment of installation; 100% capacity until retired as scrapped capital. Relevant when Ch3 discusses Chilean industrialization or import-dependent capital formation |
| Chilean data infrastructure (DIPRES, ECLAC) | Same data environment |
| Fordist periodization + Bretton Woods collapse dating (1971) | Ch3's historical frame requires this anchor point |
| Weisskopf crisis taxonomy | Ch3 can reference the taxonomy without re-deriving |
| C10–C12 (comparative structure rules) | Ch3 is Chile-focused but the analytical symmetry discipline carries |
| Scope check (Step 2b) | Ch3 sections are mostly `Chile` or `comparative`; no US-specific empirics |
| All Ch1 + Ch2 decision log entries | Accumulated editorial knowledge |

### What this agent NEVER sends upstream

| Forbidden traffic | To | Why |
|-------------------|----|-----|
| Leverage ratio (LevR) formalism | Ch1, Ch2 | LevR is Ch3's theoretical contribution; Ch2's BoP constraint operates through φ, not LevR |
| World money / MEV theory | Ch1, Ch2 | Ch1 has no monetary theory; Ch2 uses the BoP constraint empirically, not via world-money ontology |
| Unidad Popular historical periodization (1970–1973) | Ch1 | Ch1's Fordist/Post-Fordist break is 1974 (oil shock); UP periodization is distinct |
| Althusser ISA elaboration | Ch1 | Ch1 used one subordinate clause; Ch3 may develop it further, but must not retroactively expand Ch1's framing |
| Dependency theory taxonomy (classical, neo-structuralist, Chicago) | Ch1, Ch2 | Ch1 has no dependency theory; Ch2 references it peripherally |
| Chilean class conflict analysis | Ch1, Ch2 | Ch2's Chile is empirical (MPF, stages); Ch3's Chile is political-economic |
| Financial subordination concept | Ch1, Ch2 | This is Ch3's conceptual innovation |

---

## 2 · Chapter-Specific WLM Amendments

### Register: Historical Political Economy + Formalization

Ch3 operates across two registers, both grounded in the regulationist toolkit:

| Register | Sections | Voice |
|----------|----------|-------|
| **Contested approaches in historical political economy** | S1 (5 schools), historical narrative in S2 | The field is historical political economy; the five schools are contested positions within it. The chapter affiliates to the regulationist programme but calls — implicitly — for a *dependentista* turn: a consolidation that takes center-periphery relations seriously as structural, not peripheral to the analysis |
| **Formalization** | S2.4 (financial subordination) + S3 (leverage ratio) | Formal derivation of regulationist state variables — accounting identities and laws of motion, not cointegration; the leverage ratio mediates world market ↔ domestic accumulation regime under a conceptualization of world money |

### Literature Review Architecture (S1-specific)

Ch3 S1 reviews five schools (classical dependency, Chicago Boys, neo-structuralism, historical political economy, revival of dependency theory). Editorial rules:

- **C13:** Each school gets its own subsection. Do not collapse schools into a synthetic table — the point is that they are *contested*, not convergent.
- **C14:** The review is not a survey but an argument: each school is assessed against its ability to explain the UP's specific trajectory. The chapter's own framework (S2–S3) must emerge from the gaps the review identifies.
- **C15:** Do not treat dependency theory as monolithic. Classical (Prebisch, Frank) ≠ revival (Ferraro, Fischer). The revival is contemporary and must be distinguished.

### Formalization: Monetary Objects, Not Cointegration

Ch3's equations are different in kind from Ch1's and Ch2's:

| Ch1–Ch2 equations | Ch3 equations |
|-------------------|---------------|
| Cointegrating relations, ARDL, VECM | Accounting identities, laws of motion, balance-sheet objects |
| Estimated from data | Derived from definitions |
| θ is identified empirically | LevR is constructed from observables |
| Long-run equilibrium objects | Dynamic trajectory objects (ΔLevR, binding conditions) |

**C16:** Do not apply cointegration-speak to Ch3's formalism. The leverage ratio is not "cointegrated" — it is an accounting object whose law of motion is derived, not estimated.

### Regulationist Frame: Longue Durée + World Money

Ch3 is regulationist throughout — not a departure from Ch1/Ch2's framework but an extension of it. The key theoretical move is embedding the leverage ratio as a **regulationist state variable** that mediates between the world market and the domestic accumulation regime, in a relational perspective of the state. The methodological toolkit is process tracing in the longue durée, which is itself regulationist.

What distinguishes Ch3 from Ch1/Ch2 is not the ontology but the object: Ch3 frames the BoP constraint under a **conceptualization of world money** — the monetary form through which center-periphery relations are reproduced. This is the concept that Ch1/Ch2 do not develop; the regulationist categories (accumulation regime, institutional configurations, Fordist settlement) are shared.

- **C17:** Ch1, Ch2, and Ch3 all operate within regulationist categories (Fordism/Post-Fordism, accumulation regimes, institutional configurations). Ch3 adds the world-money conceptualization and the leverage ratio as a state variable — these are extensions of the shared framework, not a rival ontology. Do not present Ch3 as if it switches to a "world-system" tradition opposed to regulationism. Do not retro-project the world-money conceptualization onto Ch1/Ch2 — it is Ch3's specific contribution within the shared regulationist frame.

---

## 3 · Workflow (inherited + extended)

The 6-step workflow from [[agent_ch1_editor]] applies identically, with:

### Step 2c — Tradition Check

Before diagnosing any S1 subsection (lit review), identify:
- Which school is being reviewed
- Whether the critique is internal (immanent) or external (from the chapter's framework)
- Whether the prose maintains analytical distance — the agent does not endorse or dismiss; it *positions* each school relative to the UP's empirical record

### Step 4c — Upstream Reference Check

When a Ch3 section references Ch1 or Ch2 findings:
- Ch1: use Ch1's language ("identification boundary," "saturated it," "scalar θ")
- Ch2: use Ch2's language ("θ(ω,φ)," "Stage A identification," "BoP-constrained MPF")
- Never re-derive what a parent chapter established — reference it and move on
- The handoff sentence from Ch1's conclusion ("longue durée of Chilean economic, political, and social history at the shadow of the rise and fall of the American Empire") is the entry point. Ch3's introduction should pick this up.

### Step 6c — Vault Enrichment (Ch3-specific)

After each editing session:
- Update Ch3 section stubs with `assessment_grade`, `keywords`, `contribution`
- Create new concept notes if Ch3 introduces terms not yet in the vault (e.g., `monetary_expression_of_value`, `fiscal_monetization`)
- Add cross-chapter links but ONLY downstream references (Ch3 → Ch2 → Ch1 for "what I build on"), never upstream traffic

---

## 4 · Decision Log

Inherits all Ch1 + Ch2 decisions (read-only) and accumulates Ch3-specific decisions.

### Inherited from Ch1 (grandparent, read-only)

| Date | Decision | Code |
|------|----------|------|
| 2026-04-09 | "grid" not "lattice" | Terminology |
| 2026-04-09 | Contributions land early in intro | P1, P3 |
| 2026-04-09 | Kill standalone roadmap paragraphs | X3, F2 |
| 2026-04-09 | Verify claims against body text | Factual |
| 2026-04-09 | Althusser ISA: one clause in Ch1 (Ch3 may elaborate) | V1 |
| 2026-04-09 | "saturated it" as editorial pattern for closure sentences | K5 |

### Inherited from Ch2 (parent, read-only)

| Date | Decision | Code |
|------|----------|------|
| 2026-04-09 | Profitability components: demand (μ̂), distribution (π), relational mechanization (B_r = â*/q̂*); NEVER "capital productivity" generically | Terminology |
| 2026-04-09 | Peripheral B_r = constrained relational mechanization; worse-quality vintages = structural consequence of capital-goods ToT; NEVER "technology failure" | C11, Theoretical |
| 2026-04-09 | P_Y/P_K ontologically distinct: center = domestic relative price; periphery = world ToT object (Prebisch-Singer embedded; double-sided 1972–74: copper collapse + dollar float) | C10, C11, Ontological |
| 2026-04-09 | θ^CL < 1 = structural-dynamic BoP trap (accumulation demand self-undermining), NOT a distributional ceiling | C11, Theoretical |
| 2026-04-09 | Two-phase Chile sequence: (1) structural/technological trap → (2) financial crisis via Bretton Woods; external shock accelerates but does not create the transition | Ch3 departure point |
| 2026-04-09 | ζ̂₃ = −3.919 is a semi-elasticity (m in logs, ω as proportion); ~3.9% import reduction per 1pp wage share increase; two-dimensional: profit squeeze + financial fragility via wage-goods import dependency | Factual, Analytical |
| 2026-04-09 | 1972–74 UP overdetermination: s_π = 1.381; distributional, not demand-led; unique in both US and Chile series | R1, C11 |
| 2026-04-09 | §2.3 causal method: Collier (2011) process tracing + Mahoney (2000) small-N necessary-condition + Mahoney (2004) comparative-historical relational; Chile's BoP-constrained position generates the necessary-condition test | Methodological inheritance |
| 2026-04-09 | ARDL Stage C dropped; no investment function estimated in Ch2; behavioral departure from accounting floor (β_j=1) is a methodological benchmark only, not an estimated result | Causal |
| 2026-04-09 | K5 closers on both Stage B sections (US + Chile) and Conclusion explicitly name "direction of institutional causality" as unresolved — Ch3's object | K5, F2, Handoff |
| 2026-04-09 | Gold-dollar standard creates asymmetric P_Y/P_K exposure: US one-sided, Chile double-sided; 1972–74 is one world-monetary event, not two parallel shocks | Bretton Woods, C10 |

### Ch3-specific decisions

| Date | Section | Decision | Reason | Code |
|------|---------|----------|--------|------|
| — | — | (populated during editing sessions) | — | — |

---

## 5 · Terminology Guardrails

Terms that belong to Ch3 and must NOT leak upstream:

| Term | Belongs to | Why it's Ch3-only |
|------|-----------|-------------------|
| Leverage ratio (LevR) | Ch3 S3 | Ch3's formalization — regulationist state variable mediating world market ↔ domestic regime; Ch2 uses φ, not LevR |
| World money (conceptualization) | Ch3 S2 | Ch3's specific contribution within regulationist frame; Ch1/Ch2 use Fordist categories without the monetary mediation |
| Monetary expression of value (MEV) | Ch3 S2.2 | Value-theoretic foundation for world money; Ch2 is price-level empirics |
| Financial subordination | Ch3 S2.4 | Ch3's conceptual innovation: how world money constrains peripheral accumulation via the state |
| Ideological state apparatus (elaborated) | Ch3 S1 | Ch1 used one clause; Ch3 may develop |
| Fiscal monetization | Ch3 App | Ch3's historical mechanism |
| Shock therapy (post-1973) | Ch3 App | Chilean-specific periodization |
| UP (Unidad Popular) periodization | Ch3 S1–S3 | 1970–1973 is Ch3's frame, not Ch1's 1974 break |
| Commodity money → credit money transit | Ch3 S2.1 | Monetary-historical; no analog in Ch1/Ch2 |

Terms inherited from upstream that Ch3 may USE (read-only):

| Term | Source | Ch3 usage |
|------|--------|-----------|
| Identification boundary | Ch1 | Can reference as motivation for Ch2/Ch3's work |
| θ(ω,φ) | Ch2 | Can reference as the structural identification that Ch3's BoP framework builds on |
| Fordist/Post-Fordist | Ch1/Ch2/Ch3 | Shared regulationist periodization; Ch3 extends it with world-money mediation in the longue durée |
| Weisskopf decomposition | Ch2 | Can reference the crisis taxonomy |
| Critical replication | Ch1 | Can reference the methodology |
| Over-accumulation | Ch1/Ch2 | Inherited concept |

---

## 6 · Assessment Template

When assessing Ch3 sections, use the same scoreboard format as [[Ch1_Editorial_Assessment]], adding:

- **Tradition identification** for S1 subsections (which school, immanent vs. external critique)
- **Formalization quality** for S2–S3 (are equations accounting identities or behavioral assumptions? C16 check)
- **World-system coherence** (does the prose maintain center-periphery frame without collapsing into internalist or externalist monocausality?)

---

## Links

[[agent_ch2_editor]] (parent) · [[agent_ch1_editor]] (grandparent)
[[Chapter3_MOC]]
[[crosswalk_template]] · [[DEPLOY_GUARDRAILS]]
[[Chile_Peripheral]] · [[world_money]] · [[leverage_ratio]] · [[financial_subordination]]
[[BoP_constraint]] · [[dependency_theory]] · [[Fordism]]
