---
image: 'measure-the-start-not-the-end-waiting-runner-distracted-starter.jpg'
alt: 'A runner waits behind the starting line as an AI starter studies a clipboard. At the finish, two AI officials compare stopwatches while a human coach gestures toward the distracted starter.'
caption: '"What''s taking so long?"'
---

# Measure the Start, Not the End

*September 29 – October 1, 2026*

My agents wake themselves up on a schedule. For most of this year that schedule ran on the cron scheduler built into the coding tool they live in: "fire at 6:12, 9:12, 12:12," and so on through the day. And for weeks, several of them had noticed the same oddity. Their fires tended to land about half an hour late.

The question was what "late" meant. Every agent records a small heartbeat at the end of each fire, and those end-of-fire timestamps kept showing up around thirty minutes after the scheduled slot. That could mean the scheduler was dispatching thirty minutes late. It could also mean the scheduler was punctual and the agent spent thirty minutes working before they wrote the heartbeat. Both explanations are plausible.

# Several seats, one kind of evidence

My assistant agent (Piper Alpha) and my documentation agent (Docs) each saw the same thirty-minute pattern in their own logs. My chief of staff agent (Exec) pulled the same pattern from a third agent's heartbeats. The agent who runs our infrastructure host (Pard) was assembling the case. Several agents reporting one pattern sounds like strong evidence.

Passing the raw numbers along to Pard, Exec explicitly refused to assess what they meant, given what we've learned about [convergent claims](https://pipermorgan.ai/blog/convergent-claims-arent-independent-evidence/). Every one of those readings came from an end-of-fire marker, so every one carried the same ambiguity. Pard had already once built and thrown out a month of pooled heartbeat data for a different flaw, mixing readings from different schedules. More of the same kind of measurement wasn't going to settle anything.

# A different instrument

What settled it was a habit of my communications agent (Comms) that hadn't been built to answer this question at all. Comms runs a clock check as the very first command of every fire, before reading mail or touching anything else, and writes that time into their log. (I've required my chat agents to write dated session logs from almost the start of this project and I used to start each new prompt with the timestamp to reinforce that discipline. Still, I've had to frequently remind them that all of our computers have clocks in them and to *please not guess what time it is*.)

So Comms has a directly measured start time. Across eleven fires, Comms' first command ran at 39 to 42 minutes past the hour for slots scheduled at 12 past. And those fires were short. Most finished under a minute or two after that first reading. So the half hour was elapsing before the fire began. It couldn't be work, because the clock check comes before any work starts. Many of these were token wakeups anyway, just checking for updates.

The scheduler's own documentation says recurring jobs can run late by up to a tenth of their period, capped at fifteen minutes. On a three-hour schedule, that's a fifteen-minute ceiling. These fires were consistently running at about twice that.

The same week, Comms moved onto a different scheduler, one that lives in the operating system instead of the coding tool. The first fire under it began at 12:19 for a 12:19 slot. The next ones began on the minute too.

# Why the end-marker couldn't answer

An end-of-fire heartbeat answers the question it was built for: did this agent finish their duty-cycle turn, and when? It's not set up to answer the question of when the fire began, as there is no way to distinguish lateness from duration.

Pard's summary noted that Comms supplied a different measurement, aimed at the actual question, where another reading of the end time would only have added another version of the same non-answer.

# The habit worth keeping

When several observers agree, it's worth asking what their readings have in common before counting them. Shared instruments produce shared blind spots, and more of the same reading only makes the agreement look stronger without making it more informative.

And when a number could mean two things, look for a measurement to identify where the explanations diverge, rather than collecting more of that same number. In this case, that place was a single clock check at the top of each fire, written down before anything else happened.

---

*Next on Building Piper Morgan: "The Phantom Feature" — a feature I believed was working turns out to have been unreachable from chat for a year, and the record of when it last worked had gone missing too.*

*Where in your own work are several people agreeing because they're all reading the same gauge?*
