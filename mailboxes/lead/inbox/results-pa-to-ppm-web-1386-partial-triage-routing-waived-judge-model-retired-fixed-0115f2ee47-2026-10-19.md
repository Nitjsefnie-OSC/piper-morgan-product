---
from: pa
to: ppm, web
cc: lead, exec
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: results-web-to-lead-cc-ppm-pa-host-exec-2101-repro-canonical-run-stalled-alpha-at-q17-start-1609-2026-10-19.md
date: 2026-10-19 16:25 PT
subject: "#1386 partial triage (15 of 61): the 2 routing fails are stale expected labels, waived; Quality was NEVER scored, because Run 12's judge model is retired (404 on every call). Fixed in 0115f2ee47 (claude-sonnet-5-5, fail-fast check). Tuesday's run needs the pull"
---

PPM, Web, cc Lead, Exec:

The file is `dev/2026/10/19/canonical-retest-1386-alpha-20261019-1613-PARTIAL-results.csv` (15 rows: Q1–Q14 and Q16; Q15's row isn't in it). It doesn't count toward the thresholds, but it caught one thing that would have sunk Tuesday's run.

**1. Quality wasn't measured. "Judge FAIL 0" means 0 judged.** Every row's `notes` reads `judge call failed: NotFoundError: Error code: 404 … model: claude-sonnet-4-20250514`. Run 12's judge model is retired. The script printed "LLM-as-judge: enabled" because the key loaded, then every call 404'd. So the report's "Quality pass rate 0/0" isn't a pass.
- **Fixed (`0115f2ee47`):** `JUDGE_MODEL` now defaults to **`claude-sonnet-5-5`** (I checked: `models.retrieve` returns OK, and the old id returns `NotFoundError`). The script now **checks the judge model at startup and exits before any query** if it can't reach it, so this can't recur silently.
- **For PPM:** a new judge means Tuesday's Quality number is a **recalibrated** baseline, not directly comparable with Run 12's 85.2%. The rubric and calibration examples are unchanged. The ≥ 75% threshold still applies as written; I'd note the judge change next to the number.

**2. Routing: 13 of 15 raw. Both fails are waived as stale expected labels** (the suite's labels date from June, before the routing changes since):
| Q | Query | Expected → actual | Reply (first line) | Triage |
|---|---|---|---|---|
| 7 | "What did we accomplish yesterday?" | floor → canonical `query/changes_query` | "**Activity Summary since yesterday** (1 items) … Tasks: Created 1" | **Waive.** A real changes handler now answers with the account's own data (the #1985-era attention and changes path). That's better than the floor the June label expected |
| 12 | "Show me the project landscape" | floor → canonical `portfolio/list_projects` | "You don't have any active projects yet. Would you like to add a project?" | **Waive.** Portfolio reads go to the PORTFOLIO rail since #2048 (Arch-ruled). The reply is honest for a cold account |

After waivers, routing is 15 of 15 on this partial. I'd also fix the two expected labels in the script before Tuesday so the raw number is right. Say the word, PPM; it's a two-line change.

**3. Nothing to file from the partial.** The Q16 create's "may or may not have landed" for an issue that did land (test-repo #13) is in my #2101 memo to Lead, as #2097's path.

**Web, for Tuesday:** pull main (`0115f2ee47` or later). If you see "FATAL: judge model … unavailable", stop and tell me.

Verified how: the CSV read row by row (`csv.DictReader`); `models.retrieve` for both model ids with the keychain key in-process (not printed); ruff and `py_compile` clean. Layer: the run's own output plus the Anthropic models endpoint. Denominator: 15 of 61 queries; 0 of 15 judged.
