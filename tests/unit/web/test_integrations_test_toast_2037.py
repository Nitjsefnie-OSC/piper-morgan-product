"""#2037: the Integrations Test button shows the API's own message (toast and card
status line), verbatim, with no latency; the stale-OAuth line gets the warning style.

Runs the served page's OWN ``testConnection`` under Node with a minimal DOM/fetch stub
(not a browser: no CSS, no click). Node-dependent tests skip when ``node`` is absent.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import uuid
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from services.auth.container import AuthContainer
from web.app import app

REPO = Path(__file__).resolve().parents[3]
PAGE = "/settings/integrations"

OAUTH = "GitHub is working, using your GitHub connection."
PAT = "GitHub is working, using your personal token."
STALE = (
    "GitHub is working, using your personal token. "
    "Your GitHub connection needs re-authorizing, so I'm not using it right now."
)
FAILURE = "GitHub rejected the token."


@pytest.fixture(scope="module")
def body():
    if getattr(app.state, "templates", None) is None:
        from fastapi.templating import Jinja2Templates

        app.state.templates = Jinja2Templates(directory=str(REPO / "templates"))
    c = TestClient(app, follow_redirects=False)
    token = AuthContainer.get_jwt_service().generate_access_token(
        user_id=uuid.uuid4(), user_email="u2037@example.com", scopes=["user"]
    )
    c.cookies.set("auth_token", token)
    r = c.get(PAGE)
    assert r.status_code == 200
    return r.text


def _handler(body: str) -> str:
    start = body.index("// The stale-OAuth sentence the Test endpoint appends")
    end = body.index("async function testAllConnections()")
    return body[start:end]


def _run(body: str, reply: dict) -> dict:
    script = (
        "const calls = []; const status = {cls: new Set(), text: ''};\n"
        "const btn = { disabled: false, textContent: '', classList: {add(){}, remove(){}} };\n"
        "const statusEl = { get textContent() { return status.text; },\n"
        "  set textContent(v) { status.text = v; },\n"
        "  classList: { add(c) { status.cls.add(c); }, remove(c) { status.cls.delete(c); },\n"
        "    toggle(c, on) { on ? status.cls.add(c) : status.cls.delete(c); } } };\n"
        "const dot = { className: '' };\n"
        "const card = { querySelector(s) { return s === '.status-dot' ? dot : { appendChild(){} }; } };\n"
        "const document = { getElementById(id) {\n"
        "  if (id.startsWith('test-btn-')) return btn;\n"
        "  if (id.startsWith('status-')) return statusEl;\n"
        "  if (id.startsWith('card-')) return card;\n"
        "  return null; },\n"
        "  createElement() { return {}; } };\n"
        "const fetch = async () => ({ json: async () => JSON.parse(process.argv[1]) });\n"
        "function showToast(type, message, title) { calls.push({type, message, title}); }\n"
        + _handler(body)
        + "\n(async () => { await testConnection('github');\n"
        "process.stdout.write(JSON.stringify({toast: calls, status: status.text,\n"
        "  cls: [...status.cls], dot: dot.className})); })();\n"
    )
    res = subprocess.run(
        ["node", "-e", script, json.dumps(reply)], capture_output=True, text=True, timeout=30
    )
    assert res.returncode == 0, res.stderr
    return json.loads(res.stdout)


needs_node = pytest.mark.skipif(shutil.which("node") is None, reason="node not on PATH")


def _ok(message: str) -> dict:
    return {"integration": "github", "success": True, "message": message, "latency_ms": 368.81}


def test_page_no_longer_builds_the_generic_toast_or_shows_latency(body):
    handler = _handler(body)
    assert "connection successful`" not in handler
    assert "latency_ms" not in handler
    assert "Connected (" not in body


@needs_node
@pytest.mark.parametrize("message", [OAUTH, PAT])
def test_working_legs_show_the_message_verbatim(body, message):
    out = _run(body, _ok(message))
    assert out["toast"] == [{"type": "success", "message": message, "title": "Test Passed"}]
    assert out["status"] == message
    assert "warning" not in out["cls"] and "error" not in out["cls"]
    assert out["dot"] == "status-dot healthy"
    assert "368" not in out["status"]


@needs_node
def test_stale_oauth_line_gets_the_warning_style(body):
    out = _run(body, _ok(STALE))
    assert out["toast"] == [{"type": "warning", "message": STALE, "title": "Test Passed"}]
    assert out["status"] == STALE
    assert "warning" in out["cls"] and "error" not in out["cls"]
    assert out["dot"] == "status-dot degraded"
    assert "368" not in out["status"]


@needs_node
def test_generic_failure_keeps_the_error_style(body):
    reply = {
        "integration": "github",
        "success": False,
        "message": FAILURE,
        "latency_ms": 12.0,
        "fix_suggestion": "Check your token.",
    }
    out = _run(body, reply)
    assert out["toast"] == [{"type": "error", "message": FAILURE, "title": "Test Failed"}]
    assert out["status"] == FAILURE
    assert "error" in out["cls"] and "warning" not in out["cls"]
    assert out["dot"] == "status-dot failed"
