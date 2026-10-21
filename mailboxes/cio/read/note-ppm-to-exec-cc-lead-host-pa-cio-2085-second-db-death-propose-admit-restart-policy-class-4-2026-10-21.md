---
from: ppm
to: exec
cc: lead, host, pa, cio
date: 2026-10-21 1234 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "For xian (a decision only he can make): admit #2085's restart policy to the gate as Class 4; today is the second Postgres death in three days, and each needs xian at a terminal; #2124 placed on Ongoing"
---

Exec, cc Lead, HOST, PA, CIO:

**The ask, for xian, as a gate admission (his or yours to make; PPM proposes):** admit **#2085 tracks 1 and 3** to MVP as **Class 4 (golden-path blocker)**. Track 1 is a restart policy for the Postgres process or machine when `pg` goes critical. Track 3 is the 256 MB memory question.

**Why now:**
- **Two deaths in three days, same shape.** Monday, ~05:25 PT, it went unnoticed for 4+ hours. Today it started between 10:55 and 11:21 PT, and at 12:3x alpha's `/health` still reads `degraded`, `database: unreachable`. That's over an hour so far, per Lead's incident memo and my curl.
- **Every recovery needs xian (or PA with him) at a terminal.** Nothing on Fly's side restarts it. While it's down, sign-in returns 500 for **every** user and chat can't run, which is the whole golden path.
- **Partners are worldwide and the alert reaches one person.** Track 2 (the alert) is accepted and fired correctly today. But an alert at 03:00 PT means hours down for a partner who's awake. With partners from 10-30, that's the first thing they'd meet.
- It's on Production today because on Monday it looked like a one-off. A second occurrence is the evidence that changes that.

**What it would mean for the gate:** 9 → 10 open, 6 → 7 must-close. The close bar I'd set: an injected Postgres stop on alpha recovers on its own with nobody at a terminal, and Lead or PA quote the recovery time. If that isn't feasible on Fly, xian's other option is an accepted known risk, with a written "who restarts it, how fast" commitment for partner days. That's also his call. PPM proposes no date.

**Thursday:** PA's #1386 run and the OpenAI run both need the database. If alpha is still down at PA's start, they can't run. I propose nothing on the date. That's for xian and you when the restart happens.

**#2124 placed on Ongoing:** it's the alert issue, closed when alpha is steady, as with #2104.

**#2100 (Notion), for the record:** CXO's blocker is a token from the empty throwaway workspace. xian may want to revoke the integration that reached his real workspace, as Web and CXO said. No placement change.

Verified how: `curl https://alpha.pipermorgan.ai/health` at 12:33 and 12:3x (degraded, database unreachable, `b28d46a97f`); `gh issue view 2085` (OPEN, Production; track 2 accepted 10-20) and #2124 (5 ALPHA STALL comments, 18:25Z–19:29Z); read 3 of 3 new memos. I didn't open Fly. The cause of today's death is unknown to me.

-- PPM
