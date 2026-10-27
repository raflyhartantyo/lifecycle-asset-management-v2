# ALM - Master Asset Type

Reference baseline; target V2 replacement is pending.

Source: `../screens/ALM - Master Asset Type.pa.yaml`.

Data references: Acces_Matrix, AuditLog, Master_Asset_Type, Master_Category, Master_Employee, Master_Function.
Flow calls: none found by static formula scan.
Navigation destinations: 3_HomePageMasterData, ALM-Master Asset Type-New.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Inspect the destination Studio-generated YAML shape before pasting. A full Screens: export wrapper is not assumed to be a paste-ready control snippet. Use supported screen/control copy-and-paste where compatible, or apply the supplied property formulas to the matching screen/control. Capture any rejected YAML and schema error before requesting an adapted delivery.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
| L15 /Screens/ALM - Master Asset Type/Properties/OnVisible | UpdateContext |  |  |
| L61 /Screens/ALM - Master Asset Type/Children/1/ButtonNew_CategoryMaster/Properties/OnSelect | Navigate |  |  |
| L300 /Screens/ALM - Master Asset Type/Children/2/AssetDataContainer_3/Children/1/ColumnValueMasterAsset_3/Children/8/NextArrow2_3/Properties/OnSelect | UpdateContext |  |  |
| L308 /Screens/ALM - Master Asset Type/Children/2/AssetDataContainer_3/Children/1/ColumnValueMasterAsset_3/Children/8/NextArrow2_3/Properties/Visible | LookUp | Acces_Matrix, Master_Employee |  |
| L324 /Screens/ALM - Master Asset Type/Children/3/Icon15_1/Properties/OnSelect | Navigate |  |  |
| L334 /Screens/ALM - Master Asset Type/Children/4/ButtonNew_CategoryMaster_1/Properties/OnSelect | Refresh, ClearCollect | Master_Asset_Type |  |
| L391 /Screens/ALM - Master Asset Type/Children/7/Container1_2/Children/0/Form1_2/Properties/DataSource |  | Master_Asset_Type |  |
| L408 /Screens/ALM - Master Asset Type/Children/7/Container1_2/Children/0/Form1_2/Children/0/Asset_Type_ID_DataCard2/Properties/DisplayName |  | Master_Asset_Type |  |
| L409 /Screens/ALM - Master Asset Type/Children/7/Container1_2/Children/0/Form1_2/Children/0/Asset_Type_ID_DataCard2/Properties/MaxLength |  | Master_Asset_Type |  |
| L467 /Screens/ALM - Master Asset Type/Children/7/Container1_2/Children/0/Form1_2/Children/1/Asset_Type_Name_DataCard2/Properties/DisplayName |  | Master_Asset_Type |  |
| L468 /Screens/ALM - Master Asset Type/Children/7/Container1_2/Children/0/Form1_2/Children/1/Asset_Type_Name_DataCard2/Properties/MaxLength |  | Master_Asset_Type |  |
| L544 /Screens/ALM - Master Asset Type/Children/7/Container1_2/Children/0/Form1_2/Children/2/Function_ID_DataCard2/Properties/DisplayName |  | Master_Asset_Type |  |
| L545 /Screens/ALM - Master Asset Type/Children/7/Container1_2/Children/0/Form1_2/Children/2/Function_ID_DataCard2/Properties/MaxLength |  | Master_Asset_Type |  |
| L599 /Screens/ALM - Master Asset Type/Children/7/Container1_2/Children/0/Form1_2/Children/2/Function_ID_DataCard2/Children/3/DropdownCanvas4/Properties/DefaultSelectedItems | LookUp | Master_Function |  |
| L600 /Screens/ALM - Master Asset Type/Children/7/Container1_2/Children/0/Form1_2/Children/2/Function_ID_DataCard2/Children/3/DropdownCanvas4/Properties/Items |  | Master_Function |  |
| L621 /Screens/ALM - Master Asset Type/Children/7/Container1_2/Children/0/Form1_2/Children/3/Category_ID_DataCard3/Properties/DisplayName |  | Master_Asset_Type |  |
| L622 /Screens/ALM - Master Asset Type/Children/7/Container1_2/Children/0/Form1_2/Children/3/Category_ID_DataCard3/Properties/MaxLength |  | Master_Asset_Type |  |
| L676 /Screens/ALM - Master Asset Type/Children/7/Container1_2/Children/0/Form1_2/Children/3/Category_ID_DataCard3/Children/3/DropdownCanvas4_1/Properties/DefaultSelectedItems | LookUp | Master_Category |  |
| L677 /Screens/ALM - Master Asset Type/Children/7/Container1_2/Children/0/Form1_2/Children/3/Category_ID_DataCard3/Children/3/DropdownCanvas4_1/Properties/Items |  | Master_Category |  |
| L700 /Screens/ALM - Master Asset Type/Children/7/Container1_2/Children/1/ButtonClose_Registration_15/Properties/OnSelect | UpdateContext, Filter, Patch, LookUp, Notify, Refresh, ClearCollect | Master_Employee, Master_Asset_Type, AuditLog |  |
| L839 /Screens/ALM - Master Asset Type/Children/7/Container1_2/Children/2/ButtonClose_Registration_16/Properties/OnSelect | UpdateContext |  |  |
