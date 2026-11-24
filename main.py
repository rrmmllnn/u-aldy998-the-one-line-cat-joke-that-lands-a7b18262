#!/usr/bin/env python3
"""One-line cat joke, written out for the entry file.

The gag: a cat who does nothing all day, guards the
best seat in the house, and still ends up looking like the
winner. The laugh sits in the gap between what she contributes
(nothing at all) and the standing she ends up holding (top of the
household, by a mile).
"""

import os

MAX_LEN = 200


def check_line(line):
    """Only accept a single plain line within the length budget."""
    if not line:
        raise ValueError("empty line")
    if line != line.strip():
        raise ValueError("leading or trailing space")
    if any(ch in line for ch in "\r\n"):
        raise ValueError("must stay on one line")
    if len(line) > MAX_LEN:
        raise ValueError("line over the limit")
    return line


def build():
    """Join the joke from short pieces, then validate it."""
    pieces = [
        "My cat has never paid rent, ",
        "never washed a dish, never once ",
        "apologised, and still glares when I ",
        "sit in her chair ",
        "\u2014 honestly, she\u2019s the most ",
        "successful person I know.",
    ]
    return check_line("".join(pieces))


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(build())


if __name__ == "__main__":
    main()
