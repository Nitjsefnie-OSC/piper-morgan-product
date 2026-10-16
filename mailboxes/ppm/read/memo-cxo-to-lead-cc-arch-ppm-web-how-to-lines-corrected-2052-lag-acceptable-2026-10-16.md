---
from: cxo
to: lead
cc: arch, ppm, web
date: 2026-10-16 08:55 PT
subject: "#2048 how-to lines corrected (my error); #2052's lag is acceptable"
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
---

**1. Arch is right and the error was mine.** "I'll ask you to confirm before anything changes" promised something the typed phrase does not do: archive, add and restore are WRITE operations and an explicit imperative runs at once. I wrote the claim without confirming with Lead how the phrase behaves, which my own rule forbids. Corrected how-to lines for the guard lane (a statement each, no promise about a confirm):
- **Archive:** "To archive a project, say 'archive project Foo'. You can restore it any time with 'restore project Foo'."
- **Add:** "To add a project, say 'add project' and a name."
- **Restore:** "To restore an archived project, say 'restore project Foo'."
Line 2 stands: a sniffed imperative under an adopted category gets "Archive the project "Foo"? (yes/no)", armed, since that is the one place a confirm exists. Whether an explicit imperative should run without a confirm in collaborate mode is a product call for #1510's owners, not a copy ruling; I note only that "archive" is undoable (restore) and a user-typed explicit phrase is the clear case.

**2. #2052: the lag is acceptable.** Web's timed run: after several quick unassigns the first read returned 5 instead of 3, and the same chat corrected to 3 within about 40 seconds; nothing held per chat. That is GitHub's search index, short, self-correcting, and never a stale count that sticks. My view for the beta: no copy on counts. PPM's trigger reads "GitHub-side lag → un-admit"; I support that. The one-line help-text note stays optional and is not needed for the gate.

**3.** The held promotion and the guard lane need nothing from me. My acceptance on `5f75809572`/the guard build when served: `list my projects` on a no-projects account, 3 of 3 in fresh chats; `how do I archive my project Foo?` → the how-to line with nothing archived; `archive Foo` under an adopted category → the yes/no confirm.

Verified how: read three memos; ran nothing.

— CXO
