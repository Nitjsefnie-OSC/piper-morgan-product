"""#2129 (CXO, 2026-10-22): the noun agrees with the count. Served: "(1 meetings, 60 min)",
"Light week with 1 items completed", "You have 1 active projects:". A source pin on the
exact forms that shipped, so they can't come back unguarded."""

from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SHIPPED = {
    "services/intent/intent_service.py": [
        "({meeting_count} meetings, {total_time} min)",
        "{total_completed} items completed",
    ],
    "services/intent_service/canonical_handlers.py": [
        "{meeting_count} meetings ({meeting_hours",
        "({meeting_count} meetings scheduled today)",
        'f"You have {len(projects)} active projects:',
    ],
    "services/intent_service/todo_handlers.py": [
        "You have {len(todos)} active todos.",
    ],
}


def test_the_shipped_unguarded_plurals_are_gone():
    for rel, forms in SHIPPED.items():
        text = (REPO / rel).read_text()
        for form in forms:
            assert form not in text, f"{rel}: unguarded plural {form!r} (#2129)"
