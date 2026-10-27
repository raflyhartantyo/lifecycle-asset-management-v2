# Microsoft Approvals research for LAM V2

Research date: 2026-10-27. Status: research and proposed implementation guidance; no company systems inspected or changed.

## Official platform findings

### Teams client and workflow engine

Microsoft Teams Approvals is a user interface for sent, received and historical approvals. Power Automate workflow approvals can appear there. Manually creating a basic approval in Teams is a different entry path from a flow-triggered business process. [Microsoft Support: What is Approvals?](https://support.microsoft.com/en-us/teams/shifts/what-is-approvals)

Approvals initiated directly from the Teams Approvals app use the organization's default environment. This does **not** establish that LAM's ENV-A is the default. Teams administrators can disable the app. [Native approvals in Teams](https://learn.microsoft.com/en-us/power-automate/teams/native-approvals-in-teams)

### Approval policy

| Type | Documented completion rule |
| --- | --- |
| Approve/Reject — Everyone must approve | All assigned people approve, or one person rejects. |
| Approve/Reject — First to respond | One person's approval or rejection completes the request. |
| Custom responses — Wait for all responses | Every assigned person must respond; this is not the same rejection behavior as Everyone must approve. |
| Custom responses — Wait for one response | One response completes the request. |

These distinctions are documented in [approval types and behaviors](https://learn.microsoft.com/en-us/power-automate/get-started-approvals). The rejection rule is also illustrated in Microsoft's [all-assigned approval tutorial](https://learn.microsoft.com/en-us/power-automate/all-assigned-must-approve).

Sequential workflows are supported, including a pre-approval followed by a final approval only after the first stage approves. [Sequential approvals](https://learn.microsoft.com/en-us/power-automate/sequential-modern-approvals)

### Actions and lifecycle limits

`Start and wait for an approval` creates Dataverse records, sends notifications and blocks until completion or timeout. `Create an approval` creates and notifies without waiting; decision outputs are not immediately available. `Wait for an approval` subsequently waits for the existing approval. [Action differences](https://learn.microsoft.com/en-us/troubleshoot/power-platform/power-automate/approvals/differences-between-flow-approval-actions)

Microsoft warns that an immediate response between separate Create and Wait actions can leave the flow stuck; keep the actions close together if that pattern is required. Its approvals known-issues page states an approval wait can fail after **28 days**, leaving the approval in the action center. [Approval known issues](https://learn.microsoft.com/en-us/power-automate/approvals-known-issues)

Separately, general cloud-flow limits specify a **30-day maximum run**, including pending approvals, and **30-day run-history retention**, calculated from run start. Neither limit guarantees indefinite processing or business-record retention. [Flow duration and retention](https://learn.microsoft.com/en-us/power-automate/limits-and-config)

### Storage, permissions and licensing

Approvals require Dataverse even when business data lives in SharePoint. Initial provisioning in a non-default environment requires an environment administrator. Standard approvals use a standard connector; suitable Power Automate rights included with eligible Microsoft 365/Dynamics licenses can cover standard-connector use. Recipient licensing and environment membership still need checking. [Get started and prerequisites](https://learn.microsoft.com/en-us/power-automate/get-started-approvals)

Directly querying/updating approval tables through the Microsoft Dataverse connector introduces a **Premium** connector dependency; this differs from the Approvals connector's internal storage. [Dataverse connector classification](https://learn.microsoft.com/en-us/connectors/commondataserviceforapps/)

The standard connector accepts email, UPN or Entra user IDs, with semicolon-separated recipients. Basic Approve/Reject response values are case-sensitive. Its public action list includes Create, Start and wait, and Wait; it does not expose a general-purpose cancellation/reassignment action. [Approvals connector reference](https://learn.microsoft.com/en-us/connectors/approvals/)

### Responding, notifications and administration

Approvers can respond through supported Outlook messages, Teams cards or the Power Automate action center; actual access depends on user licensing and environment configuration. [Get started with approvals](https://learn.microsoft.com/en-us/power-automate/get-started-approvals)

Recipients can reassign an approval in Power Automate. Requesters cannot use that same reassignment path; Microsoft describes cancellation and changing the approver instead. Pending requests can be cancelled through the Sent tab. [Approval how-to scenarios](https://learn.microsoft.com/en-us/power-automate/guidance/business-approvals-templates/process-approval-requests)

A separately posted Teams adaptive card may not update when someone responds in email or the action center. Do not treat a visible card as the definitive current business state. [Approval known issues](https://learn.microsoft.com/en-us/power-automate/approvals-known-issues)

### Audit and retention

Teams Approvals emits Microsoft Purview audit activities such as approval creation, decisions, cancellation and reassignment. Dataverse approval-entity auditing must be enabled/configured for additional data-operation auditing. Dataverse retention policies require administration; Teams approval-history visibility is not a project-specific retention guarantee. [Teams Approvals administration](https://learn.microsoft.com/en-us/microsoftteams/approval-admin)

## LAM design recommendations — not platform guarantees

1. Generate LAM decisions through controlled Power Automate workflows. Use Microsoft Approvals to make the decision, and LAM to initiate requests, collect respondent evidence, display authorized progress/history and link to the approval. Do not add competing app Approve/Reject buttons.
2. For an asset entity/function or Business Owner change, use Everyone must approve for the outgoing and receiving owners. Resolve canonical user identities and deduplicate **before** submission: one explicit approval may cover both owner obligations when the same person fills both roles. The sources reviewed do not guarantee automatic connector deduplication. Record both obligations against the response.
3. A rejection leaves the asset unchanged. Apply an approved change only after validating request version, pending state, expected responders, current authorization and unchanged source asset scope. Ignore duplicate, superseded, cancelled or late results; record them for investigation.
4. Stock verification uses the required Business Owner sign-off. Reconciliation requires configured Accounting/Governance sign-offs before an explicit Asset Manager apply step; order is a business-policy choice, not established by this research. Keep disposal request/approval retired and do not introduce asset-style dual-owner approvals for inventory.
5. Persist request ID, request version, process/scope, assigned identities, role obligations, approval ID/link when available, status, deadline, responses, responder identities, timestamps and application result in permission-controlled V2 business records. Business Owner reporting uses these records rather than tenant-wide approval-table access. Exact lists/columns remain to be designed.
6. Use explicit configurable expiry shorter than the documented 28-day approval-wait boundary and an exception path; the business SLA remains TBD. Failure, cancellation and expiry must never apply the requested asset change. Plan cleanup of abandoned approvals separately: marking LAM Expired or cancelling a flow is not proof that its approval disappeared.
7. Prefer Start and wait for straightforward short-lived cases. If persisting the Approval ID before waiting requires Create plus Wait, prototype the immediate-response race and recovery. Do not promise that merely splitting actions enables unlimited lifetime.
8. Keep reassignment controlled. Check whether the selected action exposes reassignment settings, test them, and revalidate actual responder authority before applying changes. Built-in reassignment must not bypass the configured Business Owner obligations or LAM's audited reassignment policy. Do not implement unsupported direct edits to system approval tables as a shortcut.
9. Test Teams/Outlook delivery and portal fallback using approved identities in ENV-A. Verify Teams app availability, Dataverse provisioning, environment access, licenses, data policies, flow owner/continuity and retention with company administrators. You implement and test; Claude supplies Q&A guidance based only on information you provide.

## Required acceptance checks

All pending; no runtime tests executed.

- Distinct owners: both approve before application; either rejects without application.
- Same owner: one explicit response satisfies both recorded obligations.
- Incorrect or reassigned unauthorized responder: cannot apply the change.
- Immediate response, repeated trigger, retried completion and stale request: no stuck request or duplicate business change; failures surface for recovery.
- Timeout, cancellation, revoked authority and changed asset scope: preserved history and no unauthorized application.
- Teams availability, email/portal response, mobile access and business-state refresh verified in the company environment.
- Reporting/history remain authorized and durable beyond ordinary flow-run retention.

The approximately 5,000-asset volume does not require one approval per registered asset. Approvals belong to business requests; asset-query delegation, indexed lists and reporting capacity require separate design.
