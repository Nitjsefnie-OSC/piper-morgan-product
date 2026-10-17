"""#2070: the consent line names the project the portfolio write targets."""

import pytest

from services.domain.models import Intent
from services.intent_service import consent_gate as cg
from services.shared_types import EffectClass, IntentCategory


def _intent(action, message):
    return Intent(
        category=IntentCategory.EXECUTION,
        action=action,
        confidence=0.9,
        original_message=message,
        context={"original_message": message},
    )


@pytest.mark.parametrize(
    "action,message,expected",
    [
        ("archive_project", "I would like to archive project Bar", "archive project Bar,"),
        ("archive_project", "archive project Bar", "archive project Bar,"),
        ("restore_project", "I would like to restore project Bar", "restore project Bar,"),
    ],
)
def test_consent_line_names_the_project(action, message, expected):
    offer = cg.build_consent_check_offer(_intent(action, message), EffectClass.WRITE)
    assert f"asking me to {expected}" in offer.question
    assert "Bar" in offer.offer["decline_message"]


def test_no_name_leaves_the_line_unchanged():
    offer = cg.build_consent_check_offer(_intent("archive_project", "archive"), EffectClass.WRITE)
    assert "asking me to archive project," in offer.question


def test_other_actions_unchanged():
    offer = cg.build_consent_check_offer(_intent("list_repos", "list repos"), EffectClass.WRITE)
    assert "asking me to list repos," in offer.question
