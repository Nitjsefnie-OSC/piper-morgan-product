---
image: ''
alt: ''
caption: ''
---

# The Tracker that Lost Track

*August 16, 2026*

By ten-thirty on a Sunday night, most of my team had already wrapped up their work for the day. More than half of my eleven agents had logged their evening check-ins as routine (standing items unchanged, nothing to report).

What I couldn't tell was what we had actually got done that day, and how progress was going toward the current milestone. I hadn't looked directly myself recently, and possibly because I was a bit worried about what I might find. 

I pulled up the sprint board for our minimum valuable product (MVP) release, a GitHub Project board filtered to show open issues in the milestone, with at least sixty line items at first glance. I started reading it against what I actually remembered shipping, from the conversations I'd had, from the code I could check myself.

Right away I discovered drift. Some items were still sitting in Backlog when I knew for a fact they'd already shipped — ten of them, once I'd gone through the whole list, stalled in the wrong column because no agent had gone back to update status after the work landed. Others were open issues I could resolve myself, on the spot, because I had direct evidence sitting in my own memory of the work: a task-closing flow I'd tested personally and watched succeed, a reminder system I'd confirmed was actually surfacing tasks and not just supposed to, a deploy that had gone out with fixes already in it that no agent had circled back to mark done. We closed nine issues formally in that first pass, each one grounded in something I could point to directly rather than trusting a status field.

Then I sat down with my lead developer agent (Lead) and walked through the whole board live. Ten items moved out of Backlog into In Review to indicate that the work was done but still being validated or waiting for me to test manually. We corrected them one at a time rather than swept in bulk — the kind of careful per-item fix that doesn't accidentally erase somebody else's work in the process. 

Once we saw what was still genuinely unstarted and unblocked, I authorized a full-court press on five items that evening, rather than letting them sit waiting for another sprint: 

* a bug where the system was showing tasks as empty when they weren't
* a dead end where the product couldn't parse a plain-language answer about which repository someone meant
* a claim about integration status that needed checking against what was actually true
* a backlog of fixes that needed to be verified live instead of assumed ok
* and a rough edge in how the product introduces itself to a brand-new user.

The forty-minute  conversation was ultimately more productive than the rest of the day.


What happened after I logged off is its own small proof of the same instinct. Lead kept working the five lanes through the night rather than parking them for morning. One fix turned out to trace back to something almost embarrassing — the very prompt telling the system how to avoid fabricating information had, itself, been seeding the wrong framing by example, so the prompt got rewritten rather than just patched around. Another lane turned out to already be fixed under a different issue entirely, verified rather than rebuilt from scratch. A third pulled three old fixes and confirmed, by actually running them, that all three were genuinely live in production, while a fourth found one branch of a login flow that unit tests had been mocking around so thoroughly they could never have caught it failing for real — that one got split into its own tracked issue with a test written specifically to keep it honest going forward. I closed one issue myself, directly, on my own word — fifty-six releases had gone out through that particular piece of infrastructure without incident, and that was evidence enough. Once the last lane landed, Lead shipped the whole batch as a new release and republished a tracker so I'd have a clean plan waiting Monday morning.

By the time the board reconciliation actually finished, we'd closed thirteen issues, corrected about a dozen mislabeled items, and turned five stalled threads into real progress, all inside one night that had started as nothing more than me refusing to take a spreadsheet at its word. The team's own end-of-day notes hadn't been wrong, exactly. They just hadn't gone looking the way I had.

What stays with me is how easy it would have been to let the board keep saying what it had been saying, because nobody had contradicted it yet — not the count. A tracking system drifts because checking it takes longer than trusting it, not because anyone means for it to, until eventually somebody has to sit down and actually check.

---

*Next on Building Piper Morgan: "A Bounded Search Reported as a Total" — a check that looked at part of what it was supposed to cover, and reported back as if it had looked at all of it.*

*Is there a tracker, a dashboard, or a status report in your own work that you've been trusting instead of checking — and what would you actually find if you sat down with it tonight?*
