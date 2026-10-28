# Purchase strategy improvement

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-006 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version (reviewed in RC-014) | [638730d] |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Task 1 changed after the first measurement run: one product per store visit instead of waiting for a price change (reviewed in RC-016) | [375cc0b] |

---

## Purpose

Decide whether the bot reaches a higher cookies-per-second (CPS) rate than the 16.6 of the first release by buying more reliably and more often. In the Docker run of MIL-004 about 40 percent of the purchase attempts failed: each failure came right after a successful purchase in the same store visit, because the game had not yet redrawn the store flags.

## Deliverable

The functions `buy_upgrade`, `get_store_items` and `run_bot` changed so that the bot buys at most one product per store visit and therefore always reads the store after the game has redrawn it, visits the store every second and also buys affordable upgrades; a Docker run of 300 seconds with its CPS, log and refreshed screenshot of step 5; the README and the wiki pages in English, Danish and Bahasa Malaysia updated with the new result and what it taught.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | In a 300 second Docker run, fewer than 5 percent of the purchase attempts log "did not raise the owned amount" | Met | Not met |
| 2 | The CPS of that run is higher than the 16.6 of the first release | Met | Not met |
| 3 | `python -m pytest`, `ruff check` and `mypy --strict` pass; `selenium` is still the only runtime dependency | Met | Not met |
| 4 | The source review record says Go | Met | Not met |
| 5 | The README and all three wiki languages show the same new CPS and screenshot | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-005 | Needs the finished bot, the Docker run and the wiki it updates |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O3, O4 in [BC-001] | Success criterion 2 (CPS reported) and the learning record of the wiki |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-03 - within the one-week limit of [BC-001]

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Wait for the store redraw after a purchase | After a successful purchase the store flags and prices are stale until the game redraws, so the next choice clicks a product that is no longer affordable. The game updates the price and owned text at once but the affordable flag only at its next redraw, so the price text is not a redraw signal (found in the first measurement run). Buy at most one product per store visit, so the next read comes a second later, after the redraw; the log of MIL-004 shows the failures follow a purchase. | No | |
| 2 | Visit the store every second | The store is visited every 5 seconds and the loop stops buying at the first failure, so cookies wait idle. Shorten `STORE_CHECK_INTERVAL_SECONDS` and keep buying while something is affordable; measure that clicks per second do not drop. | No | |
| 3 | Buy affordable upgrades | Upgrades such as the cursor and grandma boosts raise the CPS cheaply. Read the enabled upgrade crates in the `upgrades` area and click the cheapest first, behind the existing port with a fake in the tests. | No | |
| 4 | Measure the new strategy in Docker | Run the 300 second headless Docker run again, compare the CPS and the failure rate with the first release (16.6, about 40 percent) and refresh the screenshot of step 5. Environment: Docker container. | No | |
| 5 | Update the README and the wiki | Put the new CPS, the screenshot and what the improvement taught into the README and the English, Danish and Bahasa Malaysia wiki pages of step 4 and step 5. | No | |

---

[BC-001]: ../business-case.md
[638730d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/commit/638730d95ba24ba77c6448730d7999aa3e90d863
[375cc0b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/commit/375cc0b5f3919b00daeb2f8f5fcc81de25acfc4c
