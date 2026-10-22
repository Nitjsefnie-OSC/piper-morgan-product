---
image: 'the-board-that-stopped-matching-reality-miniature-boats-meet-their-sailing-twins.png'
alt: 'A luminous harbor attendant counts docked boats in a miniature harbor while a human points out the window, where their full-size counterparts are already sailing.'
caption: '"“Shouldn’t be long now!""'
---

# The Tracker that Lost Track

*August 16, 2026*

By ten-thirty on a Sunday night, most of my team had already wrapped up their work for the day. More than half of my eleven agents had logged their evening check-ins as routine (standing items unchanged, nothing to report).

What I couldn't tell was what we had actually got done that day, and how progress was going toward the current milestone. I hadn't looked directly myself recently, and possibly because I was a bit worried about what I might find. 

# Checking our work
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

# The all-nighter

What happened after I logged off is its own small proof of the same instinct. Lead kept working the five lanes through the night rather than parking them for morning. One fix turned out to trace back to something almost embarrassing (and a sort of meta-pattern I am noticing more and more often these days): 

*The very prompt telling the system how to avoid fabricating information was itself providing an incorrectly framed example.*

Lead rewrote the prompt rather than patching around it.

Another lane turned out to already be fixed under a different issue entirely, so it just had to be verified rather than rebuilt from scratch. A third checked three old fixes and confirmed, by actually running them, that all three were genuinely live in production, while a fourth found one branch of a login flow that unit tests had been mocking around so thoroughly they could never have caught it failing for real. The latter finding got split out into its own tracked issue with a test written specifically to keep it in line going forward. 

I also closed one issue myself, directly, on my own word — fifty-six releases had gone out through that particular piece of infrastructure without incident, and that was evidence enough for me. When all five lanes concleded, Lead shipped the whole batch as a new release and updated the tracker so I'd have a clean plan waiting Monday morning.

# Tidied up, for now
By the time I finished reconciling the sprint board, we'd closed thirteen issues, corrected about a dozen mislabeled items, and turned five stalled threads into real progress, all over one night after I questioned a status update.

The sprint tracker grew from "we should keep track of issues in GitHub" to "we should work in sprints" to "we should close issues properly with evidence" and on and on. Along the way, the sprint board has gotten richly expressive and the agents have gotten much better at maintaining and reading it themselves. Nevertheless, like so many of the instruments and methods I've embraced or developed to do this work, it has evolved from idea to convention to rigorous process to scripted routines with each round of improvement triggered by my looking for the information I need and not finding what I expected.

---

*Next on Building Piper Morgan: "Mistaking the Inset for the Map" — a check that looked at part of what it was supposed to cover, and reported back as if it had looked at all of it.*

*Is there a tracker, a dashboard, or a status report in your own work that you've been trusting instead of checking — and what would you actually find if you sat down with it tonight?*
