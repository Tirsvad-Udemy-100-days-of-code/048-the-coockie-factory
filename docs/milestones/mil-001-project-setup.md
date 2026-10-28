# Project setup and tooling

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version (reviewed in RC-004) | [96a9a78] |

---

## Purpose

Decide whether the repository is ready to receive code: configuration, tooling, ignore rules, API documentation setup and repository metadata exist and are reviewed.

## Deliverable

`pyproject.toml` (Python 3.13 or newer, one runtime dependency `selenium`, pytest as a dev dependency), the `src/cookie_clicker_bot/` and `tests/` skeleton with `constants.py`, a Python `.gitignore` that also ignores `.env`, a `Doxyfile`, architecture decision record architecture decision record architecture decision record ADR-0001 and the description and topics on the git host repository.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pip install -e .[dev]` succeeds in a fresh `.venv` and `python -m pytest` runs (no tests collected is allowed) | Met | Not met |
| 2 | `pyproject.toml` requires Python 3.13 or newer and lists `selenium` as the only runtime dependency | Met | Not met |
| 3 | `.env` is listed in `.gitignore` and is not tracked by git | Met | Not met |
| 4 | `doxygen Doxyfile` runs without errors on the skeleton | Met | Not met |
| 5 | The git host repository shows a description and at least five topics | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First milestone |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
O2, O3, O5 in [BC-001]

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-29 - within the one-week limit of [BC-001]

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write ADR-0001 for the Selenium dependency | Record the decision to keep Selenium as the single runtime dependency, against stakeholder S03's wish for none, and the alternatives (no dependency, Playwright). | No | |
| 2 | Create pyproject.toml and the package skeleton | Python 3.13 or newer, `selenium` as runtime dependency, pytest as dev dependency, a `src/cookie_clicker_bot/` package and `tests/` folder, and a `constants.py` for the game URL, element ids and timings. | No | |
| 3 | Add Python .gitignore | Standard Python ignore rules plus `.env`, `.venv/`, Doxygen output and screenshots working folders, so no token is ever tracked. | No | |
| 4 | Add Doxyfile | Generate API documentation from the Doxygen comments in `src/` into `docs/api/`; document the command in the README later. | No | |
| 5 | Install git hooks and the plan gate | Run `framework/scripts/install-git-hooks.sh --enable-plan-gate` so a commit under `src/` or `tests/` needs a `Task: MIL-NNN#N` trailer. | No | |
| 6 | Set repository description and topics | Use the git host API with the token read from `.env` (never printed, never imported by the project) to set a description and topics such as python, selenium, cookie-clicker, automation, udemy, 100-days-of-code. | No | |

---

[BC-001]: ../business-case.md
[96a9a78]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/commit/96a9a78f010ce8ae3fce8d84602317d8b5808a13
