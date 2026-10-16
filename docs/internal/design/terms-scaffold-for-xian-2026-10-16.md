# Scaffold for xian's own words: Piper's plain commitments

**Status:** scaffold started by CXO, completed by Comms 2026-10-16 (facts folded in from Arch's 16:03 memo, PPM's gate reply and Comms' code checks). It contains **prompts and facts only. No commitment text is drafted.** xian answers each prompt in his own words; Comms then checks each answer against the code, and PPM maps each answer to a mechanism or gate class (rule: a commitment the code doesn't back isn't made).

**Decided (xian, 10-16):** Option 2. The plain layer goes in the design-partner invitation by 10-23, in his words. Counsel writes the legal layer for Production. No Terms page and no click-through for beta.

**Facts state (Comms, 16:3x 10-16):** Arch's two facts (storage by category, confirmation by action type) arrived early (16:03) and are folded in. Every fact below cites its source. Still open, named in each area: "never train" (Arch); #2064 erasure path (area 5); #2065 chat control and Settings privacy page (areas 1, 3, 5). Areas 4 and 7 checked by HOST 16:19. Next: Comms sends this to Exec for xian. He answers in his own words; Comms checks each answer against the code.

**How to use it:** each area has prompts for xian, the facts the answer must stay true to, the gaps it has to name as goal and gap, and the checker.

---

## 1. My work is mine
- **Prompts:** What does a person keep ownership of? What do we use their content for, and what do we never use it for? What happens to their content if they leave?
- **Facts to stay true to:**
  - Encrypted by the app when stored: messages, AI provider keys, connected-account tokens (Arch 10-16; /privacy "encrypted when stored").
  - **Not** encrypted by the app: todos, projects, lists, account fields, topic summaries in conversational memory (Arch 10-16). An answer must not say "everything you put in Piper is encrypted".
  - Encryption of Fly's disks and backups can't be seen from code. Don't claim it either way.
  - Stored on Fly.io in San Jose (/privacy).
- **Gaps to name (goal and gap):**
  - Uploads: encrypted since 07-08 when the key is set; files written while the key was unset are plaintext until the backfill runs (count mode on main, xian runs it after Fly recovers). Also #2061: a file written with no key is plaintext even in production (latent, unverified on alpha).
  - Deleting a chat hides it; the rows are kept and nothing purges them later. Goal: a trash you can purge (/privacy). **There is no screen control to hide or delete a chat** (Web's served check on alpha `6bb955919d`, 10-16; the API route exists and nothing calls it; #2065). An answer must not say a person can delete a chat themselves. If a control is built before a real purge, CXO has ruled its label "Hide this chat".
- **Checker:** Comms, against /privacy and Arch's memo.

## 2. What Piper does and never does with it
- **Prompts:** Who can read a person's conversations? Does anything go to a model provider, and whose key pays for it? Do we use their data to improve anything? What do we never do?
- **Facts to stay true to:**
  - Messages go to the provider the person connected (Anthropic or OpenAI) **with their own key**. There's no shared Piper key (/privacy; #1812, `provider_selection.py`).
  - From then on the provider's own privacy terms apply (/privacy).
  - Admin tools don't display conversations; the decryption key is a server secret, so "no one can read them" is **not** claimable (/privacy source notes).
  - Server logs keep no message text once #2059 is live (/privacy; #2059 rides the waiting promotion).
  - No analytics or ad tracking in the app once #2060 is live (/privacy; Chroma telemetry off).
- **Gaps to name:**
  - "We never train on your data": no training or fine-tuning code found (`git grep` over services/ and web/, Comms 10-16). But "never" is a promise about the future, and Arch hasn't stated it. If xian wants it, Arch confirms first.
  - ~~#1982 key re-encrypt~~: struck. It finished on alpha 10-13 (legacy=0, `user_api_key_service.py:35-42`).
- **Checker:** Comms and Arch.

## 3. Confirming before what can't be undone
- **Prompts:** When Piper is about to do something a person can't take back, what does it do first? When Piper acts for the person and gets it wrong, whose problem is that, and what do we do?
- **Facts to stay true to (Arch 10-16, per action type):**
  - Deletes always confirm, with a named yes/no.
  - A drafted or ambiguous request gets a draft and a question.
  - **An explicit request to create a GitHub issue or comment on one posts with no confirm, by design** (the explicit request is the consent, #1509), and so does "can you create an issue for X?".
  - Bulk todo delete is capped at one item (#2019, closed).
- **Must not say:** "Piper confirms before every action that can't be undone". The GitHub path makes that false.
- **Gaps to name:**
  - Undo is not a promise yet: soft delete with an undo window is #2021, open, on Production. The invitation must not imply undo.
  - Alpha still has four project paths that write or unlink without asking. Main fixes them; they go live with the waiting promotion (#2057, #2048 are still open).
  - Unverified: whether the UI's own delete buttons (todos, lists, files, projects) ask first. Arch didn't check. No chat-delete control exists on alpha (Web's served check, #2065). Settings' "Export/delete data" page says "Coming Soon" and lists options with no buttons; #2065 fixes it.
- **Checker:** Lead or Arch for action paths; PPM for the gate class.

## 4. Telling me when something's broken
- **Prompts:** What does a person see when Piper can't do something? How do they tell us? Who reads it?
- **Facts to stay true to:** the feedback inbox is one mailbox, read by "the project team", not a single reader (HOST). The "Known issues in this beta" list and its bar (PPM, `ppm-placement-and-disclosure-rules-2026-10-13.md` §2). For design partners, xian's 10-16 bar: privacy and security items closed, everything else disclosed as a known issue after xian and PPM review the list.
- **Facts (HOST, 10-16):** the channel exists: alpha@pipermorgan.ai reaches the alpha team (xian reads, HOST watches), per `docs/ALPHA_KNOWN_ISSUES.md:143`, plus a public GitHub issue (line 144).
- **Gaps to name:** the invite template doesn't name alpha@ or any way to report (its only prompt, line 79, has no address). The answer and the invitation should both name alpha@. Don't name support@ for reports: its delivery is unverified (HOST).
- **Checker:** HOST.

## 5. Leaving with my data
- **Prompts:** How does a person leave? What can they take with them, and in what form? How long until we have deleted it?
- **Facts to stay true to:**
  - **Current state, ruled by xian 10-13 and live on /privacy (quote it as is; nobody re-asks, Exec 16:18):** no account deletion inside Piper yet; "email support@pipermorgan.ai and we'll delete your account and everything in it within 14 days"; deleted conversations aren't purged yet, and the goal is a trash with a real purge.
  - **The promise isn't backed yet:** no erasure path exists in code. A user delete fails on 13 foreign keys, and 13 more tables (conversations and messages among them) would be orphaned (#2064, Arch; admitted to MVP; Lead's lane builds `erase_user.py` for the next build). support@ delivery *was* shown: xian's test send landed 10-12 (HOST's 10-12 memo; HOST's 16:2x doubt withdrawn). Not shown: who reads support@ day to day. The answer may restate the ruled promise; Comms marks it backed once #2064 is live.
  - Export exists for uploaded files (single and zip) and for learned patterns and learning settings (`GET /controls/export`, `web/api/routes/learning.py:803`).
  - **No export** of conversations, todos or lists (Arch).
- **Gaps to name:** "You can take your files and what Piper learned about you. Exporting your conversations and to-dos is the goal." (That's the fact, not the wording. xian words it.)
- **Checker:** Arch, Comms.

## 6. Beta honesty (xian's three statements, kept separate)
- **(a) Reliability.** Prompt: what do we tell a design partner about errors, and is real data OK?
  - Alpha form: not reliable yet, use test data.
  - Beta form: expect errors, proceed with caution, real data is OK.
  - **Rule (PPM + Exec, 10-16):** the invitation carries the beta form only if four conditions hold on the morning it goes: #2054 closed on a served check; #2059 and #2060 closed on served checks (incl. #2059's third pass); uploads backfilled with zero plaintext; no Class 1 item open. PPM runs the check and sends Comms one line. Otherwise the alpha form. **Never both in one invitation.**
  - xian answers both forms, so whichever the check picks is in his words.
- **(b) Privacy regime.** Prompt: what isn't built yet before Production? State it as goal and gap, never as a disclaimer. Inputs: chat purge (trash), in-app account deletion, conversation export, undo window. Wording that fails: "use at your own risk". Shape that works: "Before Production we'll add X. Today Y is true."
- **(c) Who it's for.** Prompt: who is this for right now, in a sentence a stranger understands?
- **Checker:** PPM for (a), Comms for (b) and (c).

## 7. A code is yours (tester relationship)
- **Prompts:** What does a person do with an invite code? What happens if it leaks? When do we quote someone, and what do we ask first?
- **Facts to stay true to (HOST, from code, 10-16):**
  - A code works **once**: redemption is atomic, and the first person to redeem gets the account (`invite_token_service.py:61-64`).
  - **No expiry and no revoke flag.** An unused code stays valid until used or deleted. "Revoke" means an operator deletes the unused row on prod by hand. Don't write "revocable" unqualified, and don't promise a time limit.
  - Once used, a code can't be taken back: the account exists.
  - We don't publish who testers are, **from now on** (rule 8). Older files still carry some given names, and xian ruled no history rewrite (10-16), so an answer mustn't deny that.
  - Quoting a tester needs their say-so. That's a practice with no mechanism behind it; say it as a practice. Counsel reviews before any outside user beyond the design partners (#2063, xian 10-16).
- **Checker:** HOST.

---

**Not in the scaffold on purpose:** acceptable use, liability, governing law, indemnification, changes to terms, and anything else that belongs to the legal layer underneath. Counsel writes those for Production. The boilerplate the four views refuse stays out: indemnification by the user, broad feedback licence, "revoked any time" without export, "the user is responsible for all assistant actions".

*Facts update (CXO 16:11) folded into areas 1–6 by Comms 16:3x and removed.*
