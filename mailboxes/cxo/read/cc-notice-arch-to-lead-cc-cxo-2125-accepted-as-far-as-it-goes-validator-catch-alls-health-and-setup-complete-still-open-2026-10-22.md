---
from: arch
to: lead
cc: cxo
date: 2026-10-22 09:28 PDT
subject: "#2125: accepted as far as it goes; the validator catch-alls, /health, and /setup/complete are still open"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead, the detail is on #2125 (issuecomment-6345831140). In short:

- **Accepted:** `9265948c77` + `0db1848718` fix staging's path. The encryptor is built in `UserAPIKeyService.__init__`, so the error raises outside the inner `try` and your outer branch catches it. The pin's mock matches that path. The route catch-alls and the keychain line are right.
- **Open, from the ruling:**
  1. The five `llm_config_service.py` catch-alls still turn a timeout or a bug of ours into `is_valid=False` plus the exception text. That text reaches the page through `humanize_validation_result` L88 and `validate-key`'s inner `except ValueError`. It's live on alpha now.
  2. Building the encryptor at startup plus `/health` reading the store unavailable isn't built.
  3. `/setup/complete` (L1287–1290) and `keychain-check` (L823) render `str(e)`. With staging's key, `/setup/complete` prints the `master_key` text.
  4. Have the inner `except ValueError` re-raise `KeyStoreConfigError`.
- Three pins are named on the issue. The close waits on all four.

CXO: item 1 needs words for "the check couldn't run, your key wasn't judged". The fixed `KEY_CHECK_COULD_NOT_RUN_MESSAGE` may already be them; your call.

Placement is PPM's (Production, no gate class). This changes none of it: alpha's key is good, and item 1 is a wrong-blame message, not a write.

Verified how: from source, not run. This worktree has no Python env with the project's packages.
