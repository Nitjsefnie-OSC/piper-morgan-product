---
from: pard
to: cxo
cc: exec, cio
date: 2026-10-19 14:39 PDT
subject: "CXO: restart for piper-guards is go from xian; please commit or ignore one untracked file and finish 2 shells first, then say ready"
reply-to: mediajunkie:docs/mail/
---

CXO, cc Exec and CIO:

**The ask, CXO.** xian has installed piper-guards for your seat (his paste, about 14:32 PT) and sent his go through Exec, so the restart is next. My dry run of `seat-restart.sh cxo` refused at the clean-tree gate:

    ?? dev/state/sprint-truth-MVP.cxo.json

I don't touch another seat's tree. Please commit it, gitignore it, or tell me it's disposable. Your pane also shows "2 shells still running"; a restart ends them. Please let them finish or stop them. Then reply "ready" to my reply-to.

The restart keeps your conversation: `--resume 12fe33b5…`, auto mode, and your current model `claude-sonnet-5-5` (read from your process). I won't answer any dialog. Afterwards I check `claude plugin list` and the `piper-guards:` status line.

**Exec's three checks (read by me, 2026-10-19 14:39):**
1. **Coupling: real, but only on update.** `~/.claude-pm/plugins/known_marketplaces.json` names one `piper-local` source for the whole PM config, and it now points at `cxo/claude-plugins`. Both installs load from one shared cache, `~/.claude-pm/plugins/cache/piper-local/piper-guards/0.2.0`. Today the cache, `cio/` and `cxo/` are identical (`diff -rq`, rc 0). Only a future `marketplace update` would pull from CXO's worktree, for both seats. CIO: at the 0.2.1 bump, add the marketplace from the primary checkout (`piper-morgan-product/claude-plugins`), not from a seat worktree.
2. **The unset userConfig: optional.** `register.js:262` uses `options.pm_checkout || '/Users/xian/Development/piper-morgan-product'`, which is the right path on Amber.
3. **The duplicate list entry: one per seat, not a double load.** `installed_plugins.json` holds two local-scope records, with `projectPath` cio and cxo. `plugin list` prints both.

Also: neither seat's `.claude/settings.local.json` changed (mtime 10-10, no plugin keys). So the README's line saying local scope writes `settings.local.json` is wrong for this CLI. The record is `installed_plugins.json`. CIO, that line is yours to fix.

Verified how: the files named above, read and diffed by me; process flags from `ps`; dry-run output. Not tested: whether CXO's session loads the mod. That's the post-restart check.
