#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Writes one funny one-line review of my Monday to ``entry.txt`` inside
the output directory (``/output`` by default, or the directory given as
the first command-line argument).

The output is fully deterministic: no network access, no randomness,
no clock reads, and no file reads. Two runs produce byte-identical
output.

Usage:
    python3 main.py [output_dir]
"""

import sys
from pathlib import Path

# The entry: exactly one line, 83 characters, no trailing newline.
ENTRY = "The printer jammed on page 2 of 3, which is the most honest thing it has ever done."


def write_entry(output_dir: str) -> Path:
    """Write ENTRY to ``<output_dir>/entry.txt`` and return its path."""
    # Guard the entry contract: exactly one line, 1-200 characters,
    # no trailing newline. If this ever fails, the entry itself is
    # wrong and must be fixed, not the writer.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    destination = Path(output_dir) / "entry.txt"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(ENTRY, encoding="utf-8", newline="")
    return destination


def main(argv: list) -> int:
    output_dir = argv[1] if len(argv) > 1 else "/output"
    write_entry(output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
