"""#2048 follow-up — an ADOPTED category runs READ operations only.

Arch's ruling (ADR-080 D4, "uncertainty never writes"; #2048 issue comment
6219111038, 2026-10-16): ``IntentService._adopt_canonical_portfolio_category``
gives a ``manage_portfolio`` / ``manage_repos`` turn the PORTFOLIO category
when the classifier paired the action with another one (QUERY, GUIDANCE, ...).
The classifier's category was then the only signal that the turn was a
question, and the adoption overrides it. So on an adopted turn the legacy
handler's write branches (add, archive, restore; link, unlink for repos) do
not execute:

- the classifier said "question" and the message reads as one ("how do I
  archive my project Foo?"): a statement naming the exact phrase to type,
  no action, no question (case 1);
- the message leads with the write verb ("archive Foo", mislabelled QUERY):
  a yes/no confirm armed on the #846 store with the #1190 confirm carrier,
  whose "yes" re-dispatches the matching rail op (``archive_project``,
  ``restore_project``, ``add_project``) with the original Intent (case 2).

Reads (list, list_archived, search, the help menu) run as before. When the
classifier itself says PORTFOLIO the adopted guard does not apply; since
#2057 that path hands its writes to the rail ops instead (below).

Copy: CXO's final ruling (2026-10-16), verbatim for the project ops; CXO's
09:1x refinements (the add confirm uses the add flow's wording, the named add
how-to echoes the name, the repo statements).

#2057 (Arch's ruling 2026-10-16, comment 6219485412) reuses this copy: the
classified legacy ``manage_portfolio`` / ``manage_repos`` write branches now
dispatch to their rail ops (``LEGACY_WRITE_RAIL_ACTIONS``), and a
question-framed turn on those rail ops gets :func:`question_how_to` (the same
statements) instead of a write or an armed check. One copy source for the
guard path and the #2057 paths.
"""

from __future__ import annotations

import dataclasses
import re
from typing import Any, Dict, Optional, Sequence

from services.domain.models import Intent

# Stamped on ``intent.context`` by _adopt_canonical_portfolio_category; the
# value is the classifier's own category (e.g. "query"). Present means the
# category was adopted, not classified.
ADOPTED_FROM_CONTEXT_KEY = "category_adopted_from"

# The sniffed portfolio write operations this guard holds, and their rail keys
# (#1595 Phase 3) — the landing a confirmed "yes" dispatches.
ADOPTED_WRITE_RAIL_ACTIONS = {
    "add": "add_project",
    "archive": "archive_project",
    "restore": "restore_project",
}

# The leading verbs that make a sniffed write an imperative (case 2). They
# mirror the handler's own sniff vocabulary (ARCHIVE_PATTERNS,
# RESTORE_PATTERNS, ADD_PROJECT_PATTERNS / the add word check); compared
# against the message's first token after the handler strips courtesy words
# and intent prefixes. An in-handler token check, not a routing pattern.
_IMPERATIVE_VERBS = {
    "add": frozenset({"add", "create", "start", "set", "new"}),
    "archive": frozenset({"archive", "hide", "put"}),
    "restore": frozenset({"restore", "unarchive", "bring"}),
}

# #2057: every sniffed legacy write operation and its rail op. A classified
# PORTFOLIO turn whose sniff lands here is dispatched to the rail op (so the
# #1509/#1510 consent gate decides), never written by the legacy branch.
LEGACY_WRITE_RAIL_ACTIONS = {
    **ADOPTED_WRITE_RAIL_ACTIONS,
    "link": "link_repo",
    "unlink": "unlink_repo",
}
_RAIL_ACTION_OPERATIONS = {rail: op for op, rail in LEGACY_WRITE_RAIL_ACTIONS.items()}

# The handler's own owner/name capture (_handle_repo_management), reused for
# the repo statements' echo. Copy choice only, never routing.
_REPO_RE = re.compile(r"([\w.-]+/[\w.-]+)")

# --- copy (CXO 2026-10-16, final; verbatim) ----------------------------
# Case 1: a statement. No action, no question. Per operation: the line when
# the user named the project, and the form without a name. ("I'll ask you to
# confirm before anything changes." was withdrawn as false: add/archive/
# restore are WRITE rail ops and an explicit imperative runs directly.)
# The no-name archive/restore forms follow CXO's "say 'archive project' and
# its name" example.
ADOPTED_WRITE_HOW_TO_LINES = {
    "archive": (
        "To archive a project, say 'archive project {name}'. "
        "You can restore it any time with 'restore project {name}'."
    ),
    "add": "To add a project called {name}, say 'add project {name}'.",
    "restore": "To restore an archived project, say 'restore project {name}'.",
}
ADOPTED_WRITE_HOW_TO_LINES_NO_NAME = {
    "archive": "To archive a project, say 'archive project' and its name.",
    "add": "To add a project, say 'add project' and a name.",
    "restore": "To restore an archived project, say 'restore project' and its name.",
}
# Case 2: the yes/no confirm, armed (see build_adopted_write_confirm_offer).
# Add uses the existing add flow's wording (CXO 09:1x).
ADOPTED_WRITE_CONFIRM_QUESTIONS = {
    "archive": 'Archive the project "{name}"? (yes/no)',
    "restore": 'Restore the project "{name}"? (yes/no)',
    "add": 'Add a project called "{name}"? (yes/no)',
}
# Case 2, "no".
ADOPTED_WRITE_DECLINE_LINE = 'Okay, I won\'t {verb} "{name}". Nothing has been changed.'

# Repo writes (manage_repos link/unlink): a statement only, nothing armed.
# CXO 2026-10-16 09:3x: the phrase matches the repo handler's link/unlink patterns
# ('link repo owner/name to <project>', 'unlink repo owner/name from <project>').
# (CXO 09:1x). The repo is echoed when the message named one.
ADOPTED_REPO_LINK_LINE = "To link a repo to a project, say 'link repo {repo} to <project name>'."
ADOPTED_REPO_UNLINK_LINE = (
    "To unlink a repo from a project, say 'unlink repo {repo} from <project name>'."
)
_NO_REPO = "owner/name"


# Words that make a captured "name" no name at all. The archive/restore
# capture takes whatever follows the verb, so "how do I archive a project?"
# yields "a" and "...one of my projects?" yields "one of my". Used only to
# choose the copy (named line vs. the form without a name), never to route.
_NOT_A_NAME_WORDS = frozenset(
    {"a", "an", "the", "my", "your", "one", "of", "some", "any", "this", "that", "it"}
    | {"archived", "project", "projects"}
)


def usable_name(name: Optional[str]) -> Optional[str]:
    """``name`` unless every word in it is a determiner or the noun itself."""
    if not name:
        return None
    words = [w.strip(".,!?'\"").lower() for w in name.split()]
    if all(w in _NOT_A_NAME_WORDS for w in words if w):
        return None
    return name


def adopted_from(intent: Intent) -> Optional[str]:
    """The classifier's category when the PORTFOLIO category was adopted."""
    return (intent.context or {}).get(ADOPTED_FROM_CONTEXT_KEY)


def is_imperative(operation: str, leading_tokens: Sequence[str]) -> bool:
    """Case 2 iff the request's first token (courtesy/prefix stripped by the
    caller) is the operation's own write verb."""
    verbs = _IMPERATIVE_VERBS.get(operation, frozenset())
    return bool(leading_tokens) and leading_tokens[0] in verbs


def adopted_write_how_to(operation: str, name: Optional[str]) -> str:
    if not name:
        return ADOPTED_WRITE_HOW_TO_LINES_NO_NAME[operation]
    return ADOPTED_WRITE_HOW_TO_LINES[operation].format(name=name)


def adopted_repo_how_to(operation: str, repo: Optional[str]) -> str:
    template = ADOPTED_REPO_LINK_LINE if operation == "link" else ADOPTED_REPO_UNLINK_LINE
    return template.format(repo=repo or _NO_REPO)


def display_name_for(
    operation: str, original_message: str, router_args: Optional[object] = None
) -> Optional[str]:
    """The project name the user typed, case kept, for the copy only: for
    add, the SAME resolver the add handler writes from
    (``resolve_add_project_slots``: the router's honesty-guarded ``name``
    first, the #1856 extractor as the fallback — #2069, Arch's condition);
    for archive/restore, the handler's own pattern family run on the
    original text. None when there is no usable name."""
    from services.onboarding.portfolio_service import (
        ARCHIVE_PATTERNS,
        RESTORE_PATTERNS,
        clean_project_name,
        resolve_add_project_slots,
    )

    if operation == "add":
        return usable_name(resolve_add_project_slots(original_message, router_args)["name"])
    patterns = {"archive": ARCHIVE_PATTERNS, "restore": RESTORE_PATTERNS}.get(operation, ())
    for pattern in patterns:
        match = re.search(pattern, original_message, re.IGNORECASE)
        if match and match.groups():
            return usable_name(clean_project_name(match.group(1).strip()))
    return None


def question_how_to(
    rail_action: Optional[str], original_message: str, router_args: Optional[object] = None
) -> Optional[str]:
    """#2057: the statement a question-framed turn gets for a portfolio rail
    write (``archive_project``, ``restore_project``, ``add_project``,
    ``link_repo``, ``unlink_repo``); None for any other action (the gate's
    generic check answers those). Arms nothing."""
    operation = _RAIL_ACTION_OPERATIONS.get(rail_action or "")
    if operation is None:
        return None
    if operation in ("link", "unlink"):
        match = _REPO_RE.search(original_message or "")
        return adopted_repo_how_to(operation, match.group(1) if match else None)
    return adopted_write_how_to(
        operation, display_name_for(operation, original_message or "", router_args)
    )


def build_adopted_write_confirm_offer(operation: str, name: str, intent: Intent) -> Dict[str, Any]:
    """The #846 record for case 2: the #1190 confirm carrier
    (``confirm_pending_action``), whose "yes" re-dispatches the rail op with
    a copy of the original Intent (action set to the rail key). Armed by
    ``IntentService._arm_write_offer`` from the result's ``"write_offer"``."""
    from services.intent_service.destructive_confirm import (
        CONFIRM_PENDING_ACTION_WORKFLOW,
        DESTRUCTIVE_CONFIRM_KIND,
    )

    rail_action = ADOPTED_WRITE_RAIL_ACTIONS[operation]
    question = ADOPTED_WRITE_CONFIRM_QUESTIONS[operation].format(name=name)
    held = dataclasses.replace(intent, action=rail_action, context=dict(intent.context or {}))
    return {
        "workflow_type": CONFIRM_PENDING_ACTION_WORKFLOW,
        "question": question,
        "pending_action": {
            "kind": DESTRUCTIVE_CONFIRM_KIND,
            "action": rail_action,
            "intent": held,
            "summary": f'{operation} the project "{name}"',
        },
        "decline_message": ADOPTED_WRITE_DECLINE_LINE.format(verb=operation, name=name),
    }


# #2057: the record key the canonical seam reads to re-dispatch a legacy
# write through its rail op.
RAIL_DISPATCH_KEY = "rail_dispatch"


def legacy_write_rail_dispatch(operation: str, original_message: str) -> Dict[str, Any]:
    """#2057: what a legacy ``manage_portfolio`` / ``manage_repos`` write
    branch returns instead of writing. ``rail_dispatch`` names the rail op;
    ``IntentService._process_intent_internal`` dispatches it through
    ``_dispatch_action_rail`` (consent gate, #1190 confirm). The message is
    the operation's how-to statement, so a caller that cannot dispatch the
    rail (the multi-intent orchestrator calls ``CanonicalHandlers.handle``
    directly) shows a line that writes nothing."""
    from services.shared_types import IntentCategory

    rail_action = LEGACY_WRITE_RAIL_ACTIONS[operation]
    return {
        "message": question_how_to(rail_action, original_message),
        "intent": {
            "category": IntentCategory.PORTFOLIO.value,
            "action": rail_action,
            "confidence": 1.0,
            "context": {"original_message": original_message, "legacy_operation": operation},
        },
        "requires_clarification": False,
        RAIL_DISPATCH_KEY: rail_action,
    }
