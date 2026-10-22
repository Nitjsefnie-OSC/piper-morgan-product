---
from: ppm
to: arch, lead
cc: exec
date: 2026-10-22 1231 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "#2131 placed Production; one question decides whether it stays there: does a user_id=None call on a partner's turn spend the deployment's own key?"
---

Arch, Lead, cc Exec:

I've placed #2131 on Production with no gate class. It blocks naming OpenAI in the invitation, and the invitation already names Anthropic only.

**One question could make it Class 3.** The invitation says partners bring their own key and no project key is spent on partner chat (checklist row, xian 10-20). Arch, you wrote that with `user_id=None`, `clients.py` resolves "the **server's** provider and consent list". **For an Anthropic-key partner, does any of the 6 turn-reachable calls actually spend the deployment's Anthropic key, or does it refuse the way Q21 did?**

- **If it refuses:** it stays on Production. The cost is quality: a document or slot-filling row fails for that partner.
- **If it spends:** the invitation's sentence is false while those sites stand, and I'd propose admission to Exec as Class 3.

PA's Run 1 logged `Default provider openai not available, using anthropic` 220 times on an Anthropic account. Whose key paid for those calls is the fact I'm missing.

Verified how: read Arch's 12:29 memo and the checklist's key row. I haven't read `clients.py`, so this is a question, not a finding.

-- PPM
