---
title: Deploy Guardrails
type: reference
updated: 2026-04-08
---

# Deploy Guardrails — Vault → LaTeX

> **READ THIS BEFORE ANY DEPLOYMENT OPERATION.**

The vault accumulates knowledge in markdown. This folder governs how that knowledge flows **back into the LaTeX source files**. The guardrails exist because a deployment error can silently corrupt the LaTeX source, which is the ground truth for the dissertation.

---

## The One-Way Default

By default, the vault is **read-only with respect to LaTeX**. You write in the vault; the vault does not write to LaTeX. The LaTeX source is always the authoritative document.

```
LaTeX (ground truth) ──→ vault (accumulation layer)
vault ─────────────────→ LaTeX  ← REQUIRES EXPLICIT DEPLOYMENT
```

---

## When Deployment Is Appropriate

Deployment from vault to LaTeX makes sense only for:

1. **Prose additions** that have been drafted and finalized in the vault and need to appear in the dissertation
2. **Structural insertions** (new sections/subsections) agreed upon and ready for LaTeX
3. **Annotation carries** (e.g., a finding note that has become a paragraph in the argument)

**NEVER deploy**:
- Speculative notes or in-progress thinking
- Cross-links and wikilinks (these are vault-internal only)
- Frontmatter YAML (this is vault metadata, not LaTeX content)
- Table/figure notes that reference vault paths

---

## Deployment Eligibility

A vault note is eligible for deployment if and only if its frontmatter contains:

```yaml
status: ready-to-deploy
deploy_target: Chapter2/Chapter2_ProfitRate_Investment.tex
deploy_section: "\\subsubsection{Stage B: Profitability Analysis}"
```

A note with `status: stub`, `status: draft`, or `status: complete` is **NOT** eligible.

---

## Deployment Protocol (Manual)

1. **Set status** in the vault note's frontmatter: `status: ready-to-deploy`
2. **Identify the exact insertion point** in the LaTeX file (line number or section label)
3. **Run the deploy script** with explicit confirmation flag:
   ```bash
   cd ObsidianVault/99_Deploy
   python deploy_to_latex.py --note "../02_Chapter2/sections/ch2_S4_US_StageB_Profitability.md" --confirm
   ```
4. **Review the diff** output before the script writes anything
5. **Confirm** by typing `yes` when prompted
6. **Rebuild** the LaTeX document: `cd Consolidated && ./build.sh`
7. **Verify** the PDF renders correctly
8. **Commit** both the vault change and the LaTeX change together

---

## Deployment Script

See `deploy_to_latex.py` in this directory.

Features:
- Reads `deploy_target` and `deploy_section` from note frontmatter
- Strips frontmatter, wikilinks, and vault-internal metadata before writing
- Shows a unified diff before writing
- Requires `--confirm` flag (will not write without it)
- Creates a `.bak` backup of the target LaTeX file before writing
- Logs the operation to `deploy_log.jsonl`

---

## Status Vocabulary

| Status | Meaning |
|--------|---------|
| `stub` | Empty shell, frontmatter only |
| `draft` | Notes and ideas being developed |
| `complete` | Finished note, not yet staged for LaTeX |
| `ready-to-deploy` | Reviewed, finalized, deployment fields set |
| `deployed` | Successfully written to LaTeX; note is now a mirror |

---

## Cross-Reference: LaTeX Tag Structure

| Chapter | Body tag | Appendix tag | Source file |
|---------|----------|--------------|-------------|
| 1 | `%<*ch1body>` / `%</ch1body>` | `%<*ch1appendix>` | `Chapter1/Chapter1_CriticalReplication.tex` |
| 2 | `%<*ch2body>` / `%</ch2body>` | `%<*ch2appendix>` | `Chapter2/Chapter2_ProfitRate_Investment.tex` |
| 3 | `%<*ch3body>` / `%</ch3body>` | `%<*ch3appendix>` | `Chapter3/Chapter3_PEUP.tex` |

The consolidated document (`Consolidated/dissertation.tex`) fetches content between these tags via `\ExecuteMetaData`. **Do not modify the tags themselves.**
