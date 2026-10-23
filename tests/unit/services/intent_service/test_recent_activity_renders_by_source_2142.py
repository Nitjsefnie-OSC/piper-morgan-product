"""#2142 — the merged recent-activity feed renders each item under its own source.

Served on alpha fc183c41bc (Q27): "Tell me more about the GitHub integration"
said "I can see recent activity from your repo: a planning review, a 1:1 and a
team sync". Those were calendar events. The floor rendered every
``recent_activity`` item under "Recent GitHub activity" as ``#? issue``.

Arch (10-22 21:28): context given to the model carries each item's own source.
The render groups by the item's ``source`` tag; counts are per source; the
``+`` cap marks only the source that was capped; an item with no source tag is
never rendered under a connector's name. Pins are on the rendered context.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from services.intent_service.context_assembler import ContextAssembler, _counts_by_source
from services.intent_service.conversational_floor import ConversationalFloor

_GITHUB = {
    "source": "github",
    "number": 2142,
    "title": "Render activity by source",
    "state": "open",
    "type": "issue",
    "updated_at": "2026-10-22T18:00:00Z",
}
_PR = {**_GITHUB, "number": 27, "title": "Label PRs", "type": "pr"}
_MEETING = {
    "source": "calendar",
    "title": "Planning review",
    "updated_at": "2026-10-21T17:00:00Z",
    "start_time": "2026-10-21T17:00:00Z",
}
_ONE_ON_ONE = {**_MEETING, "title": "Weekly 1:1"}
_SLACK = {
    "source": "slack",
    "title": "can you look at the launch notes",
    "updated_at": "2026-10-22T16:00:00Z",
    "channel_type": "im",
}


def _render(domain_context):
    return ConversationalFloor(llm_client=MagicMock())._format_domain_context(domain_context)


def _section(text, heading):
    """The heading line and its bullets, up to the next top-level line."""
    out, inside = [], False
    for line in text.splitlines():
        if line.lstrip().startswith(f"- {heading}"):
            inside = True
            out.append(line)
            continue
        if inside:
            if line.startswith("    •"):
                out.append(line)
            else:
                break
    return "\n".join(out)


def test_calendar_events_never_appear_under_a_github_heading():
    text = _render(
        {
            "recent_activity": [_MEETING, _GITHUB, _ONE_ON_ONE],
            "recent_activity_count": 3,
            "recent_activity_window_days": 7,
        }
    )
    github = _section(text, "Recent GitHub activity")
    calendar = _section(text, "Recent calendar events")
    assert "Planning review" not in github
    assert "Weekly 1:1" not in github
    assert "Planning review" in calendar and "Weekly 1:1" in calendar
    assert "#2142 issue (open" in github
    assert "#?" not in text


def test_a_calendar_only_feed_names_no_github_at_all():
    text = _render({"recent_activity": [_MEETING, _ONE_ON_ONE], "recent_activity_count": 2})
    assert "GitHub" not in text
    assert "- Recent calendar events (2 in last 7 days):" in text


def test_counts_are_per_source_and_the_cap_marks_only_github():
    text = _render(
        {
            "recent_activity": [_GITHUB, _PR, _MEETING, _SLACK],
            "recent_activity_count": 41,
            "recent_activity_count_capped": True,
            "recent_activity_counts_by_source": {"github": 30, "calendar": 9, "slack": 2},
            "recent_activity_window_days": 7,
        }
    )
    assert "- Recent GitHub activity (30+ in last 7 days):" in text
    assert "- Recent calendar events (9 in last 7 days):" in text
    assert "- Recent Slack messages (2 in last 7 days):" in text
    assert "41" not in text  # the merged total is no source's count
    assert "#27 PR (open" in text


def test_an_untagged_item_is_never_under_a_connectors_name():
    untagged = {"title": "Something happened", "updated_at": "2026-10-22T10:00:00Z"}
    text = _render({"recent_activity": [untagged, _GITHUB]})
    assert "Something happened" not in _section(text, "Recent GitHub activity")
    assert "- Other recent activity, source not recorded (1 items):" in text
    assert "Something happened" in _section(text, "Other recent activity")


def test_without_per_source_counts_each_heading_counts_its_own_items():
    """A cached feed from before this change has no per-source counts."""
    text = _render(
        {
            "recent_activity": [_GITHUB, _MEETING, _ONE_ON_ONE],
            "recent_activity_count": 3,
        }
    )
    assert "- Recent GitHub activity (1 in last 7 days):" in text
    assert "- Recent calendar events (2 in last 7 days):" in text


def test_a_source_counted_but_not_listed_keeps_its_heading():
    """Arch 10-23: GitHub filled the 10-item list; calendar had 4 events, none listed."""
    text = _render(
        {
            "recent_activity": [_GITHUB, _PR],
            "recent_activity_counts_by_source": {"github": 12, "calendar": 4},
            "recent_activity_window_days": 7,
        }
    )
    assert "- Recent calendar events (4 in last 7 days; not listed here):" in text
    assert "- Recent GitHub activity (12 in last 7 days):" in text
    assert "Recent Slack messages" not in text  # zero items, zero count: no heading


def test_counts_by_source_counts_every_item_before_the_cap():
    assert _counts_by_source([_GITHUB, _PR, _MEETING, {"title": "x"}]) == {
        "github": 2,
        "calendar": 1,
        "unknown": 1,
    }


@pytest.mark.asyncio
async def test_the_assembler_reports_per_source_counts():
    assembler = ContextAssembler.__new__(ContextAssembler)
    with (
        patch.object(
            assembler, "_fetch_github_activity_items", new=AsyncMock(return_value=([_GITHUB], True))
        ),
        patch.object(
            assembler,
            "_fetch_calendar_activity_items",
            new=AsyncMock(return_value=[_MEETING, _ONE_ON_ONE]),
        ),
        patch.object(assembler, "_fetch_slack_activity_items", new=AsyncMock(return_value=[])),
        patch.object(assembler, "_fetch_slack_mentions_items", new=AsyncMock(return_value=[])),
    ):
        result = await assembler._compute_recent_activity("u-2142")
    assert result["recent_activity_counts_by_source"] == {"github": 1, "calendar": 2}
    assert result["recent_activity_count_capped"] is True
