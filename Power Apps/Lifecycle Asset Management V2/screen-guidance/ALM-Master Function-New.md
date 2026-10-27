# ALM-Master Function-New

Reference baseline; target V2 replacement is pending.

Source: `../screens/ALM-Master Function-New.pa.yaml`.

Data references: AuditLog, Master_Employee, Master_Function, Master_Organization.
Flow calls: none found by static formula scan.
Navigation destinations: ALM - Master Function.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Inspect the destination Studio-generated YAML shape before pasting. A full Screens: export wrapper is not assumed to be a paste-ready control snippet. Use supported screen/control copy-and-paste where compatible, or apply the supplied property formulas to the matching screen/control. Capture any rejected YAML and schema error before requesting an adapted delivery.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
| L13 /Screens/ALM-Master Function-New/Properties/OnVisible | UpdateContext |  |  |
| L113 /Screens/ALM-Master Function-New/Children/0/MainContainer_CategoryMaster_New_3/Children/1/BottomContainer_CategoryMaster_New_3/Children/0/SidebarContainer_CategoryMaster_New_3/Children/0/DataGallery_CategoryMaster_New_3/Properties/OnSelect | UpdateContext |  |  |
| L191 /Screens/ALM-Master Function-New/Children/0/MainContainer_CategoryMaster_New_3/Children/1/BottomContainer_CategoryMaster_New_3/Children/0/SidebarContainer_CategoryMaster_New_3/Children/0/DataGallery_CategoryMaster_New_3/Children/4/IconDelete_CategoryMaster_New_3/Properties/OnSelect | UpdateContext |  |  |
| L218 /Screens/ALM-Master Function-New/Children/0/MainContainer_CategoryMaster_New_3/Children/1/BottomContainer_CategoryMaster_New_3/Children/0/SidebarContainer_CategoryMaster_New_3/Children/0/DataGallery_CategoryMaster_New_3/Children/6/TextDepartment_CategoryMaster_New_3/Properties/Text | LookUp | Master_Organization |  |
| L229 /Screens/ALM-Master Function-New/Children/0/MainContainer_CategoryMaster_New_3/Children/1/BottomContainer_CategoryMaster_New_3/Children/0/SidebarContainer_CategoryMaster_New_3/Children/1/ButtonSave_CategoryMaster_New_3/Properties/OnSelect | UpdateContext, Patch, LookUp, Notify, Navigate | Master_Function, Master_Employee, AuditLog |  |
| L363 /Screens/ALM-Master Function-New/Children/0/MainContainer_CategoryMaster_New_3/Children/1/BottomContainer_CategoryMaster_New_3/Children/1/FormContainer_CategoryMaster_New_3/Children/0/Form_CategoryMaster_New_3/Properties/DataSource |  | Master_Function |  |
| L376 /Screens/ALM-Master Function-New/Children/0/MainContainer_CategoryMaster_New_3/Children/1/BottomContainer_CategoryMaster_New_3/Children/1/FormContainer_CategoryMaster_New_3/Children/0/Form_CategoryMaster_New_3/Children/0/Function_Name_DataCard2/Properties/DisplayName |  | Master_Function |  |
| L377 /Screens/ALM-Master Function-New/Children/0/MainContainer_CategoryMaster_New_3/Children/1/BottomContainer_CategoryMaster_New_3/Children/1/FormContainer_CategoryMaster_New_3/Children/0/Form_CategoryMaster_New_3/Children/0/Function_Name_DataCard2/Properties/MaxLength |  | Master_Function |  |
| L455 /Screens/ALM-Master Function-New/Children/0/MainContainer_CategoryMaster_New_3/Children/1/BottomContainer_CategoryMaster_New_3/Children/1/FormContainer_CategoryMaster_New_3/Children/0/Form_CategoryMaster_New_3/Children/1/Organization_ID_DataCard2/Properties/DisplayName |  | Master_Function |  |
| L456 /Screens/ALM-Master Function-New/Children/0/MainContainer_CategoryMaster_New_3/Children/1/BottomContainer_CategoryMaster_New_3/Children/1/FormContainer_CategoryMaster_New_3/Children/0/Form_CategoryMaster_New_3/Children/1/Organization_ID_DataCard2/Properties/MaxLength |  | Master_Function |  |
| L506 /Screens/ALM-Master Function-New/Children/0/MainContainer_CategoryMaster_New_3/Children/1/BottomContainer_CategoryMaster_New_3/Children/1/FormContainer_CategoryMaster_New_3/Children/0/Form_CategoryMaster_New_3/Children/1/Organization_ID_DataCard2/Children/3/DropdownCanvas7/Properties/DefaultSelectedItems | LookUp | Master_Organization |  |
| L507 /Screens/ALM-Master Function-New/Children/0/MainContainer_CategoryMaster_New_3/Children/1/BottomContainer_CategoryMaster_New_3/Children/1/FormContainer_CategoryMaster_New_3/Children/0/Form_CategoryMaster_New_3/Children/1/Organization_ID_DataCard2/Children/3/DropdownCanvas7/Properties/Items |  | Master_Organization |  |
| L528 /Screens/ALM-Master Function-New/Children/0/MainContainer_CategoryMaster_New_3/Children/1/BottomContainer_CategoryMaster_New_3/Children/1/FormContainer_CategoryMaster_New_3/Children/1/ButtonAddtoGallery_CategoryMaster_New_3/Properties/OnSelect | Collect, Patch, UpdateContext, Notify |  |  |
| L568 /Screens/ALM-Master Function-New/Children/1/ButtonClose_CategoryMaster_New_3/Properties/OnSelect | UpdateContext, Navigate |  |  |
| L610 /Screens/ALM-Master Function-New/Children/2/ConfirmationContainer_CategoryMaster_New_3/Children/1/ButtonConfirmationNo_CategoryMaster_New_3/Properties/OnSelect | UpdateContext |  |  |
| L620 /Screens/ALM-Master Function-New/Children/2/ConfirmationContainer_CategoryMaster_New_3/Children/2/ButtonConfirmationYes_CategoryMaster_New_3/Properties/OnSelect | Remove, UpdateContext |  |  |
