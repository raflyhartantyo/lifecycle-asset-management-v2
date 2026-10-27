# Role and permission working draft

Status: seven permanent role names, administrative scopes and respondent participation confirmed. Detailed action permissions remain proposed. No application permissions have been implemented by these planning documents.

## Confirmed responsibility and scope model

| Role / participation | Confirmed meaning or scope | Pending permission details |
|---|---|---|
| Viewer | Ordinary business role in an explicitly assigned organization/function | Read/export/reporting boundaries |
| Asset Operator | Ordinary business role in an explicitly assigned organization/function | Registration, movement, disposal and field-edit boundaries |
| Inventory Operator | Ordinary business role in an explicitly assigned organization/function | Quantity registration/transfer and history boundaries |
| Asset Manager | Operational management of assets in authorized scope | Stock/reconciliation initiation, direct disposal, reopening, exports and master-data permissions |
| Business Owner | Accountable owner of specified assets, reflected in the existing asset Business Owner field; reporting oversight including relevant request progress/status | Exact reporting visibility, exports, follow-up actions, designated approvals and report-editing rights |
| Global User | Maintenance across all functions of one assigned entity | Administration versus business-action rights, privileged-role assignment and cross-function views |
| Super User | Developer-like maintenance across all entities/functions | Detailed business-action, privileged-role, destructive-change and company-side deployment permissions |
| Respondent (task participation) | Explicit process assignment; read access to historically assigned processes; edit assigned responses while the response step is open | Historical detail visibility, reassignment, reopening and offboarding rules |

Ordinary business roles retain D002/D007's tuple-scoped contract. Global User and Super User use explicit broader administrative scopes (D013); the grant schema is designed in Phase 2 rather than faking duplicate tuple rows. Operational records still carry a valid organization/function pair.

## Confirmed policies

- D009: no blanket self-approval ban. Approval must still be authorized for the assigned workflow step and scope.
- D011: asset business ownership and operational asset management are distinct responsibilities. Ownership alone does not grant automatic approval authority.
- D012: Respondent is task participation, not a permanent broad role. Historical assigned processes are readable, including completed ones. Editing closed responses requires explicit audited reopening.
- D014: Business Owner monitors relevant request progress/status through reporting. Export, follow-up actions and report-definition editing remain open.
- D013: Global User has entity-wide maintenance scope; Super User has all-entity/function maintenance scope. Detailed permissions remain to be agreed. Actual maker/environment rights are managed in the company platform.

## Round 4 proposals — not yet approved

1. Asset Operator registers/moves assets. Asset Manager additionally runs stock verification and reconciliation and performs direct disposal in scope.
2. Business Owner reporting includes requests involving their business-owned assets even when initiated by other people, exposing only relevant records/details in authorized scope. Exports and report-editing/follow-up actions remain separate permissions.
3. Global User may maintain ordinary business-role assignments within its entity. Only Super User may grant/revoke Global User and Super User. Define role combinations and restrictions against privilege escalation in the detailed matrix after owner confirmation.

## Later decisions

Define exports, accounting field edits, master-list editing, reopen/reassign/delegate rights, final approval routing/thresholds and exception handling. Clarify historical process detail visibility and access revocation. Specify how entity-wide/all-entity administrators select context and how flows validate their authority. Validate Power BI access separately from Canvas UI permissions. No broad maintenance role silently grants an unresolved approval/destructive operation.
