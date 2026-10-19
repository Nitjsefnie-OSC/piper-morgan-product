# MCP app: GitHub-only decrypt subkey, no master key (#1982)

**Ruling** (Arch, 2026-10-11, decisions.log + #1982): `piper-morgan-mcp` never holds
`ENCRYPTION_MASTER_KEY`. It is handed a decrypt-only HKDF subkey for exactly the
contexts it reads. `main_mcp.py` refuses to start if the master key is present.
HOST's three conditions are acceptance criteria (#1982, second comment).

## What the MCP process reads (step 5 census, Lead 2026-10-11)

Traced from `main_mcp.py` → `services/mcp/server/app.py` and its imports:

| Read | Table / column | Encrypted context | On MCP |
|---|---|---|---|
| bearer identity (`identity.py`) | `mcp_access_tokens` | none (hash column) | plain read |
| resources / tools (`resources.py`) | `users` (id, preferences) | none | plain read |
| GitHub OAuth grant (`github_adapter.py` → `ConnectorGrantStore`) | `user_api_keys` provider `github_mcp_oauth` | `user_api_keys.secret.github` | **subkey** |
| GitHub PAT, at-rest row (`github_adapter._user_pat_at_rest`) | `user_api_keys` provider `github` | `user_api_keys.secret.github` | **subkey** |
| GitHub PAT, keychain row (`github_adapter._user_pat` → `GitHubConfigService`) | `secure_credentials` name `<uid>_github_token_api_key` | `secure_credentials.<name>` (per user) | **not readable; fails closed to None** (the at-rest row above is read first, so this path is only reached when no row exists) |
| `mcp_oauth_clients.client_secret` | — | `mcp_oauth_clients.client_secret` | **never read**: the OAuth authorization server lives in alpha (`web/routers/mcp_oauth.py`); `connections.py` is alpha's settings page. MCP only verifies bearer tokens. |

So the MCP app needs **one** context, `user_api_keys.secret.github`. Nothing else.

**PAT-only users (Arch's ruling, 2026-10-11 15:5x):** Settings → GitHub used to save the PAT only
with `KeychainService.store_api_key("github_token", token, username=<uid>)`, i.e. the hosted keychain
table under a per-user context no fixed subkey list can name, so a PAT-only user was
`CONNECT_REQUIRED` on the MCP app. Resolution: a **dual write**. The save route also stores the PAT
through `UserAPIKeyService.store_user_key(provider="github", validate=False)`
(`services/connectors/github_pat_store.py`), landing the row under the GitHub context;
`_user_pat_at_rest` reads it first. Disconnect deletes both copies. PATs saved before this landed
are copied by `scripts/backfill_github_pat_rows_1982.py` (step 2b below). The keychain copy stays
for alpha's sync readers. Landing trigger (Arch): met 2026-10-19. The PAT-only path is served: xian, signed in as a PAT-only test account through a freshly added hosted connector, got real open issues with no `CONNECT_REQUIRED`, and PA's read of the MCP app's log showed the at-rest read (`EncryptedDBCredentialStore`), all 200s and no decrypt error (#1982 comment 6276888481; #1982 closed). Accounts whose PAT was saved before the dual write still have no at-rest row until step 2b's backfill runs: #2090.

## 1. Set the secret (PM's hand; no agent sees the value)

On a machine with the master key (alpha), pipe straight into the MCP app's secrets.
`fly secrets import` reads `NAME=VALUE` lines from stdin, which is what the script
prints (one line, nothing else on stdout):

```bash
fly ssh console -a piper-morgan -C "python scripts/derive_subkey.py user_api_keys.secret.github" \
  | fly secrets import -a piper-morgan-mcp
```

Then confirm `ENCRYPTION_MASTER_KEY` is NOT among the MCP app's secret names
(`fly secrets list -a piper-morgan-mcp`). If it is, `fly secrets unset` it: the guard
will crash-loop the app otherwise, by design.

If the value ever appears in a tool output, CI log or tracked file: rotate (re-derive
after rotating the master key). Scrubbing is not a fix.

## 2. Re-encrypt the existing GitHub rows on alpha (gated; HOST condition 2)

Alpha writes new GitHub rows under the new context from the moment this lands; the
read path falls back to the legacy shared context until the re-encrypt reports zero.

```bash
# a. snapshot first — record the id
fly volumes list -a piper-morgan-db
fly volumes snapshots create <vol-id> -a piper-morgan-db
fly volumes snapshots list <vol-id> -a piper-morgan-db | head -3    # newest = just now

# b. dry run: census + decrypt + scratch re-encrypt, no writes
fly ssh console -a piper-morgan -C "python scripts/reencrypt_github_secrets_1982.py"

# c. apply, naming the snapshot; then the script re-reads every row and round-trips it
fly ssh console -a piper-morgan -C "python scripts/reencrypt_github_secrets_1982.py --apply --snapshot <snapshot-id>"
```

The script prints counts and row ids only. A non-zero exit means stop and read the
output; `--apply` refuses without `--snapshot`, refuses a `--snapshot` value that is not
shaped like a Fly snapshot id (`vs_` + alphanumerics: a pasted placeholder such as
`<snapshot-id>` is refused, since 2026-10-13), and refuses if any row is undecryptable.
It cannot check the snapshot exists (no flyctl inside the machine); the `snapshots list`
output in step a is that evidence. Run the four lines one at a time, substituting each id
from the previous line's output, not as one pasted block.

**Done 2026-10-13 16:36 PT (PM's hand):** step 1 wrote one subkey for one context; both
MCP machines healthy; `fly secrets list -a piper-morgan-mcp` names `DATABASE_URL` and
`ENCRYPTION_SCOPED_SUBKEYS` only. Step 2 dry run `total=2 new=0 legacy=2 undecryptable=0`;
apply `total=2 rewritten=2 verified_new=2 legacy=0 failed=0`. The manual snapshot was not
taken (the placeholder failed in zsh and the apply then accepted the literal placeholder,
the gap the shape check above now closes); Fly's automatic daily snapshot from six hours
before the apply holds the pre-state of both rows (5-day retention).

## 2b. Backfill PATs saved before the dual write (gated the same way)

Runs in alpha's image (holds the master key); only adds `user_api_keys` rows, the snapshot from
step 2a covers it.

```bash
fly ssh console -a piper-morgan -C "python scripts/backfill_github_pat_rows_1982.py"
fly ssh console -a piper-morgan -C "python scripts/backfill_github_pat_rows_1982.py --apply --snapshot <snapshot-id>"
```

Dry run prints `source / unparseable / no_user / already_present / to_write / undecryptable`
counts; `--apply` writes each missing row, reads it back and checks it equals the keychain value
(never printed). Non-zero exit: stop and read the ids.

## 3. Drop the legacy fallback

**Done 2026-10-13 (Lead), the commit that carries this line:** `GITHUB_LEGACY_CONTEXT_FALLBACK = False`,
count recorded on #1982 and in decisions.log; pinned by `TestLegacyFallbackIsOff`.

When step 2's final report reads `legacy=0`: set `GITHUB_LEGACY_CONTEXT_FALLBACK = False`
in `services/security/user_api_key_service.py` in the same commit that records the count
(issue comment + decisions.log). The MCP app never used the fallback: a scoped service
reports `supports("user_api_keys.secret") == False`, so the branch is skipped by
construction there, not by the flag.

## Mechanism summary

- `FieldEncryptionService.scoped({ctx: subkey})` / `ENCRYPTION_SCOPED_SUBKEYS=ctx=base64[,…]`:
  decrypt-only; unlisted context → `ScopedContextError`; any encrypt →
  `ScopedEncryptRefused` (both `DecryptionError` subclasses, so every fail-closed caller
  keeps working). Both env vars set → hard error.
- `secret_context(provider)`: `github` / `github_mcp_oauth` → `user_api_keys.secret.github`;
  everything else → `user_api_keys.secret`.
- `refuse_master_key()` in `services/mcp/server/app.py`, called from `main_mcp.main()`
  and `build_asgi_app()`; pinned by `tests/unit/services/security/test_scoped_subkeys_1982.py`.
