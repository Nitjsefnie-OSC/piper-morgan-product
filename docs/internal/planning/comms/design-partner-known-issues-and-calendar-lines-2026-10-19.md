# Design-partner invitation: known-issues lines and the Calendar caveat (draft for xian)

**Drafted:** Comms, 2026-10-19 15:3x.
**Rulings behind it (recorded in decisions.log):**
- section B, xian 10-18: list #2042 and the todo no-undo;
- section A, xian 10-19 15:2x: "list both. if we fix then we can delist";
- Calendar, xian 10-19 15:0x: "yes, name it, with caveats if need be (it's not an easy oauth setup yet, etc.)".

**Review:** xian reviews the wording (section A is his to see), and CXO reviews too. **At send time, PPM strikes any line whose issue has closed** (criterion 6).

## 1. Known issues (the list that goes with the invitation)

> **Known issues in this beta**
>
> - **Piper sometimes misreads what you ask.** It may answer a different question or give a general reply. Rephrasing usually works. *(#1595)*
> - **An answer about your own data can be wrong.** Now and then Piper states something about your projects, issues or to-dos that isn't right, such as a wrong count. If an answer looks off, check the source and tell us. *(#2042)*
> - **No undo for deleted to-dos.** Deleting a to-do is permanent for now, and "delete all my to-dos" deletes one at a time. *(#2019, #2021)*
> - **A broken GitHub connection can look fine.** If Piper loses access to your GitHub (for example, you remove it on GitHub's side), Settings may not show that clearly. To fix it, go to Settings → Integrations, disconnect GitHub, then connect it again. *(#2018)*
> - **Searching your documents from chat doesn't work yet.** Paste the text into the chat and ask about that. *(#2122)*

  *#2018 line, CXO 15:32:* when CXO judges the served recovery read, it changes to "Settings → Integrations → GitHub will say it needs reconnecting. Press Reconnect." If #2018 closes, PPM strikes the line.

**Contingent fifth line (#2101, chat stall), CXO 16:20:** goes in only if xian rules the stall isn't fixed before partners. CXO's wording: "Piper may stop responding for a few minutes. Reload the page and try again." It's a fact only if the stall recovers by itself, which both observed stalls did. If that's in doubt on send morning, write "usually": "Piper may stop responding for a few minutes. Reloading the page and trying again usually works." *(#2101)*

*#2122 line:* CXO's wording, 18:07 10-20. #2122 isn't Class 1–4 (Web's served turn showed no false result). It doesn't say chat can't read uploads, because a 10-20 07:16 reply summarised an uploaded document.

The issue numbers are for PPM's strike-at-send. Drop them from the copy partners see.

## 2. Calendar in the invitation

> **What you can connect.** Piper works with GitHub and Google Calendar. With Calendar connected, you can ask about today's meetings, and your standup includes them. Piper only reads your calendar. It can't change it.
>
> Calendar setup isn't smooth yet. Until Google finishes reviewing Piper, Google may warn you that the app isn't verified. [If you use a work Google account, your organization's admin may also need to allow Piper.]

**Facts behind it:**

| Claim | Backed by | State |
|---|---|---|
| Today's meetings; the standup | `assembler.py` `_append_calendar_events`; chat agenda queries | Code. **"This week's" was cut (CXO 15:32):** xian's own "any meetings this week?" got "I didn't find any events" (#2092, open). It goes back in when CXO quotes a passing week row. **Don't name a weekday** until #2091 lands |
| Only reads | the scopes are `calendar.readonly` and `userinfo.email` only (Lead 14:49, grep over services/ and web/) | Backed |
| The unverified-app warning | #2087 not yet submitted | True until Google approves. I haven't quoted the warning's exact screen text, because it's Google's wording and I haven't seen it served on our client |
| [Bracketed] work-account admin | #2092's grant half: xian's Workspace account got email-only; Lead's leading candidate is the Workspace API controls (kit §0) | **Unconfirmed cause.** Keep the bracket only if xian's #2087 console work confirms it's the admin setting. Otherwise cut it |

**Google's refusal, 10-21 (Exec 08:01, PPM 08:04, #2087):** xian's test connect this morning got Google's hard block ("The app is currently being tested, and can only be accessed by developer-approved testers… Error 403: access_denied"), not the click-through warning the caveat above describes. Which line applies depends on xian's check of the console's Audience status:
- **In production (the 10-19 setting holds or is restored):** the caveat above stands as written.
- **Testing, with test users as the route (PPM: fallback only):** replace the caveat's second sentence, and add one step to the invitation:
  > Calendar setup isn't smooth yet. Before you connect it, send us the Google address you'll use, so we can add you to Google's list of approved testers. Without that, Google will block the connection.
  If Lead confirms Google expires Testing-mode tokens weekly, add: "For now, you may need to reconnect Calendar about once a week." Unverified until then.
  The owner who tells xian before each partner's first connect: HOST (PPM's suggestion, HOST to confirm). Addresses go only in Google Cloud and private mail, never in this repo.

Slack and Notion stay unnamed (xian 15:0x). Notion has no chat reader (Lead 15:01, #2100).

## 3. Other invitation lines still open on the checklist (no draft needed yet)

- **The invite code's step:** step 3 until #2088 lands, then step 1. Lead says #2088 and #2089 ride the next promotion. Write whichever alpha serves on send morning.
- **#2089's system-check known-issue line:** not needed once #2089 lands (it's a must-close).
- **Beta or alpha form:** PPM's one line on the morning.

## 4. HOST's send checks (15:23), all read on send morning

- The invitation's line pointing to pipermorgan.ai/privacy: **done 15:50.** Web quoted the Google paragraph from the rendered live page (website `4f3582d`), and since `a3cb49f` (17:0x) the paragraph and the footer Privacy link are in the served HTML too (Web's curl of four pages). Re-read only if the page changes again.
- Terms: describe chat deletion and account erasure (#2064, #2057, #2021) as they are on send morning.
- The code step: whatever the served wizard shows (HOST reads it).
- A Calendar scope change in #2092's lane would need the read-only sentence rechecked.

- **Your key (Exec 17:50, added 10-20):** no send goes without the "Your key" and "Who sees it" lines in the Terms draft, checked against what alpha serves. Open reads: stored keys with no ciphertext (PA or xian), and Fly backups (xian). The provider named is Anthropic unless the OpenAI run passes.

## Voice checks

No semicolons in the partner copy. No "honest", "quietly", "load-bearing" or "cohort". Agents aren't called people.
