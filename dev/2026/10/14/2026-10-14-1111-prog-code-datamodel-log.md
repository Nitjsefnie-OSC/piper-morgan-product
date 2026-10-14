# Session Log: 2026-10-14-1111-prog-code-datamodel

**Role**: Coding Agent (prog-code), for Lead Developer
**Model**: Claude Sonnet 5.5
**Date**: Wednesday, October 14, 2026, 11:11 PDT
**Branch**: claude/lead-datamodel-refresh (worktree lead-datamodel), base origin/main d00ce14774

## Task

Bring `docs/internal/architecture/current/data-model.md` current (60-day rule; last touched 2026-08-11) against the schema on main.

## Ground truth (2026-10-14, main d00ce14774)

- Method: imported `services.database.models`, enumerated `Base.metadata.tables` (46 tables; matches `git grep __tablename__ -- services` = 46); alembic head `p1522drop` (single head, 84 version files).
- Migrations since 2026-08-11 in the chain: a1599admin, j1394ledger (session_activity), k1422prefs (users.preferences), l1466slack (slack_identities/link_codes/link_attempts), m1797drop (drops products/features/intents/stakeholders/tasks), n1462mcpt, o1462oaut, p1522drop (drops action_humanizations).
- Tables (owner column): artifacts(owner_id NN) audit_logs(user_id) connector_bindings(owner_id NN) connector_configs(owner_id NN) conversation_links(-) conversation_turns(-) conversational_memory_entries(user_id NN+owner_id) conversations(user_id NN+owner_id) documents(owner_id) ethics_audit_log(user_id) feedback(user_id+owner_id) insights(user_id NN+owner_id) invite_tokens(-) items(-) knowledge_edges(owner_id) knowledge_nodes(owner_id) learned_patterns(user_id NN) learning_settings(user_id NN) list_items(owner_id) list_memberships(owner_id) lists(owner_id NN) mcp_access_tokens(user_id NN) mcp_oauth_clients(-) mcp_oauth_codes(user_id NN) mcp_oauth_refresh_tokens(user_id NN) password_reset_tokens(user_id NN) personality_profiles(user_id NN+owner_id) personalization_contexts(owner_id NN) project_integrations(owner_id) project_repository_links(-) projects(owner_id) repositories(owner_id NN) secure_credentials(-) session_activity(owner_id NN) slack_identities(owner_id NN) slack_link_attempts(-) slack_link_codes(user_id NN) standup_conversations(user_id NN+owner_id) todo_items(owner_id NN) token_blacklist(user_id) uploaded_files(owner_id NN) user_api_keys(user_id NN) user_trust_profiles(user_id NN) users work_items(-) workflows(-)
- Full column/FK/index dump: scratchpad `inv.txt` (not committed; reproducible with the introspection snippet over `Base.metadata`).
- Encrypted columns: grep `Encrypted(String|JSON)(` in models.py (artifacts.content, conversations x3, conversation_turns x6, learned_patterns.pattern_data, mcp_oauth_clients.client_secret); service-level: user_api_keys.encrypted_secret, secure_credentials.encrypted_value; #1982 contexts in services/security/user_api_key_service.py.

## Work

- Rewrote stale sections of data-model.md; see commit. No code changed. `tools/schema_validator.py --ci` rc 0 (5 informational). `scripts/check-concept-links.py` rc 0. lychee not installed (skipped).
- Findings left for Lead (rules, not facts): owner scoping is repository-only (no RLS), several owner columns nullable, work_items/workflows/items have none; user_id/owner_id dual generation (ADR-071 D2); `ActionHumanization` dataclass is dead code in services/domain/models.py.
