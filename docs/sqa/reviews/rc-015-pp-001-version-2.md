# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-015 |
| CrossReference | [PP-001], [QC-PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: PP-001 version 2 (adds MIL-006) ([PP-001])
- Checklist used: [QC-PP-001]
- Scope: full review
- Language and domain: en / it (the artifact's Metadata rows)
- Language reviewer: S01 (confirmed criteria 3, 5 and 9 of QC-LANG-001 in chat on 2026-10-28)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Unchanged from RC-003 and rechecked with MIL-006 included. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | Unchanged from RC-003 and rechecked with MIL-006 included. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | Decision dates equal the Target Date of MIL-001 to MIL-006 and lie inside the window. |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage has a row for the purchase strategy improvement, mapped to MIL-006 and objective O1. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Chain MIL-001 to MIL-006 is acyclic; MIL-006 follows MIL-005. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | Unchanged from RC-003 and rechecked with MIL-006 included. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | N-A | No governance document is in scope of the Business Case; the only owner ID is S01, as in the MIL Ownership tables. |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Unchanged from RC-003 and rechecked with MIL-006 included. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Plan Risks list a new risk (CPS does not rise) with a mitigation; two risks trace to Business Case risks. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open Issues do not contradict the new row. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | The main deliverable of MIL-006 in the plan matches its Deliverable section. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | Unchanged from RC-003 and rechecked with MIL-006 included. |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | Gantt bars, table and the chain agree. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | Milestone column blank until the sync. |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | Unchanged from RC-003 and rechecked with MIL-006 included. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata has Language en and Domain it. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | en is a BCP 47 code and it is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | Confirmed by S01 in chat on 2026-10-28 (named human reviewer). Content is English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register: IT Executive English. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | Confirmed by S01 in chat on 2026-10-28 (named human reviewer). Ordinary IT terms; no dictionary exists or is needed. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Headings, keys, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | No change of language or domain. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | Confirmed by S01 in chat on 2026-10-28 (named human reviewer). S01 is competent in English and in IT. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations are spelled out at first use. |

## Overall Verdict

Go - Full re-review of version 2; all Mandatory criteria pass or are not applicable; the language criteria were confirmed by S01. Stand-in review, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
