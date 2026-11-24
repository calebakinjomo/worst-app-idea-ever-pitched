#!/usr/bin/env python3
"""PebblePal: the worst app idea ever pitched.

Writes one sentence (<=240 chars) pitching the worst, most useless app
imaginable to /output/entry.txt. Deterministic: same bytes every run.
Reviser note: docstring touch only; the entry bytes are unchanged.
"""

import os

ENTRY = (
    "PebblePal is a $4.99-a-month app that photographs the same pebble in "
    "your garden every morning, tracks its mood across the seasons, and "
    "texts you the moment it looks a bit off today, because every pebble "
    "deserves to be heard."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 240, f"entry is {len(ENTRY)} chars"
    # One sentence: no ". " mid-text (the "$4.99" price holds the only
    # other period) and exactly one sentence-ending full stop.
    assert ENTRY.strip() == ENTRY and ENTRY.endswith(".")
    assert ENTRY.count(". ") == 0 and ENTRY.count("!") == 0
    assert ENTRY.count("?") == 0
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
