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


def test_cli_rejects_unknown_arguments() -> None:
    result = subprocess.run(
        [sys.executable, "umi.py", "--unknown"],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 2
    assert "unrecognized arguments: --unknown" in result.stderr
