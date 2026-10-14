---
last_updated: 2026-10-14
currency_claim: updated same-commit with any migration or change to services/database/models.py; verified against main d00ce14774 (alembic head p1522drop)
max_age_days: 60
---

# Piper Morgan 1.0 - Data Model Document

> **Living core doc #4** (see `reviews/2026-08-architectural-review/living-core-docs.md`). Owner: Lead. Ground truth is `services/database/models.py` (46 tables as of 2026-10-14) and `alembic/versions/`; if this page and the code disagree, the code wins and this page is stale.

## Overview

This document describes the complete data model for Piper Morgan, including domain models, database schema, and the mapping between them. The system follows a domain-first approach where business logic drives technical implementation.

**Persisted vs domain-only**: not every domain dataclass below has a table. `Product`, `Feature`, `Stakeholder`, `Intent`, `Task` and `Event` are domain-only (their tables were dropped in #1797 or never existed; see [Removed and never-persisted](#removed-and-never-persisted)). The persisted set is the inventory under [Database Schema](#database-schema).

## Model Distinctions

### Product vs Project

- **Product**: What you're building/managing (domain concept)
- **Project**: PM workspace with tool integrations (configuration)

### Database vs Domain Models

- **ProjectDB**: SQLAlchemy ORM model for persistence
- **Project**: Domain model for business logic
- Always convert via `.to_domain()` at repository boundary

### Relationship Loading

- Async SQLAlchemy requires eager loading
- Use `selectinload()` for one-to-many relationships
- Load all needed relationships in repository methods

## Domain Models

> **📋 For Complete Domain Model Documentation**: See [Models Architecture Hub](models/models-architecture.md) - comprehensive documentation of all 39 domain models organized by technical layers with DDD purity warnings, usage patterns, and cross-references.
>
> **This section** focuses on database schema mapping and persistence concerns. For pure domain logic and field definitions, use the Models Architecture Hub.

### Core Entities

#### Product

Represents a product being managed. **Domain-only**: no `products` table (dropped in #1797). `Project` no longer extends it.

```python
@dataclass
class Product:
    """A product being managed"""

    id: str = field(default_factory=lambda: str(uuid4()))
    name: str = ""
    vision: str = ""
    strategy: str = ""
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    features: list["Feature"] = field(default_factory=list)
    stakeholders: list["Stakeholder"] = field(default_factory=list)
    metrics: list[Any] = field(default_factory=list)
    work_items: list["WorkItem"] = field(default_factory=list)
```

#### Project

A PM workspace with tool integrations and linked repositories. Persisted as `projects` (`ProjectDB`); owner-scoped, with per-project sharing and a lifecycle state.

```python
@dataclass
class Project:
    """A PM project with multiple tool integrations"""

    id: str = field(default_factory=lambda: str(uuid4()))
    owner_id: str = ""
    name: str = ""
    description: str = ""
    integrations: list[ProjectIntegration] = field(default_factory=list)
    repositories: list["Repository"] = field(default_factory=list)
    shared_with: list[SharePermission] = field(default_factory=list)
    is_default: bool = False
    is_archived: bool = False
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    mux_ownership: Optional[OwnershipMetadata] = None
    lifecycle_state: Optional[LifecycleState] = None
```

#### ProjectIntegration

Configuration for external system integrations. Persisted as `project_integrations`. `validate_config()` (e.g. GitHub requires a string `repository` key) lives on the dataclass.

```python
@dataclass
class ProjectIntegration:
    """Integration configuration for a project"""

    type: IntegrationType
    id: str = field(default_factory=lambda: str(uuid4()))
    project_id: str = ""
    name: str = ""
    config: Dict[str, Any] = field(default_factory=dict)
    is_active: bool = True
    created_at: datetime = field(default_factory=datetime.now)
    project: Optional["Project"] = None
```

#### Feature

A feature or capability within a product. **Domain-only**: no `features` table (dropped in #1797).

```python
@dataclass
class Feature:
    """A feature or capability"""

    id: str = field(default_factory=lambda: str(uuid4()))
    name: str = ""
    description: str = ""
    hypothesis: str = ""
    acceptance_criteria: list[str] = field(default_factory=list)
    status: str = "draft"
    product_id: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    lifecycle_state: Optional[LifecycleState] = None
    lifecycle_history: list[LifecycleTransition] = field(default_factory=list)
    dependencies: list["Feature"] = field(default_factory=list)
    risks: list[Any] = field(default_factory=list)
    work_items: list["WorkItem"] = field(default_factory=list)
```

#### Stakeholder

Someone with interest in the product. **Domain-only**: no `stakeholders` table (dropped in #1797).

```python
@dataclass
class Stakeholder:
    """Someone with interest in the product"""

    id: str = field(default_factory=lambda: str(uuid4()))
    name: str = ""
    email: Optional[str] = None
    role: str = ""
    interests: list[str] = field(default_factory=list)
    influence_level: int = 1
    satisfaction: Optional[float] = None
    created_at: datetime = field(default_factory=datetime.now)
```

#### WorkItem

Universal work item that can map to any external system. Persisted as `work_items`. `product_id` and `feature_id` are plain string columns (the FKs went with the dropped tables); the domain class carries both `metadata` and `item_metadata`, the table only `item_metadata`. `work_items` has no owner column.

```python
@dataclass
class WorkItem:
    """Universal work item - can be from any system"""

    id: str = field(default_factory=lambda: str(uuid4()))
    title: str = ""
    description: str = ""
    type: str = "task"
    status: str = "open"
    priority: str = "medium"
    labels: list[str] = field(default_factory=list)
    assignee: Optional[str] = None
    project_id: Optional[str] = None
    source_system: str = ""
    external_id: str = ""
    external_url: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    updated_at: Optional[datetime] = None
    feature_id: Optional[str] = None
    external_refs: Optional[Dict[str, Any]] = None
    product_id: Optional[str] = None
    item_metadata: Optional[Dict[str, Any]] = None
    created_at: datetime = field(default_factory=datetime.now)
    lifecycle_state: Optional[LifecycleState] = None
    lifecycle_history: list[LifecycleTransition] = field(default_factory=list)
    feature: Optional["Feature"] = None
    product: Optional["Product"] = None
```

### Intent System

#### Intent

User intent parsed from natural language. **Domain-only**: no `intents` table (dropped in #1797); a workflow keeps only `intent_id` as a plain string.

```python
@dataclass
class Intent:
    """User intent parsed from natural language"""

    category: IntentCategory
    action: str
    id: str = field(default_factory=lambda: str(uuid4()))
    context: Dict[str, Any] = field(default_factory=dict)
    confidence: float = 0.0
    original_message: str = ""
    workflow_id: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
    workflow: Optional["Workflow"] = None
```

### Conversation System (PM-034 Phase 3)

#### Conversation

A conversational session. Persisted as `conversations`, whose `context`, `topics` and `preview` columns are encrypted at rest. The table also carries `owner_id`, `topics`, `preview`, `is_private`, `turn_count` that the dataclass does not mirror one-to-one.

```python
@dataclass
class Conversation:
    """Domain model for conversational interactions"""

    id: str = field(default_factory=lambda: str(uuid4()))
    user_id: UUID = ""
    session_id: str = ""
    title: str = ""
    context: Dict[str, Any] = field(default_factory=dict)
    is_active: bool = True
    lifecycle_state: ConversationLifecycleState = ConversationLifecycleState.ACTIVE
    archived_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    last_activity_at: Optional[datetime] = None
    mux_ownership: Optional[OwnershipMetadata] = None
```

#### ConversationTurn

Individual turn within a conversation, supporting anaphoric reference resolution. Persisted as `conversation_turns`; message text and the JSON context columns are encrypted at rest.

```python
@dataclass
class ConversationTurn:
    """Domain model for individual turns in a conversation"""

    id: str = field(default_factory=lambda: str(uuid4()))
    conversation_id: str = ""
    turn_number: int = 0
    user_message: str = ""
    assistant_response: str = ""
    intent: Optional[str] = None
    entities: list[str] = field(default_factory=list)
    references: Dict[str, str] = field(default_factory=dict)
    context_used: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)
    processing_time: Optional[float] = None
    created_at: datetime = field(default_factory=datetime.now)
    completed_at: Optional[datetime] = None
```

### Workflow System

#### Workflow

Orchestrates multi-step processes. Persisted as `workflows`. `tasks` and `intent` are in-memory relations only: there is no `tasks` or `intents` table, and `workflows.intent_id` is a plain string.

```python
@dataclass
class Workflow:
    """Workflow definition and state"""

    type: WorkflowType
    id: str = field(default_factory=lambda: str(uuid4()))
    status: WorkflowStatus = WorkflowStatus.PENDING
    tasks: list[Task] = field(default_factory=list)
    context: Dict[str, Any] = field(default_factory=dict)
    result: Optional[WorkflowResult] = None
    error: Optional[str] = None
    intent_id: Optional[str] = None
    output_data: Optional[Dict[str, Any]] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    input_data: Optional[Dict[str, Any]] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    intent: Optional["Intent"] = None
```

#### Task

Individual unit of work within a workflow. **Domain-only**: no `tasks` table (dropped in #1797); tasks live inside the workflow object while it runs.

```python
@dataclass
class Task:
    """Individual task within a workflow"""

    id: str = field(default_factory=lambda: str(uuid4()))
    name: str = ""
    type: TaskType = TaskType.ANALYZE_REQUEST
    status: TaskStatus = TaskStatus.PENDING
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    output_data: Optional[Dict[str, Any]] = None
    updated_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    started_at: Optional[datetime] = None
    workflow_id: Optional[str] = None
    input_data: Optional[Dict[str, Any]] = None
    created_at: datetime = field(default_factory=datetime.now)
    workflow: Optional["Workflow"] = None
```

### Event System

#### Event

Base event for system activity tracking. **Domain-only**: there is no `events` table (the old schema section describing one never matched a migration). Durable audit trails are `audit_logs` and `ethics_audit_log`.

```python
@dataclass
class Event:
    """Base event class"""

    id: str = field(default_factory=lambda: str(uuid4()))
    type: str = ""
    data: Dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)
```

## Database Schema

The ORM lives in `services/database/models.py` (`Base` from `services/database/connection.py`). **46 tables** as of 2026-10-14 (the 2026-08-11 revision described 8 persisted tables; five have since been dropped and one, `events`, never existed). Types are `String` ids unless noted; `CrossDialectUUID` / `postgresql.UUID` columns are native UUIDs on Postgres and `CHAR(36)` on SQLite so unit tests can run in memory.

### SQLAlchemy Models

#### Base Model

```python
class TimestampMixin:
    """Mixin to add created_at and updated_at timestamps to models"""
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc),
                        onupdate=lambda: datetime.now(timezone.utc))
```

Not every table uses the mixin; some declare their own timestamps.

#### Table inventory

"Owner column" is the column a row is scoped to. See [Owner scoping](#owner-scoping) for what that does and does not guarantee.

| Table | Model | Owner column | Notes |
|---|---|---|---|
| `users` | `User` | (is the principal) | unique `username`, `email`; `role`, `is_alpha`, `is_admin`, `setup_complete`, `orientation_seen`, `preferences` JSONB (#1422) |
| `user_api_keys` | `UserAPIKey` | `user_id` NN, FK | unique `(user_id, provider)`; `encrypted_secret`; int PK |
| `token_blacklist` | `TokenBlacklist` | `user_id` FK, nullable | unique `token_id`; int PK |
| `invite_tokens` | `InviteToken` | none | token is the PK; `used_by_user_id` FK |
| `password_reset_tokens` | `PasswordResetToken` | `user_id` NN, FK | token is the PK |
| `mcp_access_tokens` | `MCPAccessToken` | `user_id` NN, FK | hash-only (`token_hash`), revocable, expiring (#1462) |
| `mcp_oauth_clients` | `MCPOAuthClient` | none | DCR client registry; `client_secret` encrypted |
| `mcp_oauth_codes` | `MCPOAuthCode` | `user_id` NN, FK | `code_hash`, PKCE `code_challenge`, single use (`used_at`) |
| `mcp_oauth_refresh_tokens` | `MCPOAuthRefreshToken` | `user_id` NN, FK | `token_hash`, revocable |
| `slack_identities` | `SlackIdentity` | `owner_id` NN, FK | unique `(slack_user_id, slack_team_id)` (#1466, ADR-079) |
| `slack_link_codes` | `SlackLinkCode` | `user_id` NN, FK | code is the PK; `expires_at`, `used_at` |
| `slack_link_attempts` | `SlackLinkAttempt` | none | attempt ledger keyed by Slack user and team; int PK |
| `audit_logs` | `AuditLog` | `user_id` FK, nullable | |
| `ethics_audit_log` | `EthicsAuditLogDB` | `user_id` (no FK) | `entry_id` PK, `redacted` flag |
| `secure_credentials` | `SecureCredentialDB` | none | keyed by composed `KeychainService` name; `encrypted_value` |
| `connector_configs` | `ConnectorConfig` | `owner_id` NN, FK | unique `(owner_id, connector)`; also `tenant_id` |
| `connector_bindings` | `ConnectorBinding` | `owner_id` NN, FK | unique `(owner_id, connector)`; also `tenant_id` |
| `personalization_contexts` | `PersonalizationContext` | `owner_id` NN, FK | unique per owner; also `tenant_id` |
| `projects` | `ProjectDB` | `owner_id` FK, nullable | unique `(owner_id, name)`; `shared_with`, `is_archived`, `lifecycle_state` |
| `project_integrations` | `ProjectIntegrationDB` | `owner_id` FK, nullable | `project_id` FK to `projects` |
| `repositories` | `RepositoryDB` | `owner_id` NN, FK | unique `(owner_id, provider, full_name)` |
| `project_repository_links` | `ProjectRepositoryLinkDB` | none | unique `(project_id, repository_id)` |
| `work_items` | `WorkItem` | none | `product_id` / `feature_id` plain strings; `lifecycle_state`, `external_refs` |
| `workflows` | `Workflow` | none | `intent_id` plain string; JSON `context` / `result` |
| `uploaded_files` | `UploadedFileDB` | `owner_id` NN, FK | |
| `documents` | `DocumentDB` | `owner_id` FK, nullable | unique `chromadb_base_id`; `is_global_pm_domain` (#1238) |
| `artifacts` | `ArtifactDB` | `owner_id` NN (string, no FK) | `content` encrypted; `lifecycle_state` (#952) |
| `conversations` | `ConversationDB` | `user_id` NN + `owner_id` nullable | `lifecycle_state` (default `active`), `archived_at`, `deleted_at`; `context` / `topics` / `preview` encrypted |
| `conversation_turns` | `ConversationTurnDB` | none (via `conversation_id`) | text and JSON columns encrypted |
| `conversation_links` | `ConversationLinkDB` | none (via `conversation_id`) | links between turns |
| `conversational_memory_entries` | `ConversationalMemoryEntryDB` | `user_id` NN + `owner_id` nullable | ADR-054 layer 1 |
| `standup_conversations` | `StandupConversationDB` | `user_id` NN + `owner_id` nullable | JSONB turns, context, versions |
| `session_activity` | `SessionActivityDB` | `owner_id` NN (string, soft refs) | ADR-078 D1 ledger of external artifacts a session created (#1394) |
| `insights` | `InsightDB` | `user_id` NN + `owner_id` nullable | `is_deleted` soft delete |
| `knowledge_nodes` | `KnowledgeNodeDB` | `owner_id` FK, nullable | |
| `knowledge_edges` | `KnowledgeEdgeDB` | `owner_id` FK, nullable | FKs to `knowledge_nodes` |
| `lists` | `ListDB` | `owner_id` NN, FK | `shared_with` JSONB (role-based), `is_archived`, `project_ids` |
| `list_items` | `ListItemDB` | `owner_id` FK, nullable | unique `(list_id, item_id)` |
| `list_memberships` | `ListMembershipDB` | `owner_id` FK, nullable | unique `(list_id, todo_id)` |
| `items` | `ItemDB` | none | polymorphic base for `todo_items` (joined-table inheritance) |
| `todo_items` | `TodoDB` | `owner_id` NN, FK | `id` is FK to `items.id`; `lifecycle_state`, `assigned_to`, `reminder_date`, `external_refs` |
| `feedback` | `FeedbackDB` | `user_id` + `owner_id`, FKs, nullable | |
| `personality_profiles` | `PersonalityProfileModel` | `user_id` NN (unique) + `owner_id` nullable | |
| `learned_patterns` | `LearnedPattern` | `user_id` NN, FK | `pattern_data` encrypted (leaf-split, `action_type` plaintext) |
| `learning_settings` | `LearningSettings` | `user_id` NN, FK (unique) | |
| `user_trust_profiles` | `UserTrustProfileDB` | `user_id` NN, FK (unique) | trust stage and history |

#### Removed and never-persisted

| Table | Status |
|---|---|
| `products`, `features`, `intents`, `stakeholders`, `tasks` | Dropped by `m1797drop` (#1797). No create-table migration ever managed them; they existed only where `create_all` ran. The domain dataclasses remain. |
| `action_humanizations` | Dropped by `p1522drop` (#1522) with `services/persistence/`. |
| `events` | Never existed in the ORM or in any migration; the earlier section describing it was aspirational. |

#### Representative tables

`projects`, the owner-scoped workspace row (abridged):

```python
class ProjectDB(Base):
    __tablename__ = "projects"
    id = Column(String, primary_key=True)
    owner_id = Column(UUID, ForeignKey("users.id"))        # nullable in the model
    name = Column(String, nullable=False)
    description = Column(Text)
    shared_with = Column(JSON)                              # role-based SharePermission list
    is_default = Column(Boolean, nullable=False)
    is_archived = Column(Boolean, nullable=False)
    lifecycle_state = Column(String(50), nullable=True)
    # UniqueConstraint("owner_id", "name", name="uq_projects_owner_name")
```

`session_activity`, the ADR-078 D1 ledger (abridged):

```python
class SessionActivityDB(Base):
    __tablename__ = "session_activity"
    id, conversation_id, owner_id    # String, NOT NULL
    turn_id                          # nullable soft ref
    action_type, target_ref          # target_ref like "owner/repo#107"; NOT NULL
    target_title, created_at
    # Index("idx_session_activity_owner_conv", owner_id, conversation_id, created_at)
```

It holds external pointers, not content. `owner_id` is NOT NULL and `SessionActivityRepository` always keys its WHERE on it.

### Cross-cutting rules

#### Owner scoping

Rows that belong to a user carry an owner column and repositories filter on it (ADR-070, ADR-071 D2, ADR-079). Two facts matter:

- **Two generations coexist.** Older tables have a string `user_id`; ADR-071 D2 added a UUID `owner_id` alongside it (additive, FK-less, nullable) on `conversations`, `conversational_memory_entries`, `standup_conversations`, `insights` and `personality_profiles`. Newer tables are `owner_id` only. Column types differ across tables (`String`, `UUID`, `CHAR(36)`).
- **The database does not enforce it.** There is no row-level security; scoping is the repository `WHERE` clause. `projects.owner_id`, `documents.owner_id`, `knowledge_*`, `list_items`, `list_memberships` and `project_integrations` allow NULL owners. `work_items`, `workflows`, `items`, `conversation_turns` and `conversation_links` have no owner column and inherit it, if at all, from a parent.

#### Lifecycle and deletion

There is no single soft-delete mechanism. `lifecycle_state` (the `LifecycleState` enum from `services/mux/lifecycle.py`, stored as a string) exists on `work_items`, `projects`, `artifacts`, `conversations` and `todo_items`. Separate flags: `projects.is_archived`, `lists.is_archived`, `insights.is_deleted`, `conversations.archived_at` / `deleted_at`. Other tables delete rows physically.

#### Encryption at rest

Field-level AES-256-GCM with a per-context HKDF subkey (`services/security/field_encryption.py`, #358). Two mechanisms:

- **ORM column types** `EncryptedString` / `EncryptedJSON` (`services/security/encrypted_types.py`): `mcp_oauth_clients.client_secret`, `artifacts.content`, `conversations.{context,topics,preview}`, `conversation_turns.{user_message,assistant_response,entities,references,context_used,metadata}`, `learned_patterns.pattern_data` (leaf-split; `action_type` stays plaintext). The context label is the `table.column` string.
- **Service-level encryption into plain text columns**: `user_api_keys.encrypted_secret` and `secure_credentials.encrypted_value`. A user's key is encrypted under context `user_api_keys.secret`, except GitHub providers (`github`, `github_mcp_oauth`), which use `user_api_keys.secret.github` (#1982, `services/security/user_api_key_service.py`). The legacy shared-context read fallback for GitHub rows is off (`GITHUB_LEGACY_CONTEXT_FALLBACK = False`) since the 2026-10-13 re-encryption reported zero legacy rows on alpha.

Two process modes (#1982): the web app holds `ENCRYPTION_MASTER_KEY` and derives any context; the MCP app holds only pre-derived, decrypt-only subkeys in `ENCRYPTION_SCOPED_SUBKEYS` (today, the GitHub context), refuses every encrypt and every unlisted context, and fails closed at startup if a master key is present (`services/mcp/server/app.py`).

Inbound bearer credentials are never stored raw: `mcp_access_tokens.token_hash`, `mcp_oauth_codes.code_hash` and `mcp_oauth_refresh_tokens.token_hash` hold SHA-256 digests. `invite_tokens` and `password_reset_tokens` store the token itself as the primary key.

## Enumerations

Canonical definitions: `services/shared_types.py`. Values below are the current members.

### IntentCategory

```python
class IntentCategory(Enum):
    EXECUTION = "execution"
    ANALYSIS = "analysis"
    SYNTHESIS = "synthesis"
    STRATEGY = "strategy"
    PLANNING = "planning"
    REVIEW = "review"
    LEARNING = "learning"
    QUERY = "query"
    CONVERSATION = "conversation"
    IDENTITY = "identity"
    DISCOVERY = "discovery"
    TEMPORAL = "temporal"
    STATUS = "status"
    PRIORITY = "priority"
    GUIDANCE = "guidance"
    TRUST = "trust"
    MEMORY = "memory"
    PORTFOLIO = "portfolio"
    PROVENANCE = "provenance"
    UNKNOWN = "unknown"
```
See `intent-categories-reference.md` for what each category means.

### WorkflowType

```python
class WorkflowType(Enum):
    CREATE_FEATURE = "create_feature"
    ANALYZE_METRICS = "analyze_metrics"
    CREATE_TICKET = "create_ticket"
    CREATE_TASK = "create_task"
    REVIEW_ITEM = "review_item"
    GENERATE_REPORT = "generate_report"
    PLAN_STRATEGY = "plan_strategy"
    LEARN_PATTERN = "learn_pattern"
    ANALYZE_FEEDBACK = "analyze_feedback"
    CONFIRM_PROJECT = "confirm_project"
    SELECT_PROJECT = "select_project"
    ANALYZE_FILE = "analyze_file"
    LIST_PROJECTS = "list_projects"
    MULTI_AGENT = "multi_agent"
```

### IntegrationType

```python
class IntegrationType(Enum):
    GITHUB = "github"
    JIRA = "jira"
    LINEAR = "linear"
    SLACK = "slack"
```

### WorkflowStatus

```python
class WorkflowStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
```

### TaskType

```python
class TaskType(Enum):
    ANALYZE_REQUEST = "analyze_request"
    EXTRACT_REQUIREMENTS = "extract_requirements"
    IDENTIFY_DEPENDENCIES = "identify_dependencies"
    CREATE_WORK_ITEM = "create_work_item"
    UPDATE_WORK_ITEM = "update_work_item"
    NOTIFY_STAKEHOLDERS = "notify_stakeholders"
    GENERATE_DOCUMENT = "generate_document"
    CREATE_SUMMARY = "create_summary"
    GITHUB_CREATE_ISSUE = "github_create_issue"
    GENERATE_GITHUB_ISSUE_CONTENT = "generate_github_issue_content"
    ANALYZE_GITHUB_ISSUE = "analyze_github_issue"
    ANALYZE_FILE = "analyze_file"
    SUMMARIZE = "summarize"
    LIST_PROJECTS = "list_projects"
    EXTRACT_WORK_ITEM = "extract_work_item"
    JIRA_CREATE_TICKET = "jira_create_ticket"
    SLACK_SEND_MESSAGE = "slack_send_message"
    PROCESS_USER_FEEDBACK = "process_user_feedback"
    ANALYZE_DOCUMENT = "analyze_document"
    QUESTION_ANSWER_DOCUMENT = "qa_document"
    COMPARE_DOCUMENTS = "compare_documents"
    SUMMARIZE_DOCUMENT = "summarize_document"
    SEARCH_DOCUMENTS = "search_documents"
```

### TaskStatus

```python
class TaskStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"
```

## Repository Pattern

### Base Repository

`services/database/repositories.py`. Repositories take an `AsyncSession` and a class-level `model`. They `flush` and `refresh` but **do not commit**; the commit belongs to the session scope (below).

```python
class BaseRepository:
    """Base repository with common CRUD operations"""

    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, **kwargs) -> Any: ...      # add, flush, refresh; generates a uuid4 id if absent
    async def get_by_id(self, id: str) -> Optional[Any]: ...
    async def list(self, limit: int = 100) -> List[Any]: ...
    async def update(self, id: str, **kwargs) -> Optional[Any]: ...   # mutates the ORM row (#1464)
    async def delete(self, id: str) -> bool: ...      # awaits session.delete (#1464)
```

Subclasses such as `ProjectRepository` override `get_by_id` to return **domain** objects, so mutations go through `_get_db_row` (`session.get(self.model, id)`), never through `get_by_id` (#1464).

### Domain-Specific Repositories

Classes in `services/database/repositories.py` (as of 2026-10-14): `WorkItemRepository`, `WorkflowRepository`, `ProjectRepository`, `ProjectIntegrationRepository`, `RepositoryRepository`, `KnowledgeGraphRepository`, `ConversationRepository`, `DBUserHistoryRepository`, `EthicsAuditRepository`, `InsightRepository`, `StandupConversationRepository`, `ArtifactRepository`, `SessionActivityRepository`. More live in `services/repositories/` (conversational memory, documents, files, todos, universal lists, user trust profiles). The #1797 twins' repository subgraph was deleted with their tables.

#### ProjectRepository

Owner-scoped reads take `owner_id` (and `is_admin`, which bypasses the owner filter per SEC-RBAC Phase 3):

```python
class ProjectRepository(BaseRepository):
    """Repository for Project operations"""

    model = ProjectDB

    async def get_by_id(self, project_id: str, owner_id: Optional[str] = None,
                        is_admin: bool = False) -> Optional[domain.Project]:
        filters = [ProjectDB.id == project_id]
        if owner_id and not is_admin:
            filters.append(ProjectDB.owner_id == owner_id)
        ...
```

`ProjectDB.to_domain()` and `ProjectDB.from_domain()` do the conversion at the repository boundary (see Model Distinctions).

## Data Access Patterns

### Query Pattern

For read-only operations, use Query Services that directly access repositories:

```python
# Query Service → Repository → Database
projects = await project_query_service.list_active_projects()
```

### Command Pattern

For state changes, use Workflows that orchestrate multiple operations:

```python
# Workflow → Tasks → Repositories → Database
workflow = await workflow_factory.create_from_intent(intent)
result = await orchestration_engine.execute_workflow(workflow.id)
```

### Transaction Boundaries

- Repository methods `flush` but do not commit; the unit of work is the session scope.
- `session_scope()` (`services/database/session_factory.py`) commits on clean exit and rolls back on error (#1193: it documented "automatic commit" for a long time without doing it).
- Workflows may span multiple transactions.
- There is no event-sourced audit trail: auditing is explicit rows in `audit_logs` / `ethics_audit_log`.

## Migration Strategy

### Schema Evolution

1. Use Alembic for database migrations (`alembic/versions/`, 84 files; single head `p1522drop` as of 2026-10-14).
2. Domain models drive schema changes, but the ORM models in `services/database/models.py` are what autogenerate compares against; the #1312 reconciliation guard keeps them equal to the live schema.
3. Backward compatibility for API changes
4. Zero-downtime deployment support

### Recent migrations (since the 2026-08-11 revision of this page)

| Revision | Change |
|---|---|
| `a1599admin` | `is_admin` grant for PM's beta account; zero-row guard keys on the `users` table state (not `FLY_APP_NAME`) |
| `j1394ledger` | `session_activity` table (ADR-078 D1) |
| `k1422prefs` | `users.preferences` JSONB column |
| `l1466slack` | `slack_identities`, `slack_link_codes` (plus `slack_link_attempts`) |
| `m1797drop` | drops `products`, `features`, `intents`, `stakeholders`, `tasks` (never migration-managed; `CASCADE` also dropped the two FKs on `work_items`; downgrade is a deliberate no-op) |
| `n1462mcpt` | `mcp_access_tokens` |
| `o1462oaut` | `mcp_oauth_clients`, `mcp_oauth_codes`, `mcp_oauth_refresh_tokens` |
| `p1522drop` | drops `action_humanizations` (#1522) |

### Example Migration

The shape to copy is a small, reversible-or-documented migration with its reasoning in the module docstring, e.g. `alembic/versions/m1797drop_dead_persistence_twin_tables.py`:

```python
revision = "m1797drop"
down_revision = "a1599admin"

_TABLES = ("tasks", "intents", "stakeholders", "features", "products")

def upgrade() -> None:
    for t in _TABLES:
        op.execute(f'DROP TABLE IF EXISTS "{t}" CASCADE')

def downgrade() -> None:
    # Intentionally a no-op: never migration-managed, empty everywhere.
    pass
```

## Performance Considerations

### Indexes

- Primary keys on all tables
- Foreign key indexes for joins
- Composite indexes for common queries
- Full-text search for descriptions

### Query Optimization

- Use eager loading for related data
- Pagination for large result sets
- Database-level filtering
- Connection pooling

### Caching Strategy

- Redis for frequently accessed data
- In-memory caching for session data
- Invalidation on updates
- TTL-based expiration

## Workflow Context Patterns

Workflows carry a context dictionary that is enriched automatically during creation. For GitHub workflows, the repository is injected if available.

**Example: GitHub Issue Creation Workflow Context**

```json
{
  "project_id": "proj-123",
  "project_name": "Mobile App",
  "repository": "acme/mobile-app",
  "title": "Login fails on iOS",
  "body": "Steps to reproduce...",
  "labels": ["bug", "ios"]
}
```

- The `repository` field is injected automatically if available from project context.
- Downstream handlers (e.g., GitHub issue creation) consume this context.

## WorkflowResult Model

```python
@dataclass
class WorkflowResult:
    """Result of workflow execution"""
    success: bool = False
    data: Dict[str, Any] = field(default_factory=dict)
    error: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
```

(An earlier revision of this page documented a `TaskResult` dataclass; no such class exists in `services/domain/models.py`. Task output lives in `Task.result` / `Task.output_data`.)

## Integration Configuration Examples

### GitHub Integration Example

```json
{
  "type": "github",
  "name": "Acme GitHub",
  "config": {
    "repository": "acme/mobile-app",
    "default_labels": ["bug", "ios"]
  },
  "is_active": true
}
```

### Jira Integration Example

```json
{
  "type": "jira",
  "name": "Acme Jira",
  "config": {
    "project_key": "ACME",
    "url": "https://acme.atlassian.net"
  },
  "is_active": true
}
```

### Workflow Creation with Context

For workflows that require repository context (e.g., GitHub issue creation), the context is enriched automatically:

```python
workflow = await workflow_factory.create_from_intent(intent, session_id, project_context)
# The resulting workflow.context will include 'repository' if available from project
```

### Action Humanization Model (persistence removed)

The `action_humanizations` table was dropped in #1522 (migration `p1522drop`) together with `services/persistence/`. The `ActionHumanization` dataclass (`services/domain/models.py`) still exists but has no persistence layer and no importer outside the domain module; it is dead code awaiting deletion.

## Schema Validation

### PM-056 Schema Validator Tool

The PM-056 Schema Validator tool compares field names, types, and structures between domain models (`services/domain/models.py`) and SQLAlchemy database models (`services/database/models.py`). Its `FIELD_MAPPINGS` configuration records the intentional differences so it only reports actionable drift.

**Usage:**
```bash
python tools/schema_validator.py            # validate all models
python tools/schema_validator.py --ci       # exit non-zero on critical issues
python tools/schema_validator.py --model Product
```

See `docs/internal/development/tools/legacy-tools/PM-056-schema-validator.md` for the original documentation. Run on 2026-10-14 against main `d00ce14774`: `--ci` exits 0 (no critical issues, 5 informational).

## Revision Log

- **June 28, 2025**: Added workflow context patterns, TaskResult model, ProjectIntegration config validation, integration config examples, and workflow creation with context example for GitHub integration
- **July 13, 2025**: Added Action Humanization Model for user-facing message generation
- **July 30, 2025**: Updated Phase 1A database schema changes:
  - Added `Workflow.result` and `Workflow.updated_at` columns
  - Added `Task.name` and `Task.result` columns
  - Added `Stakeholder.satisfaction` column
  - Renamed `WorkItem.metadata` to `WorkItem.item_metadata` to avoid SQLAlchemy conflicts
  - Added PM-056 Schema Validator tool documentation
- **November 22, 2025**: Updated SEC-RBAC Phase 1.4 - Shared Resource Access:
  - Added `List.owner_id` and `List.shared_with` fields for ownership and sharing
  - Added `Todo.shared_with` field (owner_id already existed) for shared access
  - Added repository methods: `share_list()`, `unshare_list()`, `get_list_for_read()`, `get_lists_shared_with_me()`
  - Implemented JSONB array operations for atomic sharing via `array_append()` and `array_remove()`
  - Read access now checks both ownership and shared_with array membership
- **November 22, 2025**: Updated SEC-RBAC Phase 2 - Role-Based Permissions:
  - Added `ShareRole` enum: VIEWER (read-only), EDITOR (can modify), ADMIN (can share)
  - Added `SharePermission` dataclass: user_id + role with serialization methods
  - Upgraded `List.shared_with` and `Todo.shared_with` from `List[str]` to `List[SharePermission]`
  - Added permission check methods: `get_user_role()`, `user_can_read()`, `user_can_write()`, `user_can_share()`
  - Created Alembic migration: 20251122_upgrade_shared_with_to_roles (converts old format to role-based)
  - Migration defaults existing shares to "viewer" role for backward compatibility
  - Updated serialization: `to_dict()` now includes full role information
- **October 14, 2026**: Brought current against main `d00ce14774` (alembic head `p1522drop`), 64 days after the previous revision:
  - Removed the `products`, `features`, `intents`, `stakeholders`, `tasks` and `events` table sections (#1797 dropped the first five; `events` never existed) and the `action_humanizations` persistence (#1522)
  - Added the table inventory (46 tables, owner column per table) and cross-cutting rules: owner scoping, lifecycle and deletion, encryption at rest (including the #1982 scoped GitHub subkey)
  - Added Slack identities and link codes, MCP access tokens, MCP OAuth authorization server tables, and the session-activity ledger (ADR-078)
  - Rewrote the domain-model field blocks from `services/domain/models.py`; refreshed the enumerations from `services/shared_types.py`
  - Corrected the repository and transaction rules to the code (repositories flush, `session_scope()` commits)
  - Replaced the fictional example migration and the nonexistent `TaskResult` with real ones

---

_Last Updated: October 14, 2026_
