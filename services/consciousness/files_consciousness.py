"""
Consciousness Wrapper for Files and Projects

Transforms file/project listings into conscious narrative expression.
Issue: #635 CONSCIOUSNESS-TRANSFORM: Files/Projects
ADR: ADR-056 Consciousness Expression Patterns
"""

from typing import Any, Dict, List

from services.consciousness.validation import validate_mvc


def _fix_mvc_gaps(narrative: str, mvc_result) -> str:
    """Fix MVC compliance gaps in narrative."""
    sections = [narrative]

    if "identity" in mvc_result.missing:
        # Prepend identity statement
        sections.insert(0, "I looked at your projects.")

    if "invitation" in mvc_result.missing:
        # Append invitation
        sections.append("\nWant me to tell you more about any of these?")

    if "uncertainty" in mvc_result.missing:
        # Add uncertainty marker
        sections[0] = "I think " + sections[0][0].lower() + sections[0][1:]

    return "\n".join(sections)


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

         Want me to show you the files in any of these?"

    Args:
        projects: List of project dicts with 'name' and optional 'active' keys

    Returns:
        Conscious narrative string
    """
    if not projects:
        return (
            "I don't see any projects set up yet. "
            "Want me to help you create one, or would you like to import an existing project?"
        )

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

    # Dialogue invitation
    sections.append(
        "Want me to show you the files in any of these, or tell you about recent activity?"
    )

    narrative = "\n\n".join(sections)

    # Validate MVC and fix if needed
    mvc_result = validate_mvc(narrative)
    if not mvc_result.passes:
        narrative = _fix_mvc_gaps(narrative, mvc_result)

    return narrative
