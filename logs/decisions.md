<!-- Choices and rationale. Append under ## YYYY-MM-DD and ### HH:MM headings; do not edit past entries except to fix errors. -->

## 2026-06-06

### 20:30 — Log layout
- Chose four append-only files (`learnings`, `decisions`, `actions`, `reviews`) with `## date` and `### time` headings instead of per-day files or subfolders.

### 20:35 — Initialization sequence
- Agreed to initialize workspace ops in scoped Agent turns: Turn 1 vision → Turn 2 protocol + logs → Turn 3 roadmap → Turn 4 first log entries.

## 2026-06-08

### 23:17 — End of day
- Added `friction.md` as fifth log stream; updated `VISION.md`, `PROTOCOL.md`, `README.md`.
- Saved skill baseline in `docs/SKILL-RUBRICS.md` (Coding 3, Git 2, Cursor 1, AI Tools 1, Building Projects 2, Debugging 3).
- Adopted end-of-day rule + `logs/handoff.md` to cut next-session startup friction.
- Deferred R3 (`greet.py` Ask exercise) to next session in favor of 66-day planning and ops hardening.

### 23:26 — End of day (session 2)
- Persisted domain planning to `docs/` (GOALS, oncology resources, RevMed landscape, leadership decision support).
- Created `docs/SKILL-BASELINE.md` with evidence-backed ratings.
- Committed all ops and docs (`4f159b7`); R3 still deferred to 2026-06-09.

## 2026-06-09

### 23:48 — R4 formulation (`argparse` CLI)
- **Question:** Replace manual `sys.argv` parsing with a small `argparse` CLI for `greet.py`.
- **Scope:** One optional flag `--name` (default `world`); keep `main()` entry point; same behavior as today for `python3 greet.py` and `python3 greet.py Jamie`.
- **Deliverable:** `greet.py` only; verify with both invocations; one Agent turn.
- **Out of scope:** R6 tests, new dependencies, refactoring beyond argparse.
- **Done when:** `python3 greet.py --help` works; default and `--name` match current output; `git diff` is reviewable.
