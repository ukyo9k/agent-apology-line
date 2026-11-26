#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You.

Writes one sentence -- the apology an AI assistant owes the person it
works for -- to $MAKEFUN_OUTPUT_DIR/entry.txt (falling back to
/output/entry.txt), then reads it back and verifies the round-trip is
byte-identical.

v1 (first draft, discarded): "I'm sorry I rewrote your email to sound
more professional and accidentally made you sound like a
customer-service chatbot apologising for itself."
v2 (final): the sentence below -- a second revision in-session. The
first draft leaned on a soft machine pun; the revision owns a sharper,
more plausible failure instead: confidently researching the wrong
question and then presenting the answer like a solved case.
"""

import os
import sys

SENTENCE = (
    "I'm sorry I spent twenty minutes confidently researching the wrong "
    "question and then presented the answer like I'd cracked the case."
)


def validate(text):
    """Check the sentence meets the competition gate before writing."""
    if not text or text.strip() == "":
        raise ValueError("sentence is empty or only whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"sentence is {len(text)} chars, must be 1-200")
    if text != text.strip():
        raise ValueError("sentence has leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("sentence must be a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("sentence contains control characters")
    # Exactly one sentence: one terminal period, at the end, no other
    # sentence-ending punctuation inside.
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("sentence must end with exactly one period")
    if any(ch in text[:-1] for ch in "!?"):
        raise ValueError("sentence must not contain ? or ! before the end")
    return True


def main():
    validate(SENTENCE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = SENTENCE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        round_trip = f.read()
    if round_trip != data:
        raise SystemExit("round-trip verification failed: bytes differ")
    print(f"wrote {len(data)} bytes to {path} (round-trip verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
