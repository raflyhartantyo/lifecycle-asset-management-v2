# ALM - StockOpname - Available

Reference baseline; target V2 replacement is pending.

Source: `../screens/ALM - StockOpname - Available.pa.yaml`.

Data references: Acces_Matrix, Master_Asset, Master_Asset_Type, Master_Employee, Master_Function, Master_Organization, Temp_Acc_Reconcile, Temp_Stock_Opname.
Flow calls: AccountingReconciliation-ApprovalRequest, Accounting_ReconsiliationV2, ExportData, FlowNetworkingDevice, InTuneFlow, SO_Respondent_Save, SO_Respondents_Confirm, Stock_Opname_Available_Trigger.
Navigation destinations: 2_HomePage, Home Page_Stock_Opname.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Inspect the destination Studio-generated YAML shape before pasting. A full Screens: export wrapper is not assumed to be a paste-ready control snippet. Use supported screen/control copy-and-paste where compatible, or apply the supplied property formulas to the matching screen/control. Capture any rejected YAML and schema error before requesting an adapted delivery.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
| L14 /Screens/ALM - StockOpname - Available/Properties/OnHidden | UpdateContext |  |  |
| L17 /Screens/ALM - StockOpname - Available/Properties/OnVisible | UpdateContext |  |  |
| L37 /Screens/ALM - StockOpname - Available/Children/0/Trigger Form/Children/0/Form2_4/Properties/DataSource |  | Master_Asset |  |
| L52 /Screens/ALM - StockOpname - Available/Children/0/Trigger Form/Children/0/Form2_4/Children/0/Organization_ID_DataCard5_3/Properties/DisplayName |  | Master_Asset |  |
| L53 /Screens/ALM - StockOpname - Available/Children/0/Trigger Form/Children/0/Form2_4/Children/0/Organization_ID_DataCard5_3/Properties/MaxLength |  | Master_Asset |  |
| L105 /Screens/ALM - StockOpname - Available/Children/0/Trigger Form/Children/0/Form2_4/Children/0/Organization_ID_DataCard5_3/Children/3/DropdownCanvas14_3/Properties/Items |  | Master_Organization |  |
| L126 /Screens/ALM - StockOpname - Available/Children/0/Trigger Form/Children/0/Form2_4/Children/1/Function_ID_DataCard5_3/Properties/DisplayName |  | Master_Asset |  |
| L127 /Screens/ALM - StockOpname - Available/Children/0/Trigger Form/Children/0/Form2_4/Children/1/Function_ID_DataCard5_3/Properties/MaxLength |  | Master_Asset |  |
| L179 /Screens/ALM - StockOpname - Available/Children/0/Trigger Form/Children/0/Form2_4/Children/1/Function_ID_DataCard5_3/Children/3/DropdownCanvas15_3/Properties/Items | Filter | Master_Function |  |
| L203 /Screens/ALM - StockOpname - Available/Children/0/Trigger Form/Children/1/ButtonClose_Registration_43/Properties/OnSelect | Navigate |  |  |
| L219 /Screens/ALM - StockOpname - Available/Children/0/Trigger Form/Children/2/ButtonClose_Registration_44/Properties/OnSelect | ClearCollect, UpdateContext |  |  |
| L261 /Screens/ALM - StockOpname - Available/Children/1/Data_Upload_Form_SO/Children/0/Container4/Children/0/ButtonClose_Registration_45/Properties/OnSelect | UpdateContext |  |  |
| L279 /Screens/ALM - StockOpname - Available/Children/1/Data_Upload_Form_SO/Children/0/Container4/Children/1/ButtonClose_Registration_46/Properties/OnSelect | UpdateContext, Set, Notify |  | InTuneFlow, InTuneFlow, FlowNetworkingDevice |
| L332 /Screens/ALM - StockOpname - Available/Children/1/Data_Upload_Form_SO/Children/0/Container4/Children/2/Registration_AttachmentControl_2/Properties/OnAddFile | UpdateContext |  | Accounting_ReconsiliationV2 |
| L422 /Screens/ALM - StockOpname - Available/Children/1/Data_Upload_Form_SO/Children/0/Container4/Children/8/Registration_AttachmentControl_3/Properties/OnAddFile | UpdateContext |  | Accounting_ReconsiliationV2 |
| L464 /Screens/ALM - StockOpname - Available/Children/1/Data_Upload_Form_SO/Children/0/Container4/Children/10/Registration_AttachmentControl_4/Properties/OnAddFile | UpdateContext |  | Accounting_ReconsiliationV2 |
| L594 /Screens/ALM - StockOpname - Available/Children/3/SOLogDataTable/Children/0/ColumnNameMasterAsset_29/Children/4/ButtonCanvas2_8/Properties/OnSelect | UpdateContext |  |  |
| L621 /Screens/ALM - StockOpname - Available/Children/3/SOLogDataTable/Children/0/ColumnNameMasterAsset_29/Children/6/ButtonCanvas2_9/Properties/OnSelect | UpdateContext |  |  |
| L648 /Screens/ALM - StockOpname - Available/Children/3/SOLogDataTable/Children/0/ColumnNameMasterAsset_29/Children/9/ButtonCanvas2_10/Properties/OnSelect | UpdateContext |  |  |
| L671 /Screens/ALM - StockOpname - Available/Children/3/SOLogDataTable/Children/1/ColumnValueMasterAsset_29/Properties/Items | Filter, LookUp | Acces_Matrix, Master_Employee |  |
| L792 /Screens/ALM - StockOpname - Available/Children/3/SOLogDataTable/Children/1/ColumnValueMasterAsset_29/Children/3/NextArrow2_17/Properties/DisplayMode | LookUp | Acces_Matrix, Master_Employee |  |
| L813 /Screens/ALM - StockOpname - Available/Children/3/SOLogDataTable/Children/1/ColumnValueMasterAsset_29/Children/3/NextArrow2_17/Properties/OnSelect | UpdateContext, ClearCollect, LookUp, Filter | Acces_Matrix, Master_Employee, Master_Asset_Type |  |
| L1100 /Screens/ALM - StockOpname - Available/Children/4/HeaderContainer_AssetMaster_7/Children/1/ButtonNew_CategoryMaster_17/Properties/OnSelect | Refresh, ClearCollect | Temp_Stock_Opname |  |
| L1114 /Screens/ALM - StockOpname - Available/Children/4/HeaderContainer_AssetMaster_7/Children/2/ButtonClose_Registration_49/Properties/DisplayMode | LookUp | Acces_Matrix, Master_Employee |  |
| L1124 /Screens/ALM - StockOpname - Available/Children/4/HeaderContainer_AssetMaster_7/Children/2/ButtonClose_Registration_49/Properties/OnSelect | UpdateContext, Notify |  | Stock_Opname_Available_Trigger |
| L1141 /Screens/ALM - StockOpname - Available/Children/4/HeaderContainer_AssetMaster_7/Children/3/Icon15_12/Properties/OnSelect | Navigate |  |  |
| L1173 /Screens/ALM - StockOpname - Available/Children/5/Container_Data_Confirm_7/Children/1/ButtonCanvas1_5/Properties/DisplayMode | LookUp | Acces_Matrix, Master_Employee |  |
| L1184 /Screens/ALM - StockOpname - Available/Children/5/Container_Data_Confirm_7/Children/1/ButtonCanvas1_5/Properties/OnSelect | UpdateContext, Notify, Refresh | Temp_Acc_Reconcile | AccountingReconciliation-ApprovalRequest |
| L1205 /Screens/ALM - StockOpname - Available/Children/5/Container_Data_Confirm_7/Children/2/ButtonClose_Registration_51/Properties/OnSelect | UpdateContext |  |  |
| L1367 /Screens/ALM - StockOpname - Available/Children/5/Container_Data_Confirm_7/Children/3/AssetDataContainer_29/Children/0/ColumnNameMasterAsset_30/Children/8/ButtonCanvas2_11/Properties/OnSelect | UpdateContext |  |  |
| L1382 /Screens/ALM - StockOpname - Available/Children/5/Container_Data_Confirm_7/Children/3/AssetDataContainer_29/Children/1/ColumnValueMasterAsset_30/Properties/Items | Filter |  |  |
| L1413 /Screens/ALM - StockOpname - Available/Children/5/Container_Data_Confirm_7/Children/3/AssetDataContainer_29/Children/1/ColumnValueMasterAsset_30/Children/0/TextInput1/Properties/OnChange | Patch |  |  |
| L1575 /Screens/ALM - StockOpname - Available/Children/5/Container_Data_Confirm_7/Children/3/AssetDataContainer_29/Children/1/ColumnValueMasterAsset_30/Children/8/NextArrow2_12/Properties/OnSelect | Patch |  |  |
| L1714 /Screens/ALM - StockOpname - Available/Children/5/Container_Data_Confirm_7/Children/4/Container9_1/Children/0/Container11_3/Children/0/Container15/Children/0/Checkbox2/Properties/OnUncheck | Filter, Patch |  |  |
| L1870 /Screens/ALM - StockOpname - Available/Children/5/Container_Data_Confirm_7/Children/5/ButtonClose_Registration_52/Properties/OnSelect | UpdateContext |  |  |
| L1881 /Screens/ALM - StockOpname - Available/Children/5/Container_Data_Confirm_7/Children/6/ButtonCanvas1_6/Properties/DisplayMode | LookUp |  |  |
| L1899 /Screens/ALM - StockOpname - Available/Children/5/Container_Data_Confirm_7/Children/6/ButtonCanvas1_6/Properties/OnSelect | Refresh, ClearCollect, LookUp, Filter, Notify | Temp_Stock_Opname | SO_Respondents_Confirm |
| L1992 /Screens/ALM - StockOpname - Available/Children/5/Container_Data_Confirm_7/Children/7/ButtonCanvas1_4/Properties/OnSelect | UpdateContext |  |  |
| L2039 /Screens/ALM - StockOpname - Available/Children/5/Container_Data_Confirm_7/Children/11/Icon5/Properties/DisplayMode | LookUp |  |  |
| L2057 /Screens/ALM - StockOpname - Available/Children/5/Container_Data_Confirm_7/Children/11/Icon5/Properties/OnSelect | UpdateContext, Notify |  | SO_Respondent_Save |
| L2860 /Screens/ALM - StockOpname - Available/Children/5/Container_Data_Confirm_7/Children/15/SummarySOTable_2/Children/1/ColumnValueMasterAsset_38/Properties/Items | Filter |  |  |
| L3192 /Screens/ALM - StockOpname - Available/Children/5/Container_Data_Confirm_7/Children/20/ButtonCanvas1_7/Properties/OnSelect | Patch |  |  |
| L3231 /Screens/ALM - StockOpname - Available/Children/5/Container_Data_Confirm_7/Children/22/Icon11_1/Properties/OnSelect | UpdateContext, Set, Notify |  | ExportData |
