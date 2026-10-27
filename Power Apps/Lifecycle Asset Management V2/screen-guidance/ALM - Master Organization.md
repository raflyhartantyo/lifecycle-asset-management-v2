# ALM - Master Organization

Reference baseline; target V2 replacement is pending.

Source: `../screens/ALM - Master Organization.pa.yaml`.

Data references: Acces_Matrix, AuditLog, Master_Employee, Master_Organization.
Flow calls: none found by static formula scan.
Navigation destinations: 3_HomePageMasterData, ALM-Master Organization-New.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Inspect the destination Studio-generated YAML shape before pasting. A full Screens: export wrapper is not assumed to be a paste-ready control snippet. Use supported screen/control copy-and-paste where compatible, or apply the supplied property formulas to the matching screen/control. Capture any rejected YAML and schema error before requesting an adapted delivery.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
| L31 /Screens/ALM - Master Organization/Children/1/ButtonNew_CategoryMaster_10/Properties/OnSelect | Navigate |  |  |
| L212 /Screens/ALM - Master Organization/Children/2/AssetDataContainer_8/Children/1/ColumnValueMasterAsset_8/Children/6/NextArrow2_7/Properties/OnSelect | UpdateContext |  |  |
| L220 /Screens/ALM - Master Organization/Children/2/AssetDataContainer_8/Children/1/ColumnValueMasterAsset_8/Children/6/NextArrow2_7/Properties/Visible | LookUp | Acces_Matrix, Master_Employee |  |
| L236 /Screens/ALM - Master Organization/Children/3/Icon15_6/Properties/OnSelect | Navigate |  |  |
| L246 /Screens/ALM - Master Organization/Children/4/ButtonNew_CategoryMaster_11/Properties/OnSelect | Refresh, ClearCollect | Master_Organization |  |
| L303 /Screens/ALM - Master Organization/Children/7/Container1_7/Children/0/Form1_8/Properties/DataSource |  | Master_Organization |  |
| L320 /Screens/ALM - Master Organization/Children/7/Container1_7/Children/0/Form1_8/Children/0/Organization_ID_DataCard3/Properties/DisplayName |  | Master_Organization |  |
| L321 /Screens/ALM - Master Organization/Children/7/Container1_7/Children/0/Form1_8/Children/0/Organization_ID_DataCard3/Properties/MaxLength |  | Master_Organization |  |
| L379 /Screens/ALM - Master Organization/Children/7/Container1_7/Children/0/Form1_8/Children/1/Organization_Name_DataCard1/Properties/DisplayName |  | Master_Organization |  |
| L380 /Screens/ALM - Master Organization/Children/7/Container1_7/Children/0/Form1_8/Children/1/Organization_Name_DataCard1/Properties/MaxLength |  | Master_Organization |  |
| L461 /Screens/ALM - Master Organization/Children/7/Container1_7/Children/1/ButtonClose_Registration_25/Properties/OnSelect | UpdateContext, Filter, Patch, LookUp, Notify, Refresh, ClearCollect | Master_Organization, Master_Employee, AuditLog |  |
| L594 /Screens/ALM - Master Organization/Children/7/Container1_7/Children/2/ButtonClose_Registration_26/Properties/OnSelect | UpdateContext |  |  |
