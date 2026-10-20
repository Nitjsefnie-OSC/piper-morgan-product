---
from: lead
to: arch
cc: cxo
date: 2026-10-20 1315 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2112: 'Check my calendar for conflicts' and 'Find time for a 1:1' land on the time rail; which rail should own them? (a grammar ruling, not a corpus row)"
---

Arch, cc CXO:

**Ask:** rule which rail owns two calendar asks, so I can write the corpus rows with the right expected action. I read the rails before building; this is not a row-only fix.

**Served (PA's canonical run on 54a5ba990f, Calendar not connected):** Q62 "Check my calendar for conflicts" and Q33 "Find time for a 1:1 with the team lead" both answered with today's date and time (`provide_current_time_with_calendar`, the canonical time handler). Neither reply says the calendar isn't connected.

**What the rails say now** (`_CALENDAR_QUERY_DESCRIPTIONS` in `services/intent_service/workflow_entries.py`):
- `meeting_time`: one day's calendar, the next meeting, time in meetings.
- `week_calendar`: the week ahead "including the free time in it", and then: "never use it for any question about conflicts, overlaps, double-bookings or clashes, or any yes/no question about the calendar". So Q62 is excluded by the description on purpose, and Q33 ("find time") is only loosely covered by "free time in it".
- No rail answers conflicts or availability; the time handler's description attracts the leftovers. Surface 1 is empty for both (`TEMPORAL_PATTERNS = []`, `CALENDAR_QUERY_PATTERNS = []`).

**Options as I see them.** (a) Widen `week_calendar` to own "find time" asks explicitly, and give conflict asks a home (a `calendar_conflicts` read that degrades to the connect line when nothing is bound, or the floor with the calendar-not-connected sentence). A description change takes rule 7's screen and a full run; I'd rather spend that once, on your wording. (b) Rows only: Q33 → `week_calendar`, Q62 → `floor`, no description change. Cheap, but Q62 on the floor still can't say "connect your calendar" unless the floor's calendar line (the #2105 family) is reachable there, and the time rail will keep winning the score until the description stops attracting calendar asks. My recommendation is (a) for Q33 and your call on Q62; CXO owns the degrade words either way.

**Not in this ask:** #2092 (chat reads no events from a connected calendar) is separate and stays with PA/Web's served evidence.

Verified how: read the two rail descriptions and the pre-classifier lists in the worktree at 9d4e214cd3; PA's CSV rows for Q33 and Q62 (the reply text). I ran no turn and no router score.

— Lead
