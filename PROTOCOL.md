# Daily work protocol

This routine applies on days you work in this repo. It implements the habits described in [`VISION.md`](VISION.md).

## Start of session

1. Read [`VISION.md`](VISION.md) if you need a reset on purpose or principles.
2. Open [`ROADMAP.md`](ROADMAP.md) and pick one or two milestones marked **In progress** or **Planned**.
3. Optional: append a morning note to [`logs/decisions.md`](logs/decisions.md) under today’s date heading (what you chose and why).

## Plan (Ask mode)

1. State the goal in one sentence.
2. Ask the agent for a **three-bullet plan** (or write your own).
3. Say **OK** before switching to Agent mode for edits.

Use `@` mentions (`@greet.py`, `@VISION.md`, etc.) so answers stay grounded in this repo.

## Execute (Agent mode)

1. **One logical change per turn** — one file or one behavior unless you explicitly override.
2. Review the diff before accepting.
3. **Verify** — run commands locally (e.g. `python3 greet.py`) and inspect `git diff`.
4. **Commit** when you are satisfied (the agent commits only when you ask).

Project rules still apply: [`.cursor/rules/lab.mdc`](.cursor/rules/lab.mdc) for `lab.txt`, [`.cursor/rules/python.mdc`](.cursor/rules/python.mdc) for Python files.

## Log during the day

Append entries as work happens; do not rewrite older sections except to fix mistakes.

| File | When to write |
|------|----------------|
| [`logs/decisions.md`](logs/decisions.md) | When you choose focus, scope, or approach |
| [`logs/actions.md`](logs/actions.md) | After meaningful steps (edits, runs, commits) |
| [`logs/learnings.md`](logs/learnings.md) | When something clicks or surprises you |
| [`logs/reviews.md`](logs/reviews.md) | End of session — done, blocked, tomorrow |

### Logging format

Each log file is **append-only**, with **one file per stream** (not one file per day).

```markdown
## YYYY-MM-DD

### HH:MM — optional short title
- Entry body (bullets or short paragraphs)

### HH:MM
- Another entry the same day

## YYYY-MM-DD
...
```

- **`## YYYY-MM-DD`** — day boundary (create this heading for the first entry that day).
- **`### HH:MM`** — time of entry (24-hour clock).
- **Append only** — add new sections at the bottom; preserve history.

## End of session

1. Append a short review to [`logs/reviews.md`](logs/reviews.md) under today’s date.
2. Update milestone **Status** in [`ROADMAP.md`](ROADMAP.md) if something moved forward or blocked.
3. Ensure `git status` is clean (or that you know what is left uncommitted).

## Quick reference

```text
VISION → ROADMAP (pick work) → Ask (plan) → OK → Agent (one change) → verify → commit
         ↓ during day ↓                              ↓ end ↓
    decisions / actions / learnings            reviews + roadmap update
```
