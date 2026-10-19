"""#2097 — a create that landed is confirmed, said with its number, and never retried blind.

Web, #1386 scenario B on alpha e801b1a309: "file it as is" created #10 in the test repo, the
reply said "couldn't verify it landed … say 'file it' to try again", "yes" created a duplicate
#11, and "what did we create" said nothing was confirmed. CXO (Class 3): landed → "Created
issue #10, "<title>", in <owner/repo>."; truly unconfirmed → "I sent the request to create it
in <owner/repo>, but GitHub didn't confirm it. Check there before trying again." (no retry
invitation); a second create of an open title asks first.

LAYER: the adapter's guard against a REAL in-memory MCP round-trip (the #1220 fixture, plus
a search_issues tool); the floor's renderer, the drafted-issue seam and the create handler by
direct call with the router patched at its seam. DENOMINATOR: the three unconfirmed shapes
(no number in the response, read-back miss, nothing found), the duplicate ask both ways, the
released draft.
"""

from __future__ import annotations

import contextlib
import json
from datetime import datetime, timedelta, timezone
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
import pytest_asyncio

aiosqlite = pytest.importorskip("aiosqlite")
from mcp.server.fastmcp import FastMCP  # noqa: E402
from mcp.shared.memory import create_connected_server_and_client_session  # noqa: E402
from sqlalchemy.ext.asyncio import (  # noqa: E402
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from services.connectors.binding_repository import ConnectorBindingRepository  # noqa: E402
from services.database.models import ConnectorBinding  # noqa: E402
from services.domain.models import Intent  # noqa: E402
from services.intent.intent_service import IntentService  # noqa: E402
from services.intent_service import drafted_issue as di  # noqa: E402
from services.intent_service.classifier import IntentClassifier  # noqa: E402
from services.mcp.consumer import github_adapter as gh_mod  # noqa: E402
from services.mcp.consumer.github_adapter import GitHubMCPSpatialAdapter  # noqa: E402
from services.mcp.consumer.mcp_client import MCPClient  # noqa: E402
from services.shared_types import IntentCategory  # noqa: E402

pytestmark = pytest.mark.asyncio

_ALPHA = "11111111-1111-1111-1111-111111111111"
TITLE = "Add search functionality to navigation bar"
ROUTER = "services.integrations.github.github_integration_router.GitHubIntegrationRouter"
RESOLVER = "services.integrations.github.repo_resolver"
_FULL = "dinp-machine/piper-test-activity"


@pytest_asyncio.fixture
async def sm(monkeypatch):
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as conn:
        await conn.run_sync(lambda c: ConnectorBinding.__table__.create(c, checkfirst=True))
    maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    @contextlib.asynccontextmanager
    async def _scope():
        async with maker() as s:
            yield s

    monkeypatch.setattr(gh_mod.AsyncSessionFactory, "session_scope", staticmethod(_scope))
    async with maker() as s:
        await ConnectorBindingRepository(s).upsert(
            _ALPHA, "github", status="bound", mcp_server_ref="http://srv/mcp"
        )
        await s.commit()
    yield maker
    await engine.dispose()


def _fixture(
    adapter, *, create_returns_number=True, readback_works=True, search_has_it=True, old=False
):
    """Fake github-mcp-server: issue_write/create lands #10 titled TITLE; the response may omit
    the number; issue_read may lose it; search_issues finds it by title (or not)."""
    server = FastMCP("github-2097-fixture")
    created_at = datetime.now(timezone.utc) - (timedelta(days=3) if old else timedelta(seconds=5))
    issue = {
        "number": 10,
        "title": TITLE,
        "state": "open",
        "html_url": f"https://github.com/{_FULL}/issues/10",
        "created_at": created_at.isoformat().replace("+00:00", "Z"),
    }

    @server.tool(name="issue_write")
    def issue_write(method: str, owner: str, repo: str, title: str = None, body: str = None) -> str:
        if method == "create":
            if create_returns_number:
                return json.dumps(issue)
            return json.dumps({"html_url": issue["html_url"], "title": title})
        raise ValueError(method)

    @server.tool(name="issue_read")
    def issue_read(method: str, owner: str, repo: str, issue_number: int) -> str:
        if readback_works and issue_number == 10:
            return json.dumps(issue)
        return json.dumps({})

    @server.tool(name="search_issues")
    def search_issues(query: str, sort: str = None, order: str = None, perPage: int = 30) -> str:
        if search_has_it and f"repo:{_FULL}" in query and TITLE in query:
            return json.dumps({"total_count": 1, "items": [issue]})
        return json.dumps({"total_count": 0, "items": []})

    @contextlib.asynccontextmanager
    async def _ctx(binding):
        async with create_connected_server_and_client_session(server) as session:
            yield MCPClient(session)

    adapter._mcp_client_ctx = _ctx
    return issue


class TestAdapterConfirmsByTitle:
    async def test_response_without_number_is_confirmed_by_the_title_search(self, sm):
        adapter = GitHubMCPSpatialAdapter()
        _fixture(adapter, create_returns_number=False)
        wr = await adapter.create_issue_connector(
            _ALPHA, owner="dinp-machine", repo="piper-test-activity", title=TITLE, body="b"
        )
        assert wr.verified is True and wr.issue_number == 10
        assert wr.url.endswith("/issues/10")

    async def test_readback_miss_is_confirmed_by_the_title_search(self, sm):
        adapter = GitHubMCPSpatialAdapter()
        _fixture(adapter, readback_works=False)
        wr = await adapter.create_issue_connector(
            _ALPHA, owner="dinp-machine", repo="piper-test-activity", title=TITLE, body="b"
        )
        assert wr.verified is True and wr.issue_number == 10

    async def test_nothing_found_stays_unverified(self, sm):
        adapter = GitHubMCPSpatialAdapter()
        _fixture(adapter, create_returns_number=False, search_has_it=False)
        wr = await adapter.create_issue_connector(
            _ALPHA, owner="dinp-machine", repo="piper-test-activity", title=TITLE, body="b"
        )
        assert wr.verified is False and wr.attempted is True

    async def test_an_old_match_is_not_this_write(self, sm):
        adapter = GitHubMCPSpatialAdapter()
        _fixture(adapter, create_returns_number=False, old=True)
        wr = await adapter.create_issue_connector(
            _ALPHA, owner="dinp-machine", repo="piper-test-activity", title=TITLE, body="b"
        )
        assert wr.verified is False

    async def test_find_open_issue_by_title_is_exact(self, sm):
        adapter = GitHubMCPSpatialAdapter()
        _fixture(adapter)
        hit = await adapter.find_open_issue_by_title_connector(
            _ALPHA, owner="dinp-machine", repo="piper-test-activity", title=TITLE
        )
        assert hit and hit["number"] == 10
        miss = await adapter.find_open_issue_by_title_connector(
            _ALPHA, owner="dinp-machine", repo="piper-test-activity", title="Something else"
        )
        assert miss is None


class _ExplosiveLLM:
    def __getattr__(self, name):
        raise AssertionError(f"LLM boundary touched ({name})")


@pytest.fixture
def service():
    from services.intent_service.workflow_entries import register_default_workflows

    register_default_workflows()
    with patch("services.intent.intent_service.LearningHandler"):
        with patch("services.intent.intent_service.ConversationKnowledgeGraphIntegration"):
            clf = IntentClassifier(llm_service=_ExplosiveLLM())
            return IntentService(intent_classifier=clf)


def _intent(message=f"Create a GitHub issue: '{TITLE}'", **extra):
    ctx = {
        "original_message": message,
        "user_id": _ALPHA,
        "title": TITLE,
        "repository": _FULL,
        **extra,
    }
    return Intent(
        category=IntentCategory.EXECUTION,
        action="create_issue",
        original_message=message,
        confidence=1.0,
        context=ctx,
    )


def _github_config():
    return patch(
        "services.configuration.piper_config_loader.piper_config_loader.load_github_config",
        return_value=MagicMock(default_labels=[]),
    )


def _gate_open():
    return patch(
        "services.intent_service.collaboration_gate.gate_holds", new=AsyncMock(return_value=False)
    )


class TestRendererWords:
    def test_create_unconfirmed_is_cxos_line_without_a_retry_invitation(self, service):
        intent = _intent()
        out = service._unverified_write_result(
            RuntimeError("GitHub write could not be verified — it may or may not have landed."),
            intent,
            "wf",
            repository=_FULL,
        )
        assert out.message == (
            f"I sent the request to create it in {_FULL}, but GitHub didn't confirm it. "
            "Check there before trying again."
        )
        assert "try again" not in out.message.replace("before trying again", "")
        assert out.intent_data["write_unconfirmed"] is True

    def test_update_keeps_the_general_line(self, service):
        intent = _intent()
        intent.action = "close_issue"
        out = service._unverified_write_result(
            RuntimeError("may or may not have landed"), intent, "wf"
        )
        assert "may or may not have gone through" in out.message


class TestCreateHandler:
    async def test_landed_reply_quotes_number_title_and_repo(self, service):
        created = {
            "number": 10,
            "title": TITLE,
            "html_url": f"https://github.com/{_FULL}/issues/10",
        }
        with (
            _gate_open(),
            _github_config(),
            patch(f"{ROUTER}.initialize", new=AsyncMock()),
            patch(f"{ROUTER}.is_available", new=AsyncMock(return_value=True)),
            patch(f"{ROUTER}.find_open_issue_by_title", new=AsyncMock(return_value=None)),
            patch(f"{ROUTER}.create_issue", new=AsyncMock(return_value=created)),
        ):
            result = await service._handle_create_issue(_intent(), "wf", "s-2097-a", user_id=_ALPHA)
        assert result.message == f'Created issue #10, "{TITLE}", in {_FULL}.'
        assert result.intent_data["created_activity"]["target_ref"] == f"{_FULL}#10"

    async def test_second_create_of_an_open_title_asks_first_then_yes_files(self, service):
        existing = {"number": 10, "title": TITLE}
        created = {
            "number": 11,
            "title": TITLE,
            "html_url": f"https://github.com/{_FULL}/issues/11",
        }
        sid = "s-2097-dup"
        with (
            _gate_open(),
            _github_config(),
            patch(f"{ROUTER}.initialize", new=AsyncMock()),
            patch(f"{ROUTER}.is_available", new=AsyncMock(return_value=True)),
            patch(f"{ROUTER}.find_open_issue_by_title", new=AsyncMock(return_value=existing)) as f,
            patch(f"{ROUTER}.create_issue", new=AsyncMock(return_value=created)) as w,
        ):
            asked = await service._handle_create_issue(_intent(), "wf", sid, user_id=_ALPHA)
            assert asked.message == di.duplicate_issue_question(TITLE, _FULL, 10)
            w.assert_not_awaited()
            assert service.workflow_offer_service._pending_offers.get(sid) is not None
            filed = await service.process_intent(message="yes", session_id=sid, user_id=_ALPHA)
        assert w.await_count == 1
        assert f.await_count == 1  # the allow marker skipped the second check
        assert f'Created issue #11, "{TITLE}", in {_FULL}.' in filed.message

    async def test_no_on_the_duplicate_ask_files_nothing(self, service):
        existing = {"number": 10, "title": TITLE}
        sid = "s-2097-no"
        with (
            _gate_open(),
            _github_config(),
            patch(f"{ROUTER}.initialize", new=AsyncMock()),
            patch(f"{ROUTER}.is_available", new=AsyncMock(return_value=True)),
            patch(f"{ROUTER}.find_open_issue_by_title", new=AsyncMock(return_value=existing)),
            patch(f"{ROUTER}.create_issue", new=AsyncMock()) as w,
        ):
            await service._handle_create_issue(_intent(), "wf", sid, user_id=_ALPHA)
            declined = await service.process_intent(message="no", session_id=sid, user_id=_ALPHA)
        w.assert_not_awaited()
        assert "nothing new was filed" in declined.message
        assert service.workflow_offer_service._pending_offers.get(sid) is None


class TestDraftedIssueRelease:
    async def test_unconfirmed_file_releases_the_draft_no_retry(self):
        offer = {
            "kind": "drafted_issue",
            "question": di._POST_BIND_ASK,
            "pending_action": {
                "kind": di.DRAFTED_ISSUE_KIND,
                "action": "create_issue",
                "intent": _intent(),
                "draft": {"title": TITLE, "body": "b"},
            },
        }
        svc = MagicMock()
        rail = {
            "message": f"I sent the request to create it in {_FULL}, but GitHub didn't confirm it. Check there before trying again.",
            "intent_data": {"write_unconfirmed": True},
        }
        with patch(
            "services.intent_service.workflow_entries.run_confirm_pending_action_workflow",
            new=AsyncMock(return_value=rail),
        ):
            out = await di.handle_drafted_issue_turn(
                offer, "file it as is", session_id="s-2097-rel", user_id=_ALPHA, intent_service=svc
            )
        assert out["message"] == rail["message"]
        assert "file it" not in out["message"]
        svc.workflow_offer_service.set_pending_offer.assert_not_called()
        assert out["intent_data"]["drafted_issue_released"] is True
