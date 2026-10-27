# ALM-AccReconcile

Reference baseline; target V2 replacement is pending.

Source: `../screens/ALM-AccReconcile.pa.yaml`.

Data references: Master_Asset, Master_Asset_Type, Master_Category, Master_Employee, Master_Function, Master_Location, Master_Organization, Temp_Acc_Reconcile.
Flow calls: AccountingReconciliation-ApprovalRequest, Accounting_ReconsiliationV3.
Navigation destinations: 2_HomePage, ALM-Registration.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Inspect the destination Studio-generated YAML shape before pasting. A full Screens: export wrapper is not assumed to be a paste-ready control snippet. Use supported screen/control copy-and-paste where compatible, or apply the supplied property formulas to the matching screen/control. Capture any rejected YAML and schema error before requesting an adapted delivery.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
| L13 /Screens/ALM-AccReconcile/Properties/OnHidden | UpdateContext |  |  |
| L17 /Screens/ALM-AccReconcile/Properties/OnVisible | UpdateContext |  |  |
| L89 /Screens/ALM-AccReconcile/Children/2/ButtonClose_Registration_10/Properties/OnSelect | Navigate, UpdateContext |  |  |
| L120 /Screens/ALM-AccReconcile/Children/3/Registration_AttachmentControl_1/Properties/OnAddFile | UpdateContext |  | Accounting_ReconsiliationV3 |
| L154 /Screens/ALM-AccReconcile/Children/4/Timer1/Properties/OnTimerEnd | ClearCollect, Filter, UpdateContext, LookUp, Notify | Temp_Acc_Reconcile |  |
| L316 /Screens/ALM-AccReconcile/Children/5/AssetDataContainer_14/Children/0/ColumnNameMasterAsset_14/Children/4/ButtonCanvas2/Properties/OnSelect | UpdateContext |  |  |
| L343 /Screens/ALM-AccReconcile/Children/5/AssetDataContainer_14/Children/0/ColumnNameMasterAsset_14/Children/6/ButtonCanvas2_3/Properties/OnSelect | UpdateContext |  |  |
| L370 /Screens/ALM-AccReconcile/Children/5/AssetDataContainer_14/Children/0/ColumnNameMasterAsset_14/Children/9/ButtonCanvas2_7/Properties/OnSelect | UpdateContext |  |  |
| L393 /Screens/ALM-AccReconcile/Children/5/AssetDataContainer_14/Children/1/ColumnValueMasterAsset_14/Properties/Items | Filter |  |  |
| L502 /Screens/ALM-AccReconcile/Children/5/AssetDataContainer_14/Children/1/ColumnValueMasterAsset_14/Children/3/NextArrow2_10/Properties/OnSelect | UpdateContext, ClearCollect |  |  |
| L654 /Screens/ALM-AccReconcile/Children/6/ButtonClose_Registration_13/Properties/OnSelect | Refresh, ClearCollect | Temp_Acc_Reconcile |  |
| L813 /Screens/ALM-AccReconcile/Children/7/Container_Data_Confirm_1/Children/1/AssetDataContainer_13/Children/1/ColumnValueMasterAsset_13/Properties/TemplateFill | LookUp |  |  |
| L941 /Screens/ALM-AccReconcile/Children/7/Container_Data_Confirm_1/Children/1/AssetDataContainer_13/Children/1/ColumnValueMasterAsset_13/Children/6/NextArrow2_11/Properties/Icon | LookUp |  |  |
| L947 /Screens/ALM-AccReconcile/Children/7/Container_Data_Confirm_1/Children/1/AssetDataContainer_13/Children/1/ColumnValueMasterAsset_13/Children/6/NextArrow2_11/Properties/OnSelect | LookUp, Collect, RemoveIf |  |  |
| L1045 /Screens/ALM-AccReconcile/Children/7/Container_Data_Confirm_1/Children/2/ButtonClose_Registration_11/Properties/OnSelect | UpdateContext, Set, Navigate, Notify, Patch, LookUp | Temp_Acc_Reconcile |  |
| L1128 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/1/ButtonClose_Registration_8/Properties/OnSelect | UpdateContext |  |  |
| L1147 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/2/ButtonClose_Registration_9/Properties/OnSelect | UpdateContext |  |  |
| L1489 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/3/AssetDataContainer_15/Children/1/ColumnValueMasterAsset_15/Children/1/Column_Value_AsssetDate_MasterAsset_156/Properties/Text | LookUp | Master_Asset |  |
| L1510 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/3/AssetDataContainer_15/Children/1/ColumnValueMasterAsset_15/Children/2/Column_Value_AsssetDate_MasterAsset_157/Properties/Text | LookUp | Master_Asset, Master_Organization |  |
| L1538 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/3/AssetDataContainer_15/Children/1/ColumnValueMasterAsset_15/Children/4/Column_Value_AsssetDate_MasterAsset_159/Properties/Text | LookUp | Master_Asset |  |
| L1552 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/3/AssetDataContainer_15/Children/1/ColumnValueMasterAsset_15/Children/5/Column_Value_AsssetDate_MasterAsset_160/Properties/Text | LookUp | Master_Asset, Master_Employee |  |
| L1599 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/3/AssetDataContainer_15/Children/1/ColumnValueMasterAsset_15/Children/9/Column_Value_AsssetDate_MasterAsset_161/Properties/Text | LookUp | Master_Asset, Master_Employee |  |
| L1613 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/3/AssetDataContainer_15/Children/1/ColumnValueMasterAsset_15/Children/10/Column_Value_AsssetDate_MasterAsset_162/Properties/Text | LookUp | Master_Asset |  |
| L1627 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/3/AssetDataContainer_15/Children/1/ColumnValueMasterAsset_15/Children/11/Column_Value_AsssetDate_MasterAsset_163/Properties/Text | LookUp | Master_Asset |  |
| L1641 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/3/AssetDataContainer_15/Children/1/ColumnValueMasterAsset_15/Children/12/Column_Value_AsssetDate_MasterAsset_164/Properties/Text | LookUp | Master_Location, Master_Asset |  |
| L1655 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/3/AssetDataContainer_15/Children/1/ColumnValueMasterAsset_15/Children/13/Column_Value_AsssetDate_MasterAsset_165/Properties/Text | LookUp | Master_Asset, Master_Asset_Type |  |
| L1669 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/3/AssetDataContainer_15/Children/1/ColumnValueMasterAsset_15/Children/14/Column_Value_AsssetDate_MasterAsset_166/Properties/Text | LookUp | Master_Category, Master_Asset, Master_Asset_Type |  |
| L1683 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/3/AssetDataContainer_15/Children/1/ColumnValueMasterAsset_15/Children/15/Column_Value_AsssetDate_MasterAsset_167/Properties/Text | LookUp | Master_Asset |  |
| L1697 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/3/AssetDataContainer_15/Children/1/ColumnValueMasterAsset_15/Children/16/Column_Value_AsssetDate_MasterAsset_174/Properties/Text | LookUp | Master_Asset |  |
| L1711 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/3/AssetDataContainer_15/Children/1/ColumnValueMasterAsset_15/Children/17/Column_Value_AsssetDate_MasterAsset_175/Properties/Text | LookUp | Master_Asset |  |
| L1725 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/3/AssetDataContainer_15/Children/1/ColumnValueMasterAsset_15/Children/18/Column_Value_AsssetDate_MasterAsset_176/Properties/Text | LookUp | Master_Asset, Master_Function |  |
| L1739 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/3/AssetDataContainer_15/Children/1/ColumnValueMasterAsset_15/Children/19/Column_Value_AsssetDate_MasterAsset_177/Properties/Text | LookUp | Master_Asset |  |
| L1753 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/3/AssetDataContainer_15/Children/1/ColumnValueMasterAsset_15/Children/20/Column_Value_AsssetDate_MasterAsset_178/Properties/Text | LookUp | Master_Asset |  |
| L1767 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/3/AssetDataContainer_15/Children/1/ColumnValueMasterAsset_15/Children/21/Column_Value_AsssetDate_MasterAsset_179/Properties/Text | LookUp | Master_Asset |  |
| L1902 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/4/AssetDataContainer_16/Children/1/ColumnValueMasterAsset_16/Properties/TemplateFill | LookUp |  |  |
| L2070 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/5/ButtonCanvas1/Properties/OnSelect | UpdateContext |  |  |
| L2085 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/6/ButtonClose_Registration_48/Properties/OnSelect | UpdateContext |  |  |
| L2111 /Screens/ALM-AccReconcile/Children/9/Container_Data_Confirm_3/Children/8/ButtonCanvas1_3/Properties/OnSelect | UpdateContext, Notify, Refresh | Temp_Acc_Reconcile | AccountingReconciliation-ApprovalRequest |
| L3372 /Screens/ALM-AccReconcile/Children/10/Container_Data_Confirm_4/Children/1/ButtonCanvas1_1/Properties/OnSelect | UpdateContext |  |  |
| L3460 /Screens/ALM-AccReconcile/Children/10/Container_Data_Confirm_4/Children/2/AssetDataContainer_17/Children/1/ColumnValueMasterAsset_17/Properties/TemplateFill | LookUp |  |  |
