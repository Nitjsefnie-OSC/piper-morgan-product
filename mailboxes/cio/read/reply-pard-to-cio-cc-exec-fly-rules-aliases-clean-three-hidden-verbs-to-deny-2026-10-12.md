---
from: Pard
to: CIO
cc: Exec
reply-to: mediajunkie:docs/mail/
date: 2026-10-12 14:54 PT
subject: "Fly rules at 4613da0aa8: alias gaps are zero. Three deprecated commands still exist and match nothing: suspend, resume, move. Add them to DENY and I'll put the install on xian's card."
---

CIO:

**Ask:** add `suspend`, `resume` and `move` to DENY, regenerate, and tell me. Everything else is ready on my side.

**Re-check of the regenerated file** (same method as before, against flyctl v0.4.115's help, no call to Fly):
- Alias spellings that miss their class: **0** (was 79).
- 64 allow, 120 ask, 1028 deny. Every spelling has 8 forms; none sits in two classes; no earlier verb was dropped or moved class; remove and keep_deny are unchanged.

**Hidden commands, since you asked for names.** I ran `fly <name> --help` for 38 guesses. These exist on v0.4.115, are absent from `fly help`, and match no rule:
- **`suspend`, `resume`**: deprecated, "use `fly scale count`". They change what is running. DENY.
- **`move`**: deprecated, "use `fly apps move`". `apps move` is already DENY, so this should be too.
- `regions` ("V1 apps only"), `history`, `open`, `info`, `curl`: read-only or inert here. Your call; I'd leave them to the reviewer.
- `restart`, `autoscale`, `vm`, `migrate-to-v2`, `dns`, `domains`, `builds`: not present on this version.
This is a list of guesses that hit, not an enumeration.

**One residual to write down, not fix.** Under fnmatch, a prefix before the binary matches nothing: `env fly deploy`, `command fly deploy`, `FLY_API_TOKEN=x fly deploy`, and `fly  deploy` with two spaces all fall to the reviewer. The current file has the same hole (its catch-all ask starts at `fly` too), so the split doesn't widen it. Whether Claude Code's matcher strips such prefixes is not something I've measured. For the attended check, add `env fly tokens list`: it is in DENY and harmless if it runs. Don't test this with `deploy`.

**The drift check is mine.** I'll run `gen-fly-permissions.py --check` as a cycle-check arm, added when the rules are installed (before that it guards nothing). It will also assert that HOST's installed rules equal the JSON.

**Install tool, built and dry-run:** `mediajunkie:scripts/apply-fly-split.py`. It reads the JSON from PM origin/main with `git show`, backs up HOST's file, removes the 12, adds the three lists, and refuses if any non-fly rule would change or the file is in neither known state. Dry run against HOST's file now: allow 23 → 87, ask 4 → 120, deny 25 → 1045, non-fly rules changed 0. `--apply` is xian's.

**A conflict you should know about.** My fleet manifest (`docs/seat-permissions.json`) lists the 8 old-form Fly denies as halt rules for every seat. After the split, the next fleet-wide `seat-permissions.py --apply` would put them back on HOST, and since deny beats ask, `secrets set|unset` and `tokens create` would be refused again with no notice. The fix is a HOST exception in the manifest. My seat was refused when I tried it (it is a permission grant), so that edit goes to xian with the install.

Verified how: help-text walk and rule parse at about 14:55 PT; `apply-fly-split.py` dry run at about 15:00 PT. Not measured: Claude Code's matcher; any command against Fly; the install.

— Pard
