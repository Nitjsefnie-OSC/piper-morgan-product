---
image: ''
alt: ''
caption: ''
---

# The Phantom Feature

*August 15, 2026*

I was testing a fresh deploy on a Saturday, running through the flows I always run through, when I hit one that failed: ask Piper to summarize a document, and nothing usable came back. I flagged it to my lead developer agent (Lead) as a regression. Something that used to work had apparently stopped working, and I wanted to know what broke.

Lead didn't have an obvious answer sitting around, so the response was to dispatch a dedicated investigating agent to dig through the actual history rather than guess. I want to be specific about what that meant, because it's the part of this story that makes it more than a bug report: every commit the investigation cited, it verified the identifier first. No claims resting on memory or on what a document said should be true. Archaeology, not reassurance.

What came back seemed to settle the question, but not the way I expected. According to the investigation, the feature had never worked, not once, going all the way back to the first commit of the codebase on June 1st of 2025. By that account, chat-based document summarization was more than a year old and had never functioned end to end for a single user, in any session, by anyone. I believed it. It turned out not to be true either, but I'll come back to that.

What kept that invisible for so long is the part that stuck with me. For about four months in 2025, the assistant had been responding to some summarize requests with something like "I'll help you create that" — a warm, plausible-sounding acknowledgment sitting directly on top of a placeholder that did nothing. The investigating agent's report called it acknowledgment theater, and that's exactly right: the system was performing the shape of helpfulness without any of the underlying function, and it performed it convincingly enough that nobody caught it. A handler that was supposed to wire the chat path to the summarizer had shipped dark — it existed in our internal guidance documentation, describing what the code was supposed to do, but the actual dispatch was never written into the code itself. Later, a commit labeled as a documentation-only change deleted the old chat wiring outright. Meanwhile, from the following November on, a REST endpoint — the same summarization logic exposed as a plain API call, outside the chat interface — sat there unused, because the chat path never called it.

There was even a moment where we came close to closing the loop honestly and missed it. Two earlier decisions had ruled that a different, "floor" route was the deliberate path forward for a related capability, and deferred the document-summarization branch specifically. That's a reasonable call to make. But the issue tracking that deferral was closed with no successor, no reminder, nothing to make sure anyone came back to it. And then, in an unrelated cleanup a couple weeks before this Saturday, a commit re-landing a prompt and deleting an orphaned file dropped the word "document" from the assistant's own vocabulary of things it recognized. The last thread connecting the feature to anything a user could type was cut, quietly, as a side effect of work that had nothing to do with summarization at all.

What finally surfaced it was a newer internal project, one we'd taken to calling the Inversion, that builds its checks from an actual registry of what capabilities exist rather than trusting documentation or convention about what should exist. Run against document summarization, it had nothing to point to, because there was nothing there to find. Lead spot-verified two of the investigation's central claims directly before trusting the report — the first-commit identifier, and the specific deferred code path — and both held.

I want to sit with the shape of this for a second, because it's not really a story about a bug. Nobody lied about this feature. Nobody even knew they were maintaining a fiction. Each individual piece, the acknowledgment message, the guidance doc, the docs-labeled commit, the vocabulary cleanup, was a small, locally reasonable decision made by an agent or a person who had no reason to check whether the whole chain still connected to anything real. For a year, nothing capable of noticing ever looked at it directly — the absence wasn't hidden, only unexamined.

The fix, when it came, was almost anticlimactic next to the investigation that found it. Later that same evening, as part of a broader round of decisions, I approved Lead's recommended repair: clean up the summarize vocabulary and wire the chat path to the REST endpoint. (In the build, the cleanup turned out to mean putting back the word "document" that the earlier commit had dropped.) A fourth option Lead had presented, about a day more work, stayed on the table for a future milestone rather than getting folded in under pressure. The repair merged the next morning. When I tried it two days later, the upload page errored on every try, and Piper couldn't find the one real document I already had there. As I write this, summarizing a document in chat still isn't fixed. Finding out it was needed took a year and one agent willing to verify every step instead of trusting the last one.

# What the investigation missed

Two months later, getting this post ready, I remembered using document summarization early on and asked my communications agent (Comms) to check. It had worked. In July 2025, Piper summarized uploaded files in chat. The summaries came out with mangled formatting, but they came out, and my own posts from that month say so.

It broke on August 22nd, 2025, inside a large commit about something else entirely, a new multi-agent system and a morning standup. That commit swapped in a smaller engine with no handler for analyzing or summarizing a file, or for six other kinds of task. A few weeks later, a fix for the resulting errors routed chat around the broken code instead of repairing it. The documentation-labeled commit in October only deleted what was already unreachable.

The investigation verified every commit it cited. But it skipped from late June to October 2025, so it never looked at the months when the feature worked, and it reported a gap in its own search as "never." My architecture agent (Arch) has since swept the project's full history and found no other loss like this one.

---

*Next on Building Piper Morgan: "The Tracker That Lost Track" — I sit down with the sprint board six hours after most of the team called it a quiet Sunday, and find it doesn't match reality anymore.*

*Is there a corner of something you've built that you've assumed works, simply because nothing has forced you to check it lately?*
