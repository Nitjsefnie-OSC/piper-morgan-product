# Prod alpha server key → pipermorgan.ai org — steps for Fri 2026-10-16 (PM's hand)
**Filed**: 2026-10-11 (Lead) · Trigger: Themis's ruling 10-10 — switch keys on 10-16 (the current key spends Krink's credit, which expires 10-15).
Everything below is xian's hand: Lead's seat is classifier-denied on `fly secrets` and never sees a key. Keys travel by hidden prompt only; masked form (`sk-a…1234`) in any memo.

## Before (console, 5 min)
1. In the pipermorgan.ai Anthropic org, create a workspace **for prod** (recommended name `piper-alpha-prod`), separate from `lead-scoring` ($50 cap, dev scoring). Reason: a scoring run must not starve users; a user surge must not starve scoring. Set its own monthly cap (Themis decides the number).
2. Create one API key inside that workspace. Copy it once; it goes nowhere else.

## Move (terminal, 2 min)
```bash
read -s -p "new prod key: " K && echo
fly secrets set -a piper-morgan ANTHROPIC_API_KEY="$K"   # Fly restarts the app
unset K
```
Staging (`piper-morgan-staging`) holds its own secret; move it the same way only if Themis wants staging on the org too.

## PASS criteria (Lead runs the read-only checks on request; xian runs the chat turn)
- `curl -s https://alpha.pipermorgan.ai/health` is 200 and still reports commit `4bd1a236e9` (or the current promoted sha).
- One chat turn by a user **without** a stored key is served (that turn runs on the server key).
- `fly logs -a piper-morgan` shows no `rate_limit` / workspace-limit error on that turn.
- Console: Usage → the prod workspace shows the request; `Piper Morgan` (old workspace) shows nothing new.

## After
- Revoke the old key in the console (not before PASS). A key that ever reached git is burned regardless; this one never did.
- Lead: one confirm call on the Amber `lead-scoring` slot is a separate, already-done check (10-10 17:41); nothing to redo unless xian re-stores the slot.
- Testers on their own stored keys are unaffected by any of this.
