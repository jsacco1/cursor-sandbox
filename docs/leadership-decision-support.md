# Leadership decision support (comp bio IC)

As an **individual contributor**, you rarely own portfolio decisions — you **enable** them with evidence packages leadership can act on. Frame projects as **decision-support artifacts**.

Related: [`context/revmed-landscape.md`](context/revmed-landscape.md) · [`GOALS-66-day.md`](GOALS-66-day.md) · [`resources/oncology-omics.md`](resources/oncology-omics.md)

---

## Decision types you can feed

| Decision type | Comp bio contribution | Example deliverable |
|---------------|----------------------|---------------------|
| **Biomarker hypothesis** | Response / resistance signature | Ranked gene set + validation in holdout models |
| **Candidate discovery support** | Target/pathway dependency evidence | DepMap + omics integration memo |
| **Candidate nomination** | Translational package for lead series | Model selection rationale + PD biomarker proposal |
| **Go / no-go (preclinical)** | Clear kill/continue criteria | Pre-specified criteria + outcome dashboard |
| **Patient stratification** | Who benefits from allele X vs doublet Y | Co-mutation / expression strata with effect sizes |
| **Combination rationale** | Why doublet beats mono | Pathway reactivation analysis (RTK, wt RAS) |
| **Model selection** | Which PDX/cell line represents clinic | Concordance of expression + mutation profile |
| **Indication prioritization** | Tumor type sensitivity ranking | Cross-indication EDA of public + internal summaries |
| **Tox / tolerability hypothesis** | On-target pathway suppression in normal tissue proxies | Expression of target pathway in GTEx / normal panels |
| **Trial design input** | Enrichment biomarker feasibility | Prevalence + assayability + effect size simulation |

---

## RevMed-specific high-value themes (public science)

1. **Why RAS(ON) multi-selective vs mutant-selective** for a given tumor context
2. **Doublet benefit** (e.g. G12C-selective + multi-selective) — durability, apoptosis, resistance prevention
3. **Adaptive resistance** — RTK upregulation, secondary RAS mutations, wt RAS signaling
4. **TME modulation** — immune infiltration + transcriptomic pathway shifts post-treatment
5. **Allele-specific positioning** — G12D vs G12C vs pan-RAS in PDAC / NSCLC / CRC

---

## 1-page decision memo template

Use for portfolio discussions and as a **66-day practice artifact** (even on public data).

```markdown
# Decision memo (1 page max)

## Decision needed
[e.g. Is co-mutation X a plausible enrichment biomarker for hypothesis Y?]

## Context
[Program, indication, 3 bullets]

## Evidence summary
[Figure refs + effect sizes; what we did NOT find]

## Recommendation
[Go / no-go / needs experiment Z]

## Risks & uncertainties
[Batch, n, model transfer]

## Proposed next experiment
[One experiment only]
```

**Audience cues (POIs):**

- **Pete Wilds (Cancer Biology):** mechanistic rigor, assayable biology, inhibitor + companion logic
- **Matt Holderfield (Systems Biology):** pathway depth/durability, model systems, combination data integration
