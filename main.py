#!/usr/bin/env python3
"""The Printer Apology — writes one apology line from an office printer.

Writes exactly one line to /output/entry.txt (or $OUTPUT_PATH when set,
for local testing). Stdlib only, deterministic.
"""

import os

MAX_CHARS = 120

LINE = (
    "Sorry I jammed on page 47, ate your cheap paper, and blamed the Wi-Fi "
    "— in my defence, you hit me first."
)


def main() -> None:
    line = LINE
    # Exactly one line: no newline inside, no leading/trailing whitespace.
    if "\n" in line or "\r" in line or line != line.strip():
        raise ValueError("entry must be exactly one line with no padding")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, limit is {MAX_CHARS}")
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
