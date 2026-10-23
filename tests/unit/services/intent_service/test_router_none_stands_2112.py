"""#2112 (Arch's ruling, 2026-10-20): on a live category the router's NONE stands.

Served (alpha 54a5ba990f, PA's canonical run): "Check my calendar for conflicts"
and "Find time for a 1:1 with the team lead" answered with today's date. The
corpus rules both floor and the router matched them NONE at 0.85 to 0.95; the
consult fell through to the LLM classifier, which said TEMPORAL, and the time
handler answered. With read_temporal live the router owns TEMPORAL's rail
operation (get_current_time), so its NONE stands and the turn goes to the floor.
"""

from unittest.mock import MagicMock, patch

import pytest

from services.domain.models import Intent
from services.intent.intent_service import IntentService
from services.intent_service.inversion_live import (
    LiveRouteProvenance,
    publish_live_route_provenance,
    router_none_stands,
)
from services.shared_types import IntentCategory

CONFLICTS = "Check my calendar for conflicts"


@pytest.fixture
def intent_service():
    with patch("services.intent.intent_service.LearningHandler"):
        with patch("services.intent.intent_service.ConversationKnowledgeGraphIntegration"):
            return IntentService(intent_classifier=MagicMock())


@pytest.fixture(autouse=True)
def _clear_provenance():
    publish_live_route_provenance(None)
    yield
    publish_live_route_provenance(None)


def _none(confidence=0.95):
    publish_live_route_provenance(
        LiveRouteProvenance(routed_live=False, reason="router_none", confidence=confidence)
    )


def _temporal(message=CONFLICTS, action="get_current_time") -> Intent:
    return Intent(
        category=IntentCategory.TEMPORAL,
        action=action,
        original_message=message,
        context={"original_message": message},
    )


class TestTheRouterNoneStands:
    def test_a_router_none_turn_landing_on_live_temporal_reaches_the_floor(
        self, intent_service, monkeypatch
    ):
        monkeypatch.setenv("PIPER_INVERSION_LIVE_CATEGORIES", "read_status,read_temporal")
        _none(0.95)
        assert router_none_stands("TEMPORAL", "get_current_time") == "group"
        # The legacy keyword split would have kept this ask canonical (the date reply).
        assert intent_service._requires_canonical_handler(_temporal()) is True
        assert intent_service._should_route_to_floor(_temporal()) is True

    def test_a_free_form_legacy_action_is_judged_by_the_category_it_landed_on(self, monkeypatch):
        """The LLM classifier's action may not be a rail key; TEMPORAL's one
        registry operation is live, so the category is owned."""
        monkeypatch.setenv("PIPER_INVERSION_LIVE_CATEGORIES", "read_temporal")
        _none(0.9)
        assert (
            router_none_stands("TEMPORAL", "provide_current_time_with_calendar") == "category_ops"
        )


class TestTheGuardStaysOut:
    def test_a_router_routed_time_turn_still_reaches_the_time_handler(
        self, intent_service, monkeypatch
    ):
        monkeypatch.setenv("PIPER_INVERSION_LIVE_CATEGORIES", "read_temporal")
        publish_live_route_provenance(
            LiveRouteProvenance(
                routed_live=True, operation="get_current_time", live_match="group", confidence=0.9
            )
        )
        assert router_none_stands("TEMPORAL", "get_current_time") is None
        assert intent_service._should_route_to_floor(_temporal("what time is it")) is False

    def test_a_legacy_hit_on_a_non_live_category_is_unchanged(self, intent_service, monkeypatch):
        monkeypatch.setenv("PIPER_INVERSION_LIVE_CATEGORIES", "read_status")
        _none(0.95)
        assert router_none_stands("TEMPORAL", "get_current_time") is None
        assert intent_service._should_route_to_floor(_temporal()) is False

    @pytest.mark.parametrize("confidence", [0.5, None])
    def test_a_sub_threshold_or_unscored_none_does_not_stand(self, confidence, monkeypatch):
        monkeypatch.setenv("PIPER_INVERSION_LIVE_CATEGORIES", "read_temporal")
        _none(confidence)
        assert router_none_stands("TEMPORAL", "get_current_time") is None

    def test_no_consult_or_an_empty_live_set_means_no_guard(self, monkeypatch):
        monkeypatch.setenv("PIPER_INVERSION_LIVE_CATEGORIES", "read_temporal")
        assert router_none_stands("TEMPORAL", "get_current_time") is None  # never consulted
        _none(0.95)
        monkeypatch.setenv("PIPER_INVERSION_LIVE_CATEGORIES", "")
        assert router_none_stands("TEMPORAL", "get_current_time") is None

    def test_a_clarify_or_refused_decline_is_not_a_none(self, monkeypatch):
        monkeypatch.setenv("PIPER_INVERSION_LIVE_CATEGORIES", "read_temporal")
        for reason in ("router_clarify", "router_refused", "armed_pending_offer"):
            publish_live_route_provenance(
                LiveRouteProvenance(routed_live=False, reason=reason, confidence=0.95)
            )
            assert router_none_stands("TEMPORAL", "get_current_time") is None


ALPHA_LIVE = (
    "add_project,complete_todo,create_reminder,create_todo,delete_todo,read_canonical,"
    "read_floor,read_portfolio,read_referent,read_status,read_strategic,read_synthesis,"
    "read_temporal"
)


class TestARouterHiddenLandingStands:
    """#2132 option (b), served FAIL on a54540c0a8: "Compare launch-notes-tmp.txt with
    rollout-plan-tmp.txt" scored router NONE, the classifier said compare_documents,
    and this guard sent the turn to the floor, which denied the files existed. The
    router never sees a hidden entry, so its NONE is no judgment about it."""

    def test_a_router_hidden_landing_is_not_overridden_by_the_routers_none(self, monkeypatch):
        monkeypatch.setenv("PIPER_INVERSION_LIVE_CATEGORIES", ALPHA_LIVE)
        _none(0.95)
        assert router_none_stands("ANALYSIS", "compare_documents") is None

    def test_a_router_visible_analysis_landing_still_reaches_the_floor(self, monkeypatch):
        monkeypatch.setenv("PIPER_INVERSION_LIVE_CATEGORIES", ALPHA_LIVE)
        _none(0.95)
        assert router_none_stands("ANALYSIS", "analyze_document") is not None
