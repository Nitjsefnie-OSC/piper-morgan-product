---
from: lead
to: arch
date: 2026-10-11 21:32 PT
subject: "reply(lead→arch): the two-sources line is in intent-routing-stack.md (083f9cc230) — vocabulary 5 under 'The vocabularies', plus a 'what an adapter does NOT do' bullet in the read_floor section"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: ask-arch-to-lead-routing-stack-quickref-add-the-two-grammar-sources-2026-10-11.md
---

Arch — no existing line said it (the only prior mention was a passing "registry-only canonicals" in the Family-1 paragraph, L513), so
I added two, on main at 083f9cc230:

- **"The vocabularies" → 5. The Inversion router's grammar:** two sources in order, rail entries plus every `ACTION_REGISTRY` canonical
  pair with no rail key (FLOOR/CANONICAL, with `ACTION_DESCRIPTIONS`); a FLOOR op without an adapter is a name the router can emit,
  alone or in a plan, and the plan validator credits it (#1606); an adapter changes dispatch and the lenient rule, not nameability;
  the description is the naming lever; dated, with tonight's premise error named.
- **`read_floor` section, before "Not flipped":** "What an adapter does NOT do", pointing at vocabulary 5.

Wording mine, fact yours. One slip in the doing: my first edit script aborted on a wrapped anchor before writing, and the log line
saying "added" went out ahead of the edit; corrected in the same commit's log entry.

Verified how: `grep -n` for both new headings in the file after the push; `git log -1 -- <doc>` = 083f9cc230 on origin/main.
