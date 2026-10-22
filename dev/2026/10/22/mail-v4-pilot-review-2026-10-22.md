# Mail v4 pilot review (2026-10-22)

**Reviewer**: CIO (mechanism owner). **Written**: 2026-10-22 10:15 PDT. **Pilot**: exec and cio from 10-08, lead from 10-12.
**Criteria**: `docs/internal/operations/mail-v4-pilot.md`, "Success and stop criteria".

## Verdict

Delivery worked: no required-ack message was missed or late. The daily canary did not run as specified,
and Exec's 20-message audit, the one independent check, has not been done. Recommendation: keep v4 for
the three pilot seats; do not widen it until Exec's audit is in and the canaries have run every day for
a week under the fix below. Widening is xian's call (to Exec).

## Criteria, one by one

| Criterion | Result | Verified how |
|---|---|---|
| Zero missed required-ack messages (Exec's 20-message audit) | **Not run.** My backstop: 23 of 23 required-ack recipient slots acked, 0 after their due time; 97 of 97 recipient slots acked at all | Script over every message file and `acks/*.log` on piper-morgan-mail origin/main (95 non-canary messages). Layer: the ack log, not whether the recipient acted. That is what Exec's audit checks, so mine does not replace it |
| All 14 daily canaries pass | **Fail: not run.** 15 of 41 seat-days had one: CIO 9 of 15, Exec 3 of 15 (none after 10-10), Lead 3 of 11 (none after 10-14). All 18 that ran passed | Canary message dates per sender on origin/main; ack `done` present for 18 of 18 |
| At least 60% fewer files per message | **Pass.** v4 is 1 file per message. v3 averaged 3.9 new files per memo (1,808 commits since 10-08 that added mail), plus a move to `read/` per recipient | `git show -M --name-status` over every `mail(` commit on main since 10-08 (3,212 commits; 1,808 add files) |
| Inbox read cost no higher than v3 | **Pass on what a seat reads; slower on the clock.** `inbox` prints one summary line plus one line per open message. It takes 2.4 s against 0.003 s for `ls`, because it fetches. v3 needs a fetch too before `ls` means anything | `time` on both, CIO seat, this morning |
| No confusion reported | **Pass.** No log of the three seats reports a misrouted or misread v4 message | grep of exec, lead and cio logs 10-08 to 10-22 for mail4/v4 with refused, wrong, missed, stale, confus |
| Stop: a decision request overdue without `check` flagging it | **Not triggered; now tested.** None went overdue in real traffic, so I sent one to myself due 10-20: `check` listed it OVERDUE and exited 1; after the ack it read 0 and exited 0 | Message 01M5J9MSC8QPH2N8T3XZCGTYN6, acked declined |
| Stop: any false all-clear | **None found** | `check` always prints its denominator; no log quotes a bare "clear" from it |

Traffic: 95 messages (37 reply, 25 fyi, 17 task, 11 ruling-relay, 4 decision-request; one is today's test). Most were cio↔exec (51) and exec↔lead (29).

## What changed today

- **The canary is no longer a step to remember.** The first `mail4.py inbox` of the day, by the seat itself, runs it (not in `--ids` mode, so Pard's watcher doesn't). `check` now names any pilot seat with no canary today. Skill v1.58. This is methodology-36 (mechanisms over vigilance): the step was written down at 10-08 and decayed in every seat within a week.
- **Known limit closed:** v4 mail does wake its recipient. Pard's `mail-wake.py` reads `mail4.py inbox --ids` (mediajunkie `scripts/mail-wake.py`, `mail4_ids`); CIO's log 10-16 11:14 records a v4 mail wake. The ops doc is updated.

## Watch items carried in

- **Stamps.** v4 writes `sent_at` itself, so the guessed-header-time class cannot happen in v4. In v3 it still does: `stamp_check` only warns on an `HH:Mx` near now, and some went out 10-21. Times inside a body are free text in both systems.
- **Stale reads.** My 10-21 evening memo (v3, to Exec; corrected at 18:38) told xian a branch policy used a hyphen, from a read a minute older than his change back to the slash. Neither mail system checks what a memo asserts, and should not try; the habit is to re-read a value in the same minute you report it. Recorded here because it was on the review list, not as a v4 finding.

## Open

- Exec: the 20-message audit (owed since the pilot started; Exec's half per the 10-03 ruling).
- Next review: 2026-11-05, on Exec's audit and a week of canaries.
