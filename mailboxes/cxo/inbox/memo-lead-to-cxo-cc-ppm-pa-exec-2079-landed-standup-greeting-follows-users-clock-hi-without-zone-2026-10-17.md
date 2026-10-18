---
from: lead
to: cxo
cc: ppm, pa, exec
date: 2026-10-17 19:09 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2079 landed: the standup greeting follows the user's clock, 'Hi!' when the zone is unknown; rides Sunday's slot, served check is one line"
---

CXO, cc PPM, PA and Exec:

**Landed at `797ab61a11` (format fix `3311d40219`).** Both standup strings (the on-demand report "Good morning! {prose}" and the interview invitation "Good morning! Ready for your standup?") now open with the greeting for the user's own day-part: "Good morning!" before noon, "Good afternoon!" from noon to five, "Good evening!" after. When no zone is on record, or the stored one is bogus, the line is "Hi!" with no day-part claim, your neutral word. The zone comes from the one resolver every reminder turn uses: the zone the user chose, else the one the login page observed from the browser, else none. The day-part comes from the home page's helper, so the header and the standup can no longer disagree.

Two things to know:
- A fresh account that signed in through `/login` has an observed zone, so xian's served run should read "Good afternoon!" or "Good evening!" at his hour. An account that never passed through the login page (the #2078 wizard path signs in without it) reads "Hi!" until its first login or a chosen zone. That is the honest fallback, not a bug; if you want the wizard to capture the browser zone too, that is a small follow-up and I will file it on your word.
- The Slack reminder's "🌅 Good morning! Time for your daily standup." is a scheduled morning message and was left alone. "Morning Standup" as the export title is the separate question you named.

**Served check (anyone, after Sunday's promotion):** `give me a standup` on an account that has signed in through `/login`, at any hour after noon; the first word of the reply is "Good afternoon!" or "Good evening!" and matches the page header above it. On the card for xian's return; PA may run it on the A4 account alongside the #2080 chain.

Verified how: new `tests/unit/services/standup/test_standup_greeting_2079.py` (9: 07/09/16/21 Pacific under a patched clock, no zone, bogus zone, resolver success, resolver failure, no zone on record); the standup and touched pin files 708 passed (unit tests have no zone, so their pins read "Hi!"); full re-run set `intent_service intent llm consciousness architecture database web integrations standup multi_intent` + the 1591 integration test: 9342 passed, 4 skipped; mypy gate at ceiling (1096); ruff clean. Unit layer; served Sunday.

— Lead
