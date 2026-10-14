---
last_updated: 2026-10-14
currency_claim: updated same-commit when entry points, module classification, or deploy topology change
max_age_days: 30
---

# SYSTEM.md — what is actually running

**Living core doc #2** (see `reviews/2026-08-architectural-review/living-core-docs.md`).
Successor to `current/architecture.md`, which is now HISTORICAL (banner at its head) — that
document had accreted three generations of contradictory claims and a revision log that could not
be trusted (clean-room finding, Leg D). This one states the current system only, from evidence:
the Leg B census (2026-08-29, all 491 non-init modules classified, with its same-day corrections)
plus the disposal record since. **Arch authored v1; Lead maintains.**

## One server, and what reaches it

- **Entry point**: `main.py` → uvicorn → `web.app:app`. No separate backend app.
- **~31 mounted routers** (registrations in `web/app.py` + `web/startup.py`) + the transparency
  router + 2 dev routers (404 in production via the `PIPER_ENVIRONMENT` gate).
- **Plugins**: discovery enables calendar/notion/github/slack (+demo — being env-gated per #1690;
  with `config/PIPER.user.md` absent, ALL discovered plugins enable by default).
- **Slack inbound**: Socket Mode only, config-gated, honest-skip when tokens absent (fail-closed
  hold per #1481/#1484; surface descoped to Fast Follow).
- **Background services, unconditional at startup**: blacklist cleanup, attention decay, ethics
  audit cleanup, output filter, composting scheduler. These make `services/ethics` and the
  composting half of `mux` load-bearing regardless of user traffic.
- **CLI**: `main.py` subcommands (setup/status/preferences/keys). ⚠️ `cli/commands/` standalone
  scripts are OUTSIDE the census denominator and outside pytest's testpaths — a broken import
  there is invisible to CI (proven by #1700). Treat cli/ as extension-class with weaker guarantees.

## The understanding stack (chat path)

Governing law: **ADR-080** (10-06): the LLM decides meaning; code decides permission. Order on a turn
(detail and file anchors: `current/intent-routing-stack.md`, rows L and 0-4):

1. **Live inversion router**, first, on UNARMED turns only: one constrained, stateless LLM call
   (`inversion_live.consult_inversion_live`). It dispatches only an operation named live by
   `PIPER_INVERSION_LIVE_CATEGORIES` (set **via fly secrets**, invisible to config files) that is READ
   or in `FLIP_WRITE_ALLOWLIST` (10 writes as of 10-14). Everything else falls through unchanged.
2. **Stage 0** referent resolution (B3, session-scoped ledger), then the deterministic
   **pre-classifier** (literal ceiling **90** in 35 lists on 10-14: 29 a ruled permanent floor, 61
   router-quality work after MVP), then the **legacy LLM classifier**.
3. The **action rail** (`MAX_DISPATCH_SITES = 0`), whichever surface chose the key; then category
   handlers; then the **conversational floor** (the safety net, with the anti-fabrication rails).

Consent evaluates the rail entry's EffectClass regardless of which surface produced the intent. **The
legacy classifier's retirement check (2026-09-30) was missed; stated 10-13: not met** (it still serves
four call sites plus Slack). Re-check when the #1595 Phase 3 tail reaches the ruled floor
(decisions.log 10-13). On the BYOC path there is no classifier at all: the host LLM selects tools
against the derived catalog. There is also **no floor there**, so honesty must ride tool payloads
(CONNECTORS.md rule 1).

## Module classification (census 2026-08-29, disposal in flight)

Five classes — essence / extension / experiment / superseded / dead (definitions in ESSENCE). At
census: ~69% of 491 modules load-bearing; ~19% dead-or-never-invoked. **Disposal has since
removed ~10K LOC across three batches** (epic #1698 holds the execution record; six
fresh-sweep-contradicts-census holds honored — the census is caller *evidence*, never a
skip-verification pass). Live-state detail: `reviews/2026-08-architectural-review/findings/
leg-b-live-state-census.md` (with correction block). The biggest single module remains
`services/intent/intent_service.py` (~17.4K lines on 10-14, up from ~14.4K at census) — it has grown with the inversion work, and shrinks only as the legacy classifier retires.

## Data layer

**Postgres** (port 5433; 80+ migrations; all timestamp columns verified timezone-aware — the one
subsystem where a class fix demonstrably ended its incident stream). **ChromaDB** (embeddings/RAG,
port 8000) and **Redis** (6379, usage caps) — both live and **unobserved**: zero incident history
means zero monitoring, not proven robustness (incident-record finding; treat silence as
unmeasured). Knowledge-graph writes historically failed-silently on hot paths; census-era findings
routed through the disposal/fix pipeline.

## Deploy topology

**Fly.io**, four apps as of 10-14: `piper-morgan` (the web app, `fly.toml`), `piper-morgan-mcp` (the hosted MCP server, `fly.mcp.toml`; deployed only via `scripts/deploy-mcp.sh`, v12 on 10-13), `piper-morgan-gh-mcp` (the github-mcp-server v1.5.0 sidecar, `deploy/fly/github-mcp.fly.toml`) and `piper-morgan-chroma` (`deploy/fly/chroma.fly.toml`). Local docker-compose for dev. Staging is promote-the-image on Fly (ADR-007 superseded 09-29). ⚠️ **The
deployment layer diverges from config files by design**: fly secrets carry env that no file shows
(the flip-1 lesson — a config-file census cannot see deployment state; verify on-machine).
`origin/production` is NOT what's deployed; builds trigger from `main`.

## Census hazards (for whoever measures next)

1. **Suppression rules make features mis-censusable** — e.g. the Radar placeholder renders only
   above real held state; an empty dashboard shows the *specified* nothing (#1635 lesson:
   deployment claims verify by commit-ancestry, not by looking at one rendered page).
2. **"Loaded" ≠ invoked** (parent-`__init__` side effects); **"dead" needs the live-code
   mechanism check** (B3 rule — code doesn't cite the patterns it implements).
3. **The denominator is services/ + web/ + main.py** — cli/, scripts/, alembic/ are outside it.

## Change discipline

Entry-point, classification, or topology changes update this file same-commit (the currency claim
above). Counts cite their source and date — an undated count is a rumor.
