# Workspace vision

## Purpose

This workspace exists to learn and practice a disciplined Cursor workflow—**Ask → scoped Agent → verify → commit**—in a small sandbox before applying the same habits to larger work.

The repo is a lab first and an operating system second: small, reviewable changes, explicit planning, and a written record of what was learned and decided.

## Principles

- **One logical change per Agent turn** — small diffs that are easy to review in `git diff`.
- **Plan in three bullets, wait for OK** — use Ask mode to align before Agent edits.
- **Prefer small diffs** — no drive-by refactors; match existing conventions in the repo.
- **Log what matters** — five append-only files under `logs/`, each organized by date and time headings:
  - `learnings.md` — insights and “aha” moments
  - `decisions.md` — choices and rationale
  - `actions.md` — what was done (runs, edits, commits)
  - `friction.md` — trouble, blockers, and resistance (technical, psychological, emotional)
  - `reviews.md` — end-of-session retrospectives
- **Roadmap driven by vision** — planned work lives in `ROADMAP.md` and should trace back to this document.
- **Track skill progress** — baseline and re-ratings use [`docs/SKILL-RUBRICS.md`](docs/SKILL-RUBRICS.md) (1–5 rubrics for coding, git, Cursor, AI tools, projects, debugging).

## Current phase

**Foundation complete** — Track D (modes, rules, scoped edits via `lab.txt`) and the day-2 mini Python exercise (`greet.py`) are done.

**Moving to Operations** — document the daily work protocol, initialize the development roadmap, and begin using the five log files on days you work in this repo.

## Success criteria

- A repeatable daily routine is documented in `PROTOCOL.md` and actually used.
- `ROADMAP.md` is maintained as a markdown table with clear status per milestone.
- On each work day in this repo, at least one entry is appended to `decisions`, `actions`, `learnings`, and `reviews` (under that day’s `## YYYY-MM-DD` heading); append to `friction` when something blocks or slows you.
- Agent sessions stay scoped: one file or one behavior per turn unless you explicitly override.

## Out of scope (for now)

- MCP servers, Automations, and Agent Skills
- `venv`, `requirements.txt`, and dependency-heavy Python setup
- GitHub remote and pull-request workflow — unless an active roadmap item says otherwise
- Large applications or frameworks — this remains a learning sandbox until the roadmap moves on
