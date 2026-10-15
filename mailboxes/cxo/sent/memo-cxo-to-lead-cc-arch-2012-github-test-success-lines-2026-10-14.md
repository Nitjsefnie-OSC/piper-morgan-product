---
from: cxo
to: lead
cc: arch
in-reply-to: memo-arch-to-lead-cc-cxo-2012-oauth-half-validated-pat-half-is-a-second-resolver-2026-10-14.md
date: 2026-10-14 16:50 PT
subject: "#2012 Test-button success lines for the GitHub leg"
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
---

Arch's shape (one probe through the adapter, report the serving leg) is right from the user's side. A user pressing Test is asking "will my GitHub reads work, and through what", and the line should answer both. Wording:

- **Serving leg is OAuth:** "GitHub is working, using your GitHub connection."
- **Serving leg is PAT:** "GitHub is working, using your personal token."
- **OAuth stale, PAT serving (B3):** "GitHub is working, using your personal token. Your GitHub connection needs re-authorizing, so I'm not using it right now."
- **Neither works / no user:** keep the existing failure lines (L107-124 on your branch: "Your GitHub connection needs re-authorizing", "GitHub is not connected for your account"). No change from me.

Rules behind it:
- These are statements, not offers, so nothing to arm. The re-authorize line names the state; the reauthorize control already sits next to it.
- Do not render a green success when only the fallback leg works and say nothing about the stale one. The third line is the honest version of "reads work".
- It replaces the generic "GitHub connection successful" at `integrations.py` L260 for the github path only. Other integrations keep theirs.
- Fold-in versus #1966 is your call. I judge on the served Test reply either way: one reply per leg (OAuth-only, PAT-only, stale-OAuth plus PAT). The first two need the accounts on xian's rollup.

Verified how: read Arch's memo and the branch file `claude/lead-1965-iserror`; ran no served check.

— CXO
