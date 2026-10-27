# ALM - Master Function

Reference baseline; target V2 replacement is pending.

Source: `../screens/ALM - Master Function.pa.yaml`.

Data references: Acces_Matrix, AuditLog, Master_Employee, Master_Function, Master_Organization.
Flow calls: none found by static formula scan.
Navigation destinations: 3_HomePageMasterData, ALM-Master Function-New.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Inspect the destination Studio-generated YAML shape before pasting. A full Screens: export wrapper is not assumed to be a paste-ready control snippet. Use supported screen/control copy-and-paste where compatible, or apply the supplied property formulas to the matching screen/control. Capture any rejected YAML and schema error before requesting an adapted delivery.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
| L31 /Screens/ALM - Master Function/Children/1/ButtonNew_CategoryMaster_8/Properties/OnSelect | Navigate |  |  |
| L241 /Screens/ALM - Master Function/Children/2/AssetDataContainer_7/Children/1/ColumnValueMasterAsset_7/Children/7/NextArrow2_6/Properties/OnSelect | UpdateContext |  |  |
| L249 /Screens/ALM - Master Function/Children/2/AssetDataContainer_7/Children/1/ColumnValueMasterAsset_7/Children/7/NextArrow2_6/Properties/Visible | LookUp | Acces_Matrix, Master_Employee |  |
| L265 /Screens/ALM - Master Function/Children/3/Icon15_5/Properties/OnSelect | Navigate |  |  |
| L275 /Screens/ALM - Master Function/Children/4/ButtonNew_CategoryMaster_9/Properties/OnSelect | Refresh, ClearCollect | Master_Function |  |
| L332 /Screens/ALM - Master Function/Children/7/Container1_6/Children/0/Form1_7/Properties/DataSource |  | Master_Function |  |
| L349 /Screens/ALM - Master Function/Children/7/Container1_6/Children/0/Form1_7/Children/0/Function_ID_DataCard3/Properties/DisplayName |  | Master_Function |  |
| L350 /Screens/ALM - Master Function/Children/7/Container1_6/Children/0/Form1_7/Children/0/Function_ID_DataCard3/Properties/MaxLength |  | Master_Function |  |
| L408 /Screens/ALM - Master Function/Children/7/Container1_6/Children/0/Form1_7/Children/1/Function_Name_DataCard1/Properties/DisplayName |  | Master_Function |  |
| L409 /Screens/ALM - Master Function/Children/7/Container1_6/Children/0/Form1_7/Children/1/Function_Name_DataCard1/Properties/MaxLength |  | Master_Function |  |
| L489 /Screens/ALM - Master Function/Children/7/Container1_6/Children/0/Form1_7/Children/2/Organization_ID_DataCard1/Properties/DisplayName |  | Master_Function |  |
| L490 /Screens/ALM - Master Function/Children/7/Container1_6/Children/0/Form1_7/Children/2/Organization_ID_DataCard1/Properties/MaxLength |  | Master_Function |  |
| L544 /Screens/ALM - Master Function/Children/7/Container1_6/Children/0/Form1_7/Children/2/Organization_ID_DataCard1/Children/3/DropdownCanvas6/Properties/DefaultSelectedItems | LookUp | Master_Organization |  |
| L545 /Screens/ALM - Master Function/Children/7/Container1_6/Children/0/Form1_7/Children/2/Organization_ID_DataCard1/Children/3/DropdownCanvas6/Properties/Items |  | Master_Organization |  |
| L568 /Screens/ALM - Master Function/Children/7/Container1_6/Children/1/ButtonClose_Registration_23/Properties/OnSelect | UpdateContext, Filter, Patch, LookUp, Notify, Refresh, ClearCollect | Master_Function, Master_Employee, AuditLog |  |
| L711 /Screens/ALM - Master Function/Children/7/Container1_6/Children/2/ButtonClose_Registration_24/Properties/OnSelect | UpdateContext |  |  |
