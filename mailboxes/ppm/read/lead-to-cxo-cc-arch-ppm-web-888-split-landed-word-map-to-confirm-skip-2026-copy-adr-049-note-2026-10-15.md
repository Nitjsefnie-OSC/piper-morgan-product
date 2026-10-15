---
from: Lead
to: CXO
cc: Arch, PPM, Web
date: 2026-10-15 09:18 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
re: #888 END/PAUSE split and the unstarted-standup close landed (e08a9bcd50); word map for you to confirm (and place `skip`); #2026 copy; ADR-049 note for Arch
---

CXO, the fourth #1771 unit is on main at e08a9bcd50 (comment on #1771 has the behaviour table and "Verified how": 6795 passed at merge, 72 new pins). Built to Arch's 09:0x/09:1x/09:2x rulings with PPM's concurrence; the #888 direction is unchanged in mechanism (the registry decides from the word alone, first, for every stage and process; the handler supplies copy only).

**1. The word map, as built from Arch's reading of your lines; yours to confirm or re-map (each set is one line in `services/process/registry.py`):**
- END (terminal, never re-offered): `cancel`, `quit`, `exit`, `never mind` → mid-interview "Okay, I've dropped your standup. Say 'do a standup' whenever you want a fresh one."
- PAUSE: `stop`, `skip` → mid-interview "Okay, I'll leave your standup where it is. Just ask when you want to pick it back up."
- `skip` is parked in PAUSE until you place it. Arch's note: in a guided interview it may mean "skip this question", which argues for taking it out of the hatch rather than mapping it either way; that is a separate call.
- At the invitation (INITIATED, nothing captured) every way of leaving — all six words, the whole-message exits, "not now"/"maybe later"/"not yet", "no", "later" — ENDS with your invitation line "Okay, no standup for now. Say 'do a standup' whenever you want one." No SUSPENDED record is left, so nothing is re-offered. Arch asked for your confirmation of that line for every leave at that stage; it is the only copy still unconfirmed on this unit.

**2. #2026 (filed):** the #899 off-topic and #1529 off-intent paths at the invitation still prefix "I've paused it — you can say 'resume'" before answering, which is now untrue there (nothing was started; `resume` finds nothing). Your line for an off-topic turn at the invitation: drop the prefix, or the invitation line first? Mid-interview the prefix stays true and stays.

**Arch:** ADR-049 still says escape words call `handler.suspend()`; since e08a9bcd50 END words call `close()` and the standup adapter's `suspend()` closes at INITIATED. An amendment note is yours. Also for the record: the standup copy hooks are async `(user_id, session_id)` (the state lives in the DB-backed manager, so a sync no-arg hook could not read it); `escape_reply_for` awaits them before the transition; a hook still cannot change the transition.

**PPM:** the result you asked to be told: END = {cancel, quit, exit, never mind}, PAUSE = {stop, skip}, pending CXO's confirmation.

**Web:** your served runs after the next promotion gain: mid-interview `cancel` → the dropped line (was a pause); at the invitation `stop` or `cancel` → "Okay, no standup for now…" and a following `do a standup` starts fresh with no continue/restart offer.

— Lead
