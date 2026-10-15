"""#2008: every standup surface takes the ruled empty-Yesterday line.

CXO ruling (2026-10-15): "No completions yesterday." in each format's own
wrapper. Layer: the three formatters with an empty yesterday, plus a
TestClient render of the /standup page. The page's empty-state string lives in
client-side JS inside the template, so the render test pins the served HTML;
it does not execute the JS.
"""

import uuid
from datetime import datetime, timezone

import pytest
from fastapi.testclient import TestClient

from services.auth.container import AuthContainer
from services.features.morning_standup import StandupResult
from web.api.routes.standup import format_as_markdown, format_as_slack, format_as_text

OLD = ("No accomplishments recorded", "Nothing wrapped up yesterday")


def _empty() -> StandupResult:
    return StandupResult(
        user_id="user-1",
        generated_at=datetime(2025, 10, 19, 21, 30, tzinfo=timezone.utc),
        generation_time_ms=1,
        yesterday_accomplishments=[],
        today_priorities=[],
        blockers=[],
        context_source="assembled",
        github_activity={},
        performance_metrics={},
        time_saved_minutes=0,
    )


@pytest.mark.parametrize(
    "fmt,wrapped",
    [
        (format_as_slack, "_No completions yesterday._"),
        (format_as_markdown, "*No completions yesterday.*"),
        (format_as_text, "(No completions yesterday.)"),
    ],
)
def test_formatter_empty_yesterday_line(fmt, wrapped):
    out = fmt(_empty())
    assert wrapped in out
    for old in OLD:
        assert old not in out


def test_standup_page_empty_yesterday_line():
    from pathlib import Path

    from fastapi.templating import Jinja2Templates

    from web.app import app

    if getattr(app.state, "templates", None) is None:
        repo = Path(__file__).resolve().parents[4]
        app.state.templates = Jinja2Templates(directory=str(repo / "templates"))
    client = TestClient(app, follow_redirects=False)
    token = AuthContainer.get_jwt_service().generate_access_token(
        user_id=uuid.uuid4(), user_email="u2008@example.com", scopes=["user"]
    )
    client.cookies.set("auth_token", token)
    r = client.get("/standup")
    assert r.status_code == 200
    assert "<p>No completions yesterday.</p>" in r.text
    for old in OLD:
        assert old not in r.text
    assert "Nothing flagged to watch." in r.text
