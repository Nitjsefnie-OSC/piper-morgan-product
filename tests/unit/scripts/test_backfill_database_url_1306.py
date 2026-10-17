"""#1306 backfill: the script resolves its database the way the app does.

Comms, 2026-10-17: on alpha the ``--count`` line refused the connection at
127.0.0.1:5433 because ``_database_url`` built only from ``POSTGRES_*`` and
ignored ``DATABASE_URL`` (the #1278 convention alpha runs on). These pins hold
the fix: ``DATABASE_URL`` wins, the source is named, and the dev fallback is
only reached when the app config cannot be loaded.
"""

from __future__ import annotations

import importlib

mod = importlib.import_module("scripts.backfill_encrypt_files_1306")


def test_database_url_honours_explicit_database_url(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql://u:p@dbhost.internal:6543/alpha_db")
    monkeypatch.setenv("POSTGRES_HOST", "localhost")
    monkeypatch.setenv("POSTGRES_PORT", "5433")
    url, source = mod._database_url()
    assert "dbhost.internal:6543/alpha_db" in url
    assert "localhost:5433" not in url
    assert source.startswith("app config")


def test_database_url_returns_async_driver(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql://u:p@dbhost.internal:6543/alpha_db")
    url, _ = mod._database_url()
    assert url.startswith("postgresql+asyncpg://")


def test_database_url_falls_back_loudly_when_app_config_is_unavailable(monkeypatch, capsys):
    import builtins

    real_import = builtins.__import__

    def _no_app_config(name, *args, **kwargs):
        if name == "services.database.connection":
            raise ImportError("simulated: app config unavailable")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", _no_app_config)
    monkeypatch.setenv("POSTGRES_HOST", "devhost")
    monkeypatch.setenv("POSTGRES_PORT", "5433")
    monkeypatch.setenv("POSTGRES_DB", "piper_morgan")
    url, source = mod._database_url()
    assert "devhost:5433/piper_morgan" in url
    assert source == "POSTGRES_* env"
    assert "WARNING" in capsys.readouterr().err
