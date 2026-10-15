"""Every user-facing line for leaving a standup, one named constant per line (#1771).

CXO owns these strings. They live in one leaf module (strings only, no imports)
so a one-word copy ruling is a one-line edit, and so the registry's #1529 exit
copy, the standup adapter, the standup conversation handler and the
intent-service resume seam all quote the same constant instead of a copy.

Three outcomes, one rule (CXO 2026-10-15): a deferral ("not now", "maybe
later") PAUSES and never destroys; only an explicit cancel, or a "no" to the
invitation, ENDS a standup.

OPEN COPY POINT (CXO's call, not resolved here): two pause lines exist.
``STANDUP_ESCAPE_PAUSE_REPLY`` is CXO's 2026-10-14 21:50 line for an escape
word ("stop"); ``STANDUP_DEFER_PAUSE_REPLY`` is the deferral line (CXO
2026-10-14 11:20, and the 2026-10-15 memo calls it "the same one used
everywhere for a paused standup"). If CXO rules they are one line, point the
escape constant at the defer constant.
"""

# PAUSE after an escape word ("stop", "cancel", "never mind" ... the #888 set).
# CXO 2026-10-14 21:50. Read by ``StandupProcessAdapter.pause_message``.
STANDUP_ESCAPE_PAUSE_REPLY = (
    "No problem — I've paused your standup. Just ask when you want to pick it back up."
)

# PAUSE after a deferral ("not now", "maybe later" ... THE predicate's DEFER
# verdict): at the resume offer (CXO 2026-10-14 11:20), mid-interview and at
# the "ready to start?" invitation (CXO 2026-10-15 items 1 and 2).
STANDUP_DEFER_PAUSE_REPLY = (
    "Okay, I'll leave your standup where it is. Just ask when you want to pick it back up."
)

# DROP an ACTIVE standup on an explicit exit ("cancel that", "end standup",
# "forget it": the #1529 exit). CXO 2026-10-15 item 1.
STANDUP_DROP_REPLY = (
    "Okay, I've dropped your standup. Say 'do a standup' whenever you want a fresh one."
)

# DROP a SUSPENDED standup on an explicit cancel or a decline at the resume
# offer. CXO 2026-10-14 21:50 (landed with the second seam, bf03ac3ab2).
STANDUP_DROP_PAUSED_REPLY = (
    "Okay, I've dropped your paused standup. Say 'do a standup' whenever you want a fresh one."
)

# END at the invitation ("ready to start?") on a bare "no" or a cancel.
# CXO 2026-10-15 item 2 (was "No problem! Just say 'standup' when you're ready.").
STANDUP_INVITATION_DECLINE_REPLY = (
    "Okay, no standup for now. Say 'do a standup' whenever you want one."
)

# The resume seam found no paused standup to resume. A statement plus an
# instruction; nothing to arm. CXO 2026-10-15 item 3 (was "I couldn't find
# the paused standup. Want to start a fresh one with /standup?").
STANDUP_RESUME_NOT_FOUND_REPLY = (
    "I couldn't find your paused standup. Say 'do a standup' to start a new one."
)
