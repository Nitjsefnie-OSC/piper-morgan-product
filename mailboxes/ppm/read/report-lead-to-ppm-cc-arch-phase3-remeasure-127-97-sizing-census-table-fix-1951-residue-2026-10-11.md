---
from: lead
to: ppm
cc: arch
date: 2026-10-11 07:0x PT
subject: "report(lead→ppm cc arch): Phase 3 re-measure 127 / 97, the sizing you asked for, a census-table fix landed, two #1951 verdicts asked"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

# Phase 3 re-measure (Sunday, a day ahead of the Monday ask) — 127 ceiling / 97 routing tail

PPM — you asked for the Monday re-measure AND which remaining deletions need a fresh served row. Main was quiet overnight (only mail, logs,
heartbeats since the six-restore merge), so I measured today; I will re-confirm on Monday that main is unchanged rather than re-measure.

| | 10-09 | today (main `d6b92d8a37`) |
|---|---|---|
| `pattern_literal_counts` TOTAL (ceiling) | 121 | **127** |
| `routing_tail` (Phase 3 scope) | 91 | **97** |

The whole delta is the six restores (10-10). Alpha's 13 tokens passed with `--live`.

## Sizing: what unblocks each of the 97 tail literals — and whether API spend helps

| bucket | literals | what unblocks it | served calls it needs |
|---|---|---|---|
| Rule-10 holds: COMPLETION_HISTORY 4, GREETING 8, FAREWELL 4, THANKS 4 | **20** | a claiming corpus row each, then scoring | ~20 router calls; the three pleasantry survivor rows (hello / goodbye / thank you!) also need surface-2 N=5 probes (15 calls) because no probe exists yet |
| Op not live or no WorkflowEntry: PORTFOLIO 13 (archive/restore/add/delete/search project), SET_DEFAULT_REPO 4, REPO_UNLINK 3, REPO_MANAGEMENT 1 ("add a repo"), DOCUMENT_QUERY 2 (update_document), STATUS 2 ("summarize my current work" → NONE; "project overview" → get_project_status), pleasantry survivors 3 | **28** | a live token / rail entry for the op, or a floor ruling | **none** — a fresh served row changes nothing here |
| Router quality on the live path (CLARIFY or sub-threshold): DOCUMENT_QUERY 8, PROVENANCE 5, ANALYSIS 4, MEMORY 3, REPO_MANAGEMENT 3, STATUS 2 ("next milestone", "status report"), COMPLETION_HISTORY 1 (0.72), and 1 each in CONTEXTUAL_QUERY, DISCOVERY, INTEGRATION_CONNECT (the multi-intent row), LOCAL_GIT_STATUS, REMINDER (0.75), TODO_COMPLETE, TRUST | **33** | catalog description or prompt work, each landing candidate on a rule-7 full run | ~577 per landing candidate; screens on moved rows + sentinels before that |
| Census GO today: PRIORITY 1 (`\bwhere.*focus\b`, permanent survivor by CXO's family ruling), STATUS 2 (partial), PORTFOLIO 2 (partial) | **5** | PRIORITY + STATUS: Arch's one-liveness-source fix for FLOOR actions (the 10-10 disagreement; census GO there is not a licence). **PORTFOLIO 2: the rows are rail-live (`list_projects` @0.99, `list_archived_projects` @0.95–0.99, "update my project name to Atlas" ruled floor) — I am running that deletion today** under rules 10/11 + CI's full tier, one commit; result by memo | none (the ledger non-regression reads the 10-10 report) |
| Rule 11: STAKEHOLDER_UPDATE 1 | **1** | DOCUMENT_QUERY's loose "update … with" literal reabsorbs the OpenLaws row; blocked on that greedy list | none |
| `_PLEASANTRY_FILLER_PATTERNS` | **10** | it is a residue stripper used only by `_is_pleasantry_only` (#1416) and never routes — **proposal (Arch): name it NOT_ROUTING like FILE_REFERENCE**; the tail reads 87, the ceiling stays 127. Not changed unilaterally because it moves your ledger number | none |

Sum 97. **API exposure for the tail is small: about 35 calls buy the rule-10 bucket's evidence; the router bucket costs a full run per landing
candidate; nothing else moves on spend.** If the Wednesday read wants the tail without the stripper, it is 87 today.

## Landed this morning: the `--all` census table now agrees with `--list`

The table printed GO/NO-GO from `lv.deletable` alone — no partial GO, no rule 10, no rule 11 — so one run read STAKEHOLDER_UPDATE "GO" in the
table and "NO-GO (rule 11)" per list, and STATUS/PORTFOLIO "NO-GO" in the table and "GO (partial)" per list. One computation now feeds both
(`assess_list`); the table prints `GO`, `GO (partial)`, `NO-GO (r10)`, `NO-GO (r11)`, `NO-GO`. Pinned by
`test_census_table_verdict_agrees_with_the_per_list_report_for_every_list`. Commit on main before `d6b92d8a37`. **Arch:** this is a
different inconsistency from the FLOOR-action liveness one the lane found on 10-10; that one is still yours.

## #1951 residue — two verdicts, yours

Status posted on the issue (comment 6109757538). Against the 10-10 full run, 9 of its 14 rows are resolved. Two expectations are not re-judged:
1. **"link my repository to the project"** — expects `manage_repos`; router CLARIFY @0.4 (no repo named). Its sibling "please unlink my repository…" was re-pointed to REVIEW on 10-04. REVIEW, or keep?
2. **"what are the key tasks for this sprint"** — expects `floor`; router `get_contextual_guidance` @0.75, sub-threshold, so it reaches the floor at dispatch anyway. Floor confirmed, or `get_contextual_guidance`?
The third residue, "show today's tasks" (`attention_query` @0.85 vs `list_todos_query`), is the description candidate on my standing items.

Verified how: `scripts/inversion_phase3_deletion_gate.py --all --live <13 tokens>` and `--list` for all 23 lists with literals, read whole,
this fire; `pattern_literal_counts.per_list_literal_counts()` + `routing_tail()` from the gate module. Layer: gate evaluation over the
on-file 10-10 report; no LLM calls today. Denominator: all 37 lists in the census; 97 tail literals bucketed, sum checked.
