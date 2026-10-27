# Home Page_Transaction

Reference baseline; target V2 replacement is pending.

Source: `../screens/Home Page_Transaction.pa.yaml`.

Data references: none found by static formula scan.
Flow calls: none found by static formula scan.
Navigation destinations: 2_HomePage, ALM - Dispose, ALM - Movement, ALM-Registration.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Inspect the destination Studio-generated YAML shape before pasting. A full Screens: export wrapper is not assumed to be a paste-ready control snippet. Use supported screen/control copy-and-paste where compatible, or apply the supplied property formulas to the matching screen/control. Capture any rejected YAML and schema error before requesting an adapted delivery.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
| L126 /Screens/Home Page_Transaction/Children/0/ScreenContainer1_2/Children/1/MainContainer1_3/Children/0/Container2_1/Children/0/ImageContainer1_1/Children/0/Icon3_1/Properties/OnSelect | Navigate |  |  |
| L155 /Screens/Home Page_Transaction/Children/0/ScreenContainer1_2/Children/1/MainContainer1_3/Children/0/Container2_1/Children/1/TitleContainer1_1/Children/0/FeatureItemButton1_1/Properties/OnSelect | Navigate |  |  |
| L217 /Screens/Home Page_Transaction/Children/0/ScreenContainer1_2/Children/1/MainContainer1_3/Children/1/Container21_1/Children/0/ImageContainer21_1/Children/0/Icon6_1/Properties/OnSelect | Navigate |  |  |
| L247 /Screens/Home Page_Transaction/Children/0/ScreenContainer1_2/Children/1/MainContainer1_3/Children/1/Container21_1/Children/1/TitleContainer21_1/Children/0/FeatureItemButton21_1/Properties/OnSelect | Navigate |  |  |
| L308 /Screens/Home Page_Transaction/Children/0/ScreenContainer1_2/Children/1/MainContainer1_3/Children/2/Container31_1/Children/0/ImageContainer31_1/Children/0/Icon5_1/Properties/OnSelect | Navigate |  |  |
| L337 /Screens/Home Page_Transaction/Children/0/ScreenContainer1_2/Children/1/MainContainer1_3/Children/2/Container31_1/Children/1/TitleContainer31_1/Children/0/FeatureItemButton31_1/Properties/OnSelect | Navigate |  |  |
| L357 /Screens/Home Page_Transaction/Children/1/Icon15_9/Properties/OnSelect | Navigate |  |  |
