"""Umi bootstrap CLI entrypoint."""

from __future__ import annotations

import argparse
from collections.abc import Sequence


def build_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser for the bootstrap entrypoint."""
    parser = argparse.ArgumentParser(
        prog="umi",
        description="Run the Umi bootstrap smoke command.",
        allow_abbrev=False,
    )
    return parser


def _normalize_argv(argv: Sequence[str] | None) -> list[str] | None:
    """Normalize argv for callers that accidentally include the program name."""
    if argv is None:
        return None

    normalized = list(argv)
    if normalized:
        executable = normalized[0].replace("\\", "/").rsplit("/", maxsplit=1)[-1].lower()
        if executable in {"umi", "umi.py", "umi.pyw", "umi.exe", "umi.bat", "umi.cmd"}:
            return normalized[1:]
    return normalized


def main(argv: Sequence[str] | None = None) -> int:
    """Run a minimal bootstrap command for contributors."""
    parser = build_parser()
    try:
        parser.parse_args(_normalize_argv(argv))
    except SystemExit as exc:
        if exc.code is None:
            return 0
        return int(exc.code) if isinstance(exc.code, int) else 1
    print("Umi bootstrap is working.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
