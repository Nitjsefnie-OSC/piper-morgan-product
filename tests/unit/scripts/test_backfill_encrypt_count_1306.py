"""The #1306 backfill's read-only ``--count`` mode (Exec, 2026-10-16: the narrow step
before a production write). Pins: classification never writes; the count loop never
consults the encryptor and leaves every byte as it was; the write loop still
encrypts plaintext and skips marked files; the printed shapes.
"""

from __future__ import annotations

import importlib

import pytest

mod = importlib.import_module("scripts.backfill_encrypt_files_1306")


class _ExplosiveEncryptor:
    def encrypt_bytes(self, data, context):  # pragma: no cover - must never run in count mode
        raise AssertionError("encryptor consulted in --count mode")


class _FakeEncryptor:
    def encrypt_bytes(self, data, context):
        assert context == mod._CONTEXT
        return b"<" + data[::-1] + b">"


def _files(tmp_path):
    plain = tmp_path / "plain.bin"
    plain.write_bytes(b"hello plaintext")
    marked = tmp_path / "marked.bin"
    marked.write_bytes(mod._MARKER_BYTES + b"ciphertext")
    missing = tmp_path / "gone.bin"
    return plain, marked, missing


def test_classify_file_is_read_only(tmp_path):
    plain, marked, missing = _files(tmp_path)
    before = {p: p.read_bytes() for p in (plain, marked)}
    assert mod.classify_file(plain) == "plaintext"
    assert mod.classify_file(marked) == "already"
    assert mod.classify_file(missing) == "missing"
    assert {p: p.read_bytes() for p in (plain, marked)} == before


def test_count_mode_never_writes_and_never_touches_the_encryptor(tmp_path):
    plain, marked, missing = _files(tmp_path)
    before = {p: p.read_bytes() for p in (plain, marked)}
    counts = mod.run_over_paths([plain, marked, missing], _ExplosiveEncryptor(), count_only=True)
    assert counts == {"plaintext": 1, "already": 1, "missing": 1}
    assert {p: p.read_bytes() for p in (plain, marked)} == before
    line = mod.format_counts(counts, count_only=True)
    assert line == (
        "uploaded files: 1 plaintext, 1 already encrypted, 1 missing-on-disk (count only, nothing written)"
    )


def test_write_mode_encrypts_plaintext_and_skips_marked(tmp_path):
    plain, marked, missing = _files(tmp_path)
    counts = mod.run_over_paths([plain, marked, missing], _FakeEncryptor(), count_only=False)
    assert counts == {"encrypted": 1, "already": 1, "missing": 1}
    assert plain.read_bytes().startswith(mod._MARKER_BYTES)
    assert marked.read_bytes() == mod._MARKER_BYTES + b"ciphertext"
    assert mod.format_counts(counts, count_only=False) == (
        "uploaded files: 1 encrypted, 1 already, 1 missing-on-disk"
    )
    # idempotent: a second pass changes nothing
    again = mod.run_over_paths([plain, marked, missing], _ExplosiveEncryptor(), count_only=False)
    assert again == {"encrypted": 0, "already": 2, "missing": 1}


def test_cli_flag_parses():
    assert mod._parse_args(["--count"]).count is True
    assert mod._parse_args([]).count is False


def test_count_mode_needs_no_key(monkeypatch):
    monkeypatch.delenv("ENCRYPTION_MASTER_KEY", raising=False)
    # require_encryptor would SystemExit; count mode must not call it.
    calls = []
    monkeypatch.setattr(
        mod, "require_encryptor", lambda: calls.append(1) or (_ for _ in ()).throw(SystemExit(1))
    )

    async def _no_rows():
        return []

    monkeypatch.setattr(mod, "_fetch_storage_paths", _no_rows)
    import asyncio

    asyncio.run(mod._main(count_only=True))
    assert calls == []
    with pytest.raises(SystemExit):
        asyncio.run(mod._main(count_only=False))
