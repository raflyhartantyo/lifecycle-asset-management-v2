# Target screen and component contracts

Status: proposed implementation decomposition of accepted working flows through D071. Logical IDs below are stable references for future handovers, not existing Canvas screen names or paste-ready YAML. Physical screen/container/tab grouping remains an engineering choice. The 30 baseline YAML guides describe the preserved original app, not this target inventory.

## Entry and shared navigation

| ID | Purpose / entry | Access and exit contract | Dependencies / validation |
| --- | --- | --- | --- |
| SCR-ENTRY | Resolve authenticated identity/grants and task participation | Authorized Home/context, assigned-only tasks or access/help; no fallback to unrestricted data | Backend identity/access contract; AUTH-01/02/08/09 |
| SCR-CONTEXT | Select allowed entity/function when needed | Only allowed choices; revalidate unsaved selections and caches before switching | Ordinary pair/Global entity/Super application and task boundaries |
| SCR-HOME | Relevant work and authorized navigation | Counts/actions derive from effective scope; no new permission from a visible card | Shell, scoped queries, freshness and empty/error states |
| SCR-TASKS | Current and permitted historical assignments | Respondent work opens assigned response; approval work opens authorized Microsoft approval/context | Explicit assignments, historical field contract, D039 mobile usability |

## Asset and inventory workspaces

| ID | Purpose / accepted path | Required behavior | Contract gate |
| --- | --- | --- | --- |
| SCR-ASSETS | Search/browse authorized active assets | Add to movement/disposal selection without opening each detail; distinguish full result from current page | Authorized indexed queries; selection limits/paging |
| SCR-ASSET-DETAIL | Overview, Financials, History, Documents | Scoped evidence; optional single-item Move/Dispose prefill; no invented financial values | Exact fields/history/attachments; D065 |
| SCR-REGISTER | Guided create-only entry and review | D058 field review; generated tag; company-unique Accounting Asset Code; Available; Good default; IDR; application-required fields | Tag allocation, field/people/reference contracts, initial financial behavior |
| SCR-IMPORT | Template, validate/preview, confirm valid selected new rows, results | No silent existing-record overwrite; retain per-row invalid/duplicate/applied outcomes | Final template, duplicate rules, source evidence, retry contract |
| SCR-MOVE-SELECT | Search/add → view selected list → start movement | Repeated searches preserve draft; one/many selected; no duplicates; alternate detail entry | Scope/eligibility, paging and source-batch policy |
| SCR-MOVE-EDIT | Different changes for each asset | Prior/new values; required custodian for In Use; destination entity type/category mapping | Per-row field validation and explicit keep/clear semantics |
| SCR-MOVE-REVIEW | Review/submit → individual outcomes | BAU versus required owner/scope approval route visible; approval is not application | Owner capacities, version/retry/grouping/partial-failure policy |
| SCR-DISPOSE | Selected list → per-asset Sale/Non-sale details → review/confirm → results | Required date; buyer/price for Sale; optional shared date/buyer; individual prices; retained history; no approval | Eligibility, buyer model, mixed modes, overwrite/archive/recovery |
| SCR-INVENTORY | Quantity register, entry/detail, transfer and history | Authorized quantities/scopes; no asset-style dual-owner approval; no asset-level condition/custodian assumptions | Inventory item/quantity/unit/validation and concurrency contract |

## Stock verification

| ID | Purpose / accepted path | Required behavior | Contract gate |
| --- | --- | --- | --- |
| SCR-STOCK-CYCLES | Scoped setup/filter/default due date and progress | Entity/function from access matrix/context; Available/In Use scope; explicit assignment | Cycle/filter/default/assignment schema and versioning |
| SCR-STOCK-RESPOND | Assigned-assets list | First deliberate activation Correct; second Needs correction opens detail; no timing-dependent double-click; assigned history read-only | Save/cancel/reversal/final submission contract; D067/D068 |
| SCR-STOCK-CORRECT | Correct observed assignment data | Retain original snapshot; update only own open assignment/response; never master register | Allowed response fields/evidence and authorized mutation |
| SCR-STOCK-REVIEW | Manager compares/reviews evidence | Reviewed and verified are different; separate authorized master correction; visible unresolved exceptions | Verification criteria, state vocabulary and conflict behavior |
| SCR-STOCK-SIGNOFF | Owner-specific preview/request and progress | Microsoft Approvals; only relevant subset; acknowledged exceptions remain unverified | Readiness, configured routing, stale response/reapproval and closure/reopen policy |

## Reconciliation and reporting

| ID | Purpose / accepted path | Required behavior | Contract gate |
| --- | --- | --- | --- |
| SCR-RECON-UPLOAD | Scoped ledger file/period/mapping → comparison | Provenance and validation; comparison alone writes no master changes | Template, canonical matching, duplicates/out-of-scope policy and period alignment |
| SCR-RECON-REVIEW | Findings and reviewed resolution plan | Matches/missing/value-quantity/disposed exceptions; current/proposed values; follow-up links | Eligible correction fields, disposition model and complete counts |
| SCR-RECON-APPLY | Explicit authorized preview/application → actual results | Apply before final reconciliation sign-off; retain actual applied/failed/conflicted evidence; keep prerequisite transfer approvals | Version/retry/recovery and financial boundaries; no ledger Book Value overwrite |
| SCR-RECON-SIGNOFF | Final Accounting/Governance review of actual results | Versioned result snapshot; Microsoft Approvals; applied is separate from finally certified | Rejection/rework/rollback and unresolved-follow-up eligibility remain open |
| SCR-REPORT-PROGRESS | Filter relevant processes and open detail | Business Owner sees relevant owned work started by others; counts/stages/outcomes limited to authorized subset | Metrics/fields/deadlines, historical access and freshness |
| SCR-REPORT-DETAIL | Scoped Results/Activity; eligible reminders/export | No status/master mutation; standard relevant pending-respondent reminders; exports no broader than read access | Reminder delivery/rate limits, export format/download access, mixed-owner aggregation |
| SCR-REPORT-OVERVIEW | Asset overview and history sibling views | Authorized data/freshness; preserve history; no assumed Power BI permissions | Detailed dashboard metrics/layout and Power BI architecture still pending |

## Administration

| ID | Purpose | Required boundary | Contract gate |
| --- | --- | --- | --- |
| SCR-ADMIN-REF | Approved reference maintenance | Entity Asset Types: Global within entity, Super across all; fixed Categories and shared buildings have separate policies | Authority for other references, deactivation and integrity |
| SCR-ADMIN-ACCESS | Ordinary and privileged grants | Global grants ordinary roles within entity; Super administers Global/Super; backend enforcement and audit | Identity mapping, revocation, history and least-privilege service design |
| SCR-ADMIN-CONFIG | Permitted routing/default configuration | Explicit configured approvers/due defaults; no generic permission to reassign any approval | Configuration authority, versioning, substitutions and notification rules |

## Contract required for each delivered screen

The [shared component contracts](APP-COMPONENT-CONTRACTS.md) and [operation interface catalogue](interfaces/README.md) now define the target data/event boundary for these screens. Logical names are not existing Canvas properties or exported YAML; map them to supported controls and flow adapters in each implementation delivery.

Each future screen handover must identify the source commit, entry parameters, authorized data subset, visible fields/actions, shared component inputs/events, draft persistence and cancel/back behavior, validation/error/focus behavior, operation inputs/results and status/freshness handling. Include exact control/formula resources, connection/data prerequisites, numbered manual implementation steps, unit checks, mapped company-run cases and rollback resources.

Layout acceptance is not authority to enable unresolved writes. Supply disconnected previews only when clearly labeled; replace them with concrete bindings after the relevant contract gate closes. Use authorized backend checks even when UI choices are filtered. Keep general component state separate from business operation state.

## State dimensions to keep separate

| Dimension | Example distinction | Applies to |
| --- | --- | --- |
| Draft versus submitted | Form selection/input is not a durable business action | All workspaces |
| Service acceptance versus completion | Operation reference or refresh request is not completed work | Background actions/reports |
| Approval versus application | Approved transfer can still fail to apply | Asset owner/scope transfers |
| Response versus review versus verification | Correct submitted is not automatically Verified | Stock verification |
| Applied versus finally certified | Correction applied can await/reject final sign-off | Reconciliation D070 |
| Archived/closed versus erased | Historical evidence remains under approved access/retention | Disposal and closed work |

These are logical distinctions, not final physical choice values. Final labels, transition tables and storage fields are defined per operation. Detailed source references and visual links are in [the blueprint](IMPLEMENTATION-BLUEPRINT.md).
