#!/usr/bin/env python3
"""Entry for make.fun u-suga-everyday-things-two-lines-longer-run-f8734479.

Writes two lines to /output/entry.txt (UTF-8, no network):
line 1 explains a toaster to a 10-year-old through one analogy;
line 2 says what that analogy maps and what it leaves out.
Python 3 standard library only.
"""

import os

LINE_1 = (
    "A toaster is a tiny elevator that takes your bread down into "
    "a hot basement and brings it back up brown."
)
LINE_2 = (
    "It maps the trip down into the heat and back up brown, "
    "but leaves out that elevators never cook anything."
)


def main() -> None:
    text = LINE_1 + "\n" + LINE_2 + "\n"
    # Gate assertions: exactly two lines, 1-400 characters total,
    # each line one non-empty sentence.
    body = text.rstrip("\n")
    assert 1 <= len(body) <= 400, f"entry is {len(body)} chars, must be 1-400"
    lines = body.split("\n")
    assert len(lines) == 2, f"entry has {len(lines)} lines, must be exactly 2"
    for line in lines:
        assert line.strip(), "entry line must not be empty"
        assert line.endswith("."), "each line must end with a full stop"
        assert line.count(".") == 1, "each line must be exactly one sentence"
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(out_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
