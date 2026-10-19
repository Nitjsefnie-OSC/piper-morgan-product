"""#2098 — "change the title to X" on a pending draft retitles it; the body stays.

Web, #1386 scenario B3 on alpha e801b1a309 (2 of 2 runs): "Actually, change the title to
'Implement full-text search across nav and global search bar'" came back "Added to the draft"
with the old title and the instruction pasted into the body. CXO: Class 4; acceptance: the
correction changes the title, the body is unchanged, the reply shows the new title, "file it as
is" files the new title.

LAYER: the detector directly; the turn handler through its function with the offer store
replaced by a recording stub. DENOMINATOR: six marker phrasings, quoted and bare values,
the question guard, and the three handler outcomes (retitle, body unchanged, store failure).
"""

from unittest.mock import MagicMock

import pytest

from services.intent_service import drafted_issue as di

NEW = "Implement full-text search across nav and global search bar"


class TestDetector:
    @pytest.mark.parametrize(
        "message",
        [
            f"Actually, change the title to '{NEW}'",
            f'Change the title to "{NEW}"',
            f"set the title to {NEW}",
            f"rename it to '{NEW}'",
            f"The title should be “{NEW}”",
            f"call it {NEW}.",
        ],
    )
    def test_markers_yield_the_new_title(self, message):
        assert di.extract_title_change(message) == NEW

    def test_a_question_is_not_a_title_change(self):
        assert di.extract_title_change("Should we change the title to something shorter?") is None

    def test_body_prose_is_not_a_title_change(self):
        assert (
            di.extract_title_change("Users have asked for search in the nav bar for months.")
            is None
        )

    def test_empty_value_is_none(self):
        assert di.extract_title_change("change the title to") is None


def _offer(title="Add search functionality to navigation bar", body="Users want it."):
    return {
        "kind": "drafted_issue",
        "question": di._POST_BIND_ASK,
        "pending_action": {"action": "create_issue", "draft": {"title": title, "body": body}},
    }


def _service(fail=False):
    svc = MagicMock()
    if fail:
        svc.workflow_offer_service.set_pending_offer.side_effect = RuntimeError("store down")
    return svc


class TestHandler:
    @pytest.mark.asyncio
    async def test_the_correction_changes_the_title_and_keeps_the_body(self):
        offer = _offer()
        svc = _service()
        out = await di.handle_drafted_issue_turn(
            offer,
            f"Actually, change the title to '{NEW}'",
            session_id="s-2098",
            user_id="u",
            intent_service=svc,
        )
        assert out is not None
        assert out["message"].startswith(
            "Updated the title. Nothing is filed yet. Here's the draft:"
        )
        assert f"**Title**: {NEW}" in out["message"]
        assert "**Body**:\nUsers want it." in out["message"]
        assert "Actually, change the title" not in out["message"]
        draft = offer["pending_action"]["draft"]
        assert draft["title"] == NEW and draft["body"] == "Users want it."
        svc.workflow_offer_service.set_pending_offer.assert_called_once()
        assert out["intent_data"]["drafted_issue_retitled"] is True

    @pytest.mark.asyncio
    async def test_body_prose_still_binds_as_body(self):
        offer = _offer(body="")
        svc = _service()
        out = await di.handle_drafted_issue_turn(
            offer,
            "Users have asked for search in the nav bar for months, mostly on mobile.",
            session_id="s-2098b",
            user_id="u",
            intent_service=svc,
        )
        assert out is not None and "Added to the draft" in out["message"]
        assert (
            offer["pending_action"]["draft"]["title"]
            == "Add search functionality to navigation bar"
        )

    @pytest.mark.asyncio
    async def test_store_failure_is_said_not_hidden(self):
        offer = _offer()
        out = await di.handle_drafted_issue_turn(
            offer,
            f"change the title to '{NEW}'",
            session_id="s-2098c",
            user_id="u",
            intent_service=_service(fail=True),
        )
        assert out is not None
        assert "couldn't keep the draft bound" in out["message"]
        assert "nothing was filed" in out["message"]


class TestUntitledDraftKeepsTheAnswerPath:
    @pytest.mark.asyncio
    async def test_untitled_draft_title_answer_is_not_a_retitle(self):
        # #1649's state: body given, title missing, re-ask open. "the title should be X"
        # is an ANSWER there, handled by the existing path ("that's the title").
        offer = _offer(title="", body="sessions expire after 5 min")
        svc = _service()
        out = await di.handle_drafted_issue_turn(
            offer,
            "The title should be 'Login timeout'",
            session_id="s-2098d",
            user_id="u",
            intent_service=svc,
        )
        assert out is not None
        assert "that's the title" in out["message"].lower()
        assert offer["pending_action"]["draft"]["title"] == "Login timeout"
