"""PM 2026-10-13 (relayed by Comms from the privacy Section C review): "keep
only fingerprints of logs." Every server log line that carried a user's
message, query or cached text now carries its sha256 by default and the text
only under the opt-in knob ``PIPER_INVERSION_LOG_UTTERANCE`` (default flipped
from "1" to "0"; the name is kept so an existing Fly secret keeps working).

Pinned here: the helper's default and parsing; the three inversion readers
follow it (default off → sha only; "1" → text); the pre-classifier and the
intent service no longer interpolate the message into a log line by default
(observed through structlog's capture, not inferred from source); and a
source-level sweep that the known text-logging sites all go through the
helper — a new ``os.environ.get("PIPER_INVERSION_LOG_UTTERANCE"`` or a
``logger.*(f"…{message}…")`` elsewhere fails this file.

Layer (m-43): unit; structlog capture for the emitted fields; source read for
the sweep. Not covered: what Fly keeps (7-day Grafana log search per Fly's
docs) — operational, in Lead's reply to Comms.
"""

import hashlib
import inspect
import os
import re

import pytest
from structlog.testing import capture_logs

from services.intent_service import inversion_live, inversion_shadow, preclaim_shadow
from services.intent_service.pre_classifier import PreClassifier
from services.utils import utterance_log
from services.utils.utterance_log import (
    DEFAULT,
    KNOB,
    log_full_utterance,
    utterance_fields,
    utterance_sha256,
)

_MSG = "remind me to send the invoice on Friday"
_SHA = hashlib.sha256(_MSG.encode()).hexdigest()


@pytest.fixture
def knob_unset(monkeypatch):
    monkeypatch.delenv(KNOB, raising=False)


@pytest.fixture
def knob_on(monkeypatch):
    monkeypatch.setenv(KNOB, "1")


class TestHelper:
    def test_default_is_off(self, knob_unset):
        assert DEFAULT == "0"
        assert log_full_utterance() is False

    @pytest.mark.parametrize("value", ["1", "true", "YES", " on "])
    def test_truthy_values_opt_in(self, monkeypatch, value):
        monkeypatch.setenv(KNOB, value)
        assert log_full_utterance() is True

    @pytest.mark.parametrize("value", ["0", "false", "", "no", "off"])
    def test_falsy_values_stay_off(self, monkeypatch, value):
        monkeypatch.setenv(KNOB, value)
        assert log_full_utterance() is False

    def test_fields_default_sha_only(self, knob_unset):
        assert utterance_fields(_MSG) == {"utterance_sha256": _SHA}
        assert utterance_fields(_MSG, key="query") == {"query_sha256": _SHA}
        assert utterance_sha256(_MSG) == _SHA

    def test_fields_opt_in_carries_text(self, knob_on):
        assert utterance_fields(_MSG) == {"utterance_sha256": _SHA, "utterance": _MSG}

    def test_empty_text_is_safe(self, knob_unset):
        assert utterance_fields("")["utterance_sha256"] == hashlib.sha256(b"").hexdigest()
        assert "utterance" not in utterance_fields(None)  # type: ignore[arg-type]


class TestInversionReadersFollowTheHelper:
    @pytest.mark.parametrize(
        "reader",
        [
            inversion_live._log_full_utterance,
            inversion_shadow._log_full_utterance,
            preclaim_shadow._log_full_utterance,
        ],
    )
    def test_default_off(self, knob_unset, reader):
        assert reader() is False

    @pytest.mark.parametrize(
        "reader",
        [
            inversion_live._log_full_utterance,
            inversion_shadow._log_full_utterance,
            preclaim_shadow._log_full_utterance,
        ],
    )
    def test_opt_in(self, knob_on, reader):
        assert reader() is True


class TestEmittedLines:
    def test_pre_classifier_logs_the_fingerprint_not_the_text_by_default(self, knob_unset):
        with capture_logs() as cap:
            PreClassifier.pre_classify(_MSG)
        inputs = [
            e for e in cap if str(e.get("event", "")).startswith("PRE_CLASSIFIER DEBUG - input")
        ]
        assert inputs, cap[:3]
        assert inputs[0]["utterance_sha256"] == _SHA
        assert "utterance" not in inputs[0]
        joined = " ".join(str(e) for e in cap)
        assert _MSG not in joined
        assert "Original:" not in joined

    def test_pre_classifier_opt_in_logs_the_text(self, knob_on):
        with capture_logs() as cap:
            PreClassifier.pre_classify(_MSG)
        joined = " ".join(str(e.get("event", "")) for e in cap)
        assert f"PRE_CLASSIFIER DEBUG - Original: '{_MSG}'" in joined


class TestSourceSweep:
    """Every known text-logging site goes through the helper, and no site
    re-reads the knob or interpolates the message into a log line."""

    _ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    def _read(self, rel):
        with open(os.path.join(self._ROOT, rel), encoding="utf-8") as fh:
            return fh.read()

    def test_only_the_helper_reads_the_knob(self):
        """No module reads the knob from os.environ by name — the helper reads
        it once through ``KNOB`` and every site calls the helper (a docstring
        that merely names the knob is not a read)."""
        assert KNOB == "PIPER_INVERSION_LOG_UTTERANCE"
        reader = re.compile(r"os\.environ\.get\(\s*[\"']PIPER_INVERSION_LOG_UTTERANCE")
        hits = []
        for dirpath, _, files in os.walk(os.path.join(self._ROOT, "services")):
            for f in files:
                if not f.endswith(".py"):
                    continue
                p = os.path.join(dirpath, f)
                with open(p, encoding="utf-8") as fh:
                    if reader.search(fh.read()):
                        hits.append(os.path.relpath(p, self._ROOT))
        assert hits == [], hits
        assert "os.environ.get(KNOB, DEFAULT)" in self._read("services/utils/utterance_log.py")

    def test_intent_service_processing_line_is_fingerprinted(self):
        src = self._read("services/intent/intent_service.py")
        assert 'self.logger.info("Processing intent", **_utterance_fields(message))' in src
        assert 'f"Processing intent: {message}"' not in src

    def test_cache_lines_no_longer_carry_a_text_prefix(self):
        src = self._read("services/intent_service/cache.py")
        # the 50-char prefix survives only inside _text_ref, under the opt-in branch
        assert src.count("{text[:50]}") == 1
        assert "if log_full_utterance() else" in src
        assert src.count("_text_ref(text)") == 5
        assert (
            "sha256={utterance_sha256(text)}" in src
        )  # stdlib logger: the digest rides the message

    def test_search_queries_are_fingerprinted(self):
        assert 'utterance_fields(query, key="query")' in self._read(
            "services/intent_service/document_handlers.py"
        )
        notion = self._read("services/domain/notion_domain_service.py")
        assert "query=query" not in notion
        assert notion.count('_utterance_fields(query, key="query")') == 3

    def test_no_log_line_interpolates_the_user_message(self):
        """A f-string log of the raw message/text/query in the intent stack
        is the shape this ruling retired. Scope: the modules that handle user
        turns; a new hit here is a new text-logging site to route through the
        helper. The three gated PRE_CLASSIFIER opt-in lines are the only
        permitted hits."""
        pattern = re.compile(
            r"logger\.(?:info|debug|warning|error)\(\s*f\"[^\"]*\{"
            r"(?:message|original_message|user_message|text|utterance|query|clean_msg|clean_for_matching)\b"
        )
        hits = []
        for rel in (
            "services/intent/intent_service.py",
            "services/intent_service/pre_classifier.py",
            "services/intent_service/cache.py",
            "services/intent_service/document_handlers.py",
            "services/intent_service/inversion_live.py",
            "services/intent_service/inversion_shadow.py",
            "services/intent_service/preclaim_shadow.py",
        ):
            src = self._read(rel)
            for m in pattern.finditer(src):
                hits.append((rel, src[: m.start()].count("\n") + 1))
        allowed = [h for h in hits if h[0].endswith("pre_classifier.py")]
        assert hits == allowed, hits
        assert len(allowed) == 3, hits
        pc = self._read("services/intent_service/pre_classifier.py")
        gate = pc.index("if log_full_utterance():")
        assert all(
            pc.index(f"PRE_CLASSIFIER DEBUG - {k}") > gate
            for k in ("Original", "Clean:", "Clean for matching")
        )


def test_helper_module_documents_every_reader():
    doc = inspect.getdoc(utterance_log) or ""
    for name in (
        "inversion_live",
        "inversion_shadow",
        "preclaim_shadow",
        "pre_classify",
        "process_intent",
        "cache",
        "search_documents",
        "Notion",
    ):
        assert name in doc
