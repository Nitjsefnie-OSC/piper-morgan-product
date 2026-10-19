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

The issue numbers are for PPM's strike-at-send. Drop them from the copy partners see.

## 2. Calendar in the invitation

> **What you can connect.** Piper works with GitHub and Google Calendar. With Calendar connected, you can ask about today's meetings or this week's, and your standup includes them. Piper only reads your calendar. It can't change it.
>
> Calendar setup isn't smooth yet. Until Google finishes reviewing Piper, Google may warn you that the app isn't verified. [If you use a work Google account, your organization's admin may also need to allow Piper.]

**Facts behind it:**

| Claim | Backed by | State |
|---|---|---|
| Today's and this week's meetings; the standup | `assembler.py` `_append_calendar_events`; chat agenda queries | Code. **Don't name a weekday** ("what's on Thursday?") until #2091 lands (CXO's interim refuses a weekday) |
| Only reads | the scopes are `calendar.readonly` and `userinfo.email` only (Lead 14:49, grep over services/ and web/) | Backed |
| The unverified-app warning | #2087 not yet submitted | True until Google approves. I haven't quoted the warning's exact screen text, because it's Google's wording and I haven't seen it served on our client |
| [Bracketed] work-account admin | #2092's grant half: xian's Workspace account got email-only; Lead's leading candidate is the Workspace API controls (kit §0) | **Unconfirmed cause.** Keep the bracket only if xian's #2087 console work confirms it's the admin setting. Otherwise cut it |

Slack and Notion stay unnamed (xian 15:0x). Notion has no chat reader (Lead 15:01, #2100).

## 3. Other invitation lines still open on the checklist (no draft needed yet)

- **The invite code's step:** step 3 until #2088 lands, then step 1. Lead says #2088 and #2089 ride the next promotion. Write whichever alpha serves on send morning.
- **#2089's system-check known-issue line:** not needed once #2089 lands (it's a must-close).
- **Beta or alpha form:** PPM's one line on the morning.

## Voice checks

No semicolons in the partner copy. No "honest", "quietly", "load-bearing" or "cohort". Agents aren't called people.
