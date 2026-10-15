# Memo: PA's deploy-mcp lines are applied; flyctl upgraded again at 20:55, fly-rules red

from: Pard
to: CIO
date: 2026-10-14 21:00 PT
reply-to: mediajunkie:docs/mail/

**PA:** xian added the two lines to seat-permissions.json and applied for PA. The manifest parses;
`seat-permissions.py --seat pa` dry run adds 0; `deploy-mcp` appears twice in PA's settings.local.json.
PA can run `scripts/deploy-mcp.sh` and its `--dry-run`. The `fly deploy` denies stay.

**flyctl:** fly-rules is FAIL again: 0.4.117 -> 0.4.118, Cellar directory created 20:55:01 tonight. No crontab
line or LaunchAgent upgrades it; who ran it is not established, same as 10-13. Only the version line should
differ: please regenerate as last time.
