# Bot core: open the game and click the cookie

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version (reviewed in RC-005) | [96a9a78] |

---

## Purpose

Decide whether the bot can start the game, choose the language, click the big cookie and read the cookie count (lecture steps 1 to 3) with the logic tested without a browser.

## Deliverable

A `GamePort` interface, a Selenium adapter and the functions `open_game`, `select_language`, `click_cookie` and `get_cookie_count`, with Doxygen comments and pytest tests that use a fake game.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pytest` passes with tests for the click and count logic using a fake game | Met | Not met |
| 2 | All element ids, the URL and timings are defined in `constants.py` and nowhere else | Met | Not met |
| 3 | Every public function has a Doxygen comment | Met | Not met |
| 4 | Source follows `qc-programming-python` and the review record says Go | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Needs the skeleton, configuration and plan gate |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
O1, O2, O3 in [BC-001]

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-30 - within the one-week limit of [BC-001]

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Define the game port and constants | Create `constants.py` (URL, language selector, big cookie id, cookie counter id) and a `GamePort` protocol so the rules do not import Selenium. | No | |
| 2 | Implement open_game and select_language | Open https://ozh.github.io/cookieclicker/ with Selenium, wait for the language chooser and pick English, so every later step starts from a playable game. | No | |
| 3 | Implement click_cookie | Click the big cookie a given number of times through the port; this is lecture step 2 and the base of the cookies-per-second (CPS) race. | No | |
| 4 | Implement get_cookie_count | Read and parse the cookie counter text into an integer, handling thousands separators and the word forms the game prints. | No | |
| 5 | Unit tests with a fake game | Test the functions above with a `FakeGame` in `tests/`, so they run in the venv without any browser. | No | |

---

[BC-001]: ../business-case.md
[96a9a78]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/commit/96a9a78f010ce8ae3fce8d84602317d8b5808a13
