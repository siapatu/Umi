# Codebase Review: Proposed Tasks

After reviewing the current bootstrap codebase, here are four targeted tasks (one per requested category).

## 1) Typo fix task
**Task:** Replace `entrypoint` with `entry point` in the top-level module docstring.

- **Issue found:** `umi.py` currently uses `"Umi bootstrap CLI entrypoint."`.
- **Why this matters:** Minor wording/typo issues in user-facing or maintainer-facing text reduce polish and consistency.
- **Suggested fix:** Update wording to `"Umi bootstrap CLI entry point."` (or standardize on one style across docs).
- **Acceptance criteria:**
  - The module docstring uses the agreed spelling/style consistently.
  - Any matching wording in docs is aligned.

## 2) Bug fix task
**Task:** Preserve non-integer `SystemExit` semantics in `main()`.

- **Issue found:** `main()` catches `SystemExit` and coerces all non-integer exit codes to `1`.
- **Why this matters:** If future CLI paths call `parser.exit(message=...)` or otherwise raise `SystemExit` with a string/object code, the current behavior drops that semantic information and always returns `1`.
- **Suggested fix:** Handle `None` as `0`, preserve integer codes, and consider surfacing message-like exit payloads predictably.
- **Acceptance criteria:**
  - `main()` preserves expected exit behavior for integer, `None`, and message-like `SystemExit.code` values.
  - Regression tests cover these cases.

## 3) Comment/documentation discrepancy task
**Task:** Reconcile project-status messaging in `README.md` with the actual repository state.

- **Issue found:** README says the CI/testing pipeline is not configured yet, while the repo already contains executable tests (`tests/test_umi.py`).
- **Why this matters:** New contributors can be misled about current maturity and available validation steps.
- **Suggested fix:** Reword status to distinguish between "tests exist" and "CI not yet configured".
- **Acceptance criteria:**
  - README status section accurately reflects current test availability.
  - Getting Started includes the current local test command.

## 4) Test improvement task
**Task:** Make CLI subprocess tests robust to invocation directory.

- **Issue found:** Tests invoke `python umi.py` via a relative script path, which can fail when pytest is run from a different working directory.
- **Why this matters:** Test reliability should not depend on where pytest is launched.
- **Suggested fix:** Resolve script path via `Path(__file__).resolve().parents[1] / "umi.py"` (or invoke module form where appropriate).
- **Acceptance criteria:**
  - Tests pass when invoked from repo root and from another cwd.
  - No hardcoded relative-path assumption remains in CLI subprocess tests.
