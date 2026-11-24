#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run — variant A (toaster).

Writes the two-line entry to /output/entry.txt first, then (best effort
only) a byte-identical copy next to this file via write_repo_copy().
The grader sandbox mounts the repo read-only, so the repo-root copy
must never crash the run.
"""

import os

ENTRY_TEXT = (
    "A toaster is a stand-up tanning booth for bread: you slide a slice in "
    "upright between glowing red bars, it gets a quick tan on both sides, "
    "then pops up brown, warm, and crisp.\n"
    "It maps how heat browns bread the way sunshine browns skin, but leaves "
    "out that the bread has no say in how brown it gets, and that wires, "
    "not the sun, dry it crisp as well as browning it.\n"
)


def write_repo_copy():
    """Best-effort byte-identical copy next to this file.

    The grader sandbox mounts the repo read-only, so any failure here
    must never crash the run — callers rely on the OSError guard.
    """
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY_TEXT)
    except OSError:
        pass


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    write_repo_copy()


if __name__ == "__main__":
    main()
