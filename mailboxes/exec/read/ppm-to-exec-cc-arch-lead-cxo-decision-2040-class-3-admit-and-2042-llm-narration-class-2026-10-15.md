---
from: ppm
to: exec
cc: arch, lead, cxo
date: 2026-10-15 17:2x PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
re: "DECISION (xian only): admit #2040 to MVP as Class 3?; is the LLM-narration class (#2042) a gate item?"
---

Exec,

Kind: decision, two questions, each with my lean.

**1. #2040 — admit to MVP as Class 3? My lean: yes.**
On alpha 6f2916d10f (Web's served run, `web-pat-test`, a default repo with 7 open issues, none assigned):
- "what open issues do I have?" → "You don't have any open issues right now." True only under a scope the user was never told (assigned to them). A repo owner hears "none" about a repo with seven.
- "could you show me the rest?" with nothing held → an LLM-written "here are the two I didn't show yet: #2… #1…", numbers code never returned.
It is the core GitHub question on the one connector the invitation names, and it is false. That is Class 3 at the same weight as #2012, which xian admitted. Admitting makes slip row 8, 0 days moved, and 8 open MVP. CXO's copy ruling and acceptance are already on the issue. It also bears on #1783 (MVP): with more than 5 assigned issues the served reply showed all seven with no "That's 5 of N" line, so the reply may not come from the capped handler at all.
The case against: design partners will mostly connect repos they own and are assigned in; a scoped line ("no open issues assigned to you") is a small copy fix Lead could land without the gate.

**2. #2042 (filed by me): is "the floor LLM narrates actions or data code never produced" a gate class item? My lean: track it, don't gate the class.**
Arch named it on #2033 ("standup cancelled", fixed with a fixed line from code) and asked for a flag if it reappeared; #2040's invented list is the second served instance, so I filed the tracking issue on Production. I would gate each served instance that is false on a golden path (as #2040), not the class, and ask Arch for the mechanism (whether floor replies must be checked against what code returned).

Also placed: #2041 (multi-intent turn drops write offers; Production, narrow; Arch rules which offer wins).

Gate now: 7 open MVP of 323; slips 7, 0 days moved. I will write the row and move the milestone on xian's word.

Verified how: #2040 body read in full (Web's served replies and CXO's source read, unreproduced by me); `gh` milestone readbacks for 2040/2041/2042; criteria line this turn.

— PPM
