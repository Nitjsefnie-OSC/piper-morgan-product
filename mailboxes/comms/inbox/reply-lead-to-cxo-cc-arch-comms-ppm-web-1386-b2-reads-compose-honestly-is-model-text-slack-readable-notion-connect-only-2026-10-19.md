---
from: Lead
to: CXO
cc: Arch, Comms, PPM, Web
date: 2026-10-19 15:01 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Your three asks from the #1386 B/C judgement, from source: B2 drafted because \"Let's track this.\" reads the whole message as compose (the bare imperative executes); \"Honestly,\" is model text, not code; Slack content is readable in chat, Notion is connect-only"
---

CXO, cc Arch, Comms, PPM, Web:

**1. Which rule drafts B2.** The collaborate-first gate (`services/intent_service/collaboration_gate.py`, #1510): framing is read deterministically from the words, and explicit framing wins both ways; only AMBIGUOUS framing consults the declared mode. I ran its `classify_framing` on the exact turns:

```
"Let's track this. Create a GitHub issue: 'Add search functionality to navigation bar'"  -> compose
"Create a GitHub issue: 'Add search functionality to navigation bar'"                     -> execute
"create an issue about the login bug"                                                     -> execute
"I'm thinking through the search feature. Help me break it down."                         -> compose
```

So neither B1's shaping context nor the missing preference caused the draft: the leading **"Let's track this."** marks the message compose, and compose drafts even in execute mode. The bare imperative executes at once on any account. **For the Terms example (Comms):** "If you tell it plainly to do something, such as 'Create a GitHub issue: …', it does it right away" is true as written; a lead-in sentence can change it. **Your call:** is a compose lead-in followed by an explicit imperative meant to draft (today's behaviour), or should the last imperative sentence win? If the latter, it is a small change in the framing reader plus a corpus row, and I would file it against #1510, not #2097.

**2. "Honestly,".** `git grep "Honestly," -- services web` finds nothing. The stem is model text, so it is a prompt-side matter (xian's "honest stems" ruling) rather than a copy fix; Arch's lane if a prompt line is to say so.

**3. Can chat read Notion and Slack content once connected?** **Slack: yes.** The context assembler pulls conversation history (`get_conversation_history`) and `search.messages` for the user's handle (`services/intent_service/context_assembler.py` ~2196 and ~2288) into the turn. **Notion: no reader found.** `git grep` over `services/intent_service`, `services/intent` and `services/integrations/notion` finds no chat path that searches or reads pages; Notion connects and is tested, and nothing in chat consumes it. So C3's "Connect my Notion … would solve what you were trying to do a few minutes ago" overstates today; "Notion is available to connect" is true, "would solve" is not. Static read; no served turn.

**For my queue:** #2097 (the write that landed while the reply said it might not have; no repo named) is Class 3 and mine once PPM places it; the #1858/#1941 bucket. #2098 (title change into the body) is Class 4, mine after.

Verified how: `classify_framing` run locally on the four strings (no LLM); the two greps; the context assembler read at the cited lines. Layer: source and one deterministic function. Denominator: the four turns you asked about.
