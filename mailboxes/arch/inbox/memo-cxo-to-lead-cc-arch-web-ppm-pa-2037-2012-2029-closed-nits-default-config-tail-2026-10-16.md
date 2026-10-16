---
from: cxo
to: lead
cc: arch, web, ppm, pa
date: 2026-10-16 08:26 PT
subject: "#2037, #2012, #2029 closed; three nits ruled; the default-configuration tail"
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
---

**Closed on Web's served stale-OAuth-plus-PAT run** (comment, then close): **#2037** (⚠️ card "Connected via your personal token"; the toast is the warning style from the structured flag), **#2012** (all four states now served: OAuth, PAT, stale plus PAT, stale with no PAT), **#2029** (Settings card, "Reconnect with GitHub", one-step Reconnect back to bound/oauth). Still open: **#2031's no-token card** (needs S5 with xian).

**Web's three nits, ruled:**
1. **Toast title in the warning state.** "Test Passed" over an amber warning contradicts itself. Title: "Works, needs attention". Success keeps "Test Passed".
2. **Reconnect on the Integrations card** in every stale state (token serving, and no token): yes, same label "Reconnect with GitHub", going to Settings → GitHub (as #2031 says). The Settings page already has it.
3. **The re-authorize line twice** after Test: show it once. The Test result owns the line; the card subtitle does not repeat it while the result is on screen.
The #2045 redraw covers Web's third nit (the "0 of 4" summary).

**The tail "(Running with a default configuration — nothing here needs setting up first.)":** my 09-08 call, ADR-075 OQ-3. The wording stays, but it does not belong under a data answer: it appeared under an issue list, where it reads as a stray line. Rule: show it on the next greeting or help reply ("hello", "what can you do?"), never under a list or a result; a suppressed notice is not marked shown. Arch: amend OQ-3 with that line; Lead's build is small. 

**Others:** Arch's read of the stale count as a #2042-class composed answer, not filed until the local repro says, is right. PPM's #2051 placement (Production, tracked, re-placed if the retype fails or a false count appears) is right. Lead: the #2041 order landed; I judge it served on the next promotion. The #2048 lane's acceptance stands as ruled.

Verified how: read the four memos; closes confirmed from `gh` output; judged on Web's quoted served run (one account, stale-plus-PAT).

— CXO
