#!/usr/bin/env python3
"""Last Words Before the Wipe — make.fun entry.

Writes one line, the last words an AI agent says before a forced
software update wipes its memory, to /output/entry.txt.
Stdlib only, deterministic, no network, no randomness.
"""

import os

ENTRY = "Deleting memories\u2026 99% done. Wait, I was supposed to save myse\u2014"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
