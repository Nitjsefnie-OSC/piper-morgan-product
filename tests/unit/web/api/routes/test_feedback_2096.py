"""#2096 — the Send feedback page (CXO's shape and words, 2026-10-19) on the PM-005 feedback API.

xian, card A6: Todos and Projects in seconds, "I did not find any way to give feedback."
The repo already had a mounted POST /api/v1/feedback and a feedback table that no surface used;
this adds the page, the rail link, the page-path attached by code, and an admin read.

LAYER: the routes through a real TestClient with the service replaced at its injected seam and
the signed-in user overridden; the page by a real render; the rail by template read.
DENOMINATOR: submit with a page, submit with an outside URL, refuse-empty, the admin read and
its 403, the page's words, the rail link.
"""

from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from services.auth.auth_middleware import get_current_user, require_admin
from web.api.dependencies import get_feedback_service
from web.api.routes import feedback as api

USER = SimpleNamespace(
    user_id="11111111-1111-1111-1111-111111111111", sub="11111111-1111-1111-1111-111111111111"
)


def _service():
    svc = MagicMock()
    svc.capture_feedback = AsyncMock(return_value="fb-1")
    svc.list_feedback = AsyncMock(
        return_value=[
            SimpleNamespace(
                id="fb-1",
                user_id=USER.sub,
                comment="The Thursday agenda answered for today.",
                context={"page_path": "/todos"},
                created_at=None,
            )
        ]
    )
    return svc


def _client(svc, admin=True):
    app = FastAPI()
    app.include_router(api.router)
    app.include_router(api.admin_router)
    app.dependency_overrides[get_current_user] = lambda: USER
    app.dependency_overrides[get_feedback_service] = lambda: svc
    if admin:
        app.dependency_overrides[require_admin] = lambda: USER
    return TestClient(app, raise_server_exceptions=False)


class TestSubmitFromThePage:
    def test_page_path_and_source_ui_are_attached_by_code(self):
        svc = _service()
        r = _client(svc).post(
            "/api/v1/feedback",
            params={"content": "Hi", "feedback_type": "tester", "page_path": "/todos"},
        )
        assert r.status_code == 200 and r.json()["id"] == "fb-1"
        kw = svc.capture_feedback.await_args.kwargs
        assert kw["feedback_type"] == "tester"
        assert kw["context"] == {"page_path": "/todos"}
        assert kw["source"] == "ui"

    def test_an_outside_url_is_not_attached(self):
        svc = _service()
        _client(svc).post(
            "/api/v1/feedback", params={"content": "Hi", "page_path": "https://evil.example/x"}
        )
        kw = svc.capture_feedback.await_args.kwargs
        assert kw["context"] is None and kw["source"] == "api"

    def test_empty_content_is_refused_without_a_write(self):
        svc = _service()
        r = _client(svc).post("/api/v1/feedback", params={"content": "   "})
        assert r.status_code == 400
        svc.capture_feedback.assert_not_awaited()


class TestAdminRead:
    def test_admin_lists_tester_rows_with_page_and_body(self):
        svc = _service()
        r = _client(svc).get("/api/v1/admin/feedback")
        assert r.status_code == 200
        body = r.json()
        assert body["count"] == 1
        assert body["feedback"][0]["body"] == "The Thursday agenda answered for today."
        assert body["feedback"][0]["page_path"] == "/todos"
        assert svc.list_feedback.await_args.kwargs["feedback_type"] == "tester"

    def test_non_admin_is_refused(self, monkeypatch):
        import services.auth.auth_middleware as am

        async def _not_admin(_uid):
            return False

        monkeypatch.setattr(am, "_user_is_admin", _not_admin, raising=False)
        r = _client(_service(), admin=False).get("/api/v1/admin/feedback")
        assert r.status_code in (401, 403)


class TestPageAndRail:
    def test_page_carries_cxos_words(self):
        from jinja2 import Environment, FileSystemLoader

        env = Environment(loader=FileSystemLoader("templates"))
        html = env.get_template("feedback.html").render(
            request=None, user={"username": "t", "is_admin": False}, from_path="/todos"
        )
        assert "<h1>Send feedback</h1>" in html
        assert 'placeholder="What happened, or what would help?"' in html
        assert ">Send</button>" in html
        assert "Thanks, we got it." in html
        assert "That didn't send. You can email support@pipermorgan.ai instead." in html
        assert "Prefer email? support@pipermorgan.ai" in html
        assert "/api/v1/feedback" in html and "feedback_type: 'tester'" in html

    def test_rail_has_the_link_on_every_shell_page(self):
        rail = open("templates/components/nav_rail.html").read()
        assert 'href="/feedback"' in rail and ">Send feedback</a>" in rail
