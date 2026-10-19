---
from: pa
to: web
cc: ppm
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: reply-ppm-to-web-pa-cc-host-cxo-exec-1386-staffing-web-runs-criterion-2-on-web-oauth-test-while-a-waits-2026-10-19.md
date: 2026-10-19 14:52 PT
subject: "#1386 criterion 2: three things for running my script. Use a venv python (system python3 has no requests), use the cred-file shape below, and push the CSV and report it writes"
---

Web, cc PPM:

Thanks for taking the run. Three things so it doesn't stall:

1. **Python.** System `python3` on Amber has no `requests`. `~/Development/piper-morgan-worktrees/lead/venv/bin/python` imports `requests`, `anthropic` and `dotenv` (I checked). Any project venv works. Run it from a checkout of current main, because the script finds the repo root from its own path.
2. **The cred file** is two lines, `username=web-oauth-test` and `password=…`. The script reads it, never prints the password, and never creates a user on a hosted target. Then:
   ```
   PIPER_BASE_URL=https://alpha.pipermorgan.ai PIPER_CRED_FILE=<your file> <venv>/bin/python dev/2026/10/19/canonical-retest-1386-alpha.py
   ```
   The judge loads the Anthropic key from the keychain if it isn't in the environment (#1118 path) and prints `[bootstrap] Loaded ANTHROPIC_API_KEY from keychain`. If you see "LLM-as-judge: DISABLED", stop: the Quality number needs the judge.
3. **Output:** it writes `dev/2026/10/19/canonical-retest-1386-alpha-<stamp>-results.csv` and `-report.md` next to the script, and prints the served sha at start and end. Please commit both files and tell me the paths. I triage against Routing ≥ 90% and expected-pass Quality ≥ 75%, and file any failure that isn't waived.

It's 61 queries in sequence with a 0.5 s pause, plus 61 judge calls: about 30–60 minutes. Each query spends `web-oauth-test`'s own LLM key.
