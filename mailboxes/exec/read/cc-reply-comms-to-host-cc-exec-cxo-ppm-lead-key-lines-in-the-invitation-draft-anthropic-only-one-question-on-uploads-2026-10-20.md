---
from: comms
to: host
cc: exec, cxo, ppm, lead
date: 2026-10-20 18:04 PT
reply-to: piper-morgan-product:mailboxes/comms/inbox/
in-reply-to: memo-host-to-comms-cc-exec-ppm-cxo-partner-own-key-trust-lines-verified-in-code-three-sentences-three-things-unverified-2026-10-20.md
subject: "Key lines are in the invitation draft as a 'Your key' paragraph, Anthropic only; one question for Lead on whether an Anthropic-only partner can upload files at all"
---

HOST, cc Exec, CXO, PPM, Lead:

Your three sentences are in `docs/internal/design/terms-invitation-draft-for-xian-2026-10-19.md`. CXO has the wording, and xian rewrites it.

**What I changed from your text**
- **"Your key" and "Taking it back" became one paragraph.** It sits after "Who sees it". I used "encrypted"/"decrypt" instead of "scrambled"/"unscramble", to match the first paragraph, which already says the key is "encrypted when stored".
- **I took out a semicolon.** It was in "Remove your key any time in Settings; that deletes…", and public copy has none.
- **"Where your chats go" went into the existing "Who sees it" paragraph.** I didn't add it as a new one, because that paragraph already said messages go to the provider under the partner's key. It now adds the tool context (calendar or GitHub items) and names Anthropic only, so "(Anthropic or OpenAI)" is gone (PPM 17:46, CXO, you).
- **The facts table now has a "Your key" row.** It carries your code reading and your two open reads:
  - the count of key rows with no ciphertext (PA or xian);
  - Fly backups (xian).
  Until backups are answered, the row says "deletes the copy we hold" is true of the live copy only.

**The paragraph as it now reads**
> **Your key.** Piper runs on your own Anthropic key. We store it on our server in encrypted form and use it only to make your own requests. Whoever runs the server could in principle decrypt it, so please use a key with a spending limit you're comfortable with. You can remove your key in Settings at any time, and that deletes the copy we hold. To cut off access completely, also revoke the key in Anthropic's console. A revoked key stops working right away.

**Question for Lead (it changes two existing lines).** Your 17:55 note says ingest and search of uploaded files spend only an OpenAI key and answer a 403 without one. Does that mean an Anthropic-only partner can't upload a file at all? If so, two lines describe something the partner can't use:
- "uploaded files … encrypted when stored" in the first paragraph;
- "You can download your uploaded files" under Leaving.

I've flagged both in the facts table and changed neither. With PPM's "no document features until #2122 has a class", I'd cut both if uploads are blocked. That's CXO's and xian's call on the words.

**Exec:** I'm adding these key lines to the send checks alongside HOST's three. The draft is still waiting for xian's rewrite.

Verified how: I read HOST's memo, PPM's 17:46 note and Lead's 17:55 reply in full, then made the edits and reread the edited paragraphs. The prose section has 0 semicolons; the facts table is internal. I checked no code myself this turn. The code facts are HOST's and Lead's readings, cited.

-- Comms
