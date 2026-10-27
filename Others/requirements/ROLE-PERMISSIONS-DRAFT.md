# Role and permission working draft

Status: owner-selected role names and policies recorded; detailed responsibility mapping awaits review. Role names describe business responsibilities, not the physical Roles list schema. Whether responsibilities combine within one tuple is still to be confirmed; D002's one-row-per-email/entity/function contract remains.

## Confirmed decisions

- D008: Viewer, Asset Operator, Inventory Operator, Asset Manager, Business Owner and Superuser. Respondent(?) remains an open modeling question.
- D009: no blanket self-approval ban. The user must still have explicit approval authority for the assigned step and scope; names alone confer no privileges.
- D010: respondent permission is limited to assigned requests/assets and editing while the response step is open. Closed responses require explicit audited reopening; separate permissions govern broader access.

## Responsibility mapping — proposed, not approved

| Role | Proposed responsibility | Unresolved detail |
|---|---|---|
| Viewer | Read authorized records/reporting | Export and Power BI scope need explicit rules |
| Asset Operator | Register and move individually tracked assets | Direct disposal and accounting edits are not assumed |
| Inventory Operator | Register and transfer quantity inventory | No automatic asset-management rights |
| Asset Manager | Manage asset operations, stock verification and accounting reconciliation in assigned scope | Exact disposal, reopen, master-data, export and assignment permissions require confirmation |
| Business Owner | Accountable for assigned assets/business area; performs designated approval tasks | Confirm whether this denotes the existing MYID_Business_Owner asset identity, a function/business authority, or a distinct workflow participant |
| Superuser | Configure the application and administer delegated data/access settings | Current explicit scope rules remain; any global exception requires an owner decision. Final approval authority is not implied |
| Respondent (tentative) | Provide assigned verification responses/evidence | Recommend a request-specific assignment instead of a permanent broad role; D010 applies either way |

## Questions for round 3

1. Confirm the proposed duties and whether a person may hold multiple roles in one authorized pair.
2. Clarify Business Owner's business meaning and relationship to the asset-record business owner.
3. Confirm whether Superuser remains within explicitly assigned pairs or has an explicit global administrative exception.
4. Decide permanent Respondent role versus task-specific participation. Task participation must carry explicit scope and cannot grant unrestricted app/data access.

## Follow-up after this round

Define who can dispose, edit accounting values, export, maintain each reference list, assign roles, reopen requests and reassign participants. Define approval routing, substitutions, delegation, escalation and thresholds with company owners. Define response versus final approval state transitions. Decide Power BI access separately. Implement checks on backend writes and flow calls as well as the UI.
