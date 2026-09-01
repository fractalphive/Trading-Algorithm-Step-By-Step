# How To Automate Your Trading — With Zero Skills, For Free

> A step-by-step, from-scratch series on building a **real** trading algorithm.
> No gimmicks. No sales pitches. No BS. Just infrastructure, built in public.

| | |
|---|---|
| 📺 **EP 1 (watch first)** | [How To Automate Your Trading With Zero Skills FOR FREE — EP 1](https://www.youtube.com/watch?v=LxnP1T3Ep0U) |
| ▶️ **Channel** | [@fractalphive](https://www.youtube.com/@fractalphive) |
| 💻 **This repo** | the code, the configs, the checkpoints |
| 💬 **Community** | Discord — _link added when it goes live_ |
| 🤝 **Broker I use** | Alpaca — _affiliate link added once the partner program is approved_ |

---

## ⚠️ Read this first (it's the whole point)

**This is NOT financial advice. This is NOT a profitable algorithm. This is NOT a trading strategy.**

It's a guide showing you how to build the **infrastructure** for an increasingly complex trading algorithm — the plumbing that connects your code to a broker and places an order without falling over. The first build is Dollar-Cost-Averaging: "buy $X of Y every Z." No predictions, no signals, no "I'll make you rich."

If someone's promising you millions, they're selling you something. I'm showing you how the machine works so you can build your own. Everything that teaches is free.

---

## 🔗 Links — spread these around

This is the hub for the whole series. If you're pointing people somewhere, point them here.

- **Watch the series:** [@fractalphive on YouTube](https://www.youtube.com/@fractalphive)
- **Start at EP 1:** [Zero Skills, For Free — EP 1](https://www.youtube.com/watch?v=LxnP1T3Ep0U)
- **Clone the code:** `git clone https://github.com/fractalphive/Trading-Algorithm-Step-By-Step`
- **Join the build:** Discord — _coming soon_
- **Want the shortcut, not the lessons?** See [Free vs Paid](#-free-vs-paid-how-this-stays-honest) below.

> 📌 **Maintainers:** drop the live Discord invite and the Alpaca affiliate link into the two placeholders above once they're ready. Everything else is final.

---

## 📖 What this repo actually is

The repo from a YouTube channel where I build trading algorithms starting from literally nothing — a fresh machine with nothing installed, to code that clicks "run" and buys a stock automatically.

No course. No upsell wall. Here's the path from zero to your first automated (paper) order.

The code grows **episode by episode**. Each episode gets its own tag (`ep1`, `ep2`, …) so if you get stuck at Episode 5, you can `git checkout ep5` and diff against your own code. The history *is* the course.

---

## 🚀 15-minute quickstart (what EP 1 walks through)

You don't need to be a programmer. EP 1 starts on a brand-new machine and ends with a real (paper) order. The steps:

1. **Install Python** — the only real prerequisite. (Exact version noted in `requirements.txt` when it lands.)
2. **Install the bot's libraries** — `pip install -r requirements.txt` once the code is published.
3. **Open a broker paper account** — I use **Alpaca** (paper trading is free, no real money). Generate an API key + secret.
4. **Copy `.env.example` → `.env`** and paste your key/secret in. Your keys are yours — never paste them anywhere, including Issues or Discord.
5. **Edit `config.yaml`** — symbol, dollars per buy, schedule. Start in `dry_run: true`.
6. **Run it safe:** `python bot.py --dry-run` and confirm the output looks right before anything touches a broker.

> 🧪 **Paper trading is the default.** `dry_run: true` until you personally flip it. The bot should never touch real money unless you explicitly tell it to.

EP 1 already proved this works on camera — fresh VM, VS Code, Alpaca paper keys, AI-written code, a real paper SPY order submitted. You're following a path that's been run end to end.

---

## ⚙️ The config (so you don't have to build it)

When the code publishes, this is the whole thing you edit — the rest is plumbing:

```yaml
# symbol to buy
symbol: SPY
# dollars per buy
order_size: 50
# when to buy (market days)
schedule: "daily"        # daily | weekly | custom days
buy_time: "10:00"        # Eastern Time — always ET
# safety
max_daily_spend: 50
max_monthly_spend: 2000
# start safe
dry_run: true            # flip to false when you trust it
```

The learner version teaches *why* each line exists. If you'd rather just fill out the form and have it run tonight, that's the [Starter Pack](#4-the-done-version--starter-pack-3080-one-time) — same config, assembled for you.

---

## 🗺️ The series roadmap (where this is going)

The DCA series — from a fresh machine to a bot that buys on a schedule, in the cloud, with alerts and guardrails, running 24/7 for $0/month.

| Ep | What gets built | The checkpoint |
|----|-----------------|----------------|
| **1** | Fresh machine → the plan · repo skeleton · first runnable bot | `bot.py` connects and prints account value · [▶ Watch](https://www.youtube.com/watch?v=LxnP1T3Ep0U) |
| 2 | Dollars → shares · notional orders, fractional shares | A $50 paper order placed by code |
| 3 | The schedule · market-hours awareness · "run at 10:00 ET" | Bot buys at its scheduled time |
| 4 | Config & secrets · YAML + env vars · keys never in code | Zero hardcoded values; keys in `.env` |
| 5 | Memory · order log · idempotency | Run it twice → still only **one** order |
| 6 | Alerts · Discord/Telegram webhooks | Phone buzzes on every buy |
| 7 | Guardrails · spend caps, kill switch, retries | Kill switch halts the bot mid-flight |
| 8 | The cloud for $0 · GitHub Actions cron | Bot buys while the laptop is **off** |
| 9 | Watchtower · status page / heartbeat | Dashboard shows full order history |
| 10 | The 30-day paper run · results, what broke | LIVE month of automated buys, reviewed |

_Episode links get added here as each one drops. The repo tags `ep1`…`ep10` track them._

---

## 💸 Free vs Paid — how this stays honest

The question everyone asks: *"How do you charge for anything while teaching everything free?"*

**I sell the shortcut, not the knowledge.** Teaching shows you *how* and *why*. The products remove the *work* of doing it. People pay for time saved and outcomes — information is free everywhere (I literally use AI to write the code on camera, which proves it).

The litmus test I hold every product to:

> *"If someone watches every free video and takes notes perfectly, do they still get the full result?"*
> - **Yes** → fair convenience product ✅
> - **No** (withholding the actual lesson) → that's the guru move, brand breaks ❌

Everything below passes. The gurus fail it — their free content is a teaser that hides the method. This inverts it: the method is exhaustively free; I only charge where value scales with *my time*, or where you self-select as "I don't want to DIY."

### The five products

| # | Product | What you're actually buying | Price |
|---|---------|------------------------------|-------|
| 1 | **The series + this repo** | The journey (free, forever) | **Free** |
| 2 | **The Path** (build-along track) | The *order* through the free videos + checkpoints + error encyclopedia | one-time |
| 3 | **Cohort** (live, quarterly) | Live debugging, deadline, witnesses, demo day | $50–150 |
| 4 | **The "Done" Version** (Starter Pack) | The assembled thing — skip the build | $30–80 one-time |
| 5 | **Paid Discord** | My attention, with structure | $10/mo |

**The flywheel:** free videos → repo → free Discord (harvests errors, builds waitlist) → The Path ($) → Cohort ($$$ + testimonials) → Starter Pack ($) → Paid Discord ($/mo floor) → best questions become new free videos → repeat.

Free content isn't revenue given away — it's the most persuasive ad possible, costing only what I was already doing: building bots on camera.

---

## 🤝 How to support / get help

- **Stuck?** Wrong Python version? Hit an error? Ask in the Discord (link above) or open an Issue — *"Ask questions here, I answer the best ones in the next video"* is a pinned issue.
- **Building a broker account from the tutorial?** Using my Alpaca link (above) costs you nothing and throws a little support my way — and it's a tool I already use on camera.
- **Want it running tonight without the 40-hour build?** The Starter Pack is for you (see above). If the videos are all you need, they're all you need — no pressure, no funnel tricks.

---

## 📜 License & disclaimer

- **MIT licensed** — fork it, learn from it, ship your own.
- **Paper trading by default.** `dry_run: true` until you flip it yourself.
- **Your keys are yours.** Never paste them anywhere, including Issues or Discord.
- **Not financial advice.** Not a strategy. Not a prediction. The bot automates *execution* (schedules, alerts, orders); it never makes *predictions*. Weekly analysis videos are opinions; this repo is plumbing. Keep that wall absolute.
- **Trade at your own risk.** Automation amplifies both discipline and mistakes. Understand every line before you flip `dry_run` to `false`.
