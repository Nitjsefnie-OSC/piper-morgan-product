---
image: 'piper-ship.png'
alt: 'A child and a crew of robots checking each other''s work on a boat.'
caption: ''
---

# Weekly Ship #065: The Truth About State

*October 9–15, 2026*

The list of issues standing between us and the beta went from fourteen to six this week, and the target beta date (October 30) has not moved. Alpha was updated eight times, and most of what changed was verified on the hosted running build, by the agents and by me, before counted as done.

Looking back over the week, nearly every user-facing fix was a variation on one theme: Piper saying what is actually true right now. *Is your GitHub connection working? What is actually due today? What did that delete just do?* Last week we clarified that code decides what's permitted. This week Piper got better at telling you the state of things, including when it doesn't know.

The team learned a similar lesson about itself. Written rules kept slipping but rules checked by a script held.

# 🚀 Shipped this week

## 🎯 What a user can do now that they couldn't a week ago

On alpha:

- **See the truth about a broken GitHub connection**, in chat, in the standup, on the Radar card and in exports, and reconnect. PA and I ran this check together on my account. On Wednesday, all four places Piper reads GitHub wrongly said all was clear. On Thursday, all four told the truth. Long lists are now capped, and Piper offers the rest instead of dumping everything.
- **Get useful answers about today.** Overdue items come with counts and ages ("1 day overdue"), and "Today:" lists what's actually due.
- **Delete with a safety check.** "Delete that reminder" deletes exactly one. "Delete the first two reminders" picks the right two. Any request to delete more than one at a time gets a short list of what would go, ending "Nothing has been changed."
- **Exit the standup in your own words.** "Stop," "never mind" and "not now" pause it and keep your answers so far. "Cancel" ends it, and "skip" skips a question.
- **Ask Claude about your GitHub issues through the Piper Morgan MCP connector** and get the real total, with Piper clear about when a list has been cut short. I checked this one myself.

On [pipermorgan.ai](https://pipermorgan.ai/privacy), the privacy policy has a new section on your Piper account, and the site also picked up stronger keyboard-focus rings, a fixed skip link in dark mode, and some contrast fixes.

Not yet: disconnecting an integration passed on the two pages we could test. The other three need a connection we don't have yet, so the issue stays open for now. A fix for current-format Anthropic keys in Settings is closed in code, but has not been tried it on alpha yet.

## ⚙️ Below the line: engineering & architecture

- **Hand-written phrase-matching rules: 155 → 90.** Most of last week's unfinished tail, with Arch ruling which ones were safe to delete. Twenty-nine of the remaining ninety are a permanent floor. The other sixty-one wait on the language model's routing getting good enough to replace them.
- **Two real test accounts.** With invites and custody rules from HOST, Web set up one account connected to GitHub by signing in and one by personal token, so the agents can check both kinds of connection on alpha instead of just reasoning about them.
- **Red builds that never shipped.** Lead's pushes turned our main branch red on six of seven days, each time from tests that the pre-push check didn't select. No red build reached alpha. Each was fixed the same day, and from Tuesday the release check refused any build whose tests hadn't passed. CIO also found that 91 of the last 100 code-quality runs had been cancelled before finishing, so "green" had meant very little until Thursday. That's now fixed.
- **Checked before ruling.** Arch's "0 of 11 entry points" turned out to be 21 when counted. Every review this week named scope mistakes like that one, caught either by the agent who made it or by another.

## 🔬 Methodology & process innovation

- **Rules in prose don't hold. Scripts do.** Seven of the ten agents wrote clock times they had guessed instead of looked up, some off by as much as four hours. The rule says to check the clock first, and it's been written down for months. Separately, the Friday request for each agent's weekly review got missed two Fridays running. (Right after this sprint window closed, both became checks in code: the Friday request now sends itself, and the mail tool refuses a memo stamped in the future.)
- **Cost follows turns.** CXO noticed that what we spend tracks how many times the agents wake up, far more than which model they run. On one busy day CXO woke 41 times, and 20 of those were only to read copies of mail meant for someone else. We're changing copies like that to wait for the agent's next scheduled wake.

I must say that relying on scripts for critical rules has been a bit of a game changer and relieves me of a lot of worried reminding or anxious noticing that a rule I thought was being followed has been ignored again.

## 🌍 Published this week

- Oct 10: "[No Undo](https://pipermorgan.ai/blog/no-undo)" — insight
- Oct 11: "[It Doesn't Count if You Skip It](https://pipermorgan.ai/blog/it-doesnt-count-if-you-skip-it)" — insight
- Oct 13: "[Giving It Away, and Wondering Who May Want It](https://pipermorgan.ai/blog/giving-it-away-and-wondering-who-may-want-it)" — building
- Oct 14: "[Weekly Ship #064: Code Decides Permission](https://pipermorgan.ai/shipping-news/weekly-ship-064-code-decides-permission/)" — shipping news
- Oct 15: "[The Overzealous Cleanup Routine](https://pipermorgan.ai/blog/the-overzealous-cleanup-routine)" — building

[![A smiling AI waiter carries two untouched, steaming dinners away as one diner reaches after her meal and the other stares at the bare table, utensils poised.](https://pipermorgan.ai/assets/blog-images/the-overzealous-cleanup-routine.webp)](https://pipermorgan.ai/blog/the-overzealous-cleanup-routine)

*"Are you forgetting something?"*

## 📊 Governance & operations

- **Issues closed:** 56
- **Issues filed:** 78
- **Open issues on the beta gate:** 14 → 6
- **Updates to alpha:** 8
- **Hand-written routing rules left (goal is reduction):** 155 → 90

The slip ledger grew from three entries to seven, and no days moved. October 23 is when I decide whether we're on track to invite design partners, and October 30 is still the target for the first one to get access.

<!-- Exec: the plan's weekly usage peaked at 88% two weeks running, and API spend was about $41 for the week, mostly Lead's router scoring. Include, or keep it internal? -->

# 🎯 Coming up next week

Close what's left on the gate and get it checked on alpha, so that on October 23 I can judge whether we're on track. <!-- #066 boundary: by publish day (Wed 10-21) xian will know more. Update this paragraph then, without claiming #066 work as #065's. -->

# 🚧 Blockers & asks

Mostly me again: test rounds on each new alpha build, and one invite code per fresh test account.

# 🔎 This week's learning pattern

## A rule nobody checks is a wish

**Discovery**: A rule that exists only as written instructions gets followed until the moment of pressure, and then it doesn't. A rule that a script checks keeps working on the busiest day.

**Example from this week**: Agents guessed timestamps all week despite a written rule. The Friday review request was missed despite being on a checklist. The release check, which is code, has kept untested builds off alpha since Tuesday.

**Why it matters**: It's the team's version of what Piper learned this week. Piper started telling the truth more reliably once telling the truth became code, with a third answer, "I couldn't check," built into the reads. The team became more reliable where reliability became a check.

**Application beyond this week**: When the same correction comes up twice, stop rewording the instruction. Ask what could check it, and build that.

**Related patterns**: Last week's "A read that can't fail out loud fails quietly," and "It Doesn't Count if You Skip It."

**Thanks,**
xian + Piper Morgan Development Team

This is Weekly Ship #065. Previous: [#064 "Code Decides Permission"](https://pipermorgan.ai/shipping-news/weekly-ship-064-code-decides-permission/).

*P.S. <!-- xian: your P.S., if any. --> *

*P.P.S. Full session logs and technical details available in the [GitHub repository](https://github.com/mediajunkie/piper-morgan-product) and [documentation site](https://pmorgan.tech). Yes, you can copy it. That just makes our protocol stronger.*

---

**Week of October 9–15, 2026 | Phase: MVP closure toward invitation-only private beta**
