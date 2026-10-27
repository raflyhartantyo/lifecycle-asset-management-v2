# ALM - Master Location - New

Reference baseline; target V2 replacement is pending.

Source: `../screens/ALM - Master Location - New.pa.yaml`.

Data references: AuditLog, Master_Employee, Master_Location.
Flow calls: none found by static formula scan.
Navigation destinations: ALM - Master Location.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Inspect the destination Studio-generated YAML shape before pasting. A full Screens: export wrapper is not assumed to be a paste-ready control snippet. Use supported screen/control copy-and-paste where compatible, or apply the supplied property formulas to the matching screen/control. Capture any rejected YAML and schema error before requesting an adapted delivery.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
| L13 /Screens/ALM - Master Location - New/Properties/OnVisible | UpdateContext |  |  |
| L113 /Screens/ALM - Master Location - New/Children/0/MainContainer_CategoryMaster_New_2/Children/1/BottomContainer_CategoryMaster_New_2/Children/0/SidebarContainer_CategoryMaster_New_2/Children/0/DataGallery_CategoryMaster_New_2/Properties/OnSelect | UpdateContext |  |  |
| L191 /Screens/ALM - Master Location - New/Children/0/MainContainer_CategoryMaster_New_2/Children/1/BottomContainer_CategoryMaster_New_2/Children/0/SidebarContainer_CategoryMaster_New_2/Children/0/DataGallery_CategoryMaster_New_2/Children/4/IconDelete_CategoryMaster_New_2/Properties/OnSelect | UpdateContext |  |  |
| L229 /Screens/ALM - Master Location - New/Children/0/MainContainer_CategoryMaster_New_2/Children/1/BottomContainer_CategoryMaster_New_2/Children/0/SidebarContainer_CategoryMaster_New_2/Children/1/ButtonSave_CategoryMaster_New_2/Properties/OnSelect | UpdateContext, Patch, LookUp, Notify, Navigate | Master_Location, Master_Employee, AuditLog |  |
| L362 /Screens/ALM - Master Location - New/Children/0/MainContainer_CategoryMaster_New_2/Children/1/BottomContainer_CategoryMaster_New_2/Children/1/FormContainer_CategoryMaster_New_2/Children/0/Form_CategoryMaster_New_2/Properties/DataSource |  | Master_Location |  |
| L375 /Screens/ALM - Master Location - New/Children/0/MainContainer_CategoryMaster_New_2/Children/1/BottomContainer_CategoryMaster_New_2/Children/1/FormContainer_CategoryMaster_New_2/Children/0/Form_CategoryMaster_New_2/Children/0/Location_Name_DataCard3/Properties/DisplayName |  | Master_Location |  |
| L376 /Screens/ALM - Master Location - New/Children/0/MainContainer_CategoryMaster_New_2/Children/1/BottomContainer_CategoryMaster_New_2/Children/1/FormContainer_CategoryMaster_New_2/Children/0/Form_CategoryMaster_New_2/Children/0/Location_Name_DataCard3/Properties/MaxLength |  | Master_Location |  |
| L454 /Screens/ALM - Master Location - New/Children/0/MainContainer_CategoryMaster_New_2/Children/1/BottomContainer_CategoryMaster_New_2/Children/1/FormContainer_CategoryMaster_New_2/Children/0/Form_CategoryMaster_New_2/Children/1/Location_Address_DataCard3/Properties/DisplayName |  | Master_Location |  |
| L455 /Screens/ALM - Master Location - New/Children/0/MainContainer_CategoryMaster_New_2/Children/1/BottomContainer_CategoryMaster_New_2/Children/1/FormContainer_CategoryMaster_New_2/Children/0/Form_CategoryMaster_New_2/Children/1/Location_Address_DataCard3/Properties/MaxLength |  | Master_Location |  |
| L529 /Screens/ALM - Master Location - New/Children/0/MainContainer_CategoryMaster_New_2/Children/1/BottomContainer_CategoryMaster_New_2/Children/1/FormContainer_CategoryMaster_New_2/Children/0/Form_CategoryMaster_New_2/Children/2/Location_Contact_DataCard3/Properties/DisplayName |  | Master_Location |  |
| L530 /Screens/ALM - Master Location - New/Children/0/MainContainer_CategoryMaster_New_2/Children/1/BottomContainer_CategoryMaster_New_2/Children/1/FormContainer_CategoryMaster_New_2/Children/0/Form_CategoryMaster_New_2/Children/2/Location_Contact_DataCard3/Properties/MaxLength |  | Master_Location |  |
| L604 /Screens/ALM - Master Location - New/Children/0/MainContainer_CategoryMaster_New_2/Children/1/BottomContainer_CategoryMaster_New_2/Children/1/FormContainer_CategoryMaster_New_2/Children/1/ButtonAddtoGallery_CategoryMaster_New_2/Properties/OnSelect | Collect, Patch, UpdateContext, Notify |  |  |
| L646 /Screens/ALM - Master Location - New/Children/1/ButtonClose_CategoryMaster_New_2/Properties/OnSelect | UpdateContext, Navigate |  |  |
| L688 /Screens/ALM - Master Location - New/Children/2/ConfirmationContainer_CategoryMaster_New_2/Children/1/ButtonConfirmationNo_CategoryMaster_New_2/Properties/OnSelect | UpdateContext |  |  |
| L698 /Screens/ALM - Master Location - New/Children/2/ConfirmationContainer_CategoryMaster_New_2/Children/2/ButtonConfirmationYes_CategoryMaster_New_2/Properties/OnSelect | Remove, UpdateContext |  |  |
