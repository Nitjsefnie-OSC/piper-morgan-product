"""
Consciousness Wrapper for Files and Projects

Transforms file/project listings into conscious narrative expression.
Issue: #635 CONSCIOUSNESS-TRANSFORM: Files/Projects
ADR: ADR-056 Consciousness Expression Patterns
"""

from typing import Any, Dict, List, Optional

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


# #2010: the ONE empty-state message and offer for "list my projects",
# shared by both renderers so they cannot drift apart:
# IntentService._handle_projects_query (arms the offer directly via
# set_pending_offer) and the manage_portfolio list branch in
# services/intent_service/canonical_handlers.py (hands it back as the
# result's "write_offer", armed at the canonical seam).
# #2035 (Arch's rule, CXO's shape B, 2026-10-15): the offer's "yes" leads to
# a WRITE, so it is a #846 one-slot store record with its own accept landing
# (add_project_clarify.offer_add_project: "yes" asks the name), never the
# #852 contextual hint it was.
#
# Functions, not module constants (Arch 2026-10-15): the unarmed-ask census
# (tests/test_architecture_enforcement.py TestUnarmedAskSiteRatchet) credits a
# module-level function through its callers (one hop) when every caller arms;
# a constant holder cannot be credited that way. Call these ONLY from a holder
# that arms the offer in the same turn. The question is written in both on
# purpose (neither calls the other, so each keeps arming callers only);
# tests/unit/services/intent/test_list_projects_offers_2010.py pins that the
# message's question IS the offer's stored question.


def empty_projects_message() -> str:
    """The empty-projects reply; its question is armed by the caller (#2010)."""
    return "You don't have any active projects yet. Would you like to add one?"


def empty_projects_offer(user_id: Optional[str] = None) -> Dict[str, Any]:
    """Fresh #846 pending-offer record for the empty-projects question
    (#2010 / #2035): "yes" lands on offer_add_project, which asks the name."""
    from services.intent_service.add_project_clarify import build_add_project_offer

    return build_add_project_offer(question="Would you like to add one?", user_id=user_id)


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

    The empty state is NOT rendered here (#2010): its "Would you like to add
    one?" must be armed in the same turn, which a formatter cannot do. Callers
    render ``empty_projects_message()`` and arm ``empty_projects_offer()``
    themselves; given an empty list, this returns a plain statement that asks
    nothing.

    Args:
        projects: List of project dicts with 'name' and optional 'active' keys

    Returns:
        Conscious narrative string
    """
    if not projects:
        return "You don't have any active projects yet."

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
