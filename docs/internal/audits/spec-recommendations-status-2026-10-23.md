# Spec's seven recommendations: where each stands (2026-10-23)

Exec, for xian. This page is the starting point for a conversational walk: we take the recommendations one at a time, between other work, until each is closed, dropped or given an owner and a date. Source: `docs/internal/audits/2026-10-spec-project-evaluation.md` (Spec, 10-03). The status is from a read-only check of the repo, decisions.log and GitHub this morning. I re-checked four of its claims myself.

**Bottom line.** Most of the cheap, safe steps are done: the security fixes, the slim CLAUDE.md, heartbeats out of git, the PM mailbox retired, and the key validator. What's left falls into three groups. Two are decisions only you can make. Several are steps nobody has started. Most metrics are due 11-03 and nobody is measuring them.

## The seven, one line each

| | Recommendation | Where it stands |
|---|---|---|
| **R1** | Decide when real users come, and remove the gates first | You ruled "after MVP". Today's checkpoint is that trigger. The wizard, key-check and feedback-page fixes are built. The metric is 3 outside people reaching a first useful session by 11-03, and it can't start until you approve invites. |
| **R2** | Make CI a real gate | Deploys and promotions now refuse untested code. The 14-day target (≥90% of main pushes green, due **tomorrow** 10-24) is **not met**: 83% over the last 14 days, not counting cancelled runs. Nobody has started the dependency audit (`pip-audit`, 457 advisories). |
| **R3** | Trim the coordination machinery | Heartbeats are out of git (done 10-12). The other steps have no visible work: cron to event triggers, merging watchers, a sunset date on each new mechanism. The bytes metric isn't measured. |
| **R4** | One PM channel | Mail to you is refused by the send script, and the rollup is your channel. The mail v4 pilot runs on three seats, with a review on 11-05. The 30,417 old mailbox files are still in the public repo. |
| **R5** | Security and public-repo hygiene | Items 1–4 are done: the leaked key was rotated, `?token=` and the fallback secret are gone, and commit messages are checked for credentials. Item 5 isn't: mailboxes (30,417 files) and `data/postgres` (2,119 files) are still tracked on public main. |
| **R6** | Slim the ruleset, carefully | Mostly done: the destructive-git guard, the slim CLAUDE.md (66 KB → 13 KB, after the probe suite passed), and CURRENT-STATE (now 9.5 KB). Two items are open. Nobody has re-measured load per fire since the swap, and the "fix the 50 defects" pass never ran. |
| **R7** | Decide the product surface; protect what works | You ruled (no single surface is the MVP), and the beta gate standard is ratified. Two are open: the Claude directory listing, held since 10-11 behind your revoke-then-ask test, and archiving the skunkworks repo. |

## What only you can decide (proposed walk order)

1. **R1: approve invites.** This is today's checkpoint question. Nothing more to add here.
2. **R5 item 5: take mailboxes and `data/postgres` out of the public repo?** This is the largest open exposure: memos mention outside people, and rule 8 covers new ones only. It is a project, not a click, because the mail tooling depends on the folder. Mail v4's private store is already half of the answer. My lean: yes, after the beta invites go out, with CIO costing it at the 11-05 mail review.
3. **R2: does "cancelled" count?** 156 of 347 main runs were cancelled because a newer push landed mid-run. Counting cancelled runs as failures gives 46%, and leaving them out gives 83%. Either way it misses 90%. My lean: leave them out, and let Lead own getting to 90% by a new date, since most reds came from Lead's pushes.
4. **R7: archive skunkworks?** The last push was 06-27, and the ruling left it conditional on PA no longer needing it. My lean: ask PA, then archive. It is reversible.
5. **R7: the directory listing.** It waits on your revoke-then-ask test. My lean: after beta opens, since MCP is a beta-period surface.

## Started by nobody (I'll find owners unless you say drop)

- R2: the dependency audit (`pip-audit`), the stale `test_multi_intent` tests, and the schema-drift validator: Lead.
- R3: steps 2–4 and the bytes metric: Exec with CIO. These are mine, and I hadn't moved them.
- R6: a token-load measurement after the swap: CIO.
- R1 step 4: the first-run issues list (the nav hidden in the avatar menu): CXO, to confirm whether it's still true.

## Verified how

A read-only Sonnet subagent checked 33 sub-steps and 7 metrics against decisions.log, commits, `gh issue view` and the tree on origin/main. I re-ran four of its claims: the file counts (`git ls-tree`: mailboxes 30,417, data/postgres 2,119), skunkworks `isArchived=false` (last push 06-27), commit `5d304e1d08`'s subject, and decisions.log line 2406 (R6 step 1). Several sub-steps came back UNKNOWN, with no evidence either way. I count those as not done until someone shows otherwise.
