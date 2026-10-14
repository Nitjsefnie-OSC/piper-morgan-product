"""#1605 — reminder/todo "clear"-family verb disambiguation (three-variant copy).

⚠️ RETIRED 2026-10-14 (Arch's clear_todos ruling 2026-10-07, point 1, restated
2026-10-14 point 5; named on the guard comment and the epic-0 entry): the
regex-triggered three-variant flow this docstring describes below —
``detect_clear_family_ask`` and its ``maybe_handle_clear_family`` seam at the
complete_todo / delete_todo rail entries and the #1333 unmapped branch, the
``is_clear_family_passthrough`` predicate both consent tiers called, the
off-rail verb-answer path (``_handle_verb_answer_turn``, which completed /
armed deletes OUTSIDE the action-dispatch rail), the variant-2 correction
window and the #1906 pick-target carrier (armed only by that seam), and the
``clear_family_resolved`` stand-down marker (whose only reader was that
seam) — is DELETED. The family's turns enter through the ``clear_todos``
RESOLVER rail entry (services/intent_service/clear_todos.py): the router
decides family membership and WHICH items, the resolver owns set-then-verb,
and every execution re-enters the rail via ``dispatch_workflow``. What stays
here: the verb-question carrier (kind, offer builder, bare-"yes" re-ask
workflow) the resolver arms, the ratified variant-1 sentence (the
standing invitation ``CORRECTION_WINDOW_ASK`` was dropped by CXO 2026-10-14
with the correction window it belonged to), the per-verb inference key, the
fallback answer patterns, the #1696 explicit bulk-delete seam and its
#1190-confirmed batch delete, and the pick binders #1987 shares. The text
below is the design history of the retired flow.

PM ruling (decisions.log 2026-08-13 ~14:1x, relayed by Lead): when a verb has
no confident mapping onto the baked-in operations, Piper ASKS — never a
term-of-art decree ("'clear' shall mean delete"). CXO+PPM joint design
(FINAL copy memo 2026-08-13 22:17, PPM sign-off 22:22): three variants —

1. **First encounter** (no stored default): ask which the user means, store
   the answer via the #1510 rail (store-on-verify, distinct provenance key).
2. **Stored default = complete (WRITE)**: auto-apply + disclosure-after; no
   block; correctable on the immediately-following turn ("I meant delete").
3. **Stored default = delete (DESTRUCTIVE)**: the stored preference changes
   the MAPPING, never the consent tier — the batch delete routes through the
   REAL #1190 confirm gate (DESTRUCTIVE -> CONFIRM in every consent-matrix
   cell, consent_gate.decide_consent; PPM verified the cells personally).

WHERE IT FIRES (routing moratorium honored — no pre-classifier or prompt
changes): detection is handler-internal, inside the EXECUTION surfaces that
already claim these turns — `_handle_execution_intent`'s complete_todo /
delete_todo branches (the classifier's guess for a clear-family utterance)
and its #1333 unmapped else-branch (the classifier emitted e.g.
"clear_reminders", which no surface maps — previously a false capability
denial, the exact #1605 transcript bug). The mechanism consumed is
`consent_gate.decide_verb_interpretation` (effect-weighted per #1557: a
WRITE candidate under a "stop asking me" meta-preference may auto-apply;
a DESTRUCTIVE candidate asks regardless — process steering never lowers a
destructive ask).

SCOPE (deliberate): set-complement asks ("clear these except X") are
#1563's dangling-offer lane, NOT this build — an exception clause falls
back to a variant-1-style clarification of the whole ask rather than
guessing the set (joint-design ruling; PM's original transcript phrasing
is the pinned case).

⚠️ COPY SEAM: the three variant strings below are RATIFIED verbatim (CXO
FINAL copy, PPM signed off) — a drifted word is a bug; tests pin them
exactly. The surrounding glue copy (empty-state, batch summaries, the
correction/meta re-asks) is Lead-drafted mechanism copy at this seam; CXO
owns the voice — adjust wording here (one place), not at call sites.

Vocabulary (#1569): the copy's noun tracks the user's own noun in the
triggering turn ("reminder" vs "todo" — the per-item rule's utterance-level
form); the ratified strings are the reminder-noun forms.

CORRECTION WINDOW (the "cheapest honest version", documented per the joint
design): after a variant-2 auto-apply, "I meant delete" works on the
IMMEDIATELY-FOLLOWING turn — it rides the #846 pending-offer store (one-turn
carrier, popped before classification), so the window is one turn, not the
whole session. The correction confirms via the #1190 gate before deleting
(the items are batch-completed by then; deleting removes them entirely) and
does NOT flip the stored default — the ratified copy says "this time".

#1906 (2026-09-30, PM live on the test card): the named-target UNMATCHED
branch (``named_target_unmatched``, below) was the one branch in this file
that answered "Tell me which one you mean" WITHOUT arming an offer — every
other branch in this module calls ``set_pending_offer`` (the #846 one-slot
store). The user's pick ("Clear the first one.") had nothing to bind to, so
it re-entered classification as a fresh turn; on alpha that turn fell to the
floor, which improvised an unarmed yes/no ask outside the #1855 opener
family, and "Yes" found no pending offer to execute. THE FIX: the unmatched
branch now arms ``CLEAR_PICK_TARGET_WORKFLOW`` (kind
``CLEAR_PICK_TARGET_KIND``) with the rendered candidate list bound at offer
time; the answer binds deterministically (ordinal, name/substring, or an
unambiguous status word) and re-enters the SAME post-resolution flow a
single matched name would have taken (``_act_on_resolved_targets``) —
never a fresh classification. See ``_handle_pick_target_turn``.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple
from uuid import UUID

import structlog

logger = structlog.get_logger(__name__)

# ── Carrier kinds (the #1190 pending_action carrier is action-agnostic;
#    ``kind`` is how the offer seam recognizes ours without a parallel store)
CLEAR_VERB_QUESTION_KIND = "reminder_clear_verb_question"
CLEAR_DELETE_CONFIRMATION_KIND = "reminder_clear_delete_confirmation"

# ── Registered workflow types (all action_triggered=False — offer-seam only)
CLARIFY_CLEAR_VERB_WORKFLOW = "clarify_reminder_clear_verb"
CLEAR_DELETE_WORKFLOW = "clear_reminders_delete"

# Effect-weighted gate input: a clear-family verb is a plausible-but-
# unverified mapping — between the suggestion floor (0.4) and the auto-apply
# bar (0.9). Same fixed value as the #1411 unmapped-status-value precedent.
VERB_CONFIDENCE = 0.7

VALUE_COMPLETE = "complete"
VALUE_DELETE = "delete"


def inference_key(verb: str) -> str:
    """Distinct provenance key in the #1510 verified-inference store, per
    verb — PM rejected decrees partly because every synonym would demand its
    own mapping forever; asked-once-remembered is per-verb by construction
    ("handle" gets its own first encounter; a stored "clear" never speaks
    for it). #1603: keys and values are str at the JSONB boundary."""
    return f"reminder_clear_verb:{verb}"


# ---------------------------------------------------------------------------
# RATIFIED COPY (CXO FINAL 2026-08-13 22:17; PPM sign-off 22:22) — verbatim
# for verb='clear', noun='reminder'; parametrized so sibling verbs and the
# noun form "todo" reuse the same shape (#1569 vocabulary rule).
# ---------------------------------------------------------------------------


def variant_one_question(verb: str = "clear", noun: str = "reminder") -> str:
    """Variant 1 — first encounter, no stored default."""
    return (
        f"Before I touch these — when you say '{verb}' on a {noun}, "
        f"do you want me to mark it done, or delete it? "
        f"I'll remember for next time."
    )


# ---------------------------------------------------------------------------
# #1696 explicit-bulk-delete shape detection (the clear-family ASK detector,
# detect_clear_family_ask, retired 2026-10-14 — see the module docstring)
# ---------------------------------------------------------------------------

# Exception clauses — set-complement scope, #1563's lane, never guessed here.
_EXCEPTION_RE = re.compile(
    r"\bexcept\b|\bbut\s+not\b|\bother\s+than\b|\bapart\s+from\b"
    r"|\baside\s+from\b|\bexcluding\b",
    re.IGNORECASE,
)

# #1696: PLURAL domain nouns — the bulk-shape signal for an EXPLICIT delete.
# Deliberately plural-only: 'delete my reminder' (singular, unnamed) keeps
# the which-one clarification; 'delete my reminders' is a bulk ask. These
# are shape-detection constants (the #1605 handler-internal detection
# precedent), not argument extraction — no prose is captured from them.
_BULK_REMINDER_PLURAL_RE = re.compile(r"\breminders\b", re.IGNORECASE)
_BULK_TODO_PLURAL_RE = re.compile(r"\b(?:to-?dos|tasks)\b", re.IGNORECASE)


def detect_explicit_bulk_delete_ask(message: Optional[str]) -> Optional[str]:
    """#1696 — detect an EXPLICIT bulk delete over the reminder/todo domain.

    The inverse face of the (retired 2026-10-14) ``detect_clear_family_ask``:
    that seam deliberately declined explicit imperatives (the verb is not
    ambiguous), which left 'delete my reminders' with LESS capability than
    the ambiguous 'clear my reminders' (the 1527 lane's filed finding: the
    single-item which-todo ask answered a bulk ask). This detector claims
    the PLURAL/bulk shape only: a plural domain noun, no exception clause.
    Number-free-ness and named-target-emptiness are the CALLER's checks
    (``maybe_handle_explicit_bulk_delete``) — they need todo_handlers /
    destructive_confirm machinery this module keeps lazy.

    No verb check, deliberately: this runs only inside the delete_todo rail
    entry point, so the classifier's delete_todo emission IS the verb
    evidence — remove / erase / 'get rid of' phrasings ride the same seam
    without this module growing a verb vocabulary.

    Returns the copy noun ("reminder" | "todo", #1569 — reminder wins a
    mixed mention, the #1569 render-rule tiebreak), or None.
    """
    text = (message or "").strip()
    if not text:
        return None
    if _EXCEPTION_RE.search(text):
        return None  # #1563's set-complement lane — never guess the set
    if _BULK_REMINDER_PLURAL_RE.search(text):
        return "reminder"
    if _BULK_TODO_PLURAL_RE.search(text):
        return "todo"
    return None


# ---------------------------------------------------------------------------
# Target resolution + batch operations
# ---------------------------------------------------------------------------


def _plural(noun: str, n: int) -> str:
    return noun if n == 1 else f"{noun}s"


async def _resolve_targets(todo_service, user_uuid: UUID, noun: str) -> List[Any]:
    """The whole ask's target set (scope narrowing is #1563's lane):
    noun 'reminder' -> active todos carrying a reminder_date (the
    `context:reminders` family's own membership rule); noun 'todo' -> all
    active todos. Owner-scoped via user_id (#1493/#1532)."""
    todos = await todo_service.list_todos(user_id=user_uuid, include_completed=False)
    if noun == "reminder":
        return [
            t for t in todos if getattr(t, "reminder_date", None) is not None and not t.completed
        ]
    return [t for t in todos if not t.completed]


def _due_iso(todo: Any, noun: str) -> Optional[str]:
    """#1906 — the candidate's relevant due-ish timestamp, ISO-8601 (or
    None), bound into a pick-target offer at ARM time so "the overdue one"
    can be judged on the ANSWER turn without a fresh DB read (deterministic,
    offline — the #846 carrier idiom). 'reminder' -> reminder_date (the
    same field ``_resolve_targets`` scopes the reminder noun on); 'todo' ->
    due_date (the ``find_overdue_todos`` definition, #1651)."""
    from services.utils.datetime_utils import ensure_utc

    field = "reminder_date" if noun == "reminder" else "due_date"
    dt = ensure_utc(getattr(todo, field, None))
    return dt.isoformat() if dt is not None else None


def _empty_targets_message(verb: str, noun: str) -> str:
    # Pattern-073 discipline: describe what was actually queried.
    scope = "saved reminders" if noun == "reminder" else "active todos"
    return (
        f"I checked your {scope} and there are none to {verb} right now. "
        f"Nothing has been changed."
    )


# ---------------------------------------------------------------------------
# Offer builders (all ride the EXISTING #846 store / #1190 carrier shape)
# ---------------------------------------------------------------------------


def _delete_confirmation_offer(
    principal: Optional[str],
    verb: str,
    noun: str,
    ids: List[str],
    texts: List[str],
    original_message: str,
    kind: str = CLEAR_DELETE_CONFIRMATION_KIND,
    question: Optional[str] = None,
) -> Dict[str, Any]:
    """A #1190 pending_action offer whose "yes" dispatches the batch delete
    through CONFIRM_PENDING_ACTION_WORKFLOW -> CLEAR_DELETE_WORKFLOW. The
    target ids are resolved at OFFER time so the question's N is exactly
    what a "yes" deletes — no drift between the ask and the act.

    ``question`` (#1665): the ALREADY-RENDERED confirm ask the caller returns
    this turn (since 2026-10-14 only #1696's plain bulk-delete confirm) —
    stored verbatim, never re-rendered."""
    from services.domain.models import Intent
    from services.intent_service.destructive_confirm import (
        CONFIRM_PENDING_ACTION_WORKFLOW,
    )
    from services.shared_types import IntentCategory

    n = len(ids)
    delete_intent = Intent(
        category=IntentCategory.EXECUTION,
        action=CLEAR_DELETE_WORKFLOW,
        original_message=original_message,
        confidence=1.0,
        context={
            "original_message": original_message,
            "user_id": principal,
            "clear_target_ids": list(ids),
            "clear_target_texts": list(texts),
            "clear_noun": noun,
            "clear_verb": verb,
        },
    )
    summary = f"delete {n} {_plural(noun, n)}"
    return {
        "workflow_type": CONFIRM_PENDING_ACTION_WORKFLOW,
        "question": question,
        "pending_action": {
            "kind": kind,
            "action": CLEAR_DELETE_WORKFLOW,
            "intent": delete_intent,
            "summary": summary,
            "user_id": principal,
        },
        "decline_message": (
            f"Okay — I won't delete anything. Your {_plural(noun, 2)} are untouched."
        ),
    }


def _verb_question_offer(
    principal: Optional[str],
    verb: str,
    noun: str,
    ids: List[str],
    texts: List[str],
    original_message: str,
    question: Optional[str] = None,
) -> Dict[str, Any]:
    """The variant-1 pending offer. Its answer is either/or ("mark it done" /
    "delete it"), handled kind-specifically at the offer seam BEFORE generic
    accept/decline (the verify_inference precedent). A bare affirmative falls
    to the generic accept path, which dispatches CLARIFY_CLEAR_VERB_WORKFLOW —
    an entry that re-asks and re-arms this same offer.

    ``question`` (#1665): the ALREADY-RENDERED either/or ask the caller
    returns this turn (the clear_todos resolver's variant-1-with-set ask —
    its only arm site since 2026-10-14) — stored verbatim, never re-rendered. NOT a yes/no: the verb question is pinned
    OUTSIDE the #1664 confirm-kind set."""
    return {
        "workflow_type": CLARIFY_CLEAR_VERB_WORKFLOW,
        "question": question,
        "pending_action": {
            "kind": CLEAR_VERB_QUESTION_KIND,
            "action": CLARIFY_CLEAR_VERB_WORKFLOW,
            "user_id": principal,
            "inference_key": inference_key(verb),
            "clear_verb": verb,
            "clear_noun": noun,
            "clear_target_ids": list(ids),
            "clear_target_texts": list(texts),
            "original_message": original_message,
            "summary": f"{verb} {len(ids)} {_plural(noun, len(ids))}",
        },
        "decline_message": (
            f"Okay — I haven't touched your {_plural(noun, 2)}. " f"Nothing has been changed."
        ),
    }


# ---------------------------------------------------------------------------
# The main flow — called from _handle_execution_intent's claiming branches
# ---------------------------------------------------------------------------


async def maybe_handle_explicit_bulk_delete(
    intent_service,
    intent,
    session_id: Optional[str],
    user_id: Optional[str],
    todo_user_id: UUID,
):
    """#1696 — the EXPLICIT bulk delete seam ('delete my reminders').

    Runs inside ``run_delete_todo_workflow`` (the #1605 clear-family seam
    that used to run first retired 2026-10-14 — ambiguous clear shapes now
    route to the ``clear_todos`` resolver, never here). Claims a turn
    only when ALL of: bulk plural shape (``detect_explicit_bulk_delete_ask``),
    a session to bind the confirm to, NO todo number, and NO named target —
    i.e. exactly the turns whose only prior answer was the single-item
    which-todo ask. Everything else returns None -> the caller proceeds to
    ``handle_delete_todo`` unchanged (numbered, named, and singular asks).

    The consent path is the clear-family flow's ALREADY-#1190-GATED delete
    leg: targets resolved at OFFER time (``_resolve_targets`` — the noun
    scopes the set, #1569), ids+texts bound into the pending action, and the
    crisp "yes" dispatches ``CLEAR_DELETE_WORKFLOW`` (action_triggered=False,
    offer-seam only). Nothing is deleted on the ask turn. Unlike variant 3,
    the question is the plain confirm — the user SAID delete, so no
    stored-preference framing, and nothing is read from or written to the
    #1510 verb store.
    """
    from services.intent.intent_service import IntentProcessingResult

    # Lazy import (same circularity note as the kind constants above).
    from services.intent_service.destructive_confirm import _named_delete_target

    original_message = intent.original_message or (intent.context or {}).get("original_message", "")
    noun = detect_explicit_bulk_delete_ask(original_message)
    if noun is None:
        return None
    if not session_id:
        # No session to bind the confirm answer to — never arm an offer
        # nothing can pop. Fall through to the caller's normal handling.
        return None
    if intent_service.todo_handlers._extract_todo_id(original_message):
        return None  # numbered ask — the #1190 gate's positional leg owns it
    if _named_delete_target(original_message):
        return None  # named ask — the #1527 named-target leg owns it

    principal = str(user_id) if user_id else str(todo_user_id)
    base_intent_data = {
        "category": intent.category.value if intent.category else "execution",
        "action": intent.action,
        "confidence": intent.confidence,
        "clear_noun": noun,
    }

    todo_service = intent_service.todo_handlers.todo_service
    try:
        targets = await _resolve_targets(todo_service, todo_user_id, noun)
    except Exception as e:  # silent-ok: logged at error w/ exc_info; a source failure must read as trouble-loading (#1425), never a guessed set or an ungated delete
        logger.error(
            "bulk_delete_target_resolution_failed",
            error=str(e),
            user_id=principal,
            exc_info=True,
        )
        scope = "reminders" if noun == "reminder" else "todos"
        return IntentProcessingResult(
            success=True,
            message=(
                f"I had trouble loading your {scope} just now, so I haven't "
                f"touched anything. You can try again in a moment."
            ),
            intent_data=base_intent_data,
        )

    if not targets:
        return IntentProcessingResult(
            success=True,
            message=_empty_targets_message("delete", noun),
            intent_data=base_intent_data,
        )

    ids = [str(t.id) for t in targets]
    texts = [t.text for t in targets]
    n = len(ids)
    # Plain explicit confirm — variant 3's target grammar without its
    # stored-preference clause (mechanism copy at the CXO-owned seam).
    target = f"these {n} {noun}s" if n != 1 else f"this {noun}"
    question = f"Delete {target}? (yes/no)"
    intent_service.workflow_offer_service.set_pending_offer(
        session_id,
        _delete_confirmation_offer(
            principal,
            "delete",
            noun,
            ids,
            texts,
            original_message,
            question=question,  # #1665: rendered once, stored + said
        ),
        user_id=user_id,
    )
    logger.info(
        "explicit_bulk_delete_confirmation_offered",
        noun=noun,
        count=n,
        session_id=session_id,
    )
    return IntentProcessingResult(
        success=True,
        message=question,
        intent_data={
            **base_intent_data,
            "action": CLEAR_DELETE_WORKFLOW,
            "explicit_bulk_delete": True,
            "destructive_confirmation_pending": True,
        },
        requires_clarification=True,
    )


# ---------------------------------------------------------------------------
# Offer-seam turn handling (kind-specific, BEFORE generic accept/decline —
# the verified_inference.handle_verification_turn_meta precedent). The three
# answer patterns below are the clear_todos resolver's SHARED-FALLBACK parse
# (clear_todos.handle_clear_todos_verb_answer) — their only reader since the
# 2026-10-14 retirement.
# ---------------------------------------------------------------------------

_COMPLETE_ANSWER_RE = re.compile(
    r"\bdone\b|\bcomplete(?:d)?\b|\bfinish(?:ed)?\b|\bcheck(?:ed)?\s+(?:them|these|it)?\s*off\b",
    re.IGNORECASE,
)
_NEGATED_DELETE_RE = re.compile(
    r"\b(?:don'?t|do\s+not|never)\b[^.!?]{0,20}\bdelete\b", re.IGNORECASE
)

# #1650: a delete CLAIM must be a crisp phrase — the delete verb anchored at
# the head of a short, single-line turn, after at most a lead-in ("no,",
# "wait,", "actually", "I meant…"). The old unanchored \bdelete\b claimed
# ASIDES that merely mention deleting: PM's live "please note that I'll need
# to figure out later why you thought I wanted you to delete a project."
# (one line, ~95 chars — under the #1631 floor) reads as "I meant delete" to
# a substring match, and the claim arms a live delete confirm. A false claim
# here is one crisp "yes" from data loss, so the pattern is deliberately
# narrow; a missed phrase just falls to off-intent / an honest re-ask, where
# the user can re-ask in full words.
#
# #1653: the SAME pattern (reused, not duplicated — no new extraction regex
# per the TestExtractionPatternRatchet discipline) is also the verb-answer
# turn's delete claim (now the clear_todos resolver's fallback parse, whose
# delete answer re-enters the rail as delete_todo — DESTRUCTIVE, #1190-
# confirmed), so the claim takes this crisp bar too. The unanchored
# _DELETE_ANSWER_RE it replaces was the #1650 residue the issue filed: with
# the verb QUESTION armed, the same PM aside read as "the verb means delete"
# and stored a wrong, STICKY verb default.
_CORRECTION_CLAIM_RE = re.compile(
    r"^(?:(?:no|yes|yeah|yep|wait|hold\s+on|actually|oops|oh|sorry|hmm)[,!\s]+)*"
    r"(?:i\s+(?:actually\s+)?(?:meant|want(?:ed)?\s+(?:you\s+to\s+)?)\s*)?"
    r"(?:please\s+)?(?:delete|remove|get\s+rid\s+of)\b",
    re.IGNORECASE,
)


def _principal_mismatch(payload: Dict[str, Any], user_id: Optional[str]) -> bool:
    """#1532: the store and the todos are the USER's. If the turn's principal
    differs from the one the offer was built for (auth changed between
    turns), nothing may act or store."""
    offer_user = payload.get("user_id")
    principal = str(user_id) if user_id else None
    return bool(offer_user and principal and offer_user != principal)


async def handle_reminder_clear_turn(
    pending_offer: Dict[str, Any],
    message: str,
    session_id: Optional[str],
    user_id: Optional[str],
    intent_service,
) -> Optional[Dict[str, Any]]:
    """Kind-specific handling for a popped reminder-clear offer. Returns the
    acceptance-seam dict shape ({"message", "intent_data"[, "requires_clarification"]})
    when this turn was claimed; None falls through to generic accept /
    decline / off-intent handling (bare "yes" -> the registered workflow's
    re-ask; "no"/bare exit -> the offer's honest decline copy; anything
    else -> abandoned via the pop).

    Since the 2026-10-14 retirement (Arch's clear_todos ruling, point 1 —
    module docstring), the ONLY reminder-clear kind left with an answer
    turn is the verb question, and its only arm site is the ``clear_todos``
    resolver; the answer goes straight to that resolver's handler, which
    re-enters the rail via ``dispatch_workflow`` (never acts off-rail)."""
    payload = pending_offer.get("pending_action") or {}
    if payload.get("kind") != CLEAR_VERB_QUESTION_KIND:
        return None
    from services.intent_service.clear_todos import handle_clear_todos_verb_answer

    # #1665/#1653: the arm-site's rendered ask rides the offer record —
    # threaded so the contract consult states what it knows (Arch's
    # input-adequacy condition), even when that is None.
    return await handle_clear_todos_verb_answer(
        payload,
        message,
        session_id,
        user_id,
        intent_service,
        armed_question=pending_offer.get("question"),
    )


# ---------------------------------------------------------------------------
# Pick-target binders — written for #1906's reminder-clear pick carrier
# (retired 2026-10-14 with the clear-family regex seam); still shared by
# #1987's delete_todo pick (delete_todo_pick.py) and todo_handlers.
# ---------------------------------------------------------------------------

_ORDINAL_WORDS: Dict[str, int] = {
    "first": 0,
    "second": 1,
    "third": 2,
    "fourth": 3,
    "fifth": 4,
    "sixth": 5,
    "seventh": 6,
    "eighth": 7,
    "ninth": 8,
    "tenth": 9,
}
_ORDINAL_WORD_RE = re.compile(r"\b(" + "|".join(_ORDINAL_WORDS) + r"|last)\b", re.IGNORECASE)
# Bare/hash-prefixed numeric position ("1", "#2", "2nd") — a position
# reference, never argument-extraction prose (#1595's ratchet): this is the
# SAME shape-detection precedent as the module's own named-target regexes,
# just over digits instead of quoted text.
_NUMERIC_ORDINAL_RE = re.compile(r"#\s*(\d+)\b|\b(\d+)(?:st|nd|rd|th)?\b")
_OVERDUE_WORD_RE = re.compile(r"\boverdue\b", re.IGNORECASE)
_WORD_RE = re.compile(r"[a-z0-9']+")
# #2003 — a quoted name is the user's exact reference: it binds only by
# literal containment (either direction) and is NEVER fuzzy-matched; a
# name that matches nothing stays unmatched. Shape detection (quotes),
# not argument extraction.
_QUOTED_NAME_RE = re.compile(r"[\"\u201c\u201d']([^\"\u201c\u201d']{2,})[\"\u201c\u201d']")
_NUMBER_WORDS = frozenset(
    {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"}
)
# Words that frame a pick answer ("delete the plants reminder") and must
# not count against the candidate in the #2003 coverage rule; they are
# dropped from the MESSAGE side only, never from the candidate titles.
_PICK_FRAME_WORDS = frozenset(
    {
        "reminder",
        "reminders",
        "todo",
        "todos",
        "task",
        "tasks",
        "item",
        "items",
        "remove",
        "removing",
        "deleting",
        "clearing",
        "want",
        "wanna",
        "just",
        "actually",
        "get",
        "rid",
        "drop",
        "kill",
        "called",
        "named",
        "about",
        "with",
    }
)


def _quoted_name(text: str) -> Optional[str]:
    """The first quoted segment of an answer turn, or None."""
    m = _QUOTED_NAME_RE.search(text or "")
    return m.group(1).strip() if m else None


_PICK_STOPWORDS = frozenset(
    {
        "the",
        "a",
        "an",
        "to",
        "for",
        "my",
        "on",
        "it",
        "and",
        "one",
        "that",
        "this",
        "clear",
        "delete",
        "please",
        "of",
        "in",
        "at",
        "do",
        "mean",
        "you",
    }
)


def _ordinal_index(text: str, n: int) -> Optional[int]:
    """'the first one' / 'second' / '#2' / '1' / 'last' -> a 0-based index,
    or None when the text names no IN-RANGE position (an out-of-range
    number, e.g. an issue number in an unrelated command, is deliberately
    NOT an ordinal reference here — it falls through to the other binding
    forms and then the command-release check)."""
    m = _ORDINAL_WORD_RE.search(text)
    if m:
        word = m.group(1).lower()
        if word == "last":
            return n - 1 if n else None
        idx = _ORDINAL_WORDS.get(word)
        return idx if idx is not None and idx < n else None
    m = _NUMERIC_ORDINAL_RE.search(text)
    if m:
        raw = m.group(1) or m.group(2)
        try:
            pos = int(raw)
        except (TypeError, ValueError):
            return None
        idx = pos - 1
        return idx if 0 <= idx < n else None
    return None


def _overdue_status(text: str, due_iso: List[Optional[str]]) -> Tuple[str, Optional[int]]:
    """'the overdue one' -> ('bound', idx) when EXACTLY ONE candidate's
    bound timestamp is in the past, ('ambiguous', None) when more than one
    is, or ('none', None) when the word isn't present, no candidate carries
    a timestamp, or none/multiple qualify — the status form simply doesn't
    resolve this turn (never guessed)."""
    if not _OVERDUE_WORD_RE.search(text):
        return "none", None
    now = datetime.now(timezone.utc)
    overdue: List[int] = []
    for i, iso in enumerate(due_iso):
        if not iso:
            continue
        try:
            dt = datetime.fromisoformat(iso)
        except ValueError:
            continue
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        if dt < now:
            overdue.append(i)
    if len(overdue) == 1:
        return "bound", overdue[0]
    if len(overdue) > 1:
        return "ambiguous", None
    return "none", None


def _name_index(text: str, texts: List[str]) -> Tuple[str, Optional[int]]:
    """Name/substring match against the rendered candidate texts ('review
    the pr' -> the literal match; 'the test card one' -> the candidate
    whose words COVER every significant word the user typed). Returns
    ('bound', idx), ('ambiguous', None) on a tie, or ('none', None).

    #2003 (served on alpha b713b91cb5): 'delete the reminder "web check
    alpha one"' — a title that no longer existed — used to bind to "web
    check alpha two" on word overlap. Two rules close that: a QUOTED name
    binds only by literal containment and is never fuzzy-matched; an
    unquoted reference binds only when ONE candidate contains every
    significant word of it (number words count when any candidate title
    uses them, so "…alpha one" cannot cover "…alpha two")."""
    lower = (text or "").lower()
    quoted = _quoted_name(text)
    if quoted:
        q = quoted.lower()
        hits = [
            i
            for i, t in enumerate(texts)
            if (t or "").strip() and ((t or "").lower() in q or q in (t or "").lower())
        ]
        if len(hits) == 1:
            return "bound", hits[0]
        if len(hits) > 1:
            return "ambiguous", None
        return "none", None

    exact_hits = [
        i for i, t in enumerate(texts) if (t or "").strip() and (t or "").lower() in lower
    ]
    if len(exact_hits) == 1:
        return "bound", exact_hits[0]
    if len(exact_hits) > 1:
        return "ambiguous", None

    def _significant(words: List[str], drop_frame: bool) -> set:
        out = set()
        for w in words:
            if len(w) < 3 or w in _PICK_STOPWORDS:
                continue
            if drop_frame and w in _PICK_FRAME_WORDS:
                continue
            out.add(w)
        return out

    raw_message_words = _WORD_RE.findall(lower)
    message_words = _significant(raw_message_words, drop_frame=True)
    if not message_words:
        return "none", None
    covering = [
        i
        for i, t in enumerate(texts)
        if message_words <= _significant(_WORD_RE.findall((t or "").lower()), drop_frame=False)
    ]
    if len(covering) > 1:
        return "ambiguous", None
    if not covering:
        return "none", None
    # Sibling guard: "web check alpha one" covers "web check alpha two" once
    # the number words are set aside ("one" is also the pronoun in "the
    # plants one"). When BOTH sides carry a number word and they share
    # none, the user named a sibling that is not in the list — no guess.
    msg_nums = {w for w in raw_message_words if w in _NUMBER_WORDS}
    cand_nums = {
        w for w in _WORD_RE.findall((texts[covering[0]] or "").lower()) if w in _NUMBER_WORDS
    }
    if msg_nums and cand_nums and not (msg_nums & cand_nums):
        return "none", None
    return "bound", covering[0]


def _resolve_pick_target(
    text: str, texts: List[str], due_iso: List[Optional[str]]
) -> Tuple[str, Optional[int]]:
    """Bind an answer turn to exactly one candidate. Tries, in order: an
    ordinal/positional reference (unambiguous by construction, so it wins
    outright), an unambiguous status word ("the overdue one"), then a
    name/substring match. The FIRST form that produces a verdict (bound or
    ambiguous) decides — never silently overridden by a weaker, later
    form. Returns ('bound', idx) | ('ambiguous', None) | ('none', None)."""
    idx = _ordinal_index(text, len(texts))
    if idx is not None:
        return "bound", idx
    status, idx = _overdue_status(text, due_iso)
    if status != "none":
        return status, idx
    return _name_index(text, texts)


def _rearm_verb_question(
    intent_service, session_id, user_id, payload, question: Optional[str] = None
) -> None:
    """Re-arm the variant-1 offer with its original payload (the pop already
    consumed it; a re-ask turn must re-store it or the next answer has
    nothing to bind to). ``question`` (#1665): the re-ask copy this turn
    renders — stored verbatim so the record's open question tracks what was
    actually said."""
    intent_service.workflow_offer_service.set_pending_offer(
        session_id,
        {
            "workflow_type": CLARIFY_CLEAR_VERB_WORKFLOW,
            "question": question,
            "pending_action": dict(payload),
            "decline_message": (
                f"Okay — I haven't touched your "
                f"{_plural(payload.get('clear_noun') or 'reminder', 2)}. "
                f"Nothing has been changed."
            ),
        },
        user_id=user_id,
    )


# ---------------------------------------------------------------------------
# Workflow entry points (registered action_triggered=False in
# workflow_entries.register_default_workflows — offer-seam reachable only)
# ---------------------------------------------------------------------------


async def run_clarify_reminder_clear_verb_workflow(
    session_id: str,
    user_id: Optional[str] = None,
    context: Optional[Dict[str, Any]] = None,
) -> Any:
    """Generic-accept landing for the variant-1 offer: a bare "yes" doesn't
    answer an either/or question — re-ask and re-arm the offer. effect: READ
    (nothing written; the real writes happen on an ANSWERED turn)."""
    ctx = context or {}
    payload = ctx.get("pending_action") or {}
    intent_service = ctx.get("intent_service")
    if payload.get("kind") != CLEAR_VERB_QUESTION_KIND or intent_service is None:
        logger.error(
            "clarify_reminder_clear_missing_or_foreign_payload",
            kind=payload.get("kind"),
            has_intent_service=intent_service is not None,
        )
        return None
    noun = payload.get("clear_noun") or "reminder"
    # #1665: the re-armed record's open question is this turn's re-ask copy.
    question = (
        f"Just so I get it right — for these {_plural(noun, 2)}: "
        f"mark them done, or delete them?"
    )
    _rearm_verb_question(intent_service, session_id, user_id, payload, question=question)
    return {
        "message": question,
        "intent_data": {
            "category": "execution",
            "action": CLARIFY_CLEAR_VERB_WORKFLOW,
            "verb_disambiguation_pending": True,
        },
    }


async def run_clear_reminders_delete_workflow(
    session_id: str,
    user_id: Optional[str] = None,
    context: Optional[Dict[str, Any]] = None,
) -> Any:
    """The CONFIRMED batch delete — dispatched ONLY through the #1190
    confirm path (run_confirm_pending_action_workflow re-dispatches the
    stored action on an explicit "yes"; action_triggered=False keeps the
    classifier/rail structurally away). effect: DESTRUCTIVE — deletes the
    todo rows resolved at offer time, by id, owner-scoped (#1532)."""
    ctx = context or {}
    intent = ctx.get("intent")
    intent_service = ctx.get("intent_service")
    if intent is None or intent_service is None:
        logger.error(
            "clear_reminders_delete_missing_context",
            has_intent=intent is not None,
            has_intent_service=intent_service is not None,
        )
        return None
    ictx = intent.context or {}
    ids = ictx.get("clear_target_ids") or []
    texts = ictx.get("clear_target_texts") or []
    noun = ictx.get("clear_noun") or "reminder"

    offer_user = ictx.get("user_id")
    principal = str(user_id) if user_id else offer_user
    if offer_user and principal and offer_user != principal:
        logger.warning(
            "clear_reminders_delete_principal_mismatch",
            offer_user=offer_user,
            turn_user=principal,
        )
        return {
            "message": "Let's hold off on that — nothing has been deleted.",
            "intent_data": {
                "category": "execution",
                "action": CLEAR_DELETE_WORKFLOW,
                "principal_mismatch": True,
            },
        }
    try:
        user_uuid = UUID(str(principal))
    except (ValueError, TypeError):
        return {
            "message": ("I need you to be logged in to delete todos. " "Nothing has been deleted."),
            "intent_data": {
                "category": "execution",
                "action": CLEAR_DELETE_WORKFLOW,
                "error_type": "AuthenticationRequired",
            },
        }

    todo_service = intent_service.todo_handlers.todo_service
    deleted: List[str] = []
    failed = 0
    for tid, text in zip(ids, texts):
        try:
            ok = await todo_service.delete_todo(todo_id=UUID(tid), user_id=user_uuid)
            if ok:
                deleted.append(text)
            else:
                failed += 1
        except Exception as e:  # silent-ok: counted + logged; the summary states the honest denominator (m-44), never a fabricated all-deleted
            failed += 1
            logger.warning("reminder_clear_delete_failed", todo_id=tid, error=str(e))

    logger.info(
        "reminder_clear_batch_deleted",
        deleted=len(deleted),
        failed=failed,
        session_id=session_id,
    )
    n = len(deleted)
    lines = [f"Deleted {n} {_plural(noun, n)}:"]
    lines.extend(f"• {text}" for text in deleted)
    if failed:
        lines.append(
            f"({failed} couldn't be deleted just now — it may already be gone. "
            f"Say 'show my todos' to check.)"
        )
    return {
        "message": "\n".join(lines),
        "intent_data": {
            "category": "execution",
            "action": CLEAR_DELETE_WORKFLOW,
            "deleted_count": n,
            "failed_count": failed,
        },
    }
