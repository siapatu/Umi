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


def _load_main():
    import importlib.util
    from pathlib import Path

    spec = importlib.util.spec_from_file_location("umi_module", Path("umi.py"))
    assert spec is not None
    assert spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.main


def test_main_returns_exit_code_for_parse_errors() -> None:
    main = _load_main()

    assert main(["--unknown"]) == 2


def test_main_returns_exit_code_for_help() -> None:
    main = _load_main()

    assert main(["--help"]) == 0
