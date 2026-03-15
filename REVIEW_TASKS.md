# Codebase Review: Proposed Tasks

Given the current repository is in bootstrap mode, here are four concrete, prioritized tasks that map to the requested categories.

## 1) Typo fix task
**Task:** Clean up README text formatting typo/noise.

- **Issue found:** The README body currently has a trailing space (`"Bismillah "`).
- **Why this matters:** Tiny formatting defects create noisy diffs and look unpolished.
- **Suggested fix:** Remove trailing whitespace and normalize markdown formatting.
- **Acceptance criteria:**
  - No trailing whitespace in `README.md`.
  - `git diff --check` returns clean.

## 2) Bug fix task
**Task:** Keep the bootstrap CLI runnable as the codebase evolves.

- **Issue found:** If the minimal runnable entrypoint is removed or broken, contributors lose the only smoke path.
- **Why this matters:** A guaranteed run command prevents the repo from regressing into a non-runnable state.
- **Suggested fix:** Retain and validate a minimal executable command (`python umi.py`) and keep docs in sync.
- **Acceptance criteria:**
  - The documented command `python umi.py` exists and exits successfully.
  - A smoke test verifies this behavior on a fresh clone.

## 3) Documentation discrepancy task
**Task:** Align README with actual repository contents and intended scope.

- **Issue found:** README currently has only a title and a short phrase, which does not describe purpose, usage, or architecture.
- **Why this matters:** Documentation currently implies a project exists, but provides no actionable guidance.
- **Suggested fix:** Expand README sections: project purpose, setup, usage, development workflow, and roadmap.
- **Acceptance criteria:**
  - README includes: Overview, Getting Started, Usage, and Contributing sections.
  - Instructions are validated by a clean-room run-through.

## 4) Test improvement task
**Task:** Introduce baseline CI checks for content and style quality.

- **Issue found:** No tests/checks currently exist.
- **Why this matters:** Regressions in docs/config quality will go unnoticed.
- **Suggested fix:** Add lightweight checks such as markdown linting and/or a smoke test in CI.
- **Acceptance criteria:**
  - CI workflow runs on pull requests.
  - At least one automated check verifies repository health (e.g., markdown lint, formatting, or smoke command).
