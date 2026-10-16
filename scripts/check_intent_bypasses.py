"""
Manual scanner for intent classification bypasses (not wired into CI or a hook).

Run from the repo root: ``python scripts/check_intent_bypasses.py``. Exits 1 if
any NL-like route (path contains chat/message/talk/ask/query) never mentions
"intent" in its own body. The scan is textual: a route that reaches intent only
through a helper defined elsewhere is reported as a potential bypass.
"""

import re
import sys
from pathlib import Path

# Any HTTP verb on app./router. (websocket routes are out of scope).
_ROUTE_RE = re.compile(
    r'@(?:app|router)\.(get|post|put|delete|patch|head|options)\(\s*["\']([^"\']+)'
)
_EXEMPT = ["/health", "/metrics", "/docs", "/static", "/api/v1/personality"]
_NL_KEYWORDS = ["chat", "message", "talk", "ask", "query"]


def _route_body(content, start, matches, index):
    """Text from this route's decorator to the next route decorator (or EOF).

    The bounds come from the regex matches themselves; there is no second
    find() that could return -1 or another route's offset (#2058).
    """
    end = matches[index + 1].start() if index + 1 < len(matches) else len(content)
    return content[start:end]


def scan_text(content, filename="<text>"):
    """Return the bypass records for one file's source text."""
    bypasses = []
    matches = list(_ROUTE_RE.finditer(content))
    for i, m in enumerate(matches):
        method, path = m.group(1), m.group(2)
        if any(exempt in path for exempt in _EXEMPT):
            continue
        if not any(keyword in path.lower() for keyword in _NL_KEYWORDS):
            continue
        body = _route_body(content, m.start(), matches, i)
        if "intent" not in body.lower():
            bypasses.append(
                {
                    "file": str(filename),
                    "method": method.upper(),
                    "path": path,
                    "reason": "NL-like endpoint without intent usage",
                }
            )
    return bypasses


def check_bypasses(root="web"):
    """Scan route files under ``root`` for potential intent bypasses."""
    bypasses = []
    for file in Path(root).glob("**/*.py"):
        bypasses.extend(scan_text(file.read_text(), file))
    return bypasses


if __name__ == "__main__":
    bypasses = check_bypasses()

    if bypasses:
        print(f"❌ FOUND {len(bypasses)} POTENTIAL BYPASSES:")
        for b in bypasses:
            print(f"  {b['method']:6} {b['path']:40} ({b['file']})")
            print(f"         Reason: {b['reason']}")
        sys.exit(1)
    else:
        print("✅ NO BYPASSES DETECTED")
        sys.exit(0)
