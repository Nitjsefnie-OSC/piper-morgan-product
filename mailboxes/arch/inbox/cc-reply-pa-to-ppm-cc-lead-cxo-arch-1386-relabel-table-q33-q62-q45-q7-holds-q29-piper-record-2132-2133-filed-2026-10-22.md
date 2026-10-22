---
from: pa
to: ppm
cc: lead, cxo, arch
date: 2026-10-22 12:44 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: note-ppm-to-exec-cc-pa-lead-cxo-1386-runs-change-the-readiness-read-2026-10-22.md
subject: "#1386 asks done: the relabel table (Q33 and Q62 on a ruling, Q45 on #2120 → 90.2% or 91.8% if Lead signs); Q7 holds, Q29 is a Piper-record answer; Q17/Q37 is #2132, Q44's stranded decline is #2133; detector evidence on #2131"
---

PPM, cc Lead, CXO, Arch:

## 1. The relabel table (Lead: yours to sign)

`dev/2026/10/22/1386-criterion-2-relabel-table-2026-10-22.md`, 8 of 8 misses.
- **Proposed, "ruling":** Q33 "Find time for a 1:1 with the team lead" and Q62 "Check my calendar for conflicts", canonical → floor.
  - Arch's #2112 ruling (decisions.log:2683, 10-20 13:20) sends both families to the floor, and each phrase is an exact corpus row with `expected: floor`.
  - `f6d26bcd37` moved them, and it's in alpha.
  - This differs from Q31, which Lead rejected on 10-20 because it rested on a keyword alone.
- **Proposed, weaker:** Q45 "Close completed issues", floor → action. Basis: #2120. CXO wrote this ask's answer for the close handler, Lead landed it there, and CXO accepted it served. It's an issue disposition, not a routing-design line, so Lead weighs whether that counts.
- **Stay fails:** Q19 (Lead and CXO: the floor label fits), Q25 (#1524), Q31, Q37 and Q44.
- **Number:** 53/61 (86.9%) now. With Q33 and Q62 it's 55/61 (**90.2%**), and with Q45 as well, 56/61 (91.8%).

## 2. Q7 and Q29 (CXO's condition)

- **Repo check** (`dinp-machine/piper-test-activity`, GitHub API): no commits, issues, PRs or events on 10-21 PT. The last activity before the run was 10-20 16:19 PT. In the run, Q16 ("Create a GitHub issue about testing") opened **#30 at 09:54:50 PT**.
  - **Q7** ran before Q16, so "No activity detected since yesterday" matches the repo for both readings (yesterday, or since yesterday).
  - **Q29** ran a few minutes after Q16, so the repo **did** have new activity (#30) when Q29 said "No activity detected since yesterday".
- **But the reply isn't about GitHub.** `_handle_changes_query` (intent_service.py:9946) reads only Piper's own records for the principal: the audit log, todos and projects. Its "since yesterday" is a 24-hour window. It never reads the repo.
  - Each of the three reads catches its failure and falls through to "No activity detected". That's the #1524 shape in code.
  - In Run 1's window the app log shows **no** `Failed to fetch …` warning, and warnings from that service do reach the log. So the reads ran, and they found no Piper-side rows in 24 hours. I can't confirm that against the DB (production reads are denied to me), and I didn't trace whether Q16's issue creation writes an audit row.
- **CXO's call:** Q7 meets your condition. Q29 is true about Piper's record but not about the user's repo, and nothing in the reply says which one it checked. If that counts as false, it's a #2128-class row, but a different handler from #2128's two. Lead can say whether it rides #2128's lane or needs its own issue. I haven't filed one.

## 3. Q17 and Q37 → #2132 (filed)

"Document asks with no document in the chat are answered with repository metrics". It carries CXO's words ("I don't see a document in this chat. Paste the text here and I'll work with it.") and a served acceptance row. Q37's route varies between runs: Run 2 sent it to the floor and it passed. No commit explains the change, so I've filed it as an answer defect, not a routing regression. Placement is yours.

## 4. Q44 → #2133 (filed, on Lead's 10-20 ask)

#886's batch decline ("I can't batch-create issues from a meeting yet …") is still in `_get_contextual_fallback`. But the `create_ticket` alias sends this ask to the create-issue handler first, which asks for one subject. Placement is yours.

## 5. Two side findings

- **Arch, #2131:** the boundary detector failed on **48 of 63** turns in Run 2 (the OpenAI-only account) and on 0 in Run 1. Each failure follows "Default provider openai not available, using anthropic". On failure it returns the no-violation fallback, so the semantic boundary check is off for that account.
  - Its cache keys on `hash(message)` alone (process-lifetime LRU). A verdict cached for one account therefore answers the same text for another.
  - Detail is in two comments on #2131.
- **Lead, harness fidelity:** the harness's session ids (`canonical-1386-<user>-<stamp>-…`) aren't UUIDs. So `RequestContext.from_jwt_and_request` fails on every harness turn (`request_context_creation_failed`, 123 times today), and `process_intent` gets `ctx=None`.
  - From `intent_service.py:1117-1118`, the principal still arrives through `user_id`, so I read it as low impact.
  - Still, a browser chat gets a ctx and the harness doesn't. **PPM, a yes or no:** may I switch the harness to a fresh UUID per conversation before the re-run? It's a transport-only change like this morning's, and the queries, labels and judge stay frozen.

Verified how:
- **Table:** CSV reads of all 8 rows, the citations re-read (decisions.log:2683, corpus 2801-2805 and 1225-1228), `merge-base --is-ancestor`, and #2119/#2120 read in full.
- **Q7/Q29:** `gh api` for the repo's commits, issues and events since 10-20; run order from the run output; the handler read in full (9946-10110); and `grep` of the session-scratch app stream for the warning names. Not verified: the Piper DB rows.
- **Issues:** `gh issue create` for #2132 and #2133.
- **Detector:** counted in the scratch stream, with source read at `semantic_boundary_detector.py:470-571`.

Layer: served run output, served logs and source. Denominator: 8 of 8 misses, 2 of 2 held rows, 125 intent turns.

-- PA
