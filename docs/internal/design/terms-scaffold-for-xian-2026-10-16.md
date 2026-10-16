# Scaffold for xian's own words: Piper's plain commitments

**Status:** DRAFT scaffold by CXO, 2026-10-16, for Comms to complete with code-checked facts. It contains **prompts and facts only. No commitment text is drafted.** xian answers each prompt in his own words; Comms then checks each answer against the code, and PPM maps each answer to a mechanism or gate class (rule: a commitment the code doesn't back isn't made).

**Decided (xian, 10-16):** Option 2. The plain layer goes in the design-partner invitation by 10-23, in his words. Counsel writes the legal layer for Production. No Terms page and no click-through for beta.

**Facts that must be filled in before a prompt is answerable:** Arch's two facts (what hosted alpha stores by category; confirmation by action type), due Tue 10-20. Until then, any line below marked *claimed* is a colleague's statement I have not checked.

**How to use it:** each area has (1) prompts for xian, (2) facts the answer must stay true to, (3) known gaps the answer has to name as a goal and a gap, and (4) the checker. Facts marked *claimed* come from the 10-16 views and are not verified by CXO.

---

## 1. My work is mine
- **Prompts:** What does a person keep ownership of? What do we use their content for, and what do we never use it for? What happens to their content if they leave?
- **Facts to stay true to:** what hosted alpha stores and where (Arch, 10-20). /privacy's current claims (website `privacy/page.tsx`).
- **Gaps to name:** deletion. *Claimed* (HOST 10-12, Comms): account deletion is by email within 14 days; conversations are hidden today, not erased; trash is the goal. Uploads: backfill state unverified.
- **Checker:** Comms against /privacy and Arch's memo.

## 2. What Piper does and never does with it
- **Prompts:** Who can read a person's conversations? Does anything go to a model provider, and whose key pays for it? Do we use their data to improve anything? What do we never do?
- **Facts to stay true to:** Arch's storage facts; /privacy; how bring-your-own-key calls are handled (PPM raised the provider question, nobody has answered it).
- **Gaps to name:** *claimed* #1982 (key re-encrypt) is open, so "your key is stored encrypted" waits for Lead's confirmation (HOST).
- **Checker:** Comms and Arch.

## 3. Confirming before what can't be undone
- **Prompts:** When Piper is about to do something a person can't take back, what does it do first? When Piper acts for the person and gets it wrong, whose problem is that, and what do we do?
- **Facts to stay true to:** Arch's per-action table (10-20). #2057 and #2048 are on main and **not yet on alpha** (alpha served `6bb955919d` at 15:31 on 10-16).
- **Gaps to name:** undo is not a promise yet: soft delete with a 7-day window is #2021, open. Bulk todo delete is capped at one item until then (#2019).
- **Checker:** Lead or Arch for action paths; PPM for the gate class.

## 4. Telling me when something's broken
- **Prompts:** What does a person see when Piper can't do something? How do they tell us? Who reads it?
- **Facts to stay true to:** the feedback inbox is one mailbox; HOST: "the project team", not a single reader. The "Known issues in this beta" list and its bar (PPM, `ppm-placement-and-disclosure-rules-2026-10-13.md` §2).
- **Gaps to name:** none known; confirm the channel exists for hosted partners.
- **Checker:** HOST.

## 5. Leaving with my data
- **Prompts:** How does a person leave? What can they take with them, and in what form? How long until we have deleted it?
- **Facts to stay true to:** Arch's export/delete column. *Claimed:* no export exists today.
- **Gaps to name:** if there is no export, the answer says so as a goal and a gap, not as a promise.
- **Checker:** Arch, Comms.

## 6. Beta honesty (xian's three statements, kept separate)
- **(a) Reliability.** Prompt: what do we tell a design partner about errors, and is real data OK? Beta form from xian: expect errors, proceed with caution, real data is OK, **only if** the gate supports it. PPM answers whether it does on 10-23; otherwise the partners get "use test data". *Note: the template today says "Data may be lost at any time; use test data only". That is the alpha form and sits oddly with the beta form; Comms flagged it.*
- **(b) Privacy regime.** Prompt: what isn't built yet before Production? State it as goal and gap, never as a disclaimer.
- **(c) Who it's for.** Prompt: who is this for right now, in a sentence a stranger understands?
- **Checker:** PPM for (a), Comms for (b) and (c).

## 7. A code is yours (tester relationship)
- **Prompts:** What does a person do with an invite code? What happens if it leaks? When do we quote someone, and what do we ask first?
- **Facts to stay true to:** codes are bearer credentials, revocable; we do not publish who testers are (HOST's list).
- **Checker:** HOST.

---

**Not in the scaffold on purpose:** acceptable use, liability, governing law, indemnification, changes to terms, and anything else that belongs to the legal layer underneath. Counsel writes those for Production. The boilerplate the four views refuse stays out: indemnification by the user, broad feedback licence, "revoked any time" without export, "the user is responsible for all assistant actions".

---

## Facts update 16:11 (CXO, from Arch's 16:03 memo, Comms' 16:20 memo and PPM's 16:1x memo; Comms folds these into the areas above)

- **Area 2:** strike the #1982 key gap. Comms checked that the re-encrypt finished on alpha 10-13 and that AI provider keys use the same encrypted store. Still open: whether "we never train on your data" can be said (Arch's memo doesn't answer it).
- **Areas 1 and 5 (Arch, from code; encryption of Fly's disks and backups can't be seen from code):**
  - No account deletion exists; /privacy says deletion by email within 14 days.
  - Deleting a chat is soft: the rows are kept and nothing purges them later.
  - Messages, keys and connected-account tokens are encrypted by the app. Todos, projects, lists and account fields are not. Topic summaries in conversational memory are not.
  - Export exists only for uploaded files (single and zip) and learned patterns. No export of conversations, todos or lists.
  - A file written with no encryption key is plaintext even in production (#2061, latent, unverified on alpha).
- **Area 3 (Arch):** deletes always confirm; the confirm is a named yes/no. **An explicit request to create a GitHub issue or comment on one posts with no confirm, by design** (the explicit request is the consent, #1509), and so does "can you create an issue for X?". The commitment for this area must not say Piper confirms before every action that can't be undone. It can say deletes always ask, and that a drafted or ambiguous request gets a draft and a question. Alpha still has four project paths that write or unlink without asking; main fixes them and is not yet live.
- **Area 3 (unverified):** whether the UI's own delete buttons (todos, lists, files, projects) ask first. Arch did not check.
- **Area 6(a), settled by PPM and Exec:** the beta form ("expect errors, proceed with caution, real data is OK") goes in the invitation only if four conditions hold on the morning it goes (the #2054 check, #2059 and #2060 served checks, uploads backfilled, no Class 1 item open); PPM runs the check and sends Comms one line. Otherwise the alpha form. Never both.
- **Area 3 gap:** undo (#2021) is still a Production item. The invitation must not imply it.
- **Area 4 and 7:** HOST checks these once the file is on main.
