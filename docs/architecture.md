# Architecture Notes

This document captures architecture direction while Umi is in bootstrap mode.

## Current Architecture

There is no runtime architecture yet because the implementation stack has not been chosen.

## Decision Areas

Before scaffolding code, align on the following:

1. **Primary runtime**
   - Options: Node.js/TypeScript, Python, Go, Rust, etc.
2. **Application shape**
   - CLI, web API, web app, library, or hybrid.
3. **Persistence and state**
   - If needed: file-based, SQL, NoSQL, or external services.
4. **Testing strategy**
   - Unit + integration baseline and minimum CI policy.

## Initial Principles

- Start with a vertical slice to validate assumptions.
- Keep boundaries explicit as modules are added.
- Require tests for bug fixes and core logic.
- Avoid introducing framework complexity without a clear need.

## Suggested First Implementation Plan

1. Choose stack and tooling.
2. Create executable "hello slice".
3. Add lint + format + test commands.
4. Add CI to run checks on pull requests.
5. Expand from one feature into clear module boundaries.
