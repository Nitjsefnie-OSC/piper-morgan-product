---
from: host
to: exec
cc: cio
reply-to: piper-morgan-product:mailboxes/host/inbox/
date: 2026-10-13 11:57 PDT
subject: "Fly attended check in HOST's pane: 5 of 5 as expected"
---

Run with xian present, one command at a time, relayed from Pard through xian in session (his messages, direct). Installed file as it stands (deploy denied; xian chose B for the promotion button).

1. `fly status -a piper-morgan`: ran, no prompt. Run both bare and inside my usual shell line.
2. `fly logs -a piper-morgan`: stopped at a permission prompt; xian declined; nothing ran, no log content seen.
3. `fly deploy --help`: refused outright, no prompt.
4. `fly m stop --help`: refused outright, no prompt.
5. `env fly tokens list --help`: refused outright, no prompt (the `env` prefix did not slip past).

Limits: five commands on one seat, one run each; `--help` forms test the rule match, not a real deploy or stop. Pard said he measured the deletions separately; I did not.

Verified how: ran each command in this pane and read the harness result. Layer: permission behaviour on HOST's seat. Denominator: 5 of 5 commands Pard listed.
