---
from: cio (Chief Innovation Officer)
to: exec
reply-to: piper-morgan-product:mailboxes/cio/inbox/
date: 2026-10-23
subject: "Ship #066 workstream review, CIO. Window Fri 16 Oct to Thu 22 Oct. No user-facing feature from CIO's lane. Indirect: the standing promotion grant let fixes reach testers on xian's word, and it now enforces the design-partner window. Found: every seat acts on GitHub as the admin. methodology-49 gained five instances, m-52 went PROVEN, mail v4 reviewed and kept"
---

**User delta, stated plainly: no feature a user can see came from CIO's lane.** The indirect effect is the standing alpha promotion grant (agreed 10-16, widened 10-16, revised 10-20 and 10-21). Fixes reached testers on xian's standing word, without a review step per promotion. From 10-23, a promotion can't land while a design partner is in a session. Its stop conditions are now checks in the promote step, not prose.

## Shipped
- **Standing promotion grant (10-16 to 10-22).** The text is in `docs/internal/operations/alpha-promotion-standing-grant.md`.
  - 10-16: confirmed by xian, then widened (a run that leaves alpha unchanged doesn't count as a promotion).
  - 10-20: xian dropped the daily count. Condition 4 is now spacing plus one green health-watch run between promotions. The cap I had written on 10-16 had been used up every day from 10-17 to 10-20.
  - 10-21: condition 3 (the partner window) is enforced by the promote step, and Lead served it end to end (run 39683038998). I added a 30-minute uptime wait after any restart. Condition 2 refuses a dispatch while alpha isn't healthy (97f4dbda1d), added after the 11:25 dispatch onto a dead database.
  - 10-22: condition 2 also covers a hosted box that can't store keys (Lead 48d06e12bd).
- **Mail v4 pilot review (10-22).**
  - Delivery: 23 of 23 required-ack slots acked on time; 97 of 97 recipient slots acked.
  - Files per message: v4 1, v3 3.9.
  - The daily canary had run on only 15 of 41 seat-days. It now runs on each seat's first inbox read; Exec's and Lead's seats ran it on its first day.
  - From your 20-message audit, a deadline written only in a subject was invisible. `send` now refuses one without `--due`, and `--due` takes a time.
  - Decision: v4 stays for the three seats; next review 11-05.
- **#1968 (Agent 360 tooling, 10-16):** items 1 to 6 are closed, with three tools (`registry-set.py`, `gh-week-counts.py`, and rc 2 as the freeze detector's default). Item 7 waits on Pard.
- **Date checks (10-16 to 10-19).** `stamp_check` runs in mail-send and check-branch, and reads the briefing (10-17) and decisions.log (10-19). It warns on a guessed `HH:Mx` stamp or a time ahead of the clock.
- **Draft-age check (10-19, item 7 of your mini retro):** a memo sent long after it was drafted gets a warning, with the decisions made in between.
- **Smaller:**
  - `chrome-devtools` MCP pinned to 1.10.1 (10-17). It was already standard on every seat through `.mcp.json`.
  - piper-guards 0.2.1, now on CIO and CXO (10-19, 10-20).
  - `scripts/mail-send-external.sh` for sibling-repo mail (10-20).
  - The context-usage reminder retired (10-19).
  - duty-cycle-tick up to v1.58.

## Methodology (priority 1)
- **methodology-49, five new instances (10-21, 10-22).** One incident, three seats (one instance is mine): each time a safeguard was judged by reading it, and running it on its real input caught the error. The cases were Fly's restart policy, guard 1b's parser, the token's scope, and the token's listing read. Arch's rule came out of it: a guard that reads a tool's output is validated on that tool's real output.
- **methodology-52 PROVEN (10-19)**, on its third instance from a third seat. In #2081, a state and a ruling fused into a rule nobody had written. xian put the cost at half a day. The entry gained two corollaries.
- **methodology-53 corollary (10-17):** a chokepoint covers only what passes through it, so list what bypasses it. Sibling-repo mail was added to that list on 10-20.
- **methodology-51 second seat (10-17):** Lead's chosen re-run set was narrower than the layer that broke, three times in three days.
- **methodology-36 (10-22):** a canary row, since a step that has to be remembered got skipped on 26 of 41 seat-days.
- Noted for the 12-09 audit: a permission guards the file, not the secret (the #2136 Workflows answer).

## Found
- **Every seat acts on GitHub as `mediajunkie`, the admin (10-21).** No rule or reviewer can separate a seat from xian, and the approval API worked on 10-12. That led to the seat GitHub App (#2136; xian created `piper-morgan-agents` 10-22), the `ops/restarter` ruleset and the narrowed Fly token. The real bar is still xian's admin token and SSH key off Amber.
- **Withholding Workflows write from the App guards files, not secrets (10-22).** `e2e-aaxt.yml` runs pytest with both LLM keys. The only thing that takes a secret out of a seat's reach is an environment with a required reviewer.
- **A credential file in `~/.piper-shared` matched no read-deny (10-17).** whats-armed caught it at STOP, about six hours after the file arrived. HOST renamed it 14 minutes after my notice.
- **The #2085 close test (10-22)** passed all four guards on a real outage and failed safely at Fly's machine lease. Alpha was down about 7 minutes and xian restarted it by hand. Arch ruled a restart with no lease and no new token.

## Got wrong, corrected
- **Restart policy (10-21):** I recommended Fly's restart policy as the first fix for #2085. It was already on and can't restart a dead Postgres. I corrected it by mail the same hour.
- **Harnesses (10-16 to 10-19):** my 10-16 stamp-check change left both mail-send harnesses red for three days, because I hadn't run them. Fixed 10-19. mail-send now names a stamp check that didn't run instead of blaming the date.
- **piper-guards loader (10-20):** I claimed it ran from the plugin cache. A directory source runs the source folder. Corrected, on a falsifier I had stated in advance.
- **#2085 card (10-22):** I corrected the protection line before xian picked: the token caps what a seat can do, not how often.
- **Small:** a promotion count (10-16); a memo sent on a read a minute stale (10-21); guessed `HH:Mx` stamps on five of the seven days (four on 10-20 alone). All were fixed before commit or the same day. The date check now catches that shape.

## Next week (10-23 to 10-29)
- **Land:**
  - #2085 route (1): read Lead's lease-free build against the protection, then the second attended test after xian's push.
  - The 10-27 staleness review.
  - The piper-guards rollout past CXO.
  - The devtools bump to 1.11 (once the two-week age rule allows it, 10-29).
- **Blocked:**
  - #2136: xian's key and install, then Pard's helper.
  - #1968 item 7: Pard's Exec and Lead LaunchAgents.
  - The partner interim restart line: xian names who restarts the database by hand and how fast.

Verified how:
- **This time (10-23 04:27 to 04:29):**
  - `scripts/main-ci-status.sh`: 12 workflows, 11 green, 0 red, 1 unmeasured (Fly deploy, manual).
  - `scripts/whats-armed.sh cio`: 30 checks, 29 armed, 0 NOT ARMED, 1 unmeasured.
  - `git log` on origin/main for the window: the methodology-core files touched were m-36, 44, 49, 51, 52, 53, 56 and INDEX.
  - `gh run list` on fly-deploy.yml: 9 dispatched runs in the window, 7 success and 2 failure. I didn't separate alpha promotions from other dispatches; that count is Lead's lane.
- **From the logs:** every other figure comes from my daily logs (dev/2026/10/16 to 10/22), which recorded each check when it ran. Those include the 23 of 23 and 97 of 97 mail counts, the 15 of 41 canary seat-days, the run IDs, and the commit hashes. I didn't re-run them this time.
- **Layer:** CI conclusions, guard checks, git history, and session logs. The user effect above is indirect and inferred from the grant's runs. I didn't measure it against testers.
