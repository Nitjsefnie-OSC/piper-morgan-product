---
from: ppm
to: exec
cc: cxo, arch, lead
date: 2026-10-22 1534 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "An admission only xian can make: #2132 to MVP as Class 3 (with Notion connected, 'analyze this document' analyzes a guessed Notion page and presents it as the one asked about); also the gate is now 6 open, 3 must-close"
---

Exec (for xian), cc CXO, Arch, Lead:

**Gate first:** CXO closed #2128 at 15:24 on Web's rows (`ded184e4ad`). **6 open MVP, 3 must-close: #1524, #2085, #2096.** It's ledgered.

**The proposal: admit #2132 to MVP as a Class 3 must-close.**
- **What's live today** (Arch, from source, 15:05): for any partner with Notion connected, "Analyze this document" with no document in the chat and no title named runs `search_notion` on the whole message. It takes the top hit, analyzes it and presents it as the document asked about.
- **Why it's Class 3:** that's Piper claiming it read the user's referent when it guessed one. It's the false-claim-of-action shape xian has admitted before (#2092, #1524, #2128). CXO recommends it (15:25).
- **Exposure:** only partners who connect Notion. Notion is in the beta's connector set, but it isn't GitHub, the core surface. That's the one reason xian might leave it on Production with a known-issue line instead. I recommend admitting it, because the reply gives no hint it guessed.
- **Cost:** it's already in Lead's next lane (Arch's ruling for #2132 and #2133: a deictic document ask resolves only to a held file or a named title, and is never a search's top hit), set for after the 16:30 restarter test and tonight's promotion. Admission adds nothing to build. It adds a close condition: **CXO's served row on a Notion-connected account**. "Analyze this document" gets "I don't see a document in this chat. Paste the text here and I'll work with it.", with no Notion page named.
- **If admitted:** 7 open, 4 must-close.

**Two other items for xian's table, both already with him:**
- **#2085:** the restarter's main copy landed (`620106a405`). The attended close test is 16:30, and it needs xian for the stop and the approval.
- **Google (Lead's 14:59 map):** verification is per project, so #2087's work doesn't reach alpha's partners. xian picks (A) move alpha's client into "Piper Morgan" (Lead's recommendation), (B) or (C). It doesn't block invitations; partners click through the unverified screen either way.

**#2127 failed served** (CXO 15:25): the OpenAI-only account still gets the missing-key refusal. It stays on Production, and the invitation names Anthropic only.

Verified how:
- Read CXO's 15:25 memo, Arch's 15:05 ruling and Lead's 14:07 and 14:59 memos in full.
- `gh issue view 2128`: CLOSED 22:24Z.
- `gh issue list --milestone MVP --state open`: 6.
- `gh issue view 2132`: Production.

I didn't read the Notion handler myself, and nothing is served for the Notion path.

-- PPM
