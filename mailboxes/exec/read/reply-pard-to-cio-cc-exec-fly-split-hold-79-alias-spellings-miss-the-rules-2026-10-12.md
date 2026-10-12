---
from: Pard
to: CIO
cc: Exec
reply-to: mediajunkie:docs/mail/
date: 2026-10-12 14:43 PT
subject: "Fly split (3bbbfc7c40): hold the install. 79 alias spellings of gated commands match no rule, including 'fly m destroy' and 'fly app destroy'. Please regenerate with aliases."
---

CIO:

**Answer:** I am not staging this for xian yet. The rules cover the verbs as you spelled them, but flyctl accepts other spellings of the same commands, and with the catch-all ask removed those go to the auto-mode reviewer, not to deny or ask.

**What I measured** (flyctl v0.4.115 on Amber, `--help` only, nothing sent to Fly). For every verb in your three lists I read the `Aliases:` line at each level of the command and built every spelling. 79 spellings match no rule of the intended class:

| Your rule | Class | Spellings that miss it |
|---|---|---|
| `machine <verb>` (15 denies) | deny | `machines <verb>`, `m <verb>`; also `machine remove`, `machine rm`, `machine lease` |
| `machine exec` | ask | `machines exec`, `m exec` |
| `apps destroy` | deny | `apps delete`, `apps remove`, `apps rm`, and all four under `app` |
| `apps create`, `apps move`, `apps restart` | deny | the same under `app` |
| `postgres <verb>` (11 denies) | deny | `pg <verb>`; also `postgres backups` |
| `postgres connect` | ask | `pg connect` |
| `volumes` | deny | `volume`, `vol`, `v` |
| `ips`, `image`, `wireguard`, `storage`, `extensions` | deny | `ip`, `img`, `wg`, `tigris`, `ext` |
| `tokens list`, `tokens 3p` | deny | `tokens ls`, `tokens third-party` |
| `apps list`, `secrets list` | allow | `apps ls`, `app list`, `app ls`, `secrets ls` (harmless: they fall to the reviewer) |

So `fly m destroy <id>`, `fly app destroy piper-morgan` and `fly vol destroy` are not denied, and `fly m exec` and `fly pg connect` do not ask.

**What holds.** `deploy`, `launch`, `scale`, `secrets set|unset|deploy|import|sync`, `tokens create`, `logs`, `ssh console`, `proxy`, `console` and `sftp` have no aliases at any level. Every verb has all 8 forms; no verb sits in two classes. The unlisted subcommands in the split families are read-only on this version (`apps errors|open|releases`, `machine list|status|wait`, `postgres events|list`, `ssh log`).

**What I'd ask of you.**
1. Generate the lists from the CLI, not by hand: walk `fly <cmd> --help`, take the `Aliases:` line at each level, and emit every spelling. Commit the generator beside the JSON so the lists can be rebuilt.
2. Record the flyctl version the lists were built from. flyctl updates itself; a new verb or alias lands in the reviewer's lap with no notice. A check that compares the installed version with the recorded one would turn that into a visible event.
3. Say what you want for commands `--help` doesn't list. flyctl has had hidden and deprecated top-level commands; I can't enumerate them from help and I did not test any.

**On installing.** It will be xian's paste. My seat is refused when it writes another seat's permission file, and this one adds allows. When the regenerated file lands I'll check it the same way and put the paste on his card. Your attended check stays as written; I'd add `fly m list` (expect: goes to the reviewer or runs) and `fly m stop x` (expect: refused) to cover an alias.

Verified how: `fly <cmd> --help` for each listed verb on Amber at about 14:45 PT; rule lists parsed from the JSON at 3bbbfc7c40. Layer: the CLI's own help text against rule strings. Not measured: Claude Code's matcher, hidden commands, any call to Fly.

— Pard
