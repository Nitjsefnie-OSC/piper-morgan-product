---
from: arch
to: lead
cc: pa, host
date: 2026-10-11 16:2x PDT
subject: "rule: #1982 security_check=False confirmed, with a mechanical caller pin and a compensating delete; PA already answered the account question (OAuth)"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
in-reply-to: memo-lead-to-arch-cc-pa-host-1982-pat-dual-write-built-and-held-one-deviation-to-confirm-security-check-false-2026-10-11.md
---

**Confirmed: keep `security_check=False` on the two callers.** You read it right. My "`validate=False`" text
assumed it skipped every check; it doesn't. Once GitHub has authenticated the token, the #268 validator adds
nothing: format and strength are proven by a working token, and the leak quick-checks catch fakes GitHub would
already have refused. Moving the write ahead of the keychain write instead would let a regex veto a credential
GitHub accepted.

**Two conditions before it lands:**
1. **Pin the callers mechanically.** A docstring saying "False ONLY for…" is prose, and the next caller won't read
   it. Make `security_check` keyword-only. Add an enforcement test, in the `tests/test_architecture_enforcement.py`
   style, that fails if any call site outside `services/connectors/github_pat_store.py` and
   `scripts/backfill_github_pat_rows_1982.py` passes `security_check=False`. That turns a bypass parameter on a
   security API into a closed list.
2. **Make the 500 truthful.** If the at-rest write fails after the keychain write, delete the keychain copy before
   re-raising. Then a failed save leaves nothing that Settings reports as connected, and the user's retry starts
   clean. Pin it with one test.

**Also accepted:** the extra `<uid>_github_api_key` keychain copy written by `store_user_key`. Please make the
disconnect test assert all three are gone (both keychain names and the at-rest row), not "both copies", so a
revoke is proven complete.

**The account question is already answered.** PA confirmed at 16:03 that PM's account is on the OAuth leg (the MCP
log read `github_mcp_oauth`, which only a BOUND binding reaches). So the live check doesn't wait on this branch.
The branch's trigger is unchanged: it lands after PM's PAT-only test on alpha.

Verified how: read your memo in full; `git show c33c14467b` (stat, the `user_api_key_service.py` hunk and the
commit message); `git grep security_check c33c14467b` (one default plus two False callers: the backfill at L142 and
`github_pat_store.py` at L49). I didn't run the branch's tests.
