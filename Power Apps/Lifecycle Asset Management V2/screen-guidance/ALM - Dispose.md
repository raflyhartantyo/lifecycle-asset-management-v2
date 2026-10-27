# ALM - Dispose

Reference baseline; target V2 replacement is pending.

Source: `../screens/ALM - Dispose.pa.yaml`.

Data references: Asset_Movement_History, AuditLog, Master_Asset, Master_Asset_Type, Master_Category, Master_Employee, Master_Function, Master_Location, Master_Organization.
Flow calls: none found by static formula scan.
Navigation destinations: Home Page_Transaction.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Inspect the destination Studio-generated YAML shape before pasting. A full Screens: export wrapper is not assumed to be a paste-ready control snippet. Use supported screen/control copy-and-paste where compatible, or apply the supplied property formulas to the matching screen/control. Capture any rejected YAML and schema error before requesting an adapted delivery.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
| L14 /Screens/ALM - Dispose/Properties/OnHidden | UpdateContext |  |  |
| L19 /Screens/ALM - Dispose/Properties/OnVisible | UpdateContext |  |  |
| L47 /Screens/ALM - Dispose/Children/0/HeaderContainer_AssetMaster_4/Children/1/ButtonNew_CategoryMaster_14/Properties/OnSelect | Refresh, ClearCollect, Filter, UpdateContext | Master_Asset |  |
| L80 /Screens/ALM - Dispose/Children/0/HeaderContainer_AssetMaster_4/Children/2/Icon15_10/Properties/OnSelect | Navigate |  |  |
| L96 /Screens/ALM - Dispose/Children/0/HeaderContainer_AssetMaster_4/Children/3/ButtonClose_Registration_30/Properties/OnSelect | UpdateContext |  |  |
| L208 /Screens/ALM - Dispose/Children/2/Container5/Children/1/BottomContainer_Registration_2/Children/0/SidebarContainer_Registration_2/Children/0/DataGallery_Registration_2/Properties/OnSelect | UpdateContext |  |  |
| L239 /Screens/ALM - Dispose/Children/2/Container5/Children/1/BottomContainer_Registration_2/Children/0/SidebarContainer_Registration_2/Children/0/DataGallery_Registration_2/Children/1/TextCategory_Registration_2/Properties/Text | LookUp | Master_Asset_Type |  |
| L287 /Screens/ALM - Dispose/Children/2/Container5/Children/1/BottomContainer_Registration_2/Children/0/SidebarContainer_Registration_2/Children/0/DataGallery_Registration_2/Children/4/IconDelete_Registration_2/Properties/OnSelect | UpdateContext |  |  |
| L354 /Screens/ALM - Dispose/Children/2/Container5/Children/1/BottomContainer_Registration_2/Children/0/SidebarContainer_Registration_2/Children/1/ButtonSave_Registration_2/Properties/OnSelect | Set, Notify, UpdateContext |  |  |
| L465 /Screens/ALM - Dispose/Children/2/Container5/Children/1/BottomContainer_Registration_2/Children/1/FormContainer_Registration_2/Children/0/Form_Registration_2/Children/0/Organization_ID_DataCard6/Children/3/DropdownCanvas17/Properties/DefaultSelectedItems | LookUp | Master_Organization |  |
| L467 /Screens/ALM - Dispose/Children/2/Container5/Children/1/BottomContainer_Registration_2/Children/1/FormContainer_Registration_2/Children/0/Form_Registration_2/Children/0/Organization_ID_DataCard6/Children/3/DropdownCanvas17/Properties/Items |  | Master_Organization |  |
| L530 /Screens/ALM - Dispose/Children/2/Container5/Children/1/BottomContainer_Registration_2/Children/1/FormContainer_Registration_2/Children/0/Form_Registration_2/Children/1/Function_ID_DataCard6/Children/3/DropdownCanvas18/Properties/DefaultSelectedItems | LookUp | Master_Function |  |
| L532 /Screens/ALM - Dispose/Children/2/Container5/Children/1/BottomContainer_Registration_2/Children/1/FormContainer_Registration_2/Children/0/Form_Registration_2/Children/1/Function_ID_DataCard6/Children/3/DropdownCanvas18/Properties/Items |  | Master_Function |  |
| L833 /Screens/ALM - Dispose/Children/2/Container5/Children/1/BottomContainer_Registration_2/Children/1/FormContainer_Registration_2/Children/0/Form_Registration_2/Children/6/Asset_Type_ID_DataCard1/Children/3/DropdownCanvas19/Properties/DefaultSelectedItems | LookUp | Master_Asset_Type |  |
| L835 /Screens/ALM - Dispose/Children/2/Container5/Children/1/BottomContainer_Registration_2/Children/1/FormContainer_Registration_2/Children/0/Form_Registration_2/Children/6/Asset_Type_ID_DataCard1/Children/3/DropdownCanvas19/Properties/Items |  | Master_Asset_Type |  |
| L1107 /Screens/ALM - Dispose/Children/2/Container5/Children/1/BottomContainer_Registration_2/Children/1/FormContainer_Registration_2/Children/1/ButtonAddtoGallery_Registration_2/Properties/OnSelect | Patch, Notify, UpdateContext |  |  |
| L1141 /Screens/ALM - Dispose/Children/3/ButtonClose_CategoryMaster_New_5/Properties/OnSelect | UpdateContext |  |  |
| L1183 /Screens/ALM - Dispose/Children/4/ConfirmationContainer_CategoryMaster_New_5/Children/1/ButtonConfirmationNo_CategoryMaster_New_5/Properties/OnSelect | UpdateContext |  |  |
| L1193 /Screens/ALM - Dispose/Children/4/ConfirmationContainer_CategoryMaster_New_5/Children/2/ButtonConfirmationYes_CategoryMaster_New_5/Properties/OnSelect | Remove, UpdateContext |  |  |
| L1238 /Screens/ALM - Dispose/Children/5/Container_Data_Confirm_2/Children/1/ButtonClose_Registration_31/Properties/OnSelect | UpdateContext |  |  |
| L1253 /Screens/ALM - Dispose/Children/5/Container_Data_Confirm_2/Children/2/ButtonClose_Registration_34/Properties/OnSelect | LookUp, Patch, Remove, UpdateContext, Notify, Navigate | Asset_Movement_History, Master_Asset, Master_Employee, AuditLog |  |
| L1676 /Screens/ALM - Dispose/Children/5/Container_Data_Confirm_2/Children/3/AssetDataContainer_12/Children/1/ColumnValueMasterAsset_12/Children/1/Column_Value_AsssetDate_MasterAsset_139/Properties/Text | LookUp | Master_Organization |  |
| L1718 /Screens/ALM - Dispose/Children/5/Container_Data_Confirm_2/Children/3/AssetDataContainer_12/Children/1/ColumnValueMasterAsset_12/Children/4/Column_Value_AsssetDate_MasterAsset_142/Properties/Text | LookUp | Master_Asset_Type |  |
| L1760 /Screens/ALM - Dispose/Children/5/Container_Data_Confirm_2/Children/3/AssetDataContainer_12/Children/1/ColumnValueMasterAsset_12/Children/7/Column_Value_AsssetDate_MasterAsset_145/Properties/Text | LookUp | Master_Function |  |
| L2273 /Screens/ALM - Dispose/Children/7/AssetDataContainer_11/Children/1/ColumnValueMasterAsset_11/Properties/Items | IfError, Filter |  |  |
| L2357 /Screens/ALM - Dispose/Children/7/AssetDataContainer_11/Children/1/ColumnValueMasterAsset_11/Properties/TemplateFill | LookUp |  |  |
| L2414 /Screens/ALM - Dispose/Children/7/AssetDataContainer_11/Children/1/ColumnValueMasterAsset_11/Children/1/Column_Value_AsssetDate_MasterAsset_117/Properties/Text | LookUp | Master_Organization |  |
| L2456 /Screens/ALM - Dispose/Children/7/AssetDataContainer_11/Children/1/ColumnValueMasterAsset_11/Children/4/Column_Value_AsssetDate_MasterAsset_121/Properties/Text | LookUp | Master_Employee |  |
| L2471 /Screens/ALM - Dispose/Children/7/AssetDataContainer_11/Children/1/ColumnValueMasterAsset_11/Children/5/NextArrow2_9/Properties/Icon | LookUp |  |  |
| L2477 /Screens/ALM - Dispose/Children/7/AssetDataContainer_11/Children/1/ColumnValueMasterAsset_11/Children/5/NextArrow2_9/Properties/OnSelect | LookUp, Collect, RemoveIf |  |  |
| L2521 /Screens/ALM - Dispose/Children/7/AssetDataContainer_11/Children/1/ColumnValueMasterAsset_11/Children/6/Column_Value_AsssetDate_MasterAsset_122/Properties/Text | LookUp | Master_Employee |  |
| L2563 /Screens/ALM - Dispose/Children/7/AssetDataContainer_11/Children/1/ColumnValueMasterAsset_11/Children/9/Column_Value_AsssetDate_MasterAsset_125/Properties/Text | LookUp | Master_Location |  |
| L2577 /Screens/ALM - Dispose/Children/7/AssetDataContainer_11/Children/1/ColumnValueMasterAsset_11/Children/10/Column_Value_AsssetDate_MasterAsset_126/Properties/Text | LookUp | Master_Asset_Type |  |
| L2591 /Screens/ALM - Dispose/Children/7/AssetDataContainer_11/Children/1/ColumnValueMasterAsset_11/Children/11/Column_Value_AsssetDate_MasterAsset_127/Properties/Text | LookUp | Master_Category |  |
| L2703 /Screens/ALM - Dispose/Children/7/AssetDataContainer_11/Children/1/ColumnValueMasterAsset_11/Children/19/Column_Value_AsssetDate_MasterAsset_135/Properties/Text | LookUp | Master_Function |  |
| L2823 /Screens/ALM - Dispose/Children/9/Container3_2/Children/0/Form2_2/Properties/DataSource |  | Master_Asset |  |
| L2889 /Screens/ALM - Dispose/Children/9/Container3_2/Children/0/Form2_2/Children/0/Organization_ID_DataCard4/Children/3/DropdownCanvas12/Properties/Items |  | Master_Organization |  |
| L2962 /Screens/ALM - Dispose/Children/9/Container3_2/Children/0/Form2_2/Children/1/Function_ID_DataCard4/Children/3/DropdownCanvas16/Properties/Items | Filter | Master_Function |  |
| L3268 /Screens/ALM - Dispose/Children/9/Container3_2/Children/1/ButtonClose_Registration_32/Properties/OnSelect | Navigate |  |  |
| L3284 /Screens/ALM - Dispose/Children/9/Container3_2/Children/2/ButtonClose_Registration_33/Properties/OnSelect | ClearCollect, UpdateContext |  |  |
