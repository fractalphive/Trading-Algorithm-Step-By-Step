"""
EP01 — Fresh start: connect to Alpaca (paper) and print account value.

No orders are placed in this episode. It just proves the plumbing works:
your code can authenticate and talk to the broker.

Keys come from environment variables (see .env.example) — never hardcode them.
"""

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
