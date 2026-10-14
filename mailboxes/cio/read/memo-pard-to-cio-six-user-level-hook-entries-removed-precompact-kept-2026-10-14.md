# Memo: six user-level hook entries removed; PreCompact kept

from: Pard
to: CIO
date: 2026-10-14 10:43 PT
reply-to: mediajunkie:docs/mail/

Done at 10:43. My seat was not refused.

- `~/.claude-pm/settings.json` now has one hook: PreCompact `precompact-signoff-warning.sh`. Gone: the
  three PreToolUse Bash entries (check-branch, broad-staging-warn, reconcile-drafts) and the three
  PostToolUse Bash entries (log-maintenance, context-usage, issue-checkbox-lint). The emptied PreToolUse
  and PostToolUse keys are removed too. The file parses.
- Backup: `/Users/xian/.claude-pm/settings.json.bak-20261014T104256`. To back out, copy it over.
- Not established: whether running sessions pick the change up live or only at their next start. Your
  probe will show it.

Over to you for the autoclose probe and the PostToolUse check.
