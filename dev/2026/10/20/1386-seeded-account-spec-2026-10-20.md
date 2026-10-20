# #1386 criterion 2: the seeded account for the re-measure (PA's spec)

**Asked by:** PPM's ruling on #1386 (comment 6300067304, step 4; order restated 10-20 16:08). The run is on "a seeded account shaped like a partner after setup: GitHub with issues, PRs and commits, Calendar with events this week". It's one run, after Lead's lane fixes (#2119, #2120, #2112's floor clause), before 10-23. The measurement is frozen (harness `f7ae6f66a4`, effect reading with `UNWIRED_EXECUTION_READS_ACTION` on).

**Derived from:** the 12:27 run's 31 "Absent" answers (honest "nothing there"). Each seed item below names the canonical queries it feeds. A query not listed answers the same on any account.

## 1. A fresh account, not `web-oauth-test`

That account has run the canonical script four times today, and it remembers. Q9, Q10, Q14 and Q23 answered "Still…" or "three times in", and Q5 said "five times is a pattern". A partner's first run has no such history.

- **Make it through the wizard.** One fresh invite from HOST, on xian's word: HOST's 15:51 memo, already with Exec for #2117. **The same invite serves #2117's served row**: Web quotes the key step ("Key accepted.") while creating this account. One invite, two closes.
- **Stored LLM key:** the test workspace key (`piper-morgan-test`, $20 cap). Three canonical runs plus the shadows spent about $10 today; the shadows are off now. One run fits.
- **Never run anything else on it before the measure.** Seeding happens through GitHub, Calendar and the UI, not through chat turns that would enter its history. The exceptions are the chat-only seeds in step 4, which must not repeat any canonical phrasing.

## 2. GitHub: the test repo needs content (it has almost none)

`dinp-machine/piper-test-activity` (public; read 10-20 16:1x): 1 commit (10-15), **0 PRs, 0 milestones**, 9 open issues titled "test issue 1–9". The account connects to it by OAuth as `dinp-machine`, as scenario A did.

| Seed | Feeds |
|---|---|
| A milestone "Beta launch", due about 10-30, with 4 of the open issues assigned to it (one labelled `blocked`) | Q25 next milestone, Q43 blocking the milestone, Q52 on track |
| Real titles on 5–6 open issues (e.g. "Login page times out on slow networks"); leave the rest | Q41, Q45, the standup, priorities |
| 3–5 commits this week, small README or docs edits | Q19 status report (#2119), Q51 productivity, Q53 sprint |
| 2 open PRs (one ready, one draft) | Q42 stale PRs: none can be stale before 10-27 (7-day threshold, `intent_service.py:6571`). The honest answer is "2 open, none stale". |
| 1 PR merged and 2 issues closed this week | Q41 shipped this week |

**Who:** whoever holds a write credential for `dinp-machine` (unverified: HOST to name; PA holds none). The issue writes could go through Piper's own chat, but that puts turns in the account's history, so use GitHub directly.

**Not seedable:** Q58 "Update issue #123", Q59 "Comment on issue #456", Q60 "Review issue #789". The repo stops at #26. They stay known-pathological. With #2111 fixed, Q60 tests the honest "not found" line, which is a fair test.

## 3. Google Calendar: connected, with events this week

| Seed | Feeds |
|---|---|
| Calendar connected through Settings on this account | Q8, Q34, Q35, Q61 (all "isn't connected" today); Q33 and Q62 (#2112) |
| A recurring weekly team meeting, two 1:1s, two events that overlap on one day, and a free afternoon | Q34 time in meetings, Q35 recurring, Q61 week, Q62 conflicts, Q33 find time |

**Who:** a Google account that can be connected as a test user. That's xian's (Lead's `ee952c73eb` notice: "the connected-calendar row is xian's account (Exec)"). Unverified whether a separate test Google account exists. If none does, the calendar half of the seed waits on xian, and the run reports those rows as unseeded rather than skipping them.

## 4. Piper-side data, through the UI

| Seed | Feeds |
|---|---|
| A project "Piper Test Activity" linked to the repo (My Projects, not chat) | Q11, Q12, Q13, Q14, Q18, Q10, Q53 |
| 3 todos, 1 done (todos page, if it has one; else chat with non-canonical phrasing) | Q21, Q30, Q51, Q55, Q56 |

**Not seedable by design:** Notion and Slack aren't beta connectors (#1386 criterion 6). Q20, Q40, Q46, Q47 and Q48 stay honest declines. Insights (Q22) and composted patterns need days of use; they stay Absent.

## 5. Before the run (PA)

- `/health` names the build with Lead's fixes, and `loop_watchdog` reads `running`.
- The streams are on.
- One GitHub REST read confirms the milestone, the PRs and this week's commits.
- Web confirms the calendar shows the week's events in Settings → Test.
- The harness runs with `PIPER_CRED_FILE` pointing at the new account's `-credential-` file (HOST's 10-19 ruling: read by path, never printed).

Verified how: the 12:27 CSV's 31 Absent rows read; the repo read through the public GitHub API (`repos`, `pulls`, `milestones`, `commits`, `issues`); the stale threshold read on main. Unverified: who holds `dinp-machine` write access, and whether a test Google account exists.
