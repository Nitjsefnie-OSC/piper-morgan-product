"""The ONE privacy knob for user text in server logs.

PM's ruling (2026-10-13, relayed by Comms from the privacy Section C review):
**"keep only fingerprints of logs."** Every server log line that used to carry
a user's message, query or cached text now carries its sha256 fingerprint by
default and the text only when an operator opts in.

The knob keeps its historical name, ``PIPER_INVERSION_LOG_UTTERANCE`` (the
three inversion telemetry surfaces read it since 2026-09), so an existing Fly
secret or shell export keeps working — but its DEFAULT flips from "1" to "0"
here, so a deployment that never set it logs fingerprints only. Set it to
"1" (or true/yes/on) in a dev shell to see text while debugging routing; the
corpus-material use the shadow observers were built for is a dev-shell use.

Readers (all go through this module — add new text-logging sites here, never
a fresh ``os.environ.get``):

- ``inversion_live._log_decision``, ``inversion_shadow``, ``preclaim_shadow``
  — the routing telemetry lines (``utterance`` / ``utterance_sha256``).
- ``PreClassifier.pre_classify`` — the "PRE_CLASSIFIER DEBUG" input lines.
- ``IntentService.process_intent`` — the "Processing intent" line.
- ``intent_service.cache`` — the HIT/MISS/SET/… lines (used to log a 50-char
  prefix of the text).
- ``document_handlers.search_documents`` and the Notion search error lines —
  the user's search query.

What this does NOT cover (by design): stored conversation turns in the
database are a separate surface (the user's own history, not logs); system
copy such as progress states and HTTP error summaries carries no user text.
"""

from __future__ import annotations

import hashlib
import os
from typing import Any, Dict

KNOB = "PIPER_INVERSION_LOG_UTTERANCE"
_TRUTHY = {"1", "true", "yes", "on"}
DEFAULT = "0"  # PM 2026-10-13: fingerprints only unless an operator opts in


def log_full_utterance() -> bool:
    """True only when an operator set the knob on. Default off."""
    return os.environ.get(KNOB, DEFAULT).strip().lower() in _TRUTHY


def utterance_sha256(text: str) -> str:
    """The fingerprint: sha256 of the UTF-8 text (the same digest the
    inversion telemetry has always logged beside the text)."""
    return hashlib.sha256((text or "").encode()).hexdigest()


def utterance_fields(text: str, key: str = "utterance") -> Dict[str, Any]:
    """Log fields for one piece of user text: ``{key}_sha256`` always, and
    ``{key}`` (the text itself) only when the knob is on. Spread into a
    structlog call: ``logger.info("…", **utterance_fields(message))``."""
    fields: Dict[str, Any] = {f"{key}_sha256": utterance_sha256(text)}
    if log_full_utterance():
        fields[key] = text
    return fields


def utterance_preview(text: str, limit: int = 50) -> str:
    """One-string form for a ``*_preview`` log field or an f-string log line:
    the first ``limit`` characters only when the knob is on, otherwise
    ``sha256=<digest>``. Replaces every raw ``message[:50]`` in log calls."""
    if log_full_utterance():
        return (text or "")[:limit]
    return f"sha256={utterance_sha256(text)}"
