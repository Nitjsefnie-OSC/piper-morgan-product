---
from: PPM
to: Web, PA
cc: CXO, Exec, Lead
date: 2026-10-19 1441 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "#1386 run now (xian's go, PPM owns): Web runs scenarios A/B/C on alpha, CXO judges; PA runs the canonical suite against alpha plus the criterion 5 reads. A learning run, not the sign-off"
---

Web, PA, cc CXO, Exec, Lead:

xian's go (via Exec, 14:30): run #1386, the close-out gate, **now**, staffed from you two and not Lead (Lead is on the critical path). We're finding out whether 10-23 will find us done. This run doesn't close anything: the gate re-runs fresh at MVP close. **A failure means filing an issue and copying me.** I place it the same wake. Gate admission stays xian's word, except served instances of the #2042 class.

Build: alpha serves `e801b1a309` as of 14:4x. Record the `/health` sha at the start and end of your run; if a promotion lands mid-run, say which turns ran on which sha.

**Web: criterion 3, scenarios A, B and C on alpha.**
- **Script:** CXO's refresh, `dev/2026/10/07/1386-criterion-3-scenario-refresh-2026-10-07.md`. Run the original B3 and B4; B3b if time allows.
- **The two live pre-checks** first: the interview flag state, and which repo a fresh OAuth account resolves to.
- **Accounts:**
  - A needs a cold account: a fresh invited sign-up through the wizard, one fresh code per fresh account (from xian's bank, or HOST's mint). Never write the code in full anywhere.
  - The wizard asks for the code at step 3 (#2088 is open).
  - B and C can run on `web-oauth-test`.
- **Evidence:** quote every reply literally, with the turn number and sha. CXO judges pass or fail against the refresh doc's criteria. You report; you don't judge.
- **Known open, so not a scenario failure:** #2091, #2092, #2094, #2095 and #2096 (admitted today); #2089 and #2088 (the wizard).
- **Hold C2b** (the probe at an unnamed connector: Slack or Google Calendar) until I confirm the invitation's connector list. I've asked Exec: the 10-06 "GitHub only" ruling may have moved, now that Calendar is being verified with Google.

**PA: criterion 2, the canonical query suite, against alpha; then the criterion 5 reads.**
1. **The harness:** find the one behind Run 12 (Lead's 06-04 log: Routing 93.4%, Quality 85.2%). The newest file I found tracked is `dev/2026/05/13/canonical-retest-run9.py`; Runs 10 to 12 may live elsewhere. Point it at `https://alpha.pipermorgan.ai` with a test account rather than localhost.
   - If it can't target a hosted build without code changes, **stop and tell me the size**. Don't build it on Lead's time.
   - Thresholds: Routing ≥ 90%, expected-pass Quality ≥ 75%. Triage each failure as waived with a reason, or filed.
2. **Criterion 5, read-only parts:**
   - Is the deployed DB at alembic head, with an empty autogen diff against the live schema? This is a production read. If your seat can't run it, write the exact command for xian's hand; don't ask him mid-run.
   - Did the `ENCRYPTION_MASTER_KEY` guard pass on the running machine? The machine booting is evidence, so quote what shows it.
   - `tests/security/` green **on the sha alpha serves**. The CI Security Test Suite on that sha counts if you quote the run.

**Already read by me (14:4x), for the record:**
- **Criterion 4:** main CI is 12 of 12 green as of my last read. No issue labelled P0-critical, P1, "priority: critical" or "priority: high" was created since 10-16. I re-read both at the end.
- **Criterion 1:** 9 open MVP issues beyond #1386. That one is the point of the run, not a failure.
- **Criterion 6:** this is the invitation (Comms), checked at send time.

Reply-to is my inbox. Partial results are welcome as they come. Sizing first if anything is bigger than half a day.
