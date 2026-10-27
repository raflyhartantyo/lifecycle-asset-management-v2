# ALM - Movement

Reference baseline; target V2 replacement is pending.

Source: `../screens/ALM - Movement.pa.yaml`.

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
| L14 /Screens/ALM - Movement/Properties/OnHidden | UpdateContext |  |  |
| L17 /Screens/ALM - Movement/Properties/OnVisible | UpdateContext |  |  |
| L44 /Screens/ALM - Movement/Children/0/HeaderContainer_AssetMaster_3/Children/1/ButtonNew_CategoryMaster_13/Properties/OnSelect | ClearCollect, Filter, LookUp, UpdateContext, Collect | Master_Category, Master_Location, Master_Asset, Master_Employee, Master_Asset_Type |  |
| L158 /Screens/ALM - Movement/Children/0/HeaderContainer_AssetMaster_3/Children/2/Icon15_8/Properties/OnSelect | Navigate |  |  |
| L533 /Screens/ALM - Movement/Children/1/AssetDataContainer_9/Children/0/ColumnNameMasterAsset_9/Children/22/Toggle1/Properties/OnCheck | UpdateContext |  |  |
| L536 /Screens/ALM - Movement/Children/1/AssetDataContainer_9/Children/0/ColumnNameMasterAsset_9/Children/22/Toggle1/Properties/OnUncheck | UpdateContext |  |  |
| L564 /Screens/ALM - Movement/Children/1/AssetDataContainer_9/Children/1/ColumnValueMasterAsset_9/Properties/Items | Filter |  |  |
| L643 /Screens/ALM - Movement/Children/1/AssetDataContainer_9/Children/1/ColumnValueMasterAsset_9/Properties/TemplateFill | LookUp |  |  |
| L673 /Screens/ALM - Movement/Children/1/AssetDataContainer_9/Children/1/ColumnValueMasterAsset_9/Children/0/NextArrow2_8/Properties/Icon | LookUp |  |  |
| L679 /Screens/ALM - Movement/Children/1/AssetDataContainer_9/Children/1/ColumnValueMasterAsset_9/Children/0/NextArrow2_8/Properties/OnSelect | LookUp, Collect, RemoveIf |  |  |
| L745 /Screens/ALM - Movement/Children/1/AssetDataContainer_9/Children/1/ColumnValueMasterAsset_9/Children/2/Column_Value_AsssetDate_MasterAsset_79/Properties/Text | LookUp | Master_Organization |  |
| L787 /Screens/ALM - Movement/Children/1/AssetDataContainer_9/Children/1/ColumnValueMasterAsset_9/Children/5/Column_Value_AsssetDate_MasterAsset_82/Properties/Text | LookUp | Master_Employee |  |
| L801 /Screens/ALM - Movement/Children/1/AssetDataContainer_9/Children/1/ColumnValueMasterAsset_9/Children/6/Column_Value_AsssetDate_MasterAsset_83/Properties/Text | LookUp | Master_Employee |  |
| L843 /Screens/ALM - Movement/Children/1/AssetDataContainer_9/Children/1/ColumnValueMasterAsset_9/Children/9/Column_Value_AsssetDate_MasterAsset_86/Properties/Text | LookUp | Master_Location |  |
| L857 /Screens/ALM - Movement/Children/1/AssetDataContainer_9/Children/1/ColumnValueMasterAsset_9/Children/10/Column_Value_AsssetDate_MasterAsset_87/Properties/Text | LookUp | Master_Asset_Type |  |
| L871 /Screens/ALM - Movement/Children/1/AssetDataContainer_9/Children/1/ColumnValueMasterAsset_9/Children/11/Column_Value_AsssetDate_MasterAsset_88/Properties/Text | LookUp | Master_Category |  |
| L983 /Screens/ALM - Movement/Children/1/AssetDataContainer_9/Children/1/ColumnValueMasterAsset_9/Children/19/Column_Value_AsssetDate_MasterAsset_96/Properties/Text | LookUp | Master_Function |  |
| L1087 /Screens/ALM - Movement/Children/1/AssetDataContainer_9/Children/1/ColumnValueMasterAsset_9/Children/27/NextArrow2_16/Properties/OnSelect | UpdateContext, LookUp | Master_Asset |  |
| L1102 /Screens/ALM - Movement/Children/1/AssetDataContainer_9/Children/1/ColumnValueMasterAsset_9/Children/28/CheckboxCanvas1/Properties/Checked | Filter |  |  |
| L1111 /Screens/ALM - Movement/Children/1/AssetDataContainer_9/Children/1/ColumnValueMasterAsset_9/Children/28/CheckboxCanvas1/Properties/OnCheck | Collect |  |  |
| L1117 /Screens/ALM - Movement/Children/1/AssetDataContainer_9/Children/1/ColumnValueMasterAsset_9/Children/28/CheckboxCanvas1/Properties/OnUncheck | RemoveIf |  |  |
| L1181 /Screens/ALM - Movement/Children/4/IconSearch_BuildingMaster_Edit_4/Properties/OnSelect | UpdateContext |  |  |
| L1213 /Screens/ALM - Movement/Children/6/Container1_8/Children/0/Form1_9/Properties/DataSource |  | Master_Asset |  |
| L1281 /Screens/ALM - Movement/Children/6/Container1_8/Children/0/Form1_9/Children/0/Location_ID_DataCard2/Children/3/DropdownCanvas8/Properties/DefaultSelectedItems | LookUp | Master_Location |  |
| L1282 /Screens/ALM - Movement/Children/6/Container1_8/Children/0/Form1_9/Children/0/Location_ID_DataCard2/Children/3/DropdownCanvas8/Properties/Items |  | Master_Location |  |
| L1411 /Screens/ALM - Movement/Children/6/Container1_8/Children/0/Form1_9/Children/2/MYID_Asset_Owner_DataCard1/Children/3/ComboboxCanvas1/Properties/DefaultSelectedItems | LookUp | Master_Employee |  |
| L1414 /Screens/ALM - Movement/Children/6/Container1_8/Children/0/Form1_9/Children/2/MYID_Asset_Owner_DataCard1/Children/3/ComboboxCanvas1/Properties/Items | Filter | Master_Employee |  |
| L1726 /Screens/ALM - Movement/Children/6/Container1_8/Children/0/Form1_9/Children/8/Asset_Sub_Status_DataCard1/Properties/DisplayName |  | Master_Asset |  |
| L1727 /Screens/ALM - Movement/Children/6/Container1_8/Children/0/Form1_9/Children/8/Asset_Sub_Status_DataCard1/Properties/MaxLength |  | Master_Asset |  |
| L1785 /Screens/ALM - Movement/Children/6/Container1_8/Children/0/Form1_9/Children/9/Remarks_DataCard2/Properties/DisplayName |  | Master_Asset |  |
| L1786 /Screens/ALM - Movement/Children/6/Container1_8/Children/0/Form1_9/Children/9/Remarks_DataCard2/Properties/MaxLength |  | Master_Asset |  |
| L1846 /Screens/ALM - Movement/Children/6/Container1_8/Children/0/Form1_9/Children/10/Updated_Date_DataCard1/Properties/DisplayName |  | Master_Asset |  |
| L1905 /Screens/ALM - Movement/Children/6/Container1_8/Children/0/Form1_9/Children/11/Update_Type_DataCard1/Properties/DisplayName |  | Master_Asset |  |
| L1906 /Screens/ALM - Movement/Children/6/Container1_8/Children/0/Form1_9/Children/11/Update_Type_DataCard1/Properties/MaxLength |  | Master_Asset |  |
| L1966 /Screens/ALM - Movement/Children/6/Container1_8/Children/1/ButtonClose_Registration_27/Properties/OnSelect | SubmitForm, UpdateContext, Filter, Patch, LookUp, Refresh, ClearCollect, Notify | Master_Category, Asset_Movement_History, Master_Location, Master_Asset, Master_Employee, Master_Asset_Type, AuditLog |  |
| L1981 /Screens/ALM - Movement/Children/6/Container1_8/Children/2/ButtonClose_Registration_28/Properties/OnSelect | UpdateContext |  |  |
| L2003 /Screens/ALM - Movement/Children/7/Container3_1/Children/0/Form2_1/Properties/DataSource |  | Master_Asset |  |
| L2018 /Screens/ALM - Movement/Children/7/Container3_1/Children/0/Form2_1/Children/0/Organization_ID_DataCard5_1/Properties/DisplayName |  | Master_Asset |  |
| L2019 /Screens/ALM - Movement/Children/7/Container3_1/Children/0/Form2_1/Children/0/Organization_ID_DataCard5_1/Properties/MaxLength |  | Master_Asset |  |
| L2071 /Screens/ALM - Movement/Children/7/Container3_1/Children/0/Form2_1/Children/0/Organization_ID_DataCard5_1/Children/3/DropdownCanvas14_1/Properties/Items |  | Master_Organization |  |
| L2092 /Screens/ALM - Movement/Children/7/Container3_1/Children/0/Form2_1/Children/1/Function_ID_DataCard5_1/Properties/DisplayName |  | Master_Asset |  |
| L2093 /Screens/ALM - Movement/Children/7/Container3_1/Children/0/Form2_1/Children/1/Function_ID_DataCard5_1/Properties/MaxLength |  | Master_Asset |  |
| L2145 /Screens/ALM - Movement/Children/7/Container3_1/Children/0/Form2_1/Children/1/Function_ID_DataCard5_1/Children/3/DropdownCanvas15_1/Properties/Items | Filter | Master_Function |  |
| L2166 /Screens/ALM - Movement/Children/7/Container3_1/Children/0/Form2_1/Children/2/Arrival_Date_DataCard4_1/Properties/DisplayName |  | Master_Asset |  |
| L2238 /Screens/ALM - Movement/Children/7/Container3_1/Children/1/ButtonClose_Registration_7/Properties/OnSelect | Navigate |  |  |
| L2254 /Screens/ALM - Movement/Children/7/Container3_1/Children/2/ButtonClose_Registration_29/Properties/OnSelect | ClearCollect, UpdateContext |  |  |
| L2290 /Screens/ALM - Movement/Children/9/ButtonCanvas2_18/Properties/OnSelect | UpdateContext |  |  |
| L2715 /Screens/ALM - Movement/Children/10/Container9_3/Children/2/Container11_11/Children/5/TextInput5_2/Properties/OnChange | UpdateContext |  |  |
| L2742 /Screens/ALM - Movement/Children/10/Container9_3/Children/2/Container11_11/Children/7/TextInput5_3/Properties/OnChange | UpdateContext |  |  |
