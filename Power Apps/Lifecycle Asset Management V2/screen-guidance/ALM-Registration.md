# ALM-Registration

Reference baseline; target V2 replacement is pending.

Source: `../screens/ALM-Registration.pa.yaml`.

Data references: AuditLog, Master_Asset, Master_Asset_Type, Master_Category, Master_Employee, Master_Function, Master_Location, Master_Organization.
Flow calls: Bulk_Registration.
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
| L13 /Screens/ALM-Registration/Properties/OnHidden | UpdateContext |  |  |
| L17 /Screens/ALM-Registration/Properties/OnVisible | UpdateContext, ClearCollect |  |  |
| L121 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/0/SidebarContainer_Registration/Children/0/DataGallery_Registration/Properties/OnSelect | UpdateContext |  |  |
| L200 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/0/SidebarContainer_Registration/Children/0/DataGallery_Registration/Children/4/IconDelete_Registration/Properties/OnSelect | UpdateContext |  |  |
| L228 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/0/SidebarContainer_Registration/Children/0/DataGallery_Registration/Children/6/TextDepartment_Registration/Properties/Text | LookUp | Master_Category, Master_Asset_Type |  |
| L248 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/0/SidebarContainer_Registration/Children/0/DataGallery_Registration/Children/7/TextDepartment_Registration_1/Properties/Text | LookUp | Master_Location, Master_Employee |  |
| L284 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/0/SidebarContainer_Registration/Children/0/DataGallery_Registration/Children/9/Icon14/Properties/Visible | LookUp | Master_Asset |  |
| L313 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/0/SidebarContainer_Registration/Children/1/ButtonSave_Registration/Properties/OnSelect | UpdateContext, Notify |  |  |
| L345 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Properties/DataSource |  | Master_Asset |  |
| L358 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/0/Accounting_Asset_Code_DataCard2/Properties/DisplayName |  | Master_Asset |  |
| L359 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/0/Accounting_Asset_Code_DataCard2/Properties/MaxLength |  | Master_Asset |  |
| L361 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/0/Accounting_Asset_Code_DataCard2/Properties/Update | LookUp | Master_Asset |  |
| L402 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/0/Accounting_Asset_Code_DataCard2/Children/2/ErrorMessage54/Properties/Text | LookUp | Master_Asset |  |
| L434 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/1/Asset_Name_DataCard2/Properties/DisplayName |  | Master_Asset |  |
| L435 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/1/Asset_Name_DataCard2/Properties/MaxLength |  | Master_Asset |  |
| L513 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/2/Location_ID_DataCard3/Properties/DisplayName |  | Master_Asset |  |
| L514 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/2/Location_ID_DataCard3/Properties/MaxLength |  | Master_Asset |  |
| L567 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/2/Location_ID_DataCard3/Children/3/DropdownCanvas11/Properties/DefaultSelectedItems | LookUp | Master_Location |  |
| L569 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/2/Location_ID_DataCard3/Children/3/DropdownCanvas11/Properties/Items |  | Master_Location |  |
| L590 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/3/MYID_Asset_Owner_DataCard2/Properties/DisplayName |  | Master_Asset |  |
| L591 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/3/MYID_Asset_Owner_DataCard2/Properties/MaxLength |  | Master_Asset |  |
| L644 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/3/MYID_Asset_Owner_DataCard2/Children/3/ComboboxCanvas2/Properties/DefaultSelectedItems | LookUp | Master_Employee |  |
| L646 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/3/MYID_Asset_Owner_DataCard2/Children/3/ComboboxCanvas2/Properties/Items | Filter | Master_Employee |  |
| L671 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/4/Asset_Type_ID_DataCard3/Properties/DisplayName |  | Master_Asset |  |
| L672 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/4/Asset_Type_ID_DataCard3/Properties/MaxLength |  | Master_Asset |  |
| L699 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/4/Asset_Type_ID_DataCard3/Children/1/DropdownCanvas13/Properties/DefaultSelectedItems | LookUp | Master_Asset_Type |  |
| L700 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/4/Asset_Type_ID_DataCard3/Children/1/DropdownCanvas13/Properties/Items |  | Master_Asset_Type |  |
| L783 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/5/Purchasing_Price_DataCard1/Properties/DisplayName |  | Master_Asset |  |
| L857 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/6/HostName_DataCard1/Properties/DisplayName |  | Master_Asset |  |
| L858 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/6/HostName_DataCard1/Properties/MaxLength |  | Master_Asset |  |
| L934 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/7/Serial_Number_DataCard1/Properties/DisplayName |  | Master_Asset |  |
| L935 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/7/Serial_Number_DataCard1/Properties/MaxLength |  | Master_Asset |  |
| L1026 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/8/Remarks_DataCard1/Properties/DisplayName |  | Master_Asset |  |
| L1027 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/0/Form_Registration/Children/8/Remarks_DataCard1/Properties/MaxLength |  | Master_Asset |  |
| L1085 /Screens/ALM-Registration/Children/0/MainContainer_Registration/Children/1/BottomContainer_Registration/Children/1/FormContainer_Registration/Children/1/ButtonAddtoGallery_Registration/Properties/OnSelect | Collect, LookUp, Patch, UpdateContext, Notify | Master_Category, Master_Asset_Type |  |
| L1159 /Screens/ALM-Registration/Children/2/ButtonClose_Registration/Properties/OnSelect | UpdateContext, Navigate |  |  |
| L1203 /Screens/ALM-Registration/Children/3/ConfirmationContainer_Registration/Children/1/ButtonConfirmationNo_Registration/Properties/OnSelect | UpdateContext |  |  |
| L1213 /Screens/ALM-Registration/Children/3/ConfirmationContainer_Registration/Children/2/ButtonConfirmationYes_Registration/Properties/OnSelect | Remove, UpdateContext |  |  |
| L1235 /Screens/ALM-Registration/Children/4/Registration_AttachmentControl/Properties/OnAddFile | UpdateContext, ClearCollect, LookUp | Master_Asset_Type | Bulk_Registration |
| L1338 /Screens/ALM-Registration/Children/5/Container_Data_Confirm/Children/1/ButtonClose_Registration_1/Properties/OnSelect | UpdateContext |  |  |
| L1353 /Screens/ALM-Registration/Children/5/Container_Data_Confirm/Children/2/ButtonClose_Registration_2/Properties/OnSelect | Filter, LookUp, UpdateContext, Notify, Patch, Navigate | Master_Asset, Master_Employee, AuditLog |  |
| L1729 /Screens/ALM-Registration/Children/5/Container_Data_Confirm/Children/3/AssetDataContainer_10/Children/1/ColumnValueMasterAsset_10/Children/2/Column_Value_AsssetDate_MasterAsset_100/Properties/Text | LookUp | Master_Organization |  |
| L1771 /Screens/ALM-Registration/Children/5/Container_Data_Confirm/Children/3/AssetDataContainer_10/Children/1/ColumnValueMasterAsset_10/Children/5/Column_Value_AsssetDate_MasterAsset_103/Properties/Text | LookUp | Master_Employee |  |
| L1818 /Screens/ALM-Registration/Children/5/Container_Data_Confirm/Children/3/AssetDataContainer_10/Children/1/ColumnValueMasterAsset_10/Children/9/Column_Value_AsssetDate_MasterAsset_104/Properties/Text | LookUp | Master_Employee |  |
| L1860 /Screens/ALM-Registration/Children/5/Container_Data_Confirm/Children/3/AssetDataContainer_10/Children/1/ColumnValueMasterAsset_10/Children/12/Column_Value_AsssetDate_MasterAsset_107/Properties/Text | LookUp | Master_Location |  |
| L1874 /Screens/ALM-Registration/Children/5/Container_Data_Confirm/Children/3/AssetDataContainer_10/Children/1/ColumnValueMasterAsset_10/Children/13/Column_Value_AsssetDate_MasterAsset_108/Properties/Text | LookUp | Master_Asset_Type |  |
| L1888 /Screens/ALM-Registration/Children/5/Container_Data_Confirm/Children/3/AssetDataContainer_10/Children/1/ColumnValueMasterAsset_10/Children/14/Column_Value_AsssetDate_MasterAsset_109/Properties/Text | LookUp | Master_Category, Master_Asset_Type |  |
| L1944 /Screens/ALM-Registration/Children/5/Container_Data_Confirm/Children/3/AssetDataContainer_10/Children/1/ColumnValueMasterAsset_10/Children/18/Column_Value_AsssetDate_MasterAsset_113/Properties/Text | LookUp | Master_Function |  |
| L2029 /Screens/ALM-Registration/Children/7/Container3/Children/0/Form2/Properties/DataSource |  | Master_Asset |  |
| L2044 /Screens/ALM-Registration/Children/7/Container3/Children/0/Form2/Children/0/Organization_ID_DataCard5/Properties/DisplayName |  | Master_Asset |  |
| L2045 /Screens/ALM-Registration/Children/7/Container3/Children/0/Form2/Children/0/Organization_ID_DataCard5/Properties/MaxLength |  | Master_Asset |  |
| L2097 /Screens/ALM-Registration/Children/7/Container3/Children/0/Form2/Children/0/Organization_ID_DataCard5/Children/3/DropdownCanvas14/Properties/Items |  | Master_Organization |  |
| L2118 /Screens/ALM-Registration/Children/7/Container3/Children/0/Form2/Children/1/Function_ID_DataCard5/Properties/DisplayName |  | Master_Asset |  |
| L2119 /Screens/ALM-Registration/Children/7/Container3/Children/0/Form2/Children/1/Function_ID_DataCard5/Properties/MaxLength |  | Master_Asset |  |
| L2171 /Screens/ALM-Registration/Children/7/Container3/Children/0/Form2/Children/1/Function_ID_DataCard5/Children/3/DropdownCanvas15/Properties/Items | Filter | Master_Function |  |
| L2192 /Screens/ALM-Registration/Children/7/Container3/Children/0/Form2/Children/2/Arrival_Date_DataCard4/Properties/DisplayName |  | Master_Asset |  |
| L2264 /Screens/ALM-Registration/Children/7/Container3/Children/1/ButtonClose_Registration_5/Properties/OnSelect | Navigate |  |  |
| L2280 /Screens/ALM-Registration/Children/7/Container3/Children/2/ButtonClose_Registration_6/Properties/OnSelect | ClearCollect, UpdateContext |  |  |
