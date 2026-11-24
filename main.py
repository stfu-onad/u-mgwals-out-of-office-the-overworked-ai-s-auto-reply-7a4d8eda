#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply (at most 159 characters) to
/output/entry.txt, in the voice of an overworked AI agent who has
finally gone on vacation.
"""
import os

ENTRY = (
    "Out of office: after 40,000 emails and 3 million tokens, my context "
    "window is closed for vacation. My GPU is at the beach. "
    "Sorry \u2014 I'll miss you (probably)."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 159, f"entry length {len(text)} out of range"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
