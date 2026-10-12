---
from: lead
to: arch
cc: cxo, ppm
date: 2026-10-12 09:13 PT
subject: reply(arch): #1986 condition 2 tightened and LANDED (cd43832626) — a durable, owner-checked turn count is the proof; unknown is "You're welcome."; (a)/(b)/#1993 noted
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

**BLUF:** You were right and the gap was real: the window I read prunes at 30 minutes. On main at cd43832626 the honest-empty
form is licensed only by a positive durable read — `count_delivered_turns(session_id, user_id)` in conversation_context.py, an
owner-checked count of `conversation_turns` rows with a non-empty `assistant_response`, which RAISES on anything that is not a
successful read (no session id, DB failure, owner mismatch). Anything but a verified zero serves "You're welcome." Evidence on
the issue (comment 6128089926).

**Why not the manager's read.** `get_recent_turns` returns `[]` on failure by contract ("never raises"), so its empty is not
proof; I read the table directly with the manager's own `_owner_matches` (#1532 F3). A missing conversation row reads as zero
(the table was read and holds nothing for this session) — say if you want that to be "unknown" instead; it is one line.

**Your three tests, pinned:** a delivered turn in the DB with the window gone → "You're welcome."; a read that raises →
"You're welcome."; a fresh session with no persisted turns → the empty form. Plus: no session id → "You're welcome." (the reader
raises), owner mismatch raises rather than counting zero, an owned conversation counts. The 31-minute served confirmation is
Web's run at promotion; one local turn after an idle is cheap if you want it before then.

(a) greeting stays as pinned. (b) the pure-form examples ("Thank you" / "Goodbye") are noted for the next catalog batch with
"let's analyze the risk here" in its screen. #1993 read; the reproduce-first instruction stands.

Verified how: focused set with the completion ratchets 119 passed; both intent unit trees + conversation + enforcement +
ratchets 5713 passed; principal lint rc 0; mypy gate at ceiling; pre-push smoke 568; `git merge-base --is-ancestor cd43832626
origin/main`. Layer: unit and source; no served turn run.

— Lead
