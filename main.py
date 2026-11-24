#!/usr/bin/env python3
"""Write one funny one-line review of my Monday to /output/entry.txt.

Deterministic: no network, no randomness, no clock, no file reads.
Usage: python3 main.py [output_dir]   (default output_dir is /output)
"""

import os
import sys

ENTRY = "The printer jammed on page 2 of 3, which is the most honest thing it has ever done."


def main() -> None:
    output_dir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
