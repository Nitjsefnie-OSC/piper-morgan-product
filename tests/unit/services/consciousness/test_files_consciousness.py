"""Tests for files/projects consciousness wrapper. Issue #635."""


class TestProjectsConsciousness:
    """Test consciousness wrapper for project listings."""

    def test_projects_list_has_identity(self):
        """Project listing must have identity voice."""
        from services.consciousness.files_consciousness import format_projects_conscious

        projects = [
            {"name": "piper-morgan", "active": True},
            {"name": "side-project", "active": False},
        ]
        output = format_projects_conscious(projects)
        assert "I" in output or "I'" in output, "Should have identity"

    def test_projects_list_has_no_unarmed_invitation(self):
        """#2010: the list ends plainly; a closing offer nothing keeps is a broken promise."""
        from services.consciousness.files_consciousness import format_projects_conscious

        projects = [{"name": "project1", "active": True}]
        output = format_projects_conscious(projects)
        assert "?" not in output, "closing question dropped (#2010)"

    def test_projects_highlights_active(self):
        """Active project should be emphasized."""
        from services.consciousness.files_consciousness import format_projects_conscious

        projects = [
            {"name": "active-one", "active": True},
            {"name": "inactive", "active": False},
        ]
        output = format_projects_conscious(projects)
        assert "active-one" in output

    def test_no_projects_has_identity(self):
        """No projects message should have identity."""
        from services.consciousness.files_consciousness import (
            empty_projects_message,
            format_projects_conscious,
        )

        # #2010: the empty state is the shared #852 string (one source),
        # rendered by callers that arm it; the formatter itself never asks.
        assert (
            empty_projects_message()
            == "You don't have any active projects yet. Would you like to add a project?"
        )
        assert "?" not in format_projects_conscious([])


class TestMVCCompliance:
    """Test MVC (Minimum Viable Consciousness) compliance."""

    def test_projects_passes_mvc(self):
        """Project listing should pass MVC validation."""
        from services.consciousness.files_consciousness import format_projects_conscious
        from services.consciousness.validation import validate_mvc

        projects = [{"name": "test-project", "active": True}]
        output = format_projects_conscious(projects)
        result = validate_mvc(output)
        # Identity stays; the invitation is deliberately absent (#2010).
        assert result.checks["identity"], f"Missing identity in: {output}"
        assert "?" not in output
