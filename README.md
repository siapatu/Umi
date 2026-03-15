# Umi

_Bismillah._

Umi is currently in an early bootstrap phase. This repository intentionally starts small so the project direction, architecture, and contribution practices can be defined clearly from the beginning.

## Current Status

- ✅ Repository initialized
- ✅ Baseline documentation added
- ✅ Minimal bootstrap CLI scaffolded (`python umi.py`)
- ⏳ CI/testing pipeline not configured yet

## Getting Started

The runtime stack is still being evaluated, but a minimal Python CLI bootstrap is available now.

Run:

```bash
python umi.py
```

If you're joining as a new contributor:

1. Read [Project Structure](#project-structure).
2. Read [Contributing](CONTRIBUTING.md).
3. Read [Architecture Notes](docs/architecture.md).
4. Propose or help choose the first implementation stack.

## Project Structure

```text
.
├── README.md
├── CONTRIBUTING.md
├── umi.py
├── tests/
│   └── test_umi.py
└── docs/
    └── architecture.md
```

## Suggested Next Milestones

1. Choose a target stack (for example: TypeScript, Python, Go, or Rust).
2. Scaffold an executable baseline (CLI, API, or web app).
3. Add formatting, linting, and tests.
4. Add CI checks for pull requests.
5. Implement the first end-to-end vertical slice.

## Philosophy

- Keep changes small and reviewable.
- Document decisions early.
- Prefer simple defaults over premature optimization.

---

If you'd like, open an issue proposing the initial stack and app shape so we can scaffold the first working version.
