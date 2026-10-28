# Proposed LAM V2 navigation

Status: screen organization proposed for review; Microsoft Approvals is confirmed by D042. The earlier example image is illustrative, not an implemented screen contract.

Company sign-in → resolve app grants and assigned-task participation → authorized context → Home. A user with one authorized operational entity/function pair can have that context selected automatically. Multiple pairs require the authorized session selector. A task-only participant opens only their assigned/historical work rather than receiving general register access. No valid grant or task participation leads to an access/help screen.

All sections below branch directly from Home. The lower row of the example image is not a child of Inventory.

| Navigation | Screens / purpose |
| --- | --- |
| Home | Relevant actions, overdue work, scope-aware statistics and authorized context switching |
| Assets | Browse/detail, registration/import, selected-assets movement workspace, transfer requests and direct disposal |
| Inventory | Quantity register, registration, authorized transfers and history |
| My Tasks | Assigned evidence/response tasks, status of Microsoft approval steps, authorized link to open the relevant Microsoft approval, historical task context |
| Stock Verification | Cycle setup, due dates, assignments, evidence review, owner sign-off progress and exceptions |
| Reconciliation | Ledger upload, comparison/review, explicit authorized correction application, then Accounting/Governance final sign-off progress on actual results (D070) |
| Reports | Relevant request progress, authorized dashboards and scoped exports |
| Administration | Authorized reference data, role administration, routing/default configuration |

Proposed reporting drill-down: Reports → Request progress → Scoped process detail → Review outcomes/activity, export authorized data or send an eligible standard respondent reminder. See [reporting progress design and visuals](REPORTING-PROGRESS-DESIGN.md). This supplies no new permission or approval surface.

My Tasks has two experiences: respondents enter asset-verification evidence in LAM; approvers make workflow decisions through Microsoft Approvals. Propose an Open approval action rather than a competing custom Approve/Reject implementation in LAM. Link format, environment visibility, mobile behavior and permissions require tenant validation; do not invent a hardcoded deep-link contract.

LAM displays last-synchronized state and distinguishes pending, rejected/canceled/expired, approved and applied/failed application outcomes. These are proposed display concepts, not final physical choice labels. Applied status requires a durable successful write. Final reconciliation certification is tracked separately after application under D070; an applied run awaiting final sign-off is not certified. Transfer approval alone does not mean the transfer applied.

## Frequent movements — D059

Primary movement path: search assets → add one or many to a movement selection → review selected assets → enter/confirm movement details. View means the selected list, not opening every asset detail. Propose visible row Add to movement and multi-select controls with a persistent selected count. A detail-page Move action may prefill the same workspace for one asset. Mixed-batch destination/grouping and failure semantics remain under design. No new bulk-disposal behavior is implied.
