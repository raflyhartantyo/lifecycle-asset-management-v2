# Direct disposal — working design

Status: interaction accepted D062; single and multiple selection confirmed D063; per-asset details/shared-value shortcut confirmed D064. Physical/flow implementation pending. No company resources changed or tests run.

## Accepted user flow

Select asset(s) → Choose Sale or Non-sale → Enter disposal details → Review → Confirm.

| Mode | Required business inputs |
| --- | --- |
| Sale | Disposal date, buyer and selling price |
| Non-sale | Disposal date |

Apply requiredness through the application under D044. Preserve D026's absence of mandatory BAU remarks/reason. Do not create a disposal-request approval route; direct disposal remains a permitted authorized operation under existing role/scope rules. Review/confirmation is the operator's transaction confirmation, not a new business approval.

On successful completion, remove the asset from the active register while preserving its identity and disposal/history evidence. The physical choice between retaining one lifecycle row and creating a linked inactive/archive record remains a data-contract decision; this note does not prescribe deleting a master record. Do not delete historic references or approvals.

## Selection cardinality — confirmed D063

Support one or multiple selected assets through the same selected-assets list. Search/add/review selection without requiring separate disposal sessions for every asset. The same single-asset path is a one-item selection. Validate each asset's authority, current state/version and disposal inputs; preserve per-asset outcomes/history.

Per-asset disposal details and an optional Apply to selected shortcut for shared values such as date/buyer are confirmed by D064. Selling price remains per asset; no batch-total price allocation is introduced. Mixed Sale/Non-sale behavior and exact shortcut/overwrite interactions remain to be specified.

## Proposed safeguards

Show asset identity, original values, disposal mode, date and applicable buyer/price details in a final preview. Revalidate actor scope/authority, current asset/version and outstanding movement state before execution. Use durable operation IDs, old/new audit history and explicit failure/recovery outcomes. No asset becomes Disposed merely because a confirmation button was clicked if durable application failed.

Ready to Auction remains an allowed Condition value. It does not prove disposal occurred and is not assumed to be a prerequisite for direct disposal; eligibility rules need the final business contract. No auction management module is implied. Monthly Book Value eligibility and post-disposal handling remain part of the deferred formula/finance design.

## Remaining details

Authorized direct-disposal field edits; relevant sale amount precision/range/currency rules (IDR remains fixed); buyer representation; attachments/evidence requirements; date/backdating rules; active/pending asset eligibility; interaction with transfers/monthly financial calculation; archive/state transitions; retry/failure recovery. For batch disposal, retain D064's per-asset inputs and optional shared date/buyer shortcut. Confirm mixed Sale/Non-sale handling, exact shortcut/overwrite behavior and execution/failure semantics.

## Planned checks

Sale required fields; non-sale path; optional SharePoint fields still validated by the application; unauthorized scope; stale/already-disposed assets; failed/retried application; active-register exclusion only after success; retained identity/history and report visibility. All NOT RUN. Include single-item and multi-item selection, duplicate selection prevention, selection persistence, per-asset validation/results/history, and retry/failure recovery. Include per-asset sale price, optional shared date/buyer application, later row-specific edits and no unintended buyer requirement for Non-sale. No batch-total price allocation is implemented. Final mixed-mode/overwrite checks depend on the remaining interaction decisions.

## Per-asset entry and Apply to selected — D064

Keep each asset's disposal details independently reviewable. A user can enter a date/buyer once and deliberately apply it to a chosen subset, then adjust individual rows. This action only fills the form; execution still waits for final review and confirmation. Exact overwrite affordance remains a UI proposal to review; avoid silently changing unrelated rows or clearing deliberate values.

Each Sale asset must have its own selling price and required buyer/date. Non-sale requires disposal date, with no buyer/selling-price requirement introduced by a shared shortcut. Display per-asset validation and old/new/disposal values in the review. Do not auto-allocate a total price across rows, treat a shared buyer as approval authority, or infer an asset's completed disposal from its selected condition.
