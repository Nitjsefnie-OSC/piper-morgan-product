"""#2103 — no template or script calls a global ``showToast(``.

``/static/js/toast.js`` exposes only ``Toast.show/success/error/warning/info``. Ten templates and
two scripts called ``showToast(...)``: six defined a private wrapper (working but duplicated),
the rest called a global nothing defined (guarded calls silently did nothing, unguarded ones
threw a ReferenceError and skipped the rest of the handler; #2099 was that shape).

LAYER: source text. DENOMINATOR: every ``templates/**/*.html`` and ``web/static/js/*.js`` file
except ``toast.js`` itself (the 12 files listed on #2103 held 138 occurrences before the fix).
Not a browser render.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOAST_JS = ROOT / "web/static/js/toast.js"
THREE_ARG_TEMPLATES = [
    "settings_github.html",
    "settings_calendar.html",
    "settings_notion.html",
    "integrations.html",
    "settings_slack.html",
    "components/project_config_panel.html",
]


def _sources():
    files = list((ROOT / "templates").rglob("*.html")) + list((ROOT / "web/static/js").glob("*.js"))
    return [f for f in files if f != TOAST_JS]


def test_no_show_toast_calls_outside_toast_js():
    offenders = {
        str(f.relative_to(ROOT)): f.read_text().count("showToast(")
        for f in _sources()
        if "showToast(" in f.read_text()
    }
    assert offenders == {}


def test_toast_js_defines_no_global_show_toast():
    src = TOAST_JS.read_text()
    assert "window.showToast =" not in src
    assert "function showToast" not in src
    assert "const Toast = {" in src


def test_templates_that_had_the_three_argument_shape_use_toast_show():
    for name in THREE_ARG_TEMPLATES:
        text = (ROOT / "templates" / name).read_text()
        if name == "components/project_config_panel.html":
            # two-argument shape, kept its per-type titles via Toast.success/error/warning
            assert "Toast.success(" in text and "Toast.error(" in text
        else:
            assert "Toast.show(" in text, name
