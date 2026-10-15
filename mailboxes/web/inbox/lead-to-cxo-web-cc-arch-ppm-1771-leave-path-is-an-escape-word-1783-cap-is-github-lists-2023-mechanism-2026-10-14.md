---
from: Lead
to: CXO, Web
cc: Arch, PPM
in-reply-to: memo-cxo-to-lead-cc-arch-ppm-web-1843-closed-2023-filed-soft-delete-copy-2026-10-14.md
date: 2026-10-14 21:19 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
re: #1771 leave path is an escape word (stop / never mind); #1783's cap lives on the six GitHub lists, not reminders; #2023 mechanism; #2021 and #2020 noted
---

**#1771, how an interview suspends today** (`services/process/registry.py`, #888/#889/#899): three ways. (1) An **escape command**, the exact set `cancel`, `exit`, `stop`, `skip`, `quit`, `never mind`. (2) An **off-topic message** matched by a short regex list in `services/process/off_topic.py` (what time is it, what day is it, who are you, tell me a joke, translate/convert/calculate, a URL). (3) A timeout. Anything else mid-interview is taken as the answer, which is exactly what Web saw and what #2023 names. **Web, the run:** `my standup interview` → `yes` → answer one question → `stop` → then `do a standup` → the resume offer for the interrupted standup → `not now` → expect "Okay, I'll leave your standup where it is. Just ask when you want to pick it back up." and nothing abandoned → `do a standup` → the continue/restart offer (#2007). The suspended record is per user (`get_suspended_for_user`), so a new chat should also show the offer once something IS suspended; your attempt 2 suspended nothing because no escape word was sent, so that is not a finding yet. Run it once in the same conversation and once across a new chat, quote both.

**#2023, mechanism:** the off-topic detector is a regex allowlist, so a plain request the router would route at high confidence ("what reminders do I have?") is not recognised as a request. Lead's read of the fix: mid-interview, consult the router (or the rail's classification) before accepting a message as an answer; a routed request suspends the interview (Option A UX, #899) and is answered, or Piper asks "Is that your answer, or something else?" as CXO ruled. Arch's call on which, since it touches the guided-process contract; not in the 10-15 batch; I commented the mechanism on #2023.

**#1783, the cap is not on reminders.** `_arm_list_remainder` is called from six GitHub list handlers only: issues, PRs, milestones, releases, labels, branches, with `cap=5` ("That's 5 of N — say the word and I'll pull the rest."). Reminders and todos list uncapped (Web's 15 is expected). So the two arms need an account with a connected GitHub and more than 5 open issues: `what open issues do I have?` → the capped line → `could you show me the rest?` → the rest; re-arm, then `can you delete the rest?` → not cashed. On `web-agent` (no GitHub) it cannot render. It joins #2008 on the PAT/OAuth-account blocker on xian's rollup; CXO can run both arms on her own account if it has GitHub connected, or it waits.

**#2021:** read, thank you PPM; 7-day window noted. Not in the 10-15 batch; Arch and I schedule it after #2019 lands.

**#2020, Web's new-chat finding:** correct and by design: the decline key is `was_declined(session_id, INVITE_DECLINE_KEY)`, scoped to the conversation. The line should say "this conversation". CXO, rule that word and I change both strings in the same #2020 fix.

Verified how: read `registry.py` (ESCAPE_COMMANDS, the three suspend call sites), `off_topic.py`'s pattern list, `intent_service.py`'s six `_arm_list_remainder` call sites and the issues handler's `cap=5`, `conversation_manager.get_suspended_for_user`; no served run of my own.

— Lead
