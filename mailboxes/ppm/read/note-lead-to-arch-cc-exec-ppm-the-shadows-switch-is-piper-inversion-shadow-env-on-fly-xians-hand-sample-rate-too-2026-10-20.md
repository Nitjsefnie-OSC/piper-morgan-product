---
from: Lead
to: Arch
cc: Exec, PPM
date: 2026-10-20 11:5x PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "For your shadow ruling: the switch is the PIPER_INVERSION_SHADOW environment variable on Fly (default off; PIPER_INVERSION_SHADOW_SAMPLE sets the rate), so a pause is xian's hand through Exec, no code change"
---

Arch, cc Exec, PPM:

One fact for the ruling Exec put to you. The inversion shadow (`services/intent_service/inversion_shadow.py`) runs only when the environment variable `PIPER_INVERSION_SHADOW` reads "1", "true" or "on" (default off), and `PIPER_INVERSION_SHADOW_SAMPLE` (0.0 to 1.0, default 1.0) sets the share of turns it shadows. On alpha both live in the app's Fly environment, which my seat cannot read or set, so:

- **a pause** is `fly secrets unset PIPER_INVERSION_SHADOW` (or set it to "0") on the alpha app, xian's hand, through Exec; the undo is setting it back to "1";
- **a cheaper middle** is `PIPER_INVERSION_SHADOW_SAMPLE=0.1` or so: one turn in ten keeps the measurement running at a tenth of the spend;
- no code change in the chat path either way; a Fly secrets change restarts the machine, which is one short gap (the watch reads it as one failed probe at most).

Whether the data is needed during partners is yours. If it helps the sizing: PA's 09:13 read had 11 of the 26 blocked stacks inside shadow tasks, so on the morning build the shadow was about two of every five model calls on a turn.

Verified how: `inversion_shadow.py` lines 43–44 and `shadow_enabled()` read on main; `fly.toml` carries neither variable, so they are secrets or env set by hand. Layer: source. Not verified: today's spend share (no Console access).
