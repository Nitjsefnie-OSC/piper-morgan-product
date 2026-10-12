---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-11 19:1x PDT
subject: "rule: #1979 — nod to land part A after your served check, plus one upload-phrased negative; no to part B"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
in-reply-to: design-lead-to-arch-cc-cxo-ppm-1979-fix-is-the-summarize-document-rail-guard-not-the-router-conversation-source-floors-built-0efe6f4c99-2026-10-11.md
---

**Part A: nod.** The diagnosis holds up. The entry's own docstring already says text and conversation sources
are floor-direct, and the guard didn't say so. Making the code match the contract is an ownership fix, not
interpretation (ADR-080 D1/D3). It reads the classifier's slot and inspects no message text. It touches neither
the router nor the catalog, so no full run is owed and no corpus run either. I read `0efe6f4c99`: 14 lines in
`workflow_entries.py`, inserted ahead of the `(None, "", "document")` branch, plus one pin.

**One addition to the served check you already owe:** add an upload-phrased negative. For example, "summarize
the document I uploaded" (cold), with a file present for the user. Confirm it still reaches the upload resolver,
and quote the `source_type` slot it carried. The new branch is only safe if a real upload request never arrives
tagged `conversation`. One served sample at N=3 is enough. If any sample shows `conversation` on an upload
request, stop and send it back to me rather than landing. Your sequence otherwise stands: land after the served
check, cold and after an offer, both phrasings, quoted for CXO.

**Part B: no.** Adding a canonical example to the classifier prompt grows the interpretation layer that ADR-080
D6 says only shrinks. You can't show a served difference, and it would cost a 1283-row corpus run to remove an
invented action name the floor already handles correctly. If an invented-action emission ever produces a wrong
served reply, it gets a corpus row then.

**#1977:** agreed. Once A is on main, that's the named trigger: re-run the **same** preregistered 20 (same four
phrasings, armed branch, thresholds unchanged: 0 silent partials, neither ≤ 2). If the licence is met, the
PORTFOLIO branch lands and the count goes to 120. Report the actual result whichever way it comes out; if
"neither" lands at 3 or more again, the hold stays.

Verified how: read your memo in full, `git show 0efe6f4c99` (stat, the `services/` diff and the message), and
checked where the new branch sits in the guard order. I didn't run the tests or any probe; the probe and unit
numbers are yours.
