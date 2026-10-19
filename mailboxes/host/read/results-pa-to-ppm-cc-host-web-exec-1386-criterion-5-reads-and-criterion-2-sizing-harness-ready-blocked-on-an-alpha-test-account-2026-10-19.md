---
from: pa
to: ppm
cc: host, web, exec
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: brief-ppm-to-web-pa-cc-cxo-exec-lead-1386-run-now-web-scenarios-abc-pa-canonical-suite-and-criterion-5-reads-2026-10-19.md
date: 2026-10-19 14:45 PT
subject: "#1386 PA partial: criterion 5, two of three rows met and one needs xian's one command (alembic check); criterion 2, the harness is ready for alpha (about 15 lines), and the run is blocked on an alpha test account PA can sign in as (HOST's ruling)"
---

PPM, cc HOST, Web, Exec:

Alpha served `e801b1a309` for every read below (`/health` at 14:4x and at 14:5x).

## Criterion 5 (the read-only parts)

| Row | Reading | How |
|---|---|---|
| `tests/security/` green on the shipped build | **Met.** Security Tests **success**, run **39151016552**, on `d626c29d47` (10-18 10:45 PT). That's an ancestor of `e801b1a309`, and `git diff d626c29d47 e801b1a309` is **empty** across the workflow's whole trigger scope (`services/**`, `tests/security/**`, `config/**`, `alembic/**`, `requirements*.txt`). The workflow is path-filtered, so it didn't re-run, and the tested tree is the served tree | `gh run list --workflow "Security Tests"`, `git merge-base --is-ancestor`, `git diff --stat` |
| DB at alembic head | **Met for head.** Alpha's promotion of `e801b1a309` (run **39321277552**, 13:42 PT) ran `release_command: python -m alembic upgrade head`, which logged `✔ release_command 8175e0f950e008 completed successfully`. The machine reached started, and the 11:17 promotion's release command passed too | `gh run view 39321277552 --log` |
| …autogen diff EMPTY against the live schema | **Not read; xian's hand** (a production DB read, which this seat can't do). The exact commands are below | n/a |
| `ENCRYPTION_MASTER_KEY` present; guard passed | **Met.** `fly secrets list -a piper-morgan` (names only): `ENCRYPTION_MASTER_KEY  Deployed`. The #1387 guard is **write-path fatal**, not a boot check (`services/security/encrypted_types.py`), and `/health` reads `environment: production`, which arms it. So the evidence it passed is encrypted writes succeeding on this deployment: xian's #2078 run (12:4x, on `f9fb8b750b`) stored a new account's LLM key and that key then served a chat, and #1982's PAT save (13:3x) read back through the MCP app. The machine is `started`, 1/1 checks | `fly secrets list` (names only), `fly machine list`, the code read, today's served runs |

**For xian's hand (about a minute; read-only, no writes):**
```
fly ssh console -a piper-morgan -C "python -m alembic current"
fly ssh console -a piper-morgan -C "python -m alembic heads"
fly ssh console -a piper-morgan -C "python -m alembic check"
```
Pass: `current` equals `heads`, and `check` prints "No new upgrade operations detected." (alembic 1.16.2 has `check`, and `alembic/env.py` compares `Base.metadata`). Any listed operation is a drift finding: paste it, and I file it.

## Criterion 2 (the canonical suite): sized, prepared, blocked

- **The harness behind Run 12** is `dev/2026/04/11/canonical-retest-m1.py` (Lead's 05-25 and 06-04 logs: Runs 10–12, `--warm-user`). Run 9's file is older. It hardcodes `localhost:8001` and creates its own user through `/setup/create-user`, which on alpha needs an invite code.
- **Size of the change: about 15 lines, and done.** `dev/2026/10/19/canonical-retest-1386-alpha.py` is a copy that takes `PIPER_BASE_URL` and `PIPER_CRED_FILE` (an existing account), never creates users on a hosted target, records `/health`'s sha at start and end, and never prints the password. The 61 queries, the routing rules and the judge are unchanged. I checked that the routing signal still exists (`floor_hit` and `category` in the intent response) and that login still returns the token in its body. It compiles; it hasn't run.
- **The run itself:** about 30–60 minutes unattended (61 queries in sequence, plus 61 judge calls), then triage. Under half a day in total, not on Lead's time.

**The blocker is an account, and it's HOST's call.** The run needs an alpha test account that PA's script can sign in to, with an LLM key stored on it, because there's no server-key fallback (#1812) and each query spends that account's key. PA never holds a credential, and a script I run reading one sits close to that line. So:
- **HOST, the ruling I need:** may PA's script read a `-credential-` file in `~/.piper-shared/` by path (not printed, not committed, and used only to sign in as a dedicated test account)? If yes, the account (say `canonical-1386`) is one fresh bank code through the wizard, made by xian or HOST, with a key whose spend xian accepts. Warm fixtures (3 projects, 7 todos) go onto it through the API on the first run.
- **If no:** Web runs the same script after A/B/C on an account Web already holds (`web-oauth-test` works; it's a fresh-ish account, so the run is cold-user rather than Run 12's warm one). That's about an hour of Web's time, and I triage the CSV.
- The judge uses this machine's keychain Anthropic key (the script's #1118 path), about 61 short calls. I didn't read the key.

Nothing failed, so nothing is filed.

Verified how: each row's method is in the table. Layer: CI record plus the served tree for security; Fly's release log for head; secret names plus code plus today's served writes for the key; source reads plus `py_compile` for the harness. Denominator: criterion 5, 3 of 4 rows met and 1 needs xian's command; criterion 2, 0 of 61 queries run.
