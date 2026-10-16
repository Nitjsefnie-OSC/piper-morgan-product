"""#2049 defect 2 (CXO): a tested-healthy card reads "Healthy (checked just now)",
"Healthy (checked 7:55 AM)" or "Healthy (checked Oct 15, 7:55 AM)" in the viewer's zone,
never a raw ISO UTC stamp. The route sends ``Healthy`` plus an ISO ``last_check``; the
page formats it. Layers: route function; the page's own JS under Node (skipped without
``node``). Not a browser.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import time
from datetime import datetime
from pathlib import Path
from unittest.mock import AsyncMock, patch

import pytest

from services.health.integration_health_monitor import ComponentHealth, ComponentStatus
from web.api.routes import integrations

REPO = Path(__file__).resolve().parents[3]
PAGE_SRC = (REPO / "templates/integrations.html").read_text()
needs_node = pytest.mark.skipif(shutil.which("node") is None, reason="node not on PATH")


class _Monitor:
    def __init__(self, component):
        self._component = component

    def get_component_health(self, name):
        return self._component


@pytest.mark.asyncio
async def test_route_healthy_card_is_plain_healthy_with_iso_last_check():
    comp = ComponentHealth(
        name="calendar",
        status=ComponentStatus.HEALTHY,
        last_check=time.time(),
        error_count=0,
        last_error=None,
        success_rate=1.0,
        average_latency_ms=0.0,
        metadata={},
    )
    meta = integrations.INTEGRATION_REGISTRY["calendar"]
    with (
        patch.object(
            integrations, "_get_integration_config_status", new=AsyncMock(return_value="configured")
        ),
        patch.object(integrations, "_get_health_monitor", return_value=_Monitor(comp)),
    ):
        st = await integrations._check_integration_health("calendar", meta, user_id="u1")
    assert st.status == "healthy"
    assert st.status_message == "Healthy"
    assert datetime.fromisoformat(st.last_check).tzinfo is not None


def _run(last_check: str, now: str) -> tuple[str, str, str]:
    consts = PAGE_SRC[
        PAGE_SRC.index("// Integration icons mapping") : PAGE_SRC.index(
            "// Status icons for overall health"
        )
    ]
    start = PAGE_SRC.index("function renderIntegrations(integrations) {")
    end = PAGE_SRC.index("async function testConnection(integrationName)")
    script = (
        "const out = {};\n"
        "const document = { getElementById(id) {\n"
        "  if (id === 'integrations-list') return out;\n"
        "  return null; } };\n"
        "const RealDate = Date; const FIXED = new RealDate(process.argv[2]);\n"
        "globalThis.Date = class extends RealDate {\n"
        "  constructor(...a) { if (a.length) super(...a); else super(FIXED.getTime()); }\n"
        "};\n" + consts + PAGE_SRC[start:end] + "\nconst t = new RealDate(process.argv[1]);\n"
        "renderIntegrations([{name:'calendar',display_name:'Google Calendar',status:'healthy',"
        "status_message:'Healthy',last_check:process.argv[1],can_test:true,"
        "configure_url:'/settings/integrations/calendar'}]);\n"
        "const same = t.toLocaleTimeString([], {hour:'numeric',minute:'2-digit'});\n"
        "const day = t.toLocaleDateString([], {month:'short',day:'numeric'});\n"
        "process.stdout.write(JSON.stringify({html: out.innerHTML, same, day}));\n"
    )
    res = subprocess.run(
        ["node", "-e", script, last_check, now], capture_output=True, text=True, timeout=30
    )
    assert res.returncode == 0, res.stderr
    d = json.loads(res.stdout)
    return " ".join(d["html"].split()), d["same"], d["day"]


def _line(html: str) -> str:
    return html.split('id="status-calendar">')[1].split("</span>")[0].strip()


@needs_node
def test_thirty_seconds_old_reads_just_now():
    html, _, _ = _run("2026-10-16T14:55:00Z", "2026-10-16T14:55:30Z")
    assert _line(html) == "Healthy (checked just now)"
    assert "T14:" not in html


@needs_node
def test_same_day_reads_the_viewers_clock_time():
    html, same, _ = _run("2026-10-16T14:55:00Z", "2026-10-16T14:56:30Z")
    assert _line(html) == f"Healthy (checked {same})"
    assert "T14:" not in html


@needs_node
def test_older_check_reads_short_date_and_time():
    html, same, day = _run("2026-10-14T14:55:00Z", "2026-10-16T14:56:30Z")
    assert _line(html) == f"Healthy (checked {day}, {same})"
    assert "T14:" not in html


def test_page_script_defines_the_formatter_with_an_injectable_clock():
    assert "function formatCheckedAt(iso, now)" in PAGE_SRC
