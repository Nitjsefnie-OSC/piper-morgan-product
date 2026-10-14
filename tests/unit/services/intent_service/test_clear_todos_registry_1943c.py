"""#1943 rework (c) (Arch 2026-10-14 13:3x): ``clear_todos`` enters ACTION_REGISTRY
so the LEGACY LLM classifier can emit it (its emission vocabulary is registry
canonicals, #1283). Before this, a clear-shaped turn that reached the legacy
chain (a popped #846 offer, a bound contextual offer, the armed snapshot, a
split turn, a router error) dead-ended at delete_todo with "couldn't find …
'clear'" once the #1605 regex net retired. The LLM decides meaning (D1); no
regex.

The op was already in the router's grammar via the rail entry; the one catalog
change is the ACTION_EXAMPLES row (the registry invariant: every entry has an
example), which the grammar attaches to the rail op, so it owed rule 7's x6
screen and full corpus run (Lead 2026-10-14, controls in dev/2026/10/14/).
No LLM, no DB.
"""

from __future__ import annotations

from services.intent_service.action_registry import (
    ACTION_DESCRIPTIONS,
    ACTION_EXAMPLES,
    ACTION_REGISTRY,
    ActionDisposition,
    Verb,
    get_verb,
    validate_verb_coverage,
    verb_sourcetype_to_legacy_action,
)
from services.intent_service.inversion_router import derive_routing_grammar


def test_registry_carries_clear_todos_as_a_workflow_canonical():
    assert ACTION_REGISTRY[("EXECUTION", "clear_todos")] is ActionDisposition.WORKFLOW
    assert ("EXECUTION", "clear_todos") in ACTION_DESCRIPTIONS


def test_verb_clear_exists_and_covers_the_action():
    assert Verb.CLEAR.value == "clear"
    assert get_verb("clear_todos") is Verb.CLEAR
    assert validate_verb_coverage() == []


def test_shim_canonicalizes_todo_domain_clears_only():
    for src in ("reminder", "todo", "task"):
        assert verb_sourcetype_to_legacy_action(Verb.CLEAR, src) == "clear_todos", src
    # the DELETE precedent: no (CLEAR, None) cell — a clear aimed elsewhere
    # keeps its free-form action and the honest-decline default
    assert verb_sourcetype_to_legacy_action(Verb.CLEAR, "calendar") is None
    assert verb_sourcetype_to_legacy_action(Verb.CLEAR, None) is None


def test_example_row_present_and_the_op_appears_once_in_the_grammar():
    """The registry invariant (every entry has an example) wins; the example
    reaches the router's catalog on the rail op, so it was screened x6 and
    full-corpus-run under rule 7 before landing (Lead 2026-10-14). The op
    itself was already in the grammar via the rail entry: still exactly one
    clear_todos op, with the rail's description."""
    assert ACTION_EXAMPLES[("EXECUTION", "clear_todos")] == "Clear my reminders"
    g = derive_routing_grammar()
    ops = [
        op
        for op in (getattr(g, "operations", None) or getattr(g, "ops"))
        if op.name == "clear_todos"
    ]
    assert (
        len(ops) == 1
    ), "clear_todos appears exactly once (rail canonical; the registry row is covered)"
    assert getattr(ops[0], "example", None) == "Clear my reminders"
    assert "mark done or delete" in (ops[0].description or "")


def test_legacy_prompt_vocabulary_can_name_the_verb():
    assert "clear" in [v.value for v in Verb]
