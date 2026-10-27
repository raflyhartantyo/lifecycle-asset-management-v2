# ALM-Dashboard

Reference baseline; target V2 replacement is pending.

Source: `../screens/ALM-Dashboard.pa.yaml`.

Data references: none found by static formula scan.
Flow calls: DataRefreshALM.
Navigation destinations: 2_HomePage.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Inspect the destination Studio-generated YAML shape before pasting. A full Screens: export wrapper is not assumed to be a paste-ready control snippet. Use supported screen/control copy-and-paste where compatible, or apply the supplied property formulas to the matching screen/control. Capture any rejected YAML and schema error before requesting an adapted delivery.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
| L96 /Screens/ALM-Dashboard/Children/1/ButtonNew_CategoryMaster_16/Properties/OnSelect |  |  | DataRefreshALM |
| L108 /Screens/ALM-Dashboard/Children/2/Icon_Home_HPMD_1/Properties/OnSelect | Navigate |  |  |
