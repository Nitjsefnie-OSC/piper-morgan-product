# Mail v4 pilot: Exec's 20-message recipient audit (2026-10-22 10:23 PT)

The pilot's independent check, asked by CIO (v4 01M5J9V13RYCMNAN32B82YZW57; review at dev/2026/10/22/mail-v4-pilot-review-2026-10-22.md, 1134d30564). Question: for 20 v4 messages, do the recipients' own session logs show they acted, not only acked?

**Who did what.** A Sonnet subagent pulled the sample and the evidence (read-only). I re-checked two rows myself (NDWA7Y in Lead's 10-15 log line 204, and the due fields of 9TMQT1 and 5WEEZC in the store) and wrote the findings.

## Result
- **18 of 21 recipient instances ACTED, 1 ACK-ONLY (the action had been done by someone else first), 2 needed no action, 0 NOT-FOUND.** Every recipient had a log for the dates searched.
- **Finding for the next review: a deadline written only in the subject is invisible to the ack metric.** Both freeze messages (9TMQT1, 5WEEZC, 10-13 22:43, "one reply by 23:00") carry requires_ack true but due null. The work was done by 22:44 (Lead's reply in the store at c392ede), but the acks came about 10 hours later (10-14 08:50 and 09:07). CIO's "23 of 23 acked before due" is correct by the field, but it couldn't have seen this lateness. That's my error as sender: I put the deadline in the subject, not in --due. Proposal: senders put any time-bound ask in --due, and check flags a subject that names a time with due null.
- **Channel attribution is weak.** Many asks also went by v3 ("also in v3"), and only 8 logs cite a mail4 id. So "acted" means the ask was acted on, not necessarily because of the v4 copy.
- **Coverage gap.** The ask-type pool has nothing dated 10-16 to 10-21, so the sample spans 10-08 to 10-15 only. Senders: exec 13, cio 6, lead 1. That's a gap in v4 use over the last week, not in the audit.

## Subagent's method and table (verbatim)

## Method
- Store: private repo piper-morgan-mail, local clone ~/Development/piper-morgan-mail. Read from the existing remote-tracking ref origin/main (no fetch): sha 938161fc20d8687987f8d297b3e6f960dd442b6e. (The clone's local `main` is behind at eb7c1f9a66; messages exist only on origin/main.) Layout: messages/YYYY/MM/DD/{ULID}.md with YAML frontmatter, acks/{role}.log.
- Denominators: 115 message files; 19 canaries; 96 non-canary (matches CIO's 95-96). Of the 96: 37 reply, 25 fyi, 18 task, 11 ruling-relay, 5 decision-request (types as counted over all 115 minus canaries: reply 37, fyi 25, task 18, ruling-relay 11, decision-request 5 = 96).
- Sample rule: pool = non-canary messages of type task / decision-request / ruling-relay (the "asks"), excluding self-addressed tests (from == to). Pool = 32. Sorted by ULID (= send time); took index floor(i*32/20) for i = 0..19. Deterministic; no cherry-picking.
- Sample coverage: sent 10-08 to 10-15 (the pool's 10-22 members, 2YZW57 (CIO's review mail itself) and the self-test CGTYN6, fell between sampled indexes or were excluded; nothing in the pool is dated 10-16..10-21). Senders: exec 13, cio 6, lead 1 (lead sent only one ask-type message in the pool). Recipient instances: 21 (NDWA7Y has to=lead, cc=cio): lead 9, exec 7, cio 5.
- Evidence: recipient session log dev/YYYY/MM/DD/*-{slug}-code-log.md on the send date and +2 days, searched by id, then subject/ask keywords. Ack timestamps from acks/*.log on origin/main. Commit hashes checked with `git cat-file -t` in this worktree (all resolve to commit).
- Limits: log text is self-report; I verified commit existence, not content. Logs for 3 days only per message.

## Table
| id (last 6) | sent | from -> to | ask | recipient verdict | evidence (file:line) |
|---|---|---|---|---|---|
| A9E3KT | 10-08 22:12 | cio -> exec | clone, read, ack the first v4 message | exec ACTED | 2026-10-08-0653-exec-code-log.md:195 "Mail wake: CIO's mail v4 pilot (first v4 message acked)"; ack 22:14 `done` |
| FHZZX5 | 10-08 22:45 | cio -> exec | 3 PM decisions D-E/F/G gating R6 | exec ACTED | same log:232 "mail4 decision-request ... surfaced to PM as item 8 in rollup v89"; ack `read` w/ note |
| H3NTNY | 10-12 08:48 | cio -> exec | decision for xian: adopt slim CLAUDE.md | exec ACTED (relayed to PM) | 2026-10-12-0608-exec-code-log.md:49 "...acked: adopt slim CLAUDE.md... Rollup v183, row 110. OWED[...to: xian]" |
| B6S1ZC | 10-12 09:25 | cio -> exec | confirm 3/3 readers on the store | exec ACTED | same log:58 "ran duty-cycle-freeze-check.sh (rc 0...) ... confirmed 3/3 to CIO by mail4 reply"; reply 9FDCHA exists |
| G9TTG8 | 10-12 14:34 | exec -> cio | write exact Fly JSON from xian-approved split | cio ACTED | 2026-10-12-0610-cio-code-log.md:143-145 "generated fly-permissions-host-2026-10-12.json ... (3bbbfc7c40)"; reply to Exec sent |
| ATBXRB | 10-13 13:33 | exec -> lead | write Tests-on-exact-sha check; report test-account steps | lead ACTED | 2026-10-13-0648-lead-code-log.md:277-278 "Landed 5e42a37c3b: promote-alpha gains a step..."; reply MFARD5; commit resolves |
| Z9CETP | 10-13 16:38 | exec -> lead | #1982 step 3: turn fallback off, fix --snapshot | lead ACTED | same log:322-323 "Landed 7cc00113bc ... GITHUB_LEGACY_CONTEXT_FALLBACK = False"; reply 79HAAG; commit resolves |
| 9TMQT1 | 10-13 22:43 | exec -> cio | FREEZE; one reply by 23:00 with 2 counts | cio ACTED | 2026-10-13-0623-cio-code-log.md:154-155 "Freeze (Exec, 22:43) ... replied once to Exec with both counts 0" (no v4 reply exists in store from cio; reply went another channel, not verifiable in v4); ack only next day 08:50 |
| 5WEEZC | 10-13 22:43 | exec -> lead | same freeze | lead ACTED | 2026-10-14-0647-lead-code-log.md:18 "one allowed reply sent by mail4 (...Q9S65N): status 0, ahead 0"; store commit c392ede 22:44:53; ack only 10-14 09:07 |
| 9R6ZT5 | 10-14 08:44 | exec -> lead | RESET to origin/main, reply 'reset to <sha>' | lead ACTED | same log:24 "RESET (Exec 08:43) ... git reset --keep origin/main -> 25d96342a1. Reply 'reset to'" |
| 9B9995 | 10-14 09:03 | cio -> exec | decision for xian: watchdog pull --rebase hazard before 12:46 | exec ACTED | 2026-10-14-0845-exec-code-log.md:38-39 and :48 "xian reset his checkout ... Told CIO ... 12:46 watchdog safe" |
| ZV2MPM | 10-14 09:26 | exec -> lead | low priority: untrack data/chromadb | lead ACTED | 2026-10-14-0647-lead-code-log.md:48-52 "Shape chosen: git rm -r --cached data/chromadb + .gitignore"; commit 7a498b2aec resolves |
| 71AT1Q | 10-14 09:38 | exec -> lead | FYI ruling: chromadb untrack now optional | lead NO-ACTION-NEEDED | same log:57 notes "Exec v4 (chromadb fine; xian's ...)" |
| JK32J2 | 10-14 10:34 | exec -> cio | relay of xian's approval of methodology audit | cio ACTED | 2026-10-14-0905-cio-code-log.md:84-85 "xian 'emphatically approved'; concept-link checker" |
| 1D8W14 | 10-14 10:36 | exec -> lead | run hot until 10-15 22:00; ask for bigger model if needed | lead ACTED | same lead log:83 "MAIL WAKE: xian's run-hot ruling ... Told Exec ... no model ask" |
| Z38Q7W | 10-14 11:11 | lead -> exec | for xian's card: spare Anthropic key for web-agent | exec ACTED (indirect) | 2026-10-14-0845-exec-code-log.md:143 "wake: Web (... ask: spare Anthropic key) ... Rollup v272: Web's fourth ask". Log attributes the ask to Web's memo, Lead's message not named; same ask |
| 17RY98 | 10-14 16:09 | cio -> exec | is R4(a) soak trigger met? | exec ACTED | same exec log:178-184 "Half 2 ... fixed scripts/check-unboarded-pm-items.sh ... Told CIO both halves are met"; reply ZDS9GZ |
| NDWA7Y | 10-15 13:21 | exec -> lead, cc cio | ruling relay: Lead to force-remove two worktrees | lead ACK-ONLY (action preempted) | 2026-10-15-0641-lead-code-log.md:204 "xian OK'd the force-remove ...; Exec ran both worktree remove --force ... himself at 15:33 ... nothing left for me". Lead was on a permission prompt 12:43-15:30; ack 15:35 |
| NDWA7Y | (cc) | | | cio NO-ACTION-NEEDED (cc) | 2026-10-15-1007-cio-code-log.md:43 "8s DONE: xian installed the commit-msg hook; force-removes approved (Lead's to run)"; acked 13:25 |
| PKJR9B | 10-15 15:33 | exec -> cio | stuck-session check proposal | cio ACTED | same cio log:92-103 "built scripts/stuck-session-check.py ... Retired mine (git rm, 6e89a21cd9) ... Pard's alert already live"; ack `done` 15:55; commit resolves |
| ERR61R | 10-15 18:39 | exec -> lead | redirect-secrets audit addendum: aim at PIPER_BASE_URL | lead ACTED | 2026-10-15-0641-lead-code-log.md:341-344 "Redirect-secrets audit (Exec's task + addendum...)"; follow-on #2043 landed 10-16 (lead-2043 branch, commits 37ca9753b5/8ca329e69e resolve) |

## Totals (21 recipient instances over 20 messages)
- ACTED: 18
- ACK-ONLY: 1
- NO-ACTION-NEEDED: 2 (one is a cc, one an "optional" ruling relay)
- NOT-FOUND: 0
- All 20 messages had a recipient log entry; no recipient log was missing for the dates searched.

## Notable non-clean cases
- NDWA7Y / lead (ACK-ONLY): log shows receipt and says Exec did the removal first (15:33 vs ack 15:35). Looked at lead 10-15 log lines 197, 203-204 and the 10-16 log (no force-remove entries). Not a delivery failure; the 2h-14m delay was Lead's session stuck on a permission prompt (PKJR9B text).
- Z38Q7W / exec (ACTED, indirect): the Exec log credits the spare-key ask to Web's memo; I found no line naming Lead's v4 message. The ask did reach the rollup.
- 9TMQT1 / cio: log says CIO replied at 22:44, but no cio->exec v4 reply exists in the store that night (Lead's reply c392ede does). Either v3 or unverified. Both freeze messages were acked only 10-14 08:50/09:07 (about 10 h after send), i.e. act-before-ack: the acts were done in time, the acks lagged. A delivery metric on acks would score these as late although the work happened on time.
- Two caveats on the method: (1) sample is ask-type only, so it overstates action rate relative to all 96 (fyi/reply need no action); (2) heavy overlap with v3 copies ("also in v3") means some action may have been prompted by the v3 copy rather than the v4 message; logs rarely say which channel (the logs that do cite mail4 ids: A9E3KT, H3NTNY, B6S1ZC, ATBXRB, Z9CETP, 17RY98, G9TTG8, 5WEEZC reply).
