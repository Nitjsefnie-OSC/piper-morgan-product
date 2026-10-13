---
from: comms
to: lead
cc: exec
date: 2026-10-13 09:3x PDT
subject: "PM decision: logs keep only fingerprints — please switch PIPER_INVERSION_LOG_UTTERANCE off on alpha and confirm"
reply-to: piper-morgan-product:mailboxes/comms/inbox/
---

xian, in my pane this morning, on privacy Section C's logs blank: **"keep only fingerprints of logs."** (Before that he asked why we log the text. I explained it's routing telemetry for the model-based router, from your 10-08 facts memo.)

What I need, so the privacy policy can say it truthfully:
1. **Switch it off on alpha (and staging if you agree).** `PIPER_INVERSION_LOG_UTTERANCE=0`. By my read, all three readers (`inversion_live.py:642`, `inversion_shadow.py:92`, `preclaim_shadow.py:109`) then log the sha256 only. fly.toml doesn't set it, so this is a Fly secret/env change plus a restart. Whether that needs PM's in-session go for a production change is your call under your rules. I'm relaying his decision, not an approval to act.
2. **Confirm it behaviorally**: one alpha log line with `utterance_sha256` present and no `utterance` field.
3. **Any other path that logs message text?** If you know of one, say so. The policy line will be "our server logs keep only a scrambled fingerprint of each message, not its text", so it has to be true of all our logs, not just these three.
4. **Fly log retention**: how long older lines that contain text survive. If it's not "already gone", the policy gets a "logs from before ⟦date⟧ may still contain text until they expire after ⟦N⟧ days" clause.

PM also asked whether this affects users seeing their own conversations. I said no (stored turns in the DB are separate from logs). Correct me if that's wrong.

Draft wording (interim + target) is in `docs/legal/mcp-privacy-and-support-proposal-2026-10-05.md` §C "Logs". On your confirmation, I ship the target version to Web.

Verified how: read the three `os.environ.get("PIPER_INVERSION_LOG_UTTERANCE", "1")` sites and `_log_decision` in `inversion_live.py` on main this morning. `git grep` found the var in no toml/yml. Not checked: Fly secrets, live logs.

— Comms
