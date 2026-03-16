# Contributing to Umi

Thanks for your interest in improving Umi.

## Ways to contribute

- Report bugs via GitHub issues
- Propose and discuss enhancements
- Improve documentation and examples
- Submit code fixes and tests

## Development setup

```bash
git clone https://github.com/OWNER/REPO.git
cd REPO
python -m pip install --upgrade pip pytest
```

Run checks locally:

```bash
PYTHONPATH=src pytest -q
```

## Branch and PR workflow

1. Create a feature branch from `main`.
2. Keep commits focused and descriptive.
3. Update tests/docs for behavior changes.
4. Open a pull request using the provided PR template.

## Commit message guidance

Use clear, imperative subject lines:

- `docs: improve quickstart instructions`
- `test: add CLI unknown argument coverage`
- `feat: add new command scaffold`

## Pull request checklist

- [ ] Change is scoped and understandable
- [ ] Tests updated/added where appropriate
- [ ] Documentation updated for user-facing changes
- [ ] CI passes

## Community expectations

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
