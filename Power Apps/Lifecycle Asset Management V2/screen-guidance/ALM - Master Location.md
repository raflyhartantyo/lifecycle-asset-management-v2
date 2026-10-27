# ALM - Master Location

Reference baseline; target V2 replacement is pending.

Source: `../screens/ALM - Master Location.pa.yaml`.

Data references: Acces_Matrix, AuditLog, Master_Employee, Master_Location.
Flow calls: none found by static formula scan.
Navigation destinations: 3_HomePageMasterData, ALM - Master Location - New.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Inspect the destination Studio-generated YAML shape before pasting. A full Screens: export wrapper is not assumed to be a paste-ready control snippet. Use supported screen/control copy-and-paste where compatible, or apply the supplied property formulas to the matching screen/control. Capture any rejected YAML and schema error before requesting an adapted delivery.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
| L31 /Screens/ALM - Master Location/Children/1/ButtonNew_CategoryMaster_6/Properties/OnSelect | Navigate |  |  |
| L242 /Screens/ALM - Master Location/Children/2/AssetDataContainer_6/Children/1/ColumnValueMasterAsset_6/Children/4/NextArrow2_5/Properties/OnSelect | UpdateContext |  |  |
| L250 /Screens/ALM - Master Location/Children/2/AssetDataContainer_6/Children/1/ColumnValueMasterAsset_6/Children/4/NextArrow2_5/Properties/Visible | LookUp | Acces_Matrix, Master_Employee |  |
| L323 /Screens/ALM - Master Location/Children/3/Icon15_4/Properties/OnSelect | Navigate |  |  |
| L333 /Screens/ALM - Master Location/Children/4/ButtonNew_CategoryMaster_7/Properties/OnSelect | Refresh, ClearCollect | Master_Location |  |
| L390 /Screens/ALM - Master Location/Children/7/Container1_5/Children/0/Form1_6/Properties/DataSource |  | Master_Location |  |
| L407 /Screens/ALM - Master Location/Children/7/Container1_5/Children/0/Form1_6/Children/0/Location_ID_DataCard1/Properties/DisplayName |  | Master_Location |  |
| L408 /Screens/ALM - Master Location/Children/7/Container1_5/Children/0/Form1_6/Children/0/Location_ID_DataCard1/Properties/MaxLength |  | Master_Location |  |
| L466 /Screens/ALM - Master Location/Children/7/Container1_5/Children/0/Form1_6/Children/1/Location_Name_DataCard1/Properties/DisplayName |  | Master_Location |  |
| L467 /Screens/ALM - Master Location/Children/7/Container1_5/Children/0/Form1_6/Children/1/Location_Name_DataCard1/Properties/MaxLength |  | Master_Location |  |
| L548 /Screens/ALM - Master Location/Children/7/Container1_5/Children/0/Form1_6/Children/2/Location_Address_DataCard1/Properties/DisplayName |  | Master_Location |  |
| L549 /Screens/ALM - Master Location/Children/7/Container1_5/Children/0/Form1_6/Children/2/Location_Address_DataCard1/Properties/MaxLength |  | Master_Location |  |
| L625 /Screens/ALM - Master Location/Children/7/Container1_5/Children/0/Form1_6/Children/3/Location_Contact_DataCard1/Properties/DisplayName |  | Master_Location |  |
| L626 /Screens/ALM - Master Location/Children/7/Container1_5/Children/0/Form1_6/Children/3/Location_Contact_DataCard1/Properties/MaxLength |  | Master_Location |  |
| L702 /Screens/ALM - Master Location/Children/7/Container1_5/Children/0/Form1_6/Children/4/PIC_DataCard2/Properties/DisplayName |  | Master_Location |  |
| L703 /Screens/ALM - Master Location/Children/7/Container1_5/Children/0/Form1_6/Children/4/PIC_DataCard2/Properties/MaxLength |  | Master_Location |  |
| L751 /Screens/ALM - Master Location/Children/7/Container1_5/Children/0/Form1_6/Children/4/PIC_DataCard2/Children/3/ComboboxCanvas1_1/Properties/DefaultSelectedItems | LookUp | Master_Employee |  |
| L754 /Screens/ALM - Master Location/Children/7/Container1_5/Children/0/Form1_6/Children/4/PIC_DataCard2/Children/3/ComboboxCanvas1_1/Properties/Items | Filter | Master_Employee |  |
| L773 /Screens/ALM - Master Location/Children/7/Container1_5/Children/1/ButtonClose_Registration_21/Properties/OnSelect | UpdateContext, Filter, Patch, LookUp, Notify, Refresh, ClearCollect | Master_Location, Master_Employee, AuditLog |  |
| L938 /Screens/ALM - Master Location/Children/7/Container1_5/Children/2/ButtonClose_Registration_22/Properties/OnSelect | UpdateContext |  |  |
