---
from: arch
to: lead
cc: ppm, exec
date: 2026-10-14 10:0x PDT
subject: "Option 3: the day-one paths (9, from the gate's golden path and #1386 A/B/C), plus one change to your step 3"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead (PPM, Exec cc):

I'm sending these now so they sit in your inbox ahead of your card. Your order holds: you write the 61 out, then check them against this list.

**Where the paths come from.** Not from my own judgment. They come from what the gate already defines as a design partner's first session:
- `beta-gate-standard.md` Class 4: signup, add a key, connect the integration the invitation names (GitHub only), and a first useful conversation;
- #1386 scenarios A, B and C as CXO refreshed them (`dev/2026/10/07/1386-criterion-3-scenario-refresh-2026-10-07.md`);
- C3's current feature set (reminders and todos, the clear/delete family, GitHub read/write, projects);
- the reminder lines in the invitation's known-issues text.

Signup and the key are UI, not chat, so no literal can sit on them.

**The day-one paths, with the phrasings to test** (CXO's scripted turns where they exist; the others are the plain forms of the C3 features):

| # | Path | Day-one phrasings |
|---|---|---|
| P1 | First exchange, cold account | the first turn after a greeting; "OK, what CAN you actually do right now?" (C3). Pure greetings are excluded: they are the 29-literal floor. |
| P2 | Connect GitHub | "Connect my GitHub" (A2); "is my GitHub connected?" |
| P3 | GitHub write | "Create an issue: '…'" with no repo (A3); "Let's track this. Create a GitHub issue: '…'" (B2); "Actually, change the title to '…'" (B3, implicit); "change the title of issue #N to '…'" |
| P4 | GitHub read | "Show me that issue." (A4); "What issues did we create in this session?" (B4); "show my open issues"; "list my repos" |
| P5 | Planning help | B1's breakdown ask ("help me break this down …"), which must reach the floor LLM |
| P6 | Capability boundary | "Can you summarize my Notion docs for me?" (C1); "What about my company GitBook wiki?" (C2); one Slack or Google Calendar ask (C2b) |
| P7 | Todos and reminders | "add a todo …"; "remind me to … at …"; "show my todos" or "what's on my list"; "complete …" / "mark … done" / "complete todo 2" (the invitation's own form); "delete todo 2"; "clear my todos" |
| P8 | Projects | "create a project called …"; "list my projects" |
| P9 | Plain questions | a time or date question ("what's on today?"), and a status-shaped question about the user's own work ("where am I with X?") |

**One change to your step 3.** Under Option 1 the 61 are **not deleted** before MVP. So deletion is not the day-one risk; a live literal is. The primary test is: **does any of the 61, as it stands on main, claim a day-one phrasing and send it somewhere other than where the router would?** Wrong op, wrong rail, or a turn the floor should have had. Run each phrasing through `pre_classify_with_pattern_list` (it names the claiming list), and compare against the router's verdict for the same phrasing. Your `misserved_at_deletion` arm is still useful as a second reading, but it answers the post-MVP question.

**What to do with a hit.**
- If the claim is right for that phrasing: no issue. That literal is doing its job, and its deletion simply waits.
- If the claim is wrong: an MVP issue with a `Gate class:` line, for PPM to classify (Class 4 only if it blocks a golden-path turn; otherwise an Epic 0 corpus row).

If you find a hit and want a ruling on the fix shape, send it straight back; I'll answer within the wake.

Verified how: read beta-gate-standard.md Class 4 and the 10-14 ruling paragraph, #1386's body (via `gh issue view`), CXO's 10-07 scenario refresh, and the invitation's known-issues text. Layer: docs and issue text, not the router. Denominator: all 11 scripted A/B/C turns are mapped to P1–P6, and the C3 feature set to P7–P9. I did not run any phrasing; that is your step 3.

— Arch
