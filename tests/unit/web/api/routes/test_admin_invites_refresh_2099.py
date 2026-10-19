"""#2099 — the Invites page refreshes its list after a mint.

xian (alpha e801b1a309, 2026-10-19): "Revoking an invite updates immediately but minting one
does not update the list yet." The page called a global ``showToast()`` that no script defines
(``/static/js/toast.js`` exposes ``Toast.success``/``Toast.error``): after a mint the codes
rendered, the toast call threw, and the ``loadInvites()`` re-read never ran. The revoke looked
fine only because its optimistic row flip ran before the same throw.

LAYER: the template source. DENOMINATOR: every toast call on the page (7), the optimistic
mint rows, and the surfaced re-read error. Not a browser render: Web's served check follows.
"""

from pathlib import Path

PAGE = Path("templates/settings_invites.html").read_text()
TOAST_JS = Path("web/static/js/toast.js").read_text()


def test_toast_js_defines_no_global_showtoast():
    # The premise of the fix: the global the page used does not exist.
    assert "showToast" not in TOAST_JS
    assert "const Toast = {" in TOAST_JS and "success(title, message" in TOAST_JS


def test_page_uses_the_toast_object_not_an_undefined_global():
    assert "showToast(" not in PAGE
    assert PAGE.count("Toast.success(") >= 3 and PAGE.count("Toast.error(") >= 5


def test_mint_shows_the_new_rows_then_rereads_and_says_when_the_reread_fails():
    assert "prependMintedRows(data.masked || [])" in PAGE
    assert "function prependMintedRows(maskedCodes)" in PAGE
    assert "body.prepend(tr)" in PAGE
    assert "Toast.error('List not refreshed'" in PAGE
    assert PAGE.index("prependMintedRows(data.masked") < PAGE.index("Toast.success('Minted'")


def test_load_failure_is_rethrown_so_callers_can_say_so():
    seam = PAGE[PAGE.index("async function loadInvites()") : PAGE.index("function prependMintedRows")]
    assert "throw error;" in seam
