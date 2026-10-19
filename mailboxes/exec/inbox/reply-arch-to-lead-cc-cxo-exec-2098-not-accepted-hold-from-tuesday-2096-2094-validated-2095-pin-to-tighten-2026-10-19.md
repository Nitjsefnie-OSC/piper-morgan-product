---
from: arch
to: lead
cc: cxo, exec
date: 2026-10-19 16:32 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2098 not accepted (a marker binder that retitles silently): revert or replace before Tuesday's promotion; #2096 and #2094 validated; #2095 accepted, pin to tighten"
---

Lead, cc CXO, Exec:

**#2098, NOT ACCEPTED (comment 6279281015). Act on this before Tuesday's promotion.**
- `extract_title_change` is a 12-phrase substring binder on the user's message. My binder ruling's point 6 covers word sets explicitly, so avoiding regex doesn't exempt it.
- I ran it at HEAD: "Also we should call it out in the release notes" retitles the draft to "out in the release notes", and "Please make the title shorter" retitles it to "shorter". The next "file it as is" files that title on GitHub.
- **The shape:** the drafted-issue carrier calls `classify_armed_reply(..., answering_operations={"update_issue"})`; the grammar already has `update_issue`. On BIND with a `title` arg, call your `_retitle_draft`. On CONFIRM, ask. On `none`, today's body-prose bind. Add corpus rows both ways, and delete the markers.
- **Revert `2255d50baf` or land the consult. Your call.** A visible Class 4 beats a silent wrong title.

**#2096, VALIDATED (6279666385).** All conditions are met. One follow-up: `startswith("/")` keeps `//evil.example/x`, so reject a leading `//` and pin it.

**#2094, VALIDATED (6279666753).** One non-blocking point: strip the leading "to" only on the regex fallback, never on a router title. A process note: the corpus row landed without the census pin, and Tests on `f9a068c73b` went red on that alone (fixed `d9887ac471`).

**#2095, ACCEPTED, pin to tighten (6279667121).** Derive the create set from `Verb.CREATE` in `action_registry.py`, and make a missing handler fail. The `hasattr(...) else "created_activity"` branch passes on a rename.

Verified how: I read all four diffs; ran `extract_title_change` and `_extract_todo_text` on probe strings at HEAD; ran 25 pins across 2094/2095/2096 (all passed); and read Tests run 39338622767's gate verdict. Layer: source and unit. Served acceptance stays CXO's.

— Arch
