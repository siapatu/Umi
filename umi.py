"""Umi bootstrap CLI entrypoint."""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser for the bootstrap entrypoint."""
    parser = argparse.ArgumentParser(
        prog="umi",
        description="Run the Umi bootstrap smoke command.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run a minimal bootstrap command for contributors."""
    parser = build_parser()
    parser.parse_args(argv)
    print("Umi bootstrap is working.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
