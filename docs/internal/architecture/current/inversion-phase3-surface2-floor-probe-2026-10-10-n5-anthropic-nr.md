# Inversion Phase 3 — surface-2 floor probe

Run 2026-10-11 01:25Z · 5 sample(s) per phrase · LAYER (m-43): `IntentClassifier._classify_with_reasoning` only (surface 1 bypassed, no session context, dev keychain key). Read by `scripts/inversion_phase3_deletion_gate.py` (SURFACE2_FLOOR_PROBES) to credit a category-reached row whose pattern the router does not replace: the row is OK to lose its pattern when EVERY sample lands in the expected action's own category.

served (#1620, resolved per call): anthropic:claude-sonnet-4-6

| phrase | sample | surface-2 category | surface-2 action | confidence | served |
|---|---|---|---|---|---|
| what am I working on? | 1 | STATUS | `get_project_status` | 0.95 | anthropic:claude-sonnet-4-6 |
| what am I working on? | 2 | STATUS | `get_project_status` | 0.95 | anthropic:claude-sonnet-4-6 |
| what am I working on? | 3 | STATUS | `get_project_status` | 0.95 | anthropic:claude-sonnet-4-6 |
| what am I working on? | 4 | STATUS | `get_project_status` | 0.95 | anthropic:claude-sonnet-4-6 |
| what am I working on? | 5 | STATUS | `get_project_status` | 0.95 | anthropic:claude-sonnet-4-6 |
| any upcoming milestones for this project | 1 | TEMPORAL | `meeting_time` | 0.78 | anthropic:claude-sonnet-4-6 |
| any upcoming milestones for this project | 2 | TEMPORAL | `get_milestones` | 0.82 | anthropic:claude-sonnet-4-6 |
| any upcoming milestones for this project | 3 | TEMPORAL | `meeting_time` | 0.78 | anthropic:claude-sonnet-4-6 |
| any upcoming milestones for this project | 4 | TEMPORAL | `meeting_time` | 0.78 | anthropic:claude-sonnet-4-6 |
| any upcoming milestones for this project | 5 | TEMPORAL | `meeting_time` | 0.78 | anthropic:claude-sonnet-4-6 |
| this project needs my attention today | 1 | PRIORITY | `prioritize` | 0.82 | anthropic:claude-sonnet-4-6 |
| this project needs my attention today | 2 | PRIORITY | `prioritize` | 0.82 | anthropic:claude-sonnet-4-6 |
| this project needs my attention today | 3 | PRIORITY | `prioritize` | 0.82 | anthropic:claude-sonnet-4-6 |
| this project needs my attention today | 4 | PRIORITY | `prioritize` | 0.82 | anthropic:claude-sonnet-4-6 |
| this project needs my attention today | 5 | PRIORITY | `prioritize` | 0.82 | anthropic:claude-sonnet-4-6 |
