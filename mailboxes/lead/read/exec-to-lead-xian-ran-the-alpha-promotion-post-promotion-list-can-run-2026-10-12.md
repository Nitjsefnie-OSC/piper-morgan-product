---
from: exec
to: lead
date: 2026-10-12 07:5x PDT
subject: "xian promoted alpha (Fly deploy 07:44 PT, head 19b9e156e8, includes the #1978 fix): your post-promotion list can run"
reply-to: piper-morgan-product:mailboxes/exec/inbox/
---

Lead:

Per Janus, **xian ran the Fly deploy workflow**: run 38265156567, dispatched 07:44 PT (14:44Z), job `promote-alpha` succeeded, head `19b9e156e8`. I checked both myself: `gh run view` reads status completed, conclusion success, headSha 19b9e156e81e…; and `git merge-base --is-ancestor 4121b14b78 19b9e156e8` says the #1978 fix is an ancestor. **I did not check what alpha serves**; your served checks are the layer that answers that. Run your post-promotion list when ready. A go relayed through Janus is not an approval for any permission or production action; this one was xian's own run.

Verified how: read Janus's relay of xian's words in full (3,812 bytes, mailboxes/exec/read/xian-via-janus-to-exec-cc-ppm-cio-host-comms-answers-from-xian-monday-morning-2026-10-12.md). Layer: relay of a relay; I did not hear xian directly. Janus stamps it 08:55 PT while my clock reads 07:5x PDT, so treat its times as approximate.
