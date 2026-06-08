# Skill proficiency rubrics

Reference for the 66-day challenge. Re-rate only when **observable behaviors** at the new level hold for ~two consecutive weeks—not from feeling or hours logged.

**Context:** Ratings describe proficiency in the **challenge environment** (Cursor sandbox → bio repo), which may differ from your employer toolchain.

---

## Baseline (2026-06-08)

Full evidence and level-up gates: **[`SKILL-BASELINE.md`](SKILL-BASELINE.md)**

| Skill | Rating | Label | Notes |
|-------|--------|-------|-------|
| Coding | 3 | Competent | Confirmed |
| Git | 2 | Developing | Prior survey; re-confirm at Day 30 |
| Cursor | 1 | Beginner | Confirmed |
| AI Tools | 1 | Beginner | Confirmed |
| Debugging | 3 | Competent | Confirmed (revised up from 2) |
| Building Projects | 2 | Developing | Confirmed |

### Progress log

Maintained in [`SKILL-BASELINE.md`](SKILL-BASELINE.md#progress-log).

---

## Re-rating rules

1. **Upgrade** only when you can answer **Yes** to most behaviors at the new level for two consecutive weeks.
2. **Downgrade** honestly if habits slip—adjust goals, not guilt.
3. **Cursor / AI Tools** require logged loop completion and verification habits, not time in the IDE.
4. Record changes in the progress log above with a one-line evidence note.

---

## Coding

**What this measures:** Read, write, and reason about code to solve defined problems—independently of IDE, AI, git, or project structure. Primary language for this challenge: Python.

### 1 — Beginner

**Can:**
- Run scripts others provide with copy-paste instructions
- Edit obvious literals (strings, numbers, file paths)
- Recognize syntax errors when the interpreter points to a line

**Cannot yet:**
- Write a multi-step script from a blank file without heavy guidance
- Choose appropriate data structures for a non-trivial task
- Read unfamiliar code and predict what it does

**Evidence:** Needs step-by-step instructions; frequent syntax/runtime errors without understanding why.

### 2 — Developing

**Can:**
- Write short scripts (tens of lines) from a clear spec
- Use conditionals, loops, functions, and basic file I/O
- Follow a tutorial and adapt it with small modifications
- Read simple code and explain it line-by-line with effort

**Cannot yet:**
- Design a clean module structure without a template
- Handle edge cases consistently (empty input, missing files)
- Work confidently with unfamiliar standard-library or third-party APIs

**Evidence:** Completes exercises; struggles when the problem is vague or errors are opaque.

### 3 — Competent ← *baseline*

**Can:**
- Implement a defined feature in a familiar language without a tutorial
- Decompose a problem into functions or logical steps
- Use common patterns: parsing arguments, reading CSV/TSV, basic transforms, simple CLI
- Read others' code and identify the main flow; modify a specific behavior
- Reason about types, scope, and common error messages

**Cannot yet (reliably):**
- Architect a multi-module project from scratch
- Write robust production-grade error handling and APIs
- Optimize performance or memory without profiling guidance
- Onboard quickly to a large unfamiliar codebase

**Evidence:** Small scripts and familiar library work are reachable; bioinformatics-specific APIs may still need reference material.

**Level-up to 4:** Ship one end-to-end script (load → transform → output) with validation checks, clear functions, and a README—without AI writing the core logic.

### 4 — Proficient

**Can:**
- Design and implement a small project (multiple files) from a problem formulation
- Write readable, maintainable code others can follow
- Use tests or assertions to guard critical behavior
- Apply language idioms; refactor duplication when you see it
- Integrate libraries (e.g., pandas) from documentation

**Cannot yet (reliably):**
- Own a large production system solo
- Make deep performance/architecture tradeoffs without senior review

**Evidence:** Reproducible analysis scripts; reviews rarely find structural flaws.

### 5 — Advanced

**Can:**
- Architect solutions for ambiguous problems; choose patterns deliberately
- Write code that is testable, extensible, and documented by habit
- Debug subtle logic errors across modules without AI as crutch
- Mentor others; review code for design, not just bugs
- Adapt quickly to new domains/libraries with minimal ramp time

**Evidence:** Others trust your code in collaborative or client settings.

---

## Git

**What this measures:** Version control as a daily tool for tracking work, reviewing changes, recovering from mistakes, and collaborating—not merely having git installed.

### 1 — Beginner

**Can:** Clone a repo; possibly `add`/`commit` when reminded; recognize that git saves history.

**Cannot yet:** Interpret `status`/`diff` confidently; recover from bad edits without help; write meaningful commit messages.

### 2 — Developing ← *baseline*

**Can:**
- `git status`, `git diff`, `git add`, `git commit` for local work
- View history with `git log`
- Understand working tree vs. staged vs. committed at a basic level
- Make small commits when the workflow prompts you (e.g., PROTOCOL)

**Cannot yet (reliably):**
- Use branches for isolated work
- Resolve merge conflicts without stress
- Push/pull, open PRs, or collaborate smoothly on a shared repo
- Revert with confidence

**Evidence:** Local commits on one branch; remote workflow may be untried (R5).

**Level-up to 3:** R5 (remote + push); one commit per logical change for 2+ weeks; clean `git status` every session end.

### 3 — Competent

**Can:** Atomic commits; push/pull; simple branches; read `diff` before commit; revert a file or commit; connect history to roadmap milestones.

### 4 — Proficient

**Can:** Branch, merge, resolve routine conflicts; PRs; `stash`/cherry-pick/reset when appropriate; meaningful commit messages; tag releases.

### 5 — Advanced

**Can:** Design team workflow; recover from messy states (rebase, reflog); teach version control practices.

---

## Cursor (IDE + Agent workflow)

**What this measures:** Cursor as primary development environment—modes, `@` mentions, project rules, scoped Agent edits, diff review, and the Ask → plan → OK → Agent → verify → commit loop.

### 1 — Beginner ← *baseline*

**Can:**
- Open Cursor and edit files manually
- Run terminal commands in the IDE
- Complete guided exercises with explicit instructions

**Cannot yet (reliably):**
- Choose Ask vs. Agent vs. manual edit appropriately
- Use `@file` mentions to ground agent context
- Enforce one-change-per-turn discipline
- Review diffs before accept; recover when Agent over-scopes

**Evidence:** Cursor feels like an editor with chat; Agent sessions are unpredictable; high startup friction.

**Level-up to 2:** Complete R3–R4; run full PROTOCOL 10+ times; log friction; reduce time-to-first-action.

### 2 — Developing

**Can:** Start from README → PROTOCOL → ROADMAP; Ask for plans, Agent after OK; `@` mentions and rules; verify after edits; reject over-scoped diffs.

**Cannot yet (reliably):** Steer Agent consistently on multi-file repos; configure advanced features without guidance.

### 3 — Competent

**Can:** Full daily loop autonomously on two repos; scope Agent turns precisely; integrate logging rhythm; recover from bad Agent output.

### 4 — Proficient

**Can:** Apply workflow to domain repos (notebooks, scripts); decompose roadmap into Agent-sized turns; tune rules; measure friction metrics.

### 5 — Advanced

**Can:** Personalize environment for failure modes; teach workflow; balance speed and safety on client-grade repos.

**Distinction:** Cursor = environment + workflow. AI Tools = judgement, prompting, and verification while using model-assisted features.

---

## AI Tools

**What this measures:** Productive and safe use of AI-assisted development—formulation, context, verification, scepticism, and retaining expert judgement (especially important in bioinformatics, where plausible wrong answers are common).

### 1 — Beginner ← *baseline*

**Can:** Send prompts; receive suggestions; copy-paste code or explanations.

**Cannot yet (reliably):**
- Provide enough context for reliable answers
- Distinguish good suggestions from plausible wrong ones
- Verify outputs before accepting
- Use AI for planning separately from execution

**Evidence:** Accepts diffs unread, or avoids AI due to distrust—both are level-1 patterns.

**Level-up to 2:** Formulation before every Agent session; always verify; log one personal judgement call per session.

### 2 — Developing

**Can:** Prompts with goal, constraints, and file context; Ask for plan, Agent for scoped work; verify after suggestions; reject drift.

**Cannot yet (reliably):** Catch domain-specific errors; iterate efficiently; balance speed vs. learning.

### 3 — Competent

**Can:** Formulate before implementation; challenge assumptions; use AI for boilerplate, not core judgement; document when AI was wrong; own interpretation in deliverables.

### 4 — Proficient

**Can:** Structured prompting with edge cases and test criteria; red-team generated code; know when not to use AI; improve workflow via experiments.

### 5 — Advanced

**Can:** Teach responsible AI-assisted development; design team guardrails; adapt as tools change without losing discipline.

### Anti-patterns by level

| Rating | Typical anti-pattern |
|--------|----------------------|
| 1 | "Fix this" + stack trace only; accept full diff blindly |
| 2 | Good prompts but skips biological/statistical sanity checks |
| 3 | Catches code errors; still learning domain errors |
| 4 | AI generates; you validate data + science + code |
| 5 | Model-agnostic discipline; judgement is unmistakably yours |

---

## Building Projects

**What this measures:** Moving from "a script that runs" to a structured, maintainable, deliverable project—layout, documentation, roadmap, definition of done, and outcomes someone else can pick up cold.

### 1 — Beginner

**Can:** Work on single files in isolation; follow a course repo layout without understanding why.

**Cannot yet:** Initialize a purposeful repo; define milestones; know when a task is truly done.

### 2 — Developing ← *baseline*

**Can:**
- Work inside a structured repo (VISION, PROTOCOL, ROADMAP, logs)
- Complete pre-defined milestones (R0–R6)
- Append logs and update roadmap when reminded

**Cannot yet (reliably):**
- Bootstrap the same structure independently for a new repo
- Scope a multi-week project into milestones alone
- Deliver consultant-ready artifacts (repro doc + interpretation)

**Evidence:** Strong inside sandbox; new bio repo structure not yet proven solo.

**Level-up to 3:** Clone ops pattern to bio repo; every milestone has definition of done; README with run instructions before marking Done.

### 3 — Competent

**Can:** Bootstrap new repo with ops pattern; break portfolio work into milestones; minimal reproducible package; one primary active project.

### 4 — Proficient

**Can:** Consulting-shaped projects (intake → formulation → build → memo); templates; dependency hygiene; retrospect from friction data.

### 5 — Advanced

**Can:** Repeatable engagement system; scope under uncertainty; mentor others on project discipline.

### Definition of done (consulting-oriented)

| Component | Expected by rating |
|-----------|-------------------|
| Code runs | ≥ 2 |
| Reproduce steps in README | ≥ 3 |
| Data provenance documented | ≥ 3 |
| Validation / QC checks | ≥ 3 |
| Interpretation memo | ≥ 4 |
| Reusable template for next project | ≥ 4 |

---

## Debugging

**What this measures:** Diagnose failures (code, data, environment, logic); form hypotheses; test systematically; fix or document blockers—without random changes or immediate escalation.

### 1 — Beginner

**Can:** Recognize failure; retry or ask for help.

**Cannot yet:** Read stack traces; form hypotheses; use logging/debugger purposefully.

### 2 — Developing

**Can:** Read common Python errors; search/Ask with error text; fix typos, paths, obvious logic bugs; re-run after fixes.

**Cannot yet (reliably):** Debug multi-step pipelines; write minimal reproducers; separate code vs. data vs. spec bugs; use tests for regression.

### 3 — Competent ← *baseline*

**Can:**
- Systematic approach: reproduce → isolate → hypothesize → test → fix
- Use `git diff` to see what changed when something broke
- Add assertions or sanity checks (row counts, null rates, key uniqueness)
- Write at least one automated test for critical behavior when prompted
- Separate "code wrong" vs. "data unexpected" vs. "spec ambiguous"

**Cannot yet (reliably):**
- Debug opaque library internals or performance issues quickly
- Debug multi-tool pipelines without disciplined logging

**Evidence:** Script- and data-level debugging is methodical; genomic QC surprises are tractable with a process.

**Level-up to 4:** Habitual pytest; document root causes in `learnings.md`; prevent recurrence with tests/checklists.

### 4 — Proficient

**Can:** Debug across files and tools; logging and incremental validation in pipelines; useful postmortems; prevent recurrence.

### 5 — Advanced

**Can:** Debug under ambiguity (client data, partial specs); coach others; design systems where failures are localized and observable.

### Debugging loop (reference)

```text
1. Reproduce     — exact command, exact error
2. Localize      — which line / which pipeline step
3. Hypothesize   — one sentence: "I think X because Y"
4. Test          — smallest change or check to confirm/deny
5. Fix           — minimal fix; verify; commit
6. Record        — learnings.md or reviews.md if non-obvious
```

### Bioinformatics-specific checks (use at 3+)

| Check | Catches |
|-------|---------|
| Row/column dimensions after each transform | Silent joins, filters |
| Key uniqueness where expected | Duplicate sample IDs |
| NA rate per column | Parsing failures |
| Spot-check known genes/samples | ID mapping errors |
| Compare summary stats to published norms | Unit/scaling errors |

---

## Challenge targets by Day 66

| Skill | Baseline | Day 66 target | Primary vehicle |
|-------|----------|---------------|-----------------|
| Coding | 3 | 3–4 | Narrow omics scripts, not breadth |
| Git | 2 | 3 | R5 + atomic commits in bio repo |
| Cursor | 1 | 3 | Sandbox → bio repo PROTOCOL loops |
| AI Tools | 1 | 3 | Formulation + omics sanity checks |
| Building Projects | 2 | 3 | P1 case study + DoD |
| Debugging | 3 | 3–4 | R6 pytest + QC assertions habitual |
