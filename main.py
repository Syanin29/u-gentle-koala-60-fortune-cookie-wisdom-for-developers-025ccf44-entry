"""u-gentle-koala-60 fortune-cookie entry: writes one original line of
fortune-cookie wisdom for a software developer to entry.txt.

Deterministic: no arguments, no network, no randomness, no model calls.
The line is embedded as a string literal; the program only writes it out.
"""

import os
from pathlib import Path

FORTUNE = "You will delete more code this week than you write, and it will be your best work."


def main() -> None:
    # Gate mirrors the sealed scorer: UTF-8 text of 1-120 characters,
    # not only white space. Fail loudly instead of shipping a rejected entry.
    if not 1 <= len(FORTUNE) <= 120:
        raise ValueError(f"fortune is {len(FORTUNE)} characters, must be 1-120")
    if not any(not c.isspace() for c in FORTUNE):
        raise ValueError("fortune has no non-whitespace character")
    if "\n" in FORTUNE.strip():
        raise ValueError("fortune must be a single line")
    output_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(FORTUNE, encoding="utf-8")
    target.chmod(0o644)


if __name__ == "__main__":
    main()
