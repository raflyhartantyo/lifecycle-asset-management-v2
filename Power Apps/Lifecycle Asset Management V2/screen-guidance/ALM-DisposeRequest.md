# ALM-DisposeRequest

Retired from target V2: separate disposal-request/approval. Preserve this file as baseline evidence; omit this screen and its navigation in future V2 releases.

Source: `../screens/ALM-DisposeRequest.pa.yaml`.

Data references: Master_Asset, Master_Asset_Type, Master_Employee, Master_Function, Master_Organization.
Flow calls: none found by static formula scan.
Navigation destinations: 2_HomePage.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Inspect the destination Studio-generated YAML shape before pasting. A full Screens: export wrapper is not assumed to be a paste-ready control snippet. Use supported screen/control copy-and-paste where compatible, or apply the supplied property formulas to the matching screen/control. Capture any rejected YAML and schema error before requesting an adapted delivery.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
| L13 /Screens/ALM-DisposeRequest/Properties/OnVisible | UpdateContext |  |  |
| L158 /Screens/ALM-DisposeRequest/Children/1/AssetDataContainer_22/Children/0/ColumnNameMasterAsset_22/Children/4/ButtonCanvas2_1/Properties/OnSelect | UpdateContext |  |  |
| L169 /Screens/ALM-DisposeRequest/Children/1/AssetDataContainer_22/Children/0/ColumnNameMasterAsset_22/Children/5/ButtonCanvas2_2/Properties/OnSelect | UpdateContext |  |  |
| L192 /Screens/ALM-DisposeRequest/Children/1/AssetDataContainer_22/Children/1/ColumnValueMasterAsset_22/Properties/Items | Filter |  |  |
| L317 /Screens/ALM-DisposeRequest/Children/1/AssetDataContainer_22/Children/1/ColumnValueMasterAsset_22/Children/5/NextArrow2_13/Properties/OnSelect | UpdateContext, ClearCollect, IfError |  |  |
| L421 /Screens/ALM-DisposeRequest/Children/2/ButtonClose_Registration_14/Properties/OnSelect | Refresh, ClearCollect |  |  |
| L433 /Screens/ALM-DisposeRequest/Children/3/ButtonUpload_Registration_2/Properties/OnSelect | UpdateContext |  |  |
| L449 /Screens/ALM-DisposeRequest/Children/4/ButtonClose_Registration_12/Properties/OnSelect | Navigate, UpdateContext |  |  |
| L492 /Screens/ALM-DisposeRequest/Children/5/Container_Data_Confirm_6/Children/1/ButtonCanvas1_2/Properties/OnSelect | UpdateContext |  |  |
| L507 /Screens/ALM-DisposeRequest/Children/5/Container_Data_Confirm_6/Children/2/ButtonClose_Registration_36/Properties/OnSelect | UpdateContext |  |  |
| L525 /Screens/ALM-DisposeRequest/Children/5/Container_Data_Confirm_6/Children/3/ButtonClose_Registration_37/Properties/OnSelect | UpdateContext |  |  |
| L955 /Screens/ALM-DisposeRequest/Children/5/Container_Data_Confirm_6/Children/5/AssetDataContainer_20/Children/1/ColumnValueMasterAsset_20/Properties/TemplateFill | LookUp |  |  |
| L1096 /Screens/ALM-DisposeRequest/Children/5/Container_Data_Confirm_6/Children/5/AssetDataContainer_20/Children/1/ColumnValueMasterAsset_20/Children/7/Column_Value_AsssetDate_MasterAsset_238/Properties/Text | LookUp | Master_Employee |  |
| L1159 /Screens/ALM-DisposeRequest/Children/6/Container3_3/Children/0/Form2_3/Properties/DataSource |  | Master_Asset |  |
| L1174 /Screens/ALM-DisposeRequest/Children/6/Container3_3/Children/0/Form2_3/Children/0/Organization_ID_DataCard5_2/Properties/DisplayName |  | Master_Asset |  |
| L1175 /Screens/ALM-DisposeRequest/Children/6/Container3_3/Children/0/Form2_3/Children/0/Organization_ID_DataCard5_2/Properties/MaxLength |  | Master_Asset |  |
| L1227 /Screens/ALM-DisposeRequest/Children/6/Container3_3/Children/0/Form2_3/Children/0/Organization_ID_DataCard5_2/Children/3/DropdownCanvas14_2/Properties/Items |  | Master_Organization |  |
| L1248 /Screens/ALM-DisposeRequest/Children/6/Container3_3/Children/0/Form2_3/Children/1/Function_ID_DataCard5_2/Properties/DisplayName |  | Master_Asset |  |
| L1249 /Screens/ALM-DisposeRequest/Children/6/Container3_3/Children/0/Form2_3/Children/1/Function_ID_DataCard5_2/Properties/MaxLength |  | Master_Asset |  |
| L1301 /Screens/ALM-DisposeRequest/Children/6/Container3_3/Children/0/Form2_3/Children/1/Function_ID_DataCard5_2/Children/3/DropdownCanvas15_2/Properties/Items | Filter | Master_Function |  |
| L1325 /Screens/ALM-DisposeRequest/Children/6/Container3_3/Children/1/ButtonClose_Registration_38/Properties/OnSelect | UpdateContext |  |  |
| L1341 /Screens/ALM-DisposeRequest/Children/6/Container3_3/Children/2/ButtonClose_Registration_39/Properties/OnSelect | ClearCollect, UpdateContext |  |  |
| L1535 /Screens/ALM-DisposeRequest/Children/7/Container2/Children/0/AssetDataContainer_23/Children/1/ColumnValueMasterAsset_23/Properties/Items | Filter | Master_Asset |  |
| L1582 /Screens/ALM-DisposeRequest/Children/7/Container2/Children/0/AssetDataContainer_23/Children/1/ColumnValueMasterAsset_23/Properties/TemplateFill | LookUp |  |  |
| L1677 /Screens/ALM-DisposeRequest/Children/7/Container2/Children/0/AssetDataContainer_23/Children/1/ColumnValueMasterAsset_23/Children/4/Column_Value_AsssetDate_MasterAsset_227/Properties/Text | LookUp | Master_Asset_Type |  |
| L1739 /Screens/ALM-DisposeRequest/Children/7/Container2/Children/0/AssetDataContainer_23/Children/1/ColumnValueMasterAsset_23/Children/9/NextArrow2_14/Properties/Icon | LookUp |  |  |
| L1745 /Screens/ALM-DisposeRequest/Children/7/Container2/Children/0/AssetDataContainer_23/Children/1/ColumnValueMasterAsset_23/Children/9/NextArrow2_14/Properties/OnSelect | LookUp, Collect, RemoveIf |  |  |
| L1794 /Screens/ALM-DisposeRequest/Children/7/Container2/Children/0/AssetDataContainer_23/Children/1/ColumnValueMasterAsset_23/Children/11/Column_Value_AsssetDate_MasterAsset_230/Properties/Text | LookUp | Master_Employee |  |
| L1856 /Screens/ALM-DisposeRequest/Children/7/Container2/Children/1/HeaderContainer_AssetMaster_5/Children/1/ButtonClose_Registration_40/Properties/OnSelect | UpdateContext |  |  |
| L1894 /Screens/ALM-DisposeRequest/Children/7/Container2/Children/1/HeaderContainer_AssetMaster_5/Children/3/IconSearch_BuildingMaster_Edit_6/Properties/OnSelect | Refresh | Master_Asset |  |
| L1920 /Screens/ALM-DisposeRequest/Children/7/Container2/Children/1/HeaderContainer_AssetMaster_5/Children/5/ButtonClose_Registration_42/Properties/OnSelect | UpdateContext |  |  |
| L2108 /Screens/ALM-DisposeRequest/Children/8/Container_Data_Confirm_5/Children/1/AssetDataContainer_18/Children/1/ColumnValueMasterAsset_18/Properties/TemplateFill | LookUp |  |  |
| L2207 /Screens/ALM-DisposeRequest/Children/8/Container_Data_Confirm_5/Children/1/AssetDataContainer_18/Children/1/ColumnValueMasterAsset_18/Children/3/Column_Value_AsssetDate_MasterAsset_190/Properties/Text | LookUp | Master_Employee |  |
| L2351 /Screens/ALM-DisposeRequest/Children/8/Container_Data_Confirm_5/Children/2/ButtonClose_Registration_35/Properties/OnSelect | UpdateContext, ClearCollect, LookUp, Patch | Master_Employee |  |
| L2416 /Screens/ALM-DisposeRequest/Children/8/Container_Data_Confirm_5/Children/3/ButtonClose_Registration_41/Properties/OnSelect | UpdateContext |  |  |
