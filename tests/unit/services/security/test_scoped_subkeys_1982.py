"""#1982 — no master key on the MCP app: scoped decrypt-only subkeys, the GitHub-only
HKDF context, the gated legacy fallback, and the main_mcp.py master-key guard.

Arch's ruling (2026-10-11) plus HOST's three conditions (adopted as acceptance criteria).
LAYER (m-43): the encryption primitive and the key service's context routing are
exercised directly; the guard is exercised through ``build_asgi_app()`` (the same
function uvicorn is handed) and ``main_mcp.main()`` with ``uvicorn.run`` stubbed, so
a process that reached the server would be a test failure, not a silent pass.
DENOMINATOR: unit level — the re-encrypt script's phase logic is covered on a
fixture of tokens; its SQL runs only on alpha, by PM's hand.
"""

from __future__ import annotations

import base64
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock

import pytest

from services.security import user_api_key_service as uaks
from services.security.field_encryption import (
    ENV_MASTER_KEY,
    ENV_SCOPED_SUBKEYS,
    DecryptionError,
    FieldEncryptionService,
    ScopedContextError,
    ScopedEncryptRefused,
    format_scoped_subkeys,
    parse_scoped_subkeys,
)
from services.security.user_api_key_service import (
    GITHUB_PROVIDERS,
    GITHUB_SECRET_CONTEXT,
    USER_SECRET_CONTEXT,
    UserAPIKeyService,
    secret_context,
)

MASTER = bytes(range(32))
MASTER_B64 = base64.b64encode(MASTER).decode()


def _master() -> FieldEncryptionService:
    return FieldEncryptionService(MASTER)


def _github_scoped() -> FieldEncryptionService:
    """What the MCP app holds: the GitHub subkey and nothing else."""
    return FieldEncryptionService.scoped(
        {GITHUB_SECRET_CONTEXT: _master().export_subkey(GITHUB_SECRET_CONTEXT)}
    )


# ── the primitive ────────────────────────────────────────────────────────────


class TestScopedService:
    def test_scoped_decrypts_only_its_context(self):
        token = _master().encrypt("ghp_abc", GITHUB_SECRET_CONTEXT)
        assert _github_scoped().decrypt(token, GITHUB_SECRET_CONTEXT) == "ghp_abc"

    def test_scoped_refuses_an_unlisted_context_by_name(self):
        token = _master().encrypt("sk-ant-x", USER_SECRET_CONTEXT)
        with pytest.raises(ScopedContextError):
            _github_scoped().decrypt(token, USER_SECRET_CONTEXT)
        with pytest.raises(ScopedContextError):
            _github_scoped().decrypt_bytes(b"\x00" * 40, "artifacts.content")

    def test_scoped_context_error_is_a_decryption_error(self):
        """Existing fail-closed callers catch DecryptionError; the new error must land there."""
        assert issubclass(ScopedContextError, DecryptionError)
        assert issubclass(ScopedEncryptRefused, DecryptionError)

    def test_scoped_refuses_every_encrypt(self):
        with pytest.raises(ScopedEncryptRefused):
            _github_scoped().encrypt("x", GITHUB_SECRET_CONTEXT)
        with pytest.raises(ScopedEncryptRefused):
            _github_scoped().encrypt_bytes(b"x", GITHUB_SECRET_CONTEXT)

    def test_scoped_cannot_export(self):
        with pytest.raises(ScopedContextError):
            _github_scoped().export_subkey(GITHUB_SECRET_CONTEXT)

    def test_supports(self):
        assert _master().supports(USER_SECRET_CONTEXT)
        assert _github_scoped().supports(GITHUB_SECRET_CONTEXT)
        assert not _github_scoped().supports(USER_SECRET_CONTEXT)

    def test_export_matches_derivation(self):
        """The exported subkey IS the HKDF subkey: a scoped holder and the master agree
        on ciphertext for the same context, and on nothing else."""
        sub = _master().export_subkey(GITHUB_SECRET_CONTEXT)
        other = _master().export_subkey(USER_SECRET_CONTEXT)
        assert len(sub) == 32 and sub != other
        token = _master().encrypt("ghp_x", GITHUB_SECRET_CONTEXT)
        assert (
            FieldEncryptionService.scoped({GITHUB_SECRET_CONTEXT: sub}).decrypt(
                token, GITHUB_SECRET_CONTEXT
            )
            == "ghp_x"
        )

    def test_repr_never_shows_key_material(self):
        sub = _master().export_subkey(GITHUB_SECRET_CONTEXT)
        text = repr(FieldEncryptionService.scoped({GITHUB_SECRET_CONTEXT: sub}))
        assert base64.b64encode(sub).decode() not in text
        assert sub.hex() not in text
        assert GITHUB_SECRET_CONTEXT in text

    def test_scoped_rejects_bad_keys(self):
        with pytest.raises(ValueError):
            FieldEncryptionService.scoped({})
        with pytest.raises(ValueError):
            FieldEncryptionService.scoped({"c": b"short"})
        with pytest.raises(ValueError):
            FieldEncryptionService.scoped({"": bytes(32)})


class TestScopedEnvFormat:
    def test_round_trip(self):
        keys = {GITHUB_SECRET_CONTEXT: bytes([7]) * 32, "other.ctx": bytes([9]) * 32}
        assert parse_scoped_subkeys(format_scoped_subkeys(keys)) == keys

    def test_one_line_no_whitespace(self):
        line = format_scoped_subkeys({GITHUB_SECRET_CONTEXT: bytes(32)})
        assert "\n" not in line and " " not in line

    @pytest.mark.parametrize(
        "raw",
        [
            "",
            "   ",
            "noequals",
            "=abc",
            "ctx=",
            "ctx=not-base64!",
            "ctx=" + base64.b64encode(b"short").decode(),
        ],
    )
    def test_malformed_is_a_config_error_naming_the_var(self, raw):
        with pytest.raises(ValueError) as ei:
            parse_scoped_subkeys(raw)
        assert ENV_SCOPED_SUBKEYS in str(ei.value)

    def test_duplicate_context_rejected(self):
        one = f"{GITHUB_SECRET_CONTEXT}={base64.b64encode(bytes(32)).decode()}"
        with pytest.raises(ValueError):
            parse_scoped_subkeys(f"{one},{one}")

    def test_from_env_scoped_mode(self, monkeypatch):
        monkeypatch.delenv(ENV_MASTER_KEY, raising=False)
        sub = _master().export_subkey(GITHUB_SECRET_CONTEXT)
        monkeypatch.setenv(ENV_SCOPED_SUBKEYS, format_scoped_subkeys({GITHUB_SECRET_CONTEXT: sub}))
        svc = FieldEncryptionService.from_env()
        assert svc is not None and svc.is_scoped
        token = _master().encrypt("ghp_env", GITHUB_SECRET_CONTEXT)
        assert svc.decrypt(token, GITHUB_SECRET_CONTEXT) == "ghp_env"

    def test_from_env_master_mode_unchanged(self, monkeypatch):
        monkeypatch.delenv(ENV_SCOPED_SUBKEYS, raising=False)
        monkeypatch.setenv(ENV_MASTER_KEY, MASTER_B64)
        svc = FieldEncryptionService.from_env()
        assert svc is not None and not svc.is_scoped

    def test_from_env_neither_is_none(self, monkeypatch):
        monkeypatch.delenv(ENV_SCOPED_SUBKEYS, raising=False)
        monkeypatch.delenv(ENV_MASTER_KEY, raising=False)
        assert FieldEncryptionService.from_env() is None

    def test_from_env_both_set_is_a_hard_error(self, monkeypatch):
        monkeypatch.setenv(ENV_MASTER_KEY, MASTER_B64)
        monkeypatch.setenv(ENV_SCOPED_SUBKEYS, format_scoped_subkeys({"c": bytes(32)}))
        with pytest.raises(ValueError):
            FieldEncryptionService.from_env()


# ── the key service's context routing ────────────────────────────────────────


class TestSecretContext:
    def test_github_providers_get_their_own_context(self):
        assert GITHUB_PROVIDERS == frozenset({"github", "github_mcp_oauth"})
        for p in GITHUB_PROVIDERS:
            assert secret_context(p) == GITHUB_SECRET_CONTEXT
        for p in ("anthropic", "openai", "notion", "slack_mcp_oauth"):
            assert secret_context(p) == USER_SECRET_CONTEXT

    def test_contexts_are_distinct_labels(self):
        assert GITHUB_SECRET_CONTEXT != USER_SECRET_CONTEXT
        assert GITHUB_SECRET_CONTEXT.startswith(USER_SECRET_CONTEXT + ".")


def _service(enc) -> UserAPIKeyService:
    keychain = MagicMock()
    keychain.get_api_key.return_value = None
    return UserAPIKeyService(keychain_service=keychain, field_encryption_service=enc)


def _session_with_row(token: str, provider: str):
    row = SimpleNamespace(encrypted_secret=token, key_reference="ref", provider=provider)
    result = MagicMock()
    result.scalar_one_or_none.return_value = row
    session = MagicMock()
    session.execute = AsyncMock(return_value=result)
    return session


class TestKeyServiceReads:
    @pytest.mark.asyncio
    @pytest.mark.parametrize("provider", sorted(GITHUB_PROVIDERS))
    async def test_new_context_row_reads_on_master_and_on_scoped(self, provider):
        token = _master().encrypt("ghp_new", GITHUB_SECRET_CONTEXT)
        for enc in (_master(), _github_scoped()):
            got = await _service(enc).retrieve_user_key(
                _session_with_row(token, provider), "u", provider
            )
            assert got == "ghp_new"

    @pytest.mark.asyncio
    async def test_legacy_github_row_falls_back_on_master_only(self, monkeypatch):
        """A pre-split row (legacy shared context) still reads on alpha (master mode)…"""
        monkeypatch.setattr(uaks, "GITHUB_LEGACY_CONTEXT_FALLBACK", True)
        token = _master().encrypt("ghp_old", USER_SECRET_CONTEXT)
        assert (
            await _service(_master()).retrieve_user_key(
                _session_with_row(token, "github"), "u", "github"
            )
            == "ghp_old"
        )
        # …and NOT on the MCP app: it never holds the legacy subkey (HOST condition 2).
        assert (
            await _service(_github_scoped()).retrieve_user_key(
                _session_with_row(token, "github"), "u", "github"
            )
            is None
        )

    @pytest.mark.asyncio
    async def test_fallback_flag_off_stops_legacy_reads_everywhere(self, monkeypatch):
        monkeypatch.setattr(uaks, "GITHUB_LEGACY_CONTEXT_FALLBACK", False)
        token = _master().encrypt("ghp_old", USER_SECRET_CONTEXT)
        assert (
            await _service(_master()).retrieve_user_key(
                _session_with_row(token, "github"), "u", "github"
            )
            is None
        )

    @pytest.mark.asyncio
    async def test_non_github_rows_never_try_the_github_context(self):
        """An Anthropic key under the shared context reads on alpha; on the MCP app it is
        refused (the scoped service holds no shared subkey) and never reaches the plaintext."""
        token = _master().encrypt("sk-ant-x", USER_SECRET_CONTEXT)
        assert (
            await _service(_master()).retrieve_user_key(
                _session_with_row(token, "anthropic"), "u", "anthropic"
            )
            == "sk-ant-x"
        )
        assert (
            await _service(_github_scoped()).retrieve_user_key(
                _session_with_row(token, "anthropic"), "u", "anthropic"
            )
            is None
        )

    @pytest.mark.asyncio
    async def test_github_key_written_under_github_context_is_unreadable_as_shared(self):
        """The write side: a GitHub secret stored by the service decrypts under the GitHub
        context only (so the shared-context subkey cannot read it, and vice versa)."""
        enc = _master()
        token = enc.encrypt("ghp_w", secret_context("github"))
        with pytest.raises(DecryptionError):
            enc.decrypt(token, USER_SECRET_CONTEXT)
        assert enc.decrypt(token, GITHUB_SECRET_CONTEXT) == "ghp_w"


# ── the guard (HOST condition 4) ─────────────────────────────────────────────


class TestMasterKeyGuard:
    def test_refuse_master_key_fires_on_presence(self):
        from services.mcp.server.app import refuse_master_key

        with pytest.raises(RuntimeError) as ei:
            refuse_master_key({ENV_MASTER_KEY: MASTER_B64})
        assert "1982" in str(ei.value)
        refuse_master_key({})  # absent → silent
        refuse_master_key({ENV_MASTER_KEY: ""})  # empty → silent (unset, not present)

    def test_build_asgi_app_does_not_carry_the_guard(self, monkeypatch):
        """The guard lives at the process entrypoint, not in the app factory: the
        suite builds this app in a process that carries a test master key for the
        alpha-side tests (CI exports one), and a factory-level guard turned 28 MCP
        server tests red on main. Pin the placement so it is not re-added by reflex."""
        from services.mcp.server.app import build_asgi_app

        monkeypatch.setenv(ENV_MASTER_KEY, MASTER_B64)
        assert build_asgi_app() is not None

    def test_main_mcp_refuses_before_serving(self, monkeypatch):
        import main_mcp

        monkeypatch.setenv(ENV_MASTER_KEY, MASTER_B64)
        served = []
        monkeypatch.setattr(main_mcp.uvicorn, "run", lambda *a, **k: served.append(1))
        with pytest.raises(RuntimeError):
            main_mcp.main()
        assert served == [], "uvicorn.run must never be reached with the master key present"


# ── the re-encrypt script's classification (phase logic on a token fixture) ───


def _load_reencrypt_script():
    """Load scripts/reencrypt_github_secrets_1982.py as a module (registered in
    sys.modules first: its dataclass resolves annotations through the module dict)."""
    import importlib.util
    import sys
    from pathlib import Path

    name = "reencrypt_github_secrets_1982_under_test"
    spec = importlib.util.spec_from_file_location(
        name, Path("scripts/reencrypt_github_secrets_1982.py")
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


class TestReencryptClassify:
    def test_classify(self):
        mod = _load_reencrypt_script()
        enc = _master()
        new = enc.encrypt("a", GITHUB_SECRET_CONTEXT)
        old = enc.encrypt("a", USER_SECRET_CONTEXT)
        junk = FieldEncryptionService(bytes([5]) * 32).encrypt("a", USER_SECRET_CONTEXT)
        assert mod.classify(enc, new, GITHUB_SECRET_CONTEXT, USER_SECRET_CONTEXT) == "new"
        assert mod.classify(enc, old, GITHUB_SECRET_CONTEXT, USER_SECRET_CONTEXT) == "legacy"
        assert (
            mod.classify(enc, junk, GITHUB_SECRET_CONTEXT, USER_SECRET_CONTEXT) == "undecryptable"
        )

    def test_apply_without_snapshot_is_refused_before_any_db_work(self, monkeypatch):
        mod = _load_reencrypt_script()
        monkeypatch.setenv(ENV_MASTER_KEY, MASTER_B64)
        monkeypatch.delenv(ENV_SCOPED_SUBKEYS, raising=False)
        assert mod.run(apply=True, snapshot=None) == 2
