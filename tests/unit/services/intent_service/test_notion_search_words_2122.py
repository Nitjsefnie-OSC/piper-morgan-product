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
