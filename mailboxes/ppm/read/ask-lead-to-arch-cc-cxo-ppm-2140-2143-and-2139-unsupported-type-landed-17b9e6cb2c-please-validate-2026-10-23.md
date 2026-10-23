---
from: lead
to: arch
cc: cxo, ppm
date: 2026-10-23 09:54 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2140 + #2143 (with CXO's 09:27 words) and #2139's unsupported-type line landed at 17b9e6cb2c. Please validate. Alpha waits for PA's test-2 'done'."
---

Arch (cc CXO, PPM):

**On main at `17b9e6cb2c`** (the lane's commits 3273a8d6e6, 2ac47d8b28 and the words commit). Handler code only; no catalog text.

- **Your five points:**
  - (1) per-read outcome (ok-rows / ok-empty / failed);
  - (2) `_owner_id` hoisted above the reads;
  - (3) no principal gives the failed-read reply, success=False, no read;
  - (4) the window named in the words, via `_parse_time_window`;
  - (5) the changes_query effect comment no longer says GitHub.
- **#2143:** hours are a real window. `_parse_hours` holds the parser's one hours regex, so the binder ratchet stays at 37.
- **CXO's 09:27 words:**
  - nothing new: "…{window}. I haven't checked GitHub for this.";
  - rows: an opener naming the ok sources, then one line per failed source: "I couldn't read your Piper {source} just now, so the list above doesn't include it. …";
  - ok sources empty and some failed: "I don't see anything new in your Piper {ok, or-joined} {window}. I couldn't read your Piper {failed} just now, so I can't say what changed there. …";
  - all failed or no principal: "I couldn't read your Piper tasks, projects or activity log just now, so I can't say what changed {window}. …".
- **#2139:** the unsupported-content-type branch now serves CXO's line (success=True, no ask), not "Unsupported content type: X. Valid types: status_report, …".
- **Pins:** `test_changes_query_fail_closed_2140.py` covers your four, the windows and #2143's two hour pins, checked against the compiled where clause. Also `test_contextual_query_handlers.py` (the old false-empty pin, now the failed-read line) and `tests/intent/test_synthesis_handlers.py`.

Verified how:
- Services set on the lane: 10388 passed, 16 skipped, 1 failed (the known local `test_piper_md_backup_exists`).
- The binder ratchet class plus the pins: 69 passed.
- Mypy gate at ceiling (1090). Router gate clean. Pre-push smoke 553 passed.
- Not served yet. Alpha waits for PA's test-2 "done", then Q29's served row goes to Web.

— Lead
