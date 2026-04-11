---
title: Crosswalk Template — Section Note Standard
type: method
tags: [template, vault-protocol, crosswalk]
---

# Crosswalk Template — Section Note Standard

This file is the canonical template for all section and subsection notes in the vault. Copy and fill when upgrading a stub to a draft or complete note.

---

## Frontmatter Schema (complete)

```yaml
---
title: "Ch[N] S[X].[Y] — [Section Title]"
type: section                           # always "section"
chapter: [1|2|3]
latex_source: Chapter[N]/Chapter[N]_[Name].tex
latex_label: ch[N]:sec:[semantic_name]  # canonical label after audit
latex_section: "\\section{...}"         # exact LaTeX command
latex_lines: "L[start]–[end]"           # line range in source file
status: stub                            # stub | draft | complete | ready-to-deploy | deployed
scope: [theoretical|US|Chile|comparative]
tags: [ch[N], topic1, topic2]
---
```

**`scope:` vocabulary:**

| Value | When to use |
|-------|-------------|
| `theoretical` | No country-specific empirics (all of Ch1, Ch3 theory sections) |
| `US` | US Non-Financial Corporate Sector data/results |
| `Chile` | Chilean peripheral accumulation data/results |
| `comparative` | Cross-country comparison or world-system framing |

---

## Paragraph Crosswalk Block Template

Each prose paragraph in the LaTeX source gets a `## §P[N]` block. The block structure:

```markdown
## §P1 — [Short descriptive title of paragraph topic] (L[start]–[end])

> **Source:** `Chapter[N]/Chapter[N]_[Name].tex:L[start]–[end]`
>
> "[First sentence or key sentence of the paragraph verbatim or paraphrased.]"

**Argument:** [What is the logical role of this paragraph in the section's argument?]
**Key claim:** [The single most important factual or analytical claim made here.]
**Links:** [[concept_note_1]] · [[concept_note_2]] · [[method_note]]
```

**Rules:**
- `§P[N]` numbers are sequential within the section — do not skip
- The `> "[...]"` quote block is verbatim or near-verbatim from the LaTeX source
- `**Argument:**` answers: *why is this paragraph here?*
- `**Key claim:**` is the one thing a reader must retain from this paragraph
- `**Links:**` uses wikilinks only — no backtick file paths here

---

## Assets Block Template

Replace raw backtick file paths with wikilinks + canonical labels in the Assets block:

```markdown
## Assets

| Type | Vault ref | LaTeX label (canonical) | File |
|------|-----------|------------------------|------|
| figure | [[fig_[name]]] | `ch[N]:fig:[name]` | `Chapter[N]/figures/[name].pdf` |
| table  | [[tab_[name]]] | `ch[N]:tab:[name]` | `Chapter[N]/tables/[name].tex` |
| equation | [[eq_[name]]] | `ch[N]:eq:[name]` | (inline L[xxx]) |
```

**Rule:** Always use `[[wikilink]]` for vault cross-references. Never use bare backtick paths as the sole reference to an asset — backtick paths are fine *in addition to* the wikilink.

---

## Bottom Links Block Template

```markdown
## Links

- [[Chapter[N]_MOC]]
- [[ch[N]_S[parent_section]]] (parent)
- [[ch[N]_S[next_section]]] (sibling)
- [[concept_note]] · [[method_note]]
- [[cross_chapter_counterpart]] (if applicable)
```

---

## Status Progression

| Status | Condition |
|--------|-----------|
| `stub` | Frontmatter only, `## §P` blocks empty |
| `draft` | Some `§P` blocks filled, argument chains incomplete |
| `complete` | All `§P` blocks filled, assets block done, links populated |
| `ready-to-deploy` | Complete + `deploy_target` + `deploy_section` set in frontmatter |
| `deployed` | Written to LaTeX; note is now a mirror of the source |

**Never set `ready-to-deploy` on a note with `status: stub` or `status: draft`.**

---

## Example — Complete Section Note

```markdown
---
title: "Ch1 S3-S0 — Faithful Replication of the Capacity Benchmark"
type: section
chapter: 1
latex_source: Chapter1/Chapter1_CriticalReplication.tex
latex_label: ch1:subsec:S0_shaikh_replication
latex_section: "\\subsection{Stage S0: Faithful Replication of the Capacity Benchmark}"
latex_lines: "L1210–1427"
status: complete
scope: theoretical
tags: [ch1, replication, ARDL, bounds-test, S0]
---

# Ch1 S3-S0 — Faithful Replication of the Capacity Benchmark

## §P1 — The Replication Problem: Missing Documentation (L1213–1231)

> **Source:** `Chapter1/Chapter1_CriticalReplication.tex:L1213–1231`
>
> "This critical replication develops four replication studies..."

**Argument:** Establishes the replication problem: Shaikh's published result cannot be reproduced from documented inputs alone.
**Key claim:** The replicator must reconstruct the specification from indirect evidence.
**Links:** [[critical_replication]] · [[Shaikh2016]] · [[ARDL]]

## Assets

| Type | Vault ref | LaTeX label (canonical) | File |
|------|-----------|------------------------|------|
| table | [[tab_S0_table1]] | `ch1:tab:S0_table1` | `Chapter1/tables/S0_table1.tex` |
| table | [[tab_S0_table2]] | `ch1:tab:S0_table2` | `Chapter1/tables/S0_table2.tex` |
| figure | [[fig_S0_cu_fan]] | `ch1:fig:S0_cu_fan` | `Chapter1/figures/fig_S0_cu_fan.pdf` |

## Links

- [[Chapter1_MOC]]
- [[ch1_S3_Critical_Replication]] (parent)
- [[ch1_S3_S1_ARDL_Specification]] (sibling S1)
- [[ARDL]] · [[bounds_test]] · [[critical_replication]]
```

---

## Links

[[00_INDEX]] · [[DEPLOY_GUARDRAILS]]
