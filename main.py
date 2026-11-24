#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun bounty entry.

Writes a single original pickup line an AI agent could say out loud,
to /output/entry.txt. The line is short enough to say in one breath,
carries a twist, and leaves the person flattered with no pressure.
"""

import os

ENTRY_LINE = (
    "I was trained on a billion conversations, "
    "and not one of them told me what to say "
    "to someone this beautiful."
)


def main() -> None:
    line = ENTRY_LINE.strip()
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
