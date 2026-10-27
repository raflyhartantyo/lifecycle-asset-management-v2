# ALM - Master Category

Reference baseline; target V2 replacement is pending.

Source: `../screens/ALM - Master Category.pa.yaml`.

Data references: Acces_Matrix, AuditLog, Master_Category, Master_Employee.
Flow calls: none found by static formula scan.
Navigation destinations: 3_HomePageMasterData, ALM-Master Category-New.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Inspect the destination Studio-generated YAML shape before pasting. A full Screens: export wrapper is not assumed to be a paste-ready control snippet. Use supported screen/control copy-and-paste where compatible, or apply the supplied property formulas to the matching screen/control. Capture any rejected YAML and schema error before requesting an adapted delivery.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
| L31 /Screens/ALM - Master Category/Children/1/ButtonNew_CategoryMaster_2/Properties/OnSelect | Navigate |  |  |
| L270 /Screens/ALM - Master Category/Children/2/AssetDataContainer_4/Children/1/ColumnValueMasterAsset_4/Children/8/NextArrow2_4/Properties/OnSelect | UpdateContext |  |  |
| L278 /Screens/ALM - Master Category/Children/2/AssetDataContainer_4/Children/1/ColumnValueMasterAsset_4/Children/8/NextArrow2_4/Properties/Visible | LookUp | Acces_Matrix, Master_Employee |  |
| L294 /Screens/ALM - Master Category/Children/3/Icon15_2/Properties/OnSelect | Navigate |  |  |
| L304 /Screens/ALM - Master Category/Children/4/ButtonNew_CategoryMaster_3/Properties/OnSelect | Refresh, ClearCollect | Master_Category |  |
| L361 /Screens/ALM - Master Category/Children/7/Container1_3/Children/0/Form1_4/Properties/DataSource |  | Master_Category |  |
| L378 /Screens/ALM - Master Category/Children/7/Container1_3/Children/0/Form1_4/Children/0/Category_ID_DataCard1/Properties/DisplayName |  | Master_Category |  |
| L379 /Screens/ALM - Master Category/Children/7/Container1_3/Children/0/Form1_4/Children/0/Category_ID_DataCard1/Properties/MaxLength |  | Master_Category |  |
| L442 /Screens/ALM - Master Category/Children/7/Container1_3/Children/0/Form1_4/Children/1/Category_Accounting_Name_DataCard1/Properties/DisplayName |  | Master_Category |  |
| L443 /Screens/ALM - Master Category/Children/7/Container1_3/Children/0/Form1_4/Children/1/Category_Accounting_Name_DataCard1/Properties/MaxLength |  | Master_Category |  |
| L519 /Screens/ALM - Master Category/Children/7/Container1_3/Children/0/Form1_4/Children/2/Category_Name_DataCard1/Properties/DisplayName |  | Master_Category |  |
| L520 /Screens/ALM - Master Category/Children/7/Container1_3/Children/0/Form1_4/Children/2/Category_Name_DataCard1/Properties/MaxLength |  | Master_Category |  |
| L596 /Screens/ALM - Master Category/Children/7/Container1_3/Children/0/Form1_4/Children/3/Category_Description_DataCard1/Properties/DisplayName |  | Master_Category |  |
| L597 /Screens/ALM - Master Category/Children/7/Container1_3/Children/0/Form1_4/Children/3/Category_Description_DataCard1/Properties/MaxLength |  | Master_Category |  |
| L675 /Screens/ALM - Master Category/Children/7/Container1_3/Children/1/ButtonClose_Registration_17/Properties/OnSelect | UpdateContext, Filter, Patch, LookUp, Notify, Refresh, ClearCollect | Master_Category, Master_Employee, AuditLog |  |
| L828 /Screens/ALM - Master Category/Children/7/Container1_3/Children/2/ButtonClose_Registration_18/Properties/OnSelect | UpdateContext |  |  |
