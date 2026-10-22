"""Arch's ruling (2026-10-22): one class for "a GitHub read that did not happen", on the
connector taxonomy. Two same-named classes is how a draft raised the wrong one (#1524)."""

import ast
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]


def test_exactly_one_github_read_failed_class_under_services():
    defs = []
    for f in sorted((REPO / "services").rglob("*.py")):
        for node in ast.walk(ast.parse(f.read_text())):
            if isinstance(node, ast.ClassDef) and node.name == "GitHubReadFailed":
                defs.append(str(f.relative_to(REPO)))
    assert defs == ["services/integrations/github/read_failed.py"], defs


def test_the_adapter_name_is_the_same_class():
    from services.integrations.github import read_failed
    from services.mcp.consumer import github_adapter

    assert github_adapter.GitHubReadFailed is read_failed.GitHubReadFailed


def test_reason_is_the_connector_taxonomy_and_no_credential_is_unclassified():
    from services.integrations.github.read_failed import (
        GitHubReadFailed,
        repo_unresolved,
        transport_reason,
    )
    from services.mcp.consumer.connector import DegradationReason

    assert repo_unresolved().reason is DegradationReason.REPO_UNRESOLVED
    assert transport_reason(TimeoutError()) is DegradationReason.UNREACHABLE
    assert transport_reason(RuntimeError()) is None
    rf = GitHubReadFailed("x", None, repo="o/r", detail="no_credential")
    assert rf.reason_code == "unclassified" and rf.repo == "o/r"
