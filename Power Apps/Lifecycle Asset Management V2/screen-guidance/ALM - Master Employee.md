# ALM - Master Employee

Reference baseline; target V2 replacement is pending.

Source: `../screens/ALM - Master Employee.pa.yaml`.

Data references: AuditLog, Master_Employee.
Flow calls: none found by static formula scan.
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
| L332 /Screens/ALM - Master Employee/Children/1/AssetDataContainer_5/Children/1/ColumnValueMasterAsset_5/Properties/Items | IfError, Filter |  |  |
| L706 /Screens/ALM - Master Employee/Children/2/ButtonNew_CategoryMaster_4/Properties/OnSelect | UpdateContext |  |  |
| L719 /Screens/ALM - Master Employee/Children/3/Icon15_3/Properties/OnSelect | Navigate |  |  |
| L729 /Screens/ALM - Master Employee/Children/4/ButtonNew_CategoryMaster_5/Properties/OnSelect | Refresh, ClearCollect, Filter | Master_Employee |  |
| L808 /Screens/ALM - Master Employee/Children/7/Container1_4/Children/0/Form1_5/Properties/DataSource |  | Master_Employee |  |
| L824 /Screens/ALM - Master Employee/Children/7/Container1_4/Children/0/Form1_5/Children/0/MyID_DataCard1/Properties/DisplayName |  | Master_Employee |  |
| L825 /Screens/ALM - Master Employee/Children/7/Container1_4/Children/0/Form1_5/Children/0/MyID_DataCard1/Properties/MaxLength |  | Master_Employee |  |
| L827 /Screens/ALM - Master Employee/Children/7/Container1_4/Children/0/Form1_5/Children/0/MyID_DataCard1/Properties/Update | LookUp |  |  |
| L875 /Screens/ALM - Master Employee/Children/7/Container1_4/Children/0/Form1_5/Children/0/MyID_DataCard1/Children/2/ErrorMessage38/Properties/Text | LookUp |  |  |
| L905 /Screens/ALM - Master Employee/Children/7/Container1_4/Children/0/Form1_5/Children/1/Email_DataCard2/Properties/DisplayName |  | Master_Employee |  |
| L906 /Screens/ALM - Master Employee/Children/7/Container1_4/Children/0/Form1_5/Children/1/Email_DataCard2/Properties/MaxLength |  | Master_Employee |  |
| L985 /Screens/ALM - Master Employee/Children/7/Container1_4/Children/0/Form1_5/Children/2/Display_Name_DataCard1/Properties/DisplayName |  | Master_Employee |  |
| L986 /Screens/ALM - Master Employee/Children/7/Container1_4/Children/0/Form1_5/Children/2/Display_Name_DataCard1/Properties/MaxLength |  | Master_Employee |  |
| L1062 /Screens/ALM - Master Employee/Children/7/Container1_4/Children/0/Form1_5/Children/3/Employee_Type_DataCard4/Properties/DisplayName |  | Master_Employee |  |
| L1063 /Screens/ALM - Master Employee/Children/7/Container1_4/Children/0/Form1_5/Children/3/Employee_Type_DataCard4/Properties/MaxLength |  | Master_Employee |  |
| L1130 /Screens/ALM - Master Employee/Children/7/Container1_4/Children/0/Form1_5/Children/4/Department_DataCard2/Properties/DisplayName |  | Master_Employee |  |
| L1131 /Screens/ALM - Master Employee/Children/7/Container1_4/Children/0/Form1_5/Children/4/Department_DataCard2/Properties/MaxLength |  | Master_Employee |  |
| L1190 /Screens/ALM - Master Employee/Children/7/Container1_4/Children/0/Form1_5/Children/5/Manager_DataCard2/Properties/DisplayName |  | Master_Employee |  |
| L1191 /Screens/ALM - Master Employee/Children/7/Container1_4/Children/0/Form1_5/Children/5/Manager_DataCard2/Properties/MaxLength |  | Master_Employee |  |
| L1251 /Screens/ALM - Master Employee/Children/7/Container1_4/Children/1/ButtonClose_Registration_19/Properties/OnSelect | UpdateContext, Patch, LookUp, Notify | Master_Employee, AuditLog |  |
| L1266 /Screens/ALM - Master Employee/Children/7/Container1_4/Children/2/ButtonClose_Registration_20/Properties/OnSelect | UpdateContext |  |  |
