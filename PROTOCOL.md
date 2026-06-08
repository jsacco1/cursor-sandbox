# Daily work protocol

This routine applies on days you work in this repo. It implements the habits described in [`VISION.md`](VISION.md).

## Start of session

1. Read [`logs/handoff.md`](logs/handoff.md) for yesterday’s brief and today’s plan (or say **start session** / **good morning** in Agent chat—the [end-of-day rule](.cursor/rules/end-of-day.mdc) will surface it).
2. Read [`VISION.md`](VISION.md) if you need a reset on purpose or principles.
3. Open [`ROADMAP.md`](ROADMAP.md) and pick one or two milestones marked **In progress** or **Planned** (handoff may already name one).
4. Optional: append a morning note to [`logs/decisions.md`](logs/decisions.md) under today’s date heading (what you chose and why).

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

Project rules still apply: [`.cursor/rules/lab.mdc`](.cursor/rules/lab.mdc) for `lab.txt`, [`.cursor/rules/python.mdc`](.cursor/rules/python.mdc) for Python files, [`.cursor/rules/end-of-day.mdc`](.cursor/rules/end-of-day.mdc) for end-of-day logging and handoff.

## Log during the day

Append entries as work happens; do not rewrite older sections except to fix mistakes.

| File | When to write |
|------|----------------|
| [`logs/decisions.md`](logs/decisions.md) | When you choose focus, scope, or approach |
| [`logs/actions.md`](logs/actions.md) | After meaningful steps (edits, runs, commits) |
| [`logs/learnings.md`](logs/learnings.md) | When something clicks or surprises you |
| [`logs/friction.md`](logs/friction.md) | When something blocks, slows, or derails you (technical, psychological, or emotional) |
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

Say **done for the day** (or **end of session**, **wrapping up**, **EOD**) in Agent chat. The [end-of-day rule](.cursor/rules/end-of-day.mdc) will:

1. Append your recap to all five log streams under today’s date (route decisions, actions, learnings, friction, reviews appropriately).
2. Overwrite [`logs/handoff.md`](logs/handoff.md) with a brief summary, tomorrow’s plan, first action, and open threads.
3. Update milestone **Status** in [`ROADMAP.md`](ROADMAP.md) if something moved forward or blocked.
4. Note `git status` in the handoff if not clean (commit only when you ask).

Record what you did in the same message, for example: focus/decisions, actions, learnings, friction (if any), done/blocked/tomorrow.

## Quick reference

```text
handoff (read) → VISION → ROADMAP (pick work) → Ask (plan) → OK → Agent → verify → commit
         ↓ during day ↓                                    ↓ EOD ↓
    decisions / actions / learnings / friction    5 logs + handoff + roadmap
```
