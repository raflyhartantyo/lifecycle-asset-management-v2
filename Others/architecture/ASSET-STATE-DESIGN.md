# Asset state fields

Status: business labels confirmed; implementation/data contract pending. No app, list or flow changed.

## Condition — confirmed D053

One dropdown with exactly these values:

- Good
- Broken
- Ready to Auction

The owner explicitly retained this single field after considering a separate auction-readiness flag. Do not add Auction Readiness or replace these labels with Needs Repair/Unusable. The field records the owner's operational classification; do not reconstruct a second physical-condition dimension when Ready to Auction is selected.

The default selection is not yet agreed. Do not assume all new registrations are Good. Application/business requiredness and valid combinations with Asset Status will be specified in the registration contract; SharePoint mandatory-column flags remain off for editable business fields per D044.

## Other state dimensions

Asset Status describes operational lifecycle. Available, In Use and Disposed are the agreed example states under D045; final physical labels/transitions remain part of the data contract. Condition does not replace Asset Status.

Request/approval progress belongs to the workflow and its attempts. A Microsoft approval outcome, an asset's current condition and successful transaction application are separate recorded facts.

Selecting Ready to Auction does not itself complete disposal or a sale, remove the asset from active records, create a new approval process or authorize a cross-scope transaction. The retained direct disposal process still captures the applicable disposal date and sale details and preserves history. No automatic condition-to-status transition has been approved.

## Open implementation details

Default condition, requiredness of the Condition input, condition edit authority, allowed combinations/transition guards, selection during stock-verification evidence collection versus authorized master edits, field storage names and historic snapshots. Define these without reintroducing the declined field split. Actual runtime tests remain NOT RUN.
