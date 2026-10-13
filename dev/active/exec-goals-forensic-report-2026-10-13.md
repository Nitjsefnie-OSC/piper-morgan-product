# Where has xian written down the five goals? Forensic report (2026-10-13)

## 1. Bottom line

- **Earliest dated statement found: 2026-01-05**, an agent's paraphrase of xian (HOST log), covering goals 1, 2, 3 and (loosely) 4 and 5. Nothing earlier was found in the searched places. Committed to git 2026-01-09 (log first added) and re-airlifted 2026-03-13.
- **Three restatements found** (2026-01-05, 2026-09-14 recorded 2026-09-21, 2026-10-13), plus one adjacent 2025-10-22 quote on serving only what he has tasted himself. This is not "many times."
- **No intentional, durable document holds all five goals in order.** The only complete five-in-order text is the shared-memory file written today (2026-10-13). Memory has no git history and is not read as a briefing.
- **Absent from every start-of-session surface:** CLAUDE.md, README.md, `docs/briefing/PROJECT.md`, `BRIEFING-CURRENT-STATE.md`, the Exec briefing. The memory index lists the 10-13 file only as a one-line pointer.
- **Missing:** a vision/goals document in this repo (or in the private repo). Goals 4 and 5 were never expanded anywhere; goal 5 as "revenue, open source community, consulting" appears only on 2026-10-13.

## 2. Timeline (oldest first)

| Date | Path | Speaker | Quote | Goals |
|---|---|---|---|---|
| 2025-05-27 | `docs/omnibus-logs/2025-05-27-omnibus-log.md` | agent synthesis | "Original Question... system that could learn organizational context" | none (product question, not a personal goal) |
| 2025-10-22 | `dev/2025/10/22/chief-architect-alpha-planning-report.md` (l.566) | xian, quoted | "I am not going to serve food to anyone else I have not yet tasted (and digested) myself." | 3 before 4 (ordering only) |
| 2026-01-05 | `dev/2026/01/05/2026-01-05-0958-hosr-opus-log.md` (l.93-99, 11:03 entry) | HOST agent paraphrasing xian | "xian shared the project's escalating goals (started late May 2025): 1. Learning... 2. Educational: Build in public, demystify/dehype for old-school UX/product colleagues 3. Personal utility... 4-10. Progressive ambitions: useful for other PMs → real product → open source → platform → MCP → standards" | 1, 2, 3, 4, part of 5 (open source only) |
| 2026-01-15 | `dev/2026/01/15/2026-01-15-1234-comms-opus-log.md` (l.42) | Comms agent | "Established voice: 'YouTube craftsman with a channel' - demystifying, showing warts, inviting in" | 2 |
| 2026-09-14 (recorded 2026-09-21, commit e816cc62) | private repo `designinproduct/docs/agents/themis/entities.md` ("success ladder and ship gate, on the record") | Themis agent recording xian's 9/14 call | "Five tiers: (1) Learn, achieved; (2) help others via the open blog, achieved; (3) make something Xian actually uses, not yet...; (4) useful for others; (5) sustainable." | all five, same order, terse |
| 2026-10-13 | `~/.claude-pm/.../memory/project_goals_and_weekly_ship_purpose.md` (not in git) | xian via Exec | "(1) I learn things; (2) I share my experience, demystify, and invite others into this space; (3) Piper Morgan becomes useful for me; (4) Piper becomes useful for other people; (5) Piper becomes sustainable (revenue, active open source community, consulting around supporting it)." | all five, full wording |
| 2026-10-13 | `dev/2026/10/13/2026-10-13-0422-exec-code-log.md` (l.62) | Exec | "Saved his five goals and the Ship's purpose to shared memory" | pointer |

Related, not statements of the goals: `docs/internal/planning/comms/xian-voice-tone-guide.md` l.63 "Demystifies rather than gatekeeps" (voice guide; first version 2025-08-27 in `docs/internal/planning/historical/`) touches goal 2 only.

## 3. Where it lives today / where it does not

Lives (all partial or private): (a) the 10-13 memory file, complete and in order, current, but no git history and not an intentional project document; (b) the 2026-09-21 private-repo entry, five tiers in order but one terse line with no goal 5 detail; (c) the 2026-01-05 HOST log, a dated log, stale on wording (10 "ambitions", no revenue or consulting).

Does not live in: `CLAUDE.md` (no match), `README.md` (no match), `docs/briefing/PROJECT.md` (only a "Learning Philosophy" section about learning from failed attempts; says nothing of xian's goals), `BRIEFING-CURRENT-STATE.md` (no match), `BRIEFING-ESSENTIAL-CHIEF-STAFF.md` (mission is coordination only), any PDR or ADR (`git grep` for the goal phrases returned none), `docs/public` posts (no goal statement found; "sustainable" hits there are unrelated uses). The memory index (MEMORY.md l.18) carries a one-line pointer to today's file only.

## 4. Drift

- 2026-01-05 (agent): "Personal utility... 4-10. Progressive ambitions: useful for other PMs → real product → open source → platform → MCP → standards". Sustainability and revenue are absent; open source is a rung, not part of a sustainability goal; goals 1 and 2 marked achieved.
- 2026-09-21: "(4) useful for others; (5) sustainable." Order preserved, goal 5 undefined.
- 2026-10-13: goal 5 now "revenue, active open source community, consulting". So goal 5 widened from "open source" (Jan) to a three-part sustainability bundle (Oct); "platform / MCP / standards" rungs dropped.
- Goal 3 wording shifts: "Personal utility: Persistent, learning, PM-aware AI assistant" (Jan), "make something Xian actually uses" (Sep), "Piper Morgan becomes useful for me" (Oct). Meaning stable; "useful for me" was never dropped in any version found.
- Order never changed in any version found. Revenue was never ranked higher.
- Other "goals"/"north star" uses in the repo (the "North Star test" of creating a GitHub issue; the UX audit "North Star Vision"; the duty-cycle "North Star") are product or process targets, not these goals. Do not conflate them.

## 5. Verified how

Layer: text search of committed content on `origin/main` (fetched 2026-10-13; worktree dirty with one unrelated file so I used `git grep ... origin/main`, not the working tree). Denominator: about 39,640 tracked files on origin/main; `git grep` covered all of them for the phrase searches ("demystif", "invite others", "share my experience", "useful for me", "useful for other", "I learn things", "north star") and, for the wider variants ("goals", "sustainab", "consulting", "open source community", "success ladder", "motivation", "learning project"), `docs/`, `knowledge/`, `mailboxes/`, `dev/2025`, `dev/2026`, `README.md`, `CLAUDE.md`. Dated via `git log --diff-filter=A` and `git log -S` on the HOST log and the private entry. Shared memory: grep over about 224 files in the memory dir, 1 match for the five goals (written today). Private repo: grep of `docs/` (24 entries at top level) for the same terms; one relevant hit plus voice/positioning uses of "demystifier" (an outside host's word for xian, 2026-07-25 onward, goal 2 only; not named here).

**Not searched:** the website repo (`piper-morgan-website*`) and the live site's About page; LinkedIn newsletter and Medium posts outside what is in `docs/public/`; the first six months of `dev/2025` beyond the phrase searches (no line-by-line read of day logs or the 2025-05 to 2025-12 retrospectives); `dev/2026` day logs beyond grep hits; `mailboxes/` older boxes beyond grep hits; Granola transcripts, Slack, Gmail, calendar and any live chat or voice conversation (xian says he has said it many times; spoken statements would not appear in git); Claude Desktop project instructions; `docs/internal/product/pdr/` read file by file (grep only); JSON/CSV files were excluded from the first pass; the private repo's `docs/mail/` was not read file by file.
