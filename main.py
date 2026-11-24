#!/usr/bin/env python3
"""The Funniest Out-of-Office.

Writes one funny single-line out-of-office auto-reply to /output/entry.txt.
The line is a fixed, hand-written text: deterministic, so both runs produce
byte-identical output.

Gate (from the bounty RULES.txt): /output/entry.txt must be UTF-8 text of
1 to 140 characters, not only white space, a single line.
"""

import os
import sys

REPLY = (
    "I'm out of office until Monday. I read your email the second it "
    "arrived. I'll reply on Monday as if I hadn't."
)


def gate_check(text: str) -> None:
    """Fail loudly if the text would fail the bounty gate."""
    if not (1 <= len(text) <= 140):
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    if text.strip() == "":
        raise ValueError("entry must not be only white space")
    if "\n" in text.rstrip("\n") or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")


def main() -> int:
    gate_check(REPLY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(REPLY + "\n")
    # Verify what actually landed on disk, not just what we meant to write:
    # the gate scores the file, so re-check the file content (minus the
    # single trailing newline the writer adds).
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    gate_check(written[:-1] if written.endswith("\n") else written)
    print(f"wrote {path} ({len(REPLY)} characters, verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
