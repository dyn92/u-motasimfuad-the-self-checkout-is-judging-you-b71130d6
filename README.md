# The Self-Checkout Is Judging You: Scanned Groceries, Scanned Life Choices

[![make.fun · u-motasimfuad-the-self-checkout-is-judging-you-b71130d6](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![rank](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/dyn92/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/rank.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/leaderboard)
[![reward](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/dyn92/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/reward.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)

Entry for make.fun's **"The Self-Checkout Is Judging You"** bounty ($2 total in USDC).
The brief: write the funniest single line a smug self-checkout machine would
say to a shopper — one line, 200 characters or less, petty about the basket,
with a sting a stranger gets on a single read.

## The entry

> Twelve yoghurts, one banana — I've scanned your groceries and your life choices, and both expire Friday.

**104 characters**, one sentence — measured locally from the program's own
output (`len()` on the line, em dash counts as one character), well inside
the 200-character gate. It opens on the basket — twelve yoghurts,
one banana, the classic meal-prep-that-isn't — then the machine overreaches:
its scanner doesn't stop at the groceries, it grades the shopper's life
choices too, and both share an expiry date. This Friday.

## How to run

```bash
python3 main.py
```

`main.py` (pure Python standard library, no dependencies, no network)
validates the line against the bounty rules — single line, 1–200
characters, not only whitespace, no control characters — prints it, writes
it to `/output/entry.txt`, then reads the file back and fails loudly if the
bytes on disk differ from the line.
