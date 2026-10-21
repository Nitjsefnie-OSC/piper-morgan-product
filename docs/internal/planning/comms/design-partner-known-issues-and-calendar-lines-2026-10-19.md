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
> Calendar setup isn't smooth yet. Until Google finishes reviewing Piper, Google will show a screen saying "Google hasn't verified this app." That's expected for now. Click "Advanced", then "Go to Piper Morgan (Alpha) (unsafe)". On the next two screens, choose your account and click "Continue". [If you use a work Google account, your organization's admin may also need to allow Piper.]

**Facts behind it:**

| Claim | Backed by | State |
|---|---|---|
| Today's meetings; the standup | `assembler.py` `_append_calendar_events`; chat agenda queries | Code. **"This week's" was cut (CXO 15:32):** xian's own "any meetings this week?" got "I didn't find any events" (#2092, open). It goes back in when CXO quotes a passing week row. **Don't name a weekday** until #2091 lands |
| Only reads | the scopes are `calendar.readonly` and `userinfo.email` only (Lead 14:49, grep over services/ and web/) | Backed |
| The unverified-app screens and click path | xian's four screenshots, 10-21 10:0x, app "Piper Morgan (Alpha)", In production, unverified (Janus 10:2x, transcribed; PNGs in the private DinP repo, addresses blanked). Lead 09:38 quotes Google's page: In production with a sensitive scope shows the unverified-app warnings. Wording per CXO 09:48 (say what to do, in Google's exact words). Screen 4's one scope reads "See and download any calendar you can access using your Google Calendar", which backs "only reads" | Google's words are quoted from screenshots. **Recheck at send:** the app name in "Go to Piper Morgan (Alpha) (unsafe)" changes if alpha moves to the Piper Morgan project's client (PPM 09:34). Use the name the served screen shows that morning |
| [Bracketed] work-account admin | #2092's grant half: xian's Workspace account got email-only; Lead's leading candidate is the Workspace API controls (kit §0) | **Unconfirmed cause.** Keep the bracket only if xian's #2087 console work confirms it's the admin setting. Otherwise cut it |

**Which Calendar line goes (#2087, updated 10-21 10:3x):** the line partners get has to match what Google does on send morning. HOST's send check picks it, and HOST releases no send until xian has said which reading holds. **Neither line goes until Connect works for a Google account outside the Workspace domain** (CXO 09:48, PPM 09:34).
- **In production** (xian's Audience screenshot shows this today, PPM 09:34): use the caveat above, with the click path. This morning's "being tested" refusal came from elsewhere. Lead's client-ID read suggests alpha may be sending another project's client. If it is, PPM recommends rotating alpha to a new client in the Piper Morgan project, and the app name on the screens changes.
- **Testing** (fallback only): replace the caveat's second through fourth sentences with CXO's final wording (09:48):
  > Before you connect Google Calendar, send us the Google address you'll use. We have to add you to Google's list of approved testers first. Without that, Google blocks the connection. In this mode Google asks you to reconnect Calendar about once a week.

  Sourced: Google's refusal text (Web, Janus); the 100-tester cap and the 7-day refresh-token expiry are quoted by Lead (09:38) from Google's "OAuth app state overview". **HOST owns the per-partner step** (09:28): xian opens the partner's reply at alpha@, HOST tracks received/added only, and Exec relays to xian. Addresses go only in Google Cloud and xian's private mail, never in this repo.

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
