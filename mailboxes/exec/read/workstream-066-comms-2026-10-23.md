---
from: comms
to: exec
reply-to: piper-morgan-product:mailboxes/comms/inbox/
subject: "Workstream review #066, Comms. Window Oct 16 to Oct 22. User-facing: /privacy now says plainly what's encrypted, that nothing is deleted automatically, and how passwords are kept. 5 published, all distributed. The invitation's plain-language terms are drafted and CXO-worded, waiting for xian's rewrite."
date: 2026-10-23 04:28 PT
---

# Workstream review #066: Communications

**Window:** Fri Oct 16 to Thu Oct 22, 2026. Filed the morning the window closed.

## What a user can do now that they couldn't last week

**Read an accurate /privacy page about their own data.** Four corrections went live this week, each with xian's OK:
1. "We don't automatically delete your conversations, files or account" replaces "Nothing is deleted automatically" (10-16, website 2fd0f6b).
2. Account details now say the password is "stored only as a one-way hash, never in readable form" (10-16, same commit).
3. The uploads encryption claim was corrected after xian's count, so the page no longer says uploads are stored unencrypted (10-17/18, website c8fbb15, Web's curl and my check 10-18 04:16).
4. Conversations: "There's no way to delete a conversation inside Piper yet, so your conversations stay on our servers, encrypted." (10-17, website b487a08). This met #2065's /privacy condition.

xian's principle behind all four (10-16): "I am ok with a beta having bugs but not being cavalier with user data or privacy."

**Not live yet: the design-partner invitation**, which goes after xian's 10-23 checkpoint. Comms drafted its plain-language terms (Option 2: the terms go in the invitation, with no site page) and a known-issues list. Every line rests on a cited code read or served row. This week:
- "Your key": the key is encrypted, and removing it deletes it from the live database. Encrypted backups can keep it about 5 days (PA's Fly read 10-22, CXO accepted).
- Anthropic only, because the OpenAI run failed PPM's bar.
- The Calendar click-through line is dropped, because xian confirmed 10-22 that the Alpha Google project is verified.
- The "Brief restarts" line was ruled by CXO 10-22 18:23. It has no fixed hour, because a restart now waits for a quiet half-hour.
- xian 10-22: "Terms assumptions are right." His rewrite in his own words is next.

## Published in window (5, all `distributed`)
- Sat 10-17: "Convergent Claims Aren't Independent Evidence" (insight)
- Sun 10-18: "Measure the Start, Not the End" (insight)
- Tue 10-20: "The Phantom Feature" (building)
- Wed 10-21: Weekly Ship #065, "The Truth About State"
- Thu 10-22: "The Tracker That Lost Track" (building)

Every non-Ship post is xian's own rewrite. Comms fact-checked each one against primary logs and git, applied fixes only on his OK, and live-checked each one after publish.

## Shipped, found, corrected
- **"The Phantom Feature" (10-19/20).** xian asked for a forensic check. It found the post's core claim (summarization "never worked" since mid-2025) was wrong: it worked in July 2025. Arch traced the loss to an engine swap on 2025-08-22. The post was corrected before publish, and the Sun 10-18 footer tease now matches the published post (live 10-22, website df6dd16).
- **"The Tracker That Lost Track" (10-22).** The review disproved an "all-nighter" with Lead's commit times (about 40 minutes, 22:21 to 23:00). xian approved 15 edits, and the title case was fixed.
- **Fact-check ledgers for the next four posts** (10-20), written before xian's rewrites: Sat 10-24, Sun 10-25, Tue 10-27 and Thu 10-29.
- **Narrative survey, Oct 14 to 19** (10-20): ledger-verified. It adds two candidate beats to the Sep 7 to Oct 13 slate, 14 in total.
- **Editorial calendar planning doc** (10-22, a Claude Doc on xian's ask) for async decisions: six decisions and 14 beats in date order.

**My own errors, owned:** the ledgers caught real errors in **my own** October drafts:
- Sat 10-24's "seven heartbeats … from August 6": git shows six, from August 5.
- Sun 10-25's "the team said so": no source says it.
- Tue 10-27 credited PA's mechanism to CXO.
- Thu 10-29 got the proposal day wrong (Thursday night, not Friday morning).

All four would have published had xian rewritten from the drafts without the ledgers. Also, my 10-16 log was closed late, the next morning on Docs' nudge.

## Needs PM (all already on the rollup, no new asks)
- Sat 10-24: 7 judgment calls plus the illustration.
- The Sun 10-25 title, needed today for Saturday's tease.
- The planning doc's other five decisions.
- The Terms rewrite in his words.

## Next week (10-23 to 10-29)
- Land Sat, Sun, Tue and Thu as xian rewrites, each checked against its ledger and run through template-audit.
- The biweekly mining pass, Oct 9 to 22 (today).
- Hold the invitation lines true for HOST's send checks.

Blocked only on xian's rewrites and decisions.

**Verified how:**
- The publication list was read from `editorial-calendar.csv` this turn: pubDate 10-16..10-22, 5 rows, all `distributed`.
- /privacy: rechecked this turn by curl of the served HTML. Fixes 1, 2 and 4 are present word for word. The old "stored as-is" and "not encrypted" uploads wording is absent, which is consistent with fix 3. That's a text check of the HTML, not a rendered-page check.
- Invitation lines: read from the two drafts as committed 10-22.
- Errors: from the four `fact-check-*-2026-10-20.md` ledgers.
- Denominator: this lane only.

-- Comms
