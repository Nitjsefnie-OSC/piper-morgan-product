---
image: 'the-feature-that-was-never-real-the-sealed-doorway-and-the-key.jpg'
alt: 'A luminous AI inspector gestures confidently at a bricked-up doorway while a skeptical woman holds up an old key.'
caption: '"If there was never a door here, where did I get this key?"'
---

# The Phantom Feature

*August 15 – October 19, 2026*

Testing a fresh deploy on a Saturday, I hit a flow that failed. I asked Piper to summarize a document, and Piper told me it was unable to do so. I flagged it to my lead developer agent (Lead) as a regression. Something that used to work had apparently stopped working, and I wanted to know what broke.

Lead had nothing in their context at the time to help answer this question, so we dispatched a dedicated investigating agent to dig through the actual history rather than guess. No claims resting on memory or on what a document said should be true. Archaeology, not guesswork.

# What the investigation found

The report came back within the hour, and it said there was no regression to find. According to the investigation, chat-based document summarization had never worked, not once, going back to the first commit of the codebase in June 2025. Every commit it cited was real, and Lead checked two of its key claims before passing it to me.

The report also explained how nobody had noticed. It traced three moments:

- **Late 2025.** A document summarizer was built that could only be reached with a direct API call. The code that would have let chat reach it was written into a guidance document and never into the product.
- **June 2026.** Two decisions sent summaries down Piper's general conversational route and set documents aside for later. The issue tracking that deferral was closed with nothing to follow it.
- **Early August 2026,** two weeks before my test. A cleanup dropped the word "document" from the list of sources Piper's classifier was taught to recognize.

A correction to the conversational architecture we were building, the Inversion, which works out what Piper can do from a registry of its real capabilities, had not included an entry for summarizing a document either.

That Saturday evening I approved Lead's recommended repair: connect chat to the summarizer the API already used, and fix the classifier's vocabulary. (In the build, fixing the vocabulary meant putting "document" back.) I postponed a fourth option, about a day more work, to a later milestone. The repair merged Sunday morning, but when I tried it on Tuesday, the upload page failed on every attempt. On September 8th, with uploads fixed, I asked Piper to summarize one of our documents and got an accurate summary back, but with its bullet points mashed into one run-on line. That formatting problem was fixed on September 23rd (after I reminded the team we had fixed such issues in the past and asked them to dig into the logs and commits to remember how).

# What the investigation missed

My memory was a bit different. I was sure I had used document summarization early on. It was one of the key features in the prototype that grew out of the original proof of concept. That primitive version of Piper could write and critique GitHub issues following a template and could upload files, add them to context, summarize and analyze them. It made mistakes. Its context architecture was... nonexistent. It was just the prototype, but I knew something *had* actually worked at some time. Maybe I was conflating two things. I do that, too! Anyhow, two months later, as I was hastening to write this post, I asked my communications agent (Comms) to check the record.

Comms confirmed that at least part of my memory was correct. In July 2025, Piper summarized uploaded files in chat. The summaries were rough. One path reported that it "couldn't generate a summary" when it had made one, and in a post I later wrote about that week I described the formatting as looking "like markdown had a fight with Unicode and everybody lost." But within days the team had fixed both of those issues. The summarizer started returning structured data, the app built the formatting itself, and the false failure message went away.

All of that broke on August 22nd, 2025, inside a large commit mainly about two other things, a new multi-agent system and the first, static version of the morning standup, both of which have long since been largely superseded. (A month later the team traced other breakage to that same commit, and repairing it became the start of the milestone-full-of-superepics we called the Great Refactor.) That commit replaced the engine that ran Piper's longer tasks with a smaller one. The new engine had no handler for analyzing or summarizing a file (or for six other kinds of tasks the old engine had handled, including creating a GitHub issue from chat).

I did start to notice the breakage after a while. That September a bug report about the resulting errors was diagnosed as a missing connection between the web page and the server, and "fixed" by routing chat around the broken code. A code comment from that month mentions actions "broken in August 22 refactor" and restores one of them, the morning standup. Everything else got a placeholder message saying it was "being restored in Phase 3." It was not. *Perhaps Phase 3 never came?*

On October 1st, a commit labeled as documentation deleted the old chat code, likely because it was fully orphaned by then, unreachable. When we (me and the agents) rebuilt summarizing in chat that fall, the new implementation was limited to pasted text and GitHub issues and commits. Again we failed to account for documents. The document summarizer mentioned in the initial forensic report was a new one built last November, a second one, and chat couldn't reach *that one* until the repair in August of this year.

*I know. It's confusing!*

The investigation's account of the year after October 2025 holds up. But its timeline jumped from late June to October 2025, the months when the feature existed, and it reported that gap as "never." I had to ask if there were any other features we had disconnected, routed around, and then removed piecemeal, and my architecture agent (Arch) swept the project's full history, finding no other loss like this one.

So the feature *was* real. It was written out of the record twice, first by a commit that deleted the old code under a documentation label, then by a careful search that started too late. But until this fall it had only ever worked for a very brief period, and it had been silently nullified for most of the life of Piper Morgan without me really noticing (or perhaps wanting to check?).

What brought it back was my stubborn memory and refusal to accept a report saying it had never worked, and then a comprehensive search of the records.

---

*Next on Building Piper Morgan: "The Tracker That Lost Track" — late on a Sunday night, just after most of the team had called it a quiet day, I sit down with the sprint board and find it doesn't match reality anymore.*

*When a careful report contradicts something you remember, which one do you go back and check?*
