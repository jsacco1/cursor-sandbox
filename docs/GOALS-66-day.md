# 66-day personal goals

Challenge framework: **shared system** (how) + **personal objectives** (what).  
**Baseline skills:** [`SKILL-BASELINE.md`](SKILL-BASELINE.md) · [`SKILL-RUBRICS.md`](SKILL-RUBRICS.md)  
**Domain context:** [`context/revmed-landscape.md`](context/revmed-landscape.md) · [`resources/oncology-omics.md`](resources/oncology-omics.md)  
**Daily execution:** [`PROTOCOL.md`](../PROTOCOL.md) · [`ROADMAP.md`](../ROADMAP.md)

---

## North star

By day 66, I run a daily **Cursor-centered development system** (Cursor/AI ≥2–3) and produce **one consultant-grade, oncology-relevant omics case study** plus **one decision-support artifact** framed the way preclinical leadership consumes evidence — while building habits that transfer to independent consulting long-term.

---

## Consulting wedge (deep, narrow)

**Reproducible QC + exploratory characterization of public RAS-mutant bulk RNA-seq cohorts** → portfolio case studies + composable workflow modules.

Indication starting point: **PDAC or LUAD** via TCGA/GDC (choose one in formulation before download).

---

## Survey alignment

| Survey signal | 66-day expression |
|---------------|-----------------|
| Genomic EDA | Public cohort RAS-mutant transcriptomics case study (P1) |
| Interoperable tools | QC/DE module with defined I/O + test (P2) |
| Deep narrow expertise | RAS-mutant bulk RNA-seq wedge — not tool tourism |
| Expert judgement / formulation | `decisions.md` formulation before analysis coding |
| Consultant transfer | Portfolio README + decision memo template |
| AI-resistant work | Interpretation, model selection, stratification rationale |

---

## Skill targets (Day 66)

| Skill | Baseline | Target | Primary vehicle |
|-------|----------|--------|-----------------|
| Coding | 3 | 3–4 | Narrow omics scripts |
| Git | 2 | 3 | R5 + bio repo history |
| Cursor | 1 | 3 | Sandbox → bio repo PROTOCOL loops |
| AI Tools | 1 | 3 | Formulation + omics sanity checks |
| Building Projects | 2 | 3 | P1 + P2 with definition of done |
| Debugging | 3 | 3–4 | R6 pytest + QC assertions |

**Critical path:** Cursor 1 + AI Tools 1 must reach 2–3 **before** heavy omics scope.

---

## Phase gates

| Gate | Requirement |
|------|-------------|
| No bio repo | Until 10+ sandbox PROTOCOL loops and R4 done |
| No P1 coding | Until formulation written and data subset staged |
| No P2 | Until P1 has reproduce + figures + interpretation memo |

---

## Phase plan

| Phase | Days | System | Domain |
|-------|------|--------|--------|
| **A — Calibrate** | 1–7 | Skill audit; `friction.md` | Bookmark resources in `oncology-omics.md` |
| **B — IDE boot** | 8–21 | R3–R5; daily PROTOCOL; Cursor 1→2 | No omics coding |
| **C — Engineering** | 22–28 | R6 pytest; atomic git commits | Formulate P1 in `decisions.md` |
| **D — Bio repo bridge** | 29–35 | Clone ops pattern to `oncology-omics-lab` | Stage GDC subset |
| **E — P1 execute** | 36–49 | Weekly friction review + 1 experiment | QC → DE → pathway → co-mutation |
| **F — Leadership artifact** | 50–56 | Verify + judgement logging | 1-page [decision memo](leadership-decision-support.md) |
| **G — P2 + consolidate** | 57–66 | Personal Development System doc | Wrapper module + test |

---

## Deliverables

### Sandbox (habit OS)

| ID | Milestone | Notes |
|----|-----------|-------|
| R3 | Understand `greet.py` (Ask only) | Cursor 1→2 |
| R4 | `argparse` CLI | One Agent turn |
| R5 | GitHub remote + push | Git 2→3 |
| R6 | One pytest | Debugging habit |

### P1 — Primary portfolio piece

**Example title:** *Transcriptional stratification of KRAS allele and co-mutation context in TCGA PDAC*

- **Deliverables:** script/notebook, QC report, 2–3 figures, interpretation memo, README
- **Leadership lens:** allele-specific biology vs pan-RAS strategy ([RevMed themes](leadership-decision-support.md#revmed-specific-high-value-themes-public-science))

### P2 — Interoperable utility

**Example:** `kras_cohort_qc` — inputs: expression + mutations + config; outputs: QC TSV + pass/fail; one pytest.

### P3 — Meta

- Personal Development System doc (what works, what failed, metrics)
- Consulting templates filled from P1

---

## Guardrails

- **One active repo** until day 30
- **Formulation before Agent** on analysis work (`decisions.md`)
- **Max one new tool/month** without client/program justification
- **Done** = reproduce + figures + interpretation (not "code runs")
- **Tool tourism:** log in `friction.md`; prefer finishing P1 over new stacks

---

## Weekly metrics

| Metric | Purpose |
|--------|---------|
| PROTOCOL loops completed | Habit |
| Formulation-before-code rate | Expert judgement |
| Friction entries | System improvement |
| QC checks per analysis | Debugging |
| Decision memos drafted | Leadership readiness |
| Biological judgement logged | AI-resistant skill growth |

---

## Out of scope (this challenge)

- NVC (parallel soft-skill track)
- Full Snakemake/Nextflow until P1 ships
- Unfocused tool learning without consulting transfer
