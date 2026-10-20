"""#2113: "Update issue #123" routed to the Notion document-update path.

Served (alpha 54a5ba990f, PA's canonical run, Q58): the classifier's verb shim
had one UPDATE cell, source-agnostic, pointing at update_document_query. An
issue-sourced update now maps to the rail-registered update_issue handler;
every other UPDATE source keeps the document path.
"""

from services.intent_service.action_registry import (
    Verb,
    get_disposition,
    verb_sourcetype_to_legacy_action,
)


def test_an_issue_sourced_update_maps_to_update_issue():
    assert verb_sourcetype_to_legacy_action(Verb.UPDATE, "github_issue") == "update_issue"


def test_other_update_sources_keep_the_document_path():
    for source in (None, "document", "text", "conversation", "commit_range"):
        assert verb_sourcetype_to_legacy_action(Verb.UPDATE, source) == "update_document_query"


def test_update_issue_is_a_registered_workflow_target():
    """The cell points at a handler the rail runs, not a free-form name."""
    assert get_disposition("QUERY", "update_issue").name == "WORKFLOW"
