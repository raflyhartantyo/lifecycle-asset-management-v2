# Asset state fields

Status: business labels confirmed; implementation/data contract pending. No app, list or flow changed.

## Condition — confirmed D053

One dropdown with exactly these values:

- Good
- Broken
- Ready to Auction

The owner explicitly retained this single field after considering a separate auction-readiness flag. Do not add Auction Readiness or replace these labels with Needs Repair/Unusable. The field records the owner's operational classification; do not reconstruct a second physical-condition dimension when Ready to Auction is selected.

Default the registration Condition selection to Good (D054). Preserve a deliberate selection of Broken or Ready to Auction; the default does not overwrite it. Application/business requiredness and valid combinations with Asset Status will be specified in the registration contract; SharePoint mandatory-column flags remain off for editable business fields per D044.

## Other state dimensions

Asset Status describes operational lifecycle. Available, In Use and Disposed are the agreed example states under D045; final physical labels/transitions remain part of the data contract. Condition does not replace Asset Status.

Request/approval progress belongs to the workflow and its attempts. A Microsoft approval outcome, an asset's current condition and successful transaction application are separate recorded facts.

Selecting Ready to Auction does not itself complete disposal or a sale, remove the asset from active records, create a new approval process or authorize a cross-scope transaction. The retained direct disposal process still captures the applicable disposal date and sale details and preserves history. No automatic condition-to-status transition has been approved.

## Initial registration — confirmed D054

New assets register as Available only. Do not offer In Use as an initial registration choice. Apply the same initial-state validation at registration entry points; do not silently create then immediately assign an asset as part of the registration action. Later movement to In Use follows the existing authorized update/history process and custodian rules. Available assets may have no custodian; no new rule requires that field to be cleared if supplied.

Default Condition to Good and retain the existing allowed choices. Defaults must not overwrite deliberate valid choices. Entity/function derives from the authorized session; IDR is fixed; required inputs are enforced by the application, not SharePoint Required flags. Registration does not overwrite an existing asset identified by a duplicate accounting code.

## Open implementation details

Requiredness of the Condition input, condition edit authority, allowed combinations/transition guards, selection during stock-verification evidence collection versus authorized master edits, field storage names and historic snapshots. Define these without reintroducing the declined field split. Actual runtime tests remain NOT RUN.
