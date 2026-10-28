# Upgrades and the five-minute run

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version (reviewed in RC-006) | [96a9a78] |

---

## Purpose

Decide whether the bot buys upgrades by strategy, runs for five minutes and reports its cookies-per-second (CPS) rate (lecture steps 4 and 5).

## Deliverable

The functions `get_store_items`, `choose_upgrade`, `buy_upgrade`, `get_cps` and `run_bot`, a command line entry point `main`, and tests for the strategy.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pytest` passes with tests for the purchase strategy (most expensive affordable upgrade first) | Met | Not met |
| 2 | `run_bot` stops after the duration in `constants.py` (300 seconds) and returns the CPS | Met | Not met |
| 3 | The bot uses one loop and adds no runtime dependency beyond `selenium` | Met | Not met |
| 4 | The code is reviewed against `qc-programming-python` and the review record says Go; the run against the live game is the job of MIL-004 | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | Uses the port, constants and click functions |

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

2026-10-31 - within the one-week limit of [BC-001]

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement get_store_items | Read each product in the store with its name, price and whether it can be bought, through the port. | No | |
| 2 | Implement choose_upgrade | Pure function: given the cookie count and store items, pick the most expensive upgrade that is affordable, or none. | No | |
| 3 | Implement buy_upgrade | Click the chosen product and confirm the count dropped, so a failed click is noticed. | No | |
| 4 | Implement get_cps and run_bot | Run a single loop for 300 seconds that clicks, buys on an interval and finally reads the CPS; the result is returned and printed. | No | |
| 5 | Add the main entry point | `python -m cookie_clicker_bot` starts Chrome, runs the bot and prints `Result : <cps>`; the browser is closed in a finally block. | No | |
| 6 | Unit tests for strategy and run loop | Test `choose_upgrade` with edge cases and `run_bot` with a fake game and a fake clock. | No | |

---

[BC-001]: ../business-case.md
[96a9a78]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/commit/96a9a78f010ce8ae3fce8d84602317d8b5808a13
