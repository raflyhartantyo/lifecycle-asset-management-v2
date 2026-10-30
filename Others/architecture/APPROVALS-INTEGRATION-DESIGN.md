# Proposed Microsoft Approvals integration for LAM

Status: design recommendation following confirmed platform selection D042; company availability, licensing and implementation remain unverified. Read [platform research](MICROSOFT-APPROVALS-RESEARCH.md) for Microsoft-sourced capabilities/limitations. Read [navigation](APP-NAVIGATION.md) for the revised task experience.

## Responsibility split

LAM collects business requests and stock evidence, enforces scoped visibility, displays progress and retains business history. Power Automate validates requests and routing, requests Microsoft approvals, records decisions and safely continues the authorized business operation. Approvers use the relevant Microsoft approval surface; LAM's task view provides context/status and a validated opening link. This is a proposed implementation of the user's selected approval service, not a claim that such links or synchronization have been tested.

The app submission must return a request/correlation ID promptly rather than keep a Canvas call open while waiting days for approval. A background workflow handles the human wait and updates durable state. The authenticated caller, current access grants and record scope must be checked server-side; an email/role/entity submitted by the client is not proof of authority.

## Workflow mapping

| Business workflow | Proposed Microsoft approval use | Rule after decision |
| --- | --- | --- |
| Asset scope transfer or Business Owner change | Resolve outgoing/receiving owner capacities. For two distinct named people, standard Approve/Reject — Everyone must approve is the simplest proposed route. Parallel versus sequential routing remains open. | Apply only after all required capacities approved and current asset version/authority revalidated. Rejection leaves asset unchanged. |
| Both owner capacities held by same person | Resolve the same canonical identity before sending; request one explicit decision and record both capacities. | No automatic or double approval. Do not rely on undocumented duplicate-recipient handling. |
| Stock-verification owner sign-off | Owner-specific approval for the relevant reviewed subset; show explicit unresolved exceptions. | Evidence collection remains in LAM. A sign-off cannot turn unresolved/unanswered assets into verified assets. |
| Reconciliation | Configured Accounting and Governance final sign-off assignments after explicit authorized correction application (D070); order between these approvers and same-person capacity policy remain open. | Sign-off covers a versioned snapshot of actual applied results, failures and follow-ups. Rejection/rework/rollback and unresolved-follow-up eligibility remain open; final sign-off does not itself apply corrections. |
| Direct disposal / quantity-inventory transfer | No newly added approval route. | Keep their confirmed authorized transaction/history controls. |

All-recipient transfer approvals must carry only the shared transfer snapshot and relevant context; never an unrelated entity's register or a mixed-owner stock cycle. Send owner-specific stock subsets separately. Approval assignment is not broad data access. For stock/reconciliation summaries near 5,000 assets, use concise scoped summaries and authorized report links, not thousands of rows in an approval message.

## State and evidence requirements

Final physical lists/columns follow with operational contracts. Required logical records include:

- Business request ID, workflow type, entity/function or source/destination scopes, subject record versions and immutable review snapshot/version.
- Approval attempt/version and service approval ID when available, environment alias and correlation to the flow run. Retried creation must not silently send duplicate requests; ambiguous creation results need reconciliation rather than blind recreation.
- Required approval capacities, assigned identity IDs, effective responder identity, response/time/comments if supplied, and reassignment/cancellation evidence. Separate service decision from business validity.
- Business outcome, application attempt/results, failure/retry state, audit records and history accessible only to authorized historical participants. Preserve superseded attempts when reopening or resubmitting.

The Microsoft approval is the authoritative decision event; LAM's business ledger records how that decision relates to scope, snapshot and application. A manually edited client status is not an accepted approval. Synchronization and record updates need retry/reconciliation paths; stale status must be visible rather than interpreted as completion.

## Reliability and policy gates

- Choose a bounded approval deadline safely within documented wait constraints, with reminder, expiry and recovery paths. Exact business deadline and handling of work that legitimately lasts longer remain open.
- Evaluate Start and wait versus split Create/Wait in the implementation prototype. Split creation can expose the ID early but has a documented fast-response race; short action spacing is a mitigation to test, not proof of correctness. Do not change Microsoft-managed Dataverse statuses as an improvised workaround.
- Treat canceled, timed-out, superseded and failed attempts explicitly. A timeout is not a rejection or approval. A late response for an old attempt cannot modify the register.
- For approval-gated transfers, revalidate approval identity/capacity, request version, current authority and asset state before applying the transaction. If review-relevant details changed, invalidate the stale attempt and obtain a new decision rather than applying approval to unseen changes.
- For reconciliation, preserve the actual application results and versioned final-review snapshot before requesting sign-off (D070). Later changes must not inherit certification of unseen results; define invalidation/resubmission and rejection/rework handling before implementation.
- Platform reassignment capability does not settle the company policy. Respondent reassignment D022 is not permission to delegate Business Owner or Accounting/Governance approval. Final policy must define accepted substitutes and audit evidence; unauthorized substitutes cannot complete a capacity.
- Native request cancellation and flow-run cancellation are separate operations to validate. Define an operator-supported cleanup/reconciliation route for abandoned approvals; no blanket connector cancellation capability is assumed.
- Store durable business evidence under approved access and retention controls. Neither transient run history nor a Teams notification card is the business audit ledger. Retention duration remains a company dependency.

## Implementation-time checks, independent of new site creation

D072 defers general capability questionnaires; these remain optional checks for the relevant implementation step. The owner handles setup, with Claude explaining supplied observations if needed:

1. Is Approvals available in company Teams? Open the app and inspect only; no request creation required.
2. Can the user open Power Automate in ENV-A and view existing owned/shared flows? ENV-A's type/default status and Dataverse/Approvals provisioning are UNKNOWN unless an authorized administrator confirms them.
3. Ask the relevant administrator/flow owner whether Approvals is already provisioned in ENV-A, what creator/responder licenses apply, whether SharePoint/Approvals/Teams connectors can be combined under company policy, and whether an approved flow owner/connection identity exists.
4. Confirm approved test identities and notification destinations before a later integration test. Do not provision Dataverse or trigger first-use approval setup during this read-only check.

These are implementation references, not a requested general report or permission to change company settings. D073 hosts dedicated LAM resources on SITE-F, the existing Function site; no dedicated-site creation is required. SharePoint lists/connections are configured with their affected feature, and architecture design continues independently.

## Company tests required before acceptance

Two-person all-approve; one rejection; same-person dual capacity; allowed self-approval; unauthorized responder/reassignment; changed asset version; duplicate creation/update retries; rapid response before the wait; timeout/late response; cancel/reopen/resubmit; app/Teams/Outlook state convergence; correct ENV-A visibility; mobile opening; historical participant scope; 5,000-asset summary completeness and applied-but-not-finally-signed-off reconciliation. All are NOT RUN. Final cases/fixtures accompany the actual flow implementation.
