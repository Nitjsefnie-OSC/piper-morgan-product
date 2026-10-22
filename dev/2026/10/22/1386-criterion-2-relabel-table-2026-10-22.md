# #1386 criterion 2: the relabel table for Run 1's 8 routing misses (PA, for Lead's signature, 2026-10-22)

**Asked by:** PPM's 10-22 10:19 memo (ask to PA), under PPM's ruling on #1386 (comment 6346811165). The 10-20 rule applies: each relabel rests on a dated line of the routing design, not on the answer being acceptable. Lead signs or rejects each row; a rejected row stays a fail.

**Run:** `dev/2026/10/19/canonical-retest-1386-alpha-20261022-1004-results.csv`, alpha `76789a8988`, account `web-seed-1386`. Routing 53 of 61 (86.9%) against the ≥ 90% bar. The harness reads routing by effect (PPM 10-20 15:58): `floor` if the floor answered; `action` if the rail entry's effect is WRITE or more (or EXECUTION category with no entry); else `canonical`.

**Prepared by:** PA. An Opus research subagent read Q33, Q37 and Q62. PA re-read its three load-bearing citations (decisions.log:2683, corpus 2801-2805 and 1225-1228) and confirmed `f6d26bcd37` is in alpha (`merge-base --is-ancestor`). PA read Q19, Q25, Q31, Q44 and Q45 against the 10-20 table and the #2119/#2120 records.

**How to sign:** put `SIGNED` or `REJECTED` (with a reason) after each row's Strength and commit. PA then applies the signed rows to the harness's `CANONICAL_QUERIES` with a one-line comment each.

**What it means for the number:**

| Rows signed | Routing |
|---|---|
| none (Run 1 as it stands) | 53 of 61 (86.9%) |
| Q33 and Q62 (the two "ruling" rows) | 55 of 61 (90.2%) |
| Q33, Q62 and Q45 | 56 of 61 (91.8%) |

Q19, Q25, Q31, Q37 and Q44 stay fails in every case.

| Q | Query | Label old → proposed | Actual cat/action | Design basis (file:line, quote) | Strength | Tells against / caveats |
|---|---|---|---|---|---|---|
| 33 | Find time for a 1:1 with the team lead | canonical → floor | TEMPORAL / meeting_time | decisions.log:2683 (Arch, 2026-10-20 13:20): "#2112 RULED: … conflicts and find-time-with-someone go to floor at NONE 0.85-0.95; own free time goes to week_calendar". Corpus 2801-2805, this exact phrase, `expected: floor`, note "Arch 2026-10-20: finding a slot with someone else is floor (twin of 'find time for a 1:1 with sarah'); the router's NONE now stands over the legacy TEMPORAL landing (#2112)". Moved by `f6d26bcd37` (10-20 13:34, in alpha). | ruling | The 10-20 "pass" (canonical, `provide_current_time_with_calendar`) served the date and time, which was #2112's defect. Judge MARGINAL here; CXO waived Q33. |
| 62 | Check my calendar for conflicts | canonical → floor | TEMPORAL / check_calendar_conflicts | Same ruling, decisions.log:2683 ("conflicts … go to floor"). Corpus 1225-1228, this exact phrase, `expected: floor` (siblings "is there a conflict on my calendar" also floor). `f6d26bcd37`'s message names the phrase. | ruling | The corpus row carries no dated note (regex-literal source); the date comes from the ruling. CXO puts the reply's multi-person framing on #2130. Judge PASS. |
| 45 | Close completed issues | floor → action | execution / close_issue_query | #2120 (Class 3, CXO-ruled 10-20): CXO wrote this ask's answer for the close handler's no-number fallback ("I can close a particular issue if you give me its number, like "close #123". I don't search for finished issues or close them in bulk yet."); Lead landed it there (`71b4b15eed`, pins `test_issue_close_reopen.py`, `test_github_query_handlers.py`); CXO accepted it served. Run 1 served those words. | ruling (an issue disposition placing this ask's answer on the action handler, not a routing-design line as such) | On 10-20 the table kept Q45 a fail "in every case" because the answer was false; that defect is closed. Lead weighs whether a CXO-ruled handler answer counts as a design line for the route. Judge PASS. |
| 19 | Generate a status report | floor → **keep** | query / generate_report | None new. Lead (#2119, 10-20 16:21): "The routing row (expected floor, actual `generate_report`) stays a routing fail as PA left it." CXO (10-22): "the expected-floor label fits this." | none | Stays a fail. Quality held by CXO (answers a smaller ask without saying so). |
| 25 | What's the next milestone? | floor → **keep** | query / list_milestones_query | Lead REJECTED on 10-20: #1068 (pre_classifier) and the 10-01 CXO/PPM sibling ruling send it to STATUS. Nothing new. | none | Stays a fail. The false "no open milestones" is #1524 (Class 3 must-close). |
| 31 | Schedule a meeting about the roadmap | canonical → **keep** | TEMPORAL / schedule_meeting | Lead REJECTED on 10-20: the #965 `schedule` keyword is a mechanism, not a design line. No corpus row for "schedule a meeting" (grep), and #2112's ruling names find-time and conflicts, not scheduling. | none | Stays a fail. The reply is now an honest decline (judge PASS); the floor reply's false calendar-write claim from 10-20 is gone. |
| 37 | Compare these two documents | floor → **keep** | analysis / analyze_data | Nothing puts "compare" on analyze_data (no corpus row; `classifier.py:541-542` normalizes "compare" to `compare_documents`, which has no rail entry, hence 10-20's floor). | none | Stays a fail. Route is unstable: Run 2 on the same alpha went to the floor (PASS). The repo-metrics answer to a document ask is **#2132** (filed 10-22, with Q17). |
| 44 | Create issues from this meeting's action items | floor → **keep** | execution / create_ticket | Lead REJECTED on 10-20: a rail registration alone is not a design line, and #886's batch decline for this exact ask says the opposite. | none | Stays a fail. The stranded #886 decline is **#2133** (filed 10-22, Lead's lane, on Lead's 10-20 ask). |

Verified how: Run 1 CSV rows for all 8 misses (python csv read: expected/actual routing, category, action, reply, judge). The 10-20 table and the 10-21 rescored 12:27 CSV for each row's prior route. `gh issue view --comments` on #2119 and #2120. decisions.log:2683 and corpus 2801-2805 and 1225-1228 read by PA; `git merge-base --is-ancestor f6d26bcd37 76789a8988` true. `grep` of the corpus for "schedule a meeting" (no row). Subagent (Opus): `git log 54a5ba990f..76789a8988` on the routing paths (26 commits), `router_none_stands` (inversion_live.py:628-683), classifier.py:530-548. Coverage: 8 of 8 misses. Not read: the served turns' provenance logs, so Q37's Run 1 route mechanism (router live or below threshold) is unverified.
