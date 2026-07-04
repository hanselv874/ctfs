#!/usr/bin/env python3
"""Helper runner for Challenge1.

Usage:
  python3 solver/solve.py --input "1234"
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def run_binary(user_input: str) -> str:
    challenge_bin = Path(__file__).resolve().parents[1] / "challenge" / "crackMe"
    proc = subprocess.run(
        [str(challenge_bin)],
        input=(user_input + "\n").encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return proc.stdout.decode("utf-8", errors="replace")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run crackMe with one input value")
    parser.add_argument("--input", default="", help="Input to send to crackMe")
    args = parser.parse_args()

    output = run_binary(args.input)
    print(output)


if __name__ == "__main__":
    main()
