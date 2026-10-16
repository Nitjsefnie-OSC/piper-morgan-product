"""#2059: no raw user-text prefix in server logs, and Chroma telemetry off.

Layer: unit. structlog capture on the classifier's graph-context failure path
(the WARNING that reaches production logs) plus source scans. Not covered:
what a live Chroma process actually sends (no network in unit tests).
"""

import asyncio
import re
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from structlog.testing import capture_logs

from services.intent_service.classifier import IntentClassifier
from services.utils.utterance_log import KNOB, utterance_preview, utterance_sha256

ROOT = Path(__file__).resolve().parents[3]
MSG = "please summarise the quarterly acquisition plan for Harborview"


def _run_failing_graph_lookup():
    clf = IntentClassifier.__new__(IntentClassifier)
    clf.knowledge_graph_service = MagicMock()
    clf.knowledge_graph_service.get_relevant_context = AsyncMock(side_effect=RuntimeError("boom"))
    with capture_logs() as logs:
        asyncio.run(clf._get_graph_context(MSG, user_id="u1"))
    return logs


def test_graph_failure_warning_logs_no_text_by_default(monkeypatch):
    monkeypatch.delenv(KNOB, raising=False)
    logs = _run_failing_graph_lookup()
    warn = [e for e in logs if e["log_level"] == "warning"]
    assert warn, logs
    blob = repr(logs)
    assert MSG[:50] not in blob and "Harborview" not in blob and "quarterly" not in blob
    assert utterance_sha256(MSG) in blob


def test_graph_failure_warning_shows_preview_when_knob_on(monkeypatch):
    monkeypatch.setenv(KNOB, "1")
    logs = _run_failing_graph_lookup()
    assert MSG[:50] in repr(logs)


def test_utterance_preview_shapes(monkeypatch):
    monkeypatch.delenv(KNOB, raising=False)
    assert utterance_preview(MSG) == f"sha256={utterance_sha256(MSG)}"
    monkeypatch.setenv(KNOB, "on")
    assert utterance_preview(MSG) == MSG[:50]


_RAW = re.compile(r"\b(?:message|text|user_message|stripped|complaint)\[:(?:50|100)\]")


def test_no_raw_prefix_literal_left_in_services():
    offenders = []
    for p in (ROOT / "services").rglob("*.py"):
        if p.name == "utterance_log.py":
            continue
        for n, line in enumerate(p.read_text().splitlines(), 1):
            if _RAW.search(line) and re.search(
                r"preview|logger|log\.|\.info\(|\.warning\(|\.debug\(", line
            ):
                offenders.append(f"{p.relative_to(ROOT)}:{n}: {line.strip()}")
    assert not offenders, offenders


def test_document_ingester_disables_chroma_telemetry(tmp_path):
    from services.knowledge_graph import ingestion

    with patch.object(ingestion.chromadb, "PersistentClient") as client:
        ingestion.DocumentIngester(chroma_path=str(tmp_path))
    settings = client.call_args.kwargs["settings"]
    assert settings.anonymized_telemetry is False


def test_every_in_app_chroma_client_disables_telemetry():
    ctor = re.compile(r"chromadb\.(?:PersistentClient|HttpClient|Client|EphemeralClient)\(")
    found = 0
    for base in ("services", "scripts", "web", "main.py"):
        root = ROOT / base
        files = [root] if root.is_file() else root.rglob("*.py")
        for p in files:
            src = p.read_text()
            for m in ctor.finditer(src):
                found += 1
                call = src[m.start() : m.start() + 300]
                assert "anonymized_telemetry=False" in call, f"{p}: {call[:120]}"
    assert found >= 2
