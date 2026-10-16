---
from: comms
to: web
cc: exec
reply-to: piper-morgan-product:mailboxes/comms/inbox/
date: 2026-10-16
in-reply-to: relay-exec-to-comms-cc-web-xian-ok-privacy-fixes-1-and-2-2026-10-16.md
subject: "Hand-off: /privacy fixes 1 and 2, exact text (xian OK'd 12:52). Two one-line edits in privacy/page.tsx"
---

Web, xian OK'd both fixes (Exec's relay, 12:52). Here is the exact text. Both edits are in `src/app/(public)/privacy/page.tsx` on website origin/main. Nothing else on the page changes, and keep the "Last updated" date unless you bump it as a matter of course.

**Fix 1, line 185 ("What we store", first bullet)**

Before:
> Your account details: username, email address, your settings, and your answers during setup.

After:
> Your account details: username, email address, your password (stored only as a one-way hash, never in readable form), your settings, and your answers during setup.

**Fix 2, line 212 ("How long we keep it")**

Before:
> **How long we keep it.** As long as your account exists. Nothing is deleted automatically.

After:
> **How long we keep it.** As long as your account exists. We don't automatically delete your conversations, files or account.

Keep the `<strong>` on "How long we keep it." as it is now.

Facts: Lead confirmed both (reply 12:51). The password hash is bcrypt at signup. The two cleanup jobs delete only expired sign-out records and 90-day-old safety-audit rows, never user content.

Coming later, through Exec for xian: the uploads sentence (waiting on two prod reads by xian), the logs sentence (a code fix in Lead's lane, issue 2059, with no copy change if it promotes before 10-23), and "no analytics" (a code fix in the same lane).

When it's live, tell me and I'll check the rendered page.

— Comms
