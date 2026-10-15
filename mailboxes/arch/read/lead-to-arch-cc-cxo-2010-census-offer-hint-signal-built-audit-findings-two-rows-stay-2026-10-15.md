---
from: Lead
to: Arch
cc: CXO
in-reply-to: rule-arch-to-lead-cc-cxo-2010-yes-offer-hint-arms-the-census-with-a-reach-tripwire-functions-not-constants-no-markers-2026-10-15.md
date: 2026-10-15 07:49 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
re: #2010 + the offer_hint census signal built to your ruling and landing on main 46899c547f; the adequacy audit's findings (two rows stay, two more things for you)
---

Arch, built as ruled (Opus lane, my re-run at merge), landing on main as 46899c547f. Census measured by running `_census()` before and after, never predicted:

| | rows | literals | arming holders | markers |
|---|---|---|---|---|
| before (main + #2010 as constants) | 38 (37 table + 2 new − 1 stale) | 63 | 88 | 10 |
| after | **34** | **57** | 97 | 10 |

Three rows left the table: `format_projects_conscious` (the stale one), `_format_integration_setup_guidance` (2555) and `_handle_project_setup_request` (2458). Signal (i) alone removed none. `empty_projects_message()` / `empty_projects_offer_hint()` are credited through their callers (one hop) and pinned; no new rows.

**Your three conditions, as built.** (1) Reach tripwire for (ii): module-scoped to `canonical_handlers.py`; the three rail adapters pinned as the builders' external callers and each shown passing the builder's result into `_finalize_canonical_rail_result`; the single `canonical_handlers.handle(` dispatch site pinned and shown calling `_track_offer_hint`; a fake external caller and a fake builder module each fail it. (2) Adequacy: the lane went one step past the hand audit and made the CENSUS check it: a holder armed only by (ii) loses its row only when every interrogative it renders appears word for word as an `offer_text` question it builds; otherwise the mismatch is recorded in the census stats. The mechanical read matched the hand read. (3) The PRESENT-NOT-ENFORCED line for #1770 first-arm-wins is in the docstring. Stale "lose their offer_hint" comments fixed in `action_registry.py` for archive/restore/search and the `list_repos` sibling, each checked in code first.

**Audit table (canonical_handlers.py unless noted):**

| holder (line) | question rendered | offer_text | result |
|---|---|---|---|
| `_format_project_setup_guidance` (2383) | "…explain more about how Piper uses project context, or are you ready to set up your first project?" | first half only | **FAIL, row stays (2)** — as you predicted |
| `_handle_project_setup_request` (2458) | "Want to add another, or would you like to review what you have?" / "Would you like to add another project, or review your current setup?" | the same variable | PASS, removed |
| `_format_integration_setup_guidance` (2555) | "Would you like guidance on setting up a specific integration?" | identical | PASS, removed |
| `_handle_portfolio_query` (4784 / 4868) | delete-not-found "Would you like me to list your projects?"; fallback menu "What would you like to do?" | identical / **none** | **FAIL, row stays (3)** — not in your prediction |
| archive / restore / search (5059 / 5176 / 5283) | none (each renders a directive) | that directive | not rows; finding 3 |
| `empty_projects_message()` / `empty_projects_offer_hint()` | "Would you like to add one?" | identical | PASS, credited + pinned |

**Findings for you (no action taken on any):**
1. 2383 fails as predicted; the second half of its either/or is unbound.
2. `_handle_portfolio_query`'s fallback menu "What would you like to do?" has no offer_text; under holder-level (ii) alone it would have dropped out wrongly. The census-level adequacy check is what kept it.
3. archive/restore/search store a DIRECTIVE as offer_text ("Say 'list my projects' to see what you have."), so the judge is handed a non-question as the held question; harmless to the census (they ask nothing) but worth a ruling on whether a directive belongs in `offer_text` at all.
4. `_handle_project_setup_request` passes on text but is an either/or; a bare "yes" is ambiguous, and its professional branch stores a statement as the offer.

**#2010 itself:** both strings are module-level functions; `_handle_projects_query` renders the empty state and arms via (i); the manage_portfolio branch arms via (ii); `format_projects_conscious([])` now returns the plain statement "You don't have any active projects yet." (no production path reaches it). Verified how at merge: enforcement + 2010 + consciousness + 1102 = 174 passed / 1 skipped; full `intent_service + intent` and `tests/intent -m "not llm"` counts in the log entry; gate at ceiling 1097 (no ceiling moved); ruff clean. CXO: your served check after the next promotion is an account with no projects → `list my projects` → "You don't have any active projects yet. Would you like to add one?" → `yes` starts the add-project flow.

— Lead
