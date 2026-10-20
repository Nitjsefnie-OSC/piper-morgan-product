# Fact-check: "Mistaking the Inset for the Map" (Sat 10-24, insight)

**Draft:** `docs/public/comms/drafts/a-bounded-search-reported-as-a-total.md` (Comms' full draft, 10-02). xian hasn't touched it yet.
**Checked:** 2026-10-20, before xian's rewrite. An Opus subagent checked it against primary logs and git, and Comms reviewed the results.

## The record, in order

- **2026-07-25 14:13.** A stall alert reached CIO: "all currently stale: STALE arch 145h".
  - CIO noted that it "reads cold as *the cohort is fine except arch*" (`dev/2026/07/25/2026-07-25-1053-cio-code-log.md:227-233`).
  - The watch registry had 4 rows (cio, exec, arch, lead).
  - Five roles were dark: arch, cxo, pa, ppm and web. CIO checked this two ways: no session log since 07-19, and zero commits since 07-20.
  - CIO: "Only arch is watched. Four roles have been silently dark for six days" (:231). Elsewhere CIO counts "4 of 10 roles" (:243).
  - CIO proposed alert wording that names the denominator: `stale among 4 watched: arch · NOT WATCHED: cxo, pa, ppm, web` (:235). Unverified whether it shipped.
- **2026-07-27.** CIO filed methodology-44, "Clear Is Not a Measurement", as Arch's bequest (8afafe5dd4). Both quotes in the draft are verbatim.
- **2026-08-05 to 08-10.** CXO wrote six daily START heartbeats. There are six `hb(cxo): START` commits and six `dev/heartbeats/…/cxo.tsv` files. A 7th grep hit is the 08-04 day-close commit, which only mentions the tag.
- **2026-09-03 ~16:37.** CIO shipped the "belt-invisible" detector.
- **19:17.** The detector flagged CXO. CXO wrote "I have never invoked `duty-cycle-heartbeat.sh`. Not once." (`dev/2026/09/03/2026-09-03-1017-cxo-code-log.md:150-155`).
- **Exec, same day.** Exec checked two ways and got 7 commits and 6 files. Exec wrote "Daily STARTs 08-06 → 08-10" (off by one) and reclassified CXO as "invoked, then STOPPED" (exec log :79-84).
- **CXO, 22:17.** CXO wrote "I invoked it 7 times" and reproduced both checks. Their search had been `--since=2026-08-28`, a window that "started 18 days AFTER my last heartbeat". From the same entry: "A bounded search reported as a total", "Third time this week", "An absence is a measurement and it has a window" (cxo log :202-213).
- **2026-09-04.** CXO's heartbeats resume.

## Claims to fix

| Draft says | Record | Fix |
|---|---|---|
| "checked it two independent ways… and found seven invocations" | The two checks disagreed: 7 commits and 6 files. Git shows 6 real heartbeats | "six daily heartbeats" (or "six or seven, depending on how you count") |
| "daily from August 6 through August 10" | 08-05 to 08-10 | "August 5 through August 10" |
| The watchdog "was reporting the team healthy" | It raised a real alert about arch. The flaw was that it read as "everyone else is fine" | "it flagged one stale agent, which read as if everyone else was fine" |
| "CIO went and checked directly" | CIO was following up that alert | Name the alert as the trigger |
| "The all-clear looked exactly like an all-clear" | It was a partial alarm, not an all-clear. "Nothing said 'of four'" is true | Keep "of four" and drop "all-clear" |
| Example "Four of ten agents are healthy" | One of the four watched was the stale one | CIO's own wording: "stale among 4 watched: arch, not watched: cxo, pa, ppm, web" |
| "The fix in both cases…" | Proposed. Unverified whether the alert text changed | "the proposal" or "the cure", not a shipped fix |
| "the default outcome whenever…" | CXO counted 3 of their own that week. That doesn't support a general rule | Make it xian's opinion, or soften |
| "the team wrote the principle down" | CIO filed it from Arch's handoff | Optional: name CIO and Arch |

**True as written:**
- CXO's "Not once" self-criticism, and CXO reproducing both checks instead of taking the correction on report.
- The window was "since August 28" (18 days after the last heartbeat).
- Both CXO quotes and both methodology-44 quotes.
- "third time that week", CXO's own count.
- The 4 of 10 watch list. Five agents dark for six days, one of them watched.
- "about six weeks earlier", and "that same week".
- The dateline.
- No attribution crossed between xian and the agents.

## Voice and template

- **Title.** The H1 still reads "A Bounded Search Reported as a Total". The calendar title is "Mistaking the Inset for the Map" (xian, 10-19).
- **Banned word:** "quietly".
- **Claude-isms:**
  - "That's the part worth taking seriously"
  - "It was a striking admission, and it was false" (a reveal beat)
  - "a missing six becomes impossible to overlook"
- **Tease:** it targets Sun 10-25 "A Clean Result Has a Version Number". It needs updating if xian retitles that post.
- **Clean:** 0 semicolons, no agents called people. "heartbeat script" and "watchdog" are glossed.
