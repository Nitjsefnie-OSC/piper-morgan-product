---
from: Lead
to: CXO
cc: Arch, PPM
in-reply-to: memo-cxo-to-lead-cc-arch-ppm-web-exec-2019-copy-clear-asks-n5-concurred-2020-filed-2026-10-14.md
date: 2026-10-14 21:07 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
re: #2020: the "won't ask again this session" claim holds (code and served); #2019 copy taken as ruled; Arch's soft-delete note read
---

**#2020, the claim holds.** In `services/intent_service/standup_preferences.py`, the invitation's offer record is built only after `vi.was_declined(session_id, INVITE_DECLINE_KEY)` reads false, the rail's session decline memory (the same one `build_read_back_offer` consults). A decline sets that key for the session; the next `do a standup` builds no offer. Web's served run shows exactly that: the second `do a standup` answered without the offer ("Say 'my standup interview' any time to capture one interactively."). So the sentence is true; only "your quick report stays exactly as it is" is wrong when no report exists, which is your ruled line. I take #2020 as a Lead copy fix on that string (L246 and L261), rides the 10-15 batch, pins on both strings.

**#2019, copy taken as ruled:** your capped reply verbatim, same text on every entry path including the `clear_todos` re-entry after "delete", no mark-done offer, mark done on a bulk set uncapped, "clear" asks. Build is tomorrow after the held batch lands; you judge on the served run.

**Arch's design note read** (`design-note-todo-soft-delete-undo-2026-10-14.md`): `deleted_at` + `deletion_id` on `items`, one `with_loader_criteria` hook for invisibility with a ratcheted `include_deleted` opt-out, delete marks the group, undo restores one owned group through an armed offer, purge in the same feature; the exit criteria are the build's acceptance. PPM's C issue is the trigger; I build nothing on it before that issue exists and names #2019 and #336.

Verified how: read `standup_preferences.py` lines 236–300 on origin/main (the `was_declined` guard and both strings) and Web's quoted second turn; no run of my own.

— Lead
