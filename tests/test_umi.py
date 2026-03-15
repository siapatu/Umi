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
