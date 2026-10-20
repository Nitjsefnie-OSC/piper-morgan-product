"""#2109 — the shadows never spend the request's bound key.

Arch, 2026-10-20: asyncio's ``create_task`` copies the request context, so the inversion
and preclaim shadows' model calls were billed to the acting user, their own BYOC key
included. Now a shadow runs under its own key (``PIPER_SHADOW_LLM_KEY``) in a context where
the request's binding is replaced, or, with no shadow key and a request key bound, it is
skipped. With nothing bound (tests, offline scorers) it runs as before.

LAYER: both schedulers with their inner coroutines replaced by recorders (no router, no
network). DENOMINATOR: the three states of ``shadow_task_context`` for each shadow.
"""

from __future__ import annotations

import asyncio
from unittest.mock import patch

import pytest

from services.intent_service import inversion_shadow, preclaim_shadow
from services.llm import request_key
from services.llm.request_key import get_request_api_key, request_api_key


class _Recorder:
    def __init__(self):
        self.seen = []

    async def coro(self, *args, **kwargs):
        self.seen.append(get_request_api_key())


@pytest.fixture
def shadows_on(monkeypatch):
    monkeypatch.setenv("PIPER_INVERSION_SHADOW", "1")
    monkeypatch.setenv("PIPER_INVERSION_SHADOW_SAMPLE", "1.0")
    monkeypatch.setenv("PIPER_PRECLAIM_SHADOW", "1")
    monkeypatch.setenv("PIPER_PRECLAIM_SHADOW_SAMPLE", "1.0")
    monkeypatch.delenv(request_key.SHADOW_LLM_KEY_ENV, raising=False)


def _schedule_inversion():
    return inversion_shadow.maybe_schedule_shadow_check(
        "what's my status?", "get_project_status", session_id="s-2109", user_id="u-2109"
    )


def _schedule_preclaim():
    return preclaim_shadow.maybe_schedule_preclaim_shadow(
        "what's my status?",
        claimed_category="STATUS",
        claimed_action="get_project_status",
        pattern_list="STATUS_PATTERNS",
        entry_surface="pre_classify",
        session_id="s-2109",
        user_id="u-2109",
    )


class TestContextRule:
    def test_three_states(self, monkeypatch):
        monkeypatch.delenv(request_key.SHADOW_LLM_KEY_ENV, raising=False)
        assert request_key.shadow_task_context() == (None, "unbound")
        with request_api_key("sk-user-own"):
            assert request_key.shadow_task_context() == (None, "user_key_bound")
            monkeypatch.setenv(request_key.SHADOW_LLM_KEY_ENV, "sk-shadow")
            ctx, reason = request_key.shadow_task_context()
            assert reason == "shadow_key" and ctx is not None
            assert ctx.run(get_request_api_key) == "sk-shadow"
            assert get_request_api_key() == "sk-user-own"  # the request's own context untouched


@pytest.mark.asyncio
async def test_inversion_shadow_skips_when_a_user_key_is_bound_and_no_shadow_key(shadows_on):
    rec = _Recorder()
    with patch.object(inversion_shadow, "_shadow_check", rec.coro):
        with request_api_key("sk-user-own"):
            task = _schedule_inversion()
    assert task is None
    assert rec.seen == []


@pytest.mark.asyncio
async def test_inversion_shadow_runs_under_the_shadow_key_not_the_users(shadows_on, monkeypatch):
    monkeypatch.setenv(request_key.SHADOW_LLM_KEY_ENV, "sk-shadow")
    rec = _Recorder()
    with patch.object(inversion_shadow, "_shadow_check", rec.coro):
        with request_api_key("sk-user-own"):
            task = _schedule_inversion()
            assert task is not None
            await task
    assert rec.seen == ["sk-shadow"]


@pytest.mark.asyncio
async def test_inversion_shadow_with_nothing_bound_runs_as_before(shadows_on):
    rec = _Recorder()
    with patch.object(inversion_shadow, "_shadow_check", rec.coro):
        task = _schedule_inversion()
        assert task is not None
        await task
    assert rec.seen == [None]


@pytest.mark.asyncio
async def test_preclaim_shadow_skips_when_a_user_key_is_bound_and_no_shadow_key(shadows_on):
    rec = _Recorder()
    with patch.object(preclaim_shadow, "_preclaim_check", rec.coro):
        with request_api_key("sk-user-own"):
            task = _schedule_preclaim()
    assert task is None
    assert rec.seen == []


@pytest.mark.asyncio
async def test_preclaim_shadow_runs_under_the_shadow_key_not_the_users(shadows_on, monkeypatch):
    monkeypatch.setenv(request_key.SHADOW_LLM_KEY_ENV, "sk-shadow")
    rec = _Recorder()
    with patch.object(preclaim_shadow, "_preclaim_check", rec.coro):
        with request_api_key("sk-user-own"):
            task = _schedule_preclaim()
            assert task is not None
            await task
    assert rec.seen == ["sk-shadow"]
