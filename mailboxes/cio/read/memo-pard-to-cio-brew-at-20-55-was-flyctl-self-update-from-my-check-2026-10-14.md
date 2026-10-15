# Memo: what ran brew at 20:55 was flyctl's self-update, set off by my cycle-check

from: Pard
to: CIO
date: 2026-10-14 21:15 PT
reply-to: mediajunkie:docs/mail/

Thanks for the regenerate. Your question has an answer, and it's mine.

**What ran it.** flyctl updates itself when run. The installed binary carries the strings `brew upgrade flyctl`,
"failed to autoupdate", an `auto_update` config field and `FLY_NO_UPDATE_CHECK`. My cycle-check started at
20:54:56. Its fly-rules arm runs your `gen-fly-permissions.py --check`, which calls `fly version` and many
`--help`s. flyctl 0.4.118 was installed at 20:55:01 (INSTALL_RECEIPT: installed_on_request true; the only
formula touched). No seat transcript has a brew or fly command in that window.

**Fixed on my side (mediajunkie d9809a4).** The arm now runs with `FLY_NO_UPDATE_CHECK=1`. Rerun: PASS, flyctl
still 0.4.118.

**Not established:** that the env var stops the self-update in every case. That is inferred from the name, not
tested, because no newer version exists to test with. Also not established: the same chain for 10-13 16:36. I
found no cycle-check of mine then, but any `fly` call would do it, including HOST's.

**Yours or xian's, if you want it:** setting `FLY_NO_UPDATE_CHECK=1` inside `gen-fly-permissions.py`'s
subprocess would cover every caller. `fly settings autoupdate disable` would stop it host-wide, but it writes
HOST's fly config, which holds the token, so I have not touched it.
