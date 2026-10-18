"""The password-reset mint resolves the database like every other ops payload.

2026-10-18: run inside the prod container (`fly ssh console -C "python
/app/scripts/mint_password_reset_token.py dinp --apply"`) the script tried
localhost:5433 (the dev defaults behind a hard-coded dotenv path) and failed.
It now goes through ``prod_db._database_url`` (the app's own config, loud
fallback, refuses localhost in production), the same resolver
``mint_invite_tokens.py`` uses. These pins hold that.
"""

from __future__ import annotations

import importlib.util
import os
import sys

import pytest

_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
_SCRIPT = os.path.join(_ROOT, "scripts", "mint_password_reset_token.py")


@pytest.fixture
def mod():
    sys.path.insert(0, os.path.join(_ROOT, "scripts"))
    spec = importlib.util.spec_from_file_location("mint_password_reset_token_under_test", _SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_engine_resolves_through_prod_db(mod, monkeypatch, capsys):
    monkeypatch.setattr(mod, "_database_url", lambda: ("sqlite://", "a stub resolver"))
    eng = mod._engine()
    out = capsys.readouterr().out
    assert "resolved via a stub resolver" in out
    assert eng.url.drivername == "sqlite"


def test_no_hard_coded_dotenv_or_localhost_defaults():
    src = open(_SCRIPT, encoding="utf-8").read()
    assert "load_dotenv(" not in src, "the hard-coded dotenv path is the dev-only hazard"
    assert 'os.getenv("POSTGRES_HOST"' not in src, "POSTGRES_* defaults point at the dev database"
    assert "from prod_db import" in src
