# 1_LandingPage

Reference baseline; target V2 replacement is pending.

Source: `../screens/1_LandingPage.pa.yaml`.

Data references: Acces_Matrix, Master_Employee.
Flow calls: none found by static formula scan.
Navigation destinations: 2_HomePage, Home Page_Asset_Inventory, Inventaris.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Inspect the destination Studio-generated YAML shape before pasting. A full Screens: export wrapper is not assumed to be a paste-ready control snippet. Use supported screen/control copy-and-paste where compatible, or apply the supplied property formulas to the matching screen/control. Capture any rejected YAML and schema error before requesting an adapted delivery.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
| L67 /Screens/1_LandingPage/Children/1/Ctr_LP/Children/2/Btn_Start_LP/Properties/DisplayMode | LookUp | Acces_Matrix, Master_Employee |  |
| L71 /Screens/1_LandingPage/Children/1/Ctr_LP/Children/2/Btn_Start_LP/Properties/OnSelect | LookUp, UpdateContext, Navigate, Notify | Acces_Matrix, Master_Employee |  |
