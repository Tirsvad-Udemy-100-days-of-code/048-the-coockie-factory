# Wiki in three languages and release

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version (reviewed in RC-008) | [96a9a78] |

---

## Purpose

Decide whether the project is ready to share: the wiki explains what each lecture step taught in English, Danish and Bahasa Malaysia, and everything is consistent.

## Deliverable

Wiki pages under `docs/wiki/` in English (no suffix), Danish (`-da`) and Bahasa Malaysia (`-ms`) with the same page set, the screenshots per lecture step, a `_Sidebar.md`, and the publish workflow template.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Every English wiki page has a `-da` and an `-ms` twin with the same page set | Met | Not met |
| 2 | Each lecture step page embeds its screenshot and has a section on what was gained | Met | Not met |
| 3 | `bash framework/scripts/check-languages.sh` passes | Met | Not met |
| 4 | Doxygen runs clean and `python -m pytest` still passes | Met | Not met |
| 5 | A final summary of milestones, reviews and stand-in decisions is written for S01 | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-004 | Needs the screenshots and README |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
O4, O5 in [BC-001]

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-04 - within the one-week limit of [BC-001]

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the English wiki | Pages Home, Description, Install, one page per lecture step with its screenshot and what was gained, Appendix-Documentation and `_Sidebar.md`, following the framework wiki checklist. | No | |
| 2 | Translate the wiki to Danish | Same page set as English with suffix `-da`; code, commands and IDs stay in English; language line at the top of each page. | No | |
| 3 | Translate the wiki to Bahasa Malaysia | Same page set as English with suffix `-ms`; code, commands and IDs stay in English; language line at the top of each page. | No | |
| 4 | Add the wiki publish workflow | Copy the framework's publish-wiki template into the project's CI folder so the wiki reaches the git host on merge. | No | |
| 5 | Final verification and summary | Run tests, Doxygen and the framework checks, confirm the repository description and topics, and prepare the run summary for S01. | No | |

---

[BC-001]: ../business-case.md
[96a9a78]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/commit/96a9a78f010ce8ae3fce8d84602317d8b5808a13
