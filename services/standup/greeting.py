"""#2079: the standup's greeting follows the user's clock, not the server's.

Served 2026-10-17 16:29 PT: "give me a standup" opened "**Good morning!**"
while the page header above it read "Good afternoon". Both standup strings
were literals. CXO's words (18:48): the greeting follows the user's local
time; when the zone is unknown, a neutral "Hi". The day-part comes from the
home page's helper (``conversation_consciousness._current_time_of_day``),
which already refuses to present the server's UTC day-part as the user's
(#1381 family), and the zone from the one #1887 resolver every reminder
turn uses (``user_timezone.get_user_timezone``). Every failure degrades to
the neutral greeting; a greeting must never cost a standup turn.
"""

from typing import Optional

import structlog

from services.consciousness.conversation_consciousness import _current_time_of_day
from services.utils.user_timezone import get_user_timezone

logger = structlog.get_logger(__name__)

NEUTRAL_GREETING = "Hi!"

_GREETINGS = {
    "morning": "Good morning!",
    "late_morning": "Good morning!",
    "afternoon": "Good afternoon!",
    "evening": "Good evening!",
}


def standup_greeting(user_timezone: Optional[str]) -> str:
    """The greeting for the user's current day-part, or ``NEUTRAL_GREETING``
    when the zone is unknown or invalid (no day-part claim without a zone)."""
    return _GREETINGS.get(_current_time_of_day(user_timezone), NEUTRAL_GREETING)


async def standup_greeting_for(user_id) -> str:
    """``standup_greeting`` for the zone resolved for ``user_id`` (chosen zone,
    else the zone observed at login, else none)."""
    try:
        user_timezone = await get_user_timezone(user_id)
    except Exception as e:  # silent-ok: #2079 — a greeting never costs the standup turn; the resolver already fails safe, this is the belt; logged WARNING
        logger.warning("standup_greeting_timezone_failed", user_id=str(user_id), error=str(e))
        user_timezone = None
    return standup_greeting(user_timezone)
