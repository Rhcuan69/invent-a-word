"""Invent a Word We Need — entry program.

Writes one invented English word and its one-line definition to
/output/entry.txt. Standard library only; deterministic: the same
bytes on every run. No network access, no files read.
"""

import os

ENTRY = "Clocklapse (n.): checking the time and losing it the instant you look away."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(ENTRY) <= 140 or not ENTRY.strip():
        raise SystemExit("entry fails the 1-140 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
