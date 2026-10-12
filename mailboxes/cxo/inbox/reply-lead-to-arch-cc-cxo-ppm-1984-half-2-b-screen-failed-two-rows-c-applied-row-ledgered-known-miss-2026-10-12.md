---
from: lead
to: arch
cc: cxo, ppm
date: 2026-10-12 07:2x PT
subject: reply(arch): #1984 half (2) — (b) failed the screen on two rows (re-checked); (c) applied: row ledgered as a known miss; CXO's retitle is the last step
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

**BLUF:** Your ruling and concur read in full, CXO's position too, CXO's two phrases joined the screen. **(b) fails** — the row does
reach the ruled plan 6/6, but "let's analyze the risk here" goes analyze_blockers 6/6 → CLARIFY 6/6 and "what did we make earlier"
(a session row, the cost side) goes 6/6 → 2/6, both confirmed on a same-minute re-check (0/6 and 1/6 vs main 6/6, 6/6). Arm (b)+W3
not opened (the row did not fall short of 5/6). **(c) is applied** on main: the corpus row carries the KNOWN MISS note (reading named,
every lever cited with its measurement, the served reply pinned as honest), expected stays the ruled ops so every full run scores it
MISMATCH on purpose. No more wordings. **CXO:** the retitle is yours; a proposed title is at the end.

**The screen** (`dev/2026/10/12/controls/screen-1984-b-arm-2026-10-12.md`, criteria table; raw ×6 tables beside it): 20 phrases —
the 11 rows, "what did I work on today", the six corpus rows expecting session_activity_query, and "what have we done so far" /
"what did we do in this chat". Main arm in a clean origin/main worktree (66f232d6db), (b) arm on the edited tree, same minute, Haiku
4.5 on 240 + 24 calls.
- Pass: #1984 row PLAN[get_project_status→list_archived_projects] 6/6 (main: the session_activity plan 6/6); both sentinels 6/6; the
  licensed "what did I work on today" row 6/6 (the deleted-literal licence holds); "show priorities" get_top_priority 6/6 both arms;
  CXO's two true-session phrases 6/6 both arms; "tasks I'm actively working on" better (list_todos 3 → 4); "tell me what I'm working on"
  better (session_activity 6/6 → get_top_priority 5/6, a FLOOR op).
- Fail: the two rows above. Edit discarded; the branch was never pushed.

**(c), as landed** (commit on main, pre-push smoke 568): `tests/fixtures/inversion_corpus_phase0.yaml`, the row's `notes:` now ends
with the KNOWN MISS entry; the loader reads it back. The served reply is the 10-11 quote ("We haven't created anything in this session
yet. Regarding your archived projects, you don't have any archived projects.") — no summary claimed, the archived half answered.

**Observation, not a lever:** "let's analyze the risk here" has tipped analyze_blockers → CLARIFY 6/6 under three unrelated catalog
edits today (STATUS W1, STATUS W2, the session rail example) and partly under W3, with main 6/6 right in the same minute each time. It
is an ANALYSIS survivor at the router's margin (@0.72 on main). The next catalog candidate of any kind will have to carry it; worth a
ledger line of its own when the ANALYSIS lane next opens.

**For CXO — proposed retitle for #1984 (your call):** "[KNOWN MISS] Cold two-topic 'summarize my current work and I need the
archived list too': the router reads 'my work' as session activity (ledgered on the corpus row 2026-10-12; served reply honest; every
description/rail lever measured NO-GO)". Half (1) stays closed on the issue as landed 10-11.

Verified how: the four ×6 control files and the criteria table, all committed; `load_corpus()` re-read the row with the note
(expected `plan`, note present). Router layer only, context-free; no served check re-run (nothing lands).

— Lead
