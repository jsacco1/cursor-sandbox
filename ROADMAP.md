# Development roadmap

Planned work for this workspace, aligned with [`VISION.md`](VISION.md). Update **Status** and **Notes** as milestones move.

| ID | Phase | Milestone | Status | Depends on | Target | Notes |
|----|-------|-----------|--------|------------|--------|-------|
| R0 | Foundation | Cursor lab (Track D) | Done | — | — | `lab.txt`, project rules |
| R1 | Foundation | Mini Python (`greet.py`) | Done | R0 | — | Day-2 exercise complete |
| R2 | Operations | Daily protocol + logs | Done | R1 | — | `VISION.md`, `PROTOCOL.md`, `ROADMAP.md`, `logs/`, first log entries, README links |
| R3 | Learning | Day-3a: understand `greet.py` | Done | R1 | — | Ask mode; `main()`, `__name__`, `sys.argv` default |
| R4 | Feature | `argparse` CLI (`--name`) | Done | R3 | — | `--name` flag; verified default, `--help`, `--name Jamie` |
| R5 | Hygiene | GitHub remote + first push | Done | R2 | — | `origin` → github.com/jsacco1/cursor-sandbox; pushed `main` |
| R6 | Quality | One test for `greet.py` | Backlog | R4 | — | pytest when ready |

**Status values:** `Done` · `In progress` · `Planned` · `Backlog` · `Blocked`
