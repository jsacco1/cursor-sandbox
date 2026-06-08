# Domain resources: oncology preclinical R&D

Transcriptomics and genomics references for a **computational biology IC** focused on biomarker discovery, model characterization, and translational hypotheses in **RAS-driven oncology**.

Related: [`../context/revmed-landscape.md`](../context/revmed-landscape.md) · [`../leadership-decision-support.md`](../leadership-decision-support.md) · [`../GOALS-66-day.md`](../GOALS-66-day.md)

---

## A. Foundational genomics & transcriptomics

| Resource | Why it matters |
|----------|----------------|
| [GDC Data Portal](https://portal.gdc.cancer.gov/) | TCGA / TARGET — bulk RNA-seq, mutations, clinical for public EDA practice |
| [cBioPortal](https://www.cbioportal.org/) | Rapid cohort exploration, co-mutation context (KRAS allele, STK11, TP53, etc.) |
| [DepMap Portal](https://depmap.org/) | Cell line dependencies, omics, drug sensitivity — preclinical model selection |
| [COSMIC](https://cancer.sanger.ac.uk/cosmic) | Mutation landscape, allele frequencies |
| [OncoKB](https://www.oncokb.org/) | Clinical actionability framing for variants |
| [MSigDB / GSEA](https://www.gsea-msigdb.org/) | Pathway-level interpretation (MAPK, EMT, immune signatures) |
| [ARCHS4](https://maayanlab.cloud/ARCHS4/) | Large compendium for signature exploration |

---

## B. RAS / MAPK oncology context (RevMed-adjacent)

| Resource | Why it matters |
|----------|----------------|
| [Nature 2024 — RMC-7977 / RAS(ON) multi-selective](https://www.nature.com/articles/s41586-024-07205-6) | Holderfield co-author; resistance, wt RAS, combination logic |
| [Cancer Discovery — RMC-6236 translational paper](https://ir.revmed.com/news-releases/news-release-details/revolution-medicines-announces-publication-on-the-discovery) | Discovery → clinic narrative template |
| [RevMed publications & AACR decks](https://www.revmed.com/news-and-publications/) | Preclinical combo rationale (e.g. RMC-6291 + RMC-6236 doublet) |
| [ClinicalTrials.gov — NCT05379985](https://clinicaltrials.gov/search?id=NCT05379985) | Daraxonrasib (RMC-6236) trial context for biomarker thinking |
| [ClinicalTrials.gov — NCT06128551](https://clinicaltrials.gov/search?id=NCT06128551) | RMC-6236 + RMC-6291 combination trial |

---

## C. Preclinical model & translational bioinformatics

| Resource | Why it matters |
|----------|----------------|
| [CrownBio](https://www.crownbio.com/) | Preclinical model selection, omics-stratified trials (industry framing) |
| [Mouse Genome Informatics](http://www.informatics.jax.org/) | Cross-species orthology when using murine models |
| [UCSC Xena](https://xenabrowser.net/) | Fast bulk expression + genomics integration |
| [GEO](https://www.ncbi.nlm.nih.gov/geo/) | Public pre/post-treatment expression datasets for signature practice |

---

## D. Workflow, reproducibility, and engineering (habit gap)

| Resource | Why it matters |
|----------|----------------|
| [`PROTOCOL.md`](../../PROTOCOL.md) + [`logs/`](../../logs/) | Habit OS — primary for Cursor/Git 1–2 |
| [Snakemake docs](https://snakemake.readthedocs.io/) | Defer until post-R6; industry-standard reproducibility |
| [Bioconductor workflows](https://www.bioconductor.org/packages/release/BiocViews.html#___Workflow) | RNA-seq QC → DE → pathway (domain muscle) |
| [nf-core/rnaseq](https://nf-co.re/rnaseq) | Reference pipeline conventions |
| [Open Targets Platform](https://www.platform.opentargets.org/) | Target–disease evidence for nomination discussions |

---

## E. Statistical / ML judgement (AI-resistant skills)

| Resource | Why it matters |
|----------|----------------|
| [Modern Statistics for Modern Biology](https://www.huber.embl.de/msmb/) (Holmes & Huber) | Solid stats intuition for omics |
| [ISLR](https://hastie.su.domains/ElemStatLearn/) / ESL (select chapters) | When ML is/isn't justified in small-*n* oncology |
| Papers on batch effects (ComBat, SVA) | #1 silent failure in transcriptomics |

---

## F. Communication & leadership surfacing

| Resource | Why it matters |
|----------|----------------|
| *Nonviolent Communication* (Rosenberg) — **parallel track** | Stakeholder communication; outside IDE challenge scope |
| [DACI decision framework](https://www.atlassian.com/team-playbook/plays/daci) | Clear recommendations for go/no-go meetings |
| [`leadership-decision-support.md`](../leadership-decision-support.md) | 1-page decision memo template; what leadership reads |
