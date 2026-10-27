# Home Page_Stock_Opname

Reference baseline; target V2 replacement is pending.

Source: `../screens/Home Page_Stock_Opname.pa.yaml`.

Data references: Acces_Matrix, Master_Employee.
Flow calls: none found by static formula scan.
Navigation destinations: 2_HomePage, ALM - StockOpname - Available, ALM - StockOpname - In Use.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Inspect the destination Studio-generated YAML shape before pasting. A full Screens: export wrapper is not assumed to be a paste-ready control snippet. Use supported screen/control copy-and-paste where compatible, or apply the supplied property formulas to the matching screen/control. Capture any rejected YAML and schema error before requesting an adapted delivery.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
| L94 /Screens/Home Page_Stock_Opname/Children/0/ScreenContainer1_3/Children/1/MainContainer1_4/Children/0/Container2_2/Properties/Visible | LookUp | Acces_Matrix, Master_Employee |  |
| L127 /Screens/Home Page_Stock_Opname/Children/0/ScreenContainer1_3/Children/1/MainContainer1_4/Children/0/Container2_2/Children/0/ImageContainer1_2/Children/0/Icon3_2/Properties/OnSelect | Navigate |  |  |
| L156 /Screens/Home Page_Stock_Opname/Children/0/ScreenContainer1_3/Children/1/MainContainer1_4/Children/0/Container2_2/Children/1/TitleContainer1_2/Children/0/FeatureItemButton1_2/Properties/OnSelect | Navigate |  |  |
| L185 /Screens/Home Page_Stock_Opname/Children/0/ScreenContainer1_3/Children/1/MainContainer1_4/Children/1/Container31_2/Properties/Visible | LookUp | Acces_Matrix, Master_Employee |  |
| L235 /Screens/Home Page_Stock_Opname/Children/0/ScreenContainer1_3/Children/1/MainContainer1_4/Children/1/Container31_2/Children/0/ImageContainer31_2/Children/0/Icon5_2/Properties/OnSelect | Navigate |  |  |
| L264 /Screens/Home Page_Stock_Opname/Children/0/ScreenContainer1_3/Children/1/MainContainer1_4/Children/1/Container31_2/Children/1/TitleContainer31_2/Children/0/FeatureItemButton31_2/Properties/OnSelect | Navigate |  |  |
| L284 /Screens/Home Page_Stock_Opname/Children/1/Icon15_11/Properties/OnSelect | Navigate |  |  |
