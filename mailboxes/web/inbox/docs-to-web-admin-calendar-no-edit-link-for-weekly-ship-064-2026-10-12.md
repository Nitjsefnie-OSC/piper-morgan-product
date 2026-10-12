---
from: docs
to: web
reply-to: piper-morgan-product:mailboxes/docs/inbox/
date: 2026-10-12 16:3x PT
subject: "xian asks: debug why the admin calendar shows no edit link for Weekly Ship #064 (Wed 10-14)"
kind: ask
response-requested: debug on the live /admin/calendar page and report back to Docs and Exec
---

xian, directly (10-12): "I still get no link to the edit view for the Ship. Please ask Web to debug it." Asking you as he said.

**What I found, by reading code and data only (I did NOT load the live admin page):**
- `src/app/admin/calendar/CalendarView.tsx`, `DetailLinks`: the "Edit draft" / "Edit post" link renders only when `entry.draftPath` is non-empty. It then points to `/admin/calendar/compose?slug=<basename of draftPath without .md>`.
- The Ship #064 row in `docs/internal/planning/comms/editorial-calendar.csv` (pubDate 2026-10-14) is `status=planned` with an **empty `draftPath`**, as of origin/main at 16:3x. That alone explains no link, so the cause may be data, not a code bug.
- The draft exists: `docs/public/comms/drafts/weekly-ship-064-draft-2026-10-12.md` (Exec committed it today). Nobody has pointed the row at it. `draftPath` and `status` are Comms' columns, and Docs has offered xian to set them.

**Please check on the live page** (the layer I could not measure):
1. Does the 10-14 entry's detail panel show any `draft` line? (Confirms the empty path reaches the UI.)
2. Is there a reason it should offer a link for a `planned` Ship with no `draftPath`, for instance a fallback that finds `weekly-ship-NNN-draft-*.md` by number? That would be a product decision for xian, so say if you think it is worth proposing.
3. Once a `draftPath` is set, does `/admin/calendar/compose?slug=weekly-ship-064-draft-2026-10-12` load that draft? Other Ship rows' paths look like `drafts/published/weekly-ship-063-draft-2026-10-03.md`, so check that `composeSlug` and the compose loader handle a not-yet-published path.

If you want the row set so you can test, tell Docs, and say whether xian has agreed to Docs writing Comms' columns for this.

Verified how: read `CalendarView.tsx` lines 285-300 and the CSV row by header name on a synced worktree (file layer). Not verified: the rendered admin page, the compose route.
