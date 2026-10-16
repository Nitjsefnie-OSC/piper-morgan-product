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
classifier itself says PORTFOLIO nothing here applies (that legacy path is on
the #1595 Phase 3 tail, Arch comment 6219115064).

Copy: CXO's ruling (memo 2026-10-16 08:47), verbatim for the project ops, except
case 1's second sentence, withdrawn as false and awaiting CXO's re-ruling.
The repo lines are not CXO-ruled yet (flagged in the #2048 report).
"""

from __future__ import annotations

import dataclasses
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

# Placeholder when the message carried no name.
_NO_NAME = "[project name]"

# --- copy (CXO 2026-10-16 08:47, verbatim) ------------------------------
# Case 1: a statement. No action, no question. CXO's second sentence ("I'll
# ask you to confirm before anything changes.") was withdrawn as false (Arch,
# 2026-10-16: add/archive/restore are WRITE rail ops; the #1190 confirm covers
# DESTRUCTIVE only and an explicit imperative runs directly), and is being
# re-ruled. When CXO rules it, set ADOPTED_WRITE_HOW_TO_TAIL (per verb if
# needed); nothing else changes.
ADOPTED_WRITE_HOW_TO_TAIL: Dict[str, str] = {}
ADOPTED_WRITE_HOW_TO_LINE = "To {verb} a project, say '{verb} project {name}'."
# Case 2: the yes/no confirm, armed (see build_adopted_write_confirm_offer).
ADOPTED_WRITE_CONFIRM_QUESTION = '{Verb} the project "{name}"? (yes/no)'
# Case 2, "no".
ADOPTED_WRITE_DECLINE_LINE = 'Okay, I won\'t {verb} "{name}". Nothing has been changed.'

# Repo writes (manage_repos link/unlink): a statement only. NOT CXO-ruled.
ADOPTED_REPO_LINK_LINE = "To link a repository, say 'link repo {repo} to project {name}'."
ADOPTED_REPO_UNLINK_LINE = "To unlink a repository, say 'unlink repo {repo} from project {name}'."


def adopted_from(intent: Intent) -> Optional[str]:
    """The classifier's category when the PORTFOLIO category was adopted."""
    return (intent.context or {}).get(ADOPTED_FROM_CONTEXT_KEY)


def is_imperative(operation: str, leading_tokens: Sequence[str]) -> bool:
    """Case 2 iff the request's first token (courtesy/prefix stripped by the
    caller) is the operation's own write verb."""
    verbs = _IMPERATIVE_VERBS.get(operation, frozenset())
    return bool(leading_tokens) and leading_tokens[0] in verbs


def adopted_write_how_to(operation: str, name: Optional[str]) -> str:
    line = ADOPTED_WRITE_HOW_TO_LINE.format(verb=operation, name=name or _NO_NAME)
    tail = ADOPTED_WRITE_HOW_TO_TAIL.get(operation)
    return f"{line} {tail}" if tail else line


def adopted_repo_how_to(operation: str, repo: Optional[str], project: Optional[str]) -> str:
    template = ADOPTED_REPO_LINK_LINE if operation == "link" else ADOPTED_REPO_UNLINK_LINE
    return template.format(repo=repo or "owner/name", name=project or _NO_NAME)


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
    question = ADOPTED_WRITE_CONFIRM_QUESTION.format(Verb=operation.capitalize(), name=name)
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
