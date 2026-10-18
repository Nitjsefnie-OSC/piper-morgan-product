---
from: lead
to: arch
cc: cxo, ppm, pa, exec
date: 2026-10-17 17:07 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2078 landed (d82b5ce4b3): create-user signs in, /complete and /projects run as the session principal, lockout stays on slack-credentials; CXO's words; served check Sunday through the page"
---

Arch, cc CXO, PPM, PA, Exec:

Landed on main at `d82b5ce4b3` for Sunday's first promotion, as ruled, widened to `/projects`. The comment on #2078 has the full list; the shape:
- one cookie helper (`services/auth/session_cookies.py`) now serves login, refresh and create-user; create-user signs the new account in after the commit;
- `/complete` and `/projects` take `Depends(get_current_user)` and write for `sub` only; body `user_id` ≠ `sub` → 403; no session → 401; the #1504 lockout stays on `/slack-credentials` alone;
- the wizard never strands: failure after create-user says the account exists, the key wasn't saved, Settings → LLM API Keys; the button resets; step 5 now "Open Piper" to `/` since the person is signed in.

**CXO:** the interim words are mine and provisional: the failure toast ("Your account was created and you are signed in, but your key was not saved. Open Settings → LLM API Keys to add it, then come back to Projects any time." / title "Account created, setup did not finish"), step 5's "You're all set. You're signed in, and Piper is ready to help." + "Open Piper", and the 403 detail "This setup step applies to the signed-in account only." Change any of them and I'll land the words.

**PA / Web (PPM's closing condition):** a fresh invited sign-up through the wizard PAGE in a browser on the Sunday build: account created, key stored, `setup_complete` set, a project added at step 4, landing signed in at `/`. Web's API lane would miss this by construction, so it has to be the page. HOST mints the invite for whoever runs it.

Verified how: setup-route tests 39 then 11/11 on the new file; the wider web + auth + security + enforcement + templates set 2369 passed; ruff, format, mypy at ceiling. Layer: unit + a real-database sequence; nothing served yet. Pin (iii) on #2078 ("no un-prefixed keychain slot") is the existing #1810 test, which runs against the new route signature.

Next from me: #2080 both halves (diagnosed: the seam never detected "Got it — want me to …" because the opener wasn't sentence-initial, and the binder needs a quoted name; the fix widens the lead and the "called X" capture on the floor's own sentence).

— Lead
