# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [MIL-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [68c4391] |

---

## Artifact Under Review

- Instance reviewed: source of milestone MIL-002 (open_game, select_language, click_cookie, get_cookie_count, parser, Selenium adapter) ([MIL-002])
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | snake_case modules and functions, PascalCase classes, UPPER_SNAKE constants. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose: parse_game_number, wait_for_element, ELEMENT_TIMEOUT_SECONDS. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` clean; no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All signatures annotated, including -> None; mypy strict passes. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare except; ValueError and UnreadableNumberError are raised with a message. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; no builtin shadowed. |
| 7 | Files, locks and connections are managed with context managers | N-A | The browser is released by SeleniumGame.close(); the composition root in MIL-003 calls it in a finally block. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Public modules, classes and functions have Doxygen docstrings (@brief, @param, @return). |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | N-A | No logging yet; added with the run loop in MIL-003. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | Plain technical tasks; no Design Class Diagram exists or is required. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 33 tests (unit and integration) run offline with a fake game and a fake driver; positive, negative, boundary and edge cases covered. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | mypy --strict: no issues in 22 files; no Any. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | selenium is declared and is the only runtime dependency. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | URL, ids and number words are defined once in constants.py. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | domain imports only constants; application imports domain and its own port; only infrastructure/selenium_game.py imports selenium; no cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | GamePort is a narrow Protocol (4 methods); SeleniumGame receives its driver (dependency inversion); each module has one purpose. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | domain, application (ports, use_cases), infrastructure and presentation under src/; unit, integration and e2e under tests/. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All names English, snake_case, no spaces. |

## Overall Verdict

Go - All Mandatory criteria pass or are not applicable; the live-game behaviour is verified in MIL-004. Stand-in review, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[MIL-002]: ../../milestones/mil-002-bot-core-open-and-click.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[68c4391]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/commit/68c439137f13299e20cf6271e392365d9f5371c4
