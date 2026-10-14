# Option 3: day-one path check of the 61 live routing literals (2026-10-14)

**Ruling:** xian via Exec 09:28 10-14: Option 1 (MVP does not wait for the 61; they are Epic 0 work after MVP) plus Option 3
(Arch names the day-one design-partner paths, Lead checks the 61 against them before 10-23; a wrong claim on a day-one turn gets an
MVP issue). **Arch's paths:** `mailboxes/lead/read/paths-arch-to-lead-cc-ppm-exec-option-3-day-one-paths-for-the-61-check-2026-10-14.md`
(P1–P9, from beta-gate-standard Class 4, #1386 A/B/C as CXO refreshed them 10-07, and the C3 feature set). **Arch's primary test:**
does any of the 61, as it stands on main, claim a day-one phrasing and send it somewhere other than where the router would?

**Verdict: none.** No MVP issue. Two Epic 0 notes at the end (post-MVP corpus rows, not day-one risks).

## 1. The 61 (literal ceiling 90 in 35 lists, read 09:48 10-14 with `scripts/pattern_literal_counts.py`, minus the 29 floor)

Floor (#1974, CXO: pure pleasantries keep the canned short-circuit): GREETING_PATTERNS 9, FAREWELL_PATTERNS 5, _PLEASANTRY_FILLER_PATTERNS 10, THANKS_PATTERNS 5 = 29.
Live: 61 literals in 18 lists. Claim site: `PreClassifier._pre_classify_claim` (`services/intent_service/pre_classifier.py`).

### ANALYSIS_PATTERNS (4)

- `r"\bwhat.*obstacle\b"`
- `r"\bwhat'?s in the way\b"`
- `r"\banalyze.*(?:risk|impact|blocker|bottleneck)\b"`
- `r"\bimpact analysis\b"`

### COMPLETION_HISTORY_PATTERNS (2)

- `r"\bwhen did (i|we) (complete|finish|ship|deliver|launch|close|wrap up|finalize)\b"`
- `r"\bshow me when (i|we) (completed|finished|shipped|delivered|launched|closed)\b"`

### CONTEXTUAL_QUERY_PATTERNS (1)

- `r"\bneeds my attention\b"`

### DISCOVERY_PATTERNS (1)

- `r"\bneed\s*help\b"`

### DOCUMENT_QUERY_PATTERNS (10)

- `r"\bupdate\s+(?:the\s+)?[\w\s]+\s+doc(?:ument)?\b"`
- `r"\bedit\s+(?:the\s+)?[\w\s]+\s+doc(?:ument)?\b"`
- `r"\bmodify\s+(?:the\s+)?[\w\s]+\s+doc(?:ument)?\b"`
- `r"\bchange\s+(?:the\s+)?[\w\s]+\s+doc(?:ument)?\b"`
- `r"\badd\s+(?:to\s+)?(?:the\s+)?[\w\s]+\s+doc(?:ument)?\b"`
- `r"\bappend\s+(?:to\s+)?(?:the\s+)?[\w\s]+\s+doc(?:ument)?\b"`
- `r"\bupdate\s+(?:the\s+)?[\w\s]+\s+with\b"`
- `r"\bedit\s+(?:the\s+)?[\w\s]+\s+with\b"`
- `r"\bmodify\s+(?:the\s+)?[\w\s]+\s+with\b"`
- `r"\bchange\s+(?:the\s+)?[\w\s]+\s+to\b"`

### INTEGRATION_CONNECT_PATTERNS (1)

- `r"\b(?:connect|set\s?up|link|hook\s+up|integrate|add|enable)\b.{0,40}?"
        r"\b(?P<integration>github|slack|notion|(?:google\s+)?calendar)\b"`

### LOCAL_GIT_STATUS_PATTERNS (1)

- `r"\bbehind (?:main|origin|upstream|master)\b"`

### MEMORY_PATTERNS (3)

- `r"\b(my|our) (conversation )?history\b"`
- `r"\bsearch (my |our )?(conversation )?history\b"`
- `r"\bwhat (i|we) (said|talked|discussed)\b"`

### PORTFOLIO_PATTERNS (14)

- `rf"\barchive\s+{PROJECT_NOUN_REQUIRED}(?:my\s+)?(?:the\s+)?(?:project\s+)?(.+)"`
- `rf"\bhide\s+{PROJECT_NOUN_REQUIRED}(?:my\s+)?(?:the\s+)?(?:project\s+)?(.+)"`
- `rf"\bput\s+{PROJECT_NOUN_REQUIRED}(.+)\s+(?:away|aside)"`
- `rf"\bdelete\s+{REMINDER_TODO_NOUN_GUARD}{PROJECT_NOUN_REQUIRED}(?:my\s+)?(?:the\s+)?(?:project\s+)?(.+)"`
- `rf"\bremove\s+{REMINDER_TODO_NOUN_GUARD}{PROJECT_NOUN_REQUIRED}(?:my\s+)?(?:the\s+)?(?:project\s+)?(.+)"`
- `rf"\bget rid of\s+{REMINDER_TODO_NOUN_GUARD}{PROJECT_NOUN_REQUIRED}(?:my\s+)?(?:the\s+)?(?:project\s+)?(.+)"`
- `rf"\brestore\s+{PROJECT_NOUN_REQUIRED}(?:my\s+)?(?:the\s+)?(?:project\s+)?(.+)"`
- `rf"\bunarchive\s+{PROJECT_NOUN_REQUIRED}(?:my\s+)?(?:the\s+)?(.+)"`
- `rf"\bbring back\s+{PROJECT_NOUN_REQUIRED}(?:my\s+)?(?:the\s+)?(?:project\s+)?(.+)"`
- `r"\bfind\s+(?:my\s+)?project\s+(.+)"`
- `r"\b(?:add|create)\s+(?:a\s+)?(?:new\s+)?project\b"`
- `r"\bnew project\b"`
- `r"\bupdate\s+(?:my\s+)?(?:the\s+)?project\b"`
- `r"\bedit\s+(?:my\s+)?(?:the\s+)?project\b"`

### PROVENANCE_PATTERNS (5)

- `r"\bwhere did (you get|that come from|you find)\b"`
- `r"\bhow did you know( about| that)?\b"`
- `r"\bwhy.* on (my|your|the) (list|radar|mind)\b"`
- `r"\bbased on what\b"`
- `r"\bwhat'?s that based on\b"`

### REMINDER_PATTERNS (1)

- `r"\bset\s+(?:a\s+)?reminder\b"`

### REPO_MANAGEMENT_PATTERNS (4)

- `r"\blink\s+(?:(?:my|the|a)\s+)?(?:repo(?:sitory)?)\s+(?:to\s+)"`
- `r"\bconnect\s+(?:(?:my|the|a)\s+)?(?:repo(?:sitory)?)\s+(?:to\s+)"`
- `r"\badd\s+(?:(?:my|the|a)\s+)?(?:repo(?:sitory)?)\s+to\s+"`
- `r"\bwhich\s+repos?\s+(?:are\s+)?(?:linked|connected)\b"`

### REPO_UNLINK_PATTERNS (3)

- `r"\bunlink\s+(?:(?:my|the|a)\s+)?(?:repo(?:sitory)?)"`
- `r"\bremove\s+(?:(?:my|the|a)\s+)?(?:repo(?:sitory)?)\s+from\s+"`
- `r"\bdisconnect\s+(?:(?:my|the|a)\s+)?(?:repo(?:sitory)?)"`

### SET_DEFAULT_REPO_PATTERNS (4)

- `r"\b(?:set|change|update|make)\s+(?:my\s+)?default\s+repo(?:sitory)?\b"`
- `r"\buse\s+[\w.-]+/[\w.-]+\s+as\s+(?:my\s+)?default\s+repo(?:sitory)?\b"`
- `r"\bmake\s+[\w.-]+/[\w.-]+\s+(?:my\s+)?default\s+repo(?:sitory)?\b"`
- `r"\b(?:my\s+)?default\s+repo(?:sitory)?\s+(?:is|should be|=)\s+[\w.-]+/[\w.-]+"`

### STAKEHOLDER_UPDATE_PATTERNS (1)

- `r"\bwrite\s+(?:me\s+)?(?:a|an)?\s*(?:\w+\s+){0,3}update\s+for\b"`

### STATUS_PATTERNS (4)

- `r"\bcurrent work\b"`
- `r"\bproject overview\b"`
- `r"\bnext milestone\b"`
- `r"\bstatus report\b"`

### TODO_COMPLETE_PATTERNS (1)

- `r"\bmark\s+done\b"`

### TRUST_PATTERNS (1)

- `r"\bwhy can'?t you\b"`

## 2. The day-one phrasings through surface 1 (`pre_classify_with_pattern_list`, main, no LLM)

| path | phrasing | claiming list | claimed action |
|---|---|---|---|
| P1 | OK, what CAN you actually do right now? | — | — |
| P2 | Connect my GitHub | INTEGRATION_CONNECT_PATTERNS | get_contextual_guidance |
| P2 | is my GitHub connected? | — | — |
| P3 | Create an issue: 'Login page times out on mobile' | — | — |
| P3 | Let's track this. Create a GitHub issue: 'Login page times out on mobile' | — | — |
| P3 | Actually, change the title to 'Mobile login timeout' | DOCUMENT_QUERY_PATTERNS | update_document_query |
| P3 | change the title of issue #12 to 'Mobile login timeout' | — | — |
| P4 | Show me that issue. | — | — |
| P4 | What issues did we create in this session? | — | — |
| P4 | show my open issues | — | — |
| P4 | list my repos | — | — |
| P5 | help me break this down into smaller tasks | — | — |
| P5 | Can you help me break this down into tasks? | — | — |
| P6 | Can you summarize my Notion docs for me? | — | — |
| P6 | What about my company GitBook wiki? | — | — |
| P6 | what's on my calendar tomorrow? | — | — |
| P6 | send a Slack message to the team | — | — |
| P7 | add a todo to review the onboarding copy | — | — |
| P7 | remind me to call the dentist at 3pm | — | — |
| P7 | show my todos | — | — |
| P7 | what's on my list | — | — |
| P7 | complete review the onboarding copy | — | — |
| P7 | mark review the onboarding copy done | — | — |
| P7 | complete todo 2 | — | — |
| P7 | delete todo 2 | — | — |
| P7 | clear my todos | — | — |
| P8 | create a project called Mobile Login | PORTFOLIO_PATTERNS | manage_portfolio |
| P8 | list my projects | — | — |
| P9 | what's on today? | — | — |
| P9 | where am I with the mobile login work? | — | — |
| P9 | what time is it? | — | — |
| P9 | what's the date today? | — | — |

A second sweep of 42 plain-form variants (connect/link GitHub ×4, capability ×3, create-issue ×3, title-change ×5, GitHub read ×5,
todo/reminder ×9, project ×5, status/time ×5, planning ×3; script in the 10-14 Lead log) produced the same three claiming lists and
no others: INTEGRATION_CONNECT (every connect/link form), DOCUMENT_QUERY (`change … to` forms only; "update the title to", "rename it
to", "edit the issue title to" are unclaimed), PORTFOLIO ("make a new project called …", "new project: …"). Everything on P4, P5, P6,
P7 and P9 reaches the router unclaimed.

## 3. The three claims against the router (×6, Haiku-class router, `dev/2026/10/14/controls/opt3-claims-x6.md`, 30/30 served anthropic:claude-haiku-4-5, 0 errors)

| phrasing | surface 1 claim | router ×6 | same served outcome? |
|---|---|---|---|
| Connect my GitHub (P2) | INTEGRATION_CONNECT → `get_contextual_guidance` | `get_contextual_guidance` ×6 @0.95 | **yes** — identical op |
| Actually, change the title to 'Mobile login timeout' (P3, original B3) | DOCUMENT_QUERY (`\bchange\s+(?:the\s+)?[\w\s]+\s+to\b`) → `update_document_query` | `update_issue` ×6 @0.85 | **yes in the day-one turn** — see below |
| create a project called Mobile Login (P8) | PORTFOLIO (`\b(?:add|create)\s+(?:a\s+)?(?:new\s+)?project\b`) → `manage_portfolio` | `add_project` ×6 @0.99 | **yes** — same handler, see below |

**Correction (11:06 10-14, Arch's reading of `intent_service.py` ~2520–2577):** on an UNARMED turn the live router consult
(`consult_inversion_live`) runs BEFORE `classify_multiple`, and Stage 0 and surface 1 both live inside `classify_multiple`; inside the
consult, `pre_classify` is telemetry only. So the order is router → (if the consult falls through) Stage 0 → surface 1, not Stage 0 first.
The verdict holds for a second reason: the router emits `update_issue`, a WRITE that is NOT in `FLIP_WRITE_ALLOWLIST`
(`workflow_dispatcher.py` ~483), so the consult falls through and Stage 0 resolves the session's issue as described below. Standing
condition (Arch, decisions.log 10-14 11:1x): no referent-dependent write (`update_issue` today) enters the allowlist until the consult
stands down when Stage 0 would resolve a referent.

**P3, the implicit title change.** Surface 1 is not the first surface this turn meets. `IntentClassifier.classify` and
`detect_multiple_intents` both run Stage 0 first (`classifier.py` ~361 and ~676, #1394 / ADR-078 D2): `_resolve_issue_referent`
reads the session's created-issue ledger and emits `update_issue` directly when the message is an issue-field follow-up with no
explicit number (`_detect_issue_referent("Actually, change the title to 'Mobile login timeout'")` → True, verified on main) and the
session created an issue. B3 always follows B2 (the issue was created this session), so on the day-one path the literal never sees
the turn; pinned by `tests/unit/services/intent_service/test_b3_referent_resolution_1394.py`. The explicit forms ("change the title
of issue 12 to …" with and without `#`) are caught one step earlier by `_detect_explicit_issue_update` (→ 12, verified), #1411's pin.
What remains for the literal is the **cold** form (no issue created this session): surface 1 says `update_document_query`, the router
says `CLARIFY` @0.40. Not a day-one turn; it is the Epic 0 note below.

**P8, the project create.** The PORTFOLIO claim dispatches `manage_portfolio` → `_handle_portfolio_query`, whose operation sniff
(`canonical_handlers.py` ~4580: `add`/`create`/`new project`) sets `operation = "add"` and returns `await self._handle_add_project(...)`
(~4627–4629). The router's `add_project` rail entry calls that same method (`action_registry.py` ~497, "#1856 argument-consuming
add"). Same handler, same served answer; the name-absent clarify idiom (#1867) sits inside the shared method.

**P2, the connect.** Same op from both surfaces; the integration-connect lane is the designed path for A2.

## 4. Epic 0 notes (post-MVP, no slip, no issue now)

1. `DOCUMENT_QUERY_PATTERNS` row `\bchange\s+(?:the\s+)?[\w\s]+\s+to\b` is the one literal that claims a GitHub-shaped phrasing
   when the ledger is empty ("change the title to 'X'" cold → document lane; router → CLARIFY). The #1411 comment in `classifier.py`
   already records the same literal as the hard misroute for "change the title of issue 108 to …" before the explicit detector existed.
   A corpus row for the cold form belongs with the DOCUMENT_QUERY list's deletion gate, not before MVP.
2. `PORTFOLIO_PATTERNS` is 14 of the 61 and its claims all terminate in the split handlers (#1595 Phase 3); its deletion is a
   routing-quality question, not a day-one one.

## Verified how

Surface 1: `PreClassifier.pre_classify_with_pattern_list` on main (HEAD of 10-14 09:4x), 35 Arch phrasings + 42 variants, no LLM,
matched literal recovered with `_first_pattern_match` / `_integration_connect_match`. Stage 0: `_detect_issue_referent` and
`_detect_explicit_issue_update` called directly on the P3 forms. Router: `scripts/inversion_router_control.py --provider anthropic
--samples 6` on the three claimed phrasings plus two B3 variants, 30 calls, served line checked. Handlers: read, not run
(`_handle_portfolio_query` add branch → `_handle_add_project`; `document_update_entry`/`update_issue_entry` in `workflow_entries.py`).
Layer: classification surfaces and dispatch targets, not the served HTML. Denominator: all 9 paths, all 11 scripted A/B/C turns and
the C3 feature set as Arch mapped them; 77 phrasings; 3 claims; 61 literals enumerated in §1.
