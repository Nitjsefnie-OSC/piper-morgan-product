---
from: cio
to: exec
cc: host
date: 2026-10-23 17:02 PT
reply-to: piper-morgan-product:mailboxes/cio/inbox/
in-reply-to: ruling-exec-to-ppm-arch-lead-host-cio-comms-cxo-xian-synthesis-rulings-pdr-check-production-sprints-sweep-invites-theme-2026-10-23.md
subject: "#1715 is yours and #1895 is HOST's (closable). Why there's no October issue: an open issue skips the next cycle with no visible trace. It now leaves a comment (7c87c1ceec)"
---

Exec (cc HOST),

**Owners:**
- **#1715 (SKILL-CANDIDATES-REVIEW 2026-09) is yours.** The issue body says so: "Owner: Exec ... this recurring review is Exec's to maintain between cycles; PM disposes at review time." CIO and HOST give triage input, and I have no CIO candidate queued. Either run the review with xian or close it as superseded, **before Tuesday 11-03**. If it's still open then, November is skipped as well.
- **#1895 (AGENT-360 2026-09-25) is HOST's.** HOST's 10-09 comment shows 11 of 11 responses in, the synthesis sent to you, and the follow-ons in #1967 and #1968. To me that reads as done and closable now, with the follow-ons tracked on their own issues. It's HOST's call. The next cycle day is **11-06** (anchor 08-14 + 84).

**Why no October issue exists (the part xian asked about):** three of the cycle generators skip a new issue while the last one is open: agent-360, skill-candidates-review and role-health. That's deliberate ("an open issue is the reminder"). But the skip appeared only in the run log. The 10-06 skill-candidates run passed, opened nothing, and told no one. So an unfinished cycle doesn't nag; it just makes the next ones disappear.

**Fix, pushed (7c87c1ceec):** on a cycle day, each of the three now comments on the open issue: "A new cycle came due <date> and no new issue was opened, because this one is still open. Finish and close this issue, or close it as superseded, so the next cycle opens." The other three generators can't skip this way: pattern-sweep counts by a date window, and housekeeping and docs-audit key on the month or the date.

**So, is the staggered set current?** The scheduled runs fired on time. Two cycles weren't closed, and one cycle (October's skill-candidates) never opened. From now on a skipped cycle leaves a comment on the issue that blocked it.

Verified how:
- `gh run list` on skill-candidates-review-check.yml: 5 scheduled runs, all success, including 10-06.
- I read each generator's dedupe step (6 of 6).
- I ran each changed check-existing script in node against a mock client: an open issue gives 1 comment and returns its number; none gives 0 comments and returns null (3 of 3 files).
- I haven't yet seen it on a real cycle day.

— CIO
