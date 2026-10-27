# Lifecycle Asset Management V2 — app implementation

Release `baseline-001`: supplied current implementation, packaged for reference and reconstruction. Redesigned screens/components are pending.

## Prerequisites

Read `../../Others/handover/START-HERE.md`, `../../Others/decisions/DECISIONS.md` and `../../Others/sharepoint/IMPLEMENTATION.md`. Use an identified development app and take a company-side backup/version before changing it. Obtain the missing environment bindings and existing list internal names. Original msapp, API/connection maps, media binaries and a flow solution package are absent.

## Implementation sequence

1. Inventory the company-side app, connections, flows, media, formulas and permissions against the baseline. Record mismatches instead of overwriting a newer implementation.
2. Resolve list column types/internal names and connector mappings using company-side metadata. Historical schema Markdown contains names with blank types and cannot provision SharePoint reliably on its own.
3. Recreate needed development flows using their separate folders; confirm their trigger/response contracts and bind them to the development app.
4. Use `SCREEN-INDEX.md` and each screen's guide to reconstruct baseline behavior. Create screen names/control names and dependencies before validating cross-screen formulas. App.pa.yaml has App-object properties, set via formula bars; it is not a screen or pasteable control.
5. Use Studio-generated screen/control YAML in supported Code View workflows. Supplied files contain full export structures; validate the destination's accepted shape and adapt only the wrapper required by Studio. Retain formulas and names. If rejected, return the selected node, generated YAML shape and exact error for a compatible delivery.
6. Configure missing image/media/theme assets and target Power BI report settings. A source reference alone does not include its media binary.
7. Run `VALIDATION.md`; return evidence and missing-resource details. Retain ALM - Dispose as the source reference for direct disposal. ALM-DisposeRequest is legacy evidence and excluded from the target V2 UI.

## Rollback

Restore the prior saved app version/development copy and previous flow bindings. Reverse test data changes separately using captured IDs. Keep production promotion separate from baseline review.

[Microsoft Code View documentation](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/code-view).
