"""#2131 (Arch's ruling, 2026-10-22): every LLM call made for a user passes the acting
principal, because ``user_id`` picks the provider and the consent list (#1415, #946); with
None the client resolves the SERVER's provider and consent list, which is how an
OpenAI-only account got the missing-key refusal (#2127, PA's Q21).

A shrink-only ratchet in the #2101 shape: no ``.complete(`` call in ``services/`` with a
``task_type``/``prompt`` keyword may omit ``user_id``. A genuinely principal-free system
call passes ``user_id=None`` explicitly, so the choice is visible. The ceiling is 0.
"""

from __future__ import annotations

import ast
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

import pytest

REPO = Path(__file__).resolve().parents[2]
CEILING = 0  # lower-only; was 9 on 2026-10-22 before this change


def _calls_without_principal():
    out = []
    for f in sorted((REPO / "services").rglob("*.py")):
        tree = ast.parse(f.read_text())
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "complete"
            ):
                kws = {k.arg for k in node.keywords}
                if ("task_type" in kws or "prompt" in kws) and "user_id" not in kws:
                    out.append(f"{f.relative_to(REPO)}:{node.lineno}")
    return out


def _forwarders_with_a_default():
    """Arch 10-22 14:30: in any function whose LLM call passes ``user_id=<one of its own
    parameters>``, that parameter has no default; otherwise a caller one level up drops
    the principal silently (the slot-filling manager did, through extract_slots)."""
    out = []
    for f in sorted((REPO / "services").rglob("*.py")):
        tree = ast.parse(f.read_text())
        for fn in ast.walk(tree):
            if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            a = fn.args
            pos = a.posonlyargs + a.args
            has_default = dict(
                zip(
                    [p.arg for p in pos],
                    [False] * (len(pos) - len(a.defaults)) + [True] * len(a.defaults),
                )
            )
            has_default.update({p.arg: d is not None for p, d in zip(a.kwonlyargs, a.kw_defaults)})
            for node in ast.walk(fn):
                if (
                    isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Attribute)
                    and node.func.attr == "complete"
                ):
                    for kw in node.keywords:
                        if (
                            kw.arg == "user_id"
                            and isinstance(kw.value, ast.Name)
                            and has_default.get(kw.value.id)
                        ):
                            out.append(f"{f.relative_to(REPO)}:{fn.lineno} {fn.name}")
    return sorted(set(out))


FORWARDER_CEILING = 0  # lower-only; was 7 on 2026-10-22 before Arch's 14:30 ruling


def test_no_function_forwards_a_defaulted_principal_into_an_llm_call():
    found = _forwarders_with_a_default()
    assert len(found) <= FORWARDER_CEILING, (
        f"Functions forwarding a defaulted user_id into an LLM call (#2131): {found}. Make the "
        "parameter keyword-only with no default, so every caller states the principal "
        "(None for a system call)."
    )


def test_no_llm_call_omits_the_principal():
    missing = _calls_without_principal()
    assert len(missing) <= CEILING, (
        f"LLM calls without user_id (#2131): {missing}. Pass the acting principal; a "
        "system call with no user passes user_id=None explicitly."
    )


@pytest.mark.asyncio
async def test_the_slot_extractor_passes_the_principal():
    from services.slot_filling.slot_extractor import extract_slots
    from services.slot_filling.slot_template import COMMENT_ISSUE_TEMPLATE

    llm = MagicMock()
    llm.complete = AsyncMock(return_value='{"issue_number": "12", "comment": "hi"}')
    await extract_slots(
        message="comment on issue 12: hi",
        template=COMMENT_ISSUE_TEMPLATE,
        llm_service=llm,
        user_id="u-openai-only",
    )
    assert llm.complete.await_args.kwargs["user_id"] == "u-openai-only"


@pytest.mark.asyncio
async def test_the_boundary_rule_carries_the_principal_into_the_detector_context():
    from services.ethics.output_filter_rules import apply_boundary_rules

    enforcer = MagicMock()
    enforcer.enforce_boundaries = AsyncMock(return_value=MagicMock(is_violation=False))
    await apply_boundary_rules("some reply", enforcer, user_id="u-1")
    assert enforcer.enforce_boundaries.await_args.kwargs["context"]["user_id"] == "u-1"


@pytest.mark.asyncio
async def test_the_analyzer_summary_passes_the_principal():
    from services.analysis.document_analyzer import DocumentAnalyzer

    analyzer = DocumentAnalyzer.__new__(DocumentAnalyzer)
    analyzer.llm_client = MagicMock()
    analyzer.llm_client.complete = AsyncMock(return_value="Summary: x\\nKey points:\\n- a")
    for attr in ("llm", "_llm", "client"):
        setattr(analyzer, attr, analyzer.llm_client)
    try:
        await analyzer._summarize_text("some text", user_id="u-1")
    except Exception:
        pass  # parsing of the fake reply is not under test; the call's principal is
    assert analyzer.llm_client.complete.await_args.kwargs["user_id"] == "u-1"
