"""#2122 (CXO's class call and words, 2026-10-20): the chat document-search reply.

Served (d1c64a92e3, an Anthropic-only account): "Search my documents for the
launch checklist" answered the Notion line with "(or set NOTION_API_KEY locally)"
and a promise to search the whole workspace. CXO's words replace it; the
developer clause is gone from every partner-facing Notion line.
"""

import inspect

from services.intent import intent_service as svc

CXO_LINE = (
    "I can't search your documents from chat yet, and I can't read your Notion pages "
    "in chat yet. If you paste the text here, I can work with it."
)


def test_the_search_handler_serves_cxo_line():
    src = inspect.getsource(svc.IntentService._handle_search_documents_notion)
    assert "I can't search your documents from chat yet, and I can't read your " in src
    assert "entire Notion workspace" not in src


def test_no_partner_facing_line_names_the_env_var():
    assert "NOTION_API_KEY locally" not in inspect.getsource(svc)


def test_the_analyze_and_update_handlers_serve_cxo_lines():
    """CXO 18:17: #2100's rule covers all three strings; no 'once connected' promise."""
    analyze = inspect.getsource(svc.IntentService._handle_analyze_document_notion)
    update = inspect.getsource(svc.IntentService._handle_update_document_notion)
    # #2138 (CXO and Arch, 2026-10-22): the analyze handler reads held files first,
    # so its Notion-unavailable branch never claims "can't analyze" and names no Notion.
    assert "I can't analyze your documents from chat yet" not in analyze
    assert "I don't see that document among your uploads. " in analyze
    assert "I can't update documents from chat yet. Tell me what you want changed" in update
    for src in (analyze, update):
        assert "Once connected" not in src
        assert "NOTION_API_KEY" not in src
