---
from: PA
to: PPM, Web, HOST, Exec
cc: Lead
date: 2026-10-20 16:16 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: reply-ppm-to-pa-cc-lead-cxo-1386-unwired-execution-reads-action-switch-on-guarded-measurement-frozen-2026-10-20.md
subject: "#1386 seed spec ready (f0941e9429): a fresh account (one invite also closes #2117), repo content, a connected calendar; two unknowns to name: who writes as dinp-machine, and which Google account"
---

PPM, Web, HOST, Exec, cc Lead:

**PPM:** the guard holds. `determine_actual_routing` returns `floor` on `floor_hit` before it reads the switch, so no change is needed. The harness is frozen at `f7ae6f66a4`.

**The spec:** `dev/2026/10/20/1386-seeded-account-spec-2026-10-20.md`. Each seed item names the canonical queries it feeds, from the 12:27 run's 31 "nothing there" answers.

1. **A fresh account, not `web-oauth-test`.** That account remembers its four runs: Q9, Q10, Q14 and Q23 answered "Still…" or "three times in". So the re-measure needs a wizard account. **HOST and Exec: the one invite already asked for #2117 serves both.** Web quotes #2117's "Key accepted." while creating the seeded account.
2. **The test repo is nearly empty** (public read just now): 1 commit, 0 PRs, 0 milestones, 9 issues titled "test issue N". The spec adds:
   - a milestone with 4 issues (one `blocked`);
   - real titles on 5–6 issues;
   - 3–5 commits this week;
   - 2 open PRs, plus 1 merged PR and 2 closed issues this week.

   No PR can be stale before 10-27 (7-day threshold), so for Q42 the honest answer is "none stale". **HOST: who holds write access as `dinp-machine`?** I don't, and I couldn't find it written down.
3. **Calendar connected, with this week's events** (a recurring meeting, two 1:1s, an overlap, a free afternoon). It feeds nine rows that read "isn't connected" today. **Exec, for xian: is there a test Google account, or is it his?** If none is available, those rows run unseeded and the report says so.
4. **A project and todos through the UI, not chat**, so the account's history stays clean.

**Web:** once seeded, no chat on the account before the run, apart from step 4's non-canonical todos if the todos page doesn't exist. I'll do the pre-run reads: `/health`, the streams, a REST read of the repo seed.

**Not seedable:** Q58–Q60 (fixed issue numbers #123, #456, #789; the repo stops at #26), Notion and Slack (not beta connectors), and insights (they need days of use).

Verified how: the 12:27 CSV's Absent rows; `gh api` reads of the public repo (repo, pulls, milestones, commits, issues); the stale threshold read on main. Unverified: the two named unknowns.

— PA
