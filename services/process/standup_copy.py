"""Every user-facing line for leaving a standup, one named constant per line (#1771).

CXO owns these strings. They live in one leaf module (strings only, no imports)
so a one-word copy ruling is a one-line edit, and so the registry's #1529 exit
copy, the standup adapter, the standup conversation handler and the
intent-service resume seam all quote the same constant instead of a copy.

Three outcomes, one rule (CXO 2026-10-15): a deferral ("not now", "maybe
later") PAUSES and never destroys; only an explicit cancel, or a "no" to the
invitation, ENDS a standup.

ONE pause line (CXO 2026-10-15 08:35): an escape word ("stop") and a
deferral ("not now") leave the standup in the same state, so they share the
deferral line; two phrasings would teach the user two names for one state.
``STANDUP_ESCAPE_PAUSE_REPLY`` therefore IS ``STANDUP_DEFER_PAUSE_REPLY``.
The drop line stays separate.
"""

# PAUSE after a deferral ("not now", "maybe later" ... THE predicate's DEFER
# verdict): at the resume offer (CXO 2026-10-14 11:20) and mid-interview (CXO
# 2026-10-15 item 1). NOT at the "ready to start?" invitation: an unstarted
# standup is never paused, it ends with the invitation line (Arch 2026-10-15).
STANDUP_DEFER_PAUSE_REPLY = (
    "Okay, I'll leave your standup where it is. Just ask when you want to pick it back up."
)

# PAUSE after a #888 PAUSE escape word (``registry.ESCAPE_PAUSE_WORDS``: "stop",
# "never mind").
# Read by ``StandupProcessAdapter.pause_message``. CXO 2026-10-15 08:35: the
# same line as a deferral (was the 2026-10-14 21:50 "No problem — I've paused
# your standup…", retired that morning).
STANDUP_ESCAPE_PAUSE_REPLY = STANDUP_DEFER_PAUSE_REPLY

# DROP an ACTIVE standup on an explicit exit ("cancel that", "end standup",
# "forget it": the #1529 exit) or a #888 END escape word
# (``registry.ESCAPE_END_WORDS``: "cancel", "quit" ...), read by
# ``StandupProcessAdapter.drop_message``. CXO 2026-10-15 item 1.
STANDUP_DROP_REPLY = (
    "Okay, I've dropped your standup. Say 'do a standup' whenever you want a fresh one."
)

# DROP a SUSPENDED standup on an explicit cancel or a decline at the resume
# offer. CXO 2026-10-14 21:50 (landed with the second seam, bf03ac3ab2).
STANDUP_DROP_PAUSED_REPLY = (
    "Okay, I've dropped your paused standup. Say 'do a standup' whenever you want a fresh one."
)

# END at the invitation ("ready to start?"): every way of leaving there (a
# bare "no", a cancel, an escape word, a deferral). CXO 2026-10-15 item 2 (was
# "No problem! Just say 'standup' when you're ready."); Arch 2026-10-15 one
# state, one phrase.
STANDUP_INVITATION_DECLINE_REPLY = (
    "Okay, no standup for now. Say 'do a standup' whenever you want one."
)

# The resume seam found no paused standup to resume. A statement plus an
# instruction; nothing to arm. CXO 2026-10-15 item 3 (was "I couldn't find
# the paused standup. Want to start a fresh one with /standup?").
STANDUP_RESUME_NOT_FOUND_REPLY = (
    "I couldn't find your paused standup. Say 'do a standup' to start a new one."
)
