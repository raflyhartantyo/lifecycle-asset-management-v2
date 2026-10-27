# Proposed LAM V2 navigation

Status: screen organization proposed for review; Microsoft Approvals is confirmed by D042. The earlier example image is illustrative, not an implemented screen contract.

Company sign-in → resolve app grants and assigned-task participation → authorized context → Home. A user with one authorized operational entity/function pair can have that context selected automatically. Multiple pairs require the authorized session selector. A task-only participant opens only their assigned/historical work rather than receiving general register access. No valid grant or task participation leads to an access/help screen.

All sections below branch directly from Home. The lower row of the example image is not a child of Inventory.

| Navigation | Screens / purpose |
| --- | --- |
| Home | Relevant actions, overdue work, scope-aware statistics and authorized context switching |
| Assets | Browse/detail, registration/import, BAU edits, transfer requests and direct disposal |
| Inventory | Quantity register, registration, authorized transfers and history |
| My Tasks | Assigned evidence/response tasks, status of Microsoft approval steps, authorized link to open the relevant Microsoft approval, historical task context |
| Stock Verification | Cycle setup, due dates, assignments, evidence review, owner sign-off progress and exceptions |
| Reconciliation | Ledger upload, comparison, Accounting/Governance approval progress and explicit correction application |
| Reports | Relevant request progress, authorized dashboards and scoped exports |
| Administration | Authorized reference data, role administration, routing/default configuration |

My Tasks has two experiences: respondents enter asset-verification evidence in LAM; approvers make workflow decisions through Microsoft Approvals. Propose an Open approval action rather than a competing custom Approve/Reject implementation in LAM. Link format, environment visibility, mobile behavior and permissions require tenant validation; do not invent a hardcoded deep-link contract.

LAM displays last-synchronized state and distinguishes pending, rejected/canceled/expired, approved and applied/failed application outcomes. These are proposed display concepts, not final physical choice labels. No transfer or reconciliation correction is shown as completed merely because approval was granted.
