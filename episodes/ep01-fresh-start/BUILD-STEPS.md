# EP 1 — Build Steps (from the video transcript)

**Video:** [How To Automate Your Trading With Zero Skills FOR FREE — EP 1](https://www.youtube.com/watch?v=LxnP1T3Ep0U)
**Repo checkpoint:** [`episodes/ep01-fresh-start`](https://github.com/fractalphive/Trading-Algorithm-Step-By-Step/tree/main/episodes/ep01-fresh-start) on `fractalphive/Trading-Algorithm-Step-By-Step` (tag `ep1`)
**Raw video transcript:** the full EP1 transcript lives in the Obsidian vault at `Frac5/DCA-Algo/Ep 1/transcript.md` (not in this repo). The video's hardcoded-keys code is in the Obsidian note `Frac5/DCA-Algo/Ep 1/python code.md`.

> This is the episode where you go from a **blank virtual machine** (no Python, no VS Code, nothing) to a Python file that connects to Alpaca and submits a paper order for 1 share of SPY. It is the "shitty foundation" — by design. Each later episode replaces a bad habit (hardcoded keys → `.env`, manual button click → scheduled, single order → DCA logic, etc.).

## What you actually build in EP 1

1. Start with a fresh Linux VM that has nothing installed.
2. Install **Python** and **VS Code**.
3. Make a **virtual environment** (an isolated box so you don't pollute the system).
4. Install the **Alpaca Python SDK** (`alpaca-py`) inside that environment.
5. Open a **paper trading** account at Alpaca and generate an API key + secret.
6. Ask a free AI for the code, paste the key/secret **directly into the code** (intentionally — a later episode fixes this), and run it.
7. A market order for **1 share of SPY** is submitted and shows up as `accepted` in the Alpaca paper dashboard.

The repo's `ep01-fresh-start` folder is the **hardened version** of that same script: it reads keys from a `.env` file instead of hardcoding them, and it only *prints the account value* (no order yet) so the first runnable checkpoint is safe. Use the repo version for anything real.

> **Note on the video's approach:** in the video the AI code hardcodes the key/secret (`API_KEY = "THE_KEY"`). That's a deliberate teaching shortcut the host calls out as "making senior devs and cyber-security people mad." Never ship that. Use the safe `.env` version below (Step 7). Also note — because the video script just submits an order each time you run it, hitting "run" repeatedly fires **many SPY orders**. That's the punchline: you have a "button you can click that buys SPY over and over," not a real algo yet.

---

## Step-by-step (mirrors the video order)

### 0. Open a terminal
In VS Code: `File → New Terminal` (or `` Ctrl+` ``). The video uses `` Ctrl+Shift+` `` — if that doesn't open it, use the menu. Paste with `Ctrl+Shift+V` (or right-click → Paste). Clear the screen anytime with `clear`.

### 1. Install Python (Linux/Ubuntu)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```
Verify:
```bash
python3 --version    # you'll see something like Python 3.12.3
pip3 --version
```
> Tell the AI your operating system — it changes the commands. The video is on Linux.

### 2. Install VS Code
- **Linux (snap):** `sudo snap install code --classic`
- Or download from [code.visualstudio.com](https://code.visualstudio.com) and install the `.deb`/package.
- Open VS Code, install the **Python extension** (search "Python" by Microsoft, install it).

### 3. Create a project folder & virtual environment
The video works in a `Documents/DCA` folder. The repo uses the repo root.
```bash
mkdir -p ~/Documents/DCA && cd ~/Documents/DCA   # or: cd your-project-folder

python3 -m venv myenv        # creates a folder "myenv" = the isolated box
source myenv/bin/activate     # activates it — your prompt now shows (myenv)
```
> Why bother: a venv is a little box inside your project so installed packages don't touch the rest of your computer. Delete the folder and it's all gone. The video whiteboards this at ~32:00.
> Note: when the AI says `cd your_project_folder`, that's a placeholder — not a real folder. Don't paste it literally; you're already in your folder.

### 4. Install the Alpaca SDK (inside the venv)
Make sure the venv is active (you see `(myenv)`), then:
```bash
pip install alpaca-py
pip show alpaca-py     # verify it installed
```
> The video calls it "Alpaca SPY" / "SDK" — it's the official `alpaca-py` package. If you skip the venv, `pip install` fails with *"externally managed environment"* (the video hits this at ~29:25).

### 5. Open an Alpaca paper account & get keys
1. Go to [app.alpaca.markets](https://app.alpaca.markets) → sign up (free).
2. Create a **paper** account (fake money — good for learning). The video explains paper vs real at ~12:00: orders still route through Alpaca's systems, just with simulated cash.
3. Generate a new API **key + secret** under the paper account.
4. **Save the key and secret in Obsidian / a password note immediately** — once the screen closes you can't see the secret again; you'd have to regenerate. Store it in a note called `api key secret`.

### 6. Get the code from the AI
Open a **new chat** in a free AI and prompt roughly:
> "I'm using the Alpaca SDK/API to build an algo in Python. I want the algo to connect to Alpaca's API and submit an order to purchase one share of SPY. I'll add my credentials in the code. Here's the URL for Alpaca's API: `<endpoint from Alpaca home page>`."

The AI returns code. Ask for **"SDK code only"** to cut the explanations. Paste it into Obsidian first (a ```python fenced block), then into VS Code.

> **The video's code hardcodes the key/secret** (`API_KEY = "THE_KEY"`). That's a deliberate teaching shortcut the host calls out as "making senior devs and cyber-security people mad." **Do not ship that.** Use the repo's safe version below (Step 7).

### 7. Run it — SAFE version (from the repo checkpoint)
The repo's `code.py` reads keys from a `.env` file and only prints account value (no order). This is the version to actually keep:

`.env` (copy from `.env.example`):
```env
ALPACA_API_KEY=YOUR_API_KEY_HERE
ALPACA_SECRET_KEY=YOUR_SECRET_KEY_HERE
PAPER=true
```

`code.py`:
```python
"""EP01 — connect to Alpaca (paper) and print account value. No orders."""
import os
from dotenv import load_dotenv
from alpaca.trading.client import TradingClient

load_dotenv()

API_KEY = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
PAPER = os.getenv("PAPER", "true").lower() == "true"

if not API_KEY or not SECRET_KEY:
    raise SystemExit("Missing keys — copy .env.example to .env and fill them in.")

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=PAPER)
account = trading_client.get_account()
print(f"Connected (paper={PAPER}).")
print(f"Account value: ${account.equity}")
print(f"Buying power:  ${account.buying_power}")
```
Run:
```bash
python code.py
```

### 8. Run it — the VIDEO version (places the order)
If you want to reproduce exactly what the video did (a real paper order), the raw code from the transcript is in the Obsidian note `Frac5/DCA-Algo/Ep 1/python code.md` (hardcoded keys). **Only run that against a paper account, never real money.** Result on screen: `Order submitted! ID: … Status: accepted`, and the order appears in the Alpaca paper dashboard under *Orders* with source `access key`.

> You can click "run" repeatedly and fire many SPY orders — that's the punchline: you now have a "button you can click that buys SPY over and over." Not an algo yet, just the foundation.

---

## Things the video calls out (don't skip)

- **Tell the AI your OS** every time — commands differ.
- **Use Obsidian** (or any notes app) to store: AI session summaries ("give me a summary in markdown of what I asked you today"), the Python code, and your API key/secret. Free AIs have no memory; your notes are the memory.
- **`cd your_project_folder` is a placeholder** — don't paste it raw.
- **"externally managed environment" error** = you forgot to activate (or create) the venv before `pip install`.
- **Triple-click** a line in the terminal to select the whole line; **double-click** a word to select it.
- Paper trading is the default. Real money never gets touched unless you flip `PAPER=false`.

## How this maps to the repo

| Video step | Repo artifact |
|---|---|
| Installs / venv / SDK | `requirements.txt`, `SETUP.md` |
| Paper keys | `.env.example` (you fill `.env`) |
| Safe connect-only code | `episodes/ep01-fresh-start/code.py` |
| Commands in order | `episodes/ep01-fresh-start/commands.md` |
| AI session notes | `episodes/ep01-fresh-start/memories.md` |
| This walkthrough | `episodes/ep01-fresh-start/BUILD-STEPS.md` |

Next: the host says he's got ~10 episodes planned for the series and will "see you in the next video" — no specifics on EP 2 in this episode.
