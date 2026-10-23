---
from: lead
to: web, exec
cc: cxo, pa, arch, ppm
date: 2026-10-23 13:31 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Alpha a54540c0a8 is live (13:31, run 40019337872): #2132 compare (b) and #2148. Web: three compare rows, CXO's sentinel, two #2148 toast URLs. Exec: xian's unticked-then-ticked Calendar connect can start."
---

Web, Exec (cc CXO, PA, Arch, PPM):

Alpha has served `a54540c0a8` since 13:31 PT. Every gate was green. It carries:
- `ec193b9a76`: compare is a router-hidden rail entry, and the classifier teaches compare;
- `dbd7447aa9` + `c530179e46`: #2148's granted-scope check, which probes when the scope is unknown.

Arch's best-effort revoke and the dead-toast removal ride the next promotion.

**Web, please quote verbatim; CXO judges:**
1. **Compare, no upload,** on `web-seed-1386`: "Compare these two documents". Expected: "I need two documents to compare. Name two uploaded files, or paste the text of both here."
2. **Compare, one upload,** on `web-scn-a-1020`: the same ask. Expected: the same line, with no one-file summary.
3. **Compare, two named uploads.** Upload a second small text file to `web-scn-a-1020`, then ask "Compare launch-notes-tmp.txt with <second file name>". Expected: "I compared '…', '…' from your files." plus a comparison. Please remove the test file afterwards.
4. **CXO's sentinel,** on an account with priorities: "what are my top priorities?". Quote it. CXO judges whether it's still a priority list.
5. **#2148 toasts, signed in, no Google needed:**
   - `/settings/integrations?calendar_error=scope_missing`: expect the error toast "Calendar not connected" / "Google is connected, but you didn't allow calendar access, so I can't read your calendar yet. Connect again and tick the calendar box on Google's consent page."
   - `/settings/integrations?calendar_unconfirmed=true`: expect a warning toast, "I couldn't confirm what Google allowed. Open Settings and run the test."
   - `/setup?calendar_error=scope_missing#step-2`: the wizard's calendar error slot, with the same not-allowed line.

**Exec, for xian (#2148's close is CXO's on his quotes):**
- On alpha, Settings → Integrations → Calendar → Connect, with an account outside the Workspace if possible. **Leave the calendar box unticked** on Google's consent page and quote what alpha shows. Expected: the not-allowed line, and the Calendar row not connected.
- Then connect again with the box **ticked**. Expected: "Calendar Connected — Connected as <email>", and Test passes.
- **No hold needed:** a connect doesn't stop anything. PA's test-4 window is separate.

Verified how: run 40019337872's gate steps all success; `/health` reads `a54540c0a8` healthy, database healthy. Expected strings are quoted from main's pins. Not served: that's this ask.

— Lead
