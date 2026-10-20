"""#2111 — a GitHub 404 inside a JSON-RPC error is the resource, not the server.

PA's read of the closing canonical run (2026-10-20): an issue read for a missing number
answered "GitHub's MCP server is unreachable right now". The live github-mcp-server raises
the read-back of a missing issue as an ``McpError`` whose text carries GitHub's status
("… 404 Not Found"); ``_degrade_reason_for_exc`` mapped every such leaf to UNREACHABLE.
It now reads the leaf's text through ``_reason_for_tool_error``.

LAYER: the classifier against synthetic exception groups. DENOMINATOR: 404, 401 and an
unspecific McpError; the wrapped (ExceptionGroup) form; the tool-error leaf unchanged.
"""

from __future__ import annotations

from mcp.shared.exceptions import McpError
from mcp.types import ErrorData

from services.mcp.consumer.connector import DegradationReason
from services.mcp.consumer.github_adapter import GitHubMCPSpatialAdapter, GitHubToolError


def _mcp(text: str) -> McpError:
    return McpError(ErrorData(code=-32603, message=text))


def test_404_in_an_mcp_error_is_resource_not_found():
    exc = _mcp(
        "failed to get issue: GET https://api.github.com/repos/o/r/issues/99999: 404 Not Found []"
    )
    assert (
        GitHubMCPSpatialAdapter._degrade_reason_for_exc(exc) is DegradationReason.RESOURCE_NOT_FOUND
    )


def test_wrapped_in_a_task_group_still_reads_the_leaf():
    exc = ExceptionGroup("unhandled errors in a TaskGroup", [_mcp("GET …/issues/5: 404 Not Found")])
    assert (
        GitHubMCPSpatialAdapter._degrade_reason_for_exc(exc) is DegradationReason.RESOURCE_NOT_FOUND
    )


def test_401_in_an_mcp_error_is_a_stale_token():
    exc = _mcp("failed to list issues: 401 Bad credentials")
    assert GitHubMCPSpatialAdapter._degrade_reason_for_exc(exc) is DegradationReason.STALE_TOKEN


def test_an_unspecific_mcp_error_stays_unreachable():
    exc = _mcp("connection closed")
    assert GitHubMCPSpatialAdapter._degrade_reason_for_exc(exc) is DegradationReason.UNREACHABLE


def test_tool_error_leaf_keeps_its_own_reason():
    exc = GitHubToolError("GitHub answered 401 Bad credentials")  # the reason comes from the text
    assert GitHubMCPSpatialAdapter._degrade_reason_for_exc(exc) is DegradationReason.STALE_TOKEN
