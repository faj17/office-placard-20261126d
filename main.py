#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest — entry for the stapler.

Writes a single museum-placard-style line (1-180 chars, no trailing
newline) to /output/entry.txt.
"""

import os
import sys

MAX_CHARS = 180

FRAGMENTS = [
    "Stapler, c. 1998.",
    "Steel and spring.",
    "A ritual press that wed two sheets with a single tooth;",
    "gift of the filing clerks, who believed no page should die alone.",
]


def assemble(fragments=FRAGMENTS):
    return " ".join(fragments)


def validate(line, max_chars=MAX_CHARS):
    if not 1 <= len(line) <= max_chars:
        raise ValueError(f"placard line must be 1-{max_chars} chars, got {len(line)}")
    if line.endswith("\n"):
        raise ValueError("placard line must not end with a newline")
    return line


ENTRY = validate(assemble())

OUTPUT_PATH = "/output/entry.txt"


def write_entry(path=OUTPUT_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return path


def main():
    path = write_entry()
    print(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to {path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
