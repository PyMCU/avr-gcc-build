"""Entry point for the pymcu-avr-toolchain-info console script."""

from __future__ import annotations

import json
import sys


def main() -> None:
    try:
        from pymcu_avr_toolchain import get_bin_dir, manifest
        bin_dir = get_bin_dir()
        print(f"bin_dir: {bin_dir}")
        print(f"manifest: {json.dumps(manifest(), indent=2)}")
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
