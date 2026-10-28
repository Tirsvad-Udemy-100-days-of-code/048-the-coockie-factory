# Screenshots per lecture step and README

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version (reviewed in RC-007) | pending |

---

## Purpose

Decide whether the real bot works against the live game and whether the repository explains it: one screenshot per lecture step and a README from the framework template.

## Deliverable

A Docker setup with headless Chrome, a capture run that writes one PNG per lecture step to `docs/images/`, and `README.md` built from the framework template with the screenshots, the `.venv` setup, `python -m pip install --upgrade pip`, and the run and test instructions.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The Docker run exits 0 and `docs/images/` holds one screenshot for each of the five lecture steps | Met | Not met |
| 2 | The headless run prints a cookies-per-second (CPS) value after 300 seconds | Met | Not met |
| 3 | `bash framework/scripts/check-readme.sh` passes on `README.md` | Met | Not met |
| 4 | The README explains creating and using a local `.venv` and running the tests | Met | Not met |
| 5 | No graphical user interface (GUI) was started on the host desktop | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | Needs the complete bot |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
O1, O4, O5 in [BC-001]

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-02 - within the one-week limit of [BC-001]

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Dockerfile with headless Chrome | Build a Linux image with Chrome, chromedriver and the project installed; the run is headless so it does not take the host's mouse or keyboard. Environment: Docker container. | No | |
| 2 | Capture one screenshot per lecture step | A small capture module saves a PNG after each lecture step (open, click, count, buy, final CPS) into a folder shared with the host. Environment: Docker container. | No | |
| 3 | Run the full five-minute bot in Docker | Run the real bot against the live game, keep the log, and record the CPS reached. Environment: Docker container. | No | |
| 4 | Write README from the framework template | Fill the template: overview, requirements, venv setup with `python -m pip install --upgrade pip`, run, tests, license, links, appendix, and embed the screenshots. | No | |
| 5 | Run README and plan checks | Run `check-readme.sh` and `check-plan.sh` and fix findings before the pull request. | No | |

---

[BC-001]: ../business-case.md
