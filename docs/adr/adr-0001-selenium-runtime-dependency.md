# Selenium as the single runtime dependency

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version (reviewed in RC-009) | [ad3334f] |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The assignment is to automate the Cookie Clicker game in a real browser with Selenium ([BC-001], objective O1). GitHub viewers (S03) asked for no runtime dependencies (concern CN-006 in [SA-001]), and the Business Case constraint says to avoid runtime dependencies unless needed. The bot must read the page and click elements, so something has to drive a browser.

Options evaluated:

1. **Selenium** as the one runtime dependency. It is what the assignment and the course use, and Selenium Manager downloads a matching driver.
2. **No dependency**, driving Chrome through the DevTools protocol with the standard library only. This needs a hand-written WebSocket client and protocol code, which is long, fragile and unreadable for S02.
3. **Playwright**. A comparable dependency, but not the library of the assignment, so S02 could not compare solutions.
4. **Selenium plus a threading helper** (the author's earlier solution used `continuous_threading`). A second dependency for something the standard library `threading` or a single loop already does.

## Decision

Selenium is the only runtime dependency; pytest, ruff and mypy are development dependencies, and everything else uses the standard library.

## Consequences

**Positive:**

- The code matches the assignment, so S02 can compare solutions directly.
- Only one package is installed to run the bot (`pip install .`).
- The decision logic is behind a port, so tests need neither Selenium nor a browser.

**Negative:**

- S03's wish for no dependencies is met only in part; the README states why Selenium is needed.
- Running the bot needs Chrome installed (Selenium Manager fetches the driver); the Docker image covers this for the screenshots.
- Performance Efficiency: Selenium calls cost milliseconds each, which limits the clicks per second.

## Affected Artifacts

- [BC-001] — fixes the runtime dependency list for success criterion 4.
- [SA-001] — records the mitigation of the conflict between CN-006 and the assignment.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[ad3334f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/commit/ad3334fa13c4261c3d034fbffcc7b43fe95fbb31
