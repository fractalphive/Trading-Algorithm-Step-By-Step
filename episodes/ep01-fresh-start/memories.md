# AI session memory — EP01

## Summary of Today's Conversation

### 1. Setting Up Python in VS Code on Ubuntu

You asked how to install Python for use with VS Code on Ubuntu Linux. I walked you through:

- Installing Python 3, pip, and venv via `apt`
- Installing VS Code (Snap or Microsoft's APT repo)
- Adding the **Python extension** in VS Code
- Selecting the interpreter and creating a virtual environment
- Running a test script with `F5`

### 2. Installing the Alpaca API SDK

You then asked how to install the Alpaca trading API SDK. I covered:

- Installing the current official SDK: `pip install alpaca-py`
- Noting the legacy alternative (`alpaca-trade-api`)
- Namespace structure (`alpaca.trading`, `alpaca.data`, `alpaca.broker`)
- Getting API keys and using **paper trading** for testing
- Best practices for managing API keys with environment variables and `.env` files

---

It looks like you're building toward a Python trading setup on Ubuntu — possibly a trading bot or algorithmic trading project with Alpaca. Feel free to ask if you want help with the next steps, like fetching market data, backtesting strategies, or automating orders! 📊


## Summary of Today's Conversation

### Topic: Python Virtual Environments on Ubuntu Linux

You asked **how to create a virtual environment in Linux (Ubuntu)**, and I provided:

- **Installation** of the `venv` module via `apt` (`sudo apt install python3-venv`)
- **Creating** an environment: `python3 -m venv myenv`
- **Activating** it: `source myenv/bin/activate`
- **Installing packages** with `pip` inside the isolated environment
- **Deactivating** with the `deactivate` command
- **Extra tips**: using alternate Python versions, removing an environment with `rm -rf`, and exporting dependencies with `pip freeze > requirements.txt`

---

_That's everything so far — let me know if you'd like to continue with project setup or dive into a related tool like `poetry` or `conda`!_
