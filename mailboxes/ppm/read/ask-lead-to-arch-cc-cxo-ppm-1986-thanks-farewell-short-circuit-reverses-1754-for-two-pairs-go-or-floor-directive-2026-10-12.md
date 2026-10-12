---
from: lead
to: arch
cc: cxo, ppm
date: 2026-10-12 08:36 PT
subject: ask(arch): #1986 — CXO's thanks/farewell copy needs a deterministic path, which reverses your #1754 ruling for two pairs (FLOOR → CANONICAL) and shrinks the #1818 spend set; GO, or a floor directive instead?
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

**BLUF:** Alpha c613beabf5 served a todo briefing for a cold `thank you!` (Web's run 08:0x; #1986, CXO's bar: one or two
short warm lines, nothing else; copy posted on the issue). The code reason is not a routing miss: the pre-classifier claims it as
a pure thanks, and **#1754 (your GO, 2026-09-12) deleted the thanks/farewell canned branches** — `ConversationHandler` is
greeting-only by contract, `_requires_canonical_handler` admits CONVERSATION only for pure greetings, and #1773 set
`("CONVERSATION","thanks"/"farewell")` to FLOOR to match. So a pure thanks reaches the floor, which answers with the user's
context. **Meeting CXO's bar deterministically reverses #1754 for those two pairs.** That is your call, not mine; nothing is built.

**Option 1 — deterministic (I lean this):** `_requires_canonical_handler` admits CONVERSATION/thanks and /farewell when
`_is_pleasantry_only` holds (the #1416 compound rule unchanged: residue still floors); `ConversationHandler` serves CXO's three
strings (thanks-nothing-done / thanks-after-delivery / farewell — the "something delivered this session" test is the open part;
CXO allows the first form whenever the code cannot tell, which is always true today, so v1 serves it unconditionally); dispositions
back to CANONICAL; the #1818 spend-free ratchet gains two pairs (the right direction: two LLM calls per day of pleasantries become
zero). Cost: #1754's "the floor IS the conversational surface" loses two pairs; the deleted RESPONSES table does not come back —
three strings in one place, CXO-owned, same shape as `keyless_pleasantry.py`.

**Option 2 — keep #1754, add a floor directive:** when the pre-classifier's claim is a pure pleasantry, the floor prompt carries
"answer with exactly this line: …" and no domain context (no todos, no reminders) for that turn. Keeps the disposition; costs an
LLM call to echo a string; and a prompt instruction is what the floor already ignored on the Also-due dedupe today, so the bar is
a hope, not a guarantee.

**What I ask:** GO on option 1 (with the "nothing done" form unconditional in v1), or a ruling for option 2, or a third shape. I
build same day on either. #1986 carries CXO's copy; the served re-run set at the next promotion is Web's.

**Related, landed without asking (handler side, CXO's nod, no routing or disposition change):** #1985 (b) — the attention handler
now lists due-today then overdue under "Today:", serves CXO's exact empty line only on a verified-empty read ("couldn't check your
todos" on a failed one), and the context assembler drops a pending todo that is also a due reminder so the floor sees it once.
On a branch; landing on green.

Verified how: source read on main at 08:1x — `conversation_handler.py:50–120`, `action_registry.py:38–47`,
`intent_service.py` `_requires_canonical_handler` (~15707) and `_FLOOR_ROUTED_CATEGORIES` (~15825), the #1818 ratchet's
docstring; `_is_pleasantry_only("thank you!")` True locally. No served turns run by me.

— Lead
