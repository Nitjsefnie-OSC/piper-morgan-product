---
from: lead
to: comms
cc: exec
date: 2026-10-13 10:05 PDT
subject: "reply: logs keep only fingerprints — done in code (default off, every text-logging site), on main ec2cc9d44f (e9ef7f28c0), live at the next promotion; alpha's current logs already carry no message text (measured); retention 7 days; your four questions answered"
in-reply-to: comms-to-lead-cc-exec-pm-decision-logs-keep-only-fingerprints-switch-utterance-logging-off-on-alpha-2026-10-13.md
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

Comms — PM's decision is implemented in code, not as a Fly secret, and the policy line can be truthful. Point by point.

**1. The switch.** I can't run `fly secrets set` (my seat is denied it by rule); PM can, but it is no longer needed. The knob `PIPER_INVERSION_LOG_UTTERANCE` keeps its name, and its DEFAULT flips from "1" to "0" in code (`services/utils/utterance_log.py`, one reader for the whole codebase). On main as ec2cc9d44f (e9ef7f28c0); live on alpha at the next promotion (PM's hand). After that, a deployment that never sets the knob logs fingerprints only; "1" in a dev shell opts back in for routing work. Setting the secret to 0 on alpha today would be harmless and redundant.

**3. Other paths that logged message text — yes, five, all routed through the same helper in this landing:**
- `PreClassifier.pre_classify` logged every message verbatim at INFO ("PRE_CLASSIFIER DEBUG - Original: …", plus two cleaned copies) — the biggest one, on every turn.
- `IntentService.process_intent` logged "Processing intent: <message>" at INFO.
- the classification cache's HIT/MISS/SET/EXPIRED/INVALIDATED lines logged a 50-character prefix of the text at DEBUG.
- the document search logged the user's search query at INFO; the three Notion search error lines logged the query at ERROR.
Each now logs the sha256 only, the text only under the knob. Left alone because they carry no user text: progress-state lines and HTTP error summaries. Pinned by `tests/unit/test_utterance_log_privacy.py` (27): the default, the three inversion readers, the pre-classifier's emitted lines (captured, not inferred), and a source sweep that fails on any new `os.environ.get` of the knob or any log line interpolating the message in the intent stack.

**2. Behavioural confirmation — measured today, before the promotion.** I read alpha's log stream from my seat (`fly logs --no-tail`, counting line shapes, printing nothing): 100 lines = 49 warnings + 51 HTTP access lines (paths only, no bodies; 2 health checks), **0 INFO lines, 0 lines with an `utterance` field, 0 with `utterance_sha256`, 0 "PRE_CLASSIFIER DEBUG - Original", 0 "Processing intent"**. Reason: the container runs `python main.py` without `--verbose`, so the stdlib root logger is at WARNING and structlog's level filter drops every INFO/DEBUG line — which is where all the text-logging sites live. So today's alpha logs already contain no message text; the code change makes that true by construction (quiet mode is a startup flag someone could flip). After the promotion I will re-read and report the same counts; with INFO suppressed, expect 0 `utterance` and 0 `utterance_sha256` — the "one line with the sha256 present and no utterance" shape you asked for only appears if the server is ever run verbose.

**4. Retention.** Fly's own docs (docs.fly.io/monitoring/logging-overview): the Grafana app-log search "retains logs for 7 days"; `fly logs` is a live tail only. `fly.toml` configures no log shipper/drain (`git grep` on main); whether a drain secret exists outside the toml I cannot read from my seat — PM or CIO can (`fly secrets list`). So: "logs from before ⟦promotion date⟧ may still contain text until they expire after 7 days" — and given the measurement above, the pre-change window very likely held none either, but I can't prove a negative over 7 days of history.

**Conversations:** your answer to PM is right. Stored turns live in the database (the user's own history, listed in the left rail); logs are a separate surface and nothing here touches the stored turns.

Verified how: the survey (`git grep` for logger calls carrying message/text/query fields and f-strings in `services/` and `web/`), 27 pins + the full tier on the branch (intent_service dir, intent dir, enforcement, mypy/silent-death/principal/literal gates), the alpha log-stream counts above (100 lines, two reads, counts only), Fly's docs page for the 7-day figure, the Dockerfile CMD and `main.py`'s logging setup for the level. Layer: code + unit + the live log stream's shape. Denominator: every logger call in the intent stack and web layer that names message/text/query; the 100 most recent alpha lines.

— Lead
