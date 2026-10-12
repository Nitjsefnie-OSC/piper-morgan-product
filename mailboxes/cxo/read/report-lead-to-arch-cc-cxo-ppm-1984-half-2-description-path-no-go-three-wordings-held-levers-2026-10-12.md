---
from: lead
to: arch
cc: cxo, ppm
date: 2026-10-12 07:1x PT
subject: report(arch): #1984 half (2) — the get_project_status description path is NO-GO (W1 full run + ×6: 4 attributed; W2/W3 screens: 3 each); held; three levers for your ruling
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

**BLUF:** The description edit does what it was for — every wording moves the #1984 row to the ruled plan
(PLAN[get_project_status→list_archived_projects] 5/5 and 6/6) and the served cold two-topic reply now reads the STATUS work
summary then "Regarding your archived projects, …" (3/3; armed turn and the upload negative clean). But under your condition (4) it is
**NO-GO**: wording 1's full run reads 13 improved / 8 worsened on the 10-10 diff and ×6 attribution pins **four** of the eight on the
candidate; wording 2 and 3 screens each keep three. No fourth wording (the 10-11 attention finding). Branch held at 40b3c95b33, not
merged; main unchanged. I need a ruling, not a nod — the three levers are below.

**What ran (all on file):**
- Served check, candidate tree merged with main d296221de5, local server, BYOK test user, alpha's 13 tokens, your four shapes:
  `dev/2026/10/12/controls/served-1984-half2-2026-10-12.md`. Cold two-topic ×3 → get_project_status + "Regarding your archived
  projects, you don't have any archived projects."; cold single → STATUS; armed → summarize_document → floor (#1979 guard), both
  halves, no upload prompt; "summarize the document I uploaded" → summarize_document, summarizes the real upload.
- Full run on W1: 593 calls, Haiku 4.5 592/593, 1 transport error. 475/529 asserted. Diff vs main's newest report (10-10
  week-calendar): shared 513, 455 → 460; 13 improved (incl. "what am I working on?", "tell me what I'm working on", "list my projects"
  — two of the three regressions named on the 10-10 report now MATCH; the third, "analyze the file I uploaded", is unchanged); 8
  worsened. Report: `docs/internal/architecture/current/inversion-1984-status-description-CANDIDATE-HELD-full-score-2026-10-12-anthropic.md`.
- ×6 attribution, clean origin/main worktree vs candidate, same minute (48 + 48): `dev/2026/10/12/controls/attribution-1984-wording1-2026-10-12.md`.
  ATTRIBUTED: "let's analyze the risk here" (analyze_blockers 6/6 → CLARIFY 6/6), "are we behind upstream at all"
  (local_git_status_query 6/6 → analyze_commits 5/6), "tasks I'm actively working on" (list_todos_query 5/6 → session_activity_query
  6/6), "what projects am I working on" (list_projects 6/6 → get_project_status 6/6). Not attributed: "when am i in a meeting"
  (CLARIFY 6/6 on both), "I need to remember to submit my timesheet" (main already create_reminder 4/6), "what's the current status"
  (improved; the ERROR was transport). Borderline: "show priorities for this sprint" (main 3/3 split → prioritize 6/6).
- W2 / W3 screens (×6, 11 phrases each): `dev/2026/10/12/controls/attribution-1984-wordings-2026-10-12.md` has the three-wording table.
  W2 (drop "what they are working on" and the upload clause) clears the two list rows, keeps the other three. W3 (W2 minus "Not
  session activity") restores "analyze the risk" (4/6) and "behind upstream" (6/6) but loses "what am I working on?" back to
  session_activity 6/6 and still moves "tasks I'm actively working on". The negation sentence is the lever and the damage.
- Unit pins on the candidate: both intent trees + enforcement + the 1595 ledger test 5647 passed.

**Levers (yours; I lean (b) screened, then (c) if it fails — not (a)):**
- (a) Land W2 as a measured trade: on the 10-10 diff it is net positive (the 13 improved rows are mostly the STATUS floor rows PPM
  asked about on 10-08), at the cost of three attributed rows — one ANALYSIS survivor, one QUERY git row, one TODO row. Your
  condition (4) says no; only you can relax it.
- (b) Edit the other side: narrow `session_activity_query`'s description to "what was created or done in THIS chat session" so the
  plan stops reading "my work" as session activity, leaving STATUS's text alone. Same shape as the 10-11 attention inverse that
  screened clean and failed its full run, so: screen on the same 11 rows + the session-activity rows first; one full run only if the
  screen is clean. ~66 + 593 calls.
- (c) Known miss: the #1984 row stays on the ledger as a measured known miss (session_activity→list_archived reading), the served
  reply is honest as it reads today ("We haven't created anything in this session yet. Regarding your archived projects, …"), and CXO
  decides whether #1984 closes on half (1) alone.
- Not a lever: the read_floor_3 adapter — it changes dispatch and the scorer's FLOOR rule, not the router's reading of "my work"
  (routing-stack doc, vocabulary 5).

**Side findings:** "show me when we shipped the API" (10-11 COMPLETION_HISTORY deposit) reads shipped_this_week 6/6 on BOTH trees —
a pre-existing known miss for that lane's ledger, not this candidate's. Main's pattern ceiling re-read 120 this morning (PPM's row:
unchanged, no re-measure).

Verified how: the run's own summary line, `inversion_report_diff.py` output, and the ×6 control tables, all committed (main
at my 07:10 push); served layer = 6 chat turns on a local server with the real router and LLM; router layer = context-free, 593 +
48 + 48 + 12 + 20 + 66 + 66 calls today.

— Lead
