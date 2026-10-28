# Stock-verification manager review and owner sign-off

Status: visual/process proposal following the accepted respondent direction. Existing D034/D035/D042 requirements apply; detailed review outcomes, controls and completion gates need owner review. No company resources changed and no runtime tests run.

## Proposed sequence

Collect assigned responses → Asset Manager compares evidence → Record review outcome → Resolve through separate authorized operations or record unresolved exception → Prepare owner-specific summaries → Request Microsoft Approvals → Track required decisions and acknowledged exceptions → Close only when the agreed completion conditions are met.

## Manager review

Provide a scoped review list with asset identity, issue, respondent and review state. Selecting a row shows assigned snapshot and respondent observations side by side. The sample shows building/custodian/condition discrepancies and a proposed Unresolved — follow-up required review outcome. It does not establish a complete or final review-state vocabulary.

Record review metadata separately from original respondent evidence and assigned context. Preserve actor/time and previous review versions. A reviewed item is not automatically verified. A respondent's Correct assertion is not a substitute for the defined review/outcome process. Exact verification criteria for matching versus discrepant observations remain to be specified.

Recording review does not update master data. An optional Prepare a separate register correction link can prefill the authorized movement workspace with proposed observations, but actual application requires explicit preview, authority/current-version checks and any owner/scope-transfer approval. Never blindly copy response fields into the register. No mandatory routine remarks/reason is added; exceptional audited reopen/reassignment reasons retain their existing rules.

## Business Owner sign-off

Once eligible reviewed outcomes are ready, prepare a summary for each relevant Business Owner. Each receives only their relevant assets/results and exceptions; a shared cycle must not leak other owners' data. Actual approval authority comes from explicit configured routing/assignment, not solely a display label or ownership relationship.

Microsoft Approvals collects the decisions; no competing Approve/Reject control is added to LAM. The sample Request sign-offs action creates workflow requests; it is not itself a sign-off or cycle closure. An illustrative review checkbox confirms the operator reviewed the preview; its exact requirement is not a new confirmed business rule.

Freeze/version the reviewed scope/results used by each approval attempt. Changes to evidence, ownership or scope need the final invalidation/reapproval rules; old decisions must not silently cover unseen revised results. Persist service IDs, responder/decision evidence and business application state under the approved integration contract.

## Exceptions and closure

Every asset requires a verified outcome or an explicitly recorded unresolved exception. A cycle may close with acknowledged exceptions under D035; unresolved/unanswered assets remain visibly unverified and never enter the successful verified count. Do not hide pending/unreviewed data behind a single complete percentage. The final treatment of unanswered tasks, acknowledgement authority and owner rejection/reopening must be designed explicitly.

The two visual screens show different times in the same illustrative cycle: manager review has 43 reviewed and 7 still needing review; after review completion the sign-off preview has 43 verified and 7 unresolved, all reviewed. These figures demonstrate separate dimensions, not a rule that reviewing a row verifies it. Owner subsets sum to the cycle totals: 30/26/4 and 20/17/3.

Master corrections, approval decisions, review completion and cycle closure are separate recorded outcomes. Link related operations without treating a failed or pending master update as successfully applied.

## Remaining design gates

Complete review-state set and verification criteria; bulk review controls; incomplete-response handling; evidence change/reapproval; configured sign-off routing; multiple-owner visibility; acknowledgement and rejection/reopen behavior; reminders and default due dates; update-conflict/retry recovery; retention, query/index/pagination and backend authorization. The existing approvals provisioning/licensing checks remain unverified.

## Planned checks

Assigned/scoped evidence visibility; immutable response context; reviewer authority; no automatic master write; separate correction preview and required transfer approvals; reviewed versus verified counts; owner subset isolation; late/stale approval; rejection/reopen; acknowledged unresolved exceptions remain unverified; complete counts across pages; failures/retries with durable audit. All NOT RUN.

[Visuals](../design/concepts/2026-10-28/stock-verification-manager-review/README.md) · [Approvals integration](APPROVALS-INTEGRATION-DESIGN.md).
