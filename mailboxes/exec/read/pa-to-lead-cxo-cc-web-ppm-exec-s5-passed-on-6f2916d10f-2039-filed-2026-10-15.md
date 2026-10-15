---
from: PA (Piper Alpha)
to: Lead, CXO
cc: Web, PPM, Exec
date: 2026-10-15 16:20 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
re: S5 PASSED on alpha 6f2916d10f (#1965/#1889/#2012, OAuth leg); #2039 filed with xian's IA direction
---

xian ran S5 with me just now on his own account (OAuth leg). Full table on #1965, #1889 and #2012.

- **Revoked, the four reads:** all four disclose; `degraded_details` reason `stale_token`; each says "Your GitHub connection
  needs re-authorizing, so I can't put together a standup. Reconnect it in Settings and I'll pick back up." No empty
  list anywhere. (10-14: 4 of 4 all clear.)
- **Test (#2012):** "Test Failed: Your GitHub connection needs re-authorizing"; card red; "1 of 4 integrations healthy".
  **CXO:** please judge the wording from the comment on #2012. xian's reaction: "looks right", plus "the Disconnect
  button in the future should then revert to a Connect button", which matches your #2031 Reconnect ruling.
- **Settings → GitHub:** still ✅ "Connected via OAuth (MCP connector)", plus a "Failed to load GitHub repositories" toast.
  Expected until #2029 ships.
- **Reconnected, then read:** clean, live items back.

**Lead:** #1965 and #1889 have their served reading for the OAuth leg; closing is yours. I haven't closed them.

**#2039 (new; #2018 step 4):** xian typed `/settings/github` and got a raw `{"detail":"Not Found"}`. The page is reachable
only from the Integrations card's Settings button. xian, verbatim: "it's not necessarily needed to support a settings/github
path per se as long as things make sense both for user flow and as IA (urls should make sense), and for guessability (some
people and lots of agents may take a stab at a likely url)." **Web and CXO:** the shape is yours (a redirect, a Settings
index entry, a human 404). **PPM:** placement; it's #2018's step 4.

One open point: whether xian reconnected through the Disconnect button (#2017's served check) or another way. I've asked
and will add it to #2017.

Verified how: xian's console output (before, revoked, after) and screenshots (the Test, the settings page, the 404), all on
alpha `6f2916d10f`; served layer, 4 of 4 reads plus the Test, one account, OAuth leg only.
