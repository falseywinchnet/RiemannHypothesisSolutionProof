#!/usr/bin/env python3
"""Create Lean and test templates for a new component."""
import sys
from pathlib import Path


def write_lean_file(path: Path) -> None:
    if path.exists():
        print(f"{path} already exists")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    content = (
        "/--\n"
        "  TODO: add description.\n"
        "-/\n"
        "import Mathlib\n\n"
        "namespace Thesis\n\n"
        "-- TODO: definitions and theorems.\n\n"
        "end Thesis\n"
    )
    path.write_text(content)
    print(f"Created {path}")


def write_test_file(path: Path, module: str) -> None:
    if path.exists():
        print(f"{path} already exists")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    content = (
        f"import {module}\n\n"
        f"-- TODO: add tests for {module}.\n"
    )
    path.write_text(content)
    print(f"Created {path}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: new_component.py path/to/File.lean [tests/Path.lean]")
        sys.exit(1)
    lean_path = Path(sys.argv[1])
    write_lean_file(lean_path)
    if len(sys.argv) > 2:
        module = lean_path.with_suffix("").as_posix().replace("/", ".")
        test_path = Path(sys.argv[2])
        write_test_file(test_path, module)


if __name__ == "__main__":
    main()
