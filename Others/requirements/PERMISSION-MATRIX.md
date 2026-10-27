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

## Round 5 proposals — require owner response

| ID | Proposal | Boundaries |
|---|---|---|
| P5-01 | Viewer reads authorized records/reporting; Inventory Operator registers/transfers quantity inventory and views history | Viewer has no business-data writes; Inventory Operator scope is its assigned organization/function |
| P5-02 | Operators export their authorized module data; Asset Manager exports in-scope operational data; Business Owner exports relevant owned-asset reports | Global User entity-wide and Super User application-wide export; Viewer and Respondent participation alone grant no bulk export; exported rows/fields respect the same visibility rules |
| P5-03 | Business Owner sends standardized reminders for pending responses in relevant requests | Only assigned participants receive reminders; no arbitrary recipient changes, response/status edits or automatic reopening implied; rate limiting and audit behavior are designed later |

## Acceptance examples for confirmed decisions

- Asset Operator can register/move an in-scope asset; direct disposal through that role alone is rejected, including calls bypassing the UI.
- Asset Manager can execute stock/reconciliation/direct-disposal actions in scope; ordinary role alone does not grant a different function's records.
- Business Owner sees relevant progress for a request initiated by another user, while unrelated owners' asset details remain inaccessible.
- Respondent can read a previously assigned completed process, but cannot edit the closed response or unassigned records through that participation.
- Global User can administer ordinary roles within its entity; requests granting privileged roles or changing another entity's assignments are rejected.
- Super User may grant/revoke Global User and Super User with attribution recorded.
- An assigned authorized approver is not blocked solely because they initiated the request; an unassigned/unauthorized user remains blocked.

These are requirement-level acceptance examples. Detailed test data, status names, API contracts, audit fields and deployment evidence are specified in later phases.
