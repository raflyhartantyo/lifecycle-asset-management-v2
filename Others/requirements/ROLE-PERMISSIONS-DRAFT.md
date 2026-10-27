# Role and permission working draft

Status: seven permanent role names, administrative scopes and respondent participation confirmed. Confirmed action permissions are distinguished from open proposals in PERMISSION-MATRIX.md. No application permissions have been implemented by these planning documents.

## Confirmed responsibility and scope model

| Role / participation | Confirmed meaning or scope | Pending permission details |
|---|---|---|
| Viewer | Read authorized records/reports; export data assigned to them (D018/D019) | Exact assignment/filter fields and report access |
| Asset Operator | Register and move assets in an explicitly assigned organization/function (D015) | Field-edit/export boundaries; operator alone has no direct-disposal permission |
| Inventory Operator | Register/transfer quantity inventory, view history and export authorized inventory-module data (D018/D019) | Field-edit/history and exceptional-action rules |
| Asset Manager | Operational asset management, stock verification, reconciliation, direct disposal, in-scope exports and standard respondent reminders (D015/D019/D020) | Reopening, master-data and approval-step permissions |
| Business Owner | Accountable asset ownership, relevant progress reporting, owned-asset report exports and standard respondent reminders (D011/D014/D016/D019/D020) | Exact reporting fields, designated approvals and report-editing rights |
| Global User | Maintenance across all functions of one assigned entity; ordinary role administration in that entity (D013/D017) | Business-action matrix; cannot grant/revoke Global User or Super User |
| Super User | Developer-like maintenance across all entities/functions; sole authority to grant/revoke Global User and Super User (D013/D017) | Detailed business actions, destructive-change and company-side deployment permissions |
| Respondent (task participation) | Read/export assigned data and historical assigned processes; edit assigned responses while their step is open (D010/D012/D019) | Historical detail fields, reassignment, reopening and offboarding rules |

Ordinary business roles retain D002/D007's tuple-scoped contract. Global User and Super User use explicit broader administrative scopes (D013); the grant schema is designed in Phase 2 rather than faking duplicate tuple rows. Operational records still carry a valid organization/function pair.

## Confirmed policies

- D009: no blanket self-approval ban. Approval must still be authorized for the assigned workflow step and scope.
- D011: asset business ownership and operational asset management are distinct responsibilities. Ownership alone does not grant automatic approval authority.
- D012: Respondent is task participation, not a permanent broad role. Historical assigned processes are readable, including completed ones. Editing closed responses requires explicit audited reopening.
- D014/D016/D019/D020: Business Owner monitors relevant request progress/status, exports owned-asset reports and sends standard reminders; report-definition editing remains open.
- D013: Global User has entity-wide maintenance scope; Super User has all-entity/function maintenance scope. Detailed permissions remain to be agreed. Actual maker/environment rights are managed in the company platform.

## Round 4 — confirmed

D015 assigns asset registration/movement to Asset Operator and adds stock verification, reconciliation and direct disposal for Asset Manager. D016 confirms Business Owner reporting on relevant owned-asset requests initiated by others. D017 reserves privileged-role grants/revocations to Super User while Global User manages ordinary roles in its entity.

## Round 5 — confirmed

D018 confirms Viewer read-only access and Inventory Operator registration/transfers/history. D019 permits Viewer and Respondent to export assigned data, while other roles export within their module/ownership/entity/application scope. D020 grants reminder authority to both Business Owner and Asset Manager. Export and reminder behavior remains subject to authorized data visibility.

## Round 6 — exception controls proposed, not approved

Asset Manager/Global User/Super User may reopen and reassign within their respective authority with recorded reasons and audit; Business Owner may request reopening. Prior respondents retain read-only historical access to assigned work. Routine business actions retain history through archiving/retirement/cancellation; permanent historical/audit removal is a separately controlled maintenance operation under company retention requirements. See PERMISSION-MATRIX.md.

## Later decisions

Define export formats/fields, reminder details, accounting field edits, master-list editing, reopen/reassign/delegate rights, final approval routing/thresholds and exception handling. Clarify historical process detail visibility and access revocation. Specify how entity-wide/all-entity administrators select context and how flows validate their authority. Validate Power BI access separately from Canvas UI permissions. No broad maintenance role silently grants an unresolved approval/destructive operation.
