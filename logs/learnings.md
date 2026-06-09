<!-- Insights and "aha" moments. Append under ## YYYY-MM-DD and ### HH:MM headings; do not edit past entries except to fix errors. -->

## 2026-06-06

### 20:40 — Scoped turns beat bulk implementation
- Day-2 ran many steps in one Agent session; the turn-by-turn init (vision → protocol → roadmap → logs) kept each diff reviewable and matched User rules.

### 20:45 — Append-only logs
- One file per stream with date/time headings avoids directory sprawl while still separating learnings, decisions, actions, and reviews.

## 2026-06-08

### 23:17 — End of day
- Cursor/AI at 1 is the critical path—omics portfolio work should wait until PROTOCOL loops are automatic.
- Skill rubrics with observable behaviors beat gut-feel re-rating; re-rate only after two weeks of evidence.
- `handoff.md` + “start session” / “done for the day” turns planning into a repeatable bookend for each day.

### 23:26 — End of day (session 2)
- Planning belongs in repo docs (`docs/`) once shaped—not only in chat—so handoff and roadmap stay grounded.
- Closing with a commit clears cognitive load; tomorrow can start on R3 without git hygiene overhead.

## 2026-06-09

### 23:48 — R3 `greet.py`
- `if __name__ == "__main__"` runs `main()` only on direct execution, not import; `print` is what the user sees, while `main()` returns `None` to Python; `sys.argv[1]` needs a length check because missing args cause `IndexError`, not because `argparse` is required yet.

## 2026-06-10

### 00:58 — End of day
- Ask → OK → Agent → verify → commit → push is a complete sandbox loop; execution days feel different from planning-only days.
