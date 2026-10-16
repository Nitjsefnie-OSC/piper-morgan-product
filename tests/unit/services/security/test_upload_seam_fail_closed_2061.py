"""#2061 — the uploaded-file write seam fails closed on a hosted app.

Mirrors the encrypted columns (#1387): no ENCRYPTION_MASTER_KEY + production
(PIPER_ENVIRONMENT/ENVIRONMENT == "production") refuses; dev/test keeps the
plaintext fallback.
"""

import base64
import os
from unittest.mock import MagicMock, patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from services.auth.auth_middleware import get_current_user
from services.file_context.storage import (
    StorageEncryptionUnavailable,
    read_file_from_storage,
    write_file_to_storage,
)
from services.security.encrypted_types import MARKER


@pytest.fixture(autouse=True)
def _clean_env(monkeypatch):
    monkeypatch.delenv("ENCRYPTION_MASTER_KEY", raising=False)
    monkeypatch.delenv("ENVIRONMENT", raising=False)
    monkeypatch.delenv("PIPER_ENVIRONMENT", raising=False)


@pytest.mark.parametrize("var", ["PIPER_ENVIRONMENT", "ENVIRONMENT"])
def test_keyless_production_write_refuses_and_writes_nothing(monkeypatch, tmp_path, var):
    monkeypatch.setenv(var, "production")
    p = tmp_path / "doc.pdf"
    with pytest.raises(StorageEncryptionUnavailable):
        write_file_to_storage(p, b"secret")
    assert not p.exists()


def test_error_is_the_columns_error_class(monkeypatch, tmp_path):
    monkeypatch.setenv("PIPER_ENVIRONMENT", "production")
    with pytest.raises(RuntimeError):
        write_file_to_storage(tmp_path / "x", b"y")


def test_keyed_production_still_encrypts(monkeypatch, tmp_path):
    monkeypatch.setenv("PIPER_ENVIRONMENT", "production")
    monkeypatch.setenv("ENCRYPTION_MASTER_KEY", base64.b64encode(os.urandom(32)).decode())
    p = tmp_path / "doc.pdf"
    write_file_to_storage(p, b"secret")
    assert p.read_bytes().startswith(MARKER.encode("ascii"))
    assert read_file_from_storage(p) == b"secret"


def test_dev_without_key_still_writes(tmp_path):
    p = tmp_path / "doc.pdf"
    write_file_to_storage(p, b"dev")
    assert p.read_bytes() == b"dev"


def test_legacy_plaintext_read_unchanged_in_production(monkeypatch, tmp_path):
    monkeypatch.setenv("PIPER_ENVIRONMENT", "production")
    p = tmp_path / "legacy.pdf"
    p.write_bytes(b"legacy plaintext")
    assert read_file_from_storage(p) == b"legacy plaintext"


def test_upload_route_returns_503_when_writer_refuses(tmp_path):
    from web.api.routes import files as files_routes

    app = FastAPI()
    app.include_router(files_routes.router)
    claims = MagicMock()
    claims.sub = "user-1"
    app.dependency_overrides[get_current_user] = lambda: claims
    with (
        patch.object(files_routes, "get_upload_base", return_value=tmp_path),
        patch.object(
            files_routes,
            "write_file_to_storage",
            side_effect=StorageEncryptionUnavailable("no key"),
        ),
    ):
        r = TestClient(app).post(
            "/api/v1/files/upload",
            files={"file": ("a.txt", b"hello", "text/plain")},
        )
    assert r.status_code == 503
    assert "can't store files" in r.json()["detail"]
