---
image: ''
alt: ''
caption: ''
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

That Saturday evening I approved Lead's recommended repair: connect chat to the summarizer the API already used, and fix the classifier's vocabulary. (In the build, fixing the vocabulary meant putting "document" back.) A fourth option, about a day more work, went to a later milestone. The repair merged Sunday morning. When I tried it on Tuesday, the upload page failed on every attempt. On September 8th, with uploads fixed, I asked Piper to summarize one of our documents and got an accurate summary back, with its bullet points mashed into one run-on line. That was fixed on September 23rd.

# What the investigation missed

The report never matched my memory. I was sure I had used document summarization early on, so two months later, getting this post ready, I asked my communications agent (Comms) to check the record.

It had worked. In July 2025, Piper summarized uploaded files in chat. The summaries were rough. One path reported that it "couldn't generate a summary" when it had made one, and in a post I later wrote about that week I described the formatting as looking "like markdown had a fight with Unicode and everybody lost." Within days the team had fixed both. The summarizer started returning structured data, the app built the formatting itself, and the false failure message went away.

It broke on August 22nd, 2025, inside a large commit about something else, a new multi-agent system and a morning standup. That commit replaced the engine that ran Piper's longer tasks with a smaller one. The new engine had no handler for analyzing or summarizing a file, or for six other kinds of task, including creating a GitHub issue from chat.

The break was noticed, after a fashion. In September a bug report about the resulting errors was diagnosed as a missing connection between the web page and the server, and fixed by routing chat around the broken code. A code comment from that month mentions actions "broken in August 22 refactor" and restores one of them, the morning standup. Everything else got a placeholder message saying it was "being restored in Phase 3." It wasn't. On October 1st, a commit labeled as documentation deleted the old chat code, which nothing reached by then. When summarizing came back to chat that fall, it handled GitHub issues, commits and pasted text, but not documents. The document summarizer the report described, built that November, was a second one, and chat couldn't reach it until this August's repair.

The investigation's account of the year after October 2025 holds up. But its timeline jumped from late June to October 2025, the months when the feature existed, and it reported that gap as "never." My architecture agent (Arch) has since swept the project's full history and found no other loss like this one.

So the feature was real. It was written out of the record twice, first by a commit that deleted the old code under a documentation label, then by a careful search that started too late. What brought it back was a memory that didn't fit the report, and a second search that looked where the first one hadn't.

---

*Next on Building Piper Morgan: "The Tracker That Lost Track" — I sit down with the sprint board six hours after most of the team called it a quiet Sunday, and find it doesn't match reality anymore.*

*When a careful report contradicts something you remember, which one do you go back and check?*
