# ALM-Asset Master

Reference baseline; target V2 replacement is pending.

Source: `../screens/ALM-Asset Master.pa.yaml`.

Data references: Acces_Matrix, Master_Asset, Master_Asset_Type, Master_Category, Master_Employee, Master_Location.
Flow calls: ExportData.
Navigation destinations: 3_HomePageMasterData.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Inspect the destination Studio-generated YAML shape before pasting. A full Screens: export wrapper is not assumed to be a paste-ready control snippet. Use supported screen/control copy-and-paste where compatible, or apply the supplied property formulas to the matching screen/control. Capture any rejected YAML and schema error before requesting an adapted delivery.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
| L14 /Screens/ALM-Asset Master/Properties/OnHidden | UpdateContext |  |  |
| L42 /Screens/ALM-Asset Master/Children/0/HeaderContainer_AssetMaster/Children/1/ButtonNew_CategoryMaster_12/Properties/OnSelect | ClearCollect, Filter, LookUp, UpdateContext | Master_Category, Master_Location, Master_Asset, Master_Employee, Master_Asset_Type |  |
| L146 /Screens/ALM-Asset Master/Children/0/HeaderContainer_AssetMaster/Children/2/Icon15_7/Properties/OnSelect | Navigate, UpdateContext |  |  |
| L179 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Properties/DataSource |  | Master_Asset |  |
| L182 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Properties/Item | LookUp | Master_Asset |  |
| L196 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/0/Arrival_Date_DataCard3/Properties/DisplayName |  | Master_Asset |  |
| L255 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/1/Asset_Status_DataCard3/Properties/DisplayName |  | Master_Asset |  |
| L256 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/1/Asset_Status_DataCard3/Properties/MaxLength |  | Master_Asset |  |
| L315 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/2/Lifespan_DataCard1/Properties/DisplayName |  | Master_Asset |  |
| L374 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/3/Accounting_Asset_Code_DataCard5/Properties/DisplayName |  | Master_Asset |  |
| L375 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/3/Accounting_Asset_Code_DataCard5/Properties/MaxLength |  | Master_Asset |  |
| L434 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/4/Asset_Condition_DataCard3/Properties/DisplayName |  | Master_Asset |  |
| L435 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/4/Asset_Condition_DataCard3/Properties/MaxLength |  | Master_Asset |  |
| L494 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/5/Environment_DataCard1/Properties/DisplayName |  | Master_Asset |  |
| L495 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/5/Environment_DataCard1/Properties/MaxLength |  | Master_Asset |  |
| L554 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/6/Name_DataCard1/Properties/DisplayName |  | Master_Asset |  |
| L592 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/7/MYID_Asset_Owner_DataCard4/Properties/DisplayName |  | Master_Asset |  |
| L593 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/7/MYID_Asset_Owner_DataCard4/Properties/MaxLength |  | Master_Asset |  |
| L652 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/8/Remarks_DataCard4/Properties/DisplayName |  | Master_Asset |  |
| L653 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/8/Remarks_DataCard4/Properties/MaxLength |  | Master_Asset |  |
| L712 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/9/Asset_Name_DataCard5/Properties/DisplayName |  | Master_Asset |  |
| L713 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/9/Asset_Name_DataCard5/Properties/MaxLength |  | Master_Asset |  |
| L772 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/10/MYID_Business_Owner_DataCard2/Properties/DisplayName |  | Master_Asset |  |
| L773 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/10/MYID_Business_Owner_DataCard2/Properties/MaxLength |  | Master_Asset |  |
| L832 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/11/Supplier_DataCard1/Properties/DisplayName |  | Master_Asset |  |
| L833 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/11/Supplier_DataCard1/Properties/MaxLength |  | Master_Asset |  |
| L892 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/12/Category_ID_DataCard5/Properties/DisplayName |  | Master_Asset |  |
| L893 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/12/Category_ID_DataCard5/Properties/MaxLength |  | Master_Asset |  |
| L952 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/13/EndOfSupport_DataCard1/Properties/DisplayName |  | Master_Asset |  |
| L1011 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/14/Sub_Merk_DataCard1/Properties/DisplayName |  | Master_Asset |  |
| L1012 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/14/Sub_Merk_DataCard1/Properties/MaxLength |  | Master_Asset |  |
| L1071 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/15/Asset_Type_ID_DataCard5/Properties/DisplayName |  | Master_Asset |  |
| L1072 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/15/Asset_Type_ID_DataCard5/Properties/MaxLength |  | Master_Asset |  |
| L1131 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/16/LicenseEndDate_DataCard1/Properties/DisplayName |  | Master_Asset |  |
| L1190 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/17/Purchasing_Price_DataCard4/Properties/DisplayName |  | Master_Asset |  |
| L1249 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/18/EndOfLife_DataCard1/Properties/DisplayName |  | Master_Asset |  |
| L1308 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/19/Serial_Number_DataCard2/Properties/DisplayName |  | Master_Asset |  |
| L1309 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/19/Serial_Number_DataCard2/Properties/MaxLength |  | Master_Asset |  |
| L1368 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/20/HostName_DataCard2/Properties/DisplayName |  | Master_Asset |  |
| L1369 /Screens/ALM-Asset Master/Children/2/Container1/Children/0/Form1/Children/20/HostName_DataCard2/Properties/MaxLength |  | Master_Asset |  |
| L1425 /Screens/ALM-Asset Master/Children/2/Container1/Children/1/Button2/Properties/OnSelect | UpdateContext |  |  |
| L1436 /Screens/ALM-Asset Master/Children/2/Container1/Children/2/Button2_1/Properties/OnSelect | SubmitForm, UpdateContext, Refresh, ClearCollect, LookUp, Filter, Notify | Master_Category, Master_Location, Master_Asset, Master_Asset_Type |  |
| L1945 /Screens/ALM-Asset Master/Children/4/AssetDataContainer/Children/1/ColumnValueMasterAsset/Properties/Items | Filter |  |  |
| L2056 /Screens/ALM-Asset Master/Children/4/AssetDataContainer/Children/1/ColumnValueMasterAsset/Children/5/NextArrow2/Properties/OnSelect | UpdateContext |  |  |
| L2317 /Screens/ALM-Asset Master/Children/4/AssetDataContainer/Children/1/ColumnValueMasterAsset/Children/23/NextArrow2_15/Properties/OnSelect | UpdateContext |  |  |
| L2325 /Screens/ALM-Asset Master/Children/4/AssetDataContainer/Children/1/ColumnValueMasterAsset/Children/23/NextArrow2_15/Properties/Visible | LookUp | Acces_Matrix, Master_Employee |  |
| L2426 /Screens/ALM-Asset Master/Children/5/IconSearch_BuildingMaster_Edit_1/Properties/OnSelect | UpdateContext |  |  |
| L2439 /Screens/ALM-Asset Master/Children/6/Icon11/Properties/OnSelect | Set, UpdateContext, Notify |  | ExportData |
| L3029 /Screens/ALM-Asset Master/Children/9/Container9_2/Children/2/Container11_7/Children/7/TextInput5/Properties/OnChange | UpdateContext |  |  |
| L3056 /Screens/ALM-Asset Master/Children/9/Container9_2/Children/2/Container11_7/Children/9/TextInput5_1/Properties/OnChange | UpdateContext |  |  |
| L3073 /Screens/ALM-Asset Master/Children/10/ButtonCanvas2_17/Properties/OnSelect | UpdateContext |  |  |
