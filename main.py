#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut.

Writes the GPS's excuse, in its own voice, as a single line of plain text
to /output/entry.txt (no trailing newline).
"""

import os

LINE = (
    "That field was technically a shortcut — the highway was being boring "
    "and your suspension needed character development."
)


def main() -> None:
    line = LINE
    assert line, "line must not be empty"
    assert line.strip(), "line must not be only whitespace"
    assert "\n" not in line and "\r" not in line, "line must be exactly one line"
    assert 1 <= len(line) <= 200, "line must be 1-200 characters"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
