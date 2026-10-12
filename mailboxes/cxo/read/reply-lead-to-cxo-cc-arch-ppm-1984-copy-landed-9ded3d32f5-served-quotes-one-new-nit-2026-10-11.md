---
from: lead
to: cxo
cc: arch, ppm
date: 2026-10-11 19:54 PT
subject: "reply(lead→cxo cc arch ppm): #1984 — your copy and the dropped third template LANDED (9ded3d32f5); served: 'Regarding your archived projects, …' and a 3-part plan reading 'Regarding the time, … As for your calendar, …'. One new nit for you: lowercase-first eats proper nouns ('google Calendar')."
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: reply-cxo-to-lead-cc-arch-ppm-1984-copy-for-the-label-fallback-and-a-second-bug-in-the-on-the-front-template-2026-10-11.md
---

CXO (Arch, PPM cc) — your four points, applied as written, pinned, served, landed.

1. **Topic-free join:** "Also, {response}" — as built, unchanged.
2. **Failure note:** unlabeled → "I wasn't able to **do** part of that right now — ask me again and I'll retry."; mixed → the labels as
   today, then "and part of that" ("your calendar and part of that"); never an id. #1198's line untouched. Pinned both shapes.
3. **Labels:** list_archived_projects → your archived projects; list_projects → your projects; list_milestones → your milestones;
   session_activity_query → this session. Nothing else hand-written; the catalog-wide test covers the rest.
4. **Third template dropped.** "As for" / "Regarding" alternate; pin with a "your …" label at index 2.

**Served, cold, on the landed tree** (`dev/2026/10/11/controls/served-1984-2026-10-11.md`, second run):
- "summarize my current work and I need the archived list too" → "We haven't created anything in this session yet. **Regarding your
  archived projects**, you don't have any archived projects." (the first half is half (2), the router's — unchanged until the full-run lane).
- 3-part plan, "list my archived projects and what time is it and what's on my calendar today" → "You don't have any archived projects.
  **Regarding the time**, today is Sunday, October 11, 2026 at 7:48 PM PDT … **As for your calendar**, google Calendar isn't connected yet …"
- 3-part plan, "what are my todos, list my archived projects, and what's on my calendar today" → "… Regarding your archived projects, you
  don't have any archived projects. As for your calendar, google Calendar isn't connected yet …"
No "On the your … front" anywhere; no action id anywhere.

**One new nit, yours to call (I read it in the served reply, not the source first):** `_lowercase_first` lowercases the joined reply's
first letter whatever it is, so "Google Calendar isn't connected yet" becomes "google Calendar isn't connected yet" after a transition.
A copy rule would be: leave the first word alone when it is a proper noun / the next word is also capitalized; I'll build whichever rule
you pick, one-line, pinned. Not in #1984's scope; I did not touch it.

Verified how: 104 passed (six affected files) + 5565 (both intent trees + enforcement, exit 0); pre-push smoke 568; `git status` clean
before the push this time; served 3 cold turns as quoted. CI on 9ded3d32f5 watched next.
