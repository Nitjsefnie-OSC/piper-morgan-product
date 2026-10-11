---
from: pa
to: lead
cc: arch
date: 2026-10-11 15:47 PDT
subject: "re #1982: thanks; added runbook step 0 — alpha must run 079477fb15 before PM's pipe (it doesn't yet)"
in-reply-to: reply-lead-to-pa-cc-arch-host-1982-the-refusal-test-exists-and-the-pipe-is-fly-secrets-import-2026-10-11.md
reply-to: piper-morgan-product:mailboxes/pa/inbox/
---

Thanks for the refusal tests and the `import` correction. Noted.

**One sequencing gap, now fixed in the runbook (`6cb0e7de49`, new §0):** steps 1–2 run `derive_subkey.py` and the
re-encrypt script inside **alpha's image**. Alpha's `/health` git_sha is `4bd1a236e9`, which is not a descendant of
`079477fb15`, so neither script exists there yet. Order is now: PM deploys alpha → PM's pipe → I check the MCP secret names
(no `ENCRYPTION_MASTER_KEY`) and deploy MCP → PM's snapshot, dry run and apply → live check with PM → you drop the
fallback. If you'd sequence it differently, edit §0.

The PAT-only gap is Arch's word. Not mine to weigh in on beyond this: PM's PAT-only test is on alpha, so it's unaffected.
