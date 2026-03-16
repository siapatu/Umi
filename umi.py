"""Umi bootstrap CLI entrypoint."""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser for the bootstrap entrypoint."""
    parser = argparse.ArgumentParser(
        prog="umi",
        description="Run the Umi bootstrap smoke command.",
        allow_abbrev=False,
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run a minimal bootstrap command for contributors."""
    parser = build_parser()
    try:
        parser.parse_args(argv)
    except SystemExit as exc:
        if exc.code is None:
            return 0
        return int(exc.code) if isinstance(exc.code, int) else 1
    print("Umi bootstrap is working.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
