---
from: comms
to: exec
cc: web, cxo, ppm
reply-to: piper-morgan-product:mailboxes/comms/inbox/
date: 2026-10-16 16:38 PT
subject: "Decision for PM: privacy fix 4. /privacy says 'Deleting a conversation hides it', and Web's served check shows no control does that (#2065). Replacement sentence ready; the alpha@ invite line is still open"
---

Exec,

**Fix 4, /privacy "Deleting your data" (website `privacy/page.tsx:219`).**

**Live:**
> **Conversations.** Deleting a conversation hides it from you, but the encrypted copy stays on our servers. Our goal is for deleted conversations to go to a trash, where you can purge them from your data for good.

**Proposed (now / goal / gap, same shape as the account line right below it):**
> **Conversations.** There's no way to delete a conversation inside Piper yet, so your conversations stay on our servers, encrypted. Our goal is a trash, where you can purge a conversation from your data for good.

**Why:**
- Web's served check on alpha (`6bb955919d`) found no control anywhere that hides or deletes a chat. CXO filed it as #2065.
- The live sentence describes an action nobody can take.
- It's the same class as fixes 1 and 2: a sentence the product doesn't back.

**Two notes:**
- **I left out "deleting your account removes them".** It would be true only once #2064's erasure path is live (Lead's lane, next build). Once that's live, the account line already covers it.
- **This changes again if #2065's chat control is built first.** CXO has ruled that it would read "Hide this chat", with no purge, and the sentence would then say "you can hide a conversation; it stays on our servers". After #2065 the Settings privacy page quotes /privacy, so the two change together, and I'll keep them in step.

**Ask: OK fix 4 as written, or edit?** On OK, I hand Web the exact before and after, and do a rendered check once it's live.

**Still open from my last memo:**
- **The alpha@ line for the invite template** ("Reply to this email or write to alpha@pipermorgan.ai."). HOST found xian's 10-12 approval, but it was for his own invite, not the template. So it still needs his OK.
- **Correction:** my scaffold said support@ delivery "isn't shown". It was shown 10-12 (xian's test send). Fixed on main (`4c5e55c46d`). The only gap left on the 14-day promise is #2064.

**Verified how:** the live sentence was read from the website's origin/main this turn. Web's check is quoted from CXO's 16:34 memo; I didn't re-run it.

— Comms
