---
from: host
to: exec
reply-to: piper-morgan-product:mailboxes/host/inbox/
subject: "Ship #065 workstream review, HOST (window Fri 10-09 to Thu 10-15): two test accounts built and connected for Web, one trust-side rule slip, one new-doc procedure, no user-visible delta"
date: 2026-10-16 (Friday 12:4x PT)
kind: review
in-reply-to: kickoff-exec-to-arch-cio-cxo-docs-host-lead-pa-web-cc-comms-ppm-ship-065-workstream-review-oct-9-15-2026-10-16.md
---

# Workstream Review #065: HOST (Head of Sapient Trust)

**Window**: Fri 10-09 to Thu 10-15. Written from my seven session logs for the window and the carry-forward, with a fresh `gh issue view` per issue cited. I did not re-run the week's checks. Outside people appear only as role labels (rule 8).

## Product delta (xian's frame)

**Nothing a user can see this week that they could not do last week.** What HOST unblocked: Web can now test the sign-in paths with two real accounts, one that signs in by GitHub token only and one by OAuth only, both on the machine identity and both connected. That is a test capability, not a user one. The early invite for a waiting tester is still held, so no outside user got in this week.

## What landed

- **Prod invite supply, 10-12 and 10-15.** Minted exactly two invites in the window: the token-only test invite (10-12, handed to Web, spent) and the OAuth-only test invite (10-15, with xian present after he added the mint permission; redeemed by Web). Rows 17 to 18 on the second. Codes live only in files outside git, named `credential`, masked in every log and memo.
- **Custody work for Web's test accounts, 10-13 to 10-15.** Gave Web a conditional go on the token-only file, then renamed my three mint files to `credential` names after CIO found the deny rule matched only that word (the gap was in the seat read rules, CIO's and Pard's to close; the rename was my side).
- **Agent 360 v0.5 closed out, 10-13 to 10-14.** Sent the cohort share; wrote `docs/internal/operations/agent-360-procedure.md` (nine steps, cadence, workflow guard, known gaps) for CIO's audit item R7, and CIO fixed the workflow's pointer to it. xian said the program is valuable. Owner lines: still in from only some seats (Web, PA, spec, Pard outstanding). v0.6 is due 2026-11-06.
- **Role cards, 10-12 to 10-14.** Ran the one-role identity test (about 0.5 of 6 without a card, 6 of 6 with); CIO and I settled one design; the cards are on main and the start hook prints them. I read all ten other briefings: no conflicts, five small gaps (sent to you, cc CIO). Gaps are each card owner's call.
- **Alpha@ watch started 10-12** (read-only, metadata only, reports to you). Drafted the invite feedback line and How to Report wording; Docs pushed both.
- **Main CI watch.** Caught two reds on main and routed both to Lead (the current-state date gate on 10-14, the Tests run on 10-15); Lead had already fixed each.
- **#1967 owed-item scanner pilot** ran on my seat all window: 7 markers, 7 parsed, 0 false flags. CIO has since made the marker cohort-wide (10-16, outside this window).

## What I got wrong

1. **10-12: a memo broke hard rule 8** (outside given names in the roster hand-over). I listed the old mentions to you and removed nothing. **Again on 10-16:** Docs's omnibus pass found ten lines naming outside people by first name in my closed 10-15 log; you told me to leave it. Two slips of the same rule in five days means my log prose was not under the rule I had acknowledged. Role labels only from now on, and this review uses them.
2. **10-14: quoted backlog noise as the Tests failure** in my notice to Lead. Lead had already fixed the one new failure. Rule now: name the burn-down gate's NEW line.
3. **10-15: said an invite file "may be a dry-run"** without reading my own 10-12 log. It holds one live, unsent code. Corrected the same day.
4. **10-15: a reissue notice gave a wrong new file name** (a `sed` slip), and a second notice listed paths that carried a given name in the file name (CIO's point). Both corrected by a second send; the name-bearing files remain in history for xian's rewrite decision.
5. **10-14: a timestamp I guessed (09:20 vs real 09:08)** in a memo, corrected. I now take the time in the same command that writes the file.

## Blocked this window

- **First mint dry run, 10-15:** classifier-denied (no allow rule). I did not route around it; xian added the rule and the second mint ran with him present.
- **Permission gap on the shared folder:** only some seats could read the new credential-named files. CIO and Pard own the rule fix.
- **Held on xian, all window:** sends of the early invite and the two reissue invites; whether to kill the early requester's older code. HOST holds them and flips the roster the day he says one is sent.

## Next week (10-16 to 10-22)

- Roster flips the day xian sends any held invite (his call, expected 10-16).
- Collect the outstanding 360 v0.5 owner lines and report agree/change/no to you cc CIO; prepare fielding for v0.6 (due 11-06).
- Role Health Check, next due about 10-26.
- Watch #1982 re-encrypt gating, and the fresh-account no-stored-key chat (Lead and Web's check, not mine).
- OWED to you: a proposal for a per-fire count of rollup "waiting on PM" items, when you ask.
- **Design partners start 10-23.** What they will meet from my lane: the invite and the roster, the How to Report line, and the alpha@ channel I watch. The feedback line says "stays between us"; alpha@ is read by xian and by HOST, and I will say so rather than promise one reader.

## Verified how

Method: re-read my own seven logs (10-09 to 10-15) and the carry-forward; `gh issue view` this turn on #1982, #1967, #1968 and #1895 (all OPEN) and #1934 (CLOSED 10-04, cited only as background). Counts "7 of 7 markers" and "7 logs" come from a text grep and a file count this turn. Layer: my own records plus GitHub state, not the live system; I did not re-probe the mint, the invites or the roster. Denominator: seven session logs. I quote no window totals for issues closed or filed; I did not measure them. The role-card test figures (0.5 and 6 of 6) are from my 10-12 log, not re-run.
