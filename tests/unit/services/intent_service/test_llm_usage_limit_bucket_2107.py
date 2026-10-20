"""#2107 — the workspace usage limit is its own bucket with an honest sentence.

Alpha, 2026-10-20 11:08 PT: Anthropic rejected the platform key with "You have reached your
specified workspace API usage limits. You will regain access on 2026-11-01 at 00:00 UTC",
and every keyless turn answered "usually a brief outage — try again in a moment". A dated
cap is not a brief outage, and the one thing the user can do (their own key) was hidden in
a conditional. The #1824 rule: a bucket earns its own name when the honest sentence differs.

LAYER: the shared text classifier, the translator's pattern table, the floor's copy map.
DENOMINATOR: the API's own wording with and without a date; the quota bucket untouched.
"""

from __future__ import annotations

from services.intent_service import conversational_floor as floor
from services.ui_messages.user_friendly_errors import (
    UserFriendlyErrorService,
    classify_llm_error_text,
    usage_limit_reset_date,
    usage_limit_sentence,
)

API_TEXT = (
    "All configured LLM providers failed. Details: anthropic: Error code: 400 - "
    "{'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'You have "
    "reached your specified workspace API usage limits. You will regain access on "
    "2026-11-01 at 00:00 UTC.'}}"
)
API_TEXT_NO_DATE = "anthropic: You have reached your specified workspace API usage limits."


class TestClassifier:
    def test_usage_limit_is_its_own_bucket_not_quota_and_not_transient(self):
        assert classify_llm_error_text(API_TEXT) == "usage_limit"
        assert classify_llm_error_text(API_TEXT_NO_DATE) == "usage_limit"

    def test_quota_wording_still_reads_quota(self):
        assert (
            classify_llm_error_text("insufficient_quota: billing hard limit") == "quota_exhausted"
        )

    def test_reset_date_is_read_from_the_providers_text(self):
        assert usage_limit_reset_date(API_TEXT) == "2026-11-01"
        assert usage_limit_reset_date(API_TEXT_NO_DATE) is None


class TestTranslatorCopy:
    def test_cxos_dated_sentence(self):
        """CXO's words (issue 2107, 2026-10-20 12:32), the provider's date read as month and day."""
        out = UserFriendlyErrorService().make_user_friendly(Exception(API_TEXT))
        assert out["category"] == "llm_usage_limit"
        assert out["message"] == (
            "I can't answer right now. The service that writes my replies has reached its usage "
            "limit, and it's expected to come back around November 1. Nothing you did caused this."
        )
        assert out["recovery"] == ""
        # the own-key sentence waits on a served check that a keyed user is not hit (CXO)
        assert "API key" not in out["message"]
        assert (
            "brief outage" not in out["message"] and "try again in a moment" not in out["message"]
        )

    def test_cxos_sentence_without_a_date(self):
        out = UserFriendlyErrorService().make_user_friendly(Exception(API_TEXT_NO_DATE))
        assert out["message"] == (
            "I can't answer right now. The service that writes my replies has reached its usage "
            "limit, and I don't know when it will come back. Nothing you did caused this."
        )

    def test_the_generic_outage_line_keeps_its_own_case(self):
        out = UserFriendlyErrorService().make_user_friendly(
            Exception("All configured LLM providers failed. Details: anthropic: connection reset")
        )
        assert out["category"] == "llm"
        assert "brief outage" in out["recovery"]


class TestFloorCopy:
    def test_floor_classifies_and_carries_the_bucket(self):
        assert floor._classify_llm_error(Exception(API_TEXT)) == "usage_limit"
        assert floor.FLOOR_FALLBACK_USAGE_LIMIT == usage_limit_sentence(API_TEXT_NO_DATE)
        assert "brief outage" not in floor.FLOOR_FALLBACK_USAGE_LIMIT
        src = open(floor.__file__).read()
        assert '"usage_limit": FLOOR_FALLBACK_USAGE_LIMIT' in src
        # the floor reads the dated form from the error text at the fallback site
        assert "fallback_message = usage_limit_sentence(str(e))" in src

    def test_one_sentence_source_for_both_surfaces(self):
        assert "around November 1" in usage_limit_sentence(API_TEXT)
        assert "I don't know when it will come back" in usage_limit_sentence(API_TEXT_NO_DATE)
