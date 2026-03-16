# Umi

Umi is a lightweight Python CLI starter project designed to be easy to fork, extend, and publish as an open-source repository.

## ✨ Highlights

- Clean Python package layout under `src/`
- CLI entrypoint available as:
  - `python umi.py` (repository script)
  - `python -m umi` (package module)
- Basic pytest suite for smoke and argument behavior
- Documentation site content in `docs/` ready for GitHub Pages
- CI and Pages workflows prepared under `.github/workflows/`

## 📦 Project Structure

```text
.
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── pages.yml
├── docs/
│   ├── architecture.md
│   ├── index.md
│   └── _config.yml
├── src/
│   └── umi/
│       ├── __init__.py
│       ├── __main__.py
│       └── cli.py
├── tests/
│   └── test_umi.py
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── umi.py
```

## 🚀 Quick Start

### Requirements

- Python 3.10+

### Run locally

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

## 📚 Documentation & GitHub Pages

This repository is configured to publish `docs/` with a GitHub Pages workflow.

1. Push to GitHub.
2. In repository settings, ensure **Pages** is set to **GitHub Actions** as source.
3. The `pages.yml` workflow will deploy on pushes to `main` (and is runnable manually).

## 🤝 Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening pull requests.

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
