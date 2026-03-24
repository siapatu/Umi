# Umi

A lightweight, production-friendly Python CLI starter template for open-source projects.

[![CI](https://img.shields.io/github/actions/workflow/status/OWNER/REPO/ci.yml?branch=main&label=ci)](https://github.com/OWNER/REPO/actions/workflows/ci.yml)
[![Pages](https://img.shields.io/github/actions/workflow/status/OWNER/REPO/pages.yml?branch=main&label=pages)](https://github.com/OWNER/REPO/actions/workflows/pages.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Deploy docs to GitHub Pages](https://github.com/siapatu/Umi/actions/workflows/pages.yml/badge.svg)](https://github.com/siapatu/Umi/actions/workflows/pages.yml)

> Replace `OWNER/REPO` badge links after forking this template.

## Why this template?

Umi gives you a clean foundation for a serious open-source project:

- ✅ `src/` layout with module entrypoint
- ✅ test suite with `pytest`
- ✅ CI workflow for pull requests and pushes
- ✅ GitHub Pages deployment workflow for docs
- ✅ contribution, security, and community health docs

## Project structure

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── config.yml
│   │   └── feature_request.md
│   ├── workflows/
│   │   ├── ci.yml
│   │   └── pages.yml
│   └── pull_request_template.md
├── docs/
│   ├── _config.yml
│   ├── architecture.md
│   └── index.md
├── src/
│   └── umi/
│       ├── __init__.py
│       ├── __main__.py
│       └── cli.py
├── tests/
│   └── test_umi.py
├── .gitignore
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── SECURITY.md
├── pyproject.toml
└── umi.py
```

## Quick start

### Requirements

- Python 3.10+

### Install dependencies

```bash
python -m pip install --upgrade pip pytest
```

### Run the CLI

```bash
python umi.py
```

or:

```bash
PYTHONPATH=src python -m umi
```

### Run tests

```bash
PYTHONPATH=src pytest -q
```

## Documentation and GitHub Pages

The repository is configured to deploy the `docs/` directory to GitHub Pages using GitHub Actions.

1. Push this repository to GitHub.
2. Go to **Settings → Pages**.
3. Set **Build and deployment / Source** to **GitHub Actions**.
4. Push to `main` (or run the workflow manually) to publish docs.

## Open-source defaults included

- [MIT License](LICENSE)
- [Contributing guide](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security policy](SECURITY.md)
- [Issue and PR templates](.github)

## Roadmap

- Add packaging/publishing workflow to PyPI
- Add linting (`ruff`) and type-checking
- Expand docs with usage examples

## License

Licensed under the MIT License. See [LICENSE](LICENSE).
