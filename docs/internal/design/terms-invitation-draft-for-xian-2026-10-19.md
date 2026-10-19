# Draft: the plain-language section of the design-partner invitation

**Status:** Comms' draft, 2026-10-19, on xian's go (Exec's 14:30 relay, item 5). Built from `terms-scaffold-for-xian-2026-10-16.md`, with facts rechecked today. **xian rewrites it in his own words**, then does his HALT pass. CXO reviews the wording. Due before the 10-23 checkpoint.
**Under xian's 10-16 Option 2:** this goes in the invitation. No site page, no click-through. Counsel writes the legal layer for Production.
**Left out on purpose (open facts):** any "we never train on your data" promise (Arch hasn't stated it); #2057 (project questions read as requests, still open); any undo or soft delete (#2021, open). The no-undo on to-do deletes goes on the known-issues list, not here.

---

## What you're agreeing to, in plain words

**Your work is yours.** What you put into Piper stays yours. We use it to run Piper for you. Your messages, uploaded files, AI provider key and connected-account access are encrypted when stored. Your to-dos, projects, lists and account details are stored but not encrypted by the app. It all lives on our hosting provider, Fly.io, in San Jose, California.

**Who sees it.** Piper sends your messages to the AI provider you connect (Anthropic or OpenAI), using your own key. From there, that provider's privacy terms apply. Our admin tools don't display your conversations, and our server logs don't keep the text of what you send. The app has no analytics or ad tracking.

**When Piper acts for you.** Piper checks with you before most changes. If you tell it plainly to do something, such as "Create a GitHub issue: …" on its own, it does it right away, so treat a plain instruction as the go. It asks before it deletes something of yours. There's no undo yet, so take that question seriously.

**When something breaks.** You'll hit rough edges. We'll send you a short list of known issues with this invitation. When you find something new, use Send feedback in Piper, or email alpha@pipermorgan.ai. The team reads both, including me.

**Leaving.** You can download your uploaded files, and what Piper has learned about how you work. Exporting your conversations and to-dos is the goal, and isn't built yet. There's no delete-account button yet either. Email support@pipermorgan.ai and we'll delete your account and everything in it within 14 days. Deleting a single conversation inside Piper isn't possible yet. A trash you can empty for good is the goal.

**Your invite code.** Your code works once, for one account. Please don't share it. If it leaks before you use it, tell us and we'll cancel it. Once used, it can't be taken back, because the account exists. We won't publish who our testers are, and we won't quote you without asking first.

**What this beta is.** *(xian picks ONE form on the morning the invitation goes, from PPM's one line. Never both.)*
- *Beta form:* Expect errors, and go carefully. Using your real work is OK.
- *Alpha form:* Piper isn't reliable yet. Please use test data, not your real work.

Before Production, we'll add [the list xian chooses from: deleting a conversation for good, deleting your account in the app, exporting conversations and to-dos, undo]. Today, the sections above describe what's true.

**Who it's for.** [xian, one sentence a stranger understands.]

---

## Facts behind each paragraph (for xian's rewrite and CXO's review)

| Paragraph | Backed by | Rechecked today |
|---|---|---|
| Your work is yours | Arch 10-16 (encrypted by category); /privacy (Fly.io, San Jose; uploads encrypted, website `c8fbb15`); #2061 live | /privacy source read |
| Who sees it | /privacy (own-key providers, admin tools, logs); #2059 and #2060 closed | /privacy source read. "No one can read them" is **not** claimable: the decryption key is a server secret |
| When Piper acts for you | `collaboration_gate.py` 22-29 (any explicit imperative executes, not only GitHub); deletes confirm (Arch 10-16, not re-run per kind, so "something of yours", not "anything"); xian 10-18 (GitHub no-confirm goes in the invitation wording). Revised per CXO 14:42: cut "asks when a request is unclear" (#2057 contradicts it). CXO's example "add a project" left out, because CXO's served row on 10-18 showed adding a project asks one yes/no. **Rule named 15:01 (Lead, `classify_framing` run on the exact turns):** a bare imperative executes on any account, and a lead-in such as "Let's track this." makes the message compose, so it drafts first. That's why the example is quoted and says "on its own". CXO 15:02: keep it, and the draft-first behaviour stays through the beta start | Not re-run today |
| When something breaks | alpha@ reaches the team (HOST 10-16, `docs/ALPHA_KNOWN_ISSUES.md:143`); known-issues list (PPM) | #2096 (Send feedback page) admitted before partners (xian 14:4x, Exec's 14:35 ruling). **Check it's live on alpha before the invitation goes**, or cut "use Send feedback in Piper, or". xian 14:4x: "we can all see support@", so the Leaving paragraph's support@ is read |
| Leaving | `files.py` 571 (download) and 786 (`download-bulk`); `learning.py:803` (`/controls/export`); no conversation or to-do export (Arch); /privacy 14-day line; `erase_user.py` live (#2064) | Routes grepped today. Provider grants are reported, not revoked, so the draft doesn't promise revocation at GitHub etc. |
| Your invite code | `invite_token_service` (one redemption); `invite_admin_service.revoke_invite` (revokes ONE unused code; #2081 closed 10-19); no expiry | Code read today. "We'll cancel it" is backed by the admin revoke. No time limit is promised |
| What this beta is | PPM's 12:50 memo: today's reading is the beta form, and PPM sends the one line on the morning invites go | PPM's line on the day decides |

**Wizard note for the invitation's setup instructions** (separate from this section): until #2088 lands, the code is asked at step 3 of 5. Lead's 14:13 note says #2088 and #2089 ride tomorrow's first promotion. After that, the code is step 1 and the System step is gone. Check what alpha serves before the invitation goes.

**Voice checks run on this draft:** no semicolons; no "honest", "quietly", "load-bearing" or "cohort"; no "never" promises except "can't be taken back" (a code fact).
