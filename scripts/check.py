import compileall
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"


def main() -> int:
    sys.path.insert(0, str(SRC))
    checks = [
        ("compileall", run_compileall),
        ("unittest", run_unittest),
        ("flake8", lambda: run_optional_module("flake8", ["src", "tests", "scripts", "main.py"])),
        ("mypy", lambda: run_optional_module("mypy", ["src"])),
    ]

    failed = []
    for name, check in checks:
        print(f"==> {name}")
        if check() != 0:
            failed.append(name)

    if failed:
        print(f"Failed checks: {', '.join(failed)}")
        return 1

    print("All checks passed.")
    return 0


def run_compileall() -> int:
    ok = compileall.compile_dir(ROOT / "src", quiet=1)
    ok = compileall.compile_dir(ROOT / "scripts", quiet=1) and ok
    ok = compileall.compile_dir(ROOT / "tests", quiet=1) and ok
    ok = compileall.compile_file(ROOT / "main.py", quiet=1) and ok
    return 0 if ok else 1


def run_unittest() -> int:
    return subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests"],
        cwd=ROOT,
        check=False,
    ).returncode


def run_optional_module(module_name: str, args: list[str]) -> int:
    result = subprocess.run(
        [sys.executable, "-m", module_name, *args],
        cwd=ROOT,
        check=False,
    )
    if result.returncode == 1 and module_name in {"flake8", "mypy"}:
        return 1
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
