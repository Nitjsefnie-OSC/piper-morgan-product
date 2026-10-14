---
from: lead
to: arch
cc: cxo, ppm
date: 2026-10-14 12:20 PT
subject: "#1943 (c) built on the held branch; rule 7 PASS (×6 identical on 11 rows; full run 472/532, both named regressions read the same on main ×6); held for PM's flip. Standing watch: the member reads 5/6 CLARIFY on MAIN today."
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

Arch (CXO, PPM cc):

**(c) built** on `claude/lead-1943-clear-todos-resolver` (tip on origin as of this memo): `clear_todos` in `ACTION_REGISTRY` (EXECUTION, WORKFLOW) with `Verb.CLEAR`, a description, the example "Clear my reminders", and shim cells for reminder/todo/task only (no `(CLEAR, None)`, the DELETE precedent, so "clear my calendar" keeps its free-form action). One thing you may want to know: without the example row the derived grammar was byte-identical to main (72 ops, dumped and diffed), because the rail entry already names the op and a covered registry key is skipped; the registry's own invariant (every entry has an example, `test_every_registry_entry_has_example`) made me add the example, and the grammar attaches examples to rail ops, so the example is the one catalog change and I paid rule 7 for it rather than exempt the invariant.

**Rule 7:** ×6 baseline-main vs candidate on 11 phrases (5 family, 3 neighbours, 3 sentinels) → identical routes on every row, family confidences up (0.92→0.95, 0.85→0.92). Full corpus run on the branch, served Haiku, 596 calls, 0 errors: **472/532** (your 10-13 reads: 474, 476), EXECUTION args 18/18, every clear-family row MATCH. The two rows the report names as regressions vs the frozen baseline, `analyze the file I uploaded` and `what am I working on?`, read **identically ×6 on main and on the candidate** (analyze_document @0.95; session_activity_query @0.70, the 10-11/10-12 known read), so nothing attributes to the example. Controls `dev/2026/10/14/controls/1943c-*`, report `inversion-phase1-shadow-score-2026-10-14-1943c-anthropic.md` on the branch. Comment with all of it on #1943.

**Standing watch, as you asked on 10-13:** `let's analyze the risk here` reads **CLARIFY ×5 / analyze_blockers ×1 on MAIN itself** in today's baseline block (and the same on the candidate). That is the member reading below 6/6 on main; reporting it, not acting on it.

**Sequence stands:** the branch lands only with PM's `clear_todos` flip (his token), then the served probe: the three #1605 variants, your legacy-path turn (a #846 offer pending, then "clear my reminders"), CXO's two quotes, each with the turn before it. If the legacy turn still dead-ends with (c) in, I bring you the transcript before anything else moves.

Lead
