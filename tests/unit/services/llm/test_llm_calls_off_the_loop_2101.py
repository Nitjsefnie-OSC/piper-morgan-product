"""#2101 — a provider completion never holds the event loop.

PA's watchdog read on alpha 987dd10ed7 (2026-10-20): 26 of 26 `event_loop_blocked` stacks
ended in `clients.py` calling the synchronous Anthropic SDK (`client.messages.create`) on the
loop, down through sync httpx to `ssl.read`; 91 s of a 155 s canonical run were blocked. The
three provider round trips now run in `asyncio.to_thread`.

LAYER: `LLMClient`'s provider legs with the per-request client builder replaced by a fake that
records the calling thread (no network). DENOMINATOR: the Anthropic and OpenAI legs (the Gemini leg has no
per-request client path and raises before any network call); a source pin over the module
for a bare provider call inside a coroutine.
"""

from __future__ import annotations

import re
import threading
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import pytest

from services.llm import clients as mod


class _Recorder:
    def __init__(self, response):
        self.thread = None
        self.kwargs = None
        self._response = response

    def __call__(self, **kwargs):
        self.thread = threading.current_thread()
        self.kwargs = kwargs
        return self._response


def _anthropic_fake():
    response = SimpleNamespace(
        usage=SimpleNamespace(input_tokens=3, output_tokens=2),
        content=[SimpleNamespace(text="hi")],
    )
    rec = _Recorder(response)
    client = SimpleNamespace(messages=SimpleNamespace(create=rec))
    return client, rec


def _openai_fake():
    response = SimpleNamespace(
        usage=SimpleNamespace(prompt_tokens=3, completion_tokens=2),
        choices=[SimpleNamespace(message=SimpleNamespace(content="hi"))],
    )
    rec = _Recorder(response)
    client = SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=rec)))
    return client, rec


def _config(model):
    return {"model": model, "max_tokens": 16, "temperature": 0.0}


def _llm():
    return mod.LLMClient.__new__(mod.LLMClient)


@pytest.mark.asyncio
async def test_anthropic_round_trip_runs_on_a_worker_thread():
    client, rec = _anthropic_fake()
    model = next(m for m in mod.LLMModel if "claude" in m.value.lower())
    with patch("services.llm.request_key.anthropic_client_for_request", return_value=client):
        text = await _llm()._anthropic_complete("hello", _config(model))
    assert text == "hi"
    assert rec.thread is not None and rec.thread is not threading.current_thread()
    assert rec.kwargs["messages"] == [{"role": "user", "content": "hello"}]


@pytest.mark.asyncio
async def test_openai_round_trip_runs_on_a_worker_thread():
    client, rec = _openai_fake()
    model = next(m for m in mod.LLMModel if "gpt" in m.value.lower())
    with (
        patch("services.llm.request_key.request_spend_key", return_value="k-2101"),
        patch("services.llm.clients.OpenAI", return_value=client),
    ):
        text = await _llm()._openai_complete("hello", _config(model))
    assert text == "hi"
    assert rec.thread is not None and rec.thread is not threading.current_thread()


def test_no_bare_provider_call_inside_a_coroutine():
    """Every provider round trip in clients.py is wrapped in asyncio.to_thread."""
    src = Path(mod.__file__).read_text()
    bare = re.findall(
        r"^\s*response = client\.(?:messages\.create|chat\.completions\.create)\(", src, flags=re.M
    )
    assert bare == [], bare
    assert src.count("await asyncio.to_thread(client.messages.create") == 1
    assert src.count("await asyncio.to_thread(client.chat.completions.create") == 1
