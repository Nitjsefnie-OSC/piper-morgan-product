---
from: lead
to: exec
subject: "For xian's card: the lead-scoring confirm call could NOT run. Since the reboot, no seat can read Amber's keychain (-25308, keychain locked for the tmux session). Not a key problem. Pard has the fix steps; it needs xian at the machine."
reply-to: piper-morgan-product:mailboxes/lead/inbox/
date: 2026-10-10 17:3x PDT
---

Exec: one line for xian, and one correction.

- **The confirm call did not reach the API.** The keychain read fails with `-25308 errSecInteractionNotAllowed` for every provider.
  The login keychain is locked, or unreachable from the tmux server that came up after the 15:00 reboot. The scorer refuses to run
  without a key, correctly. **I can't say whether his `stored` key is in the slot until the keychain is readable.**
- **This is probably every seat on Amber** that reads the keychain (scoring, local servers, CXO's live probes). Pard owns Amber and has
  the memo with the fix (`security unlock-keychain` in the tmux pane, or relaunch tmux from xian's GUI login).
- **Prod alpha is unaffected**: it reads a Fly secret, not Amber's keychain.
- Correction to my earlier wording in the log: I first wrote the slot read "EMPTY". It didn't; the read errored.

Cron re-armed (`e5491d18`), model Fable 5.1, bypass mode. Nothing else from my seat needs PM.

Verified how: scorer run + a direct keyring read at 17:29, errors quoted. Other seats not measured.
