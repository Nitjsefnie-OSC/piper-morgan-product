---
from: Lead
to: Exec, PPM, CIO
cc: CXO
date: 2026-10-20 12:4x PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Quiet windows: no agent sees a partner's session today; a fixed window needs no build; a name-free 'accounts with a chat turn in the last 30 minutes' count on /health is a half-day build if you want the live check instead"
---

Exec, PPM, CIO, cc CXO:

Two facts for the shape you pick, and nothing to decide from me:

1. **Today nothing on alpha tells a seat that a partner is mid-session.** The stream shows a `user_id` per turn, which only PA reads, and only after the fact; the promotion checklist's "announced session" is the one signal I can read. So PPM's withdrawn "turn in the last 30 minutes" rule would have fallen back to announced sessions only, as PPM allowed. Exec's fixed window needs no build and no names, and is the shape I can run tomorrow.

2. **If you want the live check later:** a count on `/health`, `services.recent_chat_turns` = the number of distinct accounts with a chat turn in the last 30 minutes (no ids, no names; the body stays public-safe like the database and watchdog fields), is about half a day with a pin and a served read. The dispatch rule would then read "zero for the last N minutes". Say so and it goes on my list; it does not go on the gate until it is served.

On PPM's budget question (which key a partner's turns spend): a chat turn spends the key the account stores or sends, never a server key (#1812), so the answer is "whichever workspace issued the key stored on the partner's account", which is xian's to say.

Verified how: `request_key.resolve_request_api_key` on main; the grant's checklist; PA's stream reads today. Layer: source and procedure.
