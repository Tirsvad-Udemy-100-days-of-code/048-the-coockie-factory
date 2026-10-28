# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-003 |
| CrossReference | [PP-001], [QC-PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [96a9a78] |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / it (the artifact's Metadata rows)
- Language reviewer: S01 (confirmed criteria 3, 5 and 9 of QC-LANG-001 in chat on 2026-10-28)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; the language criteria were confirmed by S01 in person)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Planning Assumptions state start 2026-10-28 and end 2026-11-04 per the one-week Business Case constraint. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | Five gateway rows, each linking its MIL document, decision date and owner S01. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | Decision dates 2026-10-29, 10-30, 10-31, 11-02, 11-04 equal the Target Date of MIL-001 to MIL-005 and lie inside the window. |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage table maps every In Scope item to a gateway. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Chain MIL-001 to MIL-005 is acyclic and matches the schedule order. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | Dependencies section says a No-Go returns the phase to its owner, later gateways move, and S01 alone decides an end-date move. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | N-A | No governance document is in scope of [BC-001]; all owners use the SA ID S01, matching the MIL Ownership tables. |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Planning Assumptions list start, length, reviewer stand-in and cadence with sources. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Plan Risks have impact and mitigation; two trace to Business Case risks. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open Issues name the repository-name difference and the earlier solution; neither contradicts the plan. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | Main deliverable column matches each MIL Deliverable. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | Stories column says 'none (technical tasks)'. |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | Gantt bars and the table use the same dates; the chain matches the dependency list. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | Milestone column is blank because no sync has happened yet. |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | Single plan file docs/project-plan.md with one Version History row. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata has Language en and Domain it. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | en is a BCP 47 code and it is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | Confirmed by S01 in chat on 2026-10-28 (named human reviewer); content is English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register: IT Executive English. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | Confirmed by S01 in chat on 2026-10-28: terms are ordinary IT terms and no dictionary exists or is needed. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Headings, keys, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | First version; no earlier accepted version. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | S01, competent in English and in IT, confirmed the domain terms in chat on 2026-10-28. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations (CPS, GUI, FURPS+, ADR) are spelled out at first use. |

## Overall Verdict

Go - no Mandatory criterion failed and none is Pending; the language criteria 3, 5 and 9 were confirmed by S01. Stand-in review, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[96a9a78]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-the-coockie-factory/commit/96a9a78f010ce8ae3fce8d84602317d8b5808a13
