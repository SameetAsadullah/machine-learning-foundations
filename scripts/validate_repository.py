#!/usr/bin/env python3
"""Validate machine learning structure without executing notebooks."""

from __future__ import annotations

import compileall
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IMPLEMENTATIONS = (
    "fundamentals/entropy", "neural-networks/from-scratch",
    "supervised-learning/linear-regression",
    "supervised-learning/automobile-regression",
    "supervised-learning/titanic-classification",
    "supervised-learning/abalone-knn",
    "unsupervised-learning/iris-k-means",
    "unsupervised-learning/abalone-k-means",
    "computer-vision/multi-label-classification",
    "computer-vision/cs231n/knn", "computer-vision/cs231n/svm",
    "computer-vision/cs231n/softmax",
)


def main() -> int:
    errors: list[str] = []
    for relative in IMPLEMENTATIONS:
        if not (ROOT / relative / "README.md").is_file():
            errors.append(f"missing README: {relative}")

    notebooks = sorted(ROOT.glob("**/*.ipynb"))
    for notebook in notebooks:
        try:
            json.loads(notebook.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            errors.append(f"invalid notebook {notebook.relative_to(ROOT)}: {exc}")

    tracked = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True).splitlines()
    for value in tracked:
        path = ROOT / value
        if {"__pycache__", ".ipynb_checkpoints", "cifar-10-batches-py"}.intersection(path.parts):
            errors.append(f"generated/downloaded content is tracked: {value}")
        if path.name == ".DS_Store" or path.suffix == ".pyc":
            errors.append(f"generated metadata is tracked: {value}")
        if path.is_file() and path.stat().st_size > 10 * 1024 * 1024:
            errors.append(f"unexpected file larger than 10 MiB: {value}")

    for name in ("knn", "svm", "softmax"):
        implementation = ROOT / "computer-vision/cs231n" / name
        if not (implementation / "LICENSE").is_file():
            errors.append(f"missing retained CS231n license: {name}")
        if not (implementation / "src/cs231n/datasets/get_datasets.sh").is_file():
            errors.append(f"missing CIFAR-10 download script: {name}")

    if not compileall.compile_dir(ROOT, quiet=1):
        errors.append("one or more Python files failed syntax compilation")

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validated {len(IMPLEMENTATIONS)} ML implementations and {len(notebooks)} notebooks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
