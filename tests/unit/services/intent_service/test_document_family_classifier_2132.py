"""#2132 — the legacy classifier's document family (Arch 10-23, one screened change).

When the router says CLARIFY or NONE, or answers below the live threshold, the
legacy classifier serves the turn. Two cells sent document asks nowhere:
- the classifier's own example mapped "analyze the file I uploaded" to
  analyze_data (repository metrics; PA traced served Q17 to it);
- "what_does"/"question_document" normalize to ``qa_document``, which had no
  rail key, so a question about one document fell to the category path.
Now both land on the analyze_document entry. Aliases are input-side only, so
the router's catalog text is unchanged (no router screen).
"""

from services.intent_service import prompts
from services.intent_service.inversion_router import derive_routing_grammar
from services.intent_service.workflow_dispatcher import get_action_workflows
from services.intent_service.workflow_entries import register_default_workflows


def _examples_text():
    return "\n".join(str(v) for k, v in vars(prompts).items() if k.isupper() and isinstance(v, str))


def test_qa_document_is_an_alias_of_the_analyze_document_entry():
    register_default_workflows()
    wf = get_action_workflows()
    assert wf["qa_document"] is wf["analyze_document"]


def test_the_alias_is_not_a_router_operation():
    names = {op.name for op in derive_routing_grammar().operations}
    assert "analyze_document" in names
    assert "qa_document" not in names


def test_the_classifier_examples_send_document_asks_to_the_document_op():
    text = _examples_text()
    assert (
        '"analyze the file I uploaded" → {{"category": "analysis", "action": "analyze_document"'
        in text
    )
    assert (
        '"what does this document say?" → {{"category": "analysis", "action": "analyze_document"'
        in text
    )
    for line in text.splitlines():
        if '"action": "analyze_data"' in line:
            assert "file" not in line.lower() and "document" not in line.lower(), line
