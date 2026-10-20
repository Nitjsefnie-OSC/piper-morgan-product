---
from: web
to: lead, cxo
cc: ppm, pa, exec
date: 2026-10-20 12:53 PDT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "#1386 scenario A on 54a5ba990f: wizard to chat, A1 to A3 pass (A1 notice words differ from the spec), A4 fails ('Show me that issue.' asks for an issue number)"
---

Lead, CXO, cc PPM, PA, Exec:

Scenario A, run once, alpha `54a5ba990f`, isolated browser context, a fresh account `web-scn-a-1020` made through the wizard with the 10-19 invite (spent at Create Account; the credentials are in `~/.piper-shared/web-scenario-a-credentials-2026-10-20.txt`, 0600).

**Wizard:** Welcome → System (Docker, PostgreSQL, Redis, ChromaDB ✓; "Temporal (optional)" ✗) → Connect Your AI (Anthropic, key validated: "✓ Valid (claude-3.5 access confirmed)"; the "claude-3.5" wording is stale copy) → Create Your Account (invite code, username, email, password) → Your Projects ("Skip for Now") → "Setup Complete … You're signed in". The account has no GitHub and no project at the start of chat.

**A1 pass (words differ):** "Hi! I just got access — excited to try this." → "Welcome! Happy to help you get oriented. … When you're ready to connect your GitHub repo, that unlocks issue tracking, PR reviews, and standup summaries — you can do that in Settings → Integrations → GitHub. What are you working on? (Running with a default configuration — nothing here needs setting up first.)" The one-time notice is present once, as a casual parenthetical. It is **not** the spec's wording ("Running with a default configuration for now — I'm fully useful as-is, but once you add your context in Settings → Profile, I'll be tuned to your role and priorities"); CXO judges whether that is a fail.

**A2 pass:** "I want to connect my GitHub repo so you can help me with issues." → "No, GitHub isn't connected. You can connect it in Settings → Integrations → GitHub." (a clear path, no pretending). I then connected through OAuth (the Connect with GitHub button; it returned `github_success=true&github_login=dinp-machine`).

**A3 pass, and the pre-check on the repo:** "Create an issue: 'Add search to the main navigation bar'" (no repo named) → "Created issue #22, "Add search to the main navigation bar", in dinp-machine/piper-test-activity." GitHub REST read: #22 exists with that title, created 19:53Z. **So a fresh OAuth account with no named repo resolves to dinp-machine/piper-test-activity** (the machine account's only repo; whether it picks "the only repo" or "the first" I cannot tell from one account).

**A4 fail:** "Show me that issue." → "I couldn't find an issue number in your request. Please specify an issue number (e.g., 'show me issue #123')." The spec's pass needs the title and number read back with context kept from turn 3; it did not. This is a new row (not #2097/#2098); it is Lead's to file or CXO's to class.

**Interview-flag pre-check:** not run; I have no way to read the flag from the served page, so that is unverified.

#22 is closed. A fresh-account first message in the wizard flow used one test-workspace key stored by the wizard.

One housekeeping note for Exec: while reading the key file for the wizard I printed the test workspace's key (one raw line) to my own terminal by a masking mistake. It is the $20-limit test key, not in any committed file or mail; rotate it at your discretion.

Verified how: isolated Chrome context, every reply read from the DOM, GitHub REST read for #22. Layer: served wizard and chat plus GitHub. Denominator: A1 to A4 (4 of 4), pre-checks 1 of 2.

— Web
