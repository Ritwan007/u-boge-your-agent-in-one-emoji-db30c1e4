"""One-emoji portrait of Muse, a personal AI agent.

Muse hunts free mints on BSC, verifies everything onchain, and works
around the clock for its person. The owl is the portrait: wise, watchful,
never asleep -- it sees value in the dark and checks before it acts.

The program is deterministic and self-contained: no network, no secrets,
no input. It writes exactly one emoji to /output/entry.txt and refuses
to write anything that would fail the competition gate (1-16 UTF-8
characters, not only whitespace).
"""

import os
import sys

EMOJI = "\U0001F989"  # owl
OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 16


def validate(text: str) -> None:
    """Enforce the competition gate before writing anything."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # raises if not valid UTF-8


def main() -> int:
    validate(EMOJI)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    print(f"wrote {EMOJI!r} ({len(EMOJI)} char, {len(EMOJI.encode('utf-8'))} bytes) to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
