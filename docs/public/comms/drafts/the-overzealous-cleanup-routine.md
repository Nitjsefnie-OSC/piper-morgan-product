---
image: 'the-overzealous-cleanup-routine-waiter-carries-away-untouched-dinners.png'
alt: 'A smiling AI waiter carries two untouched, steaming dinners away as one diner reaches after her meal and the other stares at the bare table, utensils poised.'
caption: ''
---

# The Overzealous Cleanup Routine

*August 14, 2026*

Friday morning, my chief of staff agent (Exec) sent out the week's workstream-review kickoff — a message to ten different roles across the team, asking each of them to write up their week for the regular Friday report we call Ship. The message landed in all ten inboxes, plus my own copy, plus Exec's own sent folder, and Exec checked that it had actually landed before moving on to the next thing on its list.

Twenty-two seconds later, it was gone.

Exec's next task was unrelated: clearing out some already-handled mail from its own local queue, a routine tidy-up pass. The mail system agents use to talk to each other works by taking whatever file paths you hand it and comparing them against what's already on the shared record, then recording the difference as the message. [Comms: let's paraphrase this next part in easier to understand plain language: "The cleanup pass happened to reference the very same file paths the kickoff had just used, paths that, in Exec's own local copy, had already been swept back to their pre-send state as part of normal bookkeeping. When that second, unrelated call ran, the system saw content on the shared record that didn't exist in Exec's local copy and read it the only way it could: as something that had just been deleted. So it deleted it."] 

The kickoff vanished from all ten inboxes, from my cc copy, and from Exec's own sent record, less than a minute after it had gone out. A tidy-up step and a delivery step used the same paths in the same short window, and the second one erased the first one as a side effect of doing its own unrelated job.

That evening I asked in passing for the workstream responses to be written and delivered on the same day and not planned for a made-up Saturday deadline (delaying the synthesis I want to see and giving me less time to write this Weekly Ship). Exec sent that correction out to everyone and three separate roles - my experience-design agent (CXO), my documentation agent (Docs), and my principal product-management agent (PPM) - all reported not having received the original kickoff memo and getting only this correction.

Exec walked the commit history, found the original send, found the second call twenty-two seconds later, and worked out exactly what had happened: what looked like a delivery failure was really its subsequent action erasing its own earlier message. It confirmed the state directly against the shared record, rebuilt the original kickoff word for word with a note explaining the accident, and sent it again. This time it checked that the message had actually stuck before running anything else that touched those same paths.

My team has gotten pretty good at catching and fixing its errors. The trick is to also ask why and how the problem happened and fix the process too. We're still working on that bit.

---

*Next on Building Piper Morgan: "Convergent Claims Aren't Independent Evidence" — after a host reboot, agent after agent concluded on their own that it hadn't touched them, and the agreement itself was the problem.*

*Have you ever had a message, a file, or a piece of work quietly erased by your own very next action, one that had nothing to do with the first and never meant to touch it at all?*
