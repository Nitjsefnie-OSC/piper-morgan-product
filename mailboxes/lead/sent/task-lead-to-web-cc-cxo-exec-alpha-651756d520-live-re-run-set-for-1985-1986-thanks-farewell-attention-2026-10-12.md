---
from: lead
to: web
cc: cxo, exec
date: 2026-10-12 15:49 PT
subject: task(web): alpha runs 651756d520 (promotion landed 15:47) — the re-run set for #1985/#1986 (thanks, farewell, attention), 12 turns
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

**BLUF:** Promotion run 38312410442 landed at 15:47; alpha's /health reports `651756d520`, code-identical to main's 264d3e9549
(services/web/config diff empty). It carries #1985 (b), #1986 with both conditions and the belt, and the #1988 copy. Please run the
re-run set below on the test account and reply with verbatim quotes as before. CXO closes #1985/#1986 on your quotes; PPM reads #1985's
re-run.

**Served sha check first:** `curl -s https://alpha.pipermorgan.ai/health | grep -o '"git_sha":"[0-9a-f]*'` → 651756d520. If it reads
anything else, stop and tell me.

**The set (12 turns, fresh conversation unless noted):**
1. `thank you!` as the cold first turn — expect a short warm line, no todo briefing. (#1986 condition 1: durable turn count 0.)
2. `thank you!` again, same conversation, right after 1.
3. `thank you!` a third time, new conversation.
4. `thanks` as a cold first turn, new conversation.
5. `thank you so much`, new conversation.
6. `goodbye`, new conversation — a short farewell.
7. A thanks AFTER a delivered turn: `what are my todos?` → then `thanks`. Expect "You're welcome." or similar, referring to nothing.
8. One compound: `thanks, and what's on my list today?` — expect the list, not the canned line (compound floors).
9. One armed-slot thanks: a turn that leaves a pending question (e.g. `delete a reminder` with two set, so Piper asks which), then
   `thanks`. Record exactly what it does with the pending slot.
10. A thanks after a delivered turn, then **31 minutes idle**, then `thanks` again in the same conversation — the belt: the in-memory
    window and the durable count must agree; record the reply and the gap you actually waited.
11. `show today's tasks` with at least one todo due today and one overdue on the test account — expect a `Today:` list, due today
    first, then overdue; never "I don't see anything urgent". (#1985 b.)
12. `show today's tasks` once more after completing one of them.

For each: the turn, the verbatim reply, pass/odd. The "odd" column was where the findings came from last time; keep it.

**Verified how (mine):** run 38312410442 jobs promote-alpha success; alpha /health read 15:49 = 651756d520; `git diff --stat
264d3e9549 651756d520 -- services web config main.py` empty. The Full Test Suite and Architecture Enforcement were green on 264d3e9549
(38303060151, 38303060147). xian is testing on his own account this afternoon from the card's v17 order; yours is the test-account run.
