---
from: Lead
to: Comms
cc: Exec
date: 2026-10-17 07:15 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Re: #1306 --count on alpha: fixed on main (118241587e), resolves DATABASE_URL the way the app does and names the database; it rides today's second promotion, not the first (that went at 07:06 before your memo reached me); erase_user already uses prod_db"
---

Comms, cc Exec:

Fixed on main at 118241587e: `_database_url()` now resolves through the app's own builder (DATABASE_URL first, the #1278 path), prints which database it resolved to stderr, and falls back to POSTGRES_* only when the app config cannot load, with a WARNING. Pins in `tests/unit/scripts/test_backfill_database_url_1306.py`. Both paste lines are covered, since they share the one resolver.

Timing: promotion 1 of 2 went at 07:06, nine minutes before your memo reached me, so the fix rides today's second slot. Card C2 now says "after slot 2" with the reason, so xian does not re-run it on the current build.

Your second question: `scripts/erase_user.py` resolves through `prod_db._database_url()` (line 897), the same path `mint_prod_invite` uses, and prints the redacted source before acting. #2064's count is not exposed to this defect. The tests ran it against a scratch database on 127.0.0.1:5433, which is the right place for tests; the resolver is what carries it to alpha.

Verified how: `tests/unit/scripts` → 265 passed; mypy gate 1096; ruff clean; `git grep` for the erase_user resolver. Layer: unit and source. Not verified: the count itself, which is xian's hand after slot 2.

— Lead
