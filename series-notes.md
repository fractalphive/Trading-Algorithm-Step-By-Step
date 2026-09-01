# Series notes — master index

One line per episode. Update as the series progresses.

| # | Slug | Title | Video | Status |
|---|------|-------|-------|--------|
| 1 | [ep01-fresh-start](episodes/ep01-fresh-start/) | Connect & print account value | [EP 1](https://www.youtube.com/watch?v=LxnP1T3Ep0U) | ✅ live |
| 2 | _(planned)_ | Dollars → shares | — | ⬜ planned |
| 3 | _(planned)_ | The schedule (market hours) | — | ⬜ planned |
| 4 | _(planned)_ | Config & secrets | — | ⬜ planned |
| 5 | _(planned)_ | Memory / order log / idempotency | — | ⬜ planned |
| 6 | _(planned)_ | Alerts (Discord/Telegram) | — | ⬜ planned |
| 7 | _(planned)_ | Guardrails / kill switch | — | ⬜ planned |
| 8 | _(planned)_ | The cloud for $0 | — | ⬜ planned |
| 9 | _(planned)_ | Watchtower / status page | — | ⬜ planned |
| 10 | _(planned)_ | 30-day paper run | — | ⬜ planned |

**Legend:** ✅ live · 🎬 recorded · ⬜ planned

## How to add an episode

1. `cp -r episodes/_template episodes/epNN-slug`
2. Build the bot; log commands to `commands.md` as you go.
3. At episode end: save `bot.py`, export chat → `chat/chat-history.md`, fill `README.md`.
4. Commit: `git commit -m "epNN: <what was built>"`
5. Tag: `git tag epNN`
6. `git push && git push --tags`
7. Add one line to the table above.
