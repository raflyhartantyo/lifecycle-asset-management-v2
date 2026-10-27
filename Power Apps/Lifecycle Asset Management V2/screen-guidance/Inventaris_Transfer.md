# Inventaris_Transfer

Reference baseline; target V2 replacement is pending.

Source: `../screens/Inventaris_Transfer.pa.yaml`.

Data references: Inventories_Movement_History, Master_Asset_Type, Master_Employee, Master_Inventories, Master_Location.
Flow calls: none found by static formula scan.
Navigation destinations: Inventaris.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Inspect the destination Studio-generated YAML shape before pasting. A full Screens: export wrapper is not assumed to be a paste-ready control snippet. Use supported screen/control copy-and-paste where compatible, or apply the supplied property formulas to the matching screen/control. Capture any rejected YAML and schema error before requesting an adapted delivery.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
| L181 /Screens/Inventaris_Transfer/Children/0/Container16_1/Children/1/AssetDataContainer_32/Children/1/ColumnValueMasterAsset_40/Properties/Items |  | Master_Inventories |  |
| L233 /Screens/Inventaris_Transfer/Children/0/Container16_1/Children/1/AssetDataContainer_32/Children/1/ColumnValueMasterAsset_40/Children/1/Column_Value_AsssetDate_MasterAsset_315/Properties/Text | LookUp | Master_Asset_Type |  |
| L254 /Screens/Inventaris_Transfer/Children/0/Container16_1/Children/1/AssetDataContainer_32/Children/1/ColumnValueMasterAsset_40/Children/2/Column_Value_AsssetDate_MasterAsset_316/Properties/Text | LookUp | Master_Location |  |
| L289 /Screens/Inventaris_Transfer/Children/0/Container16_1/Children/1/AssetDataContainer_32/Children/1/ColumnValueMasterAsset_40/Children/4/Column_Value_AsssetDate_MasterAsset_318/Properties/Text | LookUp | Master_Employee |  |
| L362 /Screens/Inventaris_Transfer/Children/0/Container16_1/Children/1/AssetDataContainer_32/Children/1/ColumnValueMasterAsset_40/Children/10/NextArrow2_20/Properties/OnSelect | UpdateContext, LookUp, ClearCollect | Master_Inventories |  |
| L390 /Screens/Inventaris_Transfer/Children/1/Icon15_16/Properties/OnSelect | Navigate |  |  |
| L410 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/0/Form1_10/Properties/DataSource |  | Master_Inventories |  |
| L427 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/0/Form1_10/Children/0/Title_DataCard1/Properties/DisplayName |  | Master_Inventories |  |
| L428 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/0/Form1_10/Children/0/Title_DataCard1/Properties/MaxLength |  | Master_Inventories |  |
| L487 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/0/Form1_10/Children/1/Item_Name_DataCard2/Properties/DisplayName |  | Master_Inventories |  |
| L488 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/0/Form1_10/Children/1/Item_Name_DataCard2/Properties/MaxLength |  | Master_Inventories |  |
| L545 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/0/Form1_10/Children/2/Category_DataCard2/Properties/Default | LookUp | Master_Asset_Type |  |
| L546 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/0/Form1_10/Children/2/Category_DataCard2/Properties/DisplayName |  | Master_Inventories |  |
| L547 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/0/Form1_10/Children/2/Category_DataCard2/Properties/MaxLength |  | Master_Inventories |  |
| L606 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/0/Form1_10/Children/3/Employee_MYID_DataCard2/Properties/DisplayName |  | Master_Inventories |  |
| L607 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/0/Form1_10/Children/3/Employee_MYID_DataCard2/Properties/MaxLength |  | Master_Inventories |  |
| L665 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/0/Form1_10/Children/4/Location_DataCard2/Properties/DisplayName |  | Master_Inventories |  |
| L666 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/0/Form1_10/Children/4/Location_DataCard2/Properties/MaxLength |  | Master_Inventories |  |
| L720 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/0/Form1_10/Children/4/Location_DataCard2/Children/4/Combobox5/Properties/DefaultSelectedItems | LookUp | Master_Location |  |
| L722 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/0/Form1_10/Children/4/Location_DataCard2/Children/4/Combobox5/Properties/Items |  | Master_Location |  |
| L735 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/0/Form1_10/Children/5/Remarks_DataCard6/Properties/DisplayName |  | Master_Inventories |  |
| L736 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/0/Form1_10/Children/5/Remarks_DataCard6/Properties/MaxLength |  | Master_Inventories |  |
| L796 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/0/Form1_10/Children/6/Quantity_DataCard2/Properties/DisplayName |  | Master_Inventories |  |
| L854 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/0/Form1_10/Children/7/Parent_ID_DataCard1/Properties/DisplayName |  | Master_Inventories |  |
| L855 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/0/Form1_10/Children/7/Parent_ID_DataCard1/Properties/MaxLength |  | Master_Inventories |  |
| L915 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/1/ButtonClose_Registration_59/Properties/OnSelect | UpdateContext, SubmitForm, Filter, Patch, Refresh, Notify | Inventories_Movement_History, Master_Inventories |  |
| L930 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/2/ButtonClose_Registration_60/Properties/OnSelect | UpdateContext |  |  |
| L947 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/3/ButtonClose_Registration_62/Properties/OnSelect | UpdateContext, Patch, LookUp, RemoveIf, Refresh, Notify | Inventories_Movement_History, Master_Inventories |  |
| L1010 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/4/Container25/Children/0/Container24/Children/1/Button4/Properties/OnSelect | Collect |  |  |
| L1170 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/4/Container25/Children/1/AssetDataContainer_33/Children/1/ColumnValueMasterAsset_41/Children/2/Combobox4/Properties/DefaultSelectedItems | LookUp | Master_Employee |  |
| L1180 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/4/Container25/Children/1/AssetDataContainer_33/Children/1/ColumnValueMasterAsset_41/Children/2/Combobox4/Properties/Items | Filter | Master_Employee |  |
| L1181 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/4/Container25/Children/1/AssetDataContainer_33/Children/1/ColumnValueMasterAsset_41/Children/2/Combobox4/Properties/OnChange | Patch, LookUp |  |  |
| L1212 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/4/Container25/Children/1/AssetDataContainer_33/Children/1/ColumnValueMasterAsset_41/Children/3/NumberInput1/Properties/OnChange | Patch, LookUp |  |  |
| L1231 /Screens/Inventaris_Transfer/Children/2/Container1_9/Children/4/Container25/Children/1/AssetDataContainer_33/Children/1/ColumnValueMasterAsset_41/Children/4/Button5/Properties/OnSelect | Remove |  |  |
