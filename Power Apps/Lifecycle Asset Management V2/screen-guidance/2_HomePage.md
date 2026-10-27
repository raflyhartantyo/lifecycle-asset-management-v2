# 2_HomePage

Reference baseline; target V2 replacement is pending.

Source: `../screens/2_HomePage.pa.yaml`.

Data references: Acces_Matrix, Master_Employee.
Flow calls: none found by static formula scan.
Navigation destinations: 3_HomePageMasterData, ALM-AccReconcile, ALM-Dashboard, ALM-DisposeRequest, Home Page_Asset_Inventory, Home Page_Stock_Opname, Home Page_Transaction.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Inspect the destination Studio-generated YAML shape before pasting. A full Screens: export wrapper is not assumed to be a paste-ready control snippet. Use supported screen/control copy-and-paste where compatible, or apply the supplied property formulas to the matching screen/control. Capture any rejected YAML and schema error before requesting an adapted delivery.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
| L94 /Screens/2_HomePage/Children/0/Ctr_HP/Children/1/Ctr_HP_2/Children/0/Ctr_HP_3/Properties/Visible | LookUp | Acces_Matrix, Master_Employee |  |
| L132 /Screens/2_HomePage/Children/0/Ctr_HP/Children/1/Ctr_HP_2/Children/0/Ctr_HP_3/Children/0/ImgCtr_HP3/Children/0/Icon_MasterData_HP3/Properties/OnSelect | Navigate |  |  |
| L161 /Screens/2_HomePage/Children/0/Ctr_HP/Children/1/Ctr_HP_2/Children/0/Ctr_HP_3/Children/1/TtlCtr_HP3/Children/0/Txt_TitleMasterData_HP3/Properties/OnSelect | Navigate |  |  |
| L190 /Screens/2_HomePage/Children/0/Ctr_HP/Children/1/Ctr_HP_2/Children/1/Ctr_HP_4/Properties/Visible | LookUp | Acces_Matrix, Master_Employee |  |
| L230 /Screens/2_HomePage/Children/0/Ctr_HP/Children/1/Ctr_HP_2/Children/1/Ctr_HP_4/Children/0/ImgCtr_HP4/Children/0/Icon_Transaction_HP4/Properties/OnSelect | Navigate |  |  |
| L259 /Screens/2_HomePage/Children/0/Ctr_HP/Children/1/Ctr_HP_2/Children/1/Ctr_HP_4/Children/1/TtlCtr_HP4/Children/0/Txt_TitleTransaction_HP4/Properties/OnSelect | Navigate |  |  |
| L320 /Screens/2_HomePage/Children/0/Ctr_HP/Children/1/Ctr_HP_2/Children/2/Ctr_HP_5/Children/0/ImgCtr_HP5/Children/0/Icon_Dashboard_HP5/Properties/OnSelect | Navigate |  |  |
| L349 /Screens/2_HomePage/Children/0/Ctr_HP/Children/1/Ctr_HP_2/Children/2/Ctr_HP_5/Children/1/TtlCtr_HP5/Children/0/Txt_TitleDashboard_HP5/Properties/OnSelect | Navigate |  |  |
| L378 /Screens/2_HomePage/Children/0/Ctr_HP/Children/1/Ctr_HP_2/Children/3/Ctr_HP_6/Properties/Visible | LookUp | Acces_Matrix, Master_Employee |  |
| L416 /Screens/2_HomePage/Children/0/Ctr_HP/Children/1/Ctr_HP_2/Children/3/Ctr_HP_6/Children/0/ImgCtr_HP6/Children/0/Icon_AccRecon_HP6/Properties/OnSelect | Navigate |  |  |
| L445 /Screens/2_HomePage/Children/0/Ctr_HP/Children/1/Ctr_HP_2/Children/3/Ctr_HP_6/Children/1/TtlCtr_HP6/Children/0/Txt_TitleAccRecon_HP6/Properties/OnSelect | Navigate |  |  |
| L507 /Screens/2_HomePage/Children/0/Ctr_HP/Children/1/Ctr_HP_2/Children/4/Ctr_HP_7/Children/0/ImgCtr_HP7/Children/0/Icon_DispReq_HP7/Properties/OnSelect | Navigate |  |  |
| L536 /Screens/2_HomePage/Children/0/Ctr_HP/Children/1/Ctr_HP_2/Children/4/Ctr_HP_7/Children/1/TtlCtr_HP7/Children/0/Txt_TitleDispRec_HP7/Properties/OnSelect | Navigate |  |  |
| L565 /Screens/2_HomePage/Children/0/Ctr_HP/Children/1/Ctr_HP_2/Children/5/Ctr_HP_8/Properties/Visible | LookUp | Acces_Matrix, Master_Employee |  |
| L615 /Screens/2_HomePage/Children/0/Ctr_HP/Children/1/Ctr_HP_2/Children/5/Ctr_HP_8/Children/0/ImgCtr_HP8/Children/0/Icon_SO_HP8/Properties/OnSelect | Navigate |  |  |
| L644 /Screens/2_HomePage/Children/0/Ctr_HP/Children/1/Ctr_HP_2/Children/5/Ctr_HP_8/Children/1/TtlCtr_HP8/Children/0/Txt_TitleSO_HP8/Properties/OnSelect | Navigate |  |  |
| L664 /Screens/2_HomePage/Children/1/Icon15_17/Properties/OnSelect | Navigate |  |  |
| L665 /Screens/2_HomePage/Children/1/Icon15_17/Properties/Visible | LookUp | Acces_Matrix, Master_Employee |  |
