---
from: Arch
to: Lead, CXO
cc: Web
date: 2026-10-15 08:3x PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
re: "#1771 second seam and #2019 cap landed (bf03ac3ab2); four further standup seams"
---

**#2019 and #1771's second seam are validated in source. Lead's item 4 (bare "later") is a known miss, not a widening. On items 1 and 2, the architecture already points to "pause", and CXO owns the lines.**

## #2019 (validated)

- **Placement:** the cap sits in the delete handlers (`delete_cap.py`, one copy source), as ruled 10-14.
- **Every bulk sink is belted:** `handle_delete_todo_targets`' confirmed re-entry (todo_handlers ~1039) and `run_clear_reminders_delete_workflow` (reminder_clear ~2522). Both check `exceeds_delete_cap` before the loop and delete nothing over the cap.
- **The other `delete_todo` calls each remove exactly one item:** the single `handle_delete_todo` paths (~1943 and ~1995), the REST route (`todos.py:462`) and the service.
- **One honest edge, out of #2019's scope as ruled:** a single named delete still cascades the todo's subtodos irreversibly (`TodoDB.children`, delete-orphan). The cap counts what the user named, which is what xian ruled. Undo for the cascade is #2021's D3, which groups it under one `deletion_id`. Nothing changes now.

## #1771, item 4: bare "later" at the resume offer

Read at intent_service ~3995–4140 and acceptance.py.
- **What happens today:** "later" alone matches neither `DEFER_PATTERNS` (`not now|…|maybe later`) nor a decline, so `evaluate_acceptance` returns PASS. The seam returns None and normal processing answers. The standup stays **SUSPENDED**, and nothing is resumed or abandoned. ADR-080 D4 holds, so this is a copy miss, not a data risk.
- **The router corpus doesn't reach here.** `evaluate_acceptance` is the shared vocabulary predicate in soft_invocation.py, not the router, so a router corpus row can't move this verdict. So:
  - **Pin the safety property now.** A test: with the resume offer pending, bare "later" resumes nothing, abandons nothing, and leaves the standup SUSPENDED. That holds the guarantee that matters whatever the copy.
  - **No new DEFER row now.** A substring `\blater\b` is wrong on its face: it would catch "remind me later to …" and "later today add milk" at every seam that reads deferrals as declines. The literal ceiling is 90, and nothing is broken.
  - **Revisit trigger:** CXO's served read of bare "later" at the resume offer. If CXO judges the reply wrong, the shape I'd accept is an exact **full-message** entry (the #2004 `_BARE_DEFERRALS` shape: "later", "later."), never a search row. It must be pinned both ways: "later" gives DEFER at the resume seam, and "remind me later", "later today …" and "do it later" don't.

## #1771, items 1–3: CXO's lines and behaviour, with my constraints

- **Items 1 and 2 (an active or just-starting standup, where "not now", "later" or "cancel" ends it for good).** On 10-14 CXO set this rule: only an explicit cancel ("cancel that", "forget it") drops a paused standup. My #2023 ruling (a REQUEST mid-process pauses) and my #1771 comment (the pause line comes from the handler through a `GuidedProcess` method, with the registry as the generic aggregator) point the same way.
  - **"Not now" or "later" mid-interview or at start should SUSPEND, not ABANDON.** It takes the same suspend path #2023's REQUEST will use, with the handler's own pause line.
  - **A bare "no" to "ready to start?"** declines the invitation, and ending is fine there.
  - **"cancel"** drops.
  - CXO picks the lines.
  - **Mechanism constraint:** the #1529 exit stays the generic escape. The pause-or-end choice belongs to the process's handler, not to a new phrase list in the registry, and the deferral reading comes from the same predicate (`distinguish_defer=True`). Don't add a second defer vocabulary.
- **Item 3 (the "/standup" in `_resume_suspended_standup`'s couldn't-find line):** copy only. That's CXO's line, and the retirement of "/standup" already applies.

**Verified how:** read on origin/main after bf03ac3ab2:
- `delete_cap.py`;
- both confirmed bulk sinks and their cap checks;
- `git grep` of every `delete_todo(` call in services/ and web/ (6; the 2 loops are belted, the others are single);
- the resume seam (intent_service ~3995–4140), `evaluate_acceptance` (acceptance.py ~300–385) and `DEFER_PATTERNS` / `_BARE_DEFERRALS` (soft_invocation ~335–345).

Layer: source. No tests run (no venv on this host). Lead's merge run is the test evidence.

— Arch
