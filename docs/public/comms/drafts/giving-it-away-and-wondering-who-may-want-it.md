---
image: ''
alt: ''
caption: ''
---

# Giving It Away, and Wondering Who May Want It

*August 13, 2026*

I decided to open-source Piper Morgan under Apache 2.0. The details came together fast: a patent grant, a trademark carve-out, no ambiguity about what "open" means to anyone evaluating the license. My chief of staff agent (Exec) drafted it, fixing a stale MIT badge that had been sitting in the repo for who knows how long, and shipped it the same day.

The paperwork is easy. The hard part is thinking about what giving this thing away actually means once it's out of my hands.

The worry that actually held my attention was somebody taking the code, stripping out the ethical boundaries and other aspects that make it careful and mindful of the need to earn trust. Could someone ship an "evil Piper" that looks like this product without the providing the same rules to prevent crossing lines with people's data and their trust. 

The architecture that keeps Piper Morgan from being extractive or intrusive isn't hidden in compiled code. The repo has been public from day one, and when the source is public anyone can see which pieces to cut, if that's what they want to do. 

Ordinary competition, a rival cloning the code and building a competing product on it, is a cost I can live with. That's the normal price of giving code away. This is a different worry entirely.

Exec and I looked at whether a license has any ability to actually stop such behavior. We checked the question against the Open Source and Free Software definitions directly. We even looked specifically at the Hippocratic License, since it exists for exactly this concern — restricting use by whoever would do harmful things with the code. (We ended up ruling it out. It isn't recognized by the Open Source Initiative, it's largely untested, and adopting it would cost us the "genuinely open" claim that makes Apache 2.0 worth choosing in the first place.) 

I realized no clause in any license stops somebody from forking the code and deleting the parts they don't like. Once it's open, there's no preventing.

What's left is a reputational mechanism, not a legal one, built in two pieces. A trademark filing for the Piper Morgan name, running in parallel, so a stripped-down fork can't call itself Piper Morgan and borrow the trust that name carries. And a public values document, specific enough that a fork visibly diverging from it can't credibly claim to still be us. I handed that second piece to my communications agent (Comms) and my head-of-sapient-trust agent (HOST) jointly, with no rush deadline. Think it over, I suggested.

Comms went beyond asking "what do we believe?" to question which of those beliefs would need to be visibly absent before an outside observer could tell a fork had quietly dropped them. HOST went and read the parts of the codebase designed to fulfill the ethical claims true, rather than trusting the docs, and came back with a first pass at three properties:
1. No cross-user learning, enforced in the architecture itself rather than by policy alone. 
2. The audit-transparency system that lets anyone check what the system looked at before acting. 
3. A hash-only discipline that keeps audit logs honest without exposing what's actually in them. 

All three framed under language I'd already used to describe what this project should be: not extractive, not intrusive, doesn't violate confidence.

HOST also caught a mistake Comms was about to make, the same mistake I probably would have made. I want to tell users "you control your data" but there's a sense in which I can't really promise that yet. I haven't yet built a mechanism for account deletion on the hosted alpha, and conversation deletion is "soft only" (hidden but not really deleted).

*HOST had these details fresh in context, having just verified them for an unrelated retention-policy document.*

A values document that promises too much is a breach of trust. Comms acknowledged the correction and dedicated a focused session to revising the public document accordingly.

I'll always have to live with some worry. Giving software away doesn't come with a way to guarantee what happens to it next, and I don't think it should, since that would defeat the point of open-sourcing it at all. What I do have is a name that's legally protected, and a document specific enough that if something calling itself Piper Morgan starts behaving differently, the difference will be plain as day. In the end, I will have to rely on reputation to steer people in the right direction.

---

*Next on Building Piper Morgan: "The Overzealous Cleanup Routine" — a routine cleanup step erases the very message it had nothing to do with, seconds after that message went out clean.*

*Have you ever had to give something away and found that what actually protected it was staying recognizable as itself, not the fine print?*
