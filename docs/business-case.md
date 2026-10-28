# Cookie Clicker Bot

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version (reviewed in RC-001) | pending |

---

## Executive Summary

Udemy's *100 Days of Code* final project of day 48 asks the participant to build a Python bot that plays the browser game Cookie Clicker with Selenium: it clicks the big cookie and buys upgrades by itself, and after five minutes reports the cookies-per-second (CPS) rate it reached. This project delivers that bot as a readable, runnable and tested repository that other course participants (S02) can compare against and GitHub visitors (S03) can browse, with a README and a three-language wiki (English, Danish, Bahasa Malaysia) that show every lecture step with a screenshot and explain what it taught.

## Methodological and Standards Foundation

The artifacts follow the SQA and QC framework mounted at `framework/` (plan first, review every artifact against its QC checklist). Quality attributes are named with ISO/IEC 25010:2023 characteristics. The code follows the framework's Python conventions and Clean Architecture (business rules free of Selenium), is tested with pytest and documented with Doxygen comments. Graphical user interface (GUI) runs are done headless in a Docker container, never on the host desktop (`framework/process/gui-testing.md`).

## Problem Statement

- The assignment is described in a lecture video only; there is no runnable reference a participant can compare with.
- A bot written as one script of module-level code with threads (the author's earlier solution targeted the old Orteil experiment page and needed an extra threading package) is hard to read, cannot be tested without a browser and does not work against the current Cookie Clicker at ozh.github.io.
- Without screenshots and an explanation per lecture step, a visitor sees code but not what each step achieves or what was learned.

## Business Opportunity

A small, well-structured reference solution makes the author's learning visible, lets other participants compare strategies (the lecture invites competition on CPS), and gives GitHub visitors a clean example of a Selenium automation project with tests, documentation and a multilingual wiki.

## Objectives

1. O1: A bot plays Cookie Clicker at https://ozh.github.io/cookieclicker/ for five minutes by clicking the big cookie and buying upgrades, then prints the CPS reached.
2. O2: The code uses the assignment's function names, constants live in `constants.py`, and every source file has Doxygen comments with a `Doxyfile` provided.
3. O3: Decision logic is covered by pytest tests that need no browser; the only runtime dependency is Selenium.
4. O4: A README and a wiki in English, Danish and Bahasa Malaysia show one screenshot per lecture step and explain what each step taught.
5. O5: The repository has a description and topics on the git host, a Python `.gitignore`, a `pyproject.toml` (Python 3.13 or newer) and instructions for creating and using a local `.venv`.

## Scope

### In Scope

- The bot for the lecture steps: open the game, choose the language, click the cookie, read the cookie count, buy affordable upgrades, run for five minutes, report CPS.
- Project configuration: `pyproject.toml`, `.gitignore`, `.venv` instructions, `Doxyfile`, `constants.py`.
- pytest tests for the logic with a fake game.
- A headless Docker run that produces one screenshot per lecture step.
- README (framework template) and wiki pages in en, da and ms.
- Description and topics on the git host repository.

### Out of Scope

- Cheating features of the game (console commands, save editing).
- Browsers other than Chrome, and the old Orteil experiment page.
- A graphical front end or packaging to PyPI.
- Contests or a leaderboard.

## Expected Benefits

### Tangible Benefits

- A runnable bot, a test suite and generated API documentation.
- Screenshots per lecture step, in the README and in three wiki languages.

### Intangible Benefits

- A learning record of Selenium, game-loop strategy and clean structure.
- A portfolio piece for GitHub visitors.

## Strategic Alignment

The project supports the author's goal of completing the 100 Days of Code bootcamp with work that is reviewable and shareable, and exercises the SQA and QC framework on a small project.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Bot run length | 300 seconds | Run log shows start and end times |
| 2 | CPS reported | A CPS value is printed at the end of the run | Console output of the headless run |
| 3 | Tests | All pytest tests pass, no browser needed | `python -m pytest` exit code 0 |
| 4 | Runtime dependencies | Exactly one: `selenium` | `dependencies` list in `pyproject.toml` |
| 5 | Lecture step screenshots | One per lecture step, in README and each wiki language | Files under `docs/images/` referenced by all pages |
| 6 | Wiki languages | Same page set in en, da and ms | `check-languages.sh` and the file listing |
| 7 | Repository metadata | Description and at least five topics set | Git host API response |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The game's page structure changes | Bot stops finding elements | Element ids live in `constants.py`; explicit waits with timeouts; note the game version tested |
| The game is unreachable from the container | No run, no screenshots | Stop and report; unit tests stay independent of the network |
| Docker or headless Chrome is unavailable | GUI run cannot be done | Stop and report per the GUI testing rule; never fall back to the host desktop |
| Selenium is a heavy dependency against S03's wish for none | Conflict between stakeholder concerns | Keep it the single runtime dependency, justified in the architecture decision record ADR-0001 |
| A token leaks into the repository | Secret exposure | `.env` stays untracked and ignored; tokens are read by scripts only and never printed |

## Assumptions

- S01 is Product Owner and reviewer; S02 and S03 cannot be interviewed, so their needs are taken from the assignment brief.
- The PO language is English and the domain is IT.
- The game at https://ozh.github.io/cookieclicker/ stays available during the project.
- Docker with a Chrome image is available on the author's machine.
- The stage is a prototype-sized learning project with no budget.

## Constraints

- Python 3.13 or newer, `venv`, pytest, `pyproject.toml`, constants in `constants.py`.
- Folder structure `src/`, `tests/`, `docs/`.
- Doxygen comments and a `Doxyfile`.
- Avoid runtime dependencies unless needed.
- Tokens come from `.env`, which is for personal use only: it is not imported by the project, not tested and not committed.
- Duration: one week, 2026-10-28 to 2026-11-04. Budget: none.
- One branch and one pull request per milestone.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About 20 hours of the author's and the AI's time, no money (qualitative assessment, justified: a learning project with no revenue and no budget) | A reviewed reference solution, a learning record and a shareable repository |

## Stakeholders

| ID | Role in this project | Reference |
| --- | --- | --- |
| S01 | Course participant, Product Owner, developer and reviewer | [SA-001] |
| S02 | Udemy coursists who compare solutions | [SA-001] |
| S03 | GitHub viewers browsing for ideas | [SA-001] |

## Recommendation

Proceed.

---

[SA-001]: ./stakeholder-analysis.md
