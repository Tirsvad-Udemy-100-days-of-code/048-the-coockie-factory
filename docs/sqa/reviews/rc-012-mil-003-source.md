# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [MIL-003], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: source of milestone MIL-003 (store, choose_upgrade, buy_upgrade, get_cps, run_bot, main) ([MIL-003])
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | PEP 8 casing throughout. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (choose_upgrade, STORE_CHECK_INTERVAL_SECONDS). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` clean, `ruff format` applied, no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All signatures annotated; mypy --strict passes on 33 files. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | Specific exceptions (ValueError, UnreadableNumberError); a failed purchase is logged and stops the buying loop instead of being swallowed. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults, no shadowed builtins. |
| 7 | Files, locks and connections are managed with context managers | Pass | The browser is released in a finally block in cli.main (tested when run_bot raises). |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Doxygen docstrings on all public items. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | Progress goes through logging; the only print is the program result `Result : <cps>` in the command line entry point; no secrets are logged. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | Plain technical tasks; no Design Class Diagram exists or is required. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 74 offline tests with a fake game and a fake clock; no sleeps, no network, no browser; positive, negative, boundary, edge, error handling and timing cases. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | mypy --strict clean; no Any. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | selenium remains the only runtime dependency. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Ids, class names, burst size and intervals live in constants.py; decimal parsing is shared by parse_game_number. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | domain imports only constants and errors; application imports domain and ports; selenium only in infrastructure; the CLI is the composition root. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Clock and GamePort are narrow Protocols; run_bot receives both (dependency inversion); one purpose per module. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Layers under src/ and unit and integration tests under tests/. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All names English, snake_case, no spaces. |

## Overall Verdict

Go - All Mandatory criteria pass or are not applicable; behaviour against the live game is verified in MIL-004. Stand-in review, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[MIL-003]: ../../milestones/mil-003-upgrades-and-five-minute-run.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
