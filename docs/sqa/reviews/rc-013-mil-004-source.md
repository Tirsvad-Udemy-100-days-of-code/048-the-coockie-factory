# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-013 |
| CrossReference | [MIL-004], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: source of milestone MIL-004 (capture_steps, Chrome environment support, retry, owned-amount purchase check) and docker/Dockerfile ([MIL-004])
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | PEP 8 casing throughout. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (StepUnreachableError, build_chrome_options, OWNED_CHECK_ATTEMPTS). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` clean, no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All signatures annotated; mypy --strict passes on 35 files. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | StepUnreachableError is raised and not swallowed; stale-element retries re-raise the last error after the limit. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults, no shadowed builtins. |
| 7 | Files, locks and connections are managed with context managers | Pass | The browser is released in a finally block in cli.main and capture_steps.main. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Doxygen docstrings on all public items. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | Progress goes through logging; print is used only for the program result; no secrets in output. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | Plain technical tasks; no Design Class Diagram exists or is required. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 99 offline tests (fake game, fake clock, fake driver); the live behaviour was checked in Docker: two full 300 second runs reported 15.7 and 16.6 cookies per second, the last one is in the README. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | mypy --strict clean; no Any. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | selenium remains the only runtime dependency; the Docker image installs only chromium for the browser. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Environment variable names, step file names and limits live in constants.py. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | selenium is imported only in infrastructure; presentation modules are composition roots. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Ports stay narrow; capture_steps uses SeleniumGame directly because screenshots are documentation tooling (decision recorded in the hand-over). |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Layers under src/, unit, integration and e2e under tests/. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All names English, no spaces; Dockerfile is a fixed tool name. |

## Overall Verdict

Go - All Mandatory criteria pass or are not applicable. GUI runs were done headless in a Docker container; no GUI was started on the host desktop. The Docker run showed that about 40 percent of the purchase attempts fail because the store flags are read just before the game redraws; the bot logs and retries at the next store check (noted for the wiki). Stand-in review, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[MIL-004]: ../../milestones/mil-004-screenshots-and-readme.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
