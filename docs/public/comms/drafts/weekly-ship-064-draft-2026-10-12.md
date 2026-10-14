---
image: 'piper-ship.png'
alt: 'A child and a crew of robots checking each other''s work on a boat.'
caption: ''
---

# Weekly Ship #064: Code Decides Permission

*October 2–8, 2026*

On Monday I ran an end-to-end test round against the live alpha and it failed in three places. Piper was fumbling natural language such as "Mark the first three complete and leave the fourth one pending." Lead prepared a quick fix: a new pair of pattern-matching rules, and I pushed back, since we had spent plenty of time replacing exactly that kind of brittle parsing ever since I asked whether we were "doing it backwards." To drive home how inadequate Piper's conversational intent-processing still is, I wrote that (as of right now) "*I* would not use this product."

This ended up forcing me to clarify something that should already have been determined in the architecture but up to that point had escaped me and all my agentic helpers. Finally, 15 months in, Arch wrote it down:

* The language model decides what a request means. 
* Code decides whether it's permitted, checks that meaning against the user's real data, and shows the user before it acts. 

I confirmed this clear bright boundary on Tuesday and it became the newest architecture decision record. By Wednesday afternoon Piper could handle requests like the above. This time, Piper answered "Complete 3 reminders … Leaving 'revise the pr' as is. (yes/no)", got a yes, and did the deed.

Another rule that got locked down this week: when Piper can't read something, they should say so outright instead of telling you there's nothing there.

# 🚀 Shipped this week

## 🎯 What a user can do now that they couldn't a week ago

On alpha:

- **Confirm that Piper is going to act on the item you meant before anything happens.** "Mark the first three complete and leave the fourth pending" gets a confirmation listing what will change and what won't. Lead ran it on our test account and checked the stored items afterward.
- **Answer Piper's question or change the subject without getting trapped in a loop.** If Piper has asked for a new project's name, replies like "show my projects" or "close issue 108" now run as commands instead of becoming the project's name. When Piper isn't sure which you meant, they ask.
- **Back out of a process mid-request** with "never mind," or **ask a wider range of everyday questions** and Piper's language model works out what you mean, instead of a hand-written rule matching your words.
- **Look up or close a GitHub issue by its number, and set a default repo by its bare name.** A default repo you choose in Settings is now recognized when you name it in chat.
- **Unlink a repo, with a confirmation step**, and get a true answer to **requests to "delete my project"**: Piper can't delete projects from chat yet, says so, and offers to archive instead. (It used to ask for confirmation and then do nothing.)
- **Remove ChatGPT's or Claude's access to your Piper account yourself**, from Settings → Connected apps. You can now revoke that connection from the Piper Morgan side rather than having to do so within your chat app. Also, the sign-in consent screen now shows name and email instead of a raw ID.

On pipermorgan.ai, the alpha page now describes the alpha accurately (hosted, invite-only, bring your own model key, nothing to install), and its Request an invite button is now wired to a working mailbox. There's a new support page, and the privacy policy now covers using Piper from ChatGPT and Claude, including how to turn it off. We held the claim that access ends right away back from both pages until we'd confirmed in a test, seeing a revoked client's next attempt fail. That test passed on Sunday, and the line is now live.

Built and waiting for the next release to alpha: the Standup and Radar features clarify when a source failed instead of "nothing to report," and GitHub work items load whether you connected by signing in or with a personal token. CXO won't count these until they've been tested in a real reply, which hasn't happened yet because there is a big testing backlog that I'm behind on.

## ⚙️ Below the line: engineering & architecture

- **The best find of the week.** Preparing a live check for that "say when a source failed" feature, Lead found that when Piper couldn't read your GitHub issues, it reported you had none, and for people who connected GitHub by signing in, Piper had no way to read them at all. The new "I couldn't check" message could never have appeared. PA found the other half: people who connected with a personal access token had no way in either, even though Settings showed them connected. One fix now handles both kinds of connection.
- **The hand-written phrase-matching rules Piper still relies on dropped from 440 to 155** over Friday and Saturday, in ten batches of deletions, each approved by Arch. Nothing further landed after that, and the remaining tail didn't finish by Thursday night, which had been the goal. Finishing those deletions is one of the things the October 30 beta waits on. It's still touch and go, but still definitely possible.
- **The first real release to alpha through our new automated release process.** It had only run as rehearsals that skipped the steps that later failed. Its first real runs on Wednesday found three bugs in three attempts, and each time it stopped rather than release something broken.
- **The ChatGPT and Claude connection is ready for more people than me.** Each person's connection can only see their own Piper data, checked with two test accounts, and each person gets their own limit on how many requests they can make. PA's review caught that the limit had been switched off on the live server while every test still passed. It's fixed, and a test now fails if it's ever off again.
- **Automated checks.** One of the checks code must pass had failed 41 times in a row without anyone noticing, because the daily look only covered one check. It now covers all twelve. When that check failed again on Wednesday, the daily look caught it within half an hour, and it was fixed that night. Every run through Thursday passed.

## 🔬 Methodology & process innovation

- **Rulings from an assumed state.** Arch corrected six of their own rulings and claims this week, each made before reading everything. The sharpest: Arch treated "Piper isn't sure what you meant" as "not a command" until ten live test requests showed a delete request would have been saved as a new project. Arch now checks what the code and Piper actually do before ruling.
- **Cheaper, safer machinery.** CIO cut the briefing every agent loads at session start from 169 KB to a 5 KB page, and destructive git commands aimed at my working copy are now blocked automatically instead of by a sentence in the instructions.
- **AI prompts human.** After outside feedback from a trusted human advisor that blog posts give off that "AI-written" smell, I've reverted to an approach I'm using elsewhere, writing all of the prose myself from a scaffold Comms supplies with the facts checked. The editorial calendar has a number of drafts that I am carefully rewriting as I come to them, and forthcoming posts will follow the model in which Claude prompts me to write instead of the other way around.
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
- **Open issues on the beta gate:** 31 → 14, mostly from my scope rulings on Tuesday rather than burn-down
- **Hand-written routing rules left (goal is reduction):** 440 → 155

The beta gate got a written standard and a "slip ledger." Every issue added to or removed from the beta list is now logged, with a brake: after a second slip, PPM stops proposing dates and brings me a choice between cutting scope and accepting a later date. The brake fired Thursday. I'm holding the dates anyway (design partners by Friday, October 23, hard stop Friday, October 30) and watching for slippage. As I write this, five slips are logged against that baseline and no days have moved.

Every agent's review this week listed at least one of their own mistakes, with the fix.

# 🎯 Coming up next week

Lead finishes the rule deletions ahead of Wednesday's checkpoint. After the next release to alpha, the agents check the new "I couldn't check" messages with one account connected to GitHub by sign-in and one by personal token. Once I've tested the Piper plugin myself, PA submits it to three directories.

# 🚧 Blockers & asks

Most of next week waits on me: the next release to alpha, a GitHub test identity for those checks, the go to publish the new privacy section about Piper accounts, and my plugin test.

# 🔎 This week's learning pattern

## A read that can't fail out loud fails quietly

**Discovery**: When code that reads a user's data can only answer "found" or "empty," every failure to read comes out as "empty," and the user gets a confident wrong sentence about their own work.

**Example from this week**: It turned up three times in two days. Closing or reopening an issue treated every non-answer from GitHub as "that issue doesn't exist." The Radar card showed a failed read as a quiet day. And for people who connected with a personal access token, Piper had no way to read GitHub at all. Each fix adds a third answer, "I couldn't check," with the reason.

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
