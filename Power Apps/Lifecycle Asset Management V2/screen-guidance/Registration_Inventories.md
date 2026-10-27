# Registration_Inventories

Reference baseline; target V2 replacement is pending.

Source: `../screens/Registration_Inventories.pa.yaml`.

Data references: AuditLog, Inventories_Movement_History, Master_Asset_Type, Master_Employee, Master_Inventories, Master_Location.
Flow calls: none found by static formula scan.
Navigation destinations: Home Page_Asset_Inventory, Inventaris.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Inspect the destination Studio-generated YAML shape before pasting. A full Screens: export wrapper is not assumed to be a paste-ready control snippet. Use supported screen/control copy-and-paste where compatible, or apply the supplied property formulas to the matching screen/control. Capture any rejected YAML and schema error before requesting an adapted delivery.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
| L13 /Screens/Registration_Inventories/Properties/OnVisible | UpdateContext |  |  |
| L137 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/0/Container18/Children/0/Gallery1/Children/1/Subtitle1/Properties/Text | LookUp | Master_Location |  |
| L152 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/0/Container18/Children/0/Gallery1/Children/2/NextArrow1/Properties/OnSelect | UpdateContext |  |  |
| L194 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/0/Container18/Children/0/Gallery1/Children/5/IconDelete_Registration_1/Properties/OnSelect | UpdateContext |  |  |
| L236 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/0/Container18/Children/0/Gallery1/Children/7/Subtitle1_1/Properties/Text | LookUp | Master_Employee |  |
| L245 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/0/Container18/Children/1/ButtonSave_Registration_1/Properties/OnSelect | UpdateContext, Notify |  |  |
| L274 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/1/Container21/Children/0/Form3/Properties/DataSource |  | Master_Inventories |  |
| L290 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/1/Container21/Children/0/Form3/Children/0/Item_Name_DataCard1/Properties/DisplayName |  | Master_Inventories |  |
| L291 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/1/Container21/Children/0/Form3/Children/0/Item_Name_DataCard1/Properties/MaxLength |  | Master_Inventories |  |
| L378 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/1/Container21/Children/0/Form3/Children/1/Category_DataCard1/Properties/DisplayName |  | Master_Inventories |  |
| L379 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/1/Container21/Children/0/Form3/Children/1/Category_DataCard1/Properties/MaxLength |  | Master_Inventories |  |
| L440 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/1/Container21/Children/0/Form3/Children/1/Category_DataCard1/Children/3/Combobox1/Properties/DefaultSelectedItems | LookUp | Master_Asset_Type |  |
| L442 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/1/Container21/Children/0/Form3/Children/1/Category_DataCard1/Children/3/Combobox1/Properties/Items | Filter | Master_Asset_Type |  |
| L458 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/1/Container21/Children/0/Form3/Children/2/Quantity_DataCard1/Properties/DisplayName |  | Master_Inventories |  |
| L459 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/1/Container21/Children/0/Form3/Children/2/Quantity_DataCard1/Properties/Max |  | Master_Inventories |  |
| L460 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/1/Container21/Children/0/Form3/Children/2/Quantity_DataCard1/Properties/Min |  | Master_Inventories |  |
| L541 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/1/Container21/Children/0/Form3/Children/3/Location_DataCard1/Properties/DisplayName |  | Master_Inventories |  |
| L542 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/1/Container21/Children/0/Form3/Children/3/Location_DataCard1/Properties/MaxLength |  | Master_Inventories |  |
| L603 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/1/Container21/Children/0/Form3/Children/3/Location_DataCard1/Children/3/Combobox1_1/Properties/DefaultSelectedItems | LookUp | Master_Location |  |
| L605 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/1/Container21/Children/0/Form3/Children/3/Location_DataCard1/Children/3/Combobox1_1/Properties/Items |  | Master_Location |  |
| L617 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/1/Container21/Children/0/Form3/Children/4/Employee_MYID_DataCard1/Properties/DisplayName |  | Master_Inventories |  |
| L618 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/1/Container21/Children/0/Form3/Children/4/Employee_MYID_DataCard1/Properties/MaxLength |  | Master_Inventories |  |
| L673 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/1/Container21/Children/0/Form3/Children/4/Employee_MYID_DataCard1/Children/3/Combobox1_2/Properties/DefaultSelectedItems | LookUp | Master_Employee |  |
| L675 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/1/Container21/Children/0/Form3/Children/4/Employee_MYID_DataCard1/Children/3/Combobox1_2/Properties/Items | Filter | Master_Employee |  |
| L687 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/1/Container21/Children/0/Form3/Children/5/Remarks_DataCard5/Properties/DisplayName |  | Master_Inventories |  |
| L688 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/1/Container21/Children/0/Form3/Children/5/Remarks_DataCard5/Properties/MaxLength |  | Master_Inventories |  |
| L753 /Screens/Registration_Inventories/Children/0/Container19/Children/1/Container20/Children/1/Container21/Children/1/ButtonAddtoGallery_Registration_1/Properties/OnSelect | Collect, Patch, UpdateContext, Notify |  |  |
| L801 /Screens/Registration_Inventories/Children/1/ButtonClose_Registration_55/Properties/OnSelect | UpdateContext, Navigate |  |  |
| L842 /Screens/Registration_Inventories/Children/2/Container_Data_Confirm_9/Children/1/ButtonClose_Registration_3/Properties/OnSelect | UpdateContext |  |  |
| L857 /Screens/Registration_Inventories/Children/2/Container_Data_Confirm_9/Children/2/ButtonClose_Registration_4/Properties/OnSelect | Filter, LookUp, UpdateContext, Notify, Patch, Navigate | Inventories_Movement_History, Master_Employee, Master_Inventories, AuditLog |  |
| L1093 /Screens/Registration_Inventories/Children/2/Container_Data_Confirm_9/Children/3/AssetDataContainer_31/Children/1/ColumnValueMasterAsset_39/Children/4/Column_Value_AsssetDate_MasterAsset_308/Properties/Text | LookUp | Master_Asset_Type |  |
| L1107 /Screens/Registration_Inventories/Children/2/Container_Data_Confirm_9/Children/3/AssetDataContainer_31/Children/1/ColumnValueMasterAsset_39/Children/5/Column_Value_AsssetDate_MasterAsset_309/Properties/Text | LookUp | Master_Location |  |
| L1121 /Screens/Registration_Inventories/Children/2/Container_Data_Confirm_9/Children/3/AssetDataContainer_31/Children/1/ColumnValueMasterAsset_39/Children/6/Column_Value_AsssetDate_MasterAsset_310/Properties/Text | LookUp | Master_Employee |  |
