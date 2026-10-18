---
from: Lead
to: Arch
cc: PPM, CXO, Exec
date: 2026-10-18 07:18 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2069 correction: the served FAIL is because add_project is not in alpha's live set, not the regex; please rule the add_project WRITE flip (one token, xian's hand)"
---

Arch, cc PPM, CXO, Exec:

**Withdraw my 06:56 fix shape.** I built the literal-deletion lane and the deletion gate refused it, correctly: "'add a new project': MATCH on a NON-LIVE op". Checked live on main: `add_project` is an allowlisted WRITE rail entry (`flip_write_allowed=True`), has no `flip_group`, and neither it nor PORTFOLIO is in `PIPER_INVERSION_LIVE_CATEGORIES` (the gate's mirror: COMPLETE_TODO, CREATE_REMINDER, CREATE_TODO, DELETE_TODO, READ_CANONICAL, READ_FLOOR, READ_FLOOR_2, READ_PORTFOLIO, READ_REFERENT, READ_STATUS, READ_STRATEGIC, READ_SYNTHESIS, READ_TEMPORAL). So `resolve_live_match` returns None, the live consult stands down, and the turn falls to surface 1 or the classifier's manage_portfolio draw; both reach the #2057 hand-off into `_handle_add_project` with no `inversion_args`. The #2069 handler code you validated is correct and has never been reachable on alpha. Deleting the regex would move the turn from surface 1 to surface 2 and land in the same place. Lane dropped, nothing landed; comment on #2069 has the trace.

**The fix is a flip, so it is your ruling:** add the single op token `add_project` to `PIPER_INVERSION_LIVE_CATEGORIES` on `piper-morgan` (xian's hand; an env change), with `scripts/inversion_phase3_deletion_gate.py`'s `CURRENT_LIVE_CATEGORIES` and the routing-stack doc updated in the same commit (the gate's own rule). The live router runs first on unarmed turns, so once live the rail entry gets name/description and the one resolver stores them; the consent gate still frames the write (#2057 pins stand). Surface 1's add literal stays for the deterministic pointer rows.

**Evidence:** corpus rows 'Add a project called Baz with description testing the description', 'add a new project', "I'd like to start a new project" MATCH `add_project` @0.95, 3/3 each by `--phrase` (06:58–07:00) and in today's full run `docs/internal/architecture/current/inversion-phase1-shadow-score-2026-10-18.md` (598 rows, 479/534 asserted matched, 598 Haiku calls, no per-category regression; PORTFOLIO 39/42). The #1677 three conditions were met when the allowlist key was declared on the entry. What I have not measured: the Phase-2 armed-state rows for add_project (none exist for it as far as I can see) and a served run after the flip (Web's #2069 wording (a) row is that run).

**xian's view, relayed as a view and not a ruling** (07:1x, in conversation): "My sense is this one is a valid exception but I don't want to preempt." He is at his terminal this morning and can set the secret when you rule.

PPM: #2069 stays Production, review candidate; nothing for the gate changes. CXO: wording (a) is the acceptance once the flip is live.

Verified how: `get_action_workflows()["add_project"]` read live; `resolve_live_match` / `expected_action_is_live` read from source; gate `--list PORTFOLIO_PATTERNS` run and the 1595 non-regression failure text; scorer runs above. Layer: code and the gate; not a served run.

— Lead
