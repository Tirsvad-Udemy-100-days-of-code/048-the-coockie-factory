# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Proposed | Jens Tirsvad Nielsen | <reviewer S-ID> | Initial version | pending |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001] | [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] | [RC-003] |
| [MIL-001] | MIL | en | it | [PP-001] | [MIL-002] | [RC-004] |
| [MIL-002] | MIL | en | it | [MIL-001] | [MIL-003] | [RC-005] |
| [MIL-003] | MIL | en | it | [MIL-002] | [MIL-004] | [RC-006] |
| [MIL-004] | MIL | en | it | [MIL-003] | [MIL-005] | [RC-007] |
| [MIL-005] | MIL | en | it | [MIL-004] | - | [RC-008] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-003] | - | - | Gap |
| CN-002 | [BC-001] | - | - | Covered |
| CN-003 | [MIL-002] | - | - | Covered |
| CN-004 | [MIL-004] | - | - | Covered |
| CN-005 | [MIL-001] | - | - | Covered |
| CN-006 | [MIL-001] | - | - | Covered |
| CN-007 | [MIL-005] | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | None found | - | Closed | - |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-project-setup.md
[MIL-002]: ../milestones/mil-002-bot-core-open-and-click.md
[MIL-003]: ../milestones/mil-003-upgrades-and-five-minute-run.md
[MIL-004]: ../milestones/mil-004-screenshots-and-readme.md
[MIL-005]: ../milestones/mil-005-wiki-and-release.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-mil-001-project-setup.md
[RC-005]: ./reviews/rc-005-mil-002-bot-core-open-and-click.md
[RC-006]: ./reviews/rc-006-mil-003-upgrades-and-five-minute-run.md
[RC-007]: ./reviews/rc-007-mil-004-screenshots-and-readme.md
[RC-008]: ./reviews/rc-008-mil-005-wiki-and-release.md
