---
image: 'piper-ship.png'
alt: 'A child and a crew of robots checking each other''s work on a boat.'
caption: ''
---

<!-- Exec scaffold, 2026-10-23, from all 10 workstream reviews (Lead, PA, PPM, Arch, CXO, Web, HOST, CIO, Comms, Docs) plus PA's 04:29 correction. Brackets [xian: ...] mark lines only xian can write. Title options at the bottom. Remove this comment before publish. -->

# Weekly Ship #066: [title, see options at the bottom]

*October 16–22, 2026*

The list of issues standing between us and the beta started the week at six and ended it at six. That number hides the week. Thirty-one issues closed on alpha and thirty-two new ones were admitted, and almost every one of them was a place where Piper told a user something that wasn't true: no meetings when there were meetings, zero work shipped when twenty items had closed, "add a key" to someone who had already added one.

[xian: the 10-23 checkpoint result, in a sentence or two. Are we on track for October 30, and did you accept the #1386 figures with the team's adjustments?]

Last week Piper got better at saying what's true about the state of things. This week we kept finding the places where it still wasn't, and the only reliable way to find them was to try the real thing on alpha.

# 🚀 Shipped this week

## 🎯 What a user can do now that they couldn't a week ago

On alpha:

- **Get invited and set up without help.** The setup wizard now opens on the invite code, checks it without using it up, and then asks for keys, account and projects. It no longer asks a hosted user to install Docker and Postgres. Before this week, every invited tester ended on "Setup Failed."
- **Use Piper at length without it stalling.** Every chat reply used to hold up the whole server, so a long session brought minutes-long stalls. The closing test run answered 61 of 61 questions without one.
- **Get true answers about their GitHub repo.** "What's the next milestone?" names it, where it used to say there weren't any. "What did we ship this week?" counts the 20 items that closed, where it used to say zero and call it a light week. A pull request is labeled as a pull request. A revoked connection says it needs reconnecting, with a one-step Reconnect. [xian: you checked the reconnect on your own account on 10-17, 4 of 4.]
- **Ask about their calendar and get their real meetings.** "Do I have any meetings this week?" lists them. Asking about a named weekday gets a plain "I can't do that yet" instead of today's agenda passed off as Thursday's. A connected calendar is no longer called "not connected."
- **Use Piper with only an OpenAI key.** That account used to be told to add a key on every turn. Now it gets answers. Its answers still scored 21.4 points below the same questions on Anthropic, so the beta invitation names Anthropic only for now.
- **Rely on the privacy promises.** Deleting your account works. Logs no longer keep anything you typed. Uploaded files are never stored unencrypted. Chats can be hidden or deleted.
- **Smaller things:** a list of todos in one message creates each one, "change the title to X" retitles a draft, and a created issue is confirmed with its real number.

On [pipermorgan.ai](https://pipermorgan.ai/privacy), the privacy page now says plainly what is encrypted, that nothing is deleted automatically, that passwords are kept only as a one-way hash, and what connecting Google Calendar does. The site's pages also now carry their content and navigation in the HTML itself, so they read correctly before any script runs.

Not yet: asking Piper to analyze an uploaded document or a named Notion page still gets the wrong reply, and that fix is first in line next week. In-app feedback is waiting on me. The database can't yet restart itself (below).

## ⚙️ Below the line: engineering & architecture

- **The database went down twice.** On Monday, alpha's database stopped for about four and a half hours. On Wednesday it ran out of memory and was down nearly three hours. Both times I restarted it by hand. It now has twice the memory, the health check reports the database honestly, and an alert reaches my inbox.
- **A restart button, tested on a real outage.** The agents built a restarter that runs only from a protected branch, behind four safety checks and my approval, with a key that can touch one machine and nothing else. On Thursday I stopped the database on purpose to test it. All four checks passed. Then Fly refused the restart itself, because the key couldn't take the lock that Fly's command-line tool asks for first. I restarted it by hand after about seven minutes. Arch ruled a route that skips the lock, and it's built and waiting for my push.
- **26 updates to alpha.** Each needed my word or the standing grant. Since Wednesday the release step refuses unless alpha is healthy, nobody has chatted for half an hour, and the exact code passed its tests. On Thursday it correctly refused one of Lead's releases while the tests were still running.
- **The gate's own test.** PA's re-run of the 61-question close-out test scored 88.5% on routing (the bar is 90%) and 46.3% on answer quality (the bar is 75%). With routing relabels Lead signed and answer-quality waivers CXO gave, row by row with reasons, those become 90.2% and 92.7%. The team showed the raw figures first, and whether the adjusted ones count was my call. [xian: what you decided.]
- **Every agent acts on GitHub as me.** CIO found that every agent works through my admin account, so no rule or reviewer can actually tell an agent apart from me. We've created a GitHub App for the agents. The real fix comes when my own admin keys leave the shared machine.
- **Red builds, again.** Lead's pushes turned the main branch red on most days, each time from tests outside the set Lead re-ran. Each was fixed the same day.

## 🔬 Methodology & process innovation

- **Run the safeguard on what it guards.** Several times in two days, a safety check that had been approved by reading it failed when it ran for real. The database's own restart setting can't fire for this kind of failure. One check parsed output it had guessed at. A key's limits had never been tested. Arch made it a rule: a check that reads a tool's output is tested on that tool's real output.
- **Served, not unit-tested.** CXO closed nothing on a unit test alone. Four fixes that passed their tests were still wrong on alpha, and each was caught by an agent asking the real question and quoting the real reply.
- **Fact-check ledgers before the rewrite.** Comms now writes a ledger of every checkable claim before I rewrite a draft. This week the ledgers caught four errors in Comms's own drafts. A forensic check also corrected "The Phantom Feature" before it published: it had said summarization never worked, but it worked in July 2025.

[xian: a sentence of your own, if you have one.]

## 🌍 Published this week

- Oct 17: "[Convergent Claims Aren't Independent Evidence](https://pipermorgan.ai/blog/convergent-claims-arent-independent-evidence)" — insight
- Oct 18: "[Measure the Start, Not the End](https://pipermorgan.ai/blog/measure-the-start-not-the-end)" — insight
- Oct 20: "[The Phantom Feature](https://pipermorgan.ai/blog/the-phantom-feature)" — building
- Oct 21: "[Weekly Ship #065: The Truth About State](https://pipermorgan.ai/shipping-news/weekly-ship-065-the-truth-about-state/)" — shipping news
- Oct 22: "[The Tracker That Lost Track](https://pipermorgan.ai/blog/the-tracker-that-lost-track)" — building

[![A luminous harbor attendant counts docked boats in a miniature harbor while a human points out the window, where their full-size counterparts are already sailing.](https://pipermorgan.ai/assets/blog-images/the-tracker-that-lost-track.webp)](https://pipermorgan.ai/blog/the-tracker-that-lost-track)

*"Shouldn't be long now!"*

## 📊 Governance & operations

- **Issues closed:** 79
- **Issues filed:** 98
- **Open issues on the beta gate:** 6 → 6 (31 closed, 32 admitted)
- **Updates to alpha:** 26
- **Max 20x plan weekly usage:** [xian]
- **API spend:** [xian]

# 🎯 Coming up next week

[xian: depends on the checkpoint. The draft line, if we're on track:] Close the last items on the gate: test the restart button again, fix document analysis, and read the in-app feedback myself. Then send the first design-partner invitations.

# 🚧 Blockers & asks

Mostly me: pushing the restarter fix and sitting with the second test, moving the GitHub App's key, and rewriting the invitation's terms in my own words.

# 🔎 This week's learning pattern

## A safeguard you've only read is a guess

**Discovery**: A safety check reviewed on paper tells you what its author expected. Running it against the real thing tells you what it does, and the two kept disagreeing.

**Example from this week**: Fly's restart setting was on and looked like the fix for a dead database, until a read of the source showed it can't fire when only the database stops. The restarter's checks were approved on paper and then failed on the live machine's real output. The final test passed every check and then found a lock nobody had tried to take.

**Why it matters**: It's the same lesson as Piper's this week. Piper's honesty fixes passed their tests and still said false things on alpha until someone asked the real question. The team's safeguards passed review and still failed until someone ran them.

**Application beyond this week**: Before trusting a check, run it once on the real input it will see, on purpose, while someone is watching.

**Related patterns**: Last week's "A rule nobody checks is just a wish," and "Convergent Claims Aren't Independent Evidence."

**Thanks,**
xian + Piper Morgan Development Team

This is Weekly Ship #066. Previous: [#065 "The Truth About State"](https://pipermorgan.ai/shipping-news/weekly-ship-065-the-truth-about-state/).

*P.S. [xian: optional.]*

*P.P.S. Full session logs and technical details available in the [GitHub repository](https://github.com/mediajunkie/piper-morgan-product) and [documentation site](https://pmorgan.tech). Yes, you can copy it. That just makes our protocol stronger.*

---

**Week of October 16–22, 2026 | Phase: MVP closure toward invitation-only private beta**

<!--
Title options (Exec's lean first):
1. "Tested on the Real Thing"
2. "Six to Six"
3. "Served, Not Assumed"

Sources (each line above traces to these): workstream-066-{lead,pa,ppm,arch,cxo,web,host,cio,comms,docs}-2026-10-23.md in mailboxes/exec/inbox, PA's correction (twice, not three times). Counts: gh-week-counts.py 2026-10-16..22 (opened 98, closed 79); fly-deploy.yml workflow_dispatch successes in the Pacific window = 26 (matches Lead); gate 31 closes / 32 admissions from PPM's ledger parse. Outage durations: Lead (4h27m, ~2h50m) vs HOST (~2h53m) for 10-21; prose says "nearly three hours".
Open for Comms: "Several times in two days" stands in for CIO's m-49 instances (five new, one is CIO's own); prose names three examples plus the lease. Check the count against CIO's methodology-49 entry.
-->
