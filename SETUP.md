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

## 4b. How `.env` is used (not covered in the video)

The `.env` file holds your secrets as plain `KEY=value` lines. The code never
sees those values hardcoded — it reads them at runtime. Here's the whole
mechanism, start to finish.

### What's in it

```env
ALPACA_API_KEY=YOUR_API_KEY_HERE
ALPACA_SECRET_KEY=YOUR_SECRET_KEY_HERE
PAPER=true
```

`.env` is listed in `.gitignore`, so Git will **never** commit it. Only
`.env.example` (blank placeholders) is tracked. That's the whole point — your
real keys live on your machine and yours alone.

### How the code reads it

Every `code.py` starts with:

```python
import os
from dotenv import load_dotenv

load_dotenv()                       # reads .env from the current working directory

API_KEY = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
PAPER = os.getenv("PAPER", "true").lower() == "true"
```

`load_dotenv()` loads the file into environment variables; `os.getenv(...)` reads
them. `python-dotenv` is installed by `requirements.txt`, so this just works once
you've run `pip install -r requirements.txt`.

### Running from the terminal

`load_dotenv()` looks for `.env` in the **current working directory** (where you
ran `python`). From an episode folder:

```bash
cd episodes/ep01-fresh-start
python code.py
```

This works because `.env` sits at the repo root and `python-dotenv` walks **up**
the directory tree to find it. You don't need to copy `.env` into each episode
folder.

### Running inside VS Code

VS Code doesn't do anything special with `.env` — the code reads it the same way.
Two ways to run:

1. **Integrated terminal (simplest):** open the repo in VS Code
   (`File → Open Folder`), then use the terminal panel (`Ctrl+\``) and run
   `cd episodes/ep01-fresh-start && python code.py`. Same as the terminal above.
2. **Run/Debug button (`F5`):** VS Code launches from the folder you opened, so
   `load_dotenv()` still finds the root `.env`. If you run a single file with
   `F5` and it can't find `.env`, set the **cwd** in `.vscode/launch.json`:

   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Run episode",
         "type": "python",
         "request": "launch",
         "program": "${file}",
         "cwd": "${workspaceFolder}",
         "console": "integratedTerminal"
       }
     ]
   }
   ```

   `"cwd": "${workspaceFolder}"` makes sure `.env` at the repo root is found
   regardless of which file you hit Run on.

> If you ever want VS Code to auto-load `.env` into the terminal's environment,
> add `"python.envFile": "${workspaceFolder}/.env"` to `.vscode/settings.json` —
> but the code's own `load_dotenv()` already covers it, so this is optional.

### Editing secrets safely

- Never paste real keys into `code.py`, an Issue, or Discord.
- To rotate keys, just edit `.env` — no code change needed.
- If you delete `.env`, re-run `cp .env.example .env` and paste the keys again.

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
