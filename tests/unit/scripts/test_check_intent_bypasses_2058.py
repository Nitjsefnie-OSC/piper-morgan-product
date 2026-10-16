"""#2058 -- the bypass scanner reads each route's own body.

Before: ``content.find("@get")`` never matched ``@router.get`` (-1), so the
body was empty and every NL-like route was reported, whatever it contained.
"""

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "scripts"))
from check_intent_bypasses import check_bypasses, scan_text  # noqa: E402

FIXTURE = """
from fastapi import APIRouter
router = APIRouter()

@router.get("/chat/history")
async def history():
    return []

@router.post("/chat/send")
async def send(body):
    return await intent_service.process_intent(body)

@router.post("/ask/anything")
async def ask(body):
    return {"echo": body}

@router.get("/health")
async def health():
    return "ok"
"""


def test_reads_own_body_not_first_decorator_of_that_method():
    found = {(b["method"], b["path"]) for b in scan_text(FIXTURE)}
    # /chat/send uses intent -> not reported; the two without it are.
    assert found == {("GET", "/chat/history"), ("POST", "/ask/anything")}


def test_one_with_intent_one_without_gives_one_bypass():
    src = (
        '@router.post("/a/chat")\nasync def a():\n    return intent_service.x()\n'
        '@app.post("/b/message")\nasync def b():\n    return 1\n'
    )
    assert [(b["method"], b["path"]) for b in scan_text(src)] == [("POST", "/b/message")]


def test_route_with_intent_in_later_route_does_not_count():
    src = (
        '@router.get("/chat/x")\nasync def x():\n    return 1\n'
        '@router.get("/other")\nasync def y():\n    return intent_service\n'
    )
    assert [b["path"] for b in scan_text(src)] == ["/chat/x"]


def test_check_bypasses_walks_a_root(tmp_path):
    (tmp_path / "r.py").write_text(FIXTURE)
    assert len(check_bypasses(tmp_path)) == 2
