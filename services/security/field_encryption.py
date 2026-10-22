"""#358 SEC-ENCRYPT-ATREST — field-level encryption (AES-256-GCM, HKDF per-field).

One reusable primitive for the per-user secret store (#1185 floor) and, later, the
content/PII fields. AES-256-GCM gives **authenticated** encryption (confidentiality +
tamper-detection via the GCM tag). A per-field subkey is derived from the master key via
HKDF-SHA256 keyed by a context label, so a compromise/rotation of one field's subkey does
not cross-contaminate others. The master key comes from ``ENCRYPTION_MASTER_KEY``
(KEK-from-env now; AWS-KMS is the later path, #482).

Two modes (#1982, Arch's ruling 2026-10-11):

- **master mode** (``ENCRYPTION_MASTER_KEY``): every context derives on demand; encrypt
  and decrypt both work. This is the alpha web app.
- **scoped mode** (``ENCRYPTION_SCOPED_SUBKEYS``, no master key): the process holds
  only the pre-derived subkeys it was handed, decrypts only those contexts, and
  refuses every encrypt and every unlisted context with a named error. This is the
  MCP app, which reads a user's GitHub credential and nothing else. The master key
  never travels to it; ``scripts/derive_subkey.py`` on an alpha machine produces the
  value and PM pipes it straight into the MCP app's secrets.

Security properties (load-bearing — keep them):
- the master key, derived subkeys, nonce, and plaintext are **never logged** (repr is key-safe);
- a **unique random nonce** per encryption (never reuse under one key);
- a wrong key / wrong context / tampered token **raises** ``DecryptionError`` — never
  returns garbage plaintext;
- scoped mode **fails closed**: an unlisted context raises ``ScopedContextError`` and an
  encrypt raises ``ScopedEncryptRefused`` (both ``DecryptionError`` subclasses so the
  existing fail-closed callers keep working unchanged).
"""

from __future__ import annotations

import base64
import os
from typing import Any, Dict, Mapping, Optional

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

_KEY_LEN = 32  # AES-256
_NONCE_LEN = 12  # AES-GCM standard nonce length

ENV_MASTER_KEY = "ENCRYPTION_MASTER_KEY"
# #1982: ``context=base64subkey[,context=base64subkey...]`` — one line, so it can be
# piped from scripts/derive_subkey.py into ``fly secrets import`` without a seat
# ever printing it.
ENV_SCOPED_SUBKEYS = "ENCRYPTION_SCOPED_SUBKEYS"


class KeyStoreConfigError(ValueError):
    """#2125: the process cannot encrypt because its key configuration is unusable
    (a master key of the wrong length or encoding, both modes set, a bad scoped
    subkey). A ValueError still, so existing handlers and pins hold; routes that
    face a person catch this type and say the server can't store keys, never the
    parameter."""


class DecryptionError(Exception):
    """Raised when a token can't be decrypted (wrong key/context, or tampered)."""


class ScopedContextError(DecryptionError):
    """#1982: a scoped (decrypt-only) service was asked for a context it does not hold."""


class ScopedEncryptRefused(DecryptionError):
    """#1982: a scoped (decrypt-only) service was asked to encrypt. It never can."""


class FieldEncryptionService:
    """AES-256-GCM field encryptor with HKDF per-field subkeys.

    Token format = ``base64(nonce ‖ ciphertext+tag)``. The ``context`` label
    (e.g. ``"user_api_keys.secret"``) selects an HKDF-derived subkey, so one master
    key safely protects many independent fields.
    """

    def __init__(self, master_key: bytes):
        if not isinstance(master_key, (bytes, bytearray)) or len(master_key) != _KEY_LEN:
            got = (
                f"{len(master_key)} bytes"
                if isinstance(master_key, (bytes, bytearray))
                else type(master_key).__name__
            )
            raise KeyStoreConfigError(f"master_key must be {_KEY_LEN} bytes (AES-256); got {got}")
        self._master_key: Optional[bytes] = bytes(master_key)
        self._scoped: Optional[Dict[str, bytes]] = None

    # -- construction -----------------------------------------------------------

    @classmethod
    def scoped(cls, subkeys: Mapping[str, bytes]) -> "FieldEncryptionService":
        """#1982: a decrypt-only service holding exactly ``subkeys`` (context → 32-byte
        subkey). No master key exists in this process; nothing can be derived."""
        if not subkeys:
            raise KeyStoreConfigError("scoped FieldEncryptionService needs at least one context")
        held: Dict[str, bytes] = {}
        for context, key in subkeys.items():
            if not context:
                raise KeyStoreConfigError("scoped subkey context label must be non-empty")
            if not isinstance(key, (bytes, bytearray)) or len(key) != _KEY_LEN:
                raise KeyStoreConfigError(f"scoped subkey for {context!r} must be {_KEY_LEN} bytes")
            held[context] = bytes(key)
        svc = cls.__new__(cls)
        svc._master_key = None
        svc._scoped = held
        return svc

    @classmethod
    def from_env(
        cls, env_var: str = ENV_MASTER_KEY, scoped_env_var: str = ENV_SCOPED_SUBKEYS
    ) -> Optional["FieldEncryptionService"]:
        """Build from the environment, or ``None`` if neither variable is set.

        ``ENCRYPTION_MASTER_KEY`` (base64, 32 bytes) → master mode.
        ``ENCRYPTION_SCOPED_SUBKEYS`` (``ctx=base64[,ctx=base64...]``) → scoped mode.
        Both set is a hard config error: a process is one or the other (#1982).

        ``None`` lets callers fall back gracefully (e.g. local dev without the env
        var → the OS keychain), rather than hard-failing.
        """
        raw = os.getenv(env_var)
        raw_scoped = os.getenv(scoped_env_var)
        if raw and raw_scoped:
            raise KeyStoreConfigError(
                f"{env_var} and {scoped_env_var} are both set; a process holds the master "
                "key or scoped subkeys, never both (#1982)"
            )
        if raw_scoped:
            return cls.scoped(parse_scoped_subkeys(raw_scoped, env_var=scoped_env_var))
        if not raw:
            return None
        try:
            key = base64.b64decode(raw)
        except Exception as e:  # a malformed env value is a hard config error
            raise KeyStoreConfigError(f"{env_var} is not valid base64") from e
        return cls(key)

    # -- mode + key access ------------------------------------------------------

    @property
    def is_scoped(self) -> bool:
        return self._scoped is not None

    def supports(self, context: str) -> bool:
        """Can this service decrypt ``context``? Master mode: always. Scoped mode: only
        a held context. Callers use this to keep a fallback context off a process that
        was deliberately never given it (#1982, the legacy GitHub fallback)."""
        if self._scoped is None:
            return True
        return context in self._scoped

    def _subkey(self, context: str) -> bytes:
        if self._scoped is not None:
            try:
                return self._scoped[context]
            except KeyError:
                raise ScopedContextError(
                    f"scoped encryption service holds no subkey for context {context!r}"
                ) from None
        assert self._master_key is not None
        hkdf = HKDF(
            algorithm=hashes.SHA256(),
            length=_KEY_LEN,
            salt=None,
            info=context.encode("utf-8"),
        )
        return hkdf.derive(self._master_key)

    def export_subkey(self, context: str) -> bytes:
        """#1982: the derived subkey for ``context``, for handing to a scoped process.
        Master mode only; a scoped service re-exporting would widen its own scope.
        The caller is responsible for never printing, logging or committing the value
        (scripts/derive_subkey.py writes it to stdout once, for a pipe)."""
        if self._scoped is not None:
            raise ScopedContextError("a scoped encryption service cannot export subkeys")
        return self._subkey(context)

    # -- encrypt / decrypt ------------------------------------------------------

    def _refuse_encrypt_if_scoped(self) -> None:
        if self._scoped is not None:
            raise ScopedEncryptRefused("scoped encryption service is decrypt-only (#1982)")

    def encrypt(self, plaintext: str, context: str) -> str:
        self._refuse_encrypt_if_scoped()
        aes = AESGCM(self._subkey(context))
        nonce = os.urandom(_NONCE_LEN)
        ct = aes.encrypt(nonce, plaintext.encode("utf-8"), None)
        return base64.b64encode(nonce + ct).decode("ascii")

    def encrypt_bytes(self, plaintext: bytes, context: str) -> bytes:
        """#1306: bytes-native sibling of encrypt() for file content — same
        AES-256-GCM + per-context HKDF subkey; raw binary out (nonce + ct),
        no base64 (files are stored as bytes, not text columns)."""
        self._refuse_encrypt_if_scoped()
        aes = AESGCM(self._subkey(context))
        nonce = os.urandom(_NONCE_LEN)
        return nonce + aes.encrypt(nonce, plaintext, None)

    def decrypt_bytes(self, blob: bytes, context: str) -> bytes:
        """#1306: bytes-native sibling of decrypt(). Raises DecryptionError on
        tamper/wrong-key/short input, mirroring decrypt()'s contract."""
        aes = AESGCM(self._subkey(context))  # ScopedContextError propagates by name
        try:
            nonce, ct = blob[:_NONCE_LEN], blob[_NONCE_LEN:]
            return aes.decrypt(nonce, ct, None)
        except (InvalidTag, ValueError) as e:
            raise DecryptionError(f"file-content decryption failed: {type(e).__name__}") from e

    def decrypt(self, token: str, context: str) -> str:
        aes = AESGCM(self._subkey(context))  # ScopedContextError propagates by name
        try:
            raw = base64.b64decode(token)
            nonce, ct = raw[:_NONCE_LEN], raw[_NONCE_LEN:]
            return aes.decrypt(nonce, ct, None).decode("utf-8")
        except (InvalidTag, ValueError) as e:
            raise DecryptionError("decryption failed (wrong key/context or tampered token)") from e

    def __repr__(self) -> str:  # never expose key material
        if self._scoped is not None:
            return f"<FieldEncryptionService scoped contexts={sorted(self._scoped)}>"
        return f"<FieldEncryptionService key=***{_KEY_LEN}B>"


def parse_scoped_subkeys(raw: str, env_var: str = ENV_SCOPED_SUBKEYS) -> Dict[str, bytes]:
    """``ctx=base64[,ctx=base64...]`` → {ctx: 32-byte key}. Malformed input is a hard
    config error naming the variable, never the value."""
    out: Dict[str, bytes] = {}
    for item in raw.split(","):
        item = item.strip()
        if not item:
            continue
        context, sep, b64 = item.partition("=")
        context = context.strip()
        if not sep or not context or not b64.strip():
            raise ValueError(f"{env_var}: expected 'context=base64' entries")
        try:
            key = base64.b64decode(b64.strip(), validate=True)
        except Exception as e:
            raise ValueError(f"{env_var}: subkey for {context!r} is not valid base64") from e
        if len(key) != _KEY_LEN:
            raise ValueError(f"{env_var}: subkey for {context!r} must be {_KEY_LEN} bytes")
        if context in out:
            raise ValueError(f"{env_var}: context {context!r} listed twice")
        out[context] = key
    if not out:
        raise ValueError(f"{env_var} is set but holds no entries")
    return out


def format_scoped_subkeys(subkeys: Mapping[str, bytes]) -> str:
    """Inverse of :func:`parse_scoped_subkeys`: one line, ready for a secrets pipe."""
    return ",".join(
        f"{context}={base64.b64encode(key).decode('ascii')}" for context, key in subkeys.items()
    )


# -- #2125: the credential store's readiness, probed once per process ----------------------
# Built at startup (web/startup.py) and read by /health, so a box whose master key is unusable
# reads degraded before anyone presses Validate, and the promote gate's health refusal holds.
# Boot is never refused: a local dev box without the variable falls back to the OS keychain.
_CREDENTIAL_STORE_STATUS: Optional[Dict[str, Any]] = None


def probe_credential_store(force: bool = False) -> Dict[str, Any]:
    """Return {"status": healthy|unavailable|not_configured, "error_type": str|None}.

    Cached per process; a secret change restarts the process, so one probe is enough.
    Never raises: /health must answer whatever the configuration looks like.
    """
    global _CREDENTIAL_STORE_STATUS
    if _CREDENTIAL_STORE_STATUS is not None and not force:
        return _CREDENTIAL_STORE_STATUS
    try:
        svc = FieldEncryptionService.from_env()
        status = {"status": "healthy" if svc is not None else "not_configured", "error_type": None}
    except KeyStoreConfigError as e:
        status = {"status": "unavailable", "error_type": type(e).__name__}
    except Exception as e:  # a surprise is still "unavailable", never a crash
        status = {"status": "unavailable", "error_type": type(e).__name__}
    _CREDENTIAL_STORE_STATUS = status
    return status


def reset_credential_store_probe() -> None:
    """Tests only."""
    global _CREDENTIAL_STORE_STATUS
    _CREDENTIAL_STORE_STATUS = None
