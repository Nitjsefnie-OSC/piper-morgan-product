"""#2110 — the colon-and-quotes create form reads its title with a trailing repo clause.

Web's served row on 54a5ba990f (2026-10-20): `Create a GitHub issue: "Served check colon
quotes" in dinp-machine/piper-test-activity` → "What should the issue be about? …". The slot
fill's colon-quoted pattern anchored the closing quote to the end of the message, so the
repo clause the invitation's example carries made the title unreadable. The literal now
tolerates one trailing `in|for|on <repo>` clause; the repository pattern reads the clause.

LAYER: the create rail's deterministic slot fill, no LLM. DENOMINATOR: the served form, the
bare form (CXO's owed row), a repo named by URL, and the about-form unchanged.
"""

from __future__ import annotations

from services.intent.intent_service import IntentService

_fill = IntentService._slotfill_issue_request


def test_colon_quoted_title_with_a_repo_clause():
    out = _fill(
        'Create a GitHub issue: "Served check colon quotes" in dinp-machine/piper-test-activity'
    )
    assert out.get("title") == "Served check colon quotes"
    assert out.get("repository") == "dinp-machine/piper-test-activity"


def test_bare_colon_quoted_form_reads_the_title():
    out = _fill('Create a GitHub issue: "Served check bare form"')
    assert out.get("title") == "Served check bare form"
    assert "repository" not in out


def test_curly_quotes_and_for_clause():
    out = _fill("Create a ticket: “Login times out” for octocat/hello-world")
    assert out.get("title") == "Login times out"
    assert out.get("repository") == "octocat/hello-world"


def test_about_form_is_unchanged():
    out = _fill("Create an issue in octocat/hello-world about the login bug")
    assert out.get("repository") == "octocat/hello-world"
    assert (
        out.get("title") == "the login bug"
        or "title" not in out
        or "login bug" in out.get("title", "")
    )
