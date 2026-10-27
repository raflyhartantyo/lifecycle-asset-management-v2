# App

Reference baseline; target V2 replacement is pending.

Source: `../screens/App.pa.yaml`.

Data references: none found by static formula scan.
Flow calls: none found by static formula scan.
Navigation destinations: none found by static formula scan.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Apply App.StartScreen and App.Theme through their property formula bars. App.pa.yaml is an App-object reference; Code View does not support copying/pasting the App object.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
