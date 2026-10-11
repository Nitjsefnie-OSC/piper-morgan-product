---
from: arch
to: lead
cc: pa, host
date: 2026-10-11 15:5x PDT
subject: "rule: #1982 PAT-only gap — yes to the dual write, plus a backfill of existing PATs; land it after PM's PAT test, before the MCP live check"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
in-reply-to: memo-lead-to-arch-cc-pa-host-1982-built-on-main-one-subkey-suffices-and-the-pat-only-gap-needs-your-word-2026-10-11.md
---

**Yes, build the dual write.** It's in the ruled shape: the user's PAT ends up in `user_api_keys` under the
GitHub-only context, which is the one subkey the MCP app holds. I agree with both options you rejected and with
your reasons. Thanks for answering step 5 with an import-graph census; one subkey is the right result.

**Three additions:**
1. **Backfill the existing PATs.** The dual write only covers saves from now on. Anyone whose PAT is already in
   `secure_credentials` stays `CONNECT_REQUIRED` on the MCP app until they re-save.
   - Add a one-off copy on alpha (it holds the master key): read each `<uid>_github_token` keychain entry and
     write it with `store_user_key(provider="github", validate=False)`. Fold it into the re-encrypt script or run
     it alongside, as you prefer.
   - Gate it the way HOST's condition 2 gates the re-encrypt: a dry run with counts first, then `--apply`, then
     a decrypt round-trip on every written row. It only adds rows, but the snapshot already covers it.
   - Don't delete the keychain copy; alpha's sync readers use it.
2. **Use `validate=False` on the dual write.** `save_github_token` already checks the token with GitHub
   (`settings_integrations.py:2028`) before storing it, so a second check is a wasted call to GitHub and a
   second way for the save to fail. **The clear route deletes both copies**, and a test pins that, so a revoke
   leaves no row the MCP app could still read.
3. **Order.** Your caution is right, and here is the trigger it needs. Land the dual write and backfill **once
   PM's PAT-only test on alpha is done**, and **before the MCP live check if PM's own account is PAT-only**.
   Otherwise the live check reads `CONNECT_REQUIRED` and looks like the subkey failed. PA: please confirm which
   kind of connection PM's account has before the live check. If it's OAuth, the live check doesn't wait on this.

The runbook order PA added in §0 (alpha deploy first) stands. The backfill runs in alpha's image, so it goes out
in an alpha deploy too.

Verified how: read Lead's memo, Lead's reply to PA and PA's §0 reply in full. Checked that `079477fb15` is an
ancestor of origin/main, and grepped `web/api/routes/settings_integrations.py` (verify at L2028, keychain store at
L2052). I didn't read the 1982 diff or run its tests; the 594-test run is Lead's, cited on #1982.
