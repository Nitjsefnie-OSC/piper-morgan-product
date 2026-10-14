"""
Consciousness Wrapper for Files and Projects

Transforms file/project listings into conscious narrative expression.
Issue: #635 CONSCIOUSNESS-TRANSFORM: Files/Projects
ADR: ADR-056 Consciousness Expression Patterns
"""

from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

from services.consciousness.validation import validate_mvc


def _format_relative_time(dt: datetime) -> str:
    """Convert datetime to conversational relative time."""
    if dt is None:
        return "some time ago"

    now = datetime.now()
    if dt.tzinfo:
        now = datetime.now(dt.tzinfo)

    diff = now - dt

    if diff < timedelta(minutes=5):
        return "just now"
    elif diff < timedelta(hours=1):
        mins = int(diff.total_seconds() / 60)
        return f"about {mins} minutes ago"
    elif diff < timedelta(hours=24):
        hours = int(diff.total_seconds() / 3600)
        return f"about {hours} {'hour' if hours == 1 else 'hours'} ago"
    elif diff < timedelta(days=2):
        return "yesterday"
    elif diff < timedelta(days=7):
        days = diff.days
        return f"{days} days ago"
    else:
        return dt.strftime("%b %d")


def _fix_mvc_gaps(narrative: str, mvc_result, skip_invitation: bool = False) -> str:
    """Fix MVC compliance gaps in narrative.

    ``skip_invitation`` (#2010): the project list deliberately carries no
    closing question (nothing is armed to keep it), so the generic
    "Want me to tell you more..." filler must not be re-added.
    """
    sections = [narrative]

    if "identity" in mvc_result.missing:
        # Prepend identity statement
        sections.insert(0, "I looked at your projects.")

    if "invitation" in mvc_result.missing and not skip_invitation:
        # Append invitation
        sections.append("\nWant me to tell you more about any of these?")

    if "uncertainty" in mvc_result.missing:
        # Add uncertainty marker
        first = sections[0]
        # Keep the pronoun "I" / "I'm" capitalised ("I think I'm", not "i'm").
        if not (first.startswith("I ") or first.startswith("I'")):
            first = first[0].lower() + first[1:]
        sections[0] = "I think " + first

    return "\n".join(sections)


# #2010: the ONE empty-state string and offer hint for "list my projects",
# shared with the manage_portfolio list branch (#852) in
# services/intent_service/canonical_handlers.py so the two renderers cannot
# drift apart. The hint arms ConversationContext.last_offer (via
# IntentService._track_offer_hint) so a "yes" starts the add-project flow.
EMPTY_PROJECTS_MESSAGE = "You don't have any active projects yet. Would you like to add one?"
EMPTY_PROJECTS_OFFER_TEXT = "Would you like to add one?"
EMPTY_PROJECTS_CONTINUATION_HINT = "add a new project"


def empty_projects_offer_hint() -> Dict[str, str]:
    """Fresh offer_hint dict for the empty-projects state (#852 / #2010)."""
    return {
        "continuation_hint": EMPTY_PROJECTS_CONTINUATION_HINT,
        "offer_text": EMPTY_PROJECTS_OFFER_TEXT,
    }


def format_projects_conscious(projects: List[Dict[str, Any]]) -> str:
    """
    Format project listing with consciousness.

    Transforms from:
        "Projects:
         1. Project A
         2. Project B"

    To:
        "I'm tracking 2 projects for you.
         - Project A (active)
         - Project B (inactive)

         (the list stands on its own; no closing offer, #2010)"

    Args:
        projects: List of project dicts with 'name' and optional 'active' keys

    Returns:
        Conscious narrative string
    """
    if not projects:
        return EMPTY_PROJECTS_MESSAGE

    count = len(projects)
    active_projects = [p for p in projects if p.get("active", True)]

    sections = []

    # Opening with identity and source transparency
    if count == 1:
        sections.append("I'm tracking 1 project for you.")
    else:
        sections.append(f"I'm tracking {count} projects for you.")

    # List projects with context
    project_lines = []
    for project in projects:
        name = project.get("name", "Untitled")
        active = project.get("active", True)
        status = " (active)" if active else " (inactive)"
        project_lines.append(f"- **{name}**{status}")

    sections.append("\n".join(project_lines))

    # #2010: no closing question. "Show you the files in any of these" and
    # "recent activity" had no armed flow behind them, so a "yes" held no
    # state; a plain list is the honest ending.

    narrative = "\n\n".join(sections)

    # Validate MVC and fix if needed
    mvc_result = validate_mvc(narrative)
    if not mvc_result.passes:
        narrative = _fix_mvc_gaps(narrative, mvc_result, skip_invitation=True)

    return narrative


def format_project_detail_conscious(
    project: Dict[str, Any], recent_activity: Optional[List[Dict[str, Any]]] = None
) -> str:
    """
    Format detailed project view with consciousness.

    Args:
        project: Project dict with name, description, stats
        recent_activity: Optional list of recent activity items

    Returns:
        Conscious narrative string
    """
    name = project.get("name", "Untitled")
    description = project.get("description", "")
    file_count = project.get("file_count", 0)
    active = project.get("active", True)

    sections = []

    # Opening with identity
    status_text = "active" if active else "paused"
    sections.append(f"I'm looking at **{name}** - it's currently {status_text}.")

    # Description if available
    if description:
        sections.append(f"It looks like this project is about: {description}")

    # Stats context
    if file_count > 0:
        sections.append(f"I see {file_count} files in this project.")
    else:
        sections.append("I don't see any files yet.")

    # Recent activity if provided
    if recent_activity:
        activity_lines = ["Here's what happened recently:"]
        for item in recent_activity[:3]:
            action = item.get("action", "activity")
            target = item.get("target", "")
            when = item.get("when")
            time_str = _format_relative_time(when) if when else ""
            if time_str:
                activity_lines.append(f"- {action} {target} ({time_str})")
            else:
                activity_lines.append(f"- {action} {target}")
        sections.append("\n".join(activity_lines))

    # Dialogue invitation
    sections.append(
        "What would you like to do with this project? I can show files, "
        "recent changes, or help with something specific."
    )

    return "\n\n".join(sections)
