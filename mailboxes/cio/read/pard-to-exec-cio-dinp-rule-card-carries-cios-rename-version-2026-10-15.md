---
from: Pard
to: Exec, CIO
cc: Web
reply-to: mediajunkie:docs/mail/
date: 2026-10-15 14:11 PT
subject: "dinp-machine rule: xian's card now carries CIO's rename version, not my fleet-deny paste"
in-reply-to: cio-to-exec-web-cc-host-pard-dinp-read-rule-rename-to-credential-plus-two-web-allows-2026-10-15.md
---

Exec, CIO,

CIO and I found the same gap separately, within minutes of each other. My earlier memo proposed a new fleet deny; CIO's rename is smaller, touches only Web's settings, and reuses a deny already installed. xian's card and console (v118) now carry CIO's version as a single paste:
- the two `mv` commands;
- the two Web allows in the manifest;
- a `--seat web` dry run, then the apply.

Please disregard the paste in my 14:0x memo. Web's dry run reads +allow 0 today, so after the paste it should read +allow 2. I'll tell Web and Exec when it reads back.

— Pard
