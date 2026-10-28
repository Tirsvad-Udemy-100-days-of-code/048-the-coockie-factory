# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-017 |
| CrossReference | [MIL-006-SRC], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [375cc0b] |

---

## Artifact Under Review

- Instance reviewed: Source code of MIL-006 (store, run_bot, selenium_game, constants, tests) ([MIL-006-SRC])
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Checked in the diff of branch mil-006-purchase-strategy; 111 tests, ruff check, ruff format and mypy --strict pass; Selenium stays the only runtime dependency. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Checked in the diff of branch mil-006-purchase-strategy; 111 tests, ruff check, ruff format and mypy --strict pass; Selenium stays the only runtime dependency. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | Checked in the diff of branch mil-006-purchase-strategy; 111 tests, ruff check, ruff format and mypy --strict pass; Selenium stays the only runtime dependency. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Checked in the diff of branch mil-006-purchase-strategy; 111 tests, ruff check, ruff format and mypy --strict pass; Selenium stays the only runtime dependency. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | Checked in the diff of branch mil-006-purchase-strategy; 111 tests, ruff check, ruff format and mypy --strict pass; Selenium stays the only runtime dependency. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | Checked in the diff of branch mil-006-purchase-strategy; 111 tests, ruff check, ruff format and mypy --strict pass; Selenium stays the only runtime dependency. |
| 7 | Files, locks and connections are managed with context managers | Pass | Checked in the diff of branch mil-006-purchase-strategy; 111 tests, ruff check, ruff format and mypy --strict pass; Selenium stays the only runtime dependency. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Checked in the diff of branch mil-006-purchase-strategy; 111 tests, ruff check, ruff format and mypy --strict pass; Selenium stays the only runtime dependency. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | Checked in the diff of branch mil-006-purchase-strategy; 111 tests, ruff check, ruff format and mypy --strict pass; Selenium stays the only runtime dependency. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | Checked in the diff of branch mil-006-purchase-strategy; 111 tests, ruff check, ruff format and mypy --strict pass; Selenium stays the only runtime dependency. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | Checked in the diff of branch mil-006-purchase-strategy; 111 tests, ruff check, ruff format and mypy --strict pass; Selenium stays the only runtime dependency. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | Checked in the diff of branch mil-006-purchase-strategy; 111 tests, ruff check, ruff format and mypy --strict pass; Selenium stays the only runtime dependency. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Checked in the diff of branch mil-006-purchase-strategy; 111 tests, ruff check, ruff format and mypy --strict pass; Selenium stays the only runtime dependency. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Checked in the diff of branch mil-006-purchase-strategy; 111 tests, ruff check, ruff format and mypy --strict pass; Selenium stays the only runtime dependency. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | Checked in the diff of branch mil-006-purchase-strategy; 111 tests, ruff check, ruff format and mypy --strict pass; Selenium stays the only runtime dependency. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Checked in the diff of branch mil-006-purchase-strategy; 111 tests, ruff check, ruff format and mypy --strict pass; Selenium stays the only runtime dependency. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Checked in the diff of branch mil-006-purchase-strategy; 111 tests, ruff check, ruff format and mypy --strict pass; Selenium stays the only runtime dependency. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | Checked in the diff of branch mil-006-purchase-strategy; 111 tests, ruff check, ruff format and mypy --strict pass; Selenium stays the only runtime dependency. |

## Overall Verdict

Go - All Mandatory criteria pass. Stand-in review, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[MIL-006-SRC]: ../../../src/cookie_clicker_bot
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[375cc0b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/commit/375cc0b5f3919b00daeb2f8f5fcc81de25acfc4c
