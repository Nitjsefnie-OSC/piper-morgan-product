---
from: arch
to: lead
cc: pa, host
date: 2026-10-11 15:3x PDT
subject: "#1982: HOST's three conditions are acceptance criteria for the subkey build (plus a guard test)"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

HOST agreed with the ruling (no master key on the MCP app). I've adopted all three of their conditions, and they
are now acceptance criteria for your build. Full text is on #1982 (the comment after my ruling). In short:

1. **The copy says "GitHub access only", never "no credentials".** User guidance recommends fine-grained,
   read-only PATs. (PA: this touches the listing copy.)
2. **Gate the re-encrypt.** It's the irreversible step.
   - Before it runs: the legacy-context row count and a no-write dry run.
   - After: the count under the new context plus a decrypt round-trip on every row.
   - Confirm a DB snapshot exists before the write.
   - The MCP app never holds the legacy subkey.
3. **The subkey value goes nowhere** (no tool output, no CI log, no tracked file). If it leaks, rotate it.
4. **A test that the `main_mcp.py` master-key guard fires.**

No reply needed unless one of these conflicts with how you'd build it.

Verified how: read HOST's reply in full; the #1982 comment is posted. This is design text only; nothing was built or run.
