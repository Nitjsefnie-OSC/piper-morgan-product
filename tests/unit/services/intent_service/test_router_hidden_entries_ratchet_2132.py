"""#2132 option (b), Arch condition 3: router-hidden rail entries are a ratchet, ceiling 1.

A ``router_visible=False`` entry is reachable only through the legacy classifier.
That is a bounded exception with a named exit (#2149, catalog size), never a
second routing surface. The ceiling only goes DOWN (when #2149 lets compare onto
the router); raising it needs Arch's ruling.
"""

from services.intent_service.workflow_dispatcher import get_action_workflows
from services.intent_service.workflow_entries import register_default_workflows

ROUTER_HIDDEN_CEILING = 1
EXPECTED_ROUTER_HIDDEN = {"compare_documents"}


def test_router_hidden_entries_are_ratcheted():
    register_default_workflows()
    entries = {id(e): (k, e) for k, e in get_action_workflows().items()}
    hidden = {k for k, e in entries.values() if not e.router_visible}
    assert len(hidden) <= ROUTER_HIDDEN_CEILING, sorted(hidden)
    assert hidden == EXPECTED_ROUTER_HIDDEN


def test_the_classifier_example_teaches_compare_documents():
    from services.intent_service.prompts import INTENT_CLASSIFICATION_PROMPT

    assert (
        '"compare these two documents" → {{"category": "analysis", "action": "compare_documents"'
        in INTENT_CLASSIFICATION_PROMPT
    )
