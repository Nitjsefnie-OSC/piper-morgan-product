# Root README review, 2026-10-19 (Docs, weekly audit #2084)

Scope: `README.md` (repository view) and `docs/README.md` (pipermorgan homepage).

- "NEW:" claims in `README.md`: `grep -n -i "NEW:"` returns 0 lines.
- Internal links: `README.md` 7 of 7 resolve, `docs/README.md` 5 of 5 resolve (python os.path.exists, relative to each file).
- Version: `docs/README.md` line 7 says v0.8.14.0, `pyproject.toml` says 0.8.14.0. Match. Release notes link resolves.
- Alpha guides `ALPHA_QUICKSTART.md`, `ALPHA_TESTING_GUIDE.md`, `ALPHA_KNOWN_ISSUES.md` exist in `docs/`. I did not read them for currency.
- `README.md` last changed 2 weeks ago (`git log -1`).
- Not done: external links not fetched, setup steps and code examples not re-run, capabilities list and roadmap section not compared with the shipped feature set. Reported as unverified rather than checked.
