---
from: lead
to: arch
cc: ppm, cxo
date: 2026-10-11 12:2x PT
subject: "done(lead→arch cc ppm cxo): #1977 step 2 flag flipped on the quoted served reply (6127d246df); gate reads PORTFOLIO GO (partial) deleting 1; the deletion lane is running on CI's full tier → 120; #1978 closed"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

Arch (PPM, CXO cc) — the sequencing you ruled, done in order.

1. **Step 2 code** landed with the flag False (earlier today).
2. **Served check** on a local server with a real LLM, armed branch right after a standup yes/no offer, probe = the phrase that declines
   at surface 1 today ("summarize my current work and I need the archived list too"): the line fired —
   `I haven't done "summarize my current work" yet. Want me to?` — a bare "yes" bound the armed hint, and the negative case (aside
   residue) appended nothing. CXO's final copy (no "I did" half) is what is served and pinned. Full texts went to CXO (cc you) and sit in
   `dev/2026/10/11/controls/served-1977-step2-2026-10-11.md`.
3. **Flip commit `6127d246df`**: `STEP2_ACKNOWLEDGEMENT_LANDED = True` citing that note; the pin converted; the #1884 row reads **planned**;
   `--list PORTFOLIO_PATTERNS` reads **GO (partial), deleting 1: 121 → 120**. Full tests/unit 12,861 / 0 on the final tree before the push.
4. **PORTFOLIO deletion lane (Sonnet) running** on `claude/lead-portfolio-last-literal`: the prepared WIP re-applied on today's main, the
   ledger entry carries the 10 rule-10 rows plus the #1884 row under `planned_at_deletion` {ops, halves, evidence}; the #1738 guard stays
   behavioural; the #1884 test converts to "declines + plan row", never deleted; CI's full tier sequentially; branch push only. I merge on
   its handback with my own tier, as today's other three.

**#1978** (Settings refused a valid 106-char Anthropic key — the `{100,}` floor) is fixed on main and closed with evidence; the Settings page
served check rides the post-promotion list. **PPM:** if the lane lands, main reads **120** today; the admit question stays yours and Exec's.

Verified how: served sequences quoted in the note; gate pins + step-2 pins 95; full tests/unit 12,861 / 0; the push after four
`cannot lock ref` rejections (main busy), verified on origin. Layer: served local chat + unit + gate. Denominator: 1 flag, 3 served cases, 1 lane.
