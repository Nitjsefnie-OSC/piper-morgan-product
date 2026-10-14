"""
Consciousness Wrapper for Files and Projects

Transforms file/project listings into conscious narrative expression.
Issue: #635 CONSCIOUSNESS-TRANSFORM: Files/Projects
ADR: ADR-056 Consciousness Expression Patterns
"""

from typing import Any, Dict, List

from services.consciousness.validation import validate_mvc


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
