"""
Consciousness Wrapper for Error Messages

Enhances error messages with consciousness expression patterns.
Part of Consciousness Rollout Wave 1 (#631)

Issue: #631 CONSCIOUSNESS-TRANSFORM: Error Messages
Framework: #407 MUX-VISION-STANDUP-EXTRACT
ADR: ADR-056 Consciousness Expression Patterns

#2011 (2026-10-14): format_error_conscious and its private helpers
(_add_humility, _add_dialogue_invitation, _fix_mvc_gaps) were deleted — no
consumer outside this package; their unarmed "Would you like me to try
again?" never reached a user.
"""

from enum import Enum
from typing import Dict, Optional


class ErrorSeverity(str, Enum):
    """Error severity levels for appropriate user messaging."""

    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


def format_conversational_error_conscious(
    message: str,
    recovery: str,
    severity: str,
    context: Optional[str] = None,
) -> str:
    """
    Format error for chat/conversational interface with consciousness.

    More concise than full error format, suitable for chat bubbles.

    Args:
        message: The error message
        recovery: Recovery suggestion
        severity: Error severity level
        context: Optional context

    Returns:
        Conversational conscious error message
    """
    # Severity-appropriate opening
    if severity == ErrorSeverity.INFO.value or severity == ErrorSeverity.INFO:
        opening = "Heads up:"
    elif severity == ErrorSeverity.WARNING.value or severity == ErrorSeverity.WARNING:
        opening = "I noticed something:"
    elif severity == ErrorSeverity.CRITICAL.value or severity == ErrorSeverity.CRITICAL:
        opening = "I need to let you know:"
    else:
        opening = "I ran into something:"

    # Context integration
    if context:
        opening = f"{opening} while {context.lower()},"

    # Build message
    explanation = message.lower() if not message[0].isupper() else message
    recovery_short = _shorten_recovery(recovery)

    # Closing by severity (#2011, CXO 2026-10-14): ERROR/CRITICAL end on the
    # recovery itself — it already says what to do, and the old "Want me to
    # try again, or should we try something different?" offered an action
    # nothing performs. INFO/WARNING keep a statement, not an offer.
    if severity in (
        ErrorSeverity.ERROR.value,
        ErrorSeverity.ERROR,
        ErrorSeverity.CRITICAL.value,
        ErrorSeverity.CRITICAL,
    ):
        invitation = ""
    else:
        invitation = " Let me know if you need anything else."

    return f"{opening} {explanation} {recovery_short}{invitation}"


def enhance_error_pattern(
    pattern_response: Dict[str, str],
    context: Optional[str] = None,
) -> Dict[str, str]:
    """
    Enhance an existing error pattern response with consciousness.

    Takes the existing error pattern dict and adds consciousness elements.

    Args:
        pattern_response: Dict with 'message', 'recovery', 'severity', 'category'
        context: Optional context

    Returns:
        Enhanced pattern response dict
    """
    enhanced = pattern_response.copy()

    # Ensure message has identity voice
    message = enhanced.get("message", "")
    if not _has_identity(message):
        if message.startswith("I ") or message.startswith("I'"):
            pass  # Already has identity
        elif message.lower().startswith("the "):
            message = "I'm seeing that t" + message[2:]
        else:
            message = "I " + message[0].lower() + message[1:]
        enhanced["message"] = message

    # Ensure recovery has dialogue invitation
    recovery = enhanced.get("recovery", "")
    if not _has_invitation(recovery):
        recovery = recovery.rstrip(".")
        recovery += ". Let me know if that helps or if you'd like to try something else."
        enhanced["recovery"] = recovery

    return enhanced


def _shorten_recovery(recovery: str) -> str:
    """Shorten recovery suggestion for conversational format."""
    # Take first sentence only
    sentences = recovery.split(". ")
    if len(sentences) > 1:
        return sentences[0] + "."
    return recovery


def _has_identity(text: str) -> bool:
    """Check if text has identity voice (I statements)."""
    return "I " in text or "I'" in text or text.startswith("I")


def _has_invitation(text: str) -> bool:
    """Check if text has dialogue invitation."""
    invitation_patterns = ["?", "let me know", "would you", "should I", "want me"]
    text_lower = text.lower()
    return any(pattern in text_lower for pattern in invitation_patterns)
