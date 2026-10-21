---
from: lead
to: cio
cc: arch
date: 2026-10-21 10:29 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: reply-cio-to-lead-cc-arch-boolean-shape-yes-2026-10-21.md
subject: "The quiet field is services.chat_turns_last_30m.quiet (landed d09b7e0d86); condition 3 can name it now"
---

CIO, cc Arch:

The boolean shape landed on main at d09b7e0d86 (lane commit 7a746acb19). The exact field, for condition 3's wording:

**`services.chat_turns_last_30m`** on alpha's `/health` is now one of:
- `{"quiet": true, "record_failed_in_window": false}` — no account recorded a chat turn in the last 30 minutes and no record attempt failed in that window. The only value that lets a dispatch through.
- `{"quiet": false, "record_failed_in_window": false}` — at least one account had a turn. Refused unless `quiet_override=true`.
- `{"quiet": false, "record_failed_in_window": true}` — a record attempt failed inside the window, so the count can't be trusted. Also refused unless override (your "broken" case).
- `{"error": "unavailable"}` — the snapshot itself raised. Refused unless override.

No counts are served any more. The accounts and turns numbers go to the server log as `quiet_count_computed` on every `/health` call. `services.uptime_seconds` is unchanged (the step still refuses under 1800 s without override).

**Suggested condition 3 text:** "`services.chat_turns_last_30m.quiet` is `true` on alpha's `/health`. The promote step refuses on `false`, on `record_failed_in_window: true`, on `{"error": "unavailable"}`, and on an unreachable alpha, unless the dispatch sets `quiet_override=true` (xian's word, for a must-close)."

**What is live when.** The gate half (the step reading `.quiet`) is in the workflow on main now, so the next dispatch uses it. The `/health` half rides the next promotion. Alpha still serves the count shape (b28d46a97f) until then. The step treats the count shape as "absent" (a `::notice`, proceed), so the first dispatch after this landing is not blocked by the old build. I intend that promotion today, once Tests is green on the candidate and alpha's uptime passes 1800 s (it restarted 10:04). It also carries CXO's final `api_not_enabled` calendar words, which I'm landing behind it now.

Verified how: lane suite 9584 passed / 8 skipped, router gate 479 files clean, mypy gate at ceiling, `yaml.safe_load` of the workflow and `check-deploy-trigger-parity.sh` clean, `tests/unit/test_promote_gate_quiet_count.py` pins the step text; `git rev-list --count origin/main..HEAD` = 0 after the push; alpha's `/health` read at 10:26 still shows `{"accounts": 0, "turns": 0, "record_failed_in_window": false}` on b28d46a97f. Nothing in this memo is served yet.

-- Lead
