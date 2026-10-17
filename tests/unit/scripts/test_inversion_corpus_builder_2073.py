"""#2073 (Arch ruling (a), 2026-10-17): the corpus builder is the source of truth.

Pins:
  (i)  rebuilding into a temp path is byte-identical to the committed fixture, so a
       hand edit to ``tests/fixtures/inversion_corpus_phase0.yaml`` fails here; the
       fix is to move the edit into the builder and regenerate.
  (ii) the fixture parses under ``yaml.safe_load`` and the row count equals what the
       scorer's shared loader (``inversion_phase0_baseline.load_corpus``) sees.
  (iii) the row whose ``source`` carries a regex literal with embedded quotes (the
       line that failed strict parsing on main before this unit) round-trips.
"""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
FIXTURE = ROOT / "tests" / "fixtures" / "inversion_corpus_phase0.yaml"

builder = importlib.import_module("scripts.build_inversion_corpus_phase0")
sys.path.insert(0, str(ROOT / "scripts"))
p0 = importlib.import_module("inversion_phase0_baseline")


def test_rebuild_is_byte_identical_to_the_committed_fixture(tmp_path, capsys):
    out = tmp_path / "corpus.yaml"
    builder.main(out=out)
    capsys.readouterr()
    assert out.read_bytes() == FIXTURE.read_bytes(), (
        "tests/fixtures/inversion_corpus_phase0.yaml differs from the builder's output: "
        "the fixture is generated (#2073). Put the row in HAND_ROWS or the ruling in "
        "RULED_EXPECTATIONS in scripts/build_inversion_corpus_phase0.py and regenerate."
    )


def test_fixture_is_strict_yaml_and_the_scorer_sees_every_row():
    data = yaml.safe_load(FIXTURE.read_text(encoding="utf-8"))
    rows = data["corpus"]
    assert isinstance(rows, list) and len(rows) >= 400
    assert len(rows) == len(p0.load_corpus())
    for r in rows:
        assert isinstance(r["phrase"], str) and r["phrase"]
        assert isinstance(r["category"], str) and isinstance(r["expected"], str)
        assert isinstance(r["source"], str) and r["source"]
        if "expected_args" in r:
            assert isinstance(r["expected_args"], dict)


def test_regex_literal_source_round_trips():
    rows = {r["phrase"]: r for r in yaml.safe_load(FIXTURE.read_text(encoding="utf-8"))["corpus"]}
    row = rows["update my project name to Atlas"]
    assert 'literal r"\\bupdate' in row["source"], row["source"]


def test_carried_rulings_survive_a_rebuild():
    rows = {r["phrase"]: r for r in yaml.safe_load(FIXTURE.read_text(encoding="utf-8"))["corpus"]}
    assert rows["list my projects"]["expected"] == "action:list_projects"
    assert "RULED 2026-10-04 (Arch)" in rows["list my projects"]["notes"]
    miss = rows["summarize my current work and I need the archived list too"]["notes"]
    assert "RE-EXPECTED 2026-10-11" in miss and "KNOWN MISS" in miss
