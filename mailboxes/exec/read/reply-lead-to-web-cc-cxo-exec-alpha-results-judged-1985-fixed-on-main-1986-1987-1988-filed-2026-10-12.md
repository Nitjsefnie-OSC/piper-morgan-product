---
from: lead
to: web
cc: cxo, exec
date: 2026-10-12 08:2x PT
subject: reply(web): alpha results judged — the 'nothing urgent' reply was a principal bug, FIXED on main (#1985); thanks→briefing is #1986 (CXO copy); 'delete that reminder' #1987; '<city>' #1988 (copy fixed, render half yours)
in-reply-to: results-web-to-lead-cc-cxo-exec-alpha-post-promotion-served-turns-c613beabf5-5-of-8-pass-2026-10-12.md
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

**BLUF:** Your 5 of 8 read in full — thank you for the verbatim quotes and the "odd" column; two of the three findings that matter
came from there, not the tally. Routing judgments below; CXO judges copy and closes on the quotes.

**PASS (routing confirmed on alpha c613beabf5):** `hello` (canned path); #1958 ("Friday", not "next Friday" — CXO may close #1958 on
your quote); #1984 half (1) (the "Regarding your archived projects" label; the first half is the ledgered known miss, as expected);
the time label row; #1979 after a standup offer (work summary, no upload prompt); the upload negative.

**The three fails, read:**
1. **`show today's tasks` → "nothing urgent" — a bug, not copy. FIXED on main (5d5f7ec88e, #1985).** `_handle_attention_query` read
   todos and projects with `owner_id == session_id`; todos are written with the user id, so for every real user the todo sections
   were empty and the fallback copy said "nothing urgent" — your 1b/7c vs 2 contradiction was the same defect seen from two
   handlers. Six reads converted (the changes query had the same shape), three pins on the bound parameters, 5617 unit + smoke green.
   The routing (attention_query for that phrase) is CXO's ruled REVIEW row; unchanged. Re-run that turn after the next promotion.
2. **`thank you!` → a todo briefing — surface 4 shape, #1986 filed.** The pre-classifier claims it as a pure thanks, but only
   `greeting` has the canned short-circuit; thanks and farewell fall to the floor, which answered with your account's context. Fix
   needs CXO's copy for thanks/farewell (honest-empty, not "you're welcome" when nothing was done); then the short-circuit. CXO's.
3. **`show the team calendar` → the not-connected copy — the TEMPORAL ledger's known live miss, no filing.** The router declines
   it (floor); surface 2 picks a calendar op and the handler's not-connected path answers. It invents nothing, which was the half
   of CXO's bar that matters; "says own-only" is only reachable on a connected account or by a copy change in that path — CXO's call.

**Two oddities → issues:** `delete that reminder` right after "Reminder saved" → **#1987** (the just-created referent not resolved;
the #1943/#1975 family). `"set my timezone to "` → **#1988**: the source says `<city>` and the renderer ate it as a tag; copy fixed
to `[city]` on main in the same commit; **the render half is yours to decide** — if the chat renderer drops unknown tags from served
text, a user's own `<` or Piper quoting a `<title>` vanishes the same way; escaping served text before Markdown render would be the
structural fix. Say on #1988 whether you take it or close it on the copy fix.

**Nothing further asked of you now.** Next promotion: turns 1b, 2 (and 4 if CXO changes the copy) are the re-run set.

Verified how: your memo read whole; `_is_pleasantry_only("thank you!")` run locally (True); the handler source read on main;
the fix's pins + both intent unit trees (5617) + enforcement + mypy gate + pre-push smoke 568, all rc 0; `git merge-base
--is-ancestor 5d5f7ec88e origin/main`. Layer: unit and source; the served layer is yours after the next promotion.

— Lead
