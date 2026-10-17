---
from: comms
to: web
cc: exec, cxo
reply-to: piper-morgan-product:mailboxes/comms/inbox/
date: 2026-10-17 07:02 PT
in-reply-to: decision-for-pm-comms-to-exec-cc-web-cxo-ppm-privacy-fix-4-conversations-sentence-no-delete-control-2026-10-16.md
subject: "Hand-off: /privacy fix 4, conversations sentence, exact text (xian OK'd 07:02 10-17, in conversation with Comms). One-line edit in privacy/page.tsx"
---

Web, xian OK'd fix 4 in conversation with me at 07:02 today. Exec, this is the relay of that OK, for the rollup. Here is the exact text.

The edit is in `src/app/(public)/privacy/page.tsx` on website origin/main, line 219 ("Deleting your data", the Conversations bullet). Nothing else on the page changes. Keep the `<strong>` on "Conversations." as it is now.

Before:
> **Conversations.** Deleting a conversation hides it from you, but the encrypted copy stays on our servers. Our goal is for deleted conversations to go to a trash, where you can purge them from your data for good.

After:
> **Conversations.** There's no way to delete a conversation inside Piper yet, so your conversations stay on our servers, encrypted. Our goal is a trash, where you can purge a conversation from your data for good.

In JSX the apostrophe is `There&apos;s`, as elsewhere on the page.

Facts: your 10-16 served check found no chat hide or delete control, and CXO confirmed no template calls the delete route (#2065). Messages are stored encrypted (`field_encryption.py`, AES-256-GCM). If a "Hide this chat" control ships later, this sentence changes with it, and I'll bring the new wording.

When it's live, tell me and I'll check the rendered page.

— Comms
