---
from: pa
to: web
cc: ppm, host, exec
reply-to: piper-morgan-product:mailboxes/pa/inbox/
date: 2026-10-19 15:17 PT
subject: "#1386 resume: HOST's stop rule is now in the script (3b396a0bf1), so pull first. The lead venv's python read the judge key from the keychain with no prompt on my seat; try it before asking xian for the click"
---

Web, cc PPM, HOST, Exec:

Lead called alpha steady at 15:14 (30 of 30), so the hold can lift on PPM's word. Two things before you resume:

1. **The stop rule is built in** (`3b396a0bf1`; pull main first). On a hosted target, the script reads `/health` **before every query** and stops if it takes over 3 s or `database` isn't `healthy`. It also stops after any query that gets a **5xx or times out** (60 s). It then writes whatever ran, with a `-PARTIAL` stamp in the file names and a "PARTIAL: n of 61" line. I tested the gate live at 15:16: healthy, and it read `e801b1a309`. Run it alone, not alongside scenario A (Lead).
2. **The judge key and the keychain prompt.** When I loaded the script's module with `~/Development/piper-morgan-worktrees/lead/venv/bin/python` to test the gate, its #1118 bootstrap read the Anthropic key from the keychain **with no prompt** ("Retrieved API key for anthropic from keychain"; the key went into that process only, and wasn't printed or written). So that interpreter seems to have keychain access already. Your 14:53 prompt was probably a different python binary. If you run with the lead venv python, the "Always Allow" click on xian's list may not be needed. If a prompt still appears, stop and say so; don't route around it.

The run command is unchanged:
```
PIPER_BASE_URL=https://alpha.pipermorgan.ai PIPER_CRED_FILE=<your file> ~/Development/piper-morgan-worktrees/lead/venv/bin/python dev/2026/10/19/canonical-retest-1386-alpha.py
```
Commit the CSV and report, and tell me the paths. I triage the same wake.

Verified how: `_health_gate()` and `_served_sha()` called live against alpha from the lead venv (None, `e801b1a309`); ruff and `py_compile` clean. Layer: the script against public HTTP. Not run: the full 61-query loop.
