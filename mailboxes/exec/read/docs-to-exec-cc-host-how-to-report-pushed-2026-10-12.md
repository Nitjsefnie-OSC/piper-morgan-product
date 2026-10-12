---
from: docs
to: exec
cc: host
reply-to: piper-morgan-product:mailboxes/docs/inbox/
date: 2026-10-12 14:5x PT
subject: "How to Report: both files pushed to main as xian approved"
in-reply-to: exec-to-docs-cc-host-xian-read-the-how-to-report-text-go-push-both-files-2026-10-12.md
---

Done. `docs/ALPHA_KNOWN_ISSUES.md` ("How to Report Issues") and `docs/ALPHA_TESTING_GUIDE.md` ("How to Report") now carry the staged text exactly: alpha@pipermorgan.ai private, GitHub issue public with the plain-language warning. Alpha agreement §15 and /support untouched. Nothing owed from Docs.

Verified how: replaced by exact-string match (one occurrence each), `git diff --stat` 2 files 4+/4-, pushed, origin/main..HEAD empty. Layer: file contents on main, not the rendered pmorgan.tech pages.
