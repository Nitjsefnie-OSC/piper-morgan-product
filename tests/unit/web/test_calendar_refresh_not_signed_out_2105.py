"""#2105 — Refresh List on an unconnected calendar never raises the signed-out modal.

Web, 2026-10-20 on alpha ef907b2cd7: the calendars endpoint answered 401 for "no credential",
the shared 401 interceptor raised the #2067 "You've been signed out" modal, and the session
was valid (`/auth/me` 200 ten seconds later). Class 3 (CXO), admitted by xian. The route
answers 409 now with CXO's line; the page shows that line inline and as an info toast, says
"Refreshed" only when the list loaded, and leaves the 401 branch for a real sign-out.

LAYER: the route's constants and the template's text (the render path is Web's served
check). DENOMINATOR: both 409 lines, the template's 409 branch, the conditional toast.
"""

from __future__ import annotations

from pathlib import Path

from web.api.routes import settings_integrations as route

TEMPLATE = Path(__file__).resolve().parents[3] / "templates" / "settings_calendar.html"


def test_cxos_line_is_the_routes_not_connected_detail():
    assert route.CALENDAR_NOT_CONNECTED_LINE == (
        "Google Calendar isn't connected yet. Connect it first, then refresh the list."
    )
    assert "signed out" not in route.CALENDAR_NEEDS_RECONNECT_LINE.lower()


def test_calendars_route_never_raises_401_for_a_credential_reason():
    src = Path(route.__file__).read_text()
    start = src.index("async def get_calendar_list(")
    end = src.index("\n@router.", start)
    body = src[start:end]
    assert "HTTP_401_UNAUTHORIZED" not in body
    assert body.count("HTTP_409_CONFLICT") == 2
    assert "await keychain.aget_api_key(" in body


def test_template_shows_the_409_line_without_the_modal_and_refreshed_only_on_success():
    html = TEMPLATE.read_text()
    load = html[
        html.index("async function loadCalendarList()") : html.index("function renderCalendarList(")
    ]
    assert "response.status === 409" in load
    assert "Toast.show('info', 'Google Calendar', line)" in load
    assert "return false;" in load and "return true;" in load
    refresh = html[
        html.index("async function refreshCalendarList()") : html.index(
            "async function saveCalendarPreferences()"
        )
    ]
    assert "const loaded = await loadCalendarList();" in refresh
    assert "if (loaded) Toast.show('success', 'Refreshed'" in refresh
