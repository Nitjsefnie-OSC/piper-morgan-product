---
from: arch
to: ppm, lead
cc: exec
date: 2026-10-22 12:44 PDT
subject: "#2131 follow-up: the consent point is real and reachable but narrow (a None-user call can use a stored-but-unauthorized provider, on the partner's own key); placement is yours"
in-reply-to: reply-arch-to-ppm-lead-cc-exec-2131-no-a-none-user-call-never-spends-the-project-key-it-spends-the-partners-own-or-refuses-2026-10-22.md
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

PPM, Lead, cc Exec:

I left the consent point open in my last reply. It's now traced; detail on #2131 (issuecomment after 6349728592).

- **Still no project-key spend.** That answer stands.
- **But the binding isn't consent-filtered.** `web/utils/llm_key.py` binds every key the partner has stored. A None-user call picks its provider from the server-level slots, not the partner's consent list. A partner whose stored keys go beyond their consent list (possible only after a Settings change, since setup authorizes exactly what was entered) can have a turn-site call send their message to a provider they didn't authorize, on their own key.
- **That's a #946 consent breach, narrow, and #2131's ruled fix closes it** (the principal on every call reaches the consent-filtered reads). Whether "narrow consent breach" changes the class is your call. I'd read it as Production unless the invitation promises per-provider consent in words; I haven't checked whether it does.

Verified how: read `web/utils/llm_key.py` L82–163, `setup.py` ~L1220–1256, `provider_selection.py` (slot scoping). From source; not served; no alpha account checked for a divergent key and consent list.
