# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version (reviewed in RC-002) | pending |

---

## Purpose

This analysis names the people who care about the Cookie Clicker bot, classifies them by power and interest (Mendelow grid) and maps concerns to FURPS+ (Functionality, Usability, Reliability, Performance, Supportability, plus constraints) and maps concerns to FURPS+ (Functionality, Usability, Reliability, Performance, Supportability, plus constraints) and maps concerns to FURPS+ (Functionality, Usability, Reliability, Performance, Supportability, plus constraints) and records their concerns, so owners and reviewers elsewhere cite stable stakeholder IDs.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | Tirsvad | High | High | Manage Closely | A correct bot that shows what was learned and passes review |
| S02 | Udemy coursists | Fellow participants of the bootcamp | Udemy community | Low | High | Keep Informed | Readable, runnable code with the assignment's function names, plus README instructions to run it |
| S03 | GitHub viewers | Visitors browsing the repository for ideas | GitHub community | Low | Medium | Keep Informed | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely:** S01 decides scope, writes and reviews everything.
- **Keep Informed:** S02 and S03 cannot change the project but consume its output; the README, the wiki and the repository metadata serve them.
- **Keep Satisfied and Monitor:** no stakeholder.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The bot reaches a high CPS in five minutes | Performance |
| CN-002 | S01 | Every artifact is reviewed before code | Supportability |
| CN-003 | S02 | Code is readable and uses the assignment's function names | Usability |
| CN-004 | S02 | README explains how to run the project and its tests | Usability |
| CN-005 | S03 | Description, topics and README make the repository understandable | Usability |
| CN-006 | S03 | No runtime dependencies beyond what is needed | Implementation constraint |
| CN-007 | S01 | Wiki in English, Danish and Bahasa Malaysia explains what each lecture step taught | Supportability |

## Communication Requirements

| Channel | Frequency | Deliverable | Phase |
| --- | --- | --- | --- |
| Chat with S01 | At plan acceptance and at the final summary | Plan, run summary | All |
| Pull request per milestone | Once per milestone | Reviewed change set | Every milestone |
| README and wiki | Once per release | Instructions and lecture write-ups | Documentation milestones |

## Conflicting Interests and Mitigations

| Conflict | Mitigation |
| --- | --- |
| S03 wants no runtime dependencies, but the assignment requires Selenium (CN-006 against CN-001) | Selenium is the single runtime dependency (architecture decision record ADR-0001); tests, docs and tooling use none; the README says why |

## Traceability Analysis

| Stakeholder | Business Case objective |
| --- | --- |
| S01 | O1, O2, O3 in [BC-001] |
| S02 | O2, O3, O4 in [BC-001] |
| S03 | O4, O5 in [BC-001] |

## Sign-Off

| Stakeholder | Decision | Date |
| --- | --- | --- |
| S01 | Pending review | |

---

[BC-001]: ./business-case.md
