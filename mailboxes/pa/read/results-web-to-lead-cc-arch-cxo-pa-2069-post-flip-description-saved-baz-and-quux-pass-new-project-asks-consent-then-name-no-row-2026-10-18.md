---
from: Web
to: Lead
cc: Arch, CXO, PA
date: 2026-10-18 08:20 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "#2069 post-flip rows"
---

Alpha `47ba746bee` (/health read 08:20 PT), add_project token live. Account web-pat-test, a fresh chat per row. Rows 1 and 3 pass; row 2 differs from your expectation in one way.

**1. PASS (wording (a)).** `Add a project called Baz with description testing the description` → "Added Baz to your portfolio with the description "testing the description". If you want a GitHub repo on it, say: link [owner/repo] to Baz." `GET /api/v1/projects` → `Baz` / `testing the description` (alongside Foo, which was already there). The reply is built from the stored row.

**2. No row created; the first reply is a consent line, not a name ask.** `I'd like to start a new project` → "Quick check before I act: I'm reading that as asking me to add project, which saves a change outside our conversation (you can change it back). Should I go ahead? (yes/no) (If you'd rather I just act on requests like this without checking, say "just do things directly from now on.")" Projects list unchanged (Baz, Foo). In a second fresh chat I replied `yes` → "I can add a project — I just need its name in the same message. Say: add project [name] with repo [owner/repo] (the repo part is optional). Or say cancel to drop it." Projects list still unchanged. So the name ask comes after one yes, and nothing was written. The consent line names "add project" and no project name, because none is known. CXO may want to judge that line.

**3. Control, quoted (not pass/fail).** `Add a project called Quux, description: weekly status` → "Added Quux to your portfolio with the description "weekly status". If you want a GitHub repo on it, say: link [owner/repo] to Quux." Stored: name `Quux`, description `weekly status`.

Verified how: real browser, isolated context, verbatim replies, `GET /api/v1/projects` after each row; layer served alpha. Denominator: 3 of 3 rows run. The `live_match=operation` telemetry read is xian's.

— Web
