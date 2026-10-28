# Direct disposal — working design

Status: interaction accepted D062; physical/flow implementation pending. No company resources changed or tests run.

## Accepted user flow

Select asset(s) → Choose Sale or Non-sale → Enter disposal details → Review → Confirm.

| Mode | Required business inputs |
| --- | --- |
| Sale | Disposal date, buyer and selling price |
| Non-sale | Disposal date |

Apply requiredness through the application under D044. Preserve D026's absence of mandatory BAU remarks/reason. Do not create a disposal-request approval route; direct disposal remains a permitted authorized operation under existing role/scope rules. Review/confirmation is the operator's transaction confirmation, not a new business approval.

On successful completion, remove the asset from the active register while preserving its identity and disposal/history evidence. The physical choice between retaining one lifecycle row and creating a linked inactive/archive record remains a data-contract decision; this note does not prescribe deleting a master record. Do not delete historic references or approvals.

## Selection cardinality — unresolved

The owner accepted the disposal steps, but did not explicitly choose between the offered single-asset and multiple-selected-assets execution. Keep this open before designing bulk price/buyer fields or promising bulk execution. Reusing a selected-assets list is a recommended option for review, not a confirmed bulk-disposal requirement.

## Proposed safeguards

Show asset identity, original values, disposal mode, date and applicable buyer/price details in a final preview. Revalidate actor scope/authority, current asset/version and outstanding movement state before execution. Use durable operation IDs, old/new audit history and explicit failure/recovery outcomes. No asset becomes Disposed merely because a confirmation button was clicked if durable application failed.

Ready to Auction remains an allowed Condition value. It does not prove disposal occurred and is not assumed to be a prerequisite for direct disposal; eligibility rules need the final business contract. No auction management module is implied. Monthly Book Value eligibility and post-disposal handling remain part of the deferred formula/finance design.

## Remaining details

Single versus multiple selection; authorized direct-disposal field edits; relevant sale amount precision/range/currency rules (IDR remains fixed); buyer representation; attachments/evidence requirements; date/backdating rules; active/pending asset eligibility; interaction with transfers/monthly financial calculation; archive/state transitions; retry/failure recovery. For future batch disposal, confirm common versus per-asset mode/date/buyer and selling-price representation explicitly.

## Planned checks

Sale required fields; non-sale path; optional SharePoint fields still validated by the application; unauthorized scope; stale/already-disposed assets; failed/retried application; active-register exclusion only after success; retained identity/history and report visibility. All NOT RUN. Additional multi-asset checks depend on a later cardinality decision.
