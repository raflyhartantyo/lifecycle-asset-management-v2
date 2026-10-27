# ALM-Master Asset Type-New

Reference baseline; target V2 replacement is pending.

Source: `../screens/ALM-Master Asset Type-New.pa.yaml`.

Data references: AuditLog, Master_Asset_Type, Master_Category, Master_Employee, Master_Function.
Flow calls: none found by static formula scan.
Navigation destinations: ALM - Master Asset Type.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Inspect the destination Studio-generated YAML shape before pasting. A full Screens: export wrapper is not assumed to be a paste-ready control snippet. Use supported screen/control copy-and-paste where compatible, or apply the supplied property formulas to the matching screen/control. Capture any rejected YAML and schema error before requesting an adapted delivery.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
| L13 /Screens/ALM-Master Asset Type-New/Properties/OnVisible | UpdateContext |  |  |
| L113 /Screens/ALM-Master Asset Type-New/Children/0/MainContainer_CategoryMaster_New/Children/1/BottomContainer_CategoryMaster_New/Children/0/SidebarContainer_CategoryMaster_New/Children/0/DataGallery_CategoryMaster_New/Properties/OnSelect | UpdateContext |  |  |
| L180 /Screens/ALM-Master Asset Type-New/Children/0/MainContainer_CategoryMaster_New/Children/1/BottomContainer_CategoryMaster_New/Children/0/SidebarContainer_CategoryMaster_New/Children/0/DataGallery_CategoryMaster_New/Children/3/TextGroupCategory_CategoryMaster_New/Properties/Text | LookUp | Master_Category |  |
| L192 /Screens/ALM-Master Asset Type-New/Children/0/MainContainer_CategoryMaster_New/Children/1/BottomContainer_CategoryMaster_New/Children/0/SidebarContainer_CategoryMaster_New/Children/0/DataGallery_CategoryMaster_New/Children/4/IconDelete_CategoryMaster_New/Properties/OnSelect | UpdateContext |  |  |
| L219 /Screens/ALM-Master Asset Type-New/Children/0/MainContainer_CategoryMaster_New/Children/1/BottomContainer_CategoryMaster_New/Children/0/SidebarContainer_CategoryMaster_New/Children/0/DataGallery_CategoryMaster_New/Children/6/TextDepartment_CategoryMaster_New/Properties/Text | LookUp | Master_Function |  |
| L230 /Screens/ALM-Master Asset Type-New/Children/0/MainContainer_CategoryMaster_New/Children/1/BottomContainer_CategoryMaster_New/Children/0/SidebarContainer_CategoryMaster_New/Children/1/ButtonSave_CategoryMaster_New/Properties/OnSelect | UpdateContext, Patch, LookUp, Notify, Navigate | Master_Employee, Master_Asset_Type, AuditLog |  |
| L256 /Screens/ALM-Master Asset Type-New/Children/0/MainContainer_CategoryMaster_New/Children/1/BottomContainer_CategoryMaster_New/Children/1/FormContainer_CategoryMaster_New/Children/0/Form_CategoryMaster_New/Properties/DataSource |  | Master_Asset_Type |  |
| L269 /Screens/ALM-Master Asset Type-New/Children/0/MainContainer_CategoryMaster_New/Children/1/BottomContainer_CategoryMaster_New/Children/1/FormContainer_CategoryMaster_New/Children/0/Form_CategoryMaster_New/Children/0/Asset_Type_Name_DataCard1/Properties/DisplayName |  | Master_Asset_Type |  |
| L270 /Screens/ALM-Master Asset Type-New/Children/0/MainContainer_CategoryMaster_New/Children/1/BottomContainer_CategoryMaster_New/Children/1/FormContainer_CategoryMaster_New/Children/0/Form_CategoryMaster_New/Children/0/Asset_Type_Name_DataCard1/Properties/MaxLength |  | Master_Asset_Type |  |
| L345 /Screens/ALM-Master Asset Type-New/Children/0/MainContainer_CategoryMaster_New/Children/1/BottomContainer_CategoryMaster_New/Children/1/FormContainer_CategoryMaster_New/Children/0/Form_CategoryMaster_New/Children/1/Function_ID_DataCard1/Properties/DisplayName |  | Master_Asset_Type |  |
| L346 /Screens/ALM-Master Asset Type-New/Children/0/MainContainer_CategoryMaster_New/Children/1/BottomContainer_CategoryMaster_New/Children/1/FormContainer_CategoryMaster_New/Children/0/Form_CategoryMaster_New/Children/1/Function_ID_DataCard1/Properties/MaxLength |  | Master_Asset_Type |  |
| L399 /Screens/ALM-Master Asset Type-New/Children/0/MainContainer_CategoryMaster_New/Children/1/BottomContainer_CategoryMaster_New/Children/1/FormContainer_CategoryMaster_New/Children/0/Form_CategoryMaster_New/Children/1/Function_ID_DataCard1/Children/3/DropdownCanvas1/Properties/DefaultSelectedItems | LookUp | Master_Function |  |
| L400 /Screens/ALM-Master Asset Type-New/Children/0/MainContainer_CategoryMaster_New/Children/1/BottomContainer_CategoryMaster_New/Children/1/FormContainer_CategoryMaster_New/Children/0/Form_CategoryMaster_New/Children/1/Function_ID_DataCard1/Children/3/DropdownCanvas1/Properties/Items |  | Master_Function |  |
| L421 /Screens/ALM-Master Asset Type-New/Children/0/MainContainer_CategoryMaster_New/Children/1/BottomContainer_CategoryMaster_New/Children/1/FormContainer_CategoryMaster_New/Children/0/Form_CategoryMaster_New/Children/2/Category_ID_DataCard2/Properties/DisplayName |  | Master_Asset_Type |  |
| L422 /Screens/ALM-Master Asset Type-New/Children/0/MainContainer_CategoryMaster_New/Children/1/BottomContainer_CategoryMaster_New/Children/1/FormContainer_CategoryMaster_New/Children/0/Form_CategoryMaster_New/Children/2/Category_ID_DataCard2/Properties/MaxLength |  | Master_Asset_Type |  |
| L475 /Screens/ALM-Master Asset Type-New/Children/0/MainContainer_CategoryMaster_New/Children/1/BottomContainer_CategoryMaster_New/Children/1/FormContainer_CategoryMaster_New/Children/0/Form_CategoryMaster_New/Children/2/Category_ID_DataCard2/Children/3/DropdownCanvas3/Properties/DefaultSelectedItems | LookUp | Master_Category |  |
| L476 /Screens/ALM-Master Asset Type-New/Children/0/MainContainer_CategoryMaster_New/Children/1/BottomContainer_CategoryMaster_New/Children/1/FormContainer_CategoryMaster_New/Children/0/Form_CategoryMaster_New/Children/2/Category_ID_DataCard2/Children/3/DropdownCanvas3/Properties/Items |  | Master_Category |  |
| L497 /Screens/ALM-Master Asset Type-New/Children/0/MainContainer_CategoryMaster_New/Children/1/BottomContainer_CategoryMaster_New/Children/1/FormContainer_CategoryMaster_New/Children/1/ButtonAddtoGallery_CategoryMaster_New/Properties/OnSelect | Collect, Patch, UpdateContext, Notify |  |  |
| L539 /Screens/ALM-Master Asset Type-New/Children/1/ButtonClose_CategoryMaster_New/Properties/OnSelect | UpdateContext, Navigate |  |  |
| L581 /Screens/ALM-Master Asset Type-New/Children/2/ConfirmationContainer_CategoryMaster_New/Children/1/ButtonConfirmationNo_CategoryMaster_New/Properties/OnSelect | UpdateContext |  |  |
| L591 /Screens/ALM-Master Asset Type-New/Children/2/ConfirmationContainer_CategoryMaster_New/Children/2/ButtonConfirmationYes_CategoryMaster_New/Properties/OnSelect | Remove, UpdateContext |  |  |
