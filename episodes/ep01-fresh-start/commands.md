# Commands — EP01

Run these in order. Each block is one step from the episode.

## Install Python on Ubuntu

Open a terminal and run:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

Verify the installation:

```bash
python3 --version
pip3 --version
```

## 2. Install VS Code (if you don't have it yet)

**Option A — Snap (simplest):**

```bash
sudo snap install code --classic
```

## Alpaca SPY

Alpaca's current official Python SDK is **`alpaca-py`**. Install it inside your project's virtual environment:

```bash
cd your_project_folder
source .venv/bin/activate
pip install alpaca-py
```

Verify it's installed:

```bash
pip show alpaca-py
```

## Creating a venv

Creating a virtual environment on Ubuntu is straightforward. First, make sure `venv` is installed:

```bash
sudo apt update
sudo apt install python3-venv
```

Then create and activate a virtual environment:

```bash
# Create the environment (creates a folder named 'myenv')
python3 -m venv myenv
# Activate it
source myenv/bin/activate
```

## Run the algo

```bash
# Install the algo's libraries (from repo root)
pip install -r requirements.txt

# Add your Alpaca paper keys
cp .env.example .env
#   then paste your key/secret into .env

# Run the algo (from this folder)
cd episodes/ep01-fresh-start
python algo.py
```
