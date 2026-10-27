# Permission matrix — Phase 1 working draft

Status: mixed confirmed decisions and open proposals, labeled below. This document specifies business requirements, not implemented permissions. Source decisions are in ../decisions/DECISIONS.md. Broader administration and ordinary role grants must be validated in the backend as well as the UI. A grant does not bypass record entity/function integrity or workflow-step eligibility.

## Confirmed permissions

| Role / participation | Confirmed capability | Scope / boundary | Decision |
|---|---|---|---|
| Asset Operator | Register and move assets | Explicit organization/function pair; this role alone does not grant direct disposal | D015 |
| Asset Manager | Register/move, run stock verification and reconciliation, perform direct disposal | Authorized organization/function | D015 |
| Business Owner | Accountable asset ownership; monitor relevant request progress and asset details even for requests initiated by others | Owned assets and relevant details in authorized scope; exclude unrelated records | D011/D014/D016 |
| Global User | Maintain its entity across functions; manage ordinary business-role assignments | Assigned entity only; cannot grant/revoke Global User or Super User | D013/D017 |
| Super User | Application-wide maintenance; grant/revoke Global User and Super User | All entities/functions; actual company maker/deployment access is configured separately | D013/D017 |
| Respondent participation | Edit assigned open responses; read historically assigned processes | Request-specific; closed responses are read-only without audited reopening; additional history detail/offboarding rules pending | D010/D012 |
| Authorized final approver | May approve a request they initiated | Must otherwise be explicitly authorized for the workflow step; no blanket self-approval ban | D009 |

## Confirmed read, export and reminder permissions

| Role / participation | Read / business capability | Export permission | Reminder permission |
|---|---|---|---|
| Viewer | Authorized records/reports; business-data read-only | Assigned data in authorized scope | Not granted by this role |
| Asset Operator | Register/move assets | Authorized asset-module data | Not granted by this role |
| Inventory Operator | Register/transfer quantity inventory and view history | Authorized inventory-module data | Not granted by this role |
| Asset Manager | Asset operations, stock verification, reconciliation and direct disposal | Authorized operational data | Standard reminders to relevant pending respondents |
| Business Owner | Relevant owned-asset reporting including others' requests | Relevant owned-asset reports | Standard reminders to relevant pending respondents |
| Global User | Maintenance within assigned entity | Entity-wide authorized data | Broader maintenance scope confirmed; detailed operational matrix remains to be completed |
| Super User | Application-wide maintenance | Across entities | Broader maintenance scope confirmed; detailed operational matrix remains to be completed |
| Respondent participation | Assigned open responses; read-only historical assigned work | Assigned data within current/historical read visibility | Not granted through respondent participation alone |

Source: D018–D020 and earlier role decisions. Exported rows/fields never exceed authorized read visibility. Exact formats, field lists, assignment semantics for Viewer and historical detail rules remain to be specified. Not-granted entries mean this role/participation alone supplies no such permission; another explicit role may supply it.

## Round 6 proposals — require owner response

| ID | Proposal | Boundaries |
|---|---|---|
| P6-01 | Asset Manager, Global User and Super User may reopen closed work within their authority; Business Owner may request reopening | Reason and audit required; old answers/decisions remain historical; exact reset/reapproval consequences are designed per workflow |
| P6-02 | Asset Manager, Global User and Super User may reassign participants within their scope | Record reason, audit and notify affected users; former assignees retain read-only history of their assigned work, not permission to edit later work; replacement gets explicit task access |
| P6-03 | Routine app actions archive/retire/cancel with retained history | Permanent removal of historical/audit records only through separately controlled maintenance under company retention requirements; duration and legal requirements come from company owners |

## Acceptance examples for confirmed decisions

- Asset Operator can register/move an in-scope asset; direct disposal through that role alone is rejected, including calls bypassing the UI.
- Asset Manager can execute stock/reconciliation/direct-disposal actions in scope; ordinary role alone does not grant a different function's records.
- Business Owner sees relevant progress for a request initiated by another user, while unrelated owners' asset details remain inaccessible.
- Respondent can read/export a previously assigned completed process within its historical visibility, but cannot edit the closed response or expose unassigned records through that participation.
- Viewer can export assigned data but cannot broaden the export to unrelated records or modify business data.
- Inventory Operator can register/transfer authorized inventory and view history; another function is inaccessible through that role alone.
- Business Owner and Asset Manager can send relevant pending-task reminders; this action alone changes no business response/status.
- Global User can administer ordinary roles within its entity; requests granting privileged roles or changing another entity's assignments are rejected.
- Super User may grant/revoke Global User and Super User with attribution recorded.
- An assigned authorized approver is not blocked solely because they initiated the request; an unassigned/unauthorized user remains blocked.

These are requirement-level acceptance examples. Detailed test data, status names, API contracts, audit fields and deployment evidence are specified in later phases.
