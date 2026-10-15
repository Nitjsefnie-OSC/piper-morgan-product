"""
Consciousness Expression Framework

This module provides tools for transforming data-driven output into
conscious expression that feels like interaction with an embodied AI.

Created: January 21, 2026
Issue: #407 MUX-VISION-STANDUP-EXTRACT
ADR: ADR-056 Consciousness Expression Patterns

Usage:
    from services.consciousness import validate_mvc

    # Validate output meets MVC requirements
    result = validate_mvc(output)

#2011 (2026-10-14, Arch): the standup narrative chain (``injection.py``:
inject_consciousness / construct_narrative / ensure_mvc, and its copy in
``templates.py``) had no consumer outside this package and was deleted.
"""

from services.consciousness.auth_consciousness import (
    format_account_inactive_conscious,
    format_invalid_credentials_conscious,
    format_login_success_conscious,
    format_logout_success_conscious,
    format_password_changed_conscious,
    format_session_expired_conscious,
    format_settings_saved_conscious,
)
from services.consciousness.cli_consciousness import (
    format_cli_error_conscious,
    format_cli_progress_conscious,
    format_cli_success_conscious,
    format_ready_conscious,
    format_services_ready_conscious,
    format_shutdown_conscious,
    format_startup_conscious,
)

# #1754: format_chitchat/farewell/thanks_conscious deleted with
# ConversationHandler's live-unreachable non-greeting branches.
from services.consciousness.conversation_consciousness import format_greeting_conscious
from services.consciousness.error_consciousness import (
    enhance_error_pattern,
    format_conversational_error_conscious,
)
from services.consciousness.files_consciousness import (
    format_projects_conscious,
)
from services.consciousness.learning_consciousness import (
    format_patterns_learned_conscious,
)
from services.consciousness.search_consciousness import (
    format_no_results_conscious,
    format_search_error_conscious,
    format_search_results_conscious,
)
from services.consciousness.todo_consciousness import (
    format_next_todo_conscious,
    format_todo_completed_conscious,
    format_todo_created_conscious,
    format_todo_deleted_conscious,
    format_todo_list_conscious,
)
from services.consciousness.validation import MVCResult, validate_mvc

__all__ = [
    # Core framework
    "validate_mvc",
    "MVCResult",
    # Todo consciousness (Phase 3)
    "format_todo_list_conscious",
    "format_todo_created_conscious",
    "format_todo_completed_conscious",
    "format_todo_deleted_conscious",
    "format_next_todo_conscious",
    # Conversation consciousness (Phase 3; greeting-only since #1754)
    "format_greeting_conscious",
    # Error consciousness (Wave 1)
    "format_conversational_error_conscious",
    "enhance_error_pattern",
    # CLI consciousness (Wave 2)
    "format_startup_conscious",
    "format_ready_conscious",
    "format_shutdown_conscious",
    "format_cli_success_conscious",
    "format_cli_error_conscious",
    "format_cli_progress_conscious",
    "format_services_ready_conscious",
    # Search consciousness (Issue #634)
    "format_search_results_conscious",
    "format_no_results_conscious",
    "format_search_error_conscious",
    # Files/Projects consciousness (Issue #635)
    "format_projects_conscious",
    # Learning consciousness (Issue #636)
    "format_patterns_learned_conscious",
    # Auth/Settings consciousness (Issue #637)
    "format_login_success_conscious",
    "format_logout_success_conscious",
    "format_session_expired_conscious",
    "format_invalid_credentials_conscious",
    "format_settings_saved_conscious",
    "format_account_inactive_conscious",
    "format_password_changed_conscious",
]
