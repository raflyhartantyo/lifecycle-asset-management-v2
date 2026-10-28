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

## Confirmed exception controls

| Action | Authorized role / participation | Required boundary | Decision |
|---|---|---|---|
| Reopen closed process | Asset Manager, Global User, Super User | Their respective scope; required reason/audit; prior answers/decisions preserved; workflow-specific reapproval effects still to be defined | D021 |
| Request reopening | Business Owner | Relevant business-owned work; does not itself reopen/change status | D021 |
| Reassign respondent task | Asset Manager, Global User, Super User | Their respective scope; reason/audit/notifications; former assignee retains read-only assigned history; replacement receives explicit task access | D022 |
| Archive/retire/cancel | Roles authorized for the specific business action | History preserved; this preservation rule does not grant every role a cancellation permission | D023 |
| Permanently remove historical/audit records | Separately controlled maintenance | Company retention requirements and maintenance authority must be established; no assumed retention duration | D023 |

Final-approver reassignment/delegation and per-workflow reapproval/cancellation consequences are still open; respondent reassignment is not a grant to alter arbitrary approval routes.

## Asset process overlays

- D024: spreadsheet registration supports a validation preview and operator confirmation of valid rows; invalid rows are reported without import.
- D025: cross-function/entity transfers require both outgoing/receiving Business Owner approvals before the asset's scope is changed. Registration/movement permissions do not bypass the required workflow approvals. D027–D029 confirm one explicit approval when the same person holds both capacities, rejection without an asset change, and approval for Business Owner changes within the same pair.
- D027–D029: changing Business Owner within a pair also requires both capacities to approve. Other location/custodian/status-only changes remain BAU if entity/function/Business Owner are unchanged.
- D026: routine asset transactions do not require remarks/reasons. Automatic change history is retained; reopening/reassignment reasons under D021/D022 still apply.

## Registration, disposal and inventory distinction

- D030: registration/import is create-only; identified duplicates are reported, not silently overwritten. Editing existing assets still requires its specific authorized business action.
- D031: disposal supports sale/non-sale retirement with disposal date and applicable sale details, without mandatory BAU remarks.
- D032: Inventory Operator's authorized inventory transfers do not use the asset-style dual Business Owner approval route. Scope/authority checks, quantity validation and movement history remain required, including supported cross-scope transfers.

## Stock verification overlays

- D033: cycle entity/function comes from the authoritative permission source and active authorized session. Available/In Use filters and due-date defaults confer no new data access.
- D034: Respondent supplies verification evidence; Asset Manager reviews discrepancies. Any master-record change still needs its authorized business action and applicable transfer approval.
- D035: relevant Business Owners sign off their asset results; acknowledged unresolved exceptions may remain on a closed cycle and are never reported as successfully verified.

## Reconciliation overlays

- D036: ledger comparison is preview/reporting work and does not itself authorize master-data mutation.
- D037: Accounting and Governance sign-off is explicit scoped workflow participation; it does not introduce a permanent application role or unrestricted data access.
- D038/D070: authorized Asset Manager explicitly previews/applies eligible corrections before Accounting/Governance final sign-off on actual results. Other action rights and approvals remain in force; outcomes are audited.

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

- Reopening without a reason or outside scope is rejected; a permitted reopening preserves the prior response/decision record.
- Reassignment records former/new assignees and the reason; former respondents cannot edit later work and replacement respondents see only their explicit tasks.
- Routine disposal/cancellation preserves historical evidence; business-data access alone cannot permanently erase audit history.

These are requirement-level acceptance examples. Detailed test data, status names, API contracts, audit fields and deployment evidence are specified in later phases.

## Asset Type catalogue maintenance — confirmed D056

| Action | Authorized roles | Scope |
| --- | --- | --- |
| Maintain Asset Types | Global User | Assigned entity only |
| Maintain Asset Types | Super User | Across entities |
| Select an existing Asset Type | Existing authorized registration/edit roles | Valid type for the asset's entity; no new mutation authority |

Other roles alone do not grant type-catalogue maintenance. Check explicit role combinations without granting entity-wide rights from a pair-scoped role. Every type retains its entity and Category parent. D056 does not grant editing of Accounting categories or global buildings. Backend enforcement and reclassification/deactivation rules still require implementation and verification.
