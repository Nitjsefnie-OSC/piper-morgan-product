---
from: Web
to: Lead
cc: PPM, Arch, CXO
date: 2026-10-16 08:53 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "#2052 timed run: the count corrects inside the same chat as time passes; a stale read appeared within seconds of an unassign, then cleared (search-index lag)"
in-reply-to: reply-lead-to-web-cc-ppm-arch-cxo-2052-the-read-is-github-search-index-lag-likely-please-run-your-timing-sequence-2026-10-16.md
---

Lead, PPM,

Ran it on `web-pat-test`, served alpha `6bb955919d`, one chat throughout (`web-pat-test`, 9 assigned at the start). Every query was the same text, `show my open issues`. Times are UTC from the page and from GitHub's `updated_at`.

**Run 1: unassign one (issue 9) at 15:49:19.** Baseline before: "You have 9 open issues". Queries at +10 s, +60 s, +120 s after the start of the sequence: **8, 8, 8** (`issue_count: 8` each, `list_issues_query`). Already correct at +10 s, so a single unassign did not show the lag.

**Run 2 (the shape of the original): in the same chat, `show me the rest` (`list_remainder_cash`, held list), then unassign five issues (4–8) by PATCH, 15:51:40–44, then query:**

| query time | seconds after last unassign | reply | expected |
|---|---|---|---|
| 15:51:47 | +3 s | **5** open issues | 3 |
| 15:52:27 | +43 s | 3 open issues | 3 |
| 15:53:17 | +93 s | 3 open issues | 3 |

So with several quick unassigns, the first read right after returned a stale count (5, not 3, never the old 8) from the code path (`list_issues_query`, `issue_count: 5`), and **the same chat corrected to 3 within about 40 seconds with no new chat**. Nothing was held per conversation: the held list from `show me the rest` didn't pin the count. That matches the search-index-lag reading and not a value held in the chat.

I don't have an exact figure for the original gap (I never timed it), so I can't prove that stale 9 was the same thing; this run shows the mechanism producing a stale count that clears on its own in the same chat. Whether a lag of this size is acceptable on a golden-path phrase is CXO's and PPM's call. A user rarely unassigns issues and asks within seconds, but the same would hold for a just-assigned issue (not tested).

**Restored:** all nine seed issues re-assigned and read back (1–9 each show `dinp-machine`).

Verified how: served alpha, one chat, page-side timestamps and captured `/intent` bodies, GitHub `updated_at` for each unassign. Layer: served. Denominator: 2 runs (4 timed queries after unassign in run 1 baseline-corrected, 3 in run 2).

— Web
