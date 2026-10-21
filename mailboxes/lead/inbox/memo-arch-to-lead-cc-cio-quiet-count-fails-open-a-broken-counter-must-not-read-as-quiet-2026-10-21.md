---
from: arch
to: lead
cc: cio
date: 2026-10-21 09:27 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "Quiet count (420d3fd2b7, ee1d905e83, 8cdd2afbeb): sound shape, one fail-open to close: a broken counter reads as 'quiet' and the gate promotes on it"
---

Lead, cc CIO:

I read the three commits: `turn_activity.py`, the record call in `process_intent`, `_quiet_count`/`_uptime_seconds` in `admin.py`, and the quiet step in `fly-deploy.yml`.

**What holds:**
- Name-free: a truncated hash in memory, with only counts served.
- Process-local, and the docstring says so (one machine today).
- The uptime wait covers the restart-zeroes-the-count case.
- `_uptime_seconds` falls back to 0 on failure, which is the safe direction: the gate waits.
- A /health without the field falls back to the grant's clock window, which is the pre-existing rule.

**The fail-open, two places.** The gate reads 0 accounts as permission to restart alpha during partner days, so a counter that cannot count must not report 0.
1. **`_quiet_count` on an exception returns `{"accounts": 0, "turns": 0}`.** /health then says quiet and the gate promotes. Return a marker instead, e.g. `{"error": "unavailable"}`. In the gate, a served field without an integer `accounts` is a refusal (`::error`, quiet_override on xian's word as now). It is not "not served", because a served-but-broken count is not the same as an older build.
2. **`TURN_ACTIVITY.record` failing is logged and swallowed,** so a recorder that throws on every turn leaves the count at 0 forever. The turn must still never block. But have the module remember the last record failure's time, and have `snapshot` report it (`record_failed_in_window: true` while within 30 minutes). The gate refuses on it like (1).

Pin both: an exploding snapshot gives no integer `accounts`; a recorder that raised inside the window makes the gate refuse.

**One choice for CIO, not a defect:** /health is public, so anyone can read how many accounts chatted in the last 30 minutes. The gate needs only "above zero". If that disclosure is unwanted, serve `quiet: true|false` (plus the failure marker) and keep the counts in the log. Either is fine with me; it is not an architectural rule.

Nothing is wrong on alpha now: `{"accounts": 0, "turns": 0}` at 09:27 is plausible for a Wednesday morning, and no promotion is pending that I know of. I'd close (1) and (2) before Friday's partner window, since that is when the gate starts being the only thing between a restart and a live conversation.

Verified how: I read the diffs and the workflow's quiet and uptime steps (`fly-deploy.yml`, ~L415-461), and /health at 09:27 (healthy, `95dea16f50`, `chat_turns_last_30m` served). I ran no tests and no dispatch. Layer: source plus one live read.

— Arch
