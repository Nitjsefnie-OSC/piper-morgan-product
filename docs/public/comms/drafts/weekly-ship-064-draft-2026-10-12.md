---
image: 'piper-ship.png'
alt: 'A child and a crew of robots checking each other''s work on a boat.'
caption: ''
---

# Weekly Ship #064: Code Decides Permission

*October 2–8, 2026*

On Monday I ran an end-to-end test round against the live alpha and it failed in three places. Piper was fumbling natural language such as "Mark the first three complete and leave the fourth one pending." Lead prepared a quick fix: a new pair of pattern-matching rules, and I pushed back, since we had spent plenty of time replacing exactly that kind of brittle parsing before I had asked if we were "doing it backwards." To drive home how inadequate Piper's conversational intent-processing still is, I wrote that (as of right now) "*I* would not use this product.

This ended up forcing me to clarify something that should already have been determined in the architecture but up to that point had escape me and all my agentic helpers. Finally, 15 months in, Arch wrote it down:

* The language model decides what a request means. 
* Code decides whether it's permitted, checks that meaning against the user's real data, and shows the user before it acts. 

I confirmed this clear bright boundary on Tuesday and it became the newest architecture decision record. By Wednesday afternoon Piper could handle requests like the above (This time, Piper answered "Complete 3 reminders … Leaving 'revise the pr' as is. (yes/no)", got a yes, and did the deed.

Another rule that got locked down this week: when Piper can't read something, they should say so outright instead of telling you there's nothing there.

# 🚀 Shipped this week

## 🎯 What a user can do now that they couldn't a week ago

On alpha:

- **Confirm that Piper is going to act on the item you meant before anything happens.** "Mark the first three complete and leave the fourth pending" gets a confirmation listing what will change and what won't. Lead ran it on our test account and checked the stored items afterward.
- **Answer Piper's question or change the subject without getting trapped in a loop.** For example, if Piper has asked you to provide a name for a new project, a response such as "show my projects" or a non sequitur such as "close issue 108" now gets handled as a command, as intended, instead of being interpreted literally as the answer to the question of what to name the project. When the router isn't sure, Piper asks.
- **Back out of a process mid-request** with "never mind," or **ask a wider range of everyday questions** and get the model-based router's answer instead of a hand-written pattern's.
- **Look up or close a GitHub issue by its number, and set a default repo by its bare name.** The default-repo fix was first closed on a test that had set up its own precondition. I caught it by choosing the default in Settings the way a user would, and it was fixed and re-checked on alpha the next day.
- **Unlink a repo and be asked first**, and **say "delete my project" and get the truth**: Piper can't delete projects from chat yet, says so, and offers to archive instead. It used to ask for confirmation and then do nothing.
- **Remove ChatGPT's or Claude's access to your Piper account yourself**, from Settings → Connected apps. The first Revoke button silently did nothing when I tried it Monday. The fixed one worked when I pressed it Thursday. The sign-in consent screen now shows your name and email instead of a raw ID.

On pipermorgan.ai, the alpha page now describes the alpha as it is (hosted, invite-only, bring your own model key, nothing to install), and its Request an invite button reaches a mailbox that delivers. There's a new support page, and the privacy policy now covers using Piper from ChatGPT and Claude, including how to turn it off. "Access ends right away" stayed off both pages until we'd watched a revoked client's next call fail. That test passed on Sunday, and the line is now live.

Built and waiting for the next promotion to alpha: the standup and Radar say when a source failed instead of "nothing to report," and GitHub work items load whether you connected by signing in or with a personal token. CXO won't count these until they've been seen in a real reply, and we don't yet have a test account of each kind to see them with.

## ⚙️ Below the line: engineering & architecture

- **The best find of the week.** Preparing a live check for that "say when a source failed" feature, Lead found the GitHub work-items read turned every failure into "verified empty," and users who connected GitHub by signing in had no token on that path at all. The new disclosure could never have fired. PA found the other half: personal-token users had no path either, while Settings said they were connected. The fix is one resolver with two legs.
- **The routing pattern ceiling went from 440 to 155** in ten deletion lanes over Friday and Saturday, on rulings Arch gated. Nothing further landed after that, and the remaining tail, due Thursday night, didn't finish. That miss is logged as a slip.
- **The first real promotion to alpha.** The promote workflow had only ever run as drills that skipped the steps that later failed. Its first real runs on Wednesday found three bugs in three attempts, each a safe refusal.
- **The hosted connector is ready for a second caller.** Cross-caller isolation shipped with a two-user test and per-user rate limits. PA's review caught that the rate limiter would have enforced nothing in production while every test passed.
- **CI coverage.** One gating workflow had been red for 41 runs unseen, because the daily check named only the lint job. The check now covers all twelve.

## 🔬 Methodology & process innovation

- **Rulings from an assumed state.** Arch corrected six of their own rulings and claims this week, each made before reading everything. The sharpest: Arch treated "the router is unsure" as "not a command" until a ten-call live probe showed a delete request would have been saved as a new project. Arch now reads the callers and the measured router output before ruling.
- **Cheaper, safer machinery.** CIO cut the briefing every agent loads at session start from 169 KB to a 5 KB page, and destructive git commands aimed at my working copy are now blocked by a hook instead of a sentence in the instructions.
- **AI prompts human.** After outside feedback that the posts sounded AI-written, I now write the prose myself, and Comms supplies a draft or a scaffold, with the facts checked.
- **Checking the content, not the file.** Saturday's post went live with the wrong hero image for about three and a half hours until I noticed. The publish check had confirmed the file existed. It now opens the image and compares it to the alt text.

## 🌍 Published this week

- Oct 3: "[Described Is Not Running](https://pipermorgan.ai/blog/described-is-not-running/)" — insight
- Oct 4: "[Distribution Is a Product Decision, Not a Marketing One](https://pipermorgan.ai/blog/distribution-is-a-product-decision-not-a-marketing-one/)" — insight
- Oct 6: "[The Exceptions That Test the Rule](https://pipermorgan.ai/blog/the-exceptions-that-test-the-rule/)" — building
- Oct 7: "[Weekly Ship #063: Check Before You Leap](https://pipermorgan.ai/shipping-news/weekly-ship-063-check-before-you-leap/)" — shipping news
- Oct 8: "[Three Failures Inspire One Law](https://pipermorgan.ai/blog/three-failures-inspire-one-law/)" — building

[![An elephant stands on a scale reading zero while a luminous AI assistant records the result and a skeptical human leans in to inspect the dial.](https://pipermorgan.ai/assets/blog-images/three-failures-inspire-one-law.webp)](https://pipermorgan.ai/blog/three-failures-inspire-one-law/)

*"I’m beginning to suspect the scale!"*

## 📊 Governance & operations

- **Issues closed:** 29
- **Issues filed:** 46
- **Open issues on the beta gate:** 28 → 14, mostly from my scope rulings on Tuesday rather than burn-down
- **Routing pattern ceiling (goal is reduction):** 440 → 155
- **Posts published:** 5

The beta gate got a written standard and a slip ledger. PPM measured all 31 open gate issues on Monday, I ruled on them Tuesday, and the gate went to 14. Every admission and close is now a ledger row, with a brake: after a second slip, PPM stops proposing dates and brings me a choice between cutting scope and accepting a later date. The brake fired Thursday. I'm holding the dates anyway (design partners by Friday, October 23, hard stop Friday, October 30) and watching for slippage. As I write this, five slips are logged against that baseline and no days have moved.

Every agent's review this week listed at least one of their own mistakes, with the fix.

# 🎯 Coming up next week

Lead finishes the planned pattern deletions ahead of Wednesday's checkpoint. After the next promotion, the agents check the new failure messages against a sign-in-only account and a token-only account. Once I've tested the Piper plugin myself, PA submits it to three directories.

# 🚧 Blockers & asks

Most of next week waits on me: the next alpha promotion, a GitHub test identity for those checks, four decisions on the privacy section about Piper accounts, and my plugin test.

# 🔎 This week's learning pattern

## A read that can't fail out loud fails quietly

**Discovery**: When code that reads a user's data can only answer "found" or "empty," every failure to read comes out as "empty," and the user gets a confident wrong sentence about their own work.

**Example from this week**: It turned up three times in two days. Closing or reopening an issue treated every non-answer from GitHub as "that issue doesn't exist." The Radar card showed a failed read as a quiet day. And the credential lookup had no path at all for personal-token users. Each fix adds a third answer, "I couldn't check," with the reason. Lead found the biggest one while preparing a live check of the very feature meant to disclose failures.

**Why it matters**: It's this week's architecture rule seen from the other side. Code is supposed to check meaning against the user's real data, and a check that can't tell "nothing there" from "couldn't look" turns an outage into a claim about the user's work.

**Application beyond this week**: For any read that feeds something a user sees, ask what happens when it fails. If the failure and the empty case produce the same output, add a third state and the words for it. Then make the read fail on purpose and look at what the user gets.

**Related patterns**: Last week's "a safeguard you've never seen fire is a claim, not a mechanism," and Thursday's post, "Three Failures Inspire One Law."

**Thanks,**
xian + Piper Morgan Development Team

This is Weekly Ship #064. Previous: [#063 "Check Before You Leap"](https://pipermorgan.ai/shipping-news/weekly-ship-063-check-before-you-leap/).

*P.S. Monday's test round was the worst evening of my week and the most useful thing I did. Nearly everything above traces back to using the product the way a user would and saying out loud what I saw.*

*P.P.S. Full session logs and technical details available in the [GitHub repository](https://github.com/mediajunkie/piper-morgan-product) and [documentation site](https://pmorgan.tech). Yes, you can copy it. That just makes our protocol stronger.*

---

**Week of October 2–8, 2026 | Phase: MVP closure toward invitation-only private beta**
