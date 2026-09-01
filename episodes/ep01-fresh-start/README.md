# EP01 — Fresh start: connect, print account value

**Video:** [How To Automate Your Trading With Zero Skills FOR FREE — EP 1](https://www.youtube.com/watch?v=LxnP1T3Ep0U)

## What this episode builds

A brand-new machine to the first runnable code: it connects to Alpaca (paper)
and prints your account value. No orders yet — just proof the plumbing works.

## Checkpoint

`code.py` at the end of this episode connects and prints account value. Run it
from this folder after completing [SETUP.md](../../SETUP.md):

```bash
python code.py
```

## Files in this folder

- `code.py` — the runnable checkpoint
- `commands.md` — every command, in order
- `memories.md` — AI session summary of what we worked on
- `BUILD-STEPS.md` — full follow-along transcribed from the EP 1 video, with the safe (`.env`) code and the gotchas the video hits

## What the video deliberately does "wrong" (so you don't copy it)

The EP 1 video hardcodes the Alpaca API key/secret **directly in the code** (`API_KEY = "THE_KEY"`). That's an intentional teaching shortcut — the host calls it out as "making senior devs and cyber-security people mad." This folder's `code.py` does it the right way (keys in `.env`). Also: the video's script submits an order every time you run it, so clicking "run" repeatedly fires **many SPY orders**. See `BUILD-STEPS.md` for both the safe version and the faithful video version.
