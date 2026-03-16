import subprocess
import sys


def test_cli_runs_successfully() -> None:
    result = subprocess.run(
        [sys.executable, "umi.py"],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Umi bootstrap is working." in result.stdout


def test_cli_help_flag_displays_usage() -> None:
    result = subprocess.run(
        [sys.executable, "umi.py", "--help"],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "usage:" in result.stdout
    assert "Run the Umi bootstrap smoke command." in result.stdout


def test_cli_does_not_accept_abbreviated_flags() -> None:
    result = subprocess.run(
        [sys.executable, "umi.py", "--hel"],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 2
    assert "unrecognized arguments: --hel" in result.stderr


def test_cli_rejects_unknown_arguments() -> None:
    result = subprocess.run(
        [sys.executable, "umi.py", "--unknown"],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 2
    assert "unrecognized arguments: --unknown" in result.stderr


def test_main_returns_zero_for_help_without_raising() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "import umi; raise SystemExit(umi.main(['--help']))",
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "usage:" in result.stdout


def test_main_returns_two_for_unknown_args_without_raising() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "import umi; raise SystemExit(umi.main(['--unknown']))",
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 2
    assert "unrecognized arguments: --unknown" in result.stderr


def test_main_handles_systemexit_with_none_code() -> None:
    import pathlib
    import sys

    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
    import umi

    class DummyParser:
        def parse_args(self, argv: list[str] | None) -> None:
            raise SystemExit(None)

    original = umi.build_parser
    try:
        umi.build_parser = lambda: DummyParser()
        assert umi.main([]) == 0
    finally:
        umi.build_parser = original


def test_main_accepts_argv_with_program_name() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "import umi; raise SystemExit(umi.main(['umi.py', '--help']))",
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "usage:" in result.stdout


def test_main_rejects_unknown_args_when_program_name_is_present() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "import umi; raise SystemExit(umi.main(['umi', '--unknown']))",
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 2
    assert "unrecognized arguments: --unknown" in result.stderr
