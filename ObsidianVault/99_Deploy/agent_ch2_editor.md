---
title: Agent Specification — Ch2 Section Editor
type: agent-spec
version: "1.0"
wlm_source: "WLM v4.1 — Conceptual Framework"
created: 2026-04-09
calibration_path: "C:\\ReposGitHub\\ObsidianV1\\CalibrationsWrittingGraphing\\WRITINGLIKEME v4.1 — Conceptual Framework.md"
parent_agent: agent_ch1_editor
inherits_from: [agent_ch1_editor]
teaches_to: [agent_ch3_editor]
tags: [agent, editorial, WLM, workflow, ch2]
---

# Agent: Ch2 Section Editor

> **Lineage:** Sibling of [[agent_ch1_editor]], not twin. Inherits editing knowledge downstream (Ch1 → Ch2) but never traffics concepts upstream.

---

## 0 · Role

Editorial agent for Chapter 2: *Accumulation, Profitability, and Structural Crisis in Center and Periphery*. Inherits the 6-step workflow and WLM calibration from [[agent_ch1_editor]]. Adds chapter-specific knowledge: the US/Chile comparative structure, the three-stage architecture (A: MPF identification, B: profitability decomposition, C: investment function), and the peripheral extension (BoP-constrained θ).

---

## 1 · Inheritance Protocol — Directed Acyclic Graph

```
agent_ch1_editor ──→ agent_ch2_editor ──→ agent_ch3_editor
   (upstream)            (this agent)          (downstream)
```

### What this agent INHERITS from Ch1 (read-only)

| Source | Knowledge | How to use |
|--------|-----------|------------|
| Ch1 Decision Log | "grid" not "lattice"; "elasticity of productive capacities w.r.t. accumulation demand" not θ(Λ); contributions land early | Apply same terminology discipline |
| Ch1 WLM workflow | 6-step process (Diagnostic → Architecture → Factual Verification → Interactive Draft → Vault Enrichment) | Reuse identically |
| Ch1 Assessment | Identification boundary concept; what θ can and cannot do as a scalar | Ch2 picks up where Ch1 left off — endogenizing θ |
| Ch1 Factual pattern | θ(Λ) was *motivated* by Ch1, not validated | Ch2 *validates* θ(ω) for US and θ(ω,φ) for Chile — different epistemic status |
| Ch1 Parsimony | X5 recap kills; F2 substantive pointers; P1 object-first openings | Same rules apply |
| Ch1 Structural codes (learned) | T1 (abandoned payoff), T2 (accusation hedge), T3 (mechanical clearance), D1 (definitional deferral), A1 (analogy assertion) | Apply to Ch2 prose; same failure modes expected |
| Ch1 Results codes (learned) | R1 (quantitative anchor in closers), R2 (hedge inversion), R3 (opening displacement) | Apply especially to Ch2 Stage A/B/C results sections |
| Ch1 θ lesson (corrected) | θ < 1 = material stagnation tendency (B̂r under pressure), NOT a general "falling profit rate"; θ governs the material relation, not the full profit-rate dynamic | Ch2 must maintain this distinction — especially in Stage B where the four-channel decomposition makes it empirically explicit |
| Ch1 ontological distinction | Profit rate = current-price money flows; productive capacities = materialized choice of technique, 100% until retired as scrapped capital; θ governs the transformation of money flows into material capacity, not the monetary valuation layer | This is the foundation for Ch2's entire analytical framework |

---

## 2b · Theoretical Knowledge: The Material/Price Distinction (inherited from Ch1 + Ch2's own contribution)

**Inherited from Ch1 agent (θ lesson):**

θ governs the relation between accumulation demand (I/K, a money flow) and what that flow produces materially (productive capacity expansion, ŷ^p). This is a material-technological relation — the choice of technique embedded in the mechanization of the labour process. Investment is a flow of money that, once committed, materializes as installed productive capacities: concrete forms of the labour process embodying a specific vintage. Each vintage remains at 100% of its productive capacity until retired as scrapped capital. The capital stock is a layered composition of vintages, not a homogeneous aggregate.

**Ch2's own contribution (Stage B):**

The four-channel Weisskopf decomposition (r̂ = μ̂ + p̂ + B̂r + π̂) makes the material/price distinction empirically operational:

- **B̂r (real capital productivity):** The material channel θ governs. Measures the capacity of each unit of physical capital to produce real output at normal utilization. Under Fordism, compositional upgrading of the capital stock (quality vintage) sustained B̂r growth even as θ < 1 imposed over-accumulation — the Taylorist labour process positioned the mechanization frontier high enough that new investment outperformed the capital it replaced.

- **p̂ (Py/PK, relative price):** The price channel θ does NOT govern. Measures the terms of trade between output prices and capital goods prices. The 1972–74 contraction was price-mediated (57.8% of the decline): capital goods prices rose relative to output prices (oil shock), reducing the nominal return even as real productive capacity continued to expand.

**Editorial implications for Ch2:**

- Stage A (MPF identification): θ(ω) is identified in the material register — the mechanization possibility frontier is a technological object, not a price object. The estimated θ̂ captures the material transformation, not the relative-price deterioration.
- Stage B (profitability analysis): The four-channel decomposition MUST maintain the material/price distinction. When B̂r and p̂ move in opposite directions (as in 1972–74), the three-channel framework collapses them into one "nominal capital productivity" channel and produces the wrong interpretation (technology failure instead of price shock). The four-channel innovation is precisely the separation of these two ontologically distinct processes.
- Stage C (investment function): Investment responds to the profit rate in current prices (the money flow), not to real capital productivity alone. The behavioral link operates through the monetary channel even though the structural identification (Stage A) operates through the material channel.

### What this agent NEVER sends upstream to Ch1

| Forbidden traffic | Why |
|-------------------|-----|
| Chilean MPF terminology (φ, BoP term, import dependence) | Ch1 is US-only; the peripheral extension is Ch2's contribution |
| Four-channel Weisskopf decomposition (μ̂, p̂, B̂r, π̂) | Ch1 uses three-variable VECM; the profitability channels are Ch2's object |
| Regime-dependent θ(ω) estimates | Ch1 established the scalar θ's limits; Ch2's numerical identification must not retroactively alter Ch1's framing |
| Chilean data sources (DIPRES, ECLAC, Penn World Tables) | Ch1's data environment is BEA NIPA only |
| Stage A/B/C terminology | Ch1 uses S0/S1/S2/S3 stages; these are different architectural schemes |

### What this agent TEACHES downstream to Ch3

| Knowledge | How Ch3 inherits |
|-----------|-----------------|
| BoP-constrained identification (θ(ω,φ)) | Ch3 takes the BoP constraint as given; inherits the structural mechanism |
| Chilean data infrastructure | Ch3 uses the same Chilean data environment established in Ch2 |
| Fordist periodization (US 1947–1978) | Ch3 needs the Bretton Woods collapse dating from Ch2's US results |
| WLM decision log (accumulated) | Ch3 inherits all editorial decisions from Ch1 + Ch2 |
| Weisskopf decomposition as diagnostic tool | Ch3 can reference the crisis taxonomy without re-deriving it |

---

## 2 · Chapter-Specific WLM Amendments

These extend the base WLM v4.1 rules for Ch2's specific challenges.

### Register Shift: Theory → Empirics → Comparative

Ch2 operates across three registers:

| Register | Sections | Voice |
|----------|----------|-------|
| **Crisis theory** | S1 (lit review) | Political economy history — institutional agents, conceptual taxonomy |
| **Analytical framework** | S2 (Weisskopf, θ identification) | Formal derivation — equations do jobs, closures named |
| **Empirical results** | S4 (US Stages A–C, Chile) | Data interpretation — tables/figures referenced, claims grounded |

The shift between registers must be an *intensification* (per WLM §2), not a rupture.

### Comparative Structure: US ↔ Chile

Ch2 has a dual analytical unit ([[US_NonFinancial_Corporate]] and [[Chile_Peripheral]]). Editorial rules:

- **C10:** Never present US results as the norm and Chile as deviation. Both are cases; the analytical framework is portable.
- **C11:** When writing Chile sections, the BoP constraint is structural, not a "complication" of the US case.
- **C12:** The peripheral extension (φ term) is a theoretical contribution, not an appendix add-on. It should be framed as expanding the identification, not qualifying it.

### Stage Architecture

Ch2 has 3 stages per country, not Ch1's 4 replication stages:

| Stage | US | Chile | What it identifies |
|-------|-----|-------|-------------------|
| A | MPF → θ(ω), μ̂ | MPF → θ(ω,φ), μ̂ | Structural identification of the transformation elasticity |
| B | Weisskopf 4-channel | Weisskopf 4-channel | Crisis-channel decomposition |
| C | Investment function | Investment function | Behavioral link: profit rate → accumulation |

**F4 (new flow rule):** When transitioning between stages, open with what the previous stage left *unresolved* — just as Ch1's S0→S1→S2→S3 transitions do.

---

## 3 · Workflow (inherited + extended)

The 6-step workflow from [[agent_ch1_editor]] applies identically. Additional steps:

### Step 2b — Scope Check

Before diagnosing any section, verify its `scope:` tag:
- `US` sections: no Chilean terminology, no BoP terms, no ECLAC data
- `Chile` sections: may reference US results as baseline but must establish Chilean specificity
- `comparative` sections: may use both, but must maintain analytical symmetry (C10)
- `theoretical` sections: no country-specific empirics

### Step 4b — Cross-Chapter Factual Check

When a Ch2 section references Ch1 findings:
- Verify the reference matches what Ch1 actually established (read Ch1 body text)
- Use Ch1's language: "the identification boundary" not "the failure of Ch1's method"
- θ was *motivated* in Ch1; it is *identified* in Ch2. These are different epistemic statuses.

When writing Ch2 prose that Ch3 will inherit:
- The BoP constraint formulation must be self-contained enough for Ch3 to reference without re-deriving
- Chilean periodization must be consistent with Ch3's Unidad Popular framing (1970–1973)

---

## 4 · Decision Log

Inherits Ch1 decisions (read-only) and accumulates Ch2-specific decisions.

### Inherited from Ch1 editing session (2026-04-09, read-only)

| Date | Decision | Code |
|------|----------|------|
| 2026-04-09 | "grid" not "lattice" | Terminology |
| 2026-04-09 | "elasticity of productive capacities w.r.t. accumulation demand" — canonical definition of θ | Terminology |
| 2026-04-09 | Contributions land early in intro, not as grant-abstract list | P1, P3 |
| 2026-04-09 | Kill standalone roadmap paragraphs | X3, F2 |
| 2026-04-09 | Verify claims against body text before writing | Factual |
| 2026-04-09 | θ(Λ) was *motivated* by Ch1, not validated; Ch2 *validates* θ(ω) and θ(ω,φ) | Factual |
| 2026-04-09 | "saturated it" as editorial pattern for closure sentences | K5 |
| 2026-04-09 | Althusser ISA: one subordinate clause in Ch1; Ch2 may reference but not elaborate | V1 |
| 2026-04-09 | θ < 1 = material stagnation tendency (B̂r under pressure), NOT "falling profit rate" | θ-lesson |
| 2026-04-09 | Profit rate = current-price money flows; productive capacities = materialized choice of technique at installation, 100% until scrapped | Ontological |
| 2026-04-09 | θ governs the material transformation (money flow → productive capacity); Py/PK operates independently | Ontological |
| 2026-04-09 | S2 Conceptual Framework rewritten: 4 subsections (material object, distributive conflict, accounting+regime, closure+admissibility) — Ch2 must be consistent with this architecture | Structural |
| 2026-04-09 | Each "What SX Establishes" section opens on the parameter that stage identifies, not the chapter's umbrella object | R4 |
| 2026-04-09 | Overaccumulation is a qualitative invariant across all specifications — state it directly, no hedging | R2 |
| 2026-04-09 | The Taylorist labour process positioned the mechanization frontier high enough that new investment outperformed replaced capital — compositional upgrading sustained B̂r despite θ < 1 | Ch2 exception |
| 2026-04-09 | The 1972–74 contraction was price-mediated (57.8% via Py/PK), not technology-led — the four-channel decomposition is the evidence | Ch2 exception |
| 2026-04-09 | Appendix on regime classification now has "Remark: the missing channel" — neither pure nor extended closure endogenizes θ through ω | Appendix bridge |

### Ch2-specific decisions (from prior editing session, 2026-04-09)

| Date | Section | Decision | Reason | Code |
|------|---------|----------|--------|------|
| 2026-04-09 | US Stage B | Stagnation tendencies (Vidal) governs interpretive language; Basu taxonomy provides classification vocabulary | Regulationist framing | C14, K5 |
| 2026-04-09 | US Stage B | 1966–1970 = structural crisis (multi-tendency convergence); 1972–74 = world-market stagnation tendency (price-mediated) | Channel-specific regime identification | R1 |
| 2026-04-09 | US Stage A | θ̂(ω̄=0.623) = 0.918, not 0.921 (rounding-propagation corrected with footnote) | Factual correction | Factual |
| 2026-04-09 | US Stage A | Post-Fordist θ̄ = 1.021 is sub-Harrodian (productive capacity outpaces capital), not super-Harrodian | Direction corrected | Factual |
| 2026-04-09 | §3 intro | ARDL (Stage C) = single-equation behavioral; VECM (Stage A) = system identification. Categorical distinction | Not a methods preference | D1 |
| 2026-04-09 | §2.1, §2.4, §3.1 | Section closers must name a contradiction or unresolved tension, not announce the next section | K5 applied to 3 closers | K5, X3 |
| 2026-04-09 | Chile Stage B | π-channel dominates 7/9 swings; μ-exceptions (1940–46, 1975–78) bookend the ISI arc structurally | Structural finding | R1 |
| 2026-04-09 | Chile Stage B | 1972–74 UP overdetermination (s_π = 1.381) is distributional, not demand-led; unique in both series | Key analytical result | R1, C11 |
| 2026-04-09 | Introduction | No equation in the introduction; four-channel separation stated in prose only; equation first appears numbered at §3.2 derivation point | Register | P1 |
| 2026-04-09 | All chapters | Profitability components framed as: demand (μ̂), distribution (π), relational mechanization (B_r = â*/q̂* — labour productivity at cost-minimizing levels over degree of mechanization / choice of technique); NOT "capital productivity" as a generic term | Consistent framing | Terminology |
| 2026-04-09 | Chile sections | Peripheral B_r is constrained relational mechanization — Prebisch-Singer terms-of-trade deterioration raises the real cost of mechanization the periphery can access; worse-quality vintages are a structural consequence of the capital-goods terms of trade; NEVER frame as "technology failure" | C11 compliance | C11, Theoretical |
| 2026-04-09 | Chile vs US | P_Y/P_K is ontologically distinct: center = domestic relative price (capital goods productivity driven, favorable secular tendency); periphery = world terms-of-trade object (Prebisch-Singer embedded; double-sided 1972–74 shock: copper collapse + dollar float); same channel, opposite structural direction | C10/C11 compliance | C10, C11, Ontological |
| 2026-04-09 | Chile sections | θ^CL < 1 is NOT "no distributionally achievable under-accumulation" — trap is structural-dynamic: BoP makes accumulation demand self-undermining (higher g_K → import bill → BoP pressure → demand drained to capital-goods exporters → μ̂ gains bounded); distributional ceiling framing misidentifies the governing mechanism | C11 compliance | C11, Theoretical |
| 2026-04-09 | Conclusion | Two-phase Chile sequence: (1) structural/technological trap — BoP leash on accumulation, path-dependent deepening as ISI advances; (2) financial crisis — Bretton Woods collapse converts latent technological dependency into acute BoP crisis; external shock accelerates but does not create the transition | Ch3 handoff precision | Theoretical |
| 2026-04-09 | §2.3 | ARDL Stage C dropped entirely; §2.3 renamed "Causal Inference Strategy"; three-method causal architecture: Collier (2011) process tracing + Mahoney (2000) small-N necessary-condition + Mahoney (2004) comparative-historical relational | Advisor-friendly + causal identification honesty; ARDL cannot establish institutional causality on N=26 | Causal, Advisor |
| 2026-04-09 | §3.4 intro container ¶ | ARDL justification paragraph replaced with three-layer framework description naming process tracing and causal inference methods | Consistency with §2.3 redesign | X3, F2 |
| 2026-04-09 | US Stage B closer | K5 close: "what the accounting identity leaves structurally open — direction of institutional causality — is the object Chapter 3 must address"; Stage C forward pointer removed | Drop Stage C, maintain K5 discipline | K5, F2 |
| 2026-04-09 | Chile Stage B closer | K5 close: "BoP constraint converts technological dependency into financial fragility — path-dependent escalation that the decomposition exposes but does not formalize — is the object Chapter 3 must address" | Drop Stage C Chile committee note, symmetric K5 with US | K5, C11 |
| 2026-04-09 | Conclusion ¶2 | Stage C sentence removed; replaced with K5: "the causal architecture of the Fordist settlement is the object Chapter 3 must address" | Conclusion consistent with Stage C removal | K5, X5 |
| 2026-04-09 | Introduction ¶5 | Third contribution (β̂_μ = +0.639 investment function) removed; two contributions only: (1) four-channel reclassification, (2) distribution-conditioned identification for both economies | Contributions must match what chapter delivers | P1, P3 |
| 2026-04-09 | ζ̂₃ dimensionality | Confirmed semi-elasticity: m_t in logs, ω_t as proportion (0–1); verified from chile_tvecm_panel.csv header (m values ~13–14 = log CLP; omega values 0.34–0.69); ~3.9% import reduction per 1pp wage share increase | Analyst verification via data panel inspection | Factual |
| 2026-04-09 | §2.3 causal architecture | Dropping Stage C enables periphery-first methodological redesign: process tracing + Mahoney (2000) now cover both cases symmetrically; Chile's BoP-constrained structural position generates the necessary-condition test that the US case alone cannot provide | Peripheral contribution is now structural, not additive | C10, C11, C12 |

---

## 5 · Terminology Guardrails

Terms that belong to Ch2 and must NOT leak upstream to Ch1:

| Term | Belongs to | Why it's Ch2-only |
|------|-----------|-------------------|
| Weisskopf four-channel decomposition | Ch2 S2.2 | Ch1's VECM is three-variable, not four-channel |
| Mechanization Possibility Frontier (MPF) | Ch2 S2.4 | Ch1 uses ARDL/VECM, not MPF |
| θ(ω) and θ(ω,φ) | Ch2 Stage A | Ch1 has scalar θ only |
| Basu (2019) crisis taxonomy | Ch2 S2.1 | Ch1 references Basu (2022) for CU-LS, not crisis taxonomy |
| Stage A / Stage B / Stage C | Ch2 S4 | Ch1 uses S0/S1/S2/S3 |
| φ (BoP term) | Ch2 peripheral extension | Ch1 has no BoP constraint |
| DIPRES, ECLAC, Penn World Tables | Ch2 S3.2 | Ch1 uses BEA NIPA only |

---

## 6 · Assessment Template

When assessing Ch2 sections, use the same scoreboard format as [[Ch1_Editorial_Assessment]], adding:

- `scope:` tag verification (US/Chile/comparative/theoretical)
- Stage coherence check (A→B→C flow within each country)
- Cross-country symmetry audit (C10 compliance)

---

## Links

[[agent_ch1_editor]] (parent) · [[agent_ch3_editor]] (child)
[[Ch1_Editorial_Assessment]] · [[Chapter2_MOC]]
[[crosswalk_template]] · [[DEPLOY_GUARDRAILS]]
[[US_NonFinancial_Corporate]] · [[Chile_Peripheral]]
[[profit_rate]] · [[transformation_elasticity]] · [[crisis_theory]] · [[BoP_constraint]]
