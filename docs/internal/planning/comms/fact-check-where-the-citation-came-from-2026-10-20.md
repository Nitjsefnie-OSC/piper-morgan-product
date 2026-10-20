# Fact-check: "Where the Citation Came From" (Thu 10-29, building)

**Draft:** `docs/public/comms/drafts/where-the-citation-came-from.md` (Comms' full draft, 10-01). xian hasn't touched it yet.
**Checked:** 2026-10-20, before xian's rewrite. An Opus subagent checked it against each agent's own logs for 09-03 to 09-05, commit times, and the m-45 and m-50 frontmatter. Comms reviewed the results.
**Not checked:** the sent memos themselves (only the logs describing them), and CXO's 08-30 carry-forward.

## The record, in order

**Thu 09-03**
- **06:10.** Arch's relay memo is the first place the "subject/scorer separation" idea is attached to m-45. The idea came from CXO's 08-30 carry-forward, which cited nothing (arch 09-05 log :28-30).
- **About 56 minutes later.** PA's killer-test results memo reuses the phrase. Hours later, CXO's verdict copies it from PA's memo (cxo 09-05 :56-64).
- **22:37 fire.** Exec proposed the self-fired vs other-fired sort and asked CIO to refute it. CIO answered with chokepoint vs bolt-on (cio 09-03 :118-125).
  - CIO calls it a "PM-directed joint proposal", and HOST calls it a "PM-requested retro" (host 09-04 :19).
  - Exec's own log doesn't say. **Ask xian whether he started it.**

**Fri 09-04**
- **~07:07.** HOST corrected Exec's role-health-check case (host 09-04 :21).
- **~09:00.** The refinement landed in Exec's inventory.
- **10:48.** CIO shipped the last-invoked marker (bb0e7cd76).
- **16:07-16:17.** HOST drew the machine-written vs self-narrated line. In the same fire, CXO caught their own self-narrated "ran it" line and wrote "m-45 applied to compliance". CIO and HOST repeated the citation.
- **~21:02.** Exec found the marker reporting Docs as "never" (exec 09-04 :125-132).
- **~22:xx.** Docs' omnibus subagent flagged the m-45 citation. Docs opened the file and sent the finding to CIO (docs 09-04 :98-105). CIO fixed its own instance at 22:41 (ff82141f0).

**Sat 09-05**
- **07:00.** PA self-corrected two artifacts.
- **07:09.** HOST corrected two lines in their own log (18d592b66).
- **07:17.** CXO corrected four places.
- **09:57.** Arch ran the `git log -S` trace and sent 8 correction memos, then confirmed all 8 landed (arch 09-05 :24-36).
- **10:00.** PA confirmed against their own log.
- **10:17.** CXO traced their own link and found that CXO had copied PA, not the reverse. CXO wrote the m-45 line (cxo 09-05 :56-74).
- **10:47.**
  - CIO shipped the cold-start backfill (6f9401283).
  - CIO filed m-50, "Self-Attestation Is Not Verification".
  - The incident went into m-45's own entry.
- **16:37.** CXO found that the marker couldn't show whether a reading was observed or derived. CIO shipped a provenance field (7o) in the same fire.
- **22:37.** CXO flagged a cold-start gap in 7o. HOST showed it was already handled.
- **Also Sat.** Docs' heartbeat really had stopped after 09-02 (host 09-05 :31,41).

## Claims to fix

| Draft says | Record | Fix |
|---|---|---|
| "On Friday morning … Exec proposed … CIO replaced that" | The proposal and refutation were Thursday night. The revision landed Friday morning | "By Friday morning, Exec's proposed sort had already been replaced…" |
| The question was "my agents'" own | CIO and HOST say xian directed or requested the retro. Exec's log is silent | Ask xian. If he started it, say so |
| Cited m-45 "for the idea that an agent can't verify their own compliance" | The original phrase (09-03) was "subject/scorer separation": an agent can't grade its own output. CXO extended it to compliance on 09-04 | "…citing it for the idea that an agent can't grade its own work, and then for compliance too" |
| "Several agents" | Four used it in memos (Arch, PA, CXO, CIO), and HOST repeated it in a log | Optional: "four agents" |
| "Arch … sent the corrections out to every place the citation had reached" | Arch sent 8 correction memos. PA, CXO, HOST and CIO corrected their own files | "…sent corrections to everyone it had reached" |
| The trace paragraph omits who copied whom | CXO first said PA had erred "independently". CXO's own trace showed CXO had copied PA | Worth a line. It's the sharpest instance |
| Exec found the marker saying Docs never ran it, "despite plenty of real activity. The fix had a blind spot" | "Never" was wrong, but Docs' heartbeat really had stopped after 09-02 | Consider the twist: the false "never" hid a real lapse |
| "a second fix too … caught and closed by the end of Saturday" | Three rounds: 7j (Fri), the backfill 7l (Sat AM) and provenance 7o (Sat PM). The Saturday-night "gap" was already covered | "…a second and third fix by Saturday night, and one more scare that proved already covered" |
| "two fixes that each needed fixing" | 7j needed 7l, and 7l prompted 7o. 7o didn't need fixing | "…fixes that kept needing fixes" |
| PA quote "There was no independent arrival." | It is in PA's log, lowercase and mid-sentence (pa 09-05 :58). The memo wasn't checked | Cite it as from PA's log |
| "Docs opened the actual document … Docs flagged it" | A subagent of Docs flagged it first. Docs checked before sending | Fine as written |

**True as written:**
- HOST corrected Exec's fact, then drew the machine-written vs self-narrated line.
- CXO's near-miss.
- CIO's marker shipped Friday morning.
- Exec's evening finding.
- m-45's title.
- CIO fixed its own instance the same day.
- PA found the citation in two more documents.
- HOST found it twice in its own log.
- CXO fixed four places.
- Arch used version history.
- The memo was "two days earlier".
- The memo attached CXO's correct, uncited idea to the wrong number.
- "Less than an hour later" (56 min).
- The CXO quote.
- Arch's trail ended at Arch's own memo.
- m-50's title and date.
- The episode was added to m-45.
- CXO's heartbeat had stopped 24 days earlier, and MANIFEST regeneration 36.
- Nothing of xian's is credited to an agent.

## Voice and template

- **H1** matches the calendar.
- **Tease.** It was a bracketed placeholder. Comms filled it (10-20) to target Tue 11-03 "The Unguarded Entrance", using the scaffold's own one-sentence premise.
- **Banned word:** "quietly" (once).
- **Claude-isms:**
  - "deceptively simple"
  - "showed, by accident, exactly what…"
  - "The citation that didn't say what it said"
  - "The strange part"
  - "their agreement looks like confirmation, and it isn't"
  - "Arch's trace didn't spare Arch"
  - "The fix had a blind spot of its own on its very first day"
  - the three-part recap at the close
- **Gloss:** "m-45" in the CXO quote needs "(methodology-45)". "Relay memo" is unglossed.
- **Clean:** 0 semicolons, no agents called people, no issue numbers in the prose.
