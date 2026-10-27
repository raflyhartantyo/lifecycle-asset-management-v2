# ALM - StockOpname - In Use

Reference baseline; target V2 replacement is pending.

Source: `../screens/ALM - StockOpname - In Use.pa.yaml`.

Data references: Acces_Matrix, Master_Asset, Master_Asset_Type, Master_Employee, Master_Function, Master_Location, Master_Organization, Stock_Opname_InUse, Temp_Acc_Reconcile, Temp_Stock_Opname.
Flow calls: AccountingReconciliation-ApprovalRequest, Accounting_ReconsiliationV2, FlowNetworkingDevice, InTuneFlow, Stock_Opname_In_Use_Match, Stock_Opname_In_Use_Trigger.
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
| L14 /Screens/ALM - StockOpname - In Use/Properties/OnHidden | UpdateContext |  |  |
| L18 /Screens/ALM - StockOpname - In Use/Properties/OnVisible | UpdateContext |  |  |
| L37 /Screens/ALM - StockOpname - In Use/Children/0/Trigger Form_1/Children/0/Form2_5/Properties/DataSource |  | Master_Asset |  |
| L52 /Screens/ALM - StockOpname - In Use/Children/0/Trigger Form_1/Children/0/Form2_5/Children/0/Organization_ID_DataCard5_4/Properties/DisplayName |  | Master_Asset |  |
| L53 /Screens/ALM - StockOpname - In Use/Children/0/Trigger Form_1/Children/0/Form2_5/Children/0/Organization_ID_DataCard5_4/Properties/MaxLength |  | Master_Asset |  |
| L105 /Screens/ALM - StockOpname - In Use/Children/0/Trigger Form_1/Children/0/Form2_5/Children/0/Organization_ID_DataCard5_4/Children/3/DropdownCanvas14_4/Properties/Items |  | Master_Organization |  |
| L126 /Screens/ALM - StockOpname - In Use/Children/0/Trigger Form_1/Children/0/Form2_5/Children/1/Function_ID_DataCard5_4/Properties/DisplayName |  | Master_Asset |  |
| L127 /Screens/ALM - StockOpname - In Use/Children/0/Trigger Form_1/Children/0/Form2_5/Children/1/Function_ID_DataCard5_4/Properties/MaxLength |  | Master_Asset |  |
| L179 /Screens/ALM - StockOpname - In Use/Children/0/Trigger Form_1/Children/0/Form2_5/Children/1/Function_ID_DataCard5_4/Children/3/DropdownCanvas15_4/Properties/Items | Filter | Master_Function |  |
| L203 /Screens/ALM - StockOpname - In Use/Children/0/Trigger Form_1/Children/1/ButtonClose_Registration_47/Properties/OnSelect | Navigate |  |  |
| L219 /Screens/ALM - StockOpname - In Use/Children/0/Trigger Form_1/Children/2/ButtonClose_Registration_50/Properties/OnSelect | ClearCollect, UpdateContext |  |  |
| L261 /Screens/ALM - StockOpname - In Use/Children/1/Data_Upload_Form_SO_1/Children/0/Container4_1/Children/0/ButtonClose_Registration_53/Properties/OnSelect | UpdateContext |  |  |
| L279 /Screens/ALM - StockOpname - In Use/Children/1/Data_Upload_Form_SO_1/Children/0/Container4_1/Children/1/ButtonClose_Registration_54/Properties/OnSelect | UpdateContext, Set, Notify |  | InTuneFlow, InTuneFlow, FlowNetworkingDevice |
| L332 /Screens/ALM - StockOpname - In Use/Children/1/Data_Upload_Form_SO_1/Children/0/Container4_1/Children/2/Registration_AttachmentControl_5/Properties/OnAddFile | UpdateContext |  | Accounting_ReconsiliationV2 |
| L422 /Screens/ALM - StockOpname - In Use/Children/1/Data_Upload_Form_SO_1/Children/0/Container4_1/Children/8/Registration_AttachmentControl_6/Properties/OnAddFile | UpdateContext |  | Accounting_ReconsiliationV2 |
| L464 /Screens/ALM - StockOpname - In Use/Children/1/Data_Upload_Form_SO_1/Children/0/Container4_1/Children/10/Registration_AttachmentControl_7/Properties/OnAddFile | UpdateContext |  | Accounting_ReconsiliationV2 |
| L508 /Screens/ALM - StockOpname - In Use/Children/2/HeaderContainer_AssetMaster_8/Children/1/ButtonNew_CategoryMaster_18/Properties/OnSelect | Refresh, ClearCollect | Stock_Opname_InUse |  |
| L522 /Screens/ALM - StockOpname - In Use/Children/2/HeaderContainer_AssetMaster_8/Children/2/ButtonClose_Registration_58/Properties/DisplayMode | LookUp | Acces_Matrix, Master_Employee |  |
| L532 /Screens/ALM - StockOpname - In Use/Children/2/HeaderContainer_AssetMaster_8/Children/2/ButtonClose_Registration_58/Properties/OnSelect | UpdateContext |  |  |
| L545 /Screens/ALM - StockOpname - In Use/Children/2/HeaderContainer_AssetMaster_8/Children/3/Icon15_13/Properties/OnSelect | Navigate |  |  |
| L643 /Screens/ALM - StockOpname - In Use/Children/3/SOLogDataTable_1/Children/0/ColumnNameMasterAsset_31/Children/4/ButtonCanvas2_12/Properties/OnSelect | UpdateContext |  |  |
| L670 /Screens/ALM - StockOpname - In Use/Children/3/SOLogDataTable_1/Children/0/ColumnNameMasterAsset_31/Children/6/ButtonCanvas2_13/Properties/OnSelect | UpdateContext |  |  |
| L697 /Screens/ALM - StockOpname - In Use/Children/3/SOLogDataTable_1/Children/0/ColumnNameMasterAsset_31/Children/9/ButtonCanvas2_14/Properties/OnSelect | UpdateContext |  |  |
| L720 /Screens/ALM - StockOpname - In Use/Children/3/SOLogDataTable_1/Children/1/ColumnValueMasterAsset_31/Properties/Items | Filter, LookUp | Acces_Matrix, Master_Employee |  |
| L829 /Screens/ALM - StockOpname - In Use/Children/3/SOLogDataTable_1/Children/1/ColumnValueMasterAsset_31/Children/2/Column_Value_AsssetDate_MasterAsset_266/Properties/Text | IfError, Filter |  |  |
| L861 /Screens/ALM - StockOpname - In Use/Children/3/SOLogDataTable_1/Children/1/ColumnValueMasterAsset_31/Children/3/NextArrow2_18/Properties/DisplayMode | LookUp | Acces_Matrix, Master_Employee |  |
| L882 /Screens/ALM - StockOpname - In Use/Children/3/SOLogDataTable_1/Children/1/ColumnValueMasterAsset_31/Children/3/NextArrow2_18/Properties/OnSelect | UpdateContext, ClearCollect |  |  |
| L1074 /Screens/ALM - StockOpname - In Use/Children/4/Container_Data_Confirm_8/Children/1/ButtonCanvas1_8/Properties/DisplayMode | LookUp | Acces_Matrix, Master_Employee |  |
| L1085 /Screens/ALM - StockOpname - In Use/Children/4/Container_Data_Confirm_8/Children/1/ButtonCanvas1_8/Properties/OnSelect | UpdateContext, Notify, Refresh | Temp_Acc_Reconcile | AccountingReconciliation-ApprovalRequest |
| L1106 /Screens/ALM - StockOpname - In Use/Children/4/Container_Data_Confirm_8/Children/2/ButtonClose_Registration_56/Properties/OnSelect | UpdateContext |  |  |
| L1346 /Screens/ALM - StockOpname - In Use/Children/4/Container_Data_Confirm_8/Children/3/AssetDataContainer_30/Children/1/ColumnValueMasterAsset_34/Properties/Items | Filter |  |  |
| L1682 /Screens/ALM - StockOpname - In Use/Children/4/Container_Data_Confirm_8/Children/3/AssetDataContainer_30/Children/1/ColumnValueMasterAsset_34/Children/13/Combobox2/Properties/DefaultSelectedItems | LookUp | Master_Employee |  |
| L1693 /Screens/ALM - StockOpname - In Use/Children/4/Container_Data_Confirm_8/Children/3/AssetDataContainer_30/Children/1/ColumnValueMasterAsset_34/Children/13/Combobox2/Properties/OnChange | Patch |  |  |
| L1753 /Screens/ALM - StockOpname - In Use/Children/4/Container_Data_Confirm_8/Children/4/ButtonCanvas2_15/Properties/OnSelect | UpdateContext |  |  |
| L1772 /Screens/ALM - StockOpname - In Use/Children/4/Container_Data_Confirm_8/Children/5/ButtonClose_Registration_57/Properties/OnSelect | UpdateContext |  |  |
| L1786 /Screens/ALM - StockOpname - In Use/Children/4/Container_Data_Confirm_8/Children/6/ButtonCanvas1_9/Properties/OnSelect | UpdateContext |  |  |
| L1898 /Screens/ALM - StockOpname - In Use/Children/4/Container_Data_Confirm_8/Children/11/conStatusSummary/Children/0/Container8_2/Children/1/Text4/Properties/Text | Filter |  |  |
| L1949 /Screens/ALM - StockOpname - In Use/Children/4/Container_Data_Confirm_8/Children/11/conStatusSummary/Children/1/Container8_1/Children/1/Text4_9/Properties/Text | Filter |  |  |
| L1998 /Screens/ALM - StockOpname - In Use/Children/4/Container_Data_Confirm_8/Children/11/conStatusSummary/Children/2/Container8/Children/1/Text4_10/Properties/Text | Filter |  |  |
| L2061 /Screens/ALM - StockOpname - In Use/Children/4/Container_Data_Confirm_8/Children/12/Container10_1/Children/0/Container11/Children/1/Text6_1/Properties/Text | IfError, Filter |  |  |
| L2094 /Screens/ALM - StockOpname - In Use/Children/4/Container_Data_Confirm_8/Children/12/Container10_1/Children/1/Container10/Children/0/Rectangle4/Properties/Width | IfError, Filter |  |  |
| L2105 /Screens/ALM - StockOpname - In Use/Children/4/Container_Data_Confirm_8/Children/12/Container10_1/Children/1/Container10/Children/1/Rectangle4_1/Properties/Width | IfError, Filter |  |  |
| L2115 /Screens/ALM - StockOpname - In Use/Children/4/Container_Data_Confirm_8/Children/12/Container10_1/Children/2/Text7/Properties/Text | Filter |  |  |
| L2580 /Screens/ALM - StockOpname - In Use/Children/4/Container_Data_Confirm_8/Children/16/ButtonCanvas1_10/Properties/OnSelect | UpdateContext, Patch, LookUp, Refresh, ClearCollect, Notify | Stock_Opname_InUse, Temp_Stock_Opname |  |
| L2622 /Screens/ALM - StockOpname - In Use/Children/4/Container_Data_Confirm_8/Children/17/Toggle2/Properties/Default | LookUp | Stock_Opname_InUse |  |
| L2631 /Screens/ALM - StockOpname - In Use/Children/4/Container_Data_Confirm_8/Children/17/Toggle2/Properties/OnCheck | UpdateIf, Patch, Notify | Stock_Opname_InUse |  |
| L2649 /Screens/ALM - StockOpname - In Use/Children/4/Container_Data_Confirm_8/Children/17/Toggle2/Properties/OnUncheck | Patch, Notify | Stock_Opname_InUse |  |
| L2666 /Screens/ALM - StockOpname - In Use/Children/4/Container_Data_Confirm_8/Children/18/ButtonCanvas1_11/Properties/DisplayMode | LookUp | Acces_Matrix, Master_Employee |  |
| L2685 /Screens/ALM - StockOpname - In Use/Children/4/Container_Data_Confirm_8/Children/18/ButtonCanvas1_11/Properties/OnSelect | UpdateContext, Notify |  | Stock_Opname_In_Use_Trigger |
| L2940 /Screens/ALM - StockOpname - In Use/Children/5/Container6/Children/0/Container13/Children/0/Button1/Properties/OnSelect | UpdateContext |  |  |
| L3028 /Screens/ALM - StockOpname - In Use/Children/5/Container6/Children/0/Container13/Children/2/Button3/Properties/OnSelect | UpdateContext, ClearCollect, LookUp, Filter, Notify | Master_Location, Master_Asset, Master_Employee, Master_Asset_Type | Stock_Opname_In_Use_Match |
