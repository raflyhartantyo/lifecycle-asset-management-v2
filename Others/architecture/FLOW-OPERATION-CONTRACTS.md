# Flow and operation interfaces — LAM V2

Status: proposed logical interfaces through D072. [Machine-readable catalogue and request schema](interfaces/README.md) define reviewable payloads and example results. These are not flow definitions, callable deployed endpoints or a promise of one Power Automate flow per operation. Connector bindings and exact trigger/response representation follow each feature delivery.

## Interface boundary

The app calls named business operations; it never submits arbitrary list names, URLs, column names or unrestricted queries for a privileged connection to execute. Each operation specifies the input allow-list and returns an authorized data projection. Session roles/email/actor are not accepted as caller proof in the request envelope.

Trusted caller identity is resolved by the chosen implementation mechanism. Domain target identities, such as a destination Business Owner or grant recipient, remain legitimate payload fields and must be validated as targets, not used to impersonate the caller. System callbacks and monthly jobs have separate trusted entry points and are not ordinary app-invocable commands.

## Request and response contract

| Part | Proposed content | Rule |
| --- | --- | --- |
| Request | contractVersion, requestKey, operation, payload; optional contextHint; submissionKey for durable prepare/commands | Request key correlates an invocation; submission key deduplicates an intended durable action, scoped by authenticated actor and operation |
| Context hint | Organization/Function keys when a screen uses an operational context | Hint is validated against current grants and authoritative subject scope; task-only calls need no invented general context |
| Preview commit | previewRef, previewVersion, explicit selected item keys | Commit uses a server-held reviewed snapshot and current record/version checks; changed input requires a new preview/submission identity |
| Response | contractVersion, requestKey, operation, result, observedAt, data, errors; operationRef for accepted background work | Transport/dispatch result is distinct from per-item application, approval, verification and final-certification outcomes |
| Query pagination | Explicit cursor and supported bounded page size; response metadata for continuation/completeness | Cursor remains tied to the caller/query/context; no unrestricted offset or arbitrary query expression |
| Safe error | Stable code, safe message, authorized field/item target where appropriate | No hidden entity values/existence leaked in denial messages |

Supported interface result concepts: accepted, completed, validationFailed, denied, conflict, failed and indeterminate. These are transport/interface results, not stored business choice labels. Completed means this operation's specified work finished, not that an entire workflow/cycle is certified. Durable progress data independently records what applied, failed, awaits decisions or needs recovery. Do not label an entire partial batch completed without its explicit per-item outcomes and the feature's final completion policy.

An accepted result requires a durable operation reference. If the app loses the response before learning the reference, Operations.FindSubmission uses the same authenticated actor, operation and submission key to look up the prior outcome. A missing lookup after an uncertain write requires reconciliation under the operation's recovery contract; it is not blanket permission to repeat with a new key. Reusing a submission key with different inputs yields a safe conflict.

## Operation groups

| Group | Operations | Principal contract |
| --- | --- | --- |
| Session and reads | Session.Resolve; References.Query; Assets.Query/Get; Inventory.Query; Assignments.Query | Current authority and row/field projection; complete-result paging; no broad client collection |
| Registration/import | Registration.Preview/Commit; Import.Validate/Commit | Required fields, generated tag, unique accounting code, Available/Good/IDR and create-only rules; per-source-row outcomes |
| Asset movement | Movement.Preview/Submit | Independent per-asset edits/routes; existing owner/scope-transfer capacities before those transactions; versioned reviewed changes |
| Disposal/inventory | Disposal.Preview/Commit; Inventory.Preview/Commit | Explicit validated transaction without asset-style approval additions; correct quantity/current-state/retry evidence |
| Stock evidence | StockCycle.Preview/Create; StockResponse.Save; StockReview.Save | Assigned snapshot versus observations versus review/verification; no master write from response |
| Stock sign-off | StockSignoff.Prepare/Request | Owner-specific reviewed outcome version; readiness/exception policy; Microsoft Approvals assignment |
| Reconciliation | Reconciliation.Compare/PlanSave/ApplyPreview/Apply | Provenance/validated matching, explicit eligible correction application, actual outcomes and separate follow-ups |
| Final reconciliation sign-off | ReconciliationSignoff.Prepare/Request | Actual result snapshot after application; Accounting/Governance capacities; final rejection/rework/readiness policy remains open |
| Reporting/follow-up | Reports.Query/GetProcess; Reminder.Preview/Send; Export.Request; ReportRefresh.Request; Approvals.OpenContext | Same row/field scope for counts, details, files and messages; actual freshness and assigned approval opening |
| Administration | Grants.Preview/Commit; ReferenceChange.Preview/Commit | Exact Global/Super boundaries; real target identity and scope shape; shared-reference authority not inferred |
| Durable status | Operations.Get; Operations.FindSubmission | Query only permitted subject outcomes; request/operation IDs do not grant access |

The catalogue names feature-specific deferred policy gates without requiring tenant questionnaires. A payload can be structurally valid yet fail domain validation, be denied, or be unavailable until its deferred business contract is implemented. Physical flow action maps, connections, file resources and manual instructions arrive in the relevant per-flow handover.

## System-only processing

| System entry | Trigger source | Required result |
| --- | --- | --- |
| ApprovalDecision.Process | Trusted Microsoft approval orchestration | Verify service attempt/responder/capacity/snapshot; retain decision evidence; apply a transfer only after all required capacities and current-state checks; stock/reconciliation use their own semantics |
| BookValue.CalculatePeriod | Configured start-of-month schedule | Approved period/formula version, complete asset selection and per-asset results/retry recovery; formula remains deferred |
| Operation.Reconcile | Controlled recovery procedure under explicit operational authority | Resolve uncertain writes/evidence and reconcile existing identities; no generic unaudited repeat-all function |
| ReportRefresh.Observe | Reporting orchestration | Actual accepted/in-progress/completed/failed refresh evidence; no claim that submission finished the dataset refresh |

The catalogue separates these system entries from the app request schema. No endpoint lets the app send its own Approved callback or arbitrary monthly formula.

## Field intent and quantities

Omitted fields mean keep. A set intent supplies a value; a clear intent supplies none. Backend field allow-lists and requiredness decide which intents are valid in each operation. JSON Schema checks the shape, not whether the business field is editable or its target is authorized.

Use proposed decimal-string transport for quantities and IDR values to avoid relying on incidental floating-point serialization. This does not choose decimal precision, rounding, unit definitions, sale-price ranges or a depreciation formula. Date-only business dates remain distinct from timestamps/accounting periods; physical parsing/time-zone rules follow the feature contract.

## Required handler sequence

1. Parse the supported contract version and named operation; reject unknown fields/operations safely.
2. Resolve trusted invocation identity and current authority/participation.
3. Load authorized subjects and validate context, allowed fields, references, values and current versions.
4. For durable work, reconcile the authenticated submission identity and input fingerprint; return prior outcome or a conflict as appropriate.
5. Bind the exact reviewed snapshot/selection and workflow-specific prerequisites; no automatic valid-subset execution where policy is open.
6. Persist accepted work/outcomes/evidence using the delivered concurrency/recovery contract. No cross-record atomicity is assumed.
7. Return only the permitted projection with honest timestamps, pagination/completeness and recovery state.

Implementation may stage durable records before/after external calls; the exact safe ordering and recovery transitions are specified per operation. No schema validation pass proves authenticated caller identity, tenant permissions, a database transaction or runtime success.

## Planned verification

Local schema checks cover defined operations, required payload members, unknown actor/role input rejection, explicit set/clear representation, accepted-result references and example shapes. Runtime checks cover tampered subjects/snapshots/context, direct invocation, stale versions, duplicate or uncertain submissions, paging boundaries, mixed-owner rows/fields, safe export/download, response-only stock writes and actual-results reconciliation sign-off. Existing UAT remains NOT RUN until the owner implements and executes it.
