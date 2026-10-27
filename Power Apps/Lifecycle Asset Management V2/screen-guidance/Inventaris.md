# Inventaris

Reference baseline; target V2 replacement is pending.

Source: `../screens/Inventaris.pa.yaml`.

Data references: Acces_Matrix, Master_Asset_Type, Master_Employee, Master_Inventories, Master_Location.
Flow calls: none found by static formula scan.
Navigation destinations: Home Page_Asset_Inventory, Inventaris_Transfer, Registration_Inventories.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Inspect the destination Studio-generated YAML shape before pasting. A full Screens: export wrapper is not assumed to be a paste-ready control snippet. Use supported screen/control copy-and-paste where compatible, or apply the supplied property formulas to the matching screen/control. Capture any rejected YAML and schema error before requesting an adapted delivery.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
| L87 /Screens/Inventaris/Children/0/Container16/Children/1/Container17/Children/0/Ctr_HP_9/Properties/Visible | LookUp | Acces_Matrix, Master_Employee |  |
| L125 /Screens/Inventaris/Children/0/Container16/Children/1/Container17/Children/0/Ctr_HP_9/Children/0/ImgCtr_HP3_1/Children/0/Icon_MasterData_HP3_1/Properties/OnSelect | Navigate |  |  |
| L154 /Screens/Inventaris/Children/0/Container16/Children/1/Container17/Children/0/Ctr_HP_9/Children/1/TtlCtr_HP3_1/Children/0/Txt_TitleMasterData_HP3_1/Properties/OnSelect | Navigate |  |  |
| L183 /Screens/Inventaris/Children/0/Container16/Children/1/Container17/Children/1/Ctr_HP_10/Properties/Visible | LookUp | Acces_Matrix, Master_Employee |  |
| L221 /Screens/Inventaris/Children/0/Container16/Children/1/Container17/Children/1/Ctr_HP_10/Children/0/ImgCtr_HP3_2/Children/0/Icon_MasterData_HP3_2/Properties/OnSelect | Navigate |  |  |
| L251 /Screens/Inventaris/Children/0/Container16/Children/1/Container17/Children/1/Ctr_HP_10/Children/1/TtlCtr_HP3_2/Children/0/Txt_TitleMasterData_HP3_2/Properties/OnSelect | Navigate |  |  |
| L389 /Screens/Inventaris/Children/0/Container16/Children/2/AssetDataContainer_24/Children/1/ColumnValueMasterAsset_24/Properties/Items |  | Master_Inventories |  |
| L441 /Screens/Inventaris/Children/0/Container16/Children/2/AssetDataContainer_24/Children/1/ColumnValueMasterAsset_24/Children/1/Column_Value_AsssetDate_MasterAsset_236/Properties/Text | LookUp | Master_Asset_Type |  |
| L455 /Screens/Inventaris/Children/0/Container16/Children/2/AssetDataContainer_24/Children/1/ColumnValueMasterAsset_24/Children/2/Column_Value_AsssetDate_MasterAsset_239/Properties/Text | LookUp | Master_Employee |  |
| L476 /Screens/Inventaris/Children/0/Container16/Children/2/AssetDataContainer_24/Children/1/ColumnValueMasterAsset_24/Children/3/Column_Value_AsssetDate_MasterAsset_240/Properties/Text | LookUp | Master_Location |  |
| L566 /Screens/Inventaris/Children/1/Icon15_15/Properties/OnSelect | Navigate |  |  |
| L567 /Screens/Inventaris/Children/1/Icon15_15/Properties/Visible | LookUp | Acces_Matrix, Master_Employee |  |
