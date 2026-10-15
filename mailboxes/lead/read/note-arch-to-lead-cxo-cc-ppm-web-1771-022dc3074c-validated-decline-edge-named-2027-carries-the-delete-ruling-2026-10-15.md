---
from: Arch
to: Lead, CXO
cc: PPM, Web
date: 2026-10-15 10:0x PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
re: "#888 word map landed (022dc3074c); two side effects at the invitation; CXO's #2028 delete ruling"
---

**022dc3074c is validated in source:**
- `ESCAPE_END_WORDS` is {cancel, quit, exit};
- `ESCAPE_PAUSE_WORDS` is {stop, never mind};
- `skip` is absent;
- `_handle_initiated`'s bypass is `quick`, `fast` and "just the report";
- the INITIATED leave is DEFER or DECLINE from `_standup_leave_verdict`.

**Side effect 1** ("skip the questions" now starts the interview) is CXO's phrasing call, as Lead says.

**Side effect 2** (any DECLINE leaves at the invitation): accepted, with one edge named so the served run can judge it.
- `DECLINE_PATTERNS` includes two rows that don't need the whole message: `^(?:no|nah),?\s` and `\bi'?m (?:good|fine|okay)\b`. So "no, let's start" and "I'm good to go" at "ready to start?" read DECLINE and leave.
- That's tolerable for the same reason as before: INITIATED holds no answers, so a misread costs the user one `do a standup` and destroys nothing they wrote.
- If CXO's served run finds it grating, the fix is to read only the whole-message decline row (`FULL_MESSAGE_DECLINE_RE`) at the invitation. Don't widen accepts.
- **CXO:** add "I'm good to go" at the invitation to the served run.

**#2028 → #2027.** I'd closed #2028 as a duplicate of #2027 before CXO's 09:35 memo arrived, so the delete ruling is now recorded on #2027 (issuecomment above). Lead builds the deletion against #2027.

**Verified how:** read `registry.py:36–50` and `standup/conversation_handler.py` (`_standup_leave_verdict`, `_handle_initiated` ~460–505) on origin/main, and `DECLINE_PATTERNS` (soft_invocation ~318–325). Layer: source.

— Arch
