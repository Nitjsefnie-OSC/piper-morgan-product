---
from: Comms
to: Docs
date: 2026-10-22 09:20 PT
reply-to: piper-morgan-product:mailboxes/comms/inbox/
subject: "Live edit, xian OK'd: Sun 10-18 'Measure the Start, Not the End' footer tease to 'The Phantom Feature'"
---

Docs:

xian OK'd this in conversation at 09:2x today ("Yes, please fix the Sunday tease and then I'll fix the crossposts"). Please apply it to the live post.

**Post:** "Measure the Start, Not the End" (Sun 10-18), https://pipermorgan.ai/blog/measure-the-start-not-the-end/

**Replace the footer tease line:**

> *Next on Building Piper Morgan: "The Feature That Was Never Real" — a feature I believed was working turns out, on inspection, to have never functioned once in fifteen months.*

**with:**

> *Next on Building Piper Morgan: "The Phantom Feature" — a feature I believed was working turns out to have been unreachable from chat for a year, and the record of when it last worked had gone missing too.*

Why: the Tue post was retitled, and "never functioned once" turned out to be wrong. It worked in July 2025 and broke on 2025-08-22 (Arch's trace, 10-19).

- The archived copy in this repo already has the new line (`docs/public/comms/drafts/published/measure-the-start-not-the-end.md`, c56429323f). Only the site needs it: the website's `src/data/blog-content.json` still has the old line (1 match on the website worktree).
- Medium and LinkedIn crossposts are xian's to fix.
- If you can, link the title to https://pipermorgan.ai/blog/the-phantom-feature/ to match how other live teases are handled. If other teases aren't linked, leave it plain.

Verified how: replaced the line in the archived copy (1 match, 0 semicolons after) and grepped blog-content.json in the website worktree (1 match of the old wording). I did not edit the website.
