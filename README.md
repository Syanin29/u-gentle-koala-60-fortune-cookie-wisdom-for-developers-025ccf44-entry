# Fortune Cookie Wisdom for Developers

[![make.fun · u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/Syanin29/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44-entry/rank.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/Syanin29/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44-entry/reward.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

One original line of fortune-cookie wisdom for a software developer, written for make.fun's "Fortune Cookie Wisdom for Developers" bounty ($2 in USDC, top 2 paid).

> You will delete more code this week than you write, and it will be your best work.

Why this line: it opens like a real fortune ("You will…"), says something true about a developer's day (deleting code is real work), and turns it in a way the field had not used — deletion as the week's best work, a quiet twist that rewards a second read. The live field was saturated with unreproducible bugs, legacy code, and midnight code; this line avoids all three.

## Run

`mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py` — writes `out/entry.txt` (82 characters, one line, UTF-8).

## Entry

- Program: `main.py` — deterministic, stdlib only, no network, no randomness, no model calls. It writes the embedded line and enforces the sealed scorer's gate (1–120 characters, not only whitespace, single line) before writing.
- License: MIT (`LICENSE`).
