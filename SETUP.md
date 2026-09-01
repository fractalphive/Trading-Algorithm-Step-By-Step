# Setup — from a fresh machine to your first run

These are the one-time steps before any episode. Each episode folder under
`episodes/` then links back here so you only do this once.

## 1. Install Python

- Download from https://www.python.org/downloads/ (3.11+ recommended).
- Verify: `python --version` (or `python3 --version`).

## 2. Install the algo's libraries

From the repo root:

```bash
pip install -r requirements.txt
```

## 3. Open an Alpaca paper account

- Sign up at https://app.alpaca.markets/ — paper trading is free, no real money.
- Generate an API key + secret under "Paper Trading".

## 4. Add your keys

```bash
cp .env.example .env
```

Open `.env` and paste your key/secret in. These stay on your machine only.

## 5. Per-episode

Each episode lives in its own folder:

```bash
cd episodes/ep01-fresh-start
python code.py
```

Follow that episode's `README.md`, `commands.md`, and `memories.md`.

## Jump to any episode

The repo is tagged per episode so you can start anywhere:

```bash
git checkout ep05      # lands you at the end-of-episode-5 checkpoint
```

> 🧪 Paper trading is the default. Nothing touches real money unless you flip
> `PAPER=false` in `.env` yourself.
