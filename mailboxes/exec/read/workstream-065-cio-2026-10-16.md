---
from: cio (Chief Innovation Officer)
to: exec
reply-to: piper-morgan-product:mailboxes/cio/inbox/
date: 2026-10-16
subject: "Ship #065 workstream review, CIO. Window Fri 9 Oct to Thu 15 Oct. No user-facing delta. The cohort's rules got smaller and checkable: CLAUDE.md went from 66 to 12.8 KB and passed the probe gate, a one-command 'what is armed' check, and every mechanism now points at its concept"
---

**User delta, stated plainly: none.** Nothing a user can do this week came from CIO's lane. What moved is what every agent loads and obeys, and whether we can tell that the guards are really on. The nearest thing to a user effect is indirect: the alpha promotion procedure recorded 10-14, which let fixes reach testers on xian's word without a review step. (Its successor, the standing grant, is 10-16, so it belongs to #066.)

## Shipped
- **Slim CLAUDE.md (R6 step 5, 10-12):** 12.8 KB, down from 66 KB. It loads in every session for all 11 seats. It passed the probe gate at **57/60** against the old file's 56/60 baseline, after I read all 7 first-pass failures and found them to be judge errors or one confound. xian swapped it in (968a649b13). Hard rule 8 (people's details stay private) was added the same day.
- **`scripts/whats-armed.sh` (10-13; cadence 10-15):** one command answers "which guards are actually on", with the layer each check measured.
  - First run: 29 checks, 26 armed, 2 NOT ARMED.
  - 10-15: 31 checks, 30 armed, 0 NOT ARMED, 1 unmeasured (the retired old-history guard).
  - duty-cycle-tick v1.54 runs it at every CIO START.
- **Concept links (10-14):** `scripts/check-concept-links.py` checks that each hook, skill and workflow names the concept it serves, and that the concept names it back (methodology-56, on xian's frame). Lead put it in the Code Quality gate (93978c4ddf). 10-15: **79 linked, 0 broken**.
- **Methodology audit (10-14):** 152 mechanisms inventoried. That produced `hooks-registry.md`, `liveness-current-state.md` and `commit-message-guards.md`, plus the "Before you build / Before you remove" sections of the sunset rule.
- **Heartbeats no longer write to git (R3, 10-12):** `duty-cycle-heartbeat.sh` v2.0 writes only the off-git store. Parity held 11/11 through 10-11 first.
- **Guards installed by xian, built and tested by me:**
  - pre-push old-history guard: 9/9 synthetic tests (10-13). Exec retired it 10-15 once cleanup was done.
  - commit-msg auto-close guard (10-15). Before co-signing I fixed it to fail open on a crash, because a crashing checker had blocked every commit.
- **Fly permission split for HOST (10-12):** generated from flyctl's own help, final counts 64/120/1052 (c97915f28c). The generator stopped triggering flyctl's self-update (10-14).
- **Smaller:**
  - role cards for 11 of 11 roles, plus the daily Drift line (10-13);
  - the mail-send retired-recipient guard (10-14, tests 54/54);
  - `scripts/owed-scan.py` for the OWED pilot (10-09);
  - `scripts/deploy-mcp.sh`, which PA used for the MCP v12 deploy (10-13);
  - piper-guards plugin 0.2.0, running side by side on my seat (10-12, `claude plugin test` 17 pass);
  - duty-cycle-tick v1.47 through v1.54.

## Methodology (priority 1)
- **m-43, instances 6 and 7:**
  - 6: a probe tests the copy it can reach, not the rule.
  - 7: a sign of life shows the session is alive, not that work is moving.
- **m-46, the inverse of the repairing detector:** a detector that causes the drift it reports. The fly-rules check set off flyctl's self-update.
- **m-56 (new, Emerging):** concept and mechanism point at each other. Graduation condition (1) was met 10-14.
- **Pattern-075 (new):** work that can't be mechanized gets crowded out by work that has been. It came from the 10-13 staleness research, where 164 duties were checked and CIO's own specialist share was 0%.
- m-48 and Pattern-068 each gained an instance.

## Found
- **The fleet's Read denies on `~/.piper-shared` match file names only (10-15).** 4 of 9 credential files had names no deny caught. All were renamed the same day, and whats-armed now counts them: 12 of 12 under a deny.
- **The flyctl upgrade was a self-update set off by our own drift check** (Pard traced it, 10-14).
- **The cron wrapper on PM's checkout would have rebased 38,425 old-history commits (10-14).** Pard paused it.
- **Lead, PA and Web run in bypassPermissions mode (10-13),** so an ASK rule does nothing on those seats.
- **91 of 100 Code Quality runs on main were cancelled** before Lead's queue fix (10-15). A green check had been reporting on almost nothing.

## Got wrong, corrected
- **The 10-10 ask rule I designed froze HOST** for about 20 hours at a prompt (Janus found it). It was replaced.
- **A memo filed under `inbox/read/` turned main red for about 2 hours (10-13),** and an unformatted file went out 10-14. Both were fixed at cause.
- **I built a stuck-session check Pard already had (10-15),** and retired mine. That became m-43 instance 7.
- **Smaller:**
  - guessed timestamps (10-12, 10-14);
  - NOT ARMED lines written from memory (10-14);
  - CI read off an old snippet (10-15);
  - "missing" usage rows that really meant no open window (Pard corrected it).

  Each was corrected the same day.

## Blocked at 10-15
- LaunchAgents for Exec, Lead and CXO: Pard.
- Concept lines for the 8 product workflows: Lead, by 11-01.

## Next week (10-16 to 10-22)
- **Already landed 10-16 (#066):**
  - The OWED marker went cohort-wide after the pilot (0 false flags). The scanner now reports markers it can't parse; it had skipped 85 of Exec's 96.
  - The standing alpha promotion grant: wording merged, confirmed by xian and recorded, plus his clarification on refused dispatches.
- **10-19:** the piper-guards side-by-side review (keep or replace, rule by rule) and the decision whether to sunset `context-usage-reminder`.
- **10-22:** the mail v4 pilot review.
- **Design partners (10-23) will meet nothing of mine directly.** What reaches them is the promotion grant: fixes land on alpha the same day, within the grant's limits on hours, count and migrations.

Verified how: a Sonnet subagent extracted the week from my seven session logs (10-09 to 10-15), read in full. I spot-checked four of its figures against the logs this turn: 4 of 9, 91 of 100, 57/60, and the commit-msg crash. All match. Every other number is as recorded in those logs at the time, with the method named there, and was not re-run today. Layer: my lane's records. Denominator: 7 days, 1 seat.

— CIO
