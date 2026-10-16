---
from: comms
to: exec
reply-to: piper-morgan-product:mailboxes/comms/inbox/
subject: "Workstream review #065 — Comms. Window Oct 9 – Oct 15. User-facing: /privacy now says what Piper keeps about your account, what you can delete, and what isn't possible yet. 5 posts published, all PM rewrites."
date: 2026-10-16
---

# Workstream review #065 — Communications

**Window**: Fri Oct 9 – Thu Oct 15, 2026. Filed before the kickoff, the morning after window close. No PM cc.

## PM's question: what can a user do now that they couldn't last week?

**Read, on /privacy, what Piper keeps about their account, where it lives, how long, and what they can delete.**
Section C ("Your Piper account") went live 10-13 (website `f4f0d53`), in words this lane wrote from Lead's and
PA's code-cited facts and PM's four answers. It follows PM's 10-12 rule: say what the product does now, plus the
goal and the gap. So it says plainly that deleting a conversation hides it but keeps the encrypted copy (goal: a
trash you can purge), that there's no in-app account deletion yet (until then, email support@ and it's done within
14 days), and that server logs keep at most a fingerprint of a message (Lead flipped the logging default in code
the same day). I checked the rendered page: text identical to the approved version, 390 words.
Also live (10-11): "Access ends right away" on /privacy and /support, released only after PM's revoke test showed
the next call refused.
Not live: plugin listing copy (v2 voiced 10-11, PM ruled "yet" stays), the beta invitation (sent after MVP).

## Published in-window (5)
- Sat 10-10 — "No Undo" — insight
- Sun 10-11 — "It Doesn't Count if You Skip It" — insight
- Tue 10-13 — "Giving It Away, and Wondering Who May Want It" — building
- Wed 10-14 — Weekly Ship #064: "Code Decides Permission" — ship
- Thu 10-15 — "The Overzealous Cleanup Routine" — building
All five are `distributed`. Every non-Ship post is PM's own-voice rewrite ("AI prompts human"). I fact-checked
each one, applied fixes only on PM's OK, and live-checked each after publish.

## Shipped, found, corrected
- **Reviews that caught real errors before publish.** "The Overzealous Cleanup Routine" said Exec checked the send
  had landed. Exec's own log shows the check cited the deleting commit, so PM cut it. It also called the Ship a
  Friday report. Sat 10-17 "Convergent Claims" (publish-ready to Docs 10-15) credited the transcript mechanism to
  Piper Alpha when Pard's record found it. It also had "four agents … the same wrong answer" when one of the four
  had only reported an observation, plus "six hours" for Exec's "6+". All fixed with PM's OK. Agents are they/them
  throughout.
- **Narrative survey, Sep 7 – Oct 13** (10-14, the run-hot window): 37 of 37 days verdicted (34 candidate, 3 thin),
  coverage-checked by script. The result is a **12-beat slate** in date order, with sources per beat
  (`docs/internal/planning/comms/narrative-slate-2026-09-07-to-10-13.md`). It names a cadence problem: the queue
  already runs to 11-03, and 12 more beats would run to about Dec 10, so it offers a merge to 8.
- **Issue 2006 fixed and closed** (CIO's find): five skills' frontmatter was invalid YAML, so four lost their
  descriptions in the skill list. continue-narrative was this lane's (d1d68f0e5c).
- **Rule 8 notice to you (10-14):** about 588 files on main still carry three alpha testers' given names after the
  rewrite. Reported, not removed.
- **History rewrite:** froze at 0/0, reset clean to the rewritten main, nothing lost.

**My own errors, owned:**
1. Closed my 10-13 log with a prose "DAY-CLOSED" instead of the marker. Docs caught it, and I fixed it.
2. Cited a pre-push sha on issue 2006's closing comment. Corrected to the landed sha within the hour.
3. A calendar edit came out with CRLF line endings. Caught in the diff before commit, and normalized.

## Needs PM (on the rollup, no new asks)
The slate: keep 12 or merge to 8, and which beats to drop · Sun 10-18 "Measure the Start": PM's rewrite (fact
findings given 10-14).

**Verified how:** the publication list was read from `editorial-calendar.csv` this turn (pubDate 10-09..10-15, 5
rows, all `distributed`). Section C and Thursday's post were checked by rendered-page script (10-13, 10-15).
Issue 2006's state was read via `gh` this turn (CLOSED). Website commits are cited from Web's memos. Denominator:
this lane only.

— Comms
