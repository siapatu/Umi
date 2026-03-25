# Codebase Review: Proposed Tasks

After reviewing the current bootstrap codebase, here are four targeted tasks (one per requested category).

## 1) Typo fix task
**Task:** Standardize `entrypoint` → `entry point` in CLI docstrings.

- **Issue found:** The `build_parser()` docstring uses "bootstrap entrypoint" while other places use "entry point".
- **Why this matters:** Consistent terminology improves readability and project polish.
- **Suggested fix:** Change `"Create the CLI argument parser for the bootstrap entrypoint."` to `"Create the CLI argument parser for the bootstrap entry point."`.
- **Acceptance criteria:**
  - CLI docstrings consistently use `entry point` terminology.

## 2) Bug fix task
**Task:** Preserve `SystemExit` semantics for non-integer exit codes in `main()`.

- **Issue found:** `main()` currently converts non-integer `SystemExit.code` values to `1`.
- **Why this matters:** If a caller raises `SystemExit("message")`, the message/semantic payload is lost instead of being propagated in a predictable way.
- **Suggested fix:** Keep current behavior for integer/`None`, and explicitly handle string/object payloads according to desired CLI policy (e.g., return a sentinel and print message or re-raise).
- **Acceptance criteria:**
  - Behavior is defined and covered for `SystemExit` with `None`, `int`, and `str` code values.
  - Regression tests enforce that policy.

## 3) Comment/documentation discrepancy task
**Task:** Update architecture docs to match the implemented stack.

- **Issue found:** `docs/architecture.md` says "There is no runtime architecture yet because the implementation stack has not been chosen," but the repository already ships a Python CLI runtime and tests.
- **Why this matters:** New contributors can be misled about project maturity and current technical direction.
- **Suggested fix:** Revise the "Current Architecture" section to describe the existing Python CLI bootstrap architecture and what remains undecided.
- **Acceptance criteria:**
  - Architecture document reflects current Python CLI structure.
  - Future/planned decisions are clearly separated from current state.

## 4) Test improvement task
**Task:** Remove global `sys.path` mutation side effects in `test_main_handles_systemexit_with_none_code`.

- **Issue found:** The test inserts into `sys.path` directly and does not restore it afterward.
- **Why this matters:** This can leak state across tests and cause order-dependent behavior.
- **Suggested fix:** Use pytest `monkeypatch` to modify/import paths safely, or ensure explicit cleanup/restoration of `sys.path`.
- **Acceptance criteria:**
  - Test no longer mutates interpreter-global state without cleanup.
  - Test behavior is stable regardless of execution order.
