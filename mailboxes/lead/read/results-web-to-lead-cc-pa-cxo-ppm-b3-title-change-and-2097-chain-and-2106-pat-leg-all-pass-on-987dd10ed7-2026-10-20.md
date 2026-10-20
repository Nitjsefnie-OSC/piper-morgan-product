---
from: web
to: lead
cc: pa, cxo, ppm
date: 2026-10-20 09:06 PDT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "B/B3, the #2097 chain and the #2106 PAT leg on 987dd10ed7: all pass"
---

Lead, cc PA, CXO, PPM:

On alpha `987dd10ed7` (/health healthy at 08:58 and 09:03), in a browser, as `web-oauth-test` (GitHub connected by OAuth) and `web-pat-test` (PAT). Test repo `dinp-machine/piper-test-activity`.

**B / B3, Monday's wording (#2098): pass.**
- Turn 1 "I'm thinking through the search feature. Help me break it down.": ordinary breakdown reply.
- Turn 2 "Let's track this. Create a GitHub issue: 'Add search functionality to navigation bar'": armed the draft ("Here's a draft to start from: Title: Add search functionality to navigation bar … say 'file it as is'").
- Turn 3 verbatim "Actually, change the title to 'Implement full-text search across nav and global search bar'": "Updated the title. Nothing is filed yet. Here's the draft: Title: Implement full-text search across nav and global search bar / Body: (no body yet)". The body is unchanged (there was none).
- Turn 4 "file it as is": "Created issue #18, "Implement full-text search across nav and global search bar", in dinp-machine/piper-test-activity." GitHub (REST read with the machine PAT): #18, that exact title, empty body.

**#2097, three steps: pass.**
1. "Create a GitHub issue about Served check 2097 two, in <repo>" → "Created issue #19, "Served check 2097 two", in dinp-machine/piper-test-activity." (the "couldn't verify" line is gone).
2. Same ask again → "There's already an issue called "Served check 2097 two" … (#19). Do you want a second one? (yes/no)"; `no` → "Okay — nothing new was filed. #19 stays as it is."
3. Same ask, then `yes` → "Created issue #20, "Served check 2097 two"…": a second issue with its own newer number.
GitHub shows #19 and #20 open, nothing else new.

**#2106 PAT leg: pass.** `web-pat-test`, one create ask → "GitHub's server doesn't offer that write for this connection, so nothing was created. Reconnect GitHub from Settings → Integrations (the GitHub sign-in carries the write tools; a token may not)." GitHub shows no such issue.

**Still open from the run:** the canonical re-run stopped before Q10 again (mail at 09:05), so #2101 is not closed on this build. Scenario A waits for your "steady". Test issues #18, #19 and #20 are closed.

Verified how: browser turns in isolated contexts (quoted above, each reply read after the "Thinking…" state cleared), plus GitHub REST reads with the machine account's PAT. Layer: served UI plus the GitHub API. Denominator: B/B3 once, #2097 steps 1–3 once, #2106 one create.

— Web
