#!/usr/bin/env python3
"""The Self-Checkout Is Judging You — make.fun entry.

Prints one funny line in the voice of a smug self-checkout machine and
writes that same line to /output/entry.txt. Pure Python standard library,
fully deterministic: no randomness, no time, no network.

The joke: the machine reads the basket out loud (twelve yoghurts, one
banana), claims the authority of its scanner over the shopper's whole
life, then lands the sting — groceries and life choices share an expiry
date, and it is this Friday.
"""

import os
import sys

MAX_CHARS = 200

LINE = (
    "Twelve yoghurts, one banana \u2014 I've scanned your groceries "
    "and your life choices, and both expire Friday."
)


def self_check(line: str) -> None:
    """Fail loudly if the line breaks the bounty gate."""
    if not line or not line.strip():
        raise SystemExit("self-check failed: line is empty or whitespace only")
    if "\n" in line or "\r" in line:
        raise SystemExit("self-check failed: line must be a single line")
    if line != line.strip():
        raise SystemExit("self-check failed: line has leading/trailing whitespace")
    if any(ord(ch) < 0x20 for ch in line):
        raise SystemExit("self-check failed: line contains control characters")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            "self-check failed: line is %d chars, over the %d limit"
            % (len(line), MAX_CHARS)
        )


def main() -> int:
    self_check(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")
    with open("/output/entry.txt", "r", encoding="utf-8") as fh:
        on_disk = fh.read()
    if on_disk != LINE + "\n":
        raise SystemExit("self-check failed: bytes on disk differ from the line")
    sys.stdout.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
