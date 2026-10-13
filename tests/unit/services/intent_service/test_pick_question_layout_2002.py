"""#2002 — the numbered delete ask's closing sentence must render as its own
paragraph after the list, not as a lazy continuation inside the last
<li>. Pinned at two layers: the source string carries a blank line before
the tail, and (when node is on the path) the string rendered through the
SAME vendored marked build the chat page loads puts the tail outside every
<li>. Found by CXO on Web's served run of alpha b713b91cb5 (2026-10-13).
"""

from __future__ import annotations

import pathlib
import shutil
import subprocess

import pytest

from services.intent_service.delete_todo_pick import render_pick_question

ROOT = pathlib.Path(__file__).resolve().parents[4]
VENDORED_MARKED = ROOT / "web" / "static" / "vendor" / "marked-15.0.12.min.js"

_RENDER_JS = r"""
const fs = require('fs');
const vm = require('vm');
const src = fs.readFileSync(process.argv[1], 'utf8');  // node -e: argv[1] is the first extra arg
const ctx = { window: {}, self: {} }; ctx.globalThis = ctx;
vm.createContext(ctx); vm.runInContext(src, ctx);
const marked = ctx.marked || ctx.window.marked || ctx.self.marked;
process.stdout.write(marked.parse(fs.readFileSync(0, 'utf8')));
"""

TAIL = "Say the number or the name, or 'never mind' to leave them alone."


class TestSourceString:
    @pytest.mark.parametrize("reasked", [False, True])
    def test_blank_line_separates_list_from_tail(self, reasked):
        q = render_pick_question(
            "reminder", ["alpha one", "alpha two", "alpha three"], reasked=reasked
        )
        lines = q.splitlines()
        assert lines[-1] == TAIL
        assert (
            lines[-2] == ""
        ), "the tail must be preceded by a blank line (Markdown paragraph break)"
        assert lines[-3] == "3. alpha three"

    def test_more_tail_keeps_the_blank_line(self):
        q = render_pick_question("todo", ["a", "b"], more=4)
        lines = q.splitlines()
        assert lines[-2] == ""
        assert lines[-1].startswith("(+4 more — say 'show my todos' for the full list.) ")


def _render(text: str) -> str:
    node = shutil.which("node")
    if node is None or not VENDORED_MARKED.exists():
        pytest.skip("node or the vendored marked build is not available here")
    proc = subprocess.run(
        [node, "-e", _RENDER_JS, "--", str(VENDORED_MARKED)],
        input=text,
        capture_output=True,
        text=True,
        timeout=30,
        check=True,
    )
    return proc.stdout


class TestRenderedThroughVendoredMarked:
    def test_tail_is_outside_every_list_item(self):
        html = _render(render_pick_question("reminder", ["alpha one", "alpha two", "alpha three"]))
        assert "<ol>" in html and html.count("<li>") == 3
        for item in html.split("<li>")[1:]:
            body = item.split("</li>")[0]
            assert "Say the number" not in body, body
        assert "<p>Say the number or the name, or " in html

    def test_the_bug_shape_is_what_a_missing_blank_line_produces(self):
        """Control: the pre-#2002 string (no blank line) DOES put the tail
        inside the last <li> under this marked build — the test above is
        measuring the right thing."""
        bug = "Which reminder should I delete?\n1. alpha one\n2. alpha two\n" + TAIL
        html = _render(bug)
        last_item = html.split("<li>")[-1].split("</li>")[0]
        assert "Say the number" in last_item
