# Role and permission working draft

Status: seven permanent role names, administrative scopes and respondent participation confirmed. Confirmed action permissions are distinguished from open proposals in PERMISSION-MATRIX.md. No application permissions have been implemented by these planning documents.

## Confirmed responsibility and scope model

| Role / participation | Confirmed meaning or scope | Pending permission details |
|---|---|---|
| Viewer | Ordinary business role in an explicitly assigned organization/function | Read/export/reporting boundaries |
| Asset Operator | Register and move assets in an explicitly assigned organization/function (D015) | Field-edit/export boundaries; operator alone has no direct-disposal permission |
| Inventory Operator | Ordinary business role in an explicitly assigned organization/function | Quantity registration/transfer and history boundaries |
| Asset Manager | Operational asset management, stock verification, accounting reconciliation and direct disposal in authorized scope (D015) | Reopening, exports, master-data and approval-step permissions |
| Business Owner | Accountable owner of specified assets, reflected in the existing asset Business Owner field; reporting oversight including relevant request progress/status | Exact reporting visibility, exports, follow-up actions, designated approvals and report-editing rights |
| Global User | Maintenance across all functions of one assigned entity; ordinary role administration in that entity (D013/D017) | Business-action matrix; cannot grant/revoke Global User or Super User |
| Super User | Developer-like maintenance across all entities/functions; sole authority to grant/revoke Global User and Super User (D013/D017) | Detailed business actions, destructive-change and company-side deployment permissions |
| Respondent (task participation) | Explicit process assignment; read access to historically assigned processes; edit assigned responses while the response step is open | Historical detail visibility, reassignment, reopening and offboarding rules |

Ordinary business roles retain D002/D007's tuple-scoped contract. Global User and Super User use explicit broader administrative scopes (D013); the grant schema is designed in Phase 2 rather than faking duplicate tuple rows. Operational records still carry a valid organization/function pair.

## Confirmed policies

- D009: no blanket self-approval ban. Approval must still be authorized for the assigned workflow step and scope.
- D011: asset business ownership and operational asset management are distinct responsibilities. Ownership alone does not grant automatic approval authority.
- D012: Respondent is task participation, not a permanent broad role. Historical assigned processes are readable, including completed ones. Editing closed responses requires explicit audited reopening.
- D014: Business Owner monitors relevant request progress/status through reporting. Export, follow-up actions and report-definition editing remain open.
- D013: Global User has entity-wide maintenance scope; Super User has all-entity/function maintenance scope. Detailed permissions remain to be agreed. Actual maker/environment rights are managed in the company platform.

## Round 4 — confirmed

D015 assigns asset registration/movement to Asset Operator and adds stock verification, reconciliation and direct disposal for Asset Manager. D016 confirms Business Owner reporting on relevant owned-asset requests initiated by others. D017 reserves privileged-role grants/revocations to Super User while Global User manages ordinary roles in its entity.

## Round 5 — proposed, not yet approved

See PERMISSION-MATRIX.md. Viewer is scoped read-only; Inventory Operator registers/transfers quantity inventory and reads history. Module/ownership-scoped exports are proposed for operators, managers and Business Owners, with administration scopes applying to Global User/Super User. Viewer/Respondent participation alone does not grant bulk export. Business Owner may send standardized reminders for pending relevant response tasks, while response/status edits require their separate permissions.

## Later decisions

Define exports, accounting field edits, master-list editing, reopen/reassign/delegate rights, final approval routing/thresholds and exception handling. Clarify historical process detail visibility and access revocation. Specify how entity-wide/all-entity administrators select context and how flows validate their authority. Validate Power BI access separately from Canvas UI permissions. No broad maintenance role silently grants an unresolved approval/destructive operation.
